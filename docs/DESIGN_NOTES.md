# Design Notes

## V1 Goal

V1 demonstrates a small, inspectable workflow for AI-assisted task review:

1. Describe a proposed task in structured JSON.
2. Classify the task with deterministic rules.
3. Return `allowed`, `needs_human_approval`, or `blocked`.
4. Generate a receipt with the reason and evidence requirement.

## Why Deterministic Rules

The project is meant to be easy to audit. Deterministic rules make the behavior reviewable in code and reproducible in tests.

## Decision Rules

- `allowed`: no private data, no external action, no direct impact on real people, and no required human approval flag.
- `needs_human_approval`: private data, external action, direct impact on real people, or an explicit human approval flag appears without triggering the blocked condition.
- `blocked`: private data is combined with an external action.

## Non-Goals

- Production policy enforcement
- Real user data processing
- Autonomous external action
- Hidden prompts or internal agent behavior
- Claims that this is a complete safety system

