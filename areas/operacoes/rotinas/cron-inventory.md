# Inventário de Crons — Hermes / VPS

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

Status: bloqueado por autenticação.

Tentativas realizadas sem persistir credenciais:

- hosts: `72.60.150.124`, `187.127.10.158`;
- usuários testados: `root`, `hermes`, `ubuntu`, `admin`, `debian` conforme aplicável;
- secrets testados sob demanda via Doppler: `HERMES_VPS_SSH_PASS`, `HERMES_SUDO_PASS`, `VPS_ROOT_PASSWORD`;
- resultado: `Permission denied (publickey,password)`.

Conclusão: as credenciais SSH disponíveis no Doppler parecem não autenticar nas VPS atuais, ou o SSH exige chave/usuário/porta diferente.

### Tentativa de chave SSH via Hostinger

Status: parcial.

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

Conclusão: a API permitiu criar a chave na conta, mas não confirmou um caminho seguro para injetá-la na VPS em execução sem outra ação, como painel, recriação, recovery ou reset de senha.

## Rotinas documentadas ainda sem verificação real de cron na VPS

Estas rotinas existem no Brain, mas não devem ser afirmadas como ativas até conferência na VPS:

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

## Próxima ação necessária

Para completar a Rodada A, é necessário um dos itens abaixo:

1. atualizar no Doppler uma credencial SSH válida para `lc.vps`;
2. informar usuário/porta/chave SSH correta;
3. anexar pelo painel Hostinger a public key `hermes-cron-inventory-2026-05-04` à VPS, se o painel permitir;
4. autorizar explicitamente outro caminho de acesso, como reset temporário de root password via Hostinger API;
5. executar manualmente na VPS o script de inventário e colar o output redigido.

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
find /root/.hermes /root/hermes-brain -maxdepth 3 -type f \( -name '*cron*' -o -name '*schedule*' -o -name '*briefing*' -o -name '*sync*' -o -name '*heartbeat*' \) 2>/dev/null | sort
```

## Regra de comunicação

Até a verificação SSH/VPS ser concluída, dizer:

> Rotina documentada no Brain; execução real na VPS ainda não verificada.
