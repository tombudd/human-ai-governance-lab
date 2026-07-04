# Human-AI Governance Lab

![V1 tests](https://img.shields.io/badge/V1_tests-7_passing-brightgreen)
![Dependencies](https://img.shields.io/badge/dependencies-stdlib_only-blue)
![Scope](https://img.shields.io/badge/scope-clean_room_toy_examples-lightgrey)

Human-AI Governance Lab is a clean-room project exploring how AI-assisted work can be made more reviewable, testable, and accountable through lightweight risk classification, human checkpoints, and reproducible audit receipts.

This project was developed through a human-AI collaborative workflow. The repository demonstrates the public-safe artifacts of that process: examples, tests, review gates, and receipts.

The goal is not to make AI more autonomous. The goal is to make AI-assisted work more reviewable, accountable, and safe to delegate in stages.

## Public Repo Boundary

Human-AI Governance Lab is a clean-room public project for exploring how AI-assisted work can be made more reviewable, testable, and accountable through lightweight risk classification, human approval gates, and reproducible audit receipts.

This project does not expose private systems, private prompts, proprietary architecture, real user data, or production agent behavior. It uses toy examples and deterministic logic only.

## What V1 Does

Given a proposed AI-assisted action, V1 classifies it as:

- `allowed`
- `needs_human_approval`
- `blocked`

It then generates a receipt explaining the decision and the evidence requirement.

## Quick Start

Run the one-command demo:

```bash
python3 src/demo.py
```

Run the tests:

```bash
python3 -m unittest discover -s tests
```

Generate a sample report from the toy examples:

```bash
python3 src/report.py examples reports/sample_report.json
```

## Verification

The current V1 scaffold was verified locally with:

```bash
python3 -m unittest discover -s tests
```

Expected result:

```text
Ran 7 tests

OK
```

## Example Input

```json
{
  "task_id": "TASK-001",
  "task": "Draft a public README section from synthetic notes",
  "uses_private_data": false,
  "external_action": false,
  "could_affect_real_people": false,
  "requires_human_approval": false
}
```

## Example Output

```json
{
  "task_id": "TASK-001",
  "decision": "allowed",
  "risk_level": "low",
  "reason": "Synthetic public-safe drafting task with no external action, private data, or direct impact on real people.",
  "receipt_required": true
}
```

## Public-Safe Scope

This repository uses toy examples only. It does not include private logs, internal schemas, real system prompts, proprietary architecture, production controls, or claims of autonomous intelligence.
