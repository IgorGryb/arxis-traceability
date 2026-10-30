# ARXIS — Architecture Traceability & Change Governance Platform

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![CI](https://github.com/IgorGryb/arxis-traceability/actions/workflows/ci.yml/badge.svg)](https://github.com/IgorGryb/arxis-traceability/actions)
[![Tests](https://img.shields.io/badge/Tests-Passing%20(7%2F7)-success.svg)](tests/)
[![Architecture](https://img.shields.io/badge/Architecture-Dependency%20DAG-orange.svg)](#solution--decision-architecture)
[![OpenAPI 3.1](https://img.shields.io/badge/OpenAPI-3.1%20Contract-green.svg)](api/openapi.yaml)
[![ADRs](https://img.shields.io/badge/ADR-Architecture%20Decisions-purple.svg)](docs/adr/)
[![Status](https://img.shields.io/badge/Status-R%26D%20Reference%20Architecture-informational.svg)](#research-integrity--disclaimer)

> **Architectural Mission:** Eliminating costly clash rework and uncoordinated change orders in complex capital projects by mapping multi-disciplinary engineering dependencies into a Directed Acyclic Graph (DAG) with rigorous authorization gates.

---

## Executive Overview

| Dimension | Specification |
|:---|:---|
| **Domain** | AEC (Architecture, Engineering & Construction), Systems Traceability & Governance |
| **Stage** | Validated Proprietary Architecture & Decision Engine (R&D Prototype) |
| **Target User** | Project Directors, Engineering Leads, General Contractors, Infrastructure Asset Owners |
| **Core Decision** | Authorizing, gating, and cascading multi-disciplinary design and engineering modifications |
| **Key Metric** | Downstream Rework Reduction, Change-Propagation Latency, Authority Verification Rate |
| **Architecture Lead** | Igor Grybek (Product Engineering, Systems Analysis, IP Architecture) |

---

## The Strategic Problem

Large-scale infrastructure and complex architectural projects involve hundreds of specialized stakeholders spanning architectural, structural, civil, mechanical, electrical, and plumbing (MEP) disciplines. As projects progress from conceptual design to on-site execution, engineering modifications are inevitable.

However, the industry suffers from severe governance fragmentation:
1. **Uncontrolled Change Propagation:** A localized modification in one discipline (e.g. ductwork routing or structural beam sizing) frequently propagates silently across connected systems, causing physical clashes, code non-compliance, and catastrophic on-site rework.
2. **Disconnected Requirements and Artifacts:** High-level regulatory and client requirements exist in static text documents, completely detached from dynamic BIM models, engineering spreadsheets, and submittal logs.
3. **Diffused Authorization:** Change approvals are dispersed across informal emails, meeting notes, and conflicting drawing revisions, leaving project directors unable to audit who authorized a change, why it was made, or what downstream cost and schedule exposure it generated.

In mega-projects, uncoordinated design changes account for up to 10–15% of total construction cost overruns.

---

## Solution & Decision Architecture

ARXIS provides a centralized, deterministic traceability graph and change-governance engine that enforces rigorous authorization gates before design modifications can cascade into production.

```
[Requirement / Client Brief] ──► [System Requirements Graph]
                                           │
                                           ▼
[Proposed Engineering Change] ──► [Impact Analysis Engine]
                                           │
                                           ▼
             [Dependency Matrix: Structural, MEP, Civil, Cost]
                                           │
                                           ▼
             [Exposure Calculation: Budget, Schedule & Permitting]
                                           │
                             ┌─────────────┴─────────────┐
                             ▼                           ▼
                   [Authorized Gate Pass]      [Blocked / Escalated]
                             │                           │
                             ▼                           ▼
                 [Immutable Release Log]     [Resolution Workshop]
```

### Core System Mechanics:
1. **Multi-Disciplinary Dependency Graph:** Maps all project artifacts (BIM models, structural calculations, procurement specifications, municipal permits) into a directed acyclic graph (DAG), explicitly capturing functional and spatial dependencies.
2. **Automated Impact Analysis:** When an engineering team proposes a modification, ARXIS traverses the dependency graph to instantly identify all affected drawing sets, regulatory constraints, and downstream procurement orders.
3. **Strict Authorization Gates (RACI Enforcement):** Implements an explicit, multi-level sign-off workflow where changes cannot be committed to shared project baselines without verified sign-offs from impacted discipline leads and budget owners.
4. **Tamper-Evident Audit Trail:** Explores cryptographic hashing and event-logging to anchor milestone approvals into an immutable audit trail, resolving contractor liability disputes.

---

## 5-Dimensional Management Model

### 1. Technical Architecture
- **Graph Core:** Python (NetworkX) and directed graph structures modeling complex hierarchical dependencies across building systems.
- **Traceability Classifier:** Automated rule-based engine classifying revisions into minor adjustments, major coordinate alterations, and critical structural changes.

### 2. Operating Model & Change Control
- **RACI Governance:** Strict role segregation: Requestor, Impacted Lead Reviewer, Compliance Officer, and Authorizing Project Director.
- **Clash Resolution:** Eliminates informal approvals by routing conflicting cross-disciplinary requests to structured resolution gates.

### 3. Financial & Unit Economics
- **Quantified Rework Avoidance:** Bounded synthetic validation demonstrates that resolving cross-disciplinary change conflicts during digital modeling delivers a 10x cost advantage over resolving the same conflict during physical on-site assembly.
- **Coordination Cost Optimization:** Automated impact analysis reduces multidisciplinary change evaluation cycles from days to minutes.

### 4. Risk, Governance & Quality
- **Version Immutability:** Deprecates obsolete revisions immediately upon release of an approved baseline, eliminating the risk of contractors working from superseded drawing packages.
- **Zero Silent Modification:** Every parameter alteration requires a documented justification, source tag, impact assessment, and identified accountability owner before release.

### 5. Venture & Enterprise Integration
- Designed for integration with enterprise Project Management and CDE (Common Data Environment) suites.

---

## Reproducibility & Quickstart

The repository contains an automated test suite verifying dependency links, authority validation, and circular dependency rejection.

```bash
# Clone repository
git clone https://github.com/IgorGryb/arxis-traceability.git
cd arxis-traceability

# Run verification suite (7 tests)
python3 -m unittest discover -s tests -v
# Alternatively:
make test
```

Expected output:
```text
test_authority_and_version (test_core.TraceabilityTest) ... ok
test_broken_fixture (test_core.TraceabilityTest) ... ok
test_classifier_discloses_review (test_core.TraceabilityTest) ... ok
test_complete_fixture (test_core.TraceabilityTest) ... ok
test_duplicate_and_dangling_rejected (test_core.TraceabilityTest) ... ok
test_every_decision_needs_artifact (test_core.TraceabilityTest) ... ok
test_reproduction_writes_results_and_manifest (test_reproduction.ReproductionTest) ... ok

----------------------------------------------------------------------
Ran 7 tests in 0.003s

OK
```

---

## Research Integrity & Disclaimer

This repository is an architectural reference prototype and bounded decision model developed by Igor Grybek. All tests and demonstrations operate strictly on reproducible, synthetic project metadata and documents. No proprietary or confidential corporate data from historical engagements is contained herein.
