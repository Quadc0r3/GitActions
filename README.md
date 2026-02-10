# GitActions Demo - Automatisierung mit GitHub Actions

Dieses Projekt demonstriert die Mächtigkeit von GitHub Actions für Python-Projekte. Es automatisiert das Testen, die Dokumentation und die Sicherheit deines Codes.

## Features

1.  **Automatische Testfall-Generierung**: Bei jedem Push in den `src/`-Ordner prüft ein Workflow, ob für neue Python-Dateien bereits Test-Skelette in `tests/` existieren. Falls nicht, werden diese automatisch erstellt und committet.
2.  **Unit Tests**: Bei jedem Commit werden alle Tests im `tests/`-Ordner mit `pytest` ausgeführt.
3.  **Automatische Dokumentation**: Die Datei `DOKU.md` wird automatisch aus den Docstrings deines Codes generiert und aktuell gehalten.
4.  **Security Checks**:
    *   **Bandit**: Scant den Code auf bekannte Sicherheitslücken (z.B. unsichere Funktionsaufrufe).
    *   **Safety**: Prüft installierte Abhängigkeiten auf bekannte Schwachstellen.

## Projektstruktur

- `src/`: Dein Programmcode.
- `tests/`: Deine Unit Tests (werden teils automatisch generiert).
- `scripts/`: Hilfsskripte für die Automatisierung.
- `.github/workflows/`: Die Konfigurationsdateien für die GitHub Actions.
- `DOKU.md`: Die automatisch generierte Dokumentation.

## Wie es funktioniert

### CI Workflow (`ci.yml`)
Läuft bei jedem `push` oder `pull_request`.
- Installiert Abhängigkeiten.
- Führt `pytest` aus.
- Führt `bandit` für Code-Sicherheit aus.
- Führt `safety` für Dependency-Sicherheit aus.

### Automation Workflow (`automation.yml`)
Läuft bei jedem `push`, der Änderungen im `src/`-Verzeichnis enthält.
- Generiert Test-Skelette für neue Funktionen.
- Aktualisiert die `DOKU.md`.
- **Commit & Push**: Schreibt die Änderungen automatisch zurück in dein Repository.

## Voraussetzungen
Stelle sicher, dass die GitHub-Aktionen Schreibrechte haben (`Settings > Actions > General > Workflow permissions > Read and write permissions`).
