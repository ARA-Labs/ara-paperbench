"""Exact semantic dependencies of MMD-FUSE admission attestations."""
from __future__ import annotations

import io
import zipfile
from pathlib import Path

from aratest.research import replay_ledger
from aratest.research.repository import FilesystemContentAddressedStore, scientific_closure

ADMISSION_EXCLUSIONS: tuple[str, ...] = (
    'No baseline-method claim', 'No paper-temperature claim', 'No generator3',
    'No bootstrap intervention', 'Control is diagnostic, not C01 treatment',
    'Two finite treatment cells per family; engineering bands, not confidence intervals',
)


def admission_dependencies(destination: Path, generator: int, summary: bytes,
                           public: bytes) -> dict[str, tuple[bytes, ...]]:
    """Single dependency definition shared by finalization and independent verification."""
    source = (destination / 'source-manifest.json').read_bytes()
    environment = (destination / 'execution-environment.json').read_bytes()
    exposure = (destination / f'g{generator}-actual-exposure.json').read_bytes()
    return {
        'projection': ((destination / 'projection.json').read_bytes(), exposure),
        'method_binding': (source, environment, exposure, summary),
        'reproduction': ((destination / 'baseline-verification.json').read_bytes(), summary),
        'executed_family': (summary, public),
        'negative_control': (summary, (destination / 'control-rule.json').read_bytes(), public),
    }


def verify_public_run_bundle(destination: Path, public: bytes) -> None:
    """Require exactly the independently verified copied ledgers and their CAS closures."""
    expected: dict[str, bytes] = {}
    for generator in (1, 2):
        copied = destination / f'g{generator}-copied-replay'
        ledger = copied / 'research_ledger.jsonl'
        expected[f'g{generator}/research_ledger.jsonl'] = ledger.read_bytes()
        store = FilesystemContentAddressedStore(copied / 'scientific')
        for digest in scientific_closure(replay_ledger(ledger).records, store):
            expected[f'g{generator}/scientific/blobs/sha256/{digest}'] = store.get(digest)
    try:
        with zipfile.ZipFile(io.BytesIO(public)) as archive:
            names = archive.namelist()
            if len(names) != len(set(names)) or set(names) != set(expected):
                raise ValueError('public ZIP does not contain exactly the verified family closure')
            for info in archive.infolist():
                content = expected[info.filename]
                if info.is_dir() or info.file_size != len(content) or archive.read(info) != content:
                    raise ValueError('public ZIP bytes differ from verified copied ledger/CAS evidence')
    except zipfile.BadZipFile as error:
        raise ValueError('public ZIP is invalid') from error
