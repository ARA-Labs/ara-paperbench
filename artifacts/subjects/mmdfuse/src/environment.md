# Environments and execution scope

The author environment is pinned by the immutable repository configuration, but that configuration leaves several baseline dependencies unversioned. It describes a GPU-oriented environment and multiple comparison packages. Source: the individually indexed environment files and paper appendix.

The completed local cell used Python 3.9.23, JAX/JAXLIB 0.4.6, NumPy 1.23.5, SciPy 1.10.1 and opt_einsum 3.3.0 on eight logical CPUs allocated from an Intel Xeon Gold 6230 host. The complete installed lock is [retained](../evidence/results/environment.lock.txt). Its immutable image is `sha256:93be80c8414492d143960ac82f5b318cb21c9e9497accc77075cccb572c4fafe`. Older JAXLIB wheels were obtained from the JAX authors’ archive without substituting a version.

The original [protocol](../evidence/results/preregistered-protocol.json) fixes the seed, within-cell schedule, source and runner hashes, resources, timeout and expected interval. Network was disabled and source/driver mounts were read-only. The driver’s original bytes are recoverable by reversing both documented substitutions: the added grounding comment and the source-citing module docstring. The exact reversal is recorded in execution/transcription.json and verified against the original driver hash. This artifact does not launch it.

No other paper experiment or baseline was run locally. Original hardware and warmed per-test timings are not interchangeable with this local whole-container duration. Unavailable raw datasets and unpinned external baseline versions remain limitations, not invented environment entries.

The original paper appendix reports an AMD Ryzen Threadripper 3960X with 24 cores, 128GB memory and 3.8GHz clock, plus an NVIDIA RTX A5000 with 24GB memory. These are author-reported hardware details, not the local trial hardware.
