# tsugi

[![PyPI version](https://img.shields.io/pypi/v/tsugi.svg)](https://pypi.org/project/tsugi/)
[![Python versions](https://img.shields.io/pypi/pyversions/tsugi.svg)](https://pypi.org/project/tsugi/)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![CI](https://github.com/tsugiai/tsugi/actions/workflows/ci.yml/badge.svg)](https://github.com/tsugiai/tsugi/actions/workflows/ci.yml)

Unified developer surface for TsugiCinema's open-source distributed-training SDKs.

```bash
pip install tsugi
```

`tsugi` is a thin packaging-level wrapper that depends on and re-exports two physically separate Apache-2.0 SDKs published by TsugiCinema, Inc.

| PyPI package | Imports as | Role | Patent posture |
|---|---|---|---|
| `tsugi-mend` | `tsugi.mend` | Cross-rack reducer | Patent-independent |
| `tsugi-kpool` | `tsugi.kpool` | K-Pool LoRA / Infinity analog | Patent-aligned |

(`tsugi-mend` integrates Decoupled DiLoCo + DES-LOC + async-TP + FALCON; `tsugi-kpool` is the software analog of US App. 64/060,315 and 64/055,093. See the sections below.)

The two sub-SDKs share zero code. This meta-package exposes them under a unified import namespace for developer convenience. Both sub-SDKs and this meta-package are licensed under the Apache License, Version 2.0.

## Status

**Pre-Alpha (0.1.3).** APIs are stabilizing. Cross-SDK integration patterns may evolve. The sub-SDK packages (`tsugi-mend` 0.1.5, `tsugi-kpool` 0.1.2) are pinned by exact version in this meta-package's dependencies.

## Quickstart

```python
import tsugi

tsugi.about()
# tsugi 0.1.3  unified developer surface
#   tsugi-mend  0.1.5  Apache-2.0  patent-independent (Decoupled DiLoCo + DES-LOC + async-TP + FALCON)
#   tsugi-kpool 0.1.2  Apache-2.0  patent-aligned (US App. 64/060,315 K-Pool LoRA + US App. 64/055,093 Infinity)
```

### Cross-rack reducer (`tsugi.mend`)

```python
from tsugi.mend import MendConfig, mend_init, mend_shutdown

# After your model is wrapped (FSDP, TP, etc.):
config = MendConfig(quorum_min_learners=2, grace_window_ms=2000)
mend_init(model, config)

# ... train ...

mend_shutdown(model)
```

See [`tsugi-mend`](https://github.com/tsugiai/tsugi-mend) for benchmark protocols, the multi-stage validation record (Stage A through Stage E-prime), and the Phase 2 sprint plan.

### K-Pool LoRA / Infinity (`tsugi.kpool`)

```python
from tsugi.kpool import KPoolLoraConfig, plesio_init, plesio_shutdown

config = KPoolLoraConfig(
    r=16,
    lora_alpha=32,
    n_adapters=8,
    k_active=4,
    sideband_enabled=True,
    aggregation_mode="buffer_convergence",
)
plesio_init(model, config)

# ... train with K-of-N adapter routing ...

plesio_shutdown(model)
```

See [`tsugi-kpool`](https://github.com/tsugiai/tsugi-kpool) for the buffer-convergence trigger characterization and the K-of-N routing semantics.

## Architecture

`tsugi` itself is a torch-free import: `import tsugi` resolves only to configuration dataclasses on each sub-SDK. The runtime functions (`mend_init`, `plesio_init`, etc.) lazy-import torch via each sub-SDK's facade on first call. This keeps documentation builds and torch-free CI environments working.

When you actually call a runtime function, that sub-SDK loads torch and its own runtime machinery. The two sub-SDKs never cross-reference each other; they can be installed and used independently of this meta-package.

## License and IP posture

Apache-2.0 with full automatic patent grant. See [`LICENSE`](LICENSE) for the preamble that distinguishes this meta-package's grant scope from each sub-SDK's grant scope, and [`NOTICE`](NOTICE) for the attribution chain to the upstream sub-SDKs.

The patent posture, in brief:

- This meta-package itself contains no patent-exercising code. Its Apache-2.0 patent grant covers only the thin wrapper code in this repository.
- `tsugi-mend` is patent-independent. Its Apache-2.0 grant does not extend to TsugiCinema's K-Pool LoRA or Infinity patent estates.
- `tsugi-kpool` is patent-aligned. Its Apache-2.0 grant in Section 3 extends to TsugiCinema's K-Pool LoRA (US App. 64/060,315) and Infinity (US App. 64/055,093) patent estates AS PRACTICED BY THE SDK CODE AS DISTRIBUTED. Apache-2.0 Section 3's "necessarily infringed by their Contribution" language bounds the patent license to the specific embodiment present in the SDK code, not the broader scope of the patent claims as filed.

## Links

- Homepage: https://tsugilabs.ai
- Companion SDK (Mend): https://github.com/tsugiai/tsugi-mend
- Companion SDK (KPool): https://github.com/tsugiai/tsugi-kpool
