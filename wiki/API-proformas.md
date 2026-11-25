---
type: module
chemins: ["app/main.py"]
mis_a_jour: 2026-11-23
tags: [api, fastapi]
---
# API proformas

**Résumé :** API [[FastAPI]] qui stocke les proformas dans une liste Python en mémoire (perdue à chaque redémarrage, d'où l'étape [[Postgres]]). Deux exemples de départ (ids 1 et 2) et un compteur global `cpt_id` pour les nouveaux ids. Lancement : `uv run uvicorn app.main:app --reload`, doc interactive sur `/docs`.

## Contenu
- Modèles [[Pydantic]] : `ProformaCreate` (fournisseur, date_emission: date, montant_total: float > 0, devise: Literal EUR/USD/XAF) et `Proforma` (hérite, ajoute `id`).
- `GET /health` → `{"status": "ok"}`.
- `GET /proformas` → la liste.
- `POST /proformas` → 201, id donné par le serveur (`global cpt_id`), l'id envoyé par le client est ignoré.
- `GET /proformas/{id}` → la proforma ou 404 (`HTTPException`).

## Concepts clés
- Validation dans le modèle, pas dans la route : 422 automatique avant l'appel de la fonction.
- À l'étape 2b : remplacer la liste et `cpt_id` par la base ; `montant_total` passera en `NUMERIC`/`Decimal` (pas de float pour l'argent).

## Relations
- [[Tests]] : couvrent chaque route.
- [[Config-projet]] : dépendances fastapi et uvicorn.
- [[Feuille-de-route]] : étapes 1 et 2b.
