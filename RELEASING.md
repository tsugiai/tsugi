# Releasing

This project publishes from GitHub Releases to PyPI with PyPI Trusted
Publishing. The workflow uses PyPI Trusted Publishing directly, so it does not
require stored publishing credentials in GitHub.

## One-time maintainer setup

Before the first release, a maintainer with access to the PyPI project and this
GitHub repository must register a Trusted Publisher on PyPI:

- PyPI project: `tsugi`
- Owner: `tsugiai`
- Repository: `tsugi`
- Workflow filename: `release.yml`
- GitHub environment: `pypi`

No GitHub-stored publishing credential is required for this setup.

## Release steps

1. Confirm the version in `pyproject.toml` is the intended release version.
2. Merge the release-ready change to `main`.
3. Create and publish a GitHub Release whose tag matches the package version,
   for example `v0.1.0`.
4. The `Release` workflow builds the source distribution and wheel with
   `python -m build`, then publishes the files to PyPI using Trusted
   Publishing.
5. After the workflow completes, verify the published package at
   `https://pypi.org/project/tsugi/`.
