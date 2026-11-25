---
type: concept
mis_a_jour: 2026-11-23
tags: [tech, docker]
---
# Docker Compose

**Résumé :** Un fichier `compose.yaml` décrit les conteneurs (services), leurs ports, variables d'environnement et volumes ; `docker compose up -d` les lance, `down` les arrête, `down -v` supprime aussi les volumes. Image = modèle, conteneur = image en cours d'exécution, volume = données gardées hors du conteneur. Doc : docs.docker.com/compose (référence du fichier : docs.docker.com/reference/compose-file).

## Relations
- [[Postgres]] : premier service.
- [[Config-projet]] : `compose.yaml`, `.env`.
