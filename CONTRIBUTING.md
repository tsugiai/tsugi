# Contributing to tsugi

Thanks for helping improve `tsugi`. This repository is the meta-package that
provides a unified import surface for the companion SDKs `tsugi-mend` and
`tsugi-kpool`.

## Development setup

Use Python 3.10 or newer.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## Checks

Run the same checks locally before opening a pull request:

```bash
ruff check src tests
mypy src
pytest -q
```

When feasible, also run any README quickstart or example code affected by your
change.

## Branches and pull requests

- Branch from the canonical `main` branch.
- Use a short, descriptive branch name for one logical change.
- Keep pull requests focused. Separate unrelated documentation, tests, and code
  changes into separate pull requests when practical.
- Use the pull request template and include test evidence.
- Do not include secrets, private paths, customer names, or proprietary context
  in public issues, pull requests, examples, or tests.

Maintainers review pull requests and squash-merge accepted changes. Do not
expect your branch history to be preserved after merge.

## Security reports

Please do not report suspected vulnerabilities in public issues. Follow
[`SECURITY.md`](SECURITY.md) for private disclosure instructions.
