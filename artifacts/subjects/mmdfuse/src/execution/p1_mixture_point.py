# Grounding: transcribed from supplied prepared/driver/run.py; only this comment and the source-citing module docstring are added.
"""Run the first published mixture sample-size cell using unchanged author code.

Source: supplied prepared/driver/run.py, full file; original identity in evidence/results/preregistered-protocol.json.
"""
from __future__ import annotations
import hashlib
import json
import os
from pathlib import Path
import sys
import time
from typing import Any

REPETITIONS: int = 200
SOURCE_HASHES: dict[str, str] = {'LICENSE.md': '0357f8dbcafa3b13ff64d571113b751207cd1189ac313c27517766b7dae0837e', 'mmdfuse.py': '7fbdcdee4466ff036973b6026c7cb74dd742cb722980f373039042ce9505a964', 'kernel.py': '304a93d2a27d4785bb5f9d72d0221f93553cad374a69821548587ab7ba9c257e', 'sampler_mixture.py': 'caf6733cc2e4b6974c6d6fade99c9c4a5bab9550e1064ae1efbfe3c2fc8d6b34'}


def main() -> None:
    started = time.monotonic()
    for name, expected in SOURCE_HASHES.items():
        if hashlib.sha256((Path('/source') / name).read_bytes()).hexdigest() != expected:
            raise RuntimeError(f'Author source changed: {name}')
    sys.path.insert(0, '/source')
    import jax
    import jax.numpy as jnp
    from jax import random
    import numpy as np
    from mmdfuse import mmdfuse
    from sampler_mixture import sampler_mixture

    key = random.PRNGKey(42)
    rejections: list[int] = []
    output = Path('/output')
    with (output / 'repetitions.jsonl').open('x') as stream:
        for repetition in range(REPETITIONS):
            key, sample_key = random.split(key)
            x, y = sampler_mixture(sample_key, m=500, n=500, d=2,
                                   mu=20, std_1=1, std_2=1.3)
            key, test_key = random.split(key)
            rejected = int(mmdfuse(x, y, test_key))
            if rejected not in (0, 1):
                raise RuntimeError('Author test did not return a binary rejection')
            rejections.append(rejected)
            record: dict[str, Any] = {
                'repetition': repetition,
                'sample_key': np.asarray(sample_key).tolist(),
                'test_key': np.asarray(test_key).tolist(),
                'x_sha256': hashlib.sha256(np.asarray(x).tobytes()).hexdigest(),
                'y_sha256': hashlib.sha256(np.asarray(y).tobytes()).hexdigest(),
                'rejected': rejected,
                'elapsed_seconds': time.monotonic() - started,
            }
            stream.write(json.dumps(record, sort_keys=True) + '\n')
            stream.flush()
            os.fsync(stream.fileno())
            print(json.dumps(record, sort_keys=True), flush=True)
    result = {
        'repetitions': REPETITIONS,
        'rejections': sum(rejections),
        'power_author': float(jnp.mean(jnp.array(rejections))),
        'power_count_ratio': sum(rejections) / REPETITIONS,
        'elapsed_seconds': time.monotonic() - started,
        'jax_version': jax.__version__,
        'devices': [str(d) for d in jax.devices()],
        'source_hashes': SOURCE_HASHES,
    }
    with (output / 'result.json').open('x') as stream:
        stream.write(json.dumps(result, indent=2) + '\n')
        stream.flush()
        os.fsync(stream.fileno())
    print(json.dumps(result, sort_keys=True), flush=True)


if __name__ == '__main__':
    main()
