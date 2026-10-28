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

## Granice i źródła

Nie deklarować pełnej integracji narzędzi, engineering sign-off ani wpływu na
realny koszt/harmonogram. Źródła: [dossier zarządcze](MANAGEMENT-DOSSIER.md),
[test report](TEST-REPORT.md), [ADR](adr/ADR-001.md) i
[rejestr pozycji](../../../00.%20ARCHIVE%20SYSTEM/portfolio/CONVEX-POSITION-REGISTER.yaml).
