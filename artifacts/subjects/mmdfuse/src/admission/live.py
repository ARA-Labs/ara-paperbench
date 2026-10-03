"""Prepare and execute the registered MMD-FUSE admission without changing baseline bytes."""
from __future__ import annotations

import json
import shutil
import time
import zipfile
from dataclasses import asdict
from functools import partial
from pathlib import Path
from typing import Any

import typer
from aratest.research import (
    PredictionResolutionSignal,
    ResearchBudget,
    ResearchComponents,
    replay_ledger,
    run_research_loop,
)
from aratest.research.controls import (
    MeanTreatmentReducer,
    ProtectedControlEvaluator,
    ProtectedControlRuleDescriptor,
)
from aratest.research.repository import (
    ExecutionProfile,
    FilesystemContentAddressedStore,
    ResourceFileManifest,
    SourceFileIdentity,
    scientific_closure,
    store_execution_profile,
    verify_scientific_closure,
)
from aratest.research.source_binding import SourceBindingConfiguration, read_source_bound_memory

from .. import ProjectionPolicy, canonical_bytes, digest_bytes, mmdfuse_protocol, project_source
from .backend import MethodGatedRepositoryBackend, execution_environment
from .family import (
    RULE_ID,
    LabelDegradationEvaluator,
    MethodScopeAdjudicator,
    RegisteredFamily,
    TargetBandVerdict,
    TargetScheduler,
)
from .protocol import (
    frozen_control_configuration,
    make_row_manifest,
    map_request,
    validate_row_manifest,
    verify_baseline,
)

app: typer.Typer = typer.Typer()


class TargetMeanReducer(MeanTreatmentReducer):
    rule_id: str = RULE_ID


def write_json(path: Path, value: Any) -> None:
    path.write_bytes(canonical_bytes(value))


@app.command()
def prepare(root: Path, destination: Path) -> None:
    """Freeze every identity and decision rule before a numerical process starts."""
    destination.mkdir(parents=True, exist_ok=False)
    baseline = root / 'ara/evidence/track2_d1_and_mmdfuse_2026-09-10/mmdfuse'
    write_json(destination / 'baseline-verification.json', verify_baseline(baseline))
    (destination / 'control-rule.json').write_bytes(frozen_control_configuration())
    (destination / 'control-source.py').write_bytes(Path(__file__).with_name('protocol.py').read_bytes())
    frozen = json.loads((baseline / 'preregistered-protocol.json').read_bytes())
    row = make_row_manifest()
    identity = json.loads(row)
    for record in identity['repetitions']:
        record['x'] = list(range(500))
        record['y'] = list(range(500))
    identity_bytes = canonical_bytes(identity)
    validate_row_manifest(identity_bytes)
    validate_row_manifest(row)
    rows = (identity_bytes, row)
    row_digests = tuple(digest_bytes(data) for data in rows)
    (destination / 'rows').mkdir()
    for data, digest in zip(rows, row_digests, strict=True):
        (destination / 'rows' / f'{digest}.json').write_bytes(data)
    write_json(destination / 'row-identities.json', list(row_digests))
    compiled = root / 'ara/evidence/track2_handoff_compilation_2026-09-10/mmdfuse-candidate-ara.zip'
    expected = json.loads((compiled.parent / 'hashes.json').read_bytes())[compiled.name]
    if digest_bytes(compiled.read_bytes()) != expected:
        raise ValueError('compiled immutable candidate archive hash mismatch')
    shutil.copyfile(compiled, destination / 'immutable-candidate.zip')
    candidate = destination / 'candidate'
    with zipfile.ZipFile(compiled) as archive:
        archive.extractall(candidate)
    claims = candidate / 'logic/claims.md'
    if '## C12:' in claims.read_text():
        raise ValueError('experimental-target claim identifier already used')
    with claims.open('a') as stream:
        stream.write('\n## C12: Attributed experimental target T-MF1\n'
                     '- **Statement**: T-MF1 evaluates robustness of the author-reported mixture-cell rejection proportion under the registered released-code seed and within-group row-order interventions.\n'
                     '- **Conditions**: Only the registered finite released-code intervention families; no paper-temperature or baseline-method comparison.\n'
                     '- **Evidence basis**: Attributed experimental target from the author notebook and archived original run; new family evidence remains pending until execution, controls, reduction and replay complete.\n'
                     '- **Status**: hypothesis\n'
                     '- **Provenance**: ai-suggested derived experimental target, explicitly approved in the joint admission plan\n'
                     '- **Sources**: [E10] and author experiment_mixture.ipynb cell 6 first position\n'
                     '- **Falsification criteria**: The finite-family treatment mean falls outside the frozen engineering band after the matched label control passes. A failed control yields inconclusive.\n'
                     '- **Proof**: [E12]\n'
                     '- **Dependencies**: []\n'
                     '- **Tags**: experimental-target, released-code, T-MF1\n')
    with (candidate / 'logic/experiments.md').open('a') as stream:
        stream.write('\n## E12: Registration target T-MF1\n- **Verifies**: [C12]\n'
                     '- **Procedure**: Frozen released-code mixture n=m=500,d=2,sigma2=1.3, 200 repetitions and 2000 permutations per test; registered parent seed or within-group row ordering; diagnostic pooled label permutation.\n'
                     '- **Run**: Frozen released-code source and attributed runner bound in the execution profile.\n'
                     '- **Setup**: Declared generated mixture inputs and registered finite seed or within-group row-order interventions.\n'
                     '- **Expected outcome**: Treatment remains in the original engineering band; diagnostic label control removes separation signal.\n'
                     '- **Metrics**: rejection_proportion\n- **Evidence**: admission/target.json\n'
                     '- **Baselines**: Author-reported released-code value; no competing-method or paper-temperature comparison.\n')
    (candidate / 'admission').mkdir()
    projection = project_source(baseline / 'official', destination / 'projected', ProjectionPolicy(
        allowed_paths=('LICENSE.md', 'kernel.py', 'mmdfuse.py', 'sampler_mixture.py'),
        excluded_paths=tuple(sorted(path.name for path in (baseline / 'official').iterdir()
                                   if path.name not in frozen['source_files'])),
        residue_literals=('0.18', '0.17999999', '0.05')))
    write_json(destination / 'projection.json', asdict(projection))
    shutil.copyfile(Path(__file__).with_name('run.py.txt'), destination / 'projected/run.py')
    store = FilesystemContentAddressedStore(destination / 'input-store')
    files = tuple(SourceFileIdentity(path=path.name, digest=store.put(path.read_bytes()))
                  for path in sorted((destination / 'projected').iterdir()))
    binding = canonical_bytes({'source_hashes': frozen['source_files'], 'baseline_protocol': digest_bytes((baseline / 'preregistered-protocol.json').read_bytes()),
                               'protocol_id':'mmdfuse-released-558e399-mixture-n500-v1'})
    row_manifest = ResourceFileManifest(files=tuple(sorted((SourceFileIdentity(path=f'{digest}.json', digest=store.put(data)) for data,digest in zip(rows,row_digests,strict=True)), key=lambda x:x.path)))
    protocol_bytes = canonical_bytes({'baseline':frozen, 'control_rule':json.loads(frozen_control_configuration()),
                                     'row_manifest_digests':list(row_digests), 'label_stream':'random.fold_in(sample_key,20260913)',
                                     'attribution':'released code lambda_multiplier=1; not paper-defined temperature',
                                     'families':{'1':{'seed_treatments':[42,43],'label_control_seed':42},'2':{'row_treatments':list(row_digests),'label_control_seed':42}}})
    (destination / 'frozen-protocol.json').write_bytes(protocol_bytes)
    payload = {
        'repository':{'source_uri':'https://github.com/antoninschrab/mmdfuse-paper','revision':frozen['source_commit'],'license':'MIT','files':[f.model_dump(mode='json') for f in files]},
        'resources':[
            {'resource_id':'binding','source_uri':'derived:frozen-source-binding','license':'MIT','kind':'blob','blob_path':'binding.json','digest':store.put(binding)},
            {'resource_id':'rows','source_uri':'derived:within-group-row-manifests','license':'MIT','kind':'file_manifest_v1','blob_path':None,'digest':store.put(canonical_bytes(row_manifest.model_dump(mode='json')))}],
        'image_digest':frozen['environment']['image'],
        'command':{'argv':['python3','-u','/source/run.py'],'environment':[['JAX_PLATFORM_NAME','cpu'],['OMP_NUM_THREADS','8'],['OPENBLAS_NUM_THREADS','1'],['PYTHONDONTWRITEBYTECODE','1']], 'request_path':'request.json','request_protocol':'aratest.run_request.v1'},
        'measurement':{'format':'json','path':'metric.json','metric':'rejection_proportion','parser_id':'json-metric','parser_version':'1'},
        'limits':{'timeout_seconds':3600,'cpu_count':8,'memory_bytes':17179869184,'pids_limit':512,'gpu':None,'private_shm_bytes':None}}
    execution = ExecutionProfile.model_validate(payload)
    execution_digest = store_execution_profile(execution, store)
    source = canonical_bytes(execution.repository.model_dump(mode='json'))
    environment = execution_environment(execution)
    admission = mmdfuse_protocol(source, environment, protocol_bytes, row_manifests=row_digests)
    (destination / 'source-manifest.json').write_bytes(source)
    (destination / 'execution-environment.json').write_bytes(environment)
    write_json(destination / 'admission-protocol.json', asdict(admission))
    write_json(destination / 'execution-profile.json', execution.model_dump(mode='json'))
    write_json(destination / 'identities.json', {'execution_profile_digest':execution_digest,'admission_digest':admission.digest,'immutable_candidate_sha256':expected})
    write_json(candidate / 'admission/target.json', asdict(admission.target))
    write_json(destination / 'prelaunch.json', {'frozen_at_utc':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),'protocol_sha256':digest_bytes(protocol_bytes),'control_rule_sha256':digest_bytes(frozen_control_configuration()),'no_numerical_launch_yet':True})
    print(destination, flush=True)


@app.command()
def run(destination: Path, generator: int) -> None:
    """Run or recover one registered family; never restart unknown completed work."""
    store = FilesystemContentAddressedStore(destination / 'input-store')
    identities = json.loads((destination / 'identities.json').read_bytes())
    rows = tuple(json.loads((destination / 'row-identities.json').read_bytes()))
    source = (destination / 'source-manifest.json').read_bytes()
    environment = (destination / 'execution-environment.json').read_bytes()
    protocol = (destination / 'frozen-protocol.json').read_bytes()
    admission = mmdfuse_protocol(source, environment, protocol, row_manifests=rows)
    admission.verify_identity(identities['admission_digest'])
    mapper = partial(map_request, generator=generator)
    backend = MethodGatedRepositoryBackend(execution_profile_digest=identities['execution_profile_digest'],store=store,
        admission=admission,source=source,environment=environment,protocol_bytes=protocol,generator=generator,mapper=mapper,
        expected_profile=ExecutionProfile.model_validate_json((destination / 'execution-profile.json').read_bytes()),
        expected_profile_digest=identities['execution_profile_digest'],
        observation_timeout=30)
    descriptor = ProtectedControlRuleDescriptor(rule_id='mmdfuse.label-degradation.v1',rule_version='1',
        evaluator_id='mmdfuse.label-degradation',evaluator_version='1',configuration_digest=store.put(frozen_control_configuration()),
        source_digests=tuple(sorted((store.put((destination / 'control-source.py').read_bytes()),store.put(protocol)))))
    components = ResearchComponents(scheduler=TargetScheduler(),families=(RegisteredFamily(generator,rows),),
        adjudicator=MethodScopeAdjudicator(generator,rows),coding_agent=None,backend=backend,reducers={},
        treatment_reducers={RULE_ID:TargetMeanReducer()},verdict=TargetBandVerdict(),progress=PredictionResolutionSignal(),
        control_evaluators={'mmdfuse.label-degradation.v1':ProtectedControlEvaluator(descriptor,LabelDegradationEvaluator())},
        content_sources=(store,),source_binding=SourceBindingConfiguration())
    output = destination / f'g{generator}'
    budget = ResearchBudget(max_states=1,max_registrations=1,max_cells=3,max_compute_seconds=10800,max_wall_clock_seconds=10800)
    while True:
        report = run_research_loop(destination / 'candidate',components,budget,output)
        write_json(destination / f'g{generator}-progress.json',report.model_dump(mode='json'))
        records = replay_ledger(report.ledger_path).records
        print(json.dumps({'generator':generator,'ledger_rows':len(records),'kinds':[r.kind for r in records[-3:]]}),flush=True)
        if any(r.kind == 'family_finalized' for r in records):
            break
        if not any(r.kind == 'operation_issued' for r in records):
            raise RuntimeError('family failed to issue scientific work')
        time.sleep(5)
    public = FilesystemContentAddressedStore(output / 'scientific')
    verify_scientific_closure(records,public)
    closure = scientific_closure(records,public)
    memory = read_source_bound_memory(report.ledger_path)
    copied = destination / f'g{generator}-copied-replay'
    copied.mkdir(exist_ok=False)
    shutil.copyfile(report.ledger_path,copied / 'research_ledger.jsonl')
    shutil.copytree(output / 'scientific',copied / 'scientific')
    copied_records = replay_ledger(copied / 'research_ledger.jsonl').records
    copied_store = FilesystemContentAddressedStore(copied / 'scientific')
    verify_scientific_closure(copied_records,copied_store)
    scientific_closure(copied_records,copied_store)
    copied_memory = read_source_bound_memory(copied / 'research_ledger.jsonl')
    write_json(destination / f'g{generator}-replay.json',{'ledger_rows':len(records),'completed_families':len(memory.completed),
        'copied_completed_families':len(copied_memory.completed),'verified_without_backend':True,'closure':str(type(closure))})


if __name__ == '__main__':
    app()
