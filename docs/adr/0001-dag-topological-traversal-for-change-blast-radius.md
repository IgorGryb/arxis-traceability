# ADR 0001: Directed Acyclic Graph (DAG) for Change Blast Radius Traversal

- **Status:** Accepted
- **Date:** 2026-10-28
- **Context:** AEC Capital Projects Dependency Governance (ISO 19650)
- **Deciders:** Igor Grybek (Systems Architect, Arxa Group)

## Context & Problem Statement
Large construction projects coordinate architectural drawings, structural calculations, and MEP services across dozens of independent consultants. When a client modifies a floor layout or room occupancy requirement, determining which technical drawings and calculation packages are impacted is traditionally done through manual spreadsheet logs or email announcements. Unnoticed dependencies lead to design desynchronization and expensive physical site clashes (e.g. drilling ductwork through post-tensioned slabs).

## Decision Drivers
1. **Mathematical Completeness:** The system must compute the exact transitive closure of all downstream impacted entities.
2. **Cycle Prevention:** Multi-disciplinary engineering dependencies must never form cyclical feedback loops without resolution.
3. **Deterministic Blast Radius:** Fast topological calculation of affected deliverables.

## Decision Outcome
Chosen Option: **Directed Acyclic Graph (DAG) with Kahn's Algorithm / Topological Sort**.
The project model is structured as a 4-tier DAG:
$$\mathcal{G} = (\mathcal{V}, \mathcal{E}), \quad \mathcal{V} = \mathcal{V}_{\text{REQ}} \cup \mathcal{V}_{\text{DEC}} \cup \mathcal{V}_{\text{ART}} \cup \mathcal{V}_{\text{ECR}}$$
When a change request ($v \in \mathcal{V}_{\text{ECR}}$) is submitted targeting node $u$:
- A Breadth-First / Depth-First search calculates the reachable subgraph $\mathcal{R}(u) = \{ w \in \mathcal{V} \mid u \rightsquigarrow w \}$.
- All nodes in $\mathcal{R}(u)$ are atomically tagged as `PENDING_REEVALUATION`.
- Kahn's algorithm validates acyclicity; cyclical dependencies trigger an immediate hard error.

### Positive Consequences
- Guarantees 100% dependency coverage.
- Prevents uncoordinated site work by freezing downstream drawings until re-certified.

