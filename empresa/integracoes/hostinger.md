# Integração — Hostinger VPS

## Escopo

Hostinger gerencia as VPS do Grupo Cimino. A VPS `lc.vps` hospeda Docker/Traefik/Hermes/n8n/Paperclip.

## Secrets Doppler

- `HOSTINGER_API_TOKEN`
- `VPS_IP` / `VPS_HOSTNAME`
- secrets SSH/root quando existirem, sem imprimir valores.

## Read-only

- Listar VPS, IPs, status, labels e metadados pela API.
- Via SSH autorizado: `docker ps`, `docker inspect`, `docker logs`, crontab/timers/listagens e leitura de compose/configs com redaction.

## Write

- Alterações em arquivos de documentação locais do Brain são permitidas.
- Alterações na VPS não são rotina: exigem aprovação mesmo se tecnicamente pequenas.

## External-send

- Não aplicável diretamente; alertas enviados a Lucas são permitidos se informativos.

## Admin/destructive

- Root password, SSH access, firewall, DNS, ports, Docker compose, containers, volumes, networks, Traefik, n8n, Paperclip, Hermes, snapshots e rebuilds exigem aprovação explícita + backup/rollback.

## Regra atual

Modo padrão é read-only. A chave SSH dedicada de inventário deve permanecer fora do repo.

## Escala de permissões

- Read-only: consultar metadados, status, listas, métricas e registros sem alterar dados.
- Write: criar/atualizar dados internos, tags, notas, segmentos ou configurações não destrutivas.
- External-send: enviar mensagem, email, campanha, notificação ou contato com cliente/lead/parceiro. Exige preview e aprovação de Lucas.
- Admin/destructive: apagar dados, alterar credenciais, webhooks, domínios, billing, permissões, deploys, containers, produção ou integrações críticas. Exige aprovação explícita, plano de backup e rollback.

Regra de secrets: este arquivo lista apenas nomes de secrets no Doppler `lc-keys/prd`; valores reais nunca entram no GitHub.
