---
type: projet
chemins: []
mis_a_jour: 2026-11-23
tags: [plan, fde]
---
# Feuille de route

**Résumé :** ProformaAI reprend le problème du stage de Wael chez Prometal (saisie des proformas fournisseurs) en version publique, avec des données fictives. Il sert à travailler 3 sujets choisis après l'échange avec un FDE de onepoint : applications LLM et evals, industrialisation de l'IA (gateway, observabilité), IA en local. GPU : RTX 4070 Laptop, 8 Go de VRAM.

## Étapes
- 1 ✅ API en mémoire, validation Pydantic ([[API-proformas]]).
- 1.5 ✅ Tests pytest ([[Tests]]). Restes : ajouter `GET /proformas/999` → 404 au test de l'id ignoré ; remplacer le test qui lit `cpt_id` par deux POST (le 2e id plus grand).
- 2a ⏳ (en cours) [[Postgres]] dans [[Docker-Compose]], manipulation en SQL à la main, test de persistance avec et sans volume.
- 2b Brancher l'API sur Postgres (l'id est généré par la base, `cpt_id` disparaît).
- 3 Upload de PDF et extraction du texte (pdfplumber).
- 4 Extraction des champs par un LLM local (Ollama), sortie JSON validée par [[Pydantic]].
- 5 Evals : 30 proformas fictives, précision par champ, modèle local contre Claude.
- 6 Gateway LLM (LiteLLM) et observabilité (Langfuse auto-hébergé).
- 7 Interface, démo vidéo, README en étude de cas (anglais).
- Bonus : servir le modèle avec vLLM.

## Concepts clés
- Jamais de données réelles de Prometal dans ce dépôt public.
- Planning quotidien : 30 min NeetCode sans IA, 45 min cours Claude API, 45 min ProformaAI.

## Relations
- [[Mode-tuteur]] : façon de travailler sur chaque étape.
- [[Config-projet]] : fichiers touchés à l'étape 2.
