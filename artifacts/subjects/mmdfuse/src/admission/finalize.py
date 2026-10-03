"""Publishable retained admission proofs; private runtime handles are never copied."""
from __future__ import annotations

import json
import re
import shutil
import zipfile
from dataclasses import asdict
from pathlib import Path
from typing import Any

import typer
import yaml
from aratest.research import replay_ledger
from aratest.research.repository import FilesystemContentAddressedStore, scientific_closure

from .. import (
    AdmissionCheck,
    AdmissionEvidence,
    assess_admission,
    canonical_bytes,
    digest_bytes,
    mmdfuse_protocol,
)
from .evidence import ADMISSION_EXCLUSIONS, admission_dependencies
from .results import verify_family

app: typer.Typer = typer.Typer()


def _public_runs(destination: Path, path: Path) -> None:
    with zipfile.ZipFile(path, 'x', zipfile.ZIP_DEFLATED) as archive:
        for generator in (1, 2):
            copied = destination / f'g{generator}-copied-replay'
            ledger = copied / 'research_ledger.jsonl'
            records = replay_ledger(ledger).records
            store = FilesystemContentAddressedStore(copied / 'scientific')
            archive.write(ledger, f'g{generator}/research_ledger.jsonl')
            for digest in scientific_closure(records, store):
                archive.writestr(f'g{generator}/scientific/blobs/sha256/{digest}', store.get(digest))


def finalize_admission(destination: Path) -> dict[str, Any]:
    summaries = {generator: verify_family(destination, generator) for generator in (1, 2)}
    source = (destination / 'source-manifest.json').read_bytes()
    environment = (destination / 'execution-environment.json').read_bytes()
    protocol = (destination / 'frozen-protocol.json').read_bytes()
    rows = tuple(json.loads((destination / 'row-identities.json').read_bytes()))
    admission = mmdfuse_protocol(source, environment, protocol, row_manifests=rows)
    admitted_id = json.loads((destination / 'identities.json').read_bytes())['admission_digest']
    admission.verify_identity(admitted_id)
    objects: dict[str, bytes] = {}

    def retain(content: bytes) -> str:
        digest = digest_bytes(content)
        objects[digest] = content
        return digest

    decisions: dict[str, Any] = {}
    public_runs = destination / 'public-runs.zip'
    _public_runs(destination, public_runs)
    public_identity = retain(public_runs.read_bytes())
    for generator in (1, 2):
        exposure_bytes = (destination / f'g{generator}-actual-exposure.json').read_bytes()
        exposure = json.loads(exposure_bytes)
        if not exposure['protected_threshold_absent'] or not exposure['frozen_source_manifest_verified']:
            raise ValueError('actual production exposure check failed')
        summary = canonical_bytes(summaries[generator])
        (destination / f'g{generator}-verified-results.json').write_bytes(summary)
        dependencies = {name: tuple(retain(content) for content in contents)
                        for name, contents in admission_dependencies(destination, generator, summary, public_runs.read_bytes()).items()}
        checks = tuple((name, retain(AdmissionCheck(name, admission.digest, 'T-MF1', generator, True,
                                                    digests).to_bytes())) for name, digests in dependencies.items())
        decision = assess_admission(admission, AdmissionEvidence(admission.digest, 'T-MF1', generator, checks),
                                    evidence_objects=objects)
        if not decision.admitted:
            raise ValueError(f'admission refused: {decision.missing}')
        decisions[f'generator{generator}'] = {**asdict(decision), 'digest': decision.digest}
    proof = destination / 'admission-proof-objects'
    proof.mkdir()
    for digest, content in objects.items():
        if digest != public_identity:
            (proof / digest).write_bytes(content)
    result: dict[str, Any] = {'artifact': 'mmdfuse', 'target': 'T-MF1', 'protocol': admission.protocol_id,
        'protocol_digest': admission.digest, 'decisions': decisions, 'public_runs_sha256': public_identity,
        'exclusions': list(ADMISSION_EXCLUSIONS),
        'families': summaries}
    (destination / 'admission-decision.json').write_bytes(canonical_bytes(result))
    for generator in (1, 2):
        (destination / f'admission-decision-g{generator}.json').write_bytes(canonical_bytes(decisions[f'generator{generator}']))
    candidate = destination / 'derived-admitted-candidate'
    shutil.copytree(destination / 'candidate', candidate)
    evidence = candidate / 'evidence/admission'
    evidence.mkdir()
    shutil.copyfile(public_runs, evidence / 'public-runs.zip')
    (evidence / 'report.json').write_bytes(canonical_bytes(result))
    for name in ('frozen-protocol.json', 'control-rule.json', 'source-manifest.json', 'execution-environment.json', 'execution-profile.json', 'projection.json', 'identities.json'):
        shutil.copyfile(destination / name, evidence / name)
    claims_path = candidate / 'logic/claims.md'
    claims_prefix, claim_header, claim = claims_path.read_text().partition('## C12:')
    for field, text in {
        'Conditions': 'Only the registered finite families under the released-code protocol; no baseline-method or paper-temperature comparison, no bootstrap and no external dataset. The verdict concerns the preregistered finite two-treatment mean, not every seed or unrestricted robustness.',
        'Sources': '[E10] and author experiment_mixture.ipynb cell 6 first position; exact target and measured outcomes are in evidence/admission/report.json.',
        'Evidence basis': 'Completed method-bound repository operations, complete per-repetition outcomes, satisfied protected label controls and independent copied public replay.',
    }.items():
        pattern = rf'^- \*\*{re.escape(field)}\*\*:.*$'
        line = f'- **{field}**: {text}'
        claim = re.sub(pattern, line, claim, flags=re.M) if re.search(pattern, claim, re.M) else f'{claim}{line}\n'
    claims_path.write_text(f'{claims_prefix}{claim_header}{claim}')
    experiments = candidate / 'logic/experiments.md'
    prefix, header, experiment = experiments.read_text().partition('## E12:')
    for field, text in {
        'Evidence': '[admission report](../evidence/admission/report.json) and [public closure](../evidence/admission/public-runs.zip)',
        'Run': 'Frozen released driver in the captured public execution profile; generator families and all attempts are in the public closure.',
        'Setup': 'Same released implementation, generated mixture inputs and finite seed/row-order interventions; reference/control roles fixed before dispatch.',
        'Expected outcome': 'Treatment mean stays in the original engineering band while label permutation removes separation signal; a failed control blocks a target verdict.',
    }.items():
        pattern = rf'^- \*\*{re.escape(field)}\*\*:.*$'
        line = f'- **{field}**: {text}'
        experiment = re.sub(pattern, line, experiment, flags=re.M) if re.search(pattern, experiment, re.M) else f'{experiment}{line}\n'
    experiments.write_text(f'{prefix}{header}{experiment}')
    paper = candidate / 'PAPER.md'
    paper.write_text(paper.read_text().replace('admission_status: not admitted', 'admission_status: T-MF1 admitted for registered generator1 and generator2 only') +
                    '\n## Derived released-code admission\n\nThis revision adds the separately attributed experimental target T-MF1. '
                    'The original claim blocks remain source-attributed; admission does not certify their theory, comparisons, or paper temperature. '
                    'See [the full retained report](evidence/admission/report.json) and [copied public runs](evidence/admission/public-runs.zip).\n')
    g1 = json.loads(canonical_bytes(summaries[1]))
    if g1['individual_treatments_outside_reference_band']:
        outside = g1['individual_treatments_outside_reference_band'][0]
        measured = outside['value']
        seed = outside['cell']['jax_seed']
        mean = g1['registered_measurement']['value']
        low, high = admission.target.engineering_band
        boundary = high if measured > high else low
        direction = 'exceeding' if measured > high else 'below'
        with paper.open('a') as stream:
            stream.write(f'\nThe seed-{seed} cell produced {round(measured * 200)}/200 rejections ({measured}), '
                         f'{direction} the original band edge {boundary} by {abs(measured-boundary):.3f}. '
                         f'The G1 `{g1["registered_verdict"]["outcome"]}` verdict refers only to the preregistered finite two-treatment mean {mean}. '
                         'It does not say every seed reproduces or establish unrestricted seed robustness. The band and reducer were not widened. '
                         'Seed-42 baseline reproduction, runtime and source exposure checks stand independently.\n\n'
                         '**Sources**: [result] [retained family report](evidence/admission/report.json) '
                         f'«"rejection_proportion":{measured}» and «"value":{mean}»; '
                         '[input] [frozen original band](evidence/admission/frozen-protocol.json).\n')
    index = candidate / 'evidence/README.md'
    index.write_text(index.read_text().replace('## Source status', '## Historical source compilation status'))
    paper.write_text(paper.read_text().replace('Issue [#281](https://github.com/ARA-Labs/DissClaimer/issues/281) owns the future protocol/admission choice.', 'The original compilation left the protocol/admission choice in issue [#281](https://github.com/ARA-Labs/DissClaimer/issues/281). This derived revision records its released-code choice below.'))
    with index.open('a') as stream:
        stream.write('\n| [admission/report.json](admission/report.json) | Registered T-MF1 family/control and source-binding evidence |\n'
                     '| [admission/public-runs.zip](admission/public-runs.zip) | Complete copied public ledgers and exact scientific closures, without private runtime handles |\n')
    constraints = candidate / 'logic/solution/constraints.md'
    constraints.write_text(constraints.read_text().replace('# Conditions, limitations and unresolved scope',
        '# Conditions, limitations and unresolved scope\n\n## Historical source-compilation boundary\n\nThe following bullets describe the preserved original compilation and its original local run. The derived target boundary below records what changed.') +
        '\n## Derived T-MF1 admission boundary\n\nThe released-code protocol choice is now explicit. Registered seed and within-group row-order families execute through the method gate, protected label control, treatment reducer and copied public replay. '
        'The target is the finite-family mean in the original engineering band. It does not establish population robustness across arbitrary seeds, the paper-defined temperature, a method baseline comparison, a null-level claim, bootstrap validity or external-dataset coverage. '
        'The full audit artifact contains protected outcomes; only the separately measured source projection and safe artifact may enter agent inputs.\n')
    deployment_source = candidate / 'src/admission'
    deployment_source.mkdir()
    for path in sorted(Path(__file__).parent.iterdir()):
        if path.is_file() and (path.suffix == '.py' or path.name == 'run.py.txt'):
            shutil.copyfile(path, deployment_source / path.name)
    with (candidate / 'src/artifacts.md').open('a') as stream:
        stream.write('\n## Derived admission implementation\n\n')
        for path in sorted(deployment_source.iterdir()):
            stream.write(f'- [{path.name}](admission/{path.name}) — attributed admission implementation.\n')
    abort_path = destination.parent / 'aborted-exposure-attempts.json'
    if abort_path.is_file():
        shutil.copyfile(abort_path, evidence / abort_path.name)
    tree_path = candidate / 'trace/exploration_tree.yaml'
    tree = yaml.safe_load(tree_path.read_text())
    admission_nodes: list[dict[str, Any]] = [
        {'id': 'N16', 'type': 'decision', 'support_level': 'explicit', 'provenance': 'ai-executed',
         'title': 'Attribute the released-code experimental target separately', 'evidence': ['C12'],
         'choice': 'Keep released lambda_multiplier=1 and distinguish the paper-defined temperature.',
         'alternatives': ['A separately frozen paper-defined implementation comparison, outside this admission.'],
         'source_refs': ['evidence/admission/frozen-protocol.json'], 'also_depends_on': ['N15']},
        {'id': 'N17', 'type': 'dead_end', 'support_level': 'explicit', 'provenance': 'ai-executed',
         'title': 'Abort threshold-exposing preparation before admission', 'evidence': ['C12'],
         'hypothesis': 'A full protocol blob could serve as a harmless workload input.',
         'failure_mode': 'The blob exposed protected diagnostic thresholds; two new attempts were stopped as ineligible.',
         'lesson': 'Inventory actual mounted resource bytes; keep protected comparison policy exclusively on the evaluator side.',
         'source_refs': ['evidence/admission/aborted-exposure-attempts.json'], 'also_depends_on': ['N16']},
        {'id': 'N18', 'type': 'experiment', 'support_level': 'explicit', 'provenance': 'ai-executed',
         'title': 'Execute the registered seed family and label control', 'evidence': ['C12'],
         'result': 'Complete method-bound cells, satisfied diagnostic control, treatment reduction and copied public replay are retained.',
         'source_refs': ['evidence/admission/report.json', 'evidence/admission/public-runs.zip'], 'also_depends_on': ['N17']},
        {'id': 'N19', 'type': 'experiment', 'support_level': 'explicit', 'provenance': 'ai-executed',
         'title': 'Execute within-group row-order family and label control', 'evidence': ['C12'],
         'result': 'The registered per-repetition identity and shuffled row mappings executed end to end with their diagnostic control.',
         'source_refs': ['evidence/admission/report.json', 'evidence/admission/public-runs.zip'], 'also_depends_on': ['N17']},
    ]
    if not abort_path.is_file():
        admission_nodes = [node for node in admission_nodes if node['id'] != 'N17']
        for node in admission_nodes:
            node['also_depends_on'] = ['N16' if item == 'N17' else item for item in node['also_depends_on']]
    recovery = destination / 'second-cell-awaiting-recovery.json'
    if recovery.is_file():
        shutil.copyfile(recovery, evidence / recovery.name)
        admission_nodes.append({
            'id': 'N20', 'type': 'pivot', 'support_level': 'explicit', 'provenance': 'ai-executed',
            'title': 'Recover completed later cells without repeating scientific work', 'evidence': ['C12'],
            'from': 'A global pending check prevented importing the completed second cells.',
            'to': 'The request-specific terminal check lets recovery import the existing authenticated receipts and advance.',
            'trigger': 'Both second-cell containers were idle with complete authenticated outputs while the ledger stayed pending.',
            'source_refs': ['evidence/admission/second-cell-awaiting-recovery.json', 'evidence/admission/public-runs.zip'],
            'also_depends_on': ['N17' if abort_path.is_file() else 'N16'],
        })
        for node in admission_nodes:
            if node['id'] in ('N18', 'N19'):
                node['also_depends_on'].append('N20')
    tree['tree'].extend(admission_nodes)
    tree_path.write_text(yaml.safe_dump(tree, sort_keys=False, allow_unicode=True))
    return result


@app.command()
def main(destination: Path) -> None:
    result = finalize_admission(destination)
    print(json.dumps({'artifact': result['artifact'], 'admitted_generators': [1, 2]}), flush=True)


if __name__ == '__main__':
    app()
