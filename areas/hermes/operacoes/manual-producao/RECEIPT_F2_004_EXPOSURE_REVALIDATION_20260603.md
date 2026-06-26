# Receipt — F2-004 Exposure Revalidation

Gerado em: 2026-06-03T17:58:16Z  
Board: `hermes-lk-improvements`  
Card: `t_cd3dd451` — `[F2][COCKPIT][A1] Revalidate dashboard/API/webhook exposure classification`  
Modo: read-only / diagnóstico local  

## Escopo

Revalidar a classificação de exposição de API Server, Webhook e Dashboard/Cockpit antes de avançar para plugin/cockpit/status.

## Ações permitidas realizadas

- Inspeção read-only de processos Hermes por `/proc/<pid>/environ` com secrets redigidos.
- Inspeção read-only de containers Docker via `docker ps`/`docker inspect` sem alteração de container.
- Health checks HTTP GET locais e públicos.
- Listagem read-only de webhook subscriptions via CLI Hermes.
- Probe HTTP GET do hostname público do dashboard.

## Ações não realizadas

Não houve:

- restart de gateway/profile;
- alteração de Docker/Compose/Traefik/VPS;
- alteração de config/env/secrets;
- criação/alteração de webhook;
- ativação de dashboard/plugin/MCP;
- dispatch Kanban para worker;
- write externo em Shopify/Tiny/GMC/Crisp/WhatsApp/email.

## Evidência resumida

### API Server default

Estado observado:

- Processo default: PID `1`, `HERMES_HOME=/opt/data`, comando `hermes gateway run`.
- Env live redigido:
  - `API_SERVER_ENABLED=true`
  - `API_SERVER_HOST=0.0.0.0`
  - `API_SERVER_PORT=8642`
  - `API_SERVER_KEY=<set>`
- Listener interno: `0.0.0.0:8642` no PID `1`.
- Docker publish do container principal: `8642/tcp` publicado no host como `127.0.0.1:8642`.
- Traefik labels do container principal: não apontam serviço público para `8642`.
- Health local: `GET http://127.0.0.1:8642/health` → `200`, `platform=hermes-agent`.
- Endpoint sensível com bearer inválido: `GET /v1/models` → `401`, `invalid_api_key`.

Classificação atual: **host-local por Docker publish; não evidenciado como API pública**.

Risco: **baixo/médio**. O bind interno é amplo dentro do container, mas a publicação observada no host é loopback e o endpoint sensível exige API key.

### Webhook default

Estado observado:

- Processo default: PID `1`.
- Env live redigido:
  - `WEBHOOK_ENABLED=true`
  - `WEBHOOK_PORT=8644`
  - `WEBHOOK_SECRET=<set>`
- Listener interno: `0.0.0.0:8644` no PID `1`.
- Traefik labels do container principal expõem o serviço `crisp-hooks` para `8644`.
- Hostnames públicos com `GET /health` → `200`, `platform=webhook`:
  - `https://hermes-webhooks.lucascimino.com/health`
  - `https://crisp-hooks.srv1331756.hstgr.cloud/health`
- Webhook subscriptions read-only: 2 subscriptions ativas, ambas LK Shopify `orders/paid`/`orders/cancelled`, `Deliver: log`, descritas como ledger/refresh local sem writes Shopify/Tiny.
- Rotas/identificadores de webhook foram redigidos.

Classificação atual: **público via Traefik/Cloudflare**.

Risco: **médio**. A superfície é pública e deve continuar exigindo assinatura/HMAC, filtro de evento, idempotência e rollback para qualquer rota nova.

### Dashboard / cockpit / UI

Estado observado:

- Existe container adicional `hermes-agent-5ajw-hermes-agent-1` com serviço interno `4860/tcp` e publicação host `0.0.0.0:33855`/`:::33855`.
- Labels Traefik expõem hostname público `hermes-agent-5ajw.srv1331756.hstgr.cloud` para service port `4860`.
- `GET https://hermes-agent-5ajw.srv1331756.hstgr.cloud/` → `200`, HTML com título `Hermes Agent - Dashboard`.
- `GET /health` no mesmo hostname retorna a mesma aplicação SPA (`200`), não um health JSON.
- Probe `GET /v1/models` nesse hostname também retorna SPA (`200`), indicando fallback de frontend; não evidência de API Server default roteada por esse hostname.
- O HTML inclui token de sessão de frontend; valor não foi preservado no receipt.

Classificação atual: **dashboard público existente** em hostname `hermes-agent-5ajw.srv1331756.hstgr.cloud`, separado do API Server default `8642`.

Risco: **médio/alto até revisão de autenticação**. A existência de dashboard público é real; antes de usar como cockpit operacional, precisa de revisão específica de autenticação, permissões, session token, endpoints alcançáveis, logs e rollback. Não foi alterado nada nesta revalidação.

### Perfis especialistas

Perfis vivos observados com `API_SERVER_ENABLED=false` e `WEBHOOK_ENABLED=false` no ambiente live:

- `mordomo`
- `lk-growth`
- `spiti`
- `lk-ops`
- `lk-shopify`
- `lk-trends`
- `lk-collection-optimizer`

Classificação atual: **especialistas sem API/webhook expostos por env live observado**.

## Decisão operacional

1. **API Server default** pode ser usado apenas para consultas locais/read-only ou túnel controlado; não tratar como API pública.
2. **Webhook default** é superfície pública ativa; manter documentado e não adicionar rota/evento sem approval packet.
3. **Dashboard público** precisa virar próximo item P0/P1 antes de cockpit/plugin: revisar autenticação e exposição do hostname público sem modificar runtime.
4. **Plugin de status** pode ser desenhado em modo read-only, mas deve mascarar API keys, webhook secrets, rotas e qualquer token de sessão.
5. **Kanban dispatch** continua proibido para esses cards: manter unassigned até approval packet do primeiro piloto read-only.

## Resultado

Card `t_cd3dd451` pode ser concluído como revalidação read-only.

A classificação anterior foi atualizada: o ponto novo/material é que há **dashboard público separado** (`hermes-agent-5ajw.srv1331756.hstgr.cloud`) e ele deve ser revisado antes de qualquer adoção de cockpit operacional.
