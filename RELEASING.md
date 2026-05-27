# Releasing `tsugi`

Releases of the `tsugi` meta-package are published to PyPI automatically by the
`.github/workflows/release.yml` GitHub Actions workflow when a **GitHub Release**
is published. Authentication uses **PyPI Trusted Publishing (OIDC)**, so there is
**no API token or secret** stored in this repository or in the workflow.

## How a release works

1. A maintainer publishes a GitHub Release whose tag matches the version in
   `pyproject.toml` (for example, tag `v0.1.0` for version `0.1.0`).
2. The `build` job builds the source distribution and wheel with
   `python -m build`, runs `twine check`, and uploads them as a build artifact.
3. The `publish` job downloads that artifact and uploads it to PyPI with
   `pypa/gh-action-pypi-publish`, authenticating via the GitHub OIDC token. The
   `id-token: write` permission is granted only on this job.

## One-time maintainer prerequisites (account-bound; cannot be automated in this repo)

These steps must be done once by the PyPI project owner before the first
trusted-publishing release. They bind a specific repository + workflow file +
environment to the PyPI project, so they cannot live in the repo.

1. **Create / own the PyPI project.** Be an owner of the `tsugi` project on
   PyPI (`https://pypi.org/project/tsugi/`). For the very first ever upload of a
   brand-new project, see the PyPI "pending publisher" flow referenced below.
2. **Register the Trusted Publisher on PyPI.** In the project's
   *Settings -> Publishing -> Add a new pending/trusted publisher* (GitHub
   Actions), enter exactly:
   - **PyPI Project Name:** `tsugi`
   - **Owner:** `tsugiai`
   - **Repository name:** `tsugi`
   - **Workflow filename:** `release.yml`
   - **Environment name:** `pypi`
3. **Create the GitHub environment.** In the GitHub repository
   *Settings -> Environments*, create an environment named `pypi` (matching the
   `environment.name` in the workflow). Optionally add required reviewers or a
   branch/tag restriction so only release tags can deploy to it.

The PyPI project name, owner, repository name, workflow filename, and
environment name above must match the workflow byte-for-byte. If you rename the
workflow file or the environment, update the PyPI Trusted Publisher registration
to match, or the publish step will be rejected.

## Cutting a release

1. Make sure `version` in `pyproject.toml` is correct (currently `0.1.0`).
   Bump it in a normal PR if you are shipping a new version.
2. Tag and create the release (the tag drives the release; the workflow does not
   read the version from the tag, but keep them consistent):

   ```bash
   git tag v0.1.0
   git push origin v0.1.0
   gh release create v0.1.0 --title "v0.1.0" --notes "Release notes here."
   ```

   (Or create the Release from the GitHub web UI. Either way, publishing the
   Release is what triggers the workflow.)
3. Watch the **Release** workflow run. The `publish` job uploads to PyPI via
   Trusted Publishing. No secret is required.

## Dry run (optional)

You can run the `build` job without publishing by triggering the workflow
manually (*Actions -> Release -> Run workflow*, i.e. `workflow_dispatch`). The
`publish` job is skipped for non-release events, so a manual run only verifies
that the distributions build and pass `twine check`.

## Notes

- The publish action is pinned to a released tag (`pypa/gh-action-pypi-publish@v1.14.0`)
  rather than a moving branch ref, per PyPA guidance.
- Trusted Publishing must stay tokenless. If a step ever appears to require a
  PyPI API token or password, stop and re-check the Trusted Publisher
  registration instead of adding a secret.

Reference: <https://docs.pypi.org/trusted-publishers/>
