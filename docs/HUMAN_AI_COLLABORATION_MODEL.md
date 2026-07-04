# Human-AI Collaboration Model

This project models a public-safe human-AI work loop:

1. A proposed AI-assisted task is described in structured form.
2. The task is classified for risk using simple, auditable rules.
3. The review gate returns `allowed`, `needs_human_approval`, or `blocked`.
4. The receipt records the decision, reason, and evidence requirement.
5. The final output remains bounded by the decision and the public-safe scope.

## Human Role

The human defines the task, reviews higher-risk work, approves or rejects escalation, and remains accountable for final publication.

## AI Collaborator Role

The AI collaborator can help draft examples, produce candidate classifications, generate receipts, and identify missing evidence. It does not receive authority to perform external actions in this V1.

## Design Boundary

This is a demonstration workflow, not a production safety system. The rules are intentionally small so they can be reviewed quickly and tested completely.

