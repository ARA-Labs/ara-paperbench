"""Declarative method gate over the unchanged production RepositoryBackend."""
from __future__ import annotations

from collections.abc import Callable
from pathlib import Path

from aratest.generative import Perturbation
from aratest.persistence import canonical_json_bytes, sha256_digest
from aratest.research import AdapterBundle
from aratest.research.agents.repository import RepositoryBackend
from aratest.research.repository import (
    ContentAddressedStore,
    ExecutionProfile,
    RepositoryRunInput,
    ReservedOperation,
    load_execution_profile,
    read_workspace,
)

from .._adapter import validate_adapter_payload
from .._identity import canonical_bytes, digest_bytes
from .._protocols import ArtifactProtocol, InterventionRole

RequestMapper = Callable[[Perturbation], tuple[InterventionRole, dict[str, object]]]


def execution_environment(profile: ExecutionProfile) -> bytes:
    return canonical_bytes({'image_digest': profile.image_digest,
                            'command': profile.command.model_dump(mode='json'),
                            'limits': profile.limits.model_dump(mode='json')})


def verify_execution_binding(execution: ExecutionProfile, admission: ArtifactProtocol,
                             source: bytes, environment: bytes, *,
                             expected_profile: ExecutionProfile, expected_profile_digest: str) -> None:
    actual_source = canonical_bytes(execution.repository.model_dump(mode='json'))
    if actual_source != source or digest_bytes(source) != admission.source_digest:
        raise ValueError('actual execution source differs from admission source')
    if execution_environment(execution) != environment or digest_bytes(environment) != admission.environment_digest:
        raise ValueError('actual execution environment differs from admission environment')
    if execution.repository.revision != admission.source_commit:
        raise ValueError('actual execution source revision differs from admission source pin')
    frozen = canonical_json_bytes(expected_profile.model_dump(mode='json'))
    if sha256_digest(frozen) != expected_profile_digest:
        raise ValueError('expected execution profile differs from independently frozen profile digest')
    if canonical_json_bytes(execution.model_dump(mode='json')) != frozen:
        raise ValueError('complete execution profile differs from frozen admitted resources/measurement/output inventory')


def require_empty_adapter(bundle: AdapterBundle | None, workspace: Path) -> None:
    if bundle is not None and (bundle.source_digests or bundle.bundle_digest != digest_bytes(b'[]')):
        raise ValueError('declarative method profile refuses executable adapter bundles')
    if read_workspace(workspace):
        raise ValueError('declarative method profile refuses adapter files')


class MethodGatedRepositoryBackend(RepositoryBackend):
    """Map actual registered requests to validated data before container reservation.

    This profile has no arbitrary adapter surface: it refuses any coding bundle.
    The frozen repository contains the deployer-owned driver. Its declared source,
    image, command, limits, resources, measurement and output inventory are checked
    before real dispatch. expected_profile and expected_profile_digest are deployer
    authority captured from separate immutable prelaunch files; neither may be
    inferred from the candidate CAS profile being checked. The legacy admission
    source/environment encoding is retained so issued scientific identities stay fixed.
    """

    def __init__(self, *, execution_profile_digest: str, store: ContentAddressedStore,
                 admission: ArtifactProtocol, source: bytes, environment: bytes,
                 protocol_bytes: bytes, generator: int, mapper: RequestMapper,
                 expected_profile: ExecutionProfile, expected_profile_digest: str,
                 gpu_device_ids: tuple[str, ...] = (), observation_timeout: float = 30) -> None:
        execution = load_execution_profile(execution_profile_digest, store)
        verify_execution_binding(execution, admission, source, environment,
                                 expected_profile=expected_profile, expected_profile_digest=expected_profile_digest)
        if digest_bytes(protocol_bytes) != admission.protocol_digest:
            raise ValueError('frozen protocol bytes differ from admission')
        self._expected_profile = expected_profile
        self._expected_profile_digest = expected_profile_digest
        self.admission = admission
        self.source_bytes = source
        self.environment_bytes = environment
        self.protocol_bytes = protocol_bytes
        self.generator = generator
        self.mapper = mapper
        super().__init__(execution_profile_digest=execution_profile_digest, store=store,
                         gpu_device_ids=gpu_device_ids, observation_timeout=observation_timeout)

    def reserve(self, inputs: RepositoryRunInput, *, store: ContentAddressedStore,
                destination: Path) -> ReservedOperation:
        require_empty_adapter(inputs.bundle, inputs.workspace.staging_root)
        execution = load_execution_profile(self.execution_profile_digest, store)
        verify_execution_binding(execution, self.admission, self.source_bytes, self.environment_bytes,
                                 expected_profile=self._expected_profile,
                                 expected_profile_digest=self._expected_profile_digest)
        for entry in execution.repository.files:
            if digest_bytes(store.get(entry.digest)) != entry.digest:
                raise ValueError('actual method source bytes differ from frozen manifest')
        role, values = self.mapper(inputs.request.perturbation)
        payload = canonical_bytes({'protocol_digest': self.admission.digest,
                                   'target_id': self.admission.target.target_id,
                                   'generator': self.generator, 'role': role, 'interventions': values})
        validate_adapter_payload(self.admission, {'intervention.json': payload},
                                 source=self.source_bytes, environment=self.environment_bytes,
                                 protocol_bytes=self.protocol_bytes)
        # The exact registered request is independently committed and mounted by the core;
        # this validation object documents the request-to-intervention mapping in the same CAS.
        store.put(payload)
        return super().reserve(inputs, store=store, destination=destination)
