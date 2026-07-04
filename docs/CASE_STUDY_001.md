# How a Human and an AI Collaborator Built a Governed Review Workflow

## 1. The Problem

AI-assisted work can move faster than review practices. Teams need lightweight ways to decide which AI-assisted actions can proceed, which need human approval, and which should be blocked.

## 2. The Human Role

The human selected the public problem, constrained the scope, defined the safety boundary, and kept the artifact focused on toy examples rather than private material.

## 3. The AI Collaborator Role

The AI collaborator helped produce a small implementation, tests, examples, receipts, and documentation within the clean-room boundary.

## 4. The Safety Boundary

The project uses synthetic examples only. It does not expose private logs, internal schemas, real system prompts, proprietary architecture, or production controls.

## 5. The Testable Artifact

The V1 artifact is a Python workflow that classifies proposed AI-assisted tasks as `allowed`, `needs_human_approval`, or `blocked`.

## 6. The Receipt

Each decision can produce a structured receipt containing the task ID, decision, risk level, reason, evidence requirement, and public-safe boundary flags.

## 7. What Passed

The unit tests cover the three core decisions: low-risk allowed tasks, medium-risk human checkpoint tasks, and blocked private-data external-action tasks.

## 8. What Remains Limited

This is not a production safety layer. It is a compact public demonstration of how governed collaboration artifacts can be made inspectable and testable.

