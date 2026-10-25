# Full project blueprint — ARXIS — Traceable Architecture Documentation Workflow

Stable project ID: `PRJ-ARXIS-PROTOTYPE`  
Status: source-grounded target architecture; implementation and validation backlog  
Evidence boundary: this document specifies what should be built and tested. Only linked test artifacts may support implementation claims.

## 1. Project thesis and decision boundary

The credible near-term value is traceable architectural decision documentation for one residential workflow; CAD/BIM/GIS, simulation, blockchain and broad creative-platform claims remain interfaces or roadmap until independently implemented.

**Decision owner:** architectural project/documentation lead  
**Decision supported:** Whether a requirement, design decision, revision and approval chain is complete enough to proceed without unmanaged coordination, rework or handover risk.

### Users and reviewers

- architect/designer
- project manager
- consultant/engineer
- client reviewer
- document controller

### In scope for the validated portfolio case

- one residential project fixture
- requirement-to-handover traceability
- RFI/revision/approval/change states
- WBS/schedule/cost links
- human-reviewed document classification

### Explicitly outside the validated claim

- full CAD/BIM/GIS integration
- automated professional design approval
- physical simulation validation
- blockchain necessity claim
- verified construction savings

## 2. Layer architecture and operationalization

`Current` is evidence-based maturity now; `target` is the program gate. It is not a claim that the target has been achieved.

### 2.1 problem-user

**Objective:** Focus on one document-control and coordination problem in a residential delivery stage.

**Operationalization:** Define participant, contract/delivery assumptions, current handoffs, authoritative record, approval risk and handover criterion.

**Required artifact:** construction workflow problem brief  
**Acceptance test:** A practitioner confirms the workflow and identifies the most costly missing-decision pattern.  
**Course inputs:** `N-31`, `C419-101`  
**Maturity:** current L2 → target L5  
**Open gap:** Construction course materials are incomplete and practitioner validation is absent.

### 2.2 market-business

**Objective:** Test who pays for traceability and why existing CDE/BIM/document tools are insufficient.

**Operationalization:** Compare status quo, common data environment, BIM issue tools and generic document systems; quantify rework/time as ranges.

**Required artifact:** business case and alternative map  
**Acceptance test:** A buyer/user interview validates priority and rejects unsupported market-size or savings claims.  
**Course inputs:** `N-35`, `C419-195`, `C419-206`  
**Maturity:** current L2 → target L5  
**Open gap:** Existing concept has broad revenue/market claims that require revalidation.

### 2.3 product-service

**Objective:** Deliver one traceable workflow from requirement through handover.

**Operationalization:** Specify role views, decision thread, version comparison, RFI, approval, change impact, completeness dashboard and export.

**Required artifact:** product and service blueprint  
**Acceptance test:** Five role scenarios reach correct authoritative state and reveal missing/conflicting links.  
**Course inputs:** `C419-101`, `C419-179`, `C419-206`  
**Maturity:** current L3 → target L5  
**Open gap:** Current prototype covers a synthetic graph, not full role journeys.

### 2.4 operating-model

**Objective:** Assign ownership and evidence to construction-document transitions.

**Operationalization:** Map RACI, SLA, inputs/outputs and escalation for brief, design review, RFI, revision, approval, change order and handover.

**Required artifact:** document-control runbook  
**Acceptance test:** Tabletop exercise processes a late RFI, superseded issue and unauthorized change without ambiguity.  
**Course inputs:** `N-31`, `N-32`, `C419-101`, `C419-110`  
**Maturity:** current L2 → target L5  
**Open gap:** N-31/N-32 provide only incomplete source packs; actual firm process review is required.

### 2.5 data-technology

**Objective:** Maintain a versioned requirement/decision/artifact graph with controlled access.

**Operationalization:** Define entity/event schemas, provenance, authoritative-version rule, RBAC, change-impact query, classifier boundary and integration contracts.

**Required artifact:** reference architecture and executable trace graph  
**Acceptance test:** Broken links, permission bypass, conflicting versions and rebuild are tested; integrations remain explicit stubs.  
**Course inputs:** `C419-164`, `C419-163`, `C419-179`  
**Maturity:** current L4 → target L5  
**Open gap:** The narrow graph is tested; persistence, access control and realistic document volume are not.

### 2.6 analytical-model

**Objective:** Prioritize review using completeness, change impact and uncertainty without pretending to automate design judgment.

**Operationalization:** Specify rules/classifier, classes, confidence, abstention, cost of errors, manual baseline and change-impact ranking.

**Required artifact:** classification and prioritization evaluation  
**Acceptance test:** Blinded fixture shows acceptable recall/precision and every uncertain recommendation is human-reviewed.  
**Course inputs:** `C419-179`, `C419-190`  
**Maturity:** current L2 → target L5  
**Open gap:** Current rule classifier lacks representative labeled documents.

### 2.7 finance-economics

**Objective:** Connect documentation failures to schedule, rework, contingency and financing exposure as ranges.

**Operationalization:** Model event-to-WBS link, delay distribution, rework cost, contingency use, cash timing, DSCR sensitivity and assumption provenance.

**Required artifact:** cost/schedule/finance impact model  
**Acceptance test:** Sensitivity and practitioner review identify decision-relevant ranges without claiming realized savings.  
**Course inputs:** `N-33`, `N-34`, `C419-195`  
**Maturity:** current L1 → target L5  
**Open gap:** N-33/N-34 archives are incomplete and no project finance fixture is calibrated.

### 2.8 risk-security-compliance

**Objective:** Preserve professional accountability, authorization and records.

**Operationalization:** Define authoritative document, approval rights, retention, client confidentiality, audit event, AI rejection conditions and regulatory questions.

**Required artifact:** information governance and AI-assist policy  
**Acceptance test:** Unauthorized changes fail, audit trail reconstructs decisions and practitioner reviews accountability boundaries.  
**Course inputs:** `C419-163`, `C419-190`  
**Maturity:** current L2 → target L5  
**Open gap:** No project-specific regulatory/contractual review or RBAC implementation.

### 2.9 delivery-governance

**Objective:** Control roadmap scope and prevent interface claims becoming implementation claims.

**Operationalization:** Use ADRs, capability status register, release gates, change board, issue ownership and post-mortem.

**Required artifact:** delivery governance and capability register  
**Acceptance test:** A proposed CAD/BIM integration is routed through evidence, ADR and interface test without being marked implemented.  
**Course inputs:** `C419-101`, `C419-110`, `C419-179`  
**Maturity:** current L3 → target L5  
**Open gap:** Current documentation mixes far-future vision with near-term prototype boundaries.

### 2.10 evidence-validation-publication

**Objective:** Publish the narrow validated traceability case and disclose broader roadmap.

**Operationalization:** Link claims to fixture, tests, reviewer notes, source completeness, interface status and limitations.

**Required artifact:** validated residential case study  
**Acceptance test:** Claim audit removes unsupported integration, award, market and savings statements; user approves final story.  
**Course inputs:** `C419-110`, `C419-206`  
**Maturity:** current L2 → target L6  
**Open gap:** Existing snapshot requires source and claim correction before publication.

## 3. Operating state model

### Normal states

`brief captured → requirement approved → design option created → decision proposed → RFI/open issue → consultant response → revision issued → approval or rejection → change order → construction release → as-built/handover → closed`

Every transition must record actor, timestamp, input state, output state, decision/evidence reference and exception reason when applicable.

### Required exception paths

- missing approval
- conflicting revision
- superseded drawing used
- orphan requirement
- late RFI
- unauthorized change
- classifier uncertainty
- schedule/cost impact unknown

## 4. Technical and quality envelope

### Non-functional requirements

- authoritative version visible
- immutable provenance event
- role-based approval
- change impact query
- human review of AI classification
- exportable handover record
- interfaces do not imply integration

### Metrics tree

- traceability coverage
- orphan artifacts
- approval cycle time
- late or conflicting revisions
- RFI age
- change impact completeness
- modeled rework/delay exposure
- reviewer correction of classifier

Metrics must be tagged as observed, modeled or estimated. Modeled economic impact cannot be presented as realized impact.

## 5. Falsifiable hypotheses

1. A typed requirement-decision-artifact graph will expose missing or conflicting links before handover review.
2. Linking document changes to WBS, schedule and cost ranges makes review priority more useful than completeness alone.
3. A human-reviewed classifier reduces triage effort without transferring professional approval authority to AI.

A test that cannot refute a hypothesis is practice or demonstration, not validation.

## 6. Experiment sequence

1. Create a realistic residential fixture with deliberately incomplete, superseded and conflicting records.
2. Compare manual checklist and graph-based traceability on detection, time and false positives.
3. Add WBS, critical-path and cost-impact ranges; ask a practitioner to rank action priority.
4. Measure classifier accuracy and reviewer corrections while enforcing abstention for uncertain classes.

The prediction, threshold and interpretation owner must be recorded before each result. Failed or inconclusive tests remain in the evidence bundle.

## 7. Source-to-practice coverage

| Mapping | Layer | Course | Archive state | Practice/test | Evidence target |
|---|---|---|---|---|---|
| PRJSRC-0039 | operations | N-31 — Construction Management k.1: Construction Project Management | manifest-incomplete | map roles and delivery method into workflow | stakeholder/service blueprint |
| PRJSRC-0040 | operations | N-32 — Construction Management k.2: Construction Scheduling | manifest-incomplete | link decisions and artifacts to schedule activities | schedule traceability test |
| PRJSRC-0041 | finance-risk | N-33 — Construction Management k.3: Construction Cost Estimating and Cost Control | manifest-incomplete | map document changes to cost exposure | cost-impact model |
| PRJSRC-0042 | finance-risk | N-34 — Construction Management k.4: Construction Finance | manifest-incomplete | create project-finance assumptions sheet | finance appendix |
| PRJSRC-0043 | business | N-35 — Construction Management k.5: The Construction Industry: The Way Forward | manifest-incomplete | frame value proposition and market constraints | business case |
| PRJSRC-0044 | technology | C419-179 — Generative AI: Advancing Systems Analysis & Architecture | manifest-complete | formalize requirements and interface boundaries | architecture specification |
| PRJSRC-0045 | technology | C419-164 — Modern Data Architecture Fundamentals with Microsoft Fabric | manifest-complete | select storage and lineage pattern | architecture decision record |
| PRJSRC-0046 | governance | C419-163 — Microsoft Fabric: Data Governance, Security, and Analytics | manifest-complete | define document classification and RBAC | governance policy |
| PRJSRC-0047 | operations | C419-101 — Introduction to Project Management | manifest-complete | define gates and owners | delivery runbook |
| PRJSRC-0048 | operations | C419-110 — Project Management Capstone | manifest-complete | execute an end-to-end review scenario | validated demo |
| PRJSRC-0049 | business | C419-206 — Building Powerful Reports and Dashboards in Power BI | manifest-complete | build completeness and issue dashboard | review surface |
| PRJSRC-0050 | governance | C419-190 — AI Strategy and Governance | manifest-complete | define classifier accountability | AI-assist policy |
| PRJSRC-0051 | finance-risk | C419-195 — Financial Acumen for Non-Financial Managers | manifest-complete | translate delay/rework scenarios into statements | impact memo |

All rows above currently mean source routing. They become competence evidence only after the stated practice/test is executed and recorded.

## 8. Artifact backlog and gates

| Artifact ID | Layer | Deliverable | Current → target | Definition of Done |
|---|---|---|---:|---|
| ART-ARXIS-01 | problem-user | construction workflow problem brief | L2 → L5 | A practitioner confirms the workflow and identifies the most costly missing-decision pattern. |
| ART-ARXIS-02 | market-business | business case and alternative map | L2 → L5 | A buyer/user interview validates priority and rejects unsupported market-size or savings claims. |
| ART-ARXIS-03 | product-service | product and service blueprint | L3 → L5 | Five role scenarios reach correct authoritative state and reveal missing/conflicting links. |
| ART-ARXIS-04 | operating-model | document-control runbook | L2 → L5 | Tabletop exercise processes a late RFI, superseded issue and unauthorized change without ambiguity. |
| ART-ARXIS-05 | data-technology | reference architecture and executable trace graph | L4 → L5 | Broken links, permission bypass, conflicting versions and rebuild are tested; integrations remain explicit stubs. |
| ART-ARXIS-06 | analytical-model | classification and prioritization evaluation | L2 → L5 | Blinded fixture shows acceptable recall/precision and every uncertain recommendation is human-reviewed. |
| ART-ARXIS-07 | finance-economics | cost/schedule/finance impact model | L1 → L5 | Sensitivity and practitioner review identify decision-relevant ranges without claiming realized savings. |
| ART-ARXIS-08 | risk-security-compliance | information governance and AI-assist policy | L2 → L5 | Unauthorized changes fail, audit trail reconstructs decisions and practitioner reviews accountability boundaries. |
| ART-ARXIS-09 | delivery-governance | delivery governance and capability register | L3 → L5 | A proposed CAD/BIM integration is routed through evidence, ADR and interface test without being marked implemented. |
| ART-ARXIS-10 | evidence-validation-publication | validated residential case study | L2 → L6 | Claim audit removes unsupported integration, award, market and savings statements; user approves final story. |

### External validation required

- architect/construction practitioner workflow review
- document-control or BIM coordinator review
- construction finance assumptions review

## 9. Integrated delivery sequence

1. Confirm problem, decision owner, user and anti-scope; record the user's own explanation.
2. Freeze approved sources/data and record hashes, permissions and proxy limitations.
3. Pre-register hypotheses, predictions, thresholds, alternatives and falsification conditions.
4. Complete guided practice from the selected courses and save its independent output.
5. Implement the vertical slice with explicit normal and exception states.
6. Compare against baseline; run negative, security, data-quality and sensitivity tests.
7. Review business, operations, finance and governance artifacts with the appropriate role.
8. Correct model, assumptions, dependent documents and evidence manifests.
9. Ask the user to interpret the result and choose continue, pause, pivot, stop or complete.
10. Only after acceptance, regenerate case study, PDF and private web version and run a claim audit.

## 10. Publication claim boundary

Allowed now: the narrow technical baseline exists and its local tests passed.  
Not allowed now: production readiness, market adoption, realized economic impact, legal compliance, client result or broad platform implementation.  
Allowed later: only statements backed by a versioned artifact, test result, reviewer record and evidence-manifest entry.

## 11. User gates

The user participates before irreversible narrowing, before a material test, when interpreting the result and before publication. The minimum prompts are:

- explain the problem and expected mechanism in your own words;
- predict the result and name a falsifying observation;
- interpret differences between baseline, model and judgment;
- choose `continue`, `pause`, `pivot`, `stop` or `complete`;
- state what changed in your understanding.
