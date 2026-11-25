---
type: concept
mis_a_jour: 2026-11-23
tags: [tech, sql]
---
# Postgres

**Résumé :** Base de données relationnelle de l'étape 2, image officielle `postgres:17` (variables `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB` ; données dans `/var/lib/postgresql/data`). Ids générés par la base (`GENERATED ALWAYS AS IDENTITY`), montants en `NUMERIC`. Client en ligne de commande : `psql`.

## Dans le projet
- `sql/001_create_proformas.sql` (2026-11-25) : table `proformas` (id IDENTITY, fournisseur TEXT, date_emission DATE, montant_total NUMERIC(20,2) CHECK > 0, devise TEXT CHECK IN ('EUR','USD','XAF')). Exécution : `docker compose exec -T db psql -U wael -d proforma_ai < sql/001_create_proformas.sql`.
- Pièges vus : virgule manquante entre colonnes (l'erreur pointe la ligne suivante) ; `'texte'` (apostrophes) ≠ `"nom"` (guillemets = identifiant).

## Relations
- [[Docker-Compose]] : la fait tourner.
- [[API-proformas]] : remplacera la liste en mémoire.
