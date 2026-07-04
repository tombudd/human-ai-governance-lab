# Contributing

This repository is a clean-room public project. Contributions should keep the project easy to review, easy to test, and safe to publish.

## Contribution Rules

- Use toy examples only.
- Do not add private logs, private prompts, proprietary architecture, secrets, credentials, or real user data.
- Do not add production-readiness claims.
- Keep V1 deterministic and dependency-light.
- Add or update tests for behavior changes.
- Keep receipts reproducible and human-readable.

## Local Verification

Run the test suite before proposing a change:

```bash
python3 -m unittest discover -s tests
```

Regenerate the sample report when examples or receipt fields change:

```bash
python3 src/report.py examples reports/sample_report.json
```

