"""Frozen admission checks; no outcome-dependent thresholds or upstream edits."""
from __future__ import annotations

import json
import math
import random
from pathlib import Path
from typing import TypedDict, cast

from aratest.generative import Perturbation

from .._identity import canonical_bytes, digest_bytes
from .._protocols import InterventionRole

PROTOCOL_ID: str = 'mmdfuse-released-558e399-mixture-n500-v1'


class RowPermutation(TypedDict):
    repetition: int
    x: list[int]
    y: list[int]


def require_released_attribution(protocol_id: str) -> None:
    if protocol_id != PROTOCOL_ID:
        raise ValueError('released-code results require the released protocol identity')


def frozen_control_configuration() -> bytes:
    return canonical_bytes({'maximum_control': 0.10, 'minimum_drop': 0.05,
        'reference_band': [0.13, 0.23], 'repetitions': 200,
        'rationale': 'Diagnostic engineering gate frozen before launch: null rejection at most twice alpha, '
                     'with at least the original reproduction half-band reduction. Not a null-level claim or confidence interval.'})


def control_passes(reference: float, control: float, configuration: bytes) -> bool:
    if configuration != frozen_control_configuration():
        raise ValueError('control configuration differs from frozen prelaunch rule')
    return (math.isfinite(reference) and math.isfinite(control) and 0.13 <= reference <= 0.23
            and 0 <= control <= 0.10 and reference - control >= 0.05)


def make_row_manifest() -> bytes:
    rng = random.Random(20260913)
    rows: list[RowPermutation] = []
    for repetition in range(200):
        x, y = list(range(500)), list(range(500))
        rng.shuffle(x)
        rng.shuffle(y)
        rows.append({'repetition': repetition, 'x': x, 'y': y})
    return canonical_bytes({'schema': 'mmdfuse-within-group-row-order-v1', 'seed': 42,
                            'repetitions': rows})


def validate_row_manifest(content: bytes) -> list[RowPermutation]:
    document = json.loads(content)
    if canonical_bytes(document) != content:
        raise ValueError('row permutation manifest must use canonical unambiguous JSON')
    if (not isinstance(document, dict) or set(document) != {'schema', 'seed', 'repetitions'}
            or document['schema'] != 'mmdfuse-within-group-row-order-v1'
            or type(document['seed']) is not int or document['seed'] != 42):
        raise ValueError('invalid row permutation manifest')
    rows = document['repetitions']
    if not isinstance(rows, list) or len(rows) != 200:
        raise ValueError('row permutation requires all 200 repetitions')
    for index, row in enumerate(rows):
        if not isinstance(row, dict) or set(row) != {'repetition', 'x', 'y'} or type(row['repetition']) is not int or row['repetition'] != index:
            raise ValueError('invalid per-repetition permutation identity')
        for group in ('x', 'y'):
            values = row[group]
            if (not isinstance(values, list) or any(type(value) is not int for value in values)
                    or sorted(values) != list(range(500))):
                raise ValueError('each within-group mapping must be a permutation without duplicates')
    return cast(list[RowPermutation], rows)


def map_request(perturbation: Perturbation, *, generator: int) -> tuple[InterventionRole, dict[str, object]]:
    values = dict(perturbation)
    if generator == 1:
        if set(values) != {'jax_seed', 'label_permutation'}:
            raise ValueError('unexpected seed-family fields')
        seed, label = values['jax_seed'], values['label_permutation']
        if type(seed) is not int or type(label) is not int or seed not in (42, 43) or label not in (0, 1):
            raise ValueError('unregistered seed-family scalar')
        if label:
            if seed != 42:
                raise ValueError('control requires matched reference seed42')
            return 'control', {'jax_seed': seed, 'label_permutation': 1}
        return 'treatment', {'jax_seed': seed}
    if generator == 2:
        if set(values) != {'label_permutation', 'row_permutation'}:
            raise ValueError('unexpected row-family fields')
        label, manifest = values['label_permutation'], values['row_permutation']
        if type(label) is not int or label not in (0, 1) or not isinstance(manifest, str):
            raise ValueError('unregistered row-family scalar')
        if label:
            return 'control', {'jax_seed': 42, 'label_permutation': 1}
        return 'treatment', {'row_permutation': {'sha256': manifest}}
    raise ValueError('unsupported generator')


def verify_baseline(root: Path) -> dict[str, object]:
    archive_hashes = json.loads((root.parent / 'hashes.json').read_bytes())
    verified = 0
    for name, expected in archive_hashes.items():
        if name.startswith('mmdfuse/') and (root.parent / name).is_file():
            if digest_bytes((root.parent / name).read_bytes()) != expected:
                raise ValueError(f'archived hash mismatch: {name}')
            verified += 1
    protocol_bytes = (root / 'preregistered-protocol.json').read_bytes()
    protocol = json.loads(protocol_bytes)
    if digest_bytes(protocol_bytes) != (root / 'preregistered-protocol.sha256').read_text().split()[0]:
        raise ValueError('baseline protocol hash mismatch')
    for name, expected in protocol['source_files'].items():
        for area in ('prepared/source', 'official'):
            if digest_bytes((root / area / name).read_bytes()) != expected:
                raise ValueError(f'baseline source hash mismatch: {name}')
    for path, key in [('prepared/driver/run.py', 'runner_sha256'),
                      ('environment.lock.txt', 'environment_lock_sha256'),
                      ('install-report.json', 'installation_report_sha256')]:
        if digest_bytes((root / path).read_bytes()) != protocol[key]:
            raise ValueError(f'baseline identity mismatch: {path}')
    parameters = protocol['parameters']
    if any(parameters[key] != expected for key, expected in {
            'repetitions': 200, 'number_permutations': 2000, 'lambda_multiplier': 1,
            'm': 500, 'n': 500, 'd': 2, 'std_2': 1.3, 'jax_seed': 42}.items()):
        raise ValueError('baseline schedule differs from frozen released protocol')
    records = [json.loads(line) for line in (root / 'run-output/repetitions.jsonl').read_bytes().splitlines()]
    if len(records) != 200 or [r['repetition'] for r in records] != list(range(200)):
        raise ValueError('baseline must have all 200 unique ordered outcome records')
    for record in records:
        if type(record['rejected']) is not int or record['rejected'] not in (0, 1):
            raise ValueError('nonbinary archived outcome')
        for key in ('x_sha256', 'y_sha256'):
            if len(record[key]) != 64 or any(c not in '0123456789abcdef' for c in record[key]):
                raise ValueError('invalid archived sample identity')
    result = json.loads((root / 'run-output/result.json').read_bytes())
    if sum(r['rejected'] for r in records) != result['rejections'] or result['rejections'] != 36:
        raise ValueError('archived count mismatch')
    return {'repetitions': 200, 'rejections': 36, 'verified_files': verified,
            'protocol_sha256': digest_bytes(protocol_bytes),
            'outcome_records_sha256': digest_bytes((root / 'run-output/repetitions.jsonl').read_bytes()),
            'per_record_sha256': [digest_bytes(canonical_bytes(record)) for record in records]}


def verify_archive_manifest(root: Path, *, supplement: Path | None = None) -> dict[str, object]:
    """Require every archived MMD-FUSE hash, using explicit retained missing-log bytes."""
    hashes = json.loads((root / 'hashes.json').read_bytes())
    verified: list[dict[str, str]] = []
    for name, expected in hashes.items():
        if not name.startswith('mmdfuse/'):
            continue
        path = root / name
        origin = 'archive'
        if not path.is_file():
            if supplement is None or not (supplement / name).is_file():
                raise ValueError(f'missing archived evidence: {name}')
            path = supplement / name
            origin = 'verified supplement'
        if digest_bytes(path.read_bytes()) != expected:
            raise ValueError(f'archived evidence hash mismatch: {name}')
        verified.append({'path': name, 'sha256': expected, 'origin': origin})
    return {'verified_files': len(verified), 'files': verified}
