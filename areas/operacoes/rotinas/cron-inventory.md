# Inventário de Crons — Hermes / VPS

> LEGACY SNAPSHOT — inventário histórico de 2026-05-04. Não é fonte viva para crons atuais. Para controle atual, usar `areas/operacoes/rotinas/cron-control-plane.md` + `cronjob(action='list')`. Comandos de inspeção de host, paths `/root` e achados de VPS abaixo são evidência histórica e não autorização para executar ações em host/Docker/SSH sem aprovação explícita.

Data da última tentativa de verificação: 2026-05-04.

## Objetivo

Mapear quais rotinas documentadas no Hermes Brain estão realmente ativas, pausadas, legadas ou desconhecidas nos ambientes operacionais.

## Ambientes verificados

### Hermes cron local/gateway desta sessão

Status: verificado.

| Job | Schedule | Entrega | Estado | Próxima execução |
|---|---|---|---|---|
| Hermes release watch | `0 9 * * 1` | origin | scheduled | 2026-05-11 09:00 UTC |

Função: verificar semanalmente releases do Hermes Agent e avaliar novidades aplicáveis ao Hermes Brain.

### Hostinger API

Status: verificado parcialmente via API, sem expor token.

VPS encontradas:

| ID | Hostname | IP | Estado | Template |
|---:|---|---|---|---|
| 1331756 | lc.vps | 72.60.150.124 | running | Ubuntu 24.04 with Docker and Traefik |
| 1600060 | evo.lc | 187.127.10.158 | running | Ubuntu 25.10 |

### SSH na VPS

Status: resolvido para `lc.vps` após senha root fornecida pelo Lucas e instalação de chave pública dedicada.

Tentativas iniciais realizadas sem persistir credenciais:

- hosts: `72.60.150.124`, `187.127.10.158`;
- usuários testados: `root`, `hermes`, `ubuntu`, `admin`, `debian` conforme aplicável;
- credenciais históricas testadas via Doppler foram descontinuadas para este fluxo; não usar senha ou helper de senha SSH para inventário;
- resultado histórico: `Permission denied (publickey,password)`.

Conclusão inicial: as credenciais SSH disponíveis no Doppler não autenticavam nas VPS atuais.

Acesso atual: `root@72.60.150.124` via chave local dedicada `hermes-cron-inventory-2026-05-04`, instalada em `authorized_keys`. A senha root enviada em chat foi usada apenas para instalar a chave e não foi salva/commitada. Recomenda-se rotação da senha root após concluir esta sequência.

### Tentativa de chave SSH via Hostinger

Status: parcial pela API, concluído via SSH com senha root fornecida pelo Lucas.

Com aprovação do Lucas, foi criada uma public key na conta Hostinger:

| Campo | Valor |
|---|---|
| Nome | `hermes-cron-inventory-2026-05-04` |
| Hostinger public key ID | `499839` |
| Fingerprint | `SHA256:00cczrzMqMfOjR1yc8aFvBWfE8sZK0hDYVF7QhRh8T8` |

A chave privada foi gerada localmente fora do repositório em `/opt/data/hermes_bruno_ingest/ssh_keys/` e não foi commitada.

Limite encontrado:

- Hostinger API `GET /api/vps/v1/public-keys` lista chaves da conta.
- Hostinger API `GET /api/vps/v1/virtual-machines/1331756/public-keys` retorna `data: []`.
- `OPTIONS /api/vps/v1/virtual-machines/1331756/public-keys` permite apenas `GET, HEAD`; não há `POST/PUT` para anexar chave à VPS em execução nesse endpoint.

Conclusão: a API permitiu criar a chave na conta, mas não confirmou um caminho seguro para injetá-la na VPS em execução. A chave foi efetivamente instalada via SSH usando a senha root fornecida pelo Lucas.

## Inventário real coletado em `lc.vps`

Data de coleta: 2026-05-04 11:01 UTC.

### Cron do sistema

Root crontab: não há crontab para root.

`/etc/crontab` contém apenas rotinas padrão:

- hourly: `run-parts /etc/cron.hourly` no minuto 17;
- daily: `run-parts /etc/cron.daily` às 06:25;
- weekly: `run-parts /etc/cron.weekly` domingo às 06:47;
- monthly: `run-parts /etc/cron.monthly` dia 1 às 06:52.

`/etc/cron.d/` contém:

| Arquivo | Schedule | Função | Status |
|---|---|---|---|
| `docker-image-prune` | diário meia-noite + jitter até 6h | `docker image prune -af --filter until=24h` | ativo |
| `e2scrub_all` | domingo 03:30 e diário 03:10, fallback sem systemd | filesystem scrub | padrão sistema |
| `sysstat` | a cada 10min e 23:59 | coleta/rotação sysstat | ativo |

Diretórios `/etc/cron.hourly`, daily, weekly e monthly têm apenas jobs padrão do Ubuntu/sysstat/logrotate/man-db/apport.

### Systemd timers

Timers relevantes encontrados são padrão do sistema: sysstat, apt, logrotate, dpkg backup, fwupd, fstrim, tmpfiles, motd, e2scrub.

Nenhum timer de negócio/Hermes/LK/Zipper/SPITI foi encontrado.

### Serviços relevantes

- `cron.service`: active/running.
- `docker.service`: active/running.

Nenhum service systemd específico `hermes`, `lk`, `spiti`, `zipper` ou `n8n` além de Docker/cron apareceu como unidade systemd.

### Docker containers ativos

| Container | Imagem | Status | Observação |
|---|---|---|---|
| `hermes-agent-5ajw-hermes-telegram-1` | `ghcr.io/hostinger/hvps-hermes-agent:latest` | Up | gateway Telegram/Hermes foreground |
| `hermes-agent-5ajw-hermes-agent-1` | `ghcr.io/hostinger/hvps-hermes-agent:latest` | Up | serviço principal web/ttyd na porta 4860 |
| `n8n-vdgm-n8n-1` | `docker.n8n.io/n8nio/n8n` | Up | n8n |
| `paperclip-qrlt-paperclip-1` | `ghcr.io/hostinger/hvps-paperclip:latest` | Up | Paperclip |
| `traefik-traefik-1` | `traefik:latest` | Up | reverse proxy |

Compose files encontrados:

- `/docker/hermes-agent-5ajw/docker-compose.yml`
- `/docker/n8n-vdgm/docker-compose.yml`
- `/docker/paperclip-qrlt/docker-compose.yml`
- `/docker/traefik/docker-compose.yml`

### Hermes cron na VPS

`hermes cron list --all` na VPS/container mostra 1 job:

| Job | Schedule | Entrega | Estado | Próxima execução |
|---|---|---|---|---|
| Hermes release watch | `0 9 * * 1` | origin | active | 2026-05-11 09:00 UTC |

Observação: o CLI reporta “Gateway is not running — jobs won't fire automatically”, mas o container `hermes-telegram` está `Up` e logs mostram `Hermes Gateway Starting...`. Isso parece uma limitação/detecção incorreta do status por rodar em foreground Docker, ou possível conflito de múltiplos pollers visto em logs antigos. Não alterei containers.

### Logs Hermes relevantes

Logs recentes do container Telegram mostram:

- `Hermes Gateway Starting...`
- avisos antigos de conflito Telegram polling: `terminated by other getUpdates request`
- cron `Hermes release watch` criado

Como o Telegram está respondendo nesta conversa, não tratei isso como incidente ativo, apenas como ponto a monitorar.

## Status das rotinas documentadas após verificação real

### Verificadas ativas

| Rotina | Evidência | Status |
|---|---|---|
| `areas/operacoes/rotinas/hermes-release-watch.md` | `hermes cron list --all` mostra job ativo | ativa no Hermes cron |

### Rotinas de sistema/VPS não-Hermes

| Rotina | Evidência | Status |
|---|---|---|
| Docker image prune | `/etc/cron.d/docker-image-prune` | ativa |
| sysstat collect/summary | `/etc/cron.d/sysstat` + systemd timers | ativa |
| apt/logrotate/dpkg/fstrim/etc | systemd timers padrão | ativas/padrão |

## Rotinas documentadas sem execução real encontrada na VPS

Estas rotinas existem no Brain, mas não foram encontradas como cron/systemd/Hermes cron ativo em `lc.vps` durante a coleta:

### Operações

- `areas/operacoes/rotinas/brain-sync.md`
- `areas/operacoes/rotinas/heartbeat.md`
- `areas/operacoes/rotinas/brain-health-check.md`
- `areas/operacoes/rotinas/hermes-release-watch.md` — verificado no cron Hermes local, não na VPS.

### LK

- `areas/lk/rotinas/full-sync.md`
- `areas/lk/rotinas/morning-briefing.md`
- `areas/lk/rotinas/sync-log.md`
- `areas/lk/rotinas/consequence-tracker.md`
- `areas/lk/sub-areas/crm/rotinas/cross-sell-monitor.md`
- `areas/lk/sub-areas/crm/rotinas/rfm-semanal.md`
- `areas/lk/sub-areas/crm/rotinas/outcomes-tracker.md`
- `areas/lk/sub-areas/trafego-pago/rotinas/creative-pipeline.md`
- `areas/lk/sub-areas/atendimento/rotinas/consolidar-faq.md`

### Zipper

- `areas/zipper/rotinas/consulta-vendas-obras.md`
- `areas/zipper/rotinas/abordagem-colecionadores.md`
- `areas/zipper/rotinas/planejamento-feiras.md`

### SPITI

- `areas/spiti/rotinas/verificacao-lances.md`
- `areas/spiti/rotinas/alerta-lances.md`
- `areas/spiti/rotinas/relatorio-leilao.md`

## Próximas ações necessárias

1. Decidir se o acesso por chave dedicada deve permanecer ou ser removido após a sequência.
2. Rotacionar a senha root enviada por chat, se Lucas quiser reduzir risco.
3. Investigar, sem alterar produção, por que `hermes cron list` alerta gateway parado enquanto o container gateway está rodando.
4. Se existirem crons de negócio em n8n, fazer inventário via API n8n em rodada própria.
5. Atualizar `empresa/rotinas/_index.md` com coluna de status real em próxima rodada.

## Inventário n8n

Rodada executada em 2026-05-04.

Documento: `areas/operacoes/rotinas/n8n-inventory.md`.

Resultado:

- container `n8n-vdgm-n8n-1` está rodando em `lc.vps`;
- API interna e SQLite foram consultados em modo read-only;
- `workflow_entity` existe, mas `workflow_count = 0`;
- não há execuções recentes registradas;
- nenhum workflow n8n de negócio foi encontrado nesse ambiente.

Conclusão:

> n8n em `lc.vps` está rodando, mas sem workflows encontrados no banco/API durante a coleta de 2026-05-04.

## Script de inventário recomendado na VPS

Rodar como root ou usuário com permissões suficientes:

```bash
hostname; date; uname -a
crontab -l 2>&1
sed -n '1,220p' /etc/crontab 2>&1
for f in /etc/cron.d/*; do echo "--- $f"; sed -n '1,220p' "$f" 2>&1; done
for d in /etc/cron.hourly /etc/cron.daily /etc/cron.weekly /etc/cron.monthly; do echo "--- $d"; ls -la "$d" 2>&1; done
systemctl list-timers --all --no-pager 2>&1
systemctl list-units --all --type=service --no-pager 2>&1 | grep -Ei 'hermes|lk_|lk-|spiti|zipper|zpr|n8n|docker|cron|sync|briefing|rfm|shopify|klaviyo|meta|ga4|frenet|judgeme|tiny|evolution' || true
docker ps --format 'table {{.Names}}\t{{.Image}}\t{{.Status}}\t{{.Ports}}' 2>&1
find /docker /root /opt -maxdepth 4 \( -name 'docker-compose.yml' -o -name 'compose.yml' -o -name 'docker-compose.yaml' \) 2>/dev/null | sort
(command -v hermes && hermes cron list --all) 2>&1
find /opt/data /opt/data/hermes_bruno_ingest/hermes-brain -maxdepth 3 -type f \( -name '*cron*' -o -name '*schedule*' -o -name '*briefing*' -o -name '*sync*' -o -name '*heartbeat*' \) 2>/dev/null | sort
```

## Regra de comunicação

Após a verificação atual, dizer:

> Rotina documentada no Brain; execução real na VPS só foi confirmada quando listada como ativa neste inventário. Caso contrário, não encontrada como cron/systemd/Hermes cron em `lc.vps`.
