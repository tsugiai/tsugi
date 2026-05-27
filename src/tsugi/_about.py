"""Implementation of tsugi.about(). Kept separate so the top-level package
import does not have to materialize the sub-SDK __version__ attributes.
"""


def _about_text() -> str:
    import tsugi
    import tsugi_mend
    import tsugi_kpool

    return (
        f"tsugi {tsugi.__version__}  unified developer surface\n"
        f"  tsugi-mend  {tsugi_mend.__version__}  Apache-2.0  "
        "patent-independent (Decoupled DiLoCo + DES-LOC + async-TP + FALCON)\n"
        f"  tsugi-kpool {tsugi_kpool.__version__}  Apache-2.0  "
        "patent-aligned (US App. 64/060,315 K-Pool LoRA + US App. 64/055,093 Infinity)\n"
        "\n"
        "Both SDKs are licensed under the Apache License, Version 2.0.\n"
        "The two SDKs share zero code; this is a packaging-level wrapper.\n"
        "Homepage: https://tsugilabs.ai"
    )
