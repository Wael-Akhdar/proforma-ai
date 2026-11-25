---
type: index
mis_a_jour: 2026-11-23
---
# ProformaAI : index

Projet d'apprentissage de Wael (objectif : Forward Deployed Engineer). API qui reçoit des proformas fournisseurs, puis, à terme, les lit avec un LLM local et mesure la précision par des evals. Wael écrit le code lui-même ; Claude est en [[Mode-tuteur]].

| Note | Chemins | Résumé (1 ligne) |
|---|---|---|
| [[Feuille-de-route]] | — | Les étapes du projet, ce qui est fait et la suite (Postgres, Docker, LLM local, evals). |
| [[API-proformas]] | app/main.py | API FastAPI en mémoire : /health, liste, création et lecture d'une proforma. |
| [[Tests]] | tests/test_main.py | 7 tests pytest avec le TestClient de FastAPI. |
| [[_HANDOFF]] | — | Passation entre sessions : chantier en cours, état, prochaine étape. |
| [[Config-projet]] | pyproject.toml, uv.lock, .python-version, .gitignore, .env, compose.yaml | Dépendances (uv), config pytest, Docker Compose et secrets. |
| [[Mode-tuteur]] | CLAUDE.md | Règles : Claude explique et relit, Wael écrit le code. |
| [[FastAPI]] | — | Framework web, servi par uvicorn (ASGI). |
| [[Pydantic]] | — | Validation des données par les types (Field, Literal, date). |
| [[Pytest]] | — | Tests automatiques, un test par comportement. |
| [[Docker-Compose]] | — | Lancer Postgres (et plus tard l'API) en conteneurs. |
| [[Postgres]] | — | Base de données de l'étape 2. |

## Relations
- [[API-proformas]] utilise [[FastAPI]] et [[Pydantic]] ; testée par [[Tests]] ([[Pytest]]).
- [[Config-projet]] décrit les dépendances de [[API-proformas]] et le `compose.yaml` de [[Docker-Compose]] / [[Postgres]].
- [[Feuille-de-route]] ordonne le travail ; [[Mode-tuteur]] fixe la façon de travailler.

Fichiers non résumés : `.venv/`, `.pytest_cache/`, `__pycache__/`, `.git/` (générés), `uv.lock` (verrou de versions, ne pas lire), `.env` (secrets : jamais lu ni résumé).
