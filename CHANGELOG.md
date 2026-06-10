# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.2] - 2026-06-10

### Changed

- Re-pin `tsugi-mend` from `0.1.3` to `0.1.4`, which wires the world-size-aware
  multi-rack reducer live through the runtime (opt-in
  `MendConfig.expected_learner_ids`, early-finalize `all_present`,
  `learners_absent` absentee diagnostic; default mode unchanged).
  `tsugi-kpool` stays pinned at `0.1.2`.
- Ignore `uv.lock` via `.gitignore`, matching the sub-SDK repo convention.

## [0.1.1] - 2026-06-09

### Changed

- Re-pin `tsugi-mend` from `0.1.2` to `0.1.3`, which ships the lossless
  sparse-delta compression mode, the online runtime autotuner (default OFF),
  and the stall-sweep benchmark harness. `tsugi-kpool` stays pinned at `0.1.2`.
- Republishing carries the verbatim Apache-2.0 `LICENSE` file to PyPI; the
  `0.1.0` artifact predates the post-launch LICENSE-file restructure.

## [0.1.0] - 2026-05-27

### Added

- Initial public release.
