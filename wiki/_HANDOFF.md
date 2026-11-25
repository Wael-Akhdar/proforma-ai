---
mis_a_jour: 2026-11-25
---
# Passation

## ProformaAI étape 2a (Postgres)
- **Fait :** compose.yaml v4 qui tourne (db 5432 + volume nommé, adminer 8080), `.env` ignoré, `.env.example` créé. Voir [[Config-projet]].
- **État :** rien de commité depuis `2677aff` (compose, .env.example, .dockerignore, wiki, CLAUDE.md, .obsidian). Mode tuteur : Wael écrit tout, voir [[Mode-tuteur]].
- **Prochaine étape :** commit, puis psql : table `proformas` (IDENTITY, NUMERIC), 2 INSERT, SELECT, test de persistance `down`/`up` puis `down -v`. Voir [[Feuille-de-route]].
