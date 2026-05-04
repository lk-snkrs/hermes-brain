# Hermes — footprint Docker na VPS LC

Última inspeção read-only: 2026-05-04.

## Resumo

O Hermes roda em Docker na VPS `lc.vps`, mas o estado persistente dele não fica apenas dentro da imagem/container. A configuração atual usa volume bind mount:

```text
host:      /docker/hermes-agent-5ajw/data
container: /opt/data
```

Interpretação operacional:

- Runtime/processos do Hermes: containers Docker.
- Imagem: `ghcr.io/hostinger/hvps-hermes-agent:latest`.
- Dados persistentes/configuração/repos: diretório do host montado em `/opt/data` dentro dos containers.
- Alterar arquivos em `/opt/data` no ambiente Hermes altera arquivos persistentes no host em `/docker/hermes-agent-5ajw/data`.
- Isso é esperado: permite persistência entre recriações/restarts de container sem gravar na camada imutável da imagem.

## Containers verificados

| Container | Função observada | Estado observado |
|---|---|---|
| `hermes-agent-5ajw-hermes-agent-1` | Serviço web/ttyd/API Hermes, porta interna `4860` | Rodando; host `32771 -> 4860/tcp` |
| `hermes-agent-5ajw-hermes-telegram-1` | Gateway Telegram | Rodando; comando `cd /opt/hermes && exec hermes gateway run` |

Ambos usam a mesma imagem `ghcr.io/hostinger/hvps-hermes-agent:latest` e montam `./data:/opt/data`.

## Compose

Diretório compose observado:

```text
/docker/hermes-agent-5ajw/docker-compose.yml
```

Serviços observados:

- `hermes-agent`
- `hermes-telegram`

Redes observadas:

- `hermes-agent-5ajw_default`
- `n8n-vdgm_default` — conectada ao serviço `hermes-agent`.
- `paperclip-qrlt_default` — conectada ao serviço `hermes-agent`.

## Outros apps Docker na mesma VPS

Também existem containers de outros apps:

- `n8n-vdgm-n8n-1`
- `paperclip-qrlt-paperclip-1`
- `traefik-traefik-1`

Regra: não alterar/remover/recriar containers, compose, volumes, redes, Traefik, n8n, Paperclip, SSH/root ou firewall sem aprovação explícita Lucas e plano de backup/rollback.

## Operações permitidas por padrão

Somente leitura/inventário:

- `docker ps`
- `docker inspect`
- `docker logs` com cuidado para não expor secrets
- leitura de compose/config redigindo secrets
- `crontab -l`, `/etc/cron*`, systemd timers
- documentação no Hermes Brain

## Operações bloqueadas sem aprovação explícita

- `docker compose up/down/restart`
- `docker stop/rm/kill/prune`
- remover volumes/redes
- alterar `/docker/*`
- alterar Traefik/n8n/Paperclip/Hermes em produção
- alterar root password, SSH, firewall, DNS ou portas
- criar workflow/cron ativo que impacte produção

## Observação de segurança

A chave SSH dedicada usada para inventário fica fora do repo:

```text
/opt/data/hermes_bruno_ingest/ssh_keys/hermes_cron_inventory_ed25519
```

Nunca commitar chave privada nem valores de secrets. Doppler `lc-keys/prd` segue como fonte de verdade para credenciais.

## Observabilidade runtime — 2026-05-04

Consulta read-only complementar documentada em `../../operacoes/rotinas/hermes-runtime-observability.md`.

Achados principais:

- Containers Hermes estavam rodando.
- Runtime Docker Hostinger reportou Hermes Agent v0.9.0 (2026.4.13).
- Release upstream consultada no GitHub: Hermes Agent v0.12.0 (`v2026.4.30`).
- `hermes cron list` mostrou job `Hermes release watch` ativo.
- `hermes cron status` reportou `Gateway is not running`, apesar de existir processo `hermes gateway run` como processo principal do container Telegram.
- Logs mostraram warning de conflito de polling Telegram.

Interpretação: há warning operacional e gap de versão, mas nenhuma correção/restart/update deve ser feita sem aprovação explícita Lucas e plano de rollback.

