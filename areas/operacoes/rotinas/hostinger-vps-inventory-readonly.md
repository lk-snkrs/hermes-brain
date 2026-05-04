# Rotina — Hostinger/VPS Inventory Read-only

Objetivo: inventariar VPS, Docker, Traefik, n8n, Paperclip e Hermes sem modificar produção.

## Integração

- Docs: `empresa/integracoes/hostinger.md`, `areas/tecnologia/contexto/hermes-docker-footprint.md`.
- Secrets: `HOSTINGER_API_TOKEN` e, quando necessário, SSH key dedicada fora do repo.

## Permissões

- Read-only: listar VPS, containers, compose, logs recentes redigidos, crons, timers e status.
- Write: escrever documentação no Brain é permitido; escrever na VPS não é padrão.
- External-send: não aplicável.
- Admin/destructive: restart, stop, rm, compose up/down, prune, volume/network, Traefik, firewall, DNS, root, SSH e deploy exigem aprovação explícita + backup/rollback.

## Procedimento read-only

1. Confirmar alvo: `lc.vps` antes de qualquer comando remoto.
2. Preferir Hostinger API e comandos read-only.
3. Se usar SSH, usar chave dedicada fora do repo.
4. Não imprimir secrets de `.env`, compose ou logs.
5. Registrar achado no Brain com data, fonte e limitações.

## Comandos permitidos por padrão

- `docker ps`
- `docker inspect` com redaction quando necessário
- `docker logs --tail` sem secrets
- `crontab -l`
- `systemctl list-timers`
- leitura de compose/config sem valores sensíveis

## Comandos bloqueados sem aprovação

- `docker stop/rm/kill/restart/prune`
- `docker compose up/down/restart`
- alteração de volumes/networks/Traefik/n8n/Paperclip/Hermes
- alteração de root password, SSH, firewall, DNS ou ports
