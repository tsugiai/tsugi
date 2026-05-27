"""tsugi.mend: re-exports of tsugi-mend public API.

Patent-independent by deliberate construction. The Apache-2.0 patent grant
on this SDK does NOT extend to TsugiCinema's K-Pool LoRA or Infinity patent
estates. See tsugi_mend/LICENSE preamble for the full IP posture.

This module imports only MendConfig (a torch-free dataclass) at load time;
mend_init and mend_shutdown are re-exported as lazy wrappers that import
torch via tsugi_mend.runtime on first call. This keeps `import tsugi`
torch-free for docs and CI environments.
"""
from tsugi_mend import MendConfig, mend_init, mend_shutdown

__all__ = ["MendConfig", "mend_init", "mend_shutdown"]
