# ARXIS — karta systemu decyzyjnego

ID: `PXP-PRJ-ARXIS`  
Status: prywatne studium traceability i governance; nie pełna integracja CAD/BIM/GIS ani autoryzacja inżynierska.

## Znaczenie dla decyzji

ARXIS organizuje wymagania, decyzje, wersje i artefakty tak, aby wpływ zmiany
był przypisany do właściciela, kosztu, harmonogramu i przekazania. Główny
wektor: aktywa/infrastruktura/technologia; wzmacniające: dane/dowód i operacje.

## Mapa systemu

`requirement → evidence → decision right → versioned artifact → impact on
deliverable/schedule/cost → exception/escalation → review`.

## Dowód i wkład

Pakiet zawiera model traceability, role, decyzje architektoniczne, test
kompletności i ograniczenia. Wkład formalizuje widoczność zależności i authority
w procesie zmiany; nie potwierdza wykonania projektu budowlanego.

## Model i hipoteza integracji

Mechanizm wiąże dokumentację i wersjonowanie z decyzjami, kosztami oraz
harmonogramem. Hipoteza: traceable review może wykryć zależność wcześniej niż
nieustrukturyzowana lista plików, pod warunkiem pełności coverage i poprawnego
classification. Koszt utrzymania i błędna klasyfikacja pozostają ryzykiem.

## Test i następna opcja

Najtańszy test porównuje file-list review z traceable change review na tym
samym syntetycznym zbiorze zmian, w tym brakujących i błędnie sklasyfikowanych
dokumentach. Następnie można dodać jedną klasę dokumentów.

## Rdzeń biznesowy i standard architektury

**Wizja ze źródła (koncepcja historyczna):** A collaborative architectural-design environment for developing, explaining and coordinating concepts across people and disciplines.

**Pierwsze ograniczone zastosowanie:** One project change: trace requirement, decision, document version, reviewer and schedule/cost consequence against a simple file-list baseline.

**Model komercyjny (hipoteza):** A team or project subscription for architecture practices, with onboarding and migration cost explicit; adoption and price are unvalidated.

**Jednostki i czynniki ekonomiczne:** hours per change and review; rework and delay exposure; document maintenance; onboarding and integration cost; team subscription hypothesis.

**Wykonany zakres:** A small synthetic requirement-to-decision traceability prototype; no CAD/BIM/GIS integration.

**Architektura referencyjna (projekt, bez wdrożenia):** Versioned documents, structured metadata, dependency tracking, role-based approvals, audit logs and exchange interfaces.

**Opcje odroczone:** CAD/BIM/GIS connectivity, multimodal AI, simulation, blockchain provenance and creator marketplace.

| Model | Zastosowanie w tym przypadku |
|---|---|
| Techniczny | Versioned requirement/decision/artifact records and impact queries. |
| Biznesowy i produktowy | Collaborative design-governance subscription hypothesis with a narrow change-review entry point. |
| Operacyjny | Design owner, discipline reviewer and project sponsor retain explicit approval rights. |
| Finansowy | Model review effort, rework, delay and contingency as scenarios rather than savings. |
| Ryzyko i governance | Check broken links, conflicting versions, permissions and engineering-authority boundaries. |

**Źródła rozwoju:** Columbia University — Construction Management (`recorded_completed`); IBM — IBM Systems Analyst (`recorded_completed`); Microsoft — Microsoft Data Architecture for Modern Data Stacks (`recorded_completed`); Stanford Online — From Product Strategy to Product Leadership (`recorded_completed`). Są to odnotowane ukończenia programów i kandydackie połączenia zastosowań; nie stanowią samodzielnego dowodu wdrożenia lub biegłości. **Metody z zapisanym zakresem odczytu:** `M-SIPOC`, `M-RACI`, `M-MOSCOW`, `M-FEASIBILITY`, `M-MEASURE`.

## Granice i źródła

Nie deklarować pełnej integracji narzędzi, engineering sign-off ani wpływu na
realny koszt/harmonogram. Źródła: [dossier zarządcze](MANAGEMENT-DOSSIER.md),
[test report](TEST-REPORT.md), [ADR](adr/ADR-001.md) i
[rejestr pozycji](../../../00.%20ARCHIVE%20SYSTEM/portfolio/CONVEX-POSITION-REGISTER.yaml).
