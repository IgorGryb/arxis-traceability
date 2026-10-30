# ADR 0003: RACI Gate Enforcement Prior to Construction Baseline Release

- **Status:** Accepted
- **Date:** 2026-10-28
- **Context:** Project Governance & Contractual Claim Prevention (FIDIC / AIA)
- **Deciders:** Igor Grybek (Systems Architect, Arxa Group)

## Context & Problem Statement
On construction projects, disputes over delay claims and variation orders often arise because an individual engineer verbally agreed to a contractor's change without formal authorization from the discipline lead or project director.

## Decision Drivers
1. **Explicit Role-Based Sign-off:** Sign-offs must strictly match registered professional authority.
2. **Multi-Discipline Consensus:** Changes impacting multiple domains must require concurrent authorization.
3. **Audit Trail for Dispute Defense:** Full non-repudiation under FIDIC contract administration standards.

## Decision Outcome
Chosen Option: **Programmatic RACI Gate Controller**.
The engine verifies that each actor passing an authorization token holds registered authority for the specific discipline (Architectural, Structural, MEP). If an unauthorized actor attempts sign-off, or if expected baseline versions do not match, the workflow halts and logs a security exception.
