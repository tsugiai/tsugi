# Security Policy

## Supported versions

`tsugi` is pre-alpha software. Security fixes are made on the current public
release line unless a maintainer states otherwise in a release note.

## Reporting a vulnerability

Please report suspected security vulnerabilities privately to
`tong@tsugicinema.com`. Include:

- The affected package name and version.
- A concise description of the vulnerability and impact.
- Reproduction steps, proof-of-concept code, or relevant logs when available.
- Whether the issue affects `tsugi` itself, one of the companion SDKs, or the
  packaging boundary between them.

Please do not open a public issue for a suspected vulnerability before a
maintainer has reviewed it. A maintainer will acknowledge the report, assess
scope and severity, and coordinate disclosure timing with the reporter when a
fix or mitigation is needed.

## Scope

This policy covers the `tsugi` meta-package, including its import surface,
packaging metadata, documentation, and dependency declarations. If a report
appears to belong primarily to `tsugi-mend` or `tsugi-kpool`, the maintainer may
move coordination to that companion repository while keeping the original report
confidential.

## Security expectations

Do not submit secrets, credentials, private datasets, or proprietary deployment
details in issues, pull requests, examples, tests, or logs. Keep public reports
focused on reproducible engineering behavior.
