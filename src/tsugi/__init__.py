"""tsugi: unified developer surface for TsugiCinema's open-source distributed-training SDKs.

Re-exports two physically separate Apache-2.0 SDKs at a packaging level:

    tsugi.mend   cross-rack reducer; patent-independent; public-art techniques
                 (Decoupled DiLoCo, DES-LOC, async-TP, FALCON). Wraps
                 tsugi-mend.

    tsugi.kpool  K-Pool LoRA / Infinity software analog; patent-aligned.
                 Apache-2.0 patent grant extends to TsugiCinema's K-Pool LoRA
                 (US App. 64/060,315) and Infinity (US App. 64/055,093) patent
                 estates as practiced by the SDK code as distributed. Wraps
                 tsugi-kpool.

The two sub-SDKs share zero code. This package is a thin packaging-level
wrapper. See LICENSE in each sub-SDK repo for full IP-posture details.
"""
from tsugi import mend, kpool

__version__ = "0.1.4"


def about() -> None:
    """Print versions, licenses, and patent-posture for the unified package."""
    from tsugi._about import _about_text
    print(_about_text())


__all__ = ["mend", "kpool", "about", "__version__"]
