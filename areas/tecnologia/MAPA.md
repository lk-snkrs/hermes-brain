# Tecnologia — Mapa

Escopo: VPS, Docker, GitHub, Doppler, Supabase, scripts, integrações técnicas.

## Contexto operacional

- [Hermes — footprint Docker na VPS LC](contexto/hermes-docker-footprint.md): runtime em containers, dados persistentes em volume bind mount `/docker/hermes-agent-5ajw/data` → `/opt/data`, e regras de proteção para não afetar root/Docker/outros apps.

## Regra de segurança

Por padrão, operações em VPS/Docker são read-only. Alterações em containers, compose, volumes, redes, Traefik, n8n, Paperclip, SSH/root, firewall, DNS ou portas exigem aprovação explícita Lucas e plano de backup/rollback.
