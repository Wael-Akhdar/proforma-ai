---
type: dossier
chemins: ["pyproject.toml", "uv.lock", ".python-version", ".gitignore", ".env", "compose.yaml"]
mis_a_jour: 2026-11-23
tags: [config, uv, docker]
---
# Config du projet

**Résumé :** Projet géré par uv en mode application (pas de package : `src/` et `[build-system]` retirés). Python 3.10. Dépôt public `github.com/Wael-Akhdar/proforma-ai`, branche `main`.

## Contenu
- `pyproject.toml` : dépendances `fastapi[standard]`, `uvicorn[standard]` ; groupe dev `pytest`, `httpx` ; `[tool.pytest.ini_options] pythonpath = ["."]`.
- `uv.lock` : versions exactes, commité, jamais édité à la main.
- `.gitignore` : `__pycache__/`, `*.pyc`, `.venv/`, `.env` (corrigé le 2026-11-23, `.env` n'apparaît plus dans `git status`).
- `.env` : variables de [[Postgres]] (secrets, ne jamais lire ni résumer). `.env.example` : mêmes noms, valeurs factices.
- `.dockerignore` : créé, pas encore utile (servira au Dockerfile de l'API).
- `compose.yaml` : v4 lancée le 2026-11-25. `db` (`postgres:17`, port 5432, `env_file: .env`, volume nommé `proforma_data` sur `/var/lib/postgresql/data`) + `adminer` (8080). Docker nomme le volume `proformaai_proforma_data` (préfixe = nom du projet = nom du dossier). Une vingtaine de volumes anonymes (noms en hash) traînent, issus d'anciens lancements : ne pas faire `prune` sans vérifier.
- Non commités au 2026-11-23 : `compose.yaml`, `.env.example`, `.dockerignore`, `wiki/`, `CLAUDE.md`, `.obsidian/`, modif `.gitignore`.

## Relations
- [[API-proformas]], [[Tests]] : utilisent ces dépendances.
- [[Feuille-de-route]] : étape 2a.
