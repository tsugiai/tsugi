"""tsugi.kpool: re-exports of tsugi-kpool public API.

Patent-aligned. The Apache-2.0 patent grant on this SDK extends to
TsugiCinema's K-Pool LoRA (US App. 64/060,315) and Infinity (US App.
64/055,093) patent estates AS PRACTICED BY THE SDK CODE AS DISTRIBUTED.
Apache-2.0 Section 3's "necessarily infringed by their Contribution"
language bounds the patent license to the specific embodiment present in
the SDK code, not the broader scope of the patent claims as filed. See
tsugi_kpool/LICENSE preamble for the full IP posture.

This module imports only KPoolLoraConfig (a torch-free dataclass) at load
time; plesio_init, plesio_shutdown, apply_kpool_step, pre_forward_step,
and post_backward_step are re-exported as lazy wrappers that import torch
via tsugi_kpool.runtime on first call. This keeps `import tsugi` torch-free
for docs and CI environments.
"""
from tsugi_kpool import (
    KPoolLoraConfig,
    apply_kpool_step,
    plesio_init,
    plesio_shutdown,
    post_backward_step,
    pre_forward_step,
)

__all__ = [
    "KPoolLoraConfig",
    "plesio_init",
    "plesio_shutdown",
    "apply_kpool_step",
    "pre_forward_step",
    "post_backward_step",
]
