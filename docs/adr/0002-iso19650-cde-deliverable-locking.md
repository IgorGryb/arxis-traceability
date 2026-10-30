# ADR 0002: ISO 19650 Common Data Environment (CDE) Deliverable Locking

- **Status:** Accepted
- **Date:** 2026-10-28
- **Context:** Information Management in Built Assets
- **Deciders:** Igor Grybek (Systems Architect, Arxa Group)

## Context & Problem Statement
In BIM workflows, contractors frequently receive drawing revisions labeled "Draft" or "Work-in-Progress" that are mistakenly used for on-site concrete pours. ISO 19650 mandates clear information containers transitioning across Work in Progress (WIP), Shared, Published, and Archived states.

## Decision Drivers
1. **Immutable Baseline State:** Only documents in the `PUBLISHED` state may be used for physical site operations.
2. **Cryptographic Content Digest:** Every issued sheet or model must carry a SHA-256 digest to prevent unauthorized local edits.
3. **Rejection of Dangling References:** Every deliverable must link to a valid, certified decision.

## Decision Outcome
Chosen Option: **Cryptographic Version-Locked Manifests**.
ARXIS enforces strict admission criteria:
- Any deliverable referencing an unapproved decision is rejected.
- When an engineering revision is published, the prior version is archived and locked.
- Contractors verify field models against the centralized SHA-256 manifest before beginning physical execution.
