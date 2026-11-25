---
mis_a_jour: 2026-11-25
---
# Passation

## ProformaAI étape 2a (Postgres)
- **Fait :** compose.yaml v4 qui tourne (db 5432 + volume nommé, adminer 8080), `.env` ignoré, `.env.example` créé. Voir [[Config-projet]].
- **État :** commité et poussé (`c723c5c`, message « yaml » trop vague, conseil donné). psql fonctionne (`-U wael -d proforma_ai`), base vide. Mode tuteur : Wael écrit tout, voir [[Mode-tuteur]].
- **Prochaine étape :** table créée, INSERT/SELECT et les 2 CHECK testés (ids 3 et 4 consommés par les échecs). Reste : SELECT après redémarrage (oubli du `;`), ajouter IF NOT EXISTS, commit `sql/`, puis étape 2b. Voir [[Postgres]].
