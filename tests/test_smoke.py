"""Smoke tests for the unified tsugi meta-package.

These run in a torch-free environment by design: the meta-package itself
imports only the torch-free facades of each sub-SDK. The sub-SDK functions
that require torch (mend_init, plesio_init, etc.) are lazy-imported by the
sub-SDK facade and only resolve to a torch-dependent module on first call.
"""
from __future__ import annotations

import contextlib
import io

import tsugi


def test_version_string() -> None:
    assert isinstance(tsugi.__version__, str)
    assert tsugi.__version__ == "0.1.3"


def test_submodules_present() -> None:
    assert hasattr(tsugi, "mend")
    assert hasattr(tsugi, "kpool")


def test_mend_public_api_importable() -> None:
    from tsugi.mend import MendConfig, mend_init, mend_shutdown

    assert MendConfig is not None
    assert callable(mend_init)
    assert callable(mend_shutdown)


def test_kpool_public_api_importable() -> None:
    from tsugi.kpool import (
        KPoolLoraConfig,
        apply_kpool_step,
        plesio_init,
        plesio_shutdown,
        post_backward_step,
        pre_forward_step,
    )

    assert KPoolLoraConfig is not None
    for fn in (
        plesio_init,
        plesio_shutdown,
        apply_kpool_step,
        pre_forward_step,
        post_backward_step,
    ):
        assert callable(fn)


def test_about_emits_expected_strings() -> None:
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        tsugi.about()
    out = buf.getvalue()
    assert "tsugi" in out
    assert "Apache-2.0" in out
    assert "64/060,315" in out  # K-Pool LoRA application number
    assert "64/055,093" in out  # Infinity application number


def test_about_text_is_pure_string() -> None:
    """_about_text is the pure-string helper; useful for non-stdout callers."""
    from tsugi._about import _about_text

    text = _about_text()
    assert isinstance(text, str)
    assert len(text) > 0
