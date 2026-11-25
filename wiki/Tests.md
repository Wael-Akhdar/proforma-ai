---
type: module
chemins: ["tests/test_main.py"]
mis_a_jour: 2026-11-23
tags: [tests, pytest]
---
# Tests

**Résumé :** 7 tests [[Pytest]] qui appellent l'API avec le `TestClient` de [[FastAPI]]. Un dict `PROFORMA_VALIDE` sert de base, les variantes sont faites avec `{**PROFORMA_VALIDE, "champ": valeur}`. Lancement : `uv run pytest -v`.

## Contenu
- `test_post_id_ignore` : l'id envoyé par le client n'est pas repris.
- `test_post_puis_get_retrouve_la_proforma` : aller-retour POST puis GET avec l'id renvoyé.
- `test_post_valide_renvoie_201_avec_id` : lit `cpt_id` (détail interne, à remplacer).
- `test_post_montant_negatif_renvoie_422`, `test_post_devise_invalide_renvoie_422`.
- `test_get_proforma1` (dépend des données de départ), `test_get_proforma999` → 404.

## Concepts clés
- Un test = un comportement ; ne pas dépendre de l'ordre d'exécution ; vérifier l'état réel (GET après POST), pas seulement la réponse.
- Import `from app.main import app` grâce à `pythonpath = ["."]` dans le pyproject.

## Relations
- [[API-proformas]] : code testé.
- [[Config-projet]] : config pytest et dépendances de dev (pytest, httpx).
