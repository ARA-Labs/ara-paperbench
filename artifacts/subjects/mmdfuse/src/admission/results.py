"""Independent verification of retained full-cell outcomes and public family closure."""
from __future__ import annotations

import json
import math
from dataclasses import asdict
from pathlib import Path
from typing import Any

from aratest.research import ExperimentProposal, RegisteredExperiment, replay_ledger
from aratest.research.controls import ControlEvaluationResult
from aratest.research.repository import (
    ExecutionProfile,
    ExecutionTrace,
    FilesystemContentAddressedStore,
    OperationDescription,
    load_execution_profile,
    scientific_closure,
    verify_scientific_closure,
)

from .._identity import canonical_bytes, digest_bytes
from .backend import verify_execution_binding
from .evidence import ADMISSION_EXCLUSIONS, admission_dependencies, verify_public_run_bundle

ATTRIBUTION: str = 'released implementation; lambda_multiplier=1; not paper temperature'


def verify_cell_result(value: dict[str, Any], baseline: list[dict[str, Any]], *,
                       baseline_match: bool, baseline_draws: bool = True) -> dict[str, object]:
    """Require all200 outcomes; exact matching applies only to reference execution."""
    if value.get('attribution') != ATTRIBUTION:
        raise ValueError('result attribution is not the released-code protocol')
    records = value['records']
    if value['repetitions'] != 200 or len(records) != 200 or [r['repetition'] for r in records] != list(range(200)):
        raise ValueError('full cell requires all200 unique ordered outcome records')
    total = 0
    last_elapsed = 0.0
    for index, record in enumerate(records):
        rejected = record['rejected']
        if type(rejected) is not int or rejected not in (0, 1):
            raise ValueError('cell outcome is not binary')
        total += rejected
        elapsed = record['elapsed_seconds']
        if not math.isfinite(elapsed) or not last_elapsed <= elapsed <= 3600:
            raise ValueError('invalid whole-cell elapsed schedule')
        last_elapsed = elapsed
        for field in ('x_sha256', 'y_sha256', 'drawn_x_sha256', 'drawn_y_sha256'):
            digest = record[field]
            if not isinstance(digest, str) or len(digest) != 64 or any(c not in '0123456789abcdef' for c in digest):
                raise ValueError('invalid per-repetition sample hash')
        if baseline_draws:
            for field in ('sample_key', 'test_key'):
                if record[field] != baseline[index][field]:
                    raise ValueError('sampler/test keys differ from frozen reference schedule')
            for group in ('x', 'y'):
                if record[f'drawn_{group}_sha256'] != baseline[index][f'{group}_sha256']:
                    raise ValueError('drawn inputs differ from archived author sample hashes')
        if baseline_match:
            for field in ('rejected', 'x_sha256', 'y_sha256'):
                if record[field] != baseline[index][field]:
                    raise ValueError('matched released-code outcome differs from pinned implementation')
    if total != value['rejections'] or value['rejection_proportion'] != total / 200:
        raise ValueError('complete outcome count disagrees with metric')
    if abs(value['power_author'] - total / 200) > 1e-7:
        raise ValueError('author float32 aggregate differs from complete count')
    if not last_elapsed <= value['elapsed_seconds'] <= 3600:
        raise ValueError('whole-cell runtime limit exceeded')
    return {'repetitions': 200, 'rejections': total, 'rejection_proportion': total/200,
            'matched_author_outcomes': 200 if baseline_match else None,
            'matched_author_draws': 200 if baseline_draws else None,
            'all_record_sha256': [digest_bytes(canonical_bytes(record)) for record in records]}


def require_family_proposal(proposal: ExperimentProposal, generator: int, manifests: tuple[str, ...]) -> None:
    from .family import make_proposal

    if proposal != make_proposal(generator, manifests):
        raise ValueError('public execution belongs to a different registered intervention family')


def verify_family(destination: Path, generator: int) -> dict[str, object]:
    """Read only public evidence; no backend, provider, original container, or repair."""
    output = destination / f'g{generator}-copied-replay'
    records = replay_ledger(output / 'research_ledger.jsonl').records
    store = FilesystemContentAddressedStore(output / 'scientific')
    verify_scientific_closure(records, store)
    scientific_closure(records, store)
    baseline_identity = json.loads((destination / 'baseline-verification.json').read_bytes())['outcome_records_sha256']
    # The once-captured immutable candidate already carries these archived bytes.
    # Read them from the copied public store, never an original source directory.
    baseline = [json.loads(line) for line in store.get(baseline_identity).splitlines()]
    source_hashes = json.loads((destination / 'frozen-protocol.json').read_bytes())['baseline']['source_files']
    manifests = tuple(json.loads((destination / 'row-identities.json').read_bytes()))
    identity_manifest = manifests[0]
    registrations = [RegisteredExperiment.model_validate(row.payload) for row in records if row.kind == 'registration']
    if len(registrations) != 1:
        raise ValueError('family evidence requires exactly one registration')
    require_family_proposal(registrations[0].proposal, generator, manifests)
    expected_profile = json.loads((destination / 'identities.json').read_bytes())['execution_profile_digest']
    if registrations[0].execution_profile_digest != expected_profile:
        raise ValueError('registered family execution profile differs from frozen admission')
    from .. import mmdfuse_protocol
    source = (destination / 'source-manifest.json').read_bytes()
    environment = (destination / 'execution-environment.json').read_bytes()
    protocol_bytes = (destination / 'frozen-protocol.json').read_bytes()
    admission = mmdfuse_protocol(source, environment, protocol_bytes, row_manifests=manifests)
    verify_execution_binding(load_execution_profile(expected_profile, store), admission, source, environment,
        expected_profile=ExecutionProfile.model_validate_json((destination / 'execution-profile.json').read_bytes()),
        expected_profile_digest=expected_profile)
    cells: list[dict[str, object]] = []
    for record in records:
        if record.kind != 'execution_attempt':
            continue
        trace = ExecutionTrace.model_validate_json(store.get(str(record.payload['trace_digest'])))
        if trace.failure is not None or trace.metric_source_digest is None:
            raise ValueError('failed operation cannot establish admission')
        if trace.duration_seconds is None or trace.duration_seconds > 3600:
            raise ValueError('missing or exceeded whole-cell duration')
        value = json.loads(store.get(trace.metric_source_digest))
        operation = OperationDescription.model_validate_json(store.get(trace.description_digest))
        if value['request'] != operation.request.model_dump(mode='json'):
            raise ValueError('metric source request differs from actual registered operation')
        if value['source_hashes'] != source_hashes:
            raise ValueError('executed author source differs from archived source')
        perturbation = dict(value['request']['perturbation'])
        label = perturbation['label_permutation']
        reference = (not label and (perturbation.get('jax_seed') == 42 or perturbation.get('row_permutation') == identity_manifest))
        verified = verify_cell_result(value, baseline, baseline_match=reference,
                                      baseline_draws=perturbation.get('jax_seed', 42) == 42)
        cells.append({'cell': perturbation, 'trace_digest': str(record.payload['trace_digest']),
                      'metric_source_digest': trace.metric_source_digest,
                      'duration_seconds': trace.duration_seconds, **verified})
    if len(cells) != 3:
        raise ValueError('registered family needs all three executed cells')
    evaluations = [ControlEvaluationResult.model_validate_json(store.get(str(r.payload['evaluation_digest'])))
                   for r in records if r.kind == 'control_evaluation_committed']
    if len(evaluations) != 1 or evaluations[0].status != 'satisfied':
        raise ValueError('failed or unavailable control blocks admission')
    if not any(r.kind == 'family_finalized' for r in records):
        raise ValueError('family must finish reduction and finalization')
    measurements = [row.payload for row in records if row.kind == 'family_measurement']
    verdicts = [row.payload for row in records if row.kind == 'verdict']
    if len(measurements) != 1 or len(verdicts) != 1 or verdicts[0]['outcome'] not in ('holds', 'falsified'):
        raise ValueError('family requires one conclusive registered reduction and target verdict')
    outside = [{'cell': cell['cell'], 'value': cell['rejection_proportion']} for cell in cells
               if isinstance(cell['cell'], dict) and cell['cell']['label_permutation'] == 0
               and isinstance(cell['rejection_proportion'], float) and not 0.13 <= cell['rejection_proportion'] <= 0.23]
    return {'generator': generator, 'target_id': 'T-MF1', 'cells': cells,
            'registered_measurement': measurements[0], 'registered_verdict': verdicts[0],
            'individual_treatments_outside_reference_band': outside,
            'control': evaluations[0].model_dump(mode='json'),
            'copied_public_closure_verified': True, 'all_scientific_stages_within_3600_seconds': True}


def verify_retained_admission(destination: Path) -> dict[str, bool]:
    """Verify gate object closure and recheck both public family traces without execution."""
    from .. import AdmissionEvidence, assess_admission, mmdfuse_protocol

    source = (destination / 'source-manifest.json').read_bytes()
    environment = (destination / 'execution-environment.json').read_bytes()
    protocol_bytes = (destination / 'frozen-protocol.json').read_bytes()
    manifests = tuple(json.loads((destination / 'row-identities.json').read_bytes()))
    protocol = mmdfuse_protocol(source, environment, protocol_bytes, row_manifests=manifests)
    raw_record = (destination / 'admission-decision.json').read_bytes()
    record = json.loads(raw_record)
    if canonical_bytes(record) != raw_record:
        raise ValueError('retained admission record must be canonical unambiguous JSON')
    if (record['protocol_digest'] != protocol.digest or record['artifact'] != 'mmdfuse'
            or record['target'] != protocol.target.target_id or record['protocol'] != protocol.protocol_id
            or record['exclusions'] != list(ADMISSION_EXCLUSIONS)):
        raise ValueError('retained admission identity or scope differs from frozen inputs')
    if set(record['decisions']) != {'generator1', 'generator2'} or set(record['families']) != {'1', '2'}:
        raise ValueError('retained admission must contain exactly the two registered families')
    objects = {path.name: path.read_bytes() for path in (destination / 'admission-proof-objects').iterdir() if path.is_file()}
    public = (destination / 'public-runs.zip').read_bytes()
    public_digest = digest_bytes(public)
    if record['public_runs_sha256'] != public_digest:
        raise ValueError('declared public ZIP identity differs from actual retained bytes')
    objects[public_digest] = public
    checked: dict[str, bool] = {}
    for generator in (1, 2):
        stored = record['decisions'][f'generator{generator}']
        data = stored['evidence']
        if (type(stored['generator']) is not int or stored['generator'] != generator
                or type(data['generator']) is not int or data['generator'] != generator):
            raise ValueError('stored decision/evidence generator differs from verified family')
        summary = canonical_bytes(verify_family(destination, generator))
        if canonical_bytes(record['families'][str(generator)]) != summary:
            raise ValueError('displayed family summary differs from freshly verified evidence')
        if (destination / f'g{generator}-verified-results.json').read_bytes() != summary:
            raise ValueError('retained family summary differs from freshly verified evidence')
        evidence = AdmissionEvidence(data['protocol_digest'], data['target_id'], data['generator'],
                                     tuple((name, digest) for name, digest in data['checks']))
        decision = assess_admission(protocol, evidence, evidence_objects=objects)
        reconstructed = {**asdict(decision), 'digest': decision.digest}
        if not decision.admitted or canonical_bytes(stored) != canonical_bytes(reconstructed):
            raise ValueError('complete retained admission decision differs from reconstruction')
        dependencies = admission_dependencies(destination, generator, summary, public)
        for name, identity in evidence.checks:
            gate = json.loads(objects[identity])
            expected = [digest_bytes(content) for content in dependencies[name]]
            if gate['evidence_digests'] != expected:
                raise ValueError('gate references differ from verified family summary and exact evidence')
            for content, digest in zip(dependencies[name], expected, strict=True):
                if objects.get(digest) != content:
                    raise ValueError('gate proof bytes differ from verified admission inputs')
        if (destination / f'admission-decision-g{generator}.json').read_bytes() != canonical_bytes(reconstructed):
            raise ValueError('standalone decision differs from reconstructed admission')
        checked[f'generator{generator}'] = decision.admitted
    verify_public_run_bundle(destination, public)
    return checked
