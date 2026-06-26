# Hermes Task OS — ativação runtime após propagação universal

- Data: 2026-06-25
- Aprovação Lucas: “pode dar restart e ativar”
- values_printed: `false`

## Resultado

Foram reiniciados/ativados os gateways especialistas gerenciados para carregar os `AGENTS.md` com a política Task OS universal.

## Profiles gerenciados ativos pós-restart

| Profile | PID pós-ativação | AGENTS marker |
|---|---:|---|
| `lk-collection-optimizer` | `189362` | marker=1 |
| `lk-content` | `192499` | marker=1 |
| `lk-finance` | `190966` | marker=1 |
| `lk-growth` | `182476` | marker=1 |
| `lk-ops` | `196417` | marker=1 |
| `lk-shopify` | `196830` | marker=1 |
| `lk-stock` | `190116` | marker=1 |
| `lk-trends` | `188046` | marker=1 |
| `mordomo` | `195708` | marker=1 |
| `spiti` | `182751` | marker=1 |
| `spiti-atendimento` | `197880` | marker=1 |

## Main/default

O gateway Main/default permaneceu rodando e saudável, mas **não foi reiniciado de dentro da própria sessão gateway**.

Motivo: o próprio Hermes bloqueia self-restart quando chamado de dentro do gateway, porque isso mataria o comando/process group antes de completar. Isso é guardrail esperado.

Estado do Main/default:

- `gateway_state=running`
- Telegram conectado
- API `/health` OK
- Webhook `/health` OK
- `AGENTS.md` já contém a política Task OS universal

## Correção durante ativação

Durante o restart, `spiti-atendimento` apareceu conectado mas com presença de `WEBHOOK_SECRET` no ambiente após Doppler alias injection, mesmo com `WEBHOOK_ENABLED=false`.

Correção local aplicada em `/opt/data/scripts/hermes_all_gateway_watchdog.py`:

- scrub pós-Doppler de `API_SERVER_KEY/API_SERVER_PORT/API_SERVER_HOST`;
- scrub pós-Doppler de `WEBHOOK_PORT/WEBHOOK_SECRET/WEBHOOK_HOST`;
- `API_SERVER_ENABLED=false` e `WEBHOOK_ENABLED=false` no child.

Depois disso, `spiti-atendimento` subiu seguro e o watchdog ficou silent-OK.

## Verificações

- Gateways reais: 12.
- Managed profiles ativos: 11.
- Managed profiles com marcador Task OS no `AGENTS.md`: 11/11.
- `gateway_state` dos profiles ativos: running/telegram connected.
- Especialistas com API/webhook surfaces indevidas: 0.
- Global gateway watchdog: silent-OK.
- API health: 200.
- Webhook health: 200.
- `hermes-task-os`: running=0; diagnostics limpo.

## Não executado

- Docker/VPS/Traefik: 0.
- Secrets/.env/auth: 0 alterações.
- Cron schedule/delivery: 0 alterações.
- External writes: 0.
- Main/default restart: não executado por guardrail de self-restart.

## Próximo se Lucas quiser 100% Main runtime activation

Executar restart do Main/default a partir de shell externo ao gateway ou mecanismo próprio da plataforma, não de dentro desta sessão. Depois validar PID/log/API/webhook/Telegram.
