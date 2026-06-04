# F2-004 — Dashboard/API exposure classification

Gerado em: 2026-05-30T22:09:32+00:00  
Status: **concluído em modo read-only**  
Escopo: classificar exposição atual do API Server / Webhook / Dashboard do Hermes default antes de usar como cockpit.  
Não houve alteração de runtime, Docker, Traefik, config, secrets, crons, plugins, MCP ou gateway.

## 1. Resumo executivo

Classificação atual:

- **API Server default (`8642`)**: **host-local via Docker publish em `127.0.0.1:8642`**, apesar de o processo dentro do container escutar em `0.0.0.0:8642`.
- **Webhook default (`8644`)**: **publicamente acessível via Traefik/Cloudflare** nos domínios `hermes-webhooks.lucascimino.com` e `crisp-hooks.srv1331756.hstgr.cloud`.
- **Dashboard**: configuração local existe apenas como settings de tema; não foi encontrada evidência de dashboard web público separado nesta checagem.
- **Especialistas LK/Mordomo/SPITI**: processos vivos com `API_SERVER_ENABLED=false` e `WEBHOOK_ENABLED=false` no ambiente live inspecionado.

Interpretação:

- O cockpit/API para operação interna não deve ser tratado como público neste momento: o API Server aparece protegido por bind host-local e exige API key para endpoints sensíveis.
- O webhook é intencionalmente uma superfície pública. Isso não é automaticamente erro, mas precisa ficar documentado como superfície pública ativa e não deve ser expandido sem approval packet.

## 2. Evidências coletadas

### Processo default

Processo principal:

- PID: `1`
- `HERMES_HOME`: `/opt/data`
- comando: `hermes gateway run`
- env de superfície:
  - `API_SERVER_ENABLED=true`
  - `API_SERVER_HOST=0.0.0.0`
  - `API_SERVER_PORT=8642`
  - `API_SERVER_KEY=<set>`
  - `WEBHOOK_ENABLED=true`
  - `WEBHOOK_PORT=8644`
  - `WEBHOOK_SECRET=<set>`

### Listeners dentro do container/runtime

Listeners relevantes em `/proc/net/tcp`:

- `0.0.0.0:8642` → PID `1` / Hermes default
- `0.0.0.0:8644` → PID `1` / Hermes default
- `127.0.0.1:8787` → processo WACLI responder local

Observação: `0.0.0.0` aqui é o bind dentro do runtime/container; a exposição real depende de Docker/Traefik/port publish.

### Docker publish / Traefik

Container principal: `hermes-agent-5ajw-hermes-telegram-1`

Port publish:

- `8642/tcp` publicado como `127.0.0.1:8642` no host.

Labels Traefik relevantes:

- `traefik.enable=true`
- router `crisp-hooks`
- rule: `Host(hermes-webhooks.lucascimino.com)` ou `Host(crisp-hooks.srv1331756.hstgr.cloud)`
- service target port: `8644`

Não foi vista label Traefik expondo o API Server `8642`.

### Health checks

Local API health:

- `GET http://127.0.0.1:8642/health` → `200 OK`, `{"status":"ok","platform":"hermes-agent"}`

Local webhook health:

- `GET http://127.0.0.1:8644/health` → `200 OK`, `{"status":"ok","platform":"webhook"}`

Endpoint sensível com chave inválida:

- `GET http://127.0.0.1:8642/v1/models` com bearer inválido → `401 Unauthorized`, `invalid_api_key`

Webhooks públicos:

- `GET https://hermes-webhooks.lucascimino.com/health` → `200 OK`, `platform=webhook`
- `GET https://crisp-hooks.srv1331756.hstgr.cloud/health` → `200 OK`, `platform=webhook`
- `POST https://hermes-webhooks.lucascimino.com/webhooks/nonexistent` → `404 Unknown route`

### Webhook subscriptions

CLI read-only indicou 1 subscription ativa:

- descrição: LK Shopify `orders/paid|orders/cancelled` → Tiny official stock dry-run ledger / no writes
- events: `orders/paid`, `orders/cancelled`
- deliver: `log`
- rota/identificador redigidos

## 3. Profiles especialistas vivos

PIDs inspecionados por `/proc/<pid>/environ`:

- `/opt/data/profiles/mordomo` — API off / webhook off
- `/opt/data/profiles/lk-growth` — API off / webhook off
- `/opt/data/profiles/spiti` — API off / webhook off
- `/opt/data/profiles/lk-ops` — API off / webhook off
- `/opt/data/profiles/lk-shopify` — API off / webhook off
- `/opt/data/profiles/lk-trends` — API off / webhook off

Conclusão: a superfície pública relevante neste momento está concentrada no default webhook via Traefik, não nos especialistas.

## 4. Risco e decisão

### API Server default

Risco atual: **baixo/médio**.

Motivo:

- bind interno é amplo (`0.0.0.0`), mas Docker publica no host apenas em `127.0.0.1:8642`;
- endpoints sensíveis exigem API key;
- sem evidência de Traefik expondo `8642` publicamente.

Uso permitido para Fase 2:

- cockpit local/SSH tunnel/Tailscale depois de approval packet;
- consultas locais read-only;
- não usar como API pública.

### Webhook default

Risco atual: **médio**.

Motivo:

- está publicamente acessível via dois hostnames;
- health é público;
- há uma subscription ativa relacionada a Shopify events;
- ainda que a descrição indique dry-run/no writes, qualquer expansão de webhook pode virar superfície produtiva.

Uso permitido para Fase 2:

- manter como superfície pública documentada;
- não adicionar novas rotas/eventos sem approval packet;
- qualquer integração nova precisa HMAC/signature, event filter, idempotência e rollback.

### Dashboard

Risco atual: **baixo/unknown**.

Motivo:

- há config `dashboard.theme`, mas não foi encontrada evidência de dashboard público separado;
- se for ativar cockpit, primeiro deve ser local-only.

## 5. Recomendações

1. **Não mexer agora**: não há necessidade de mudança emergencial de Docker/Traefik/API.
2. **Registrar como verdade operacional**: API é local-only por publish; webhook é público via Traefik.
3. **Antes de cockpit**: criar approval packet para qualquer dashboard/API usage além de leitura local.
4. **Antes de novos webhooks**: exigir assinatura/HMAC, filtro de evento, idempotência, owner, rollback e log redigido.
5. **Antes de plugin de status**: pode ler esses estados localmente, mas não deve expor API key, webhook secret ou subscription route.
6. **Antes de Kanban real**: lembrar que default tem `kanban.dispatch_in_gateway=true`; assignment a worker pode executar.

## 6. Revalidação 2026-06-03 — Fase 2 Kanban

Receipt: `RECEIPT_F2_004_EXPOSURE_REVALIDATION_20260603.md`  
Board/card: `hermes-lk-improvements` / `t_cd3dd451`  
Modo: read-only, sem alteração de runtime/Docker/Traefik/config/secrets/gateway.

Atualização material desde a classificação inicial:

- **API default (`8642`)** segue classificada como **host-local por Docker publish**: o processo escuta `0.0.0.0:8642` dentro do container, mas o publish observado continua `127.0.0.1:8642` no host; `/v1/models` com chave inválida retorna `401 invalid_api_key`.
- **Webhook default (`8644`)** segue classificado como **público via Traefik/Cloudflare**: hostnames públicos `/health` retornam `200 platform=webhook`; há 2 subscriptions LK Shopify `orders/paid`/`orders/cancelled`, `Deliver: log`, descritas como sem writes Shopify/Tiny.
- **Dashboard/cockpit** foi reclassificado: há um **dashboard público separado** em `hermes-agent-5ajw.srv1331756.hstgr.cloud`, servido por container/serviço `4860`, exposto por Traefik. `GET /` retorna HTML `Hermes Agent - Dashboard`; `GET /health` e `GET /v1/models` nesse hostname caem no SPA, sem evidência de roteamento para a API default. O HTML inclui token de sessão de frontend; o valor não foi preservado.
- **Especialistas vivos** observados continuam com `API_SERVER_ENABLED=false` e `WEBHOOK_ENABLED=false` no env live: Mordomo, LK Growth, SPITI, LK Ops, LK Shopify, LK Trends e LK Collection Optimizer.

Decisão operacional atualizada:

1. API default pode ser usada apenas em modo local/read-only/túnel controlado; não tratar como API pública.
2. Webhook default é superfície pública ativa; nenhuma nova rota/evento sem approval packet com HMAC, filtro, idempotência, owner, rollback e logs redigidos.
3. Dashboard público exige revisão específica de autenticação/exposição antes de qualquer cockpit operacional ou plugin de status.
4. Cards Kanban de Fase 2 continuam `unassigned` até approval packet do primeiro piloto read-only.

## 7. Revisão específica do dashboard público — 2026-06-03

Receipt: `RECEIPT_F2_DASHBOARD_PUBLIC_AUTH_REVIEW_20260603.md`  
Board/card: `hermes-lk-improvements` / `t_2302a6a6`  
Modo: read-only, sem POST/PUT/PATCH/DELETE e sem alteração de runtime/Docker/Traefik/config/secrets/gateway.

Achado material:

- `GET /`, `GET /docs`, `GET /redoc` e `GET /openapi.json` estão públicos no hostname do dashboard.
- O HTML público injeta `window.__HERMES_SESSION_TOKEN__`; o valor não foi preservado.
- Sem token, alguns endpoints sensíveis retornam `401`, mas `GET /api/status` é público e expõe versão/paths/estado.
- Com o token público injetado pela própria página, endpoints read-only sensíveis responderam `200`, incluindo `/api/config`, `/api/sessions`, `/api/skills` e `/api/logs`.
- Container do dashboard está publicado por Traefik no serviço interno `4860`; OpenAPI público lista também rotas mutantes, que não foram chamadas.

Classificação atualizada:

- **Dashboard público**: risco alto para uso operacional enquanto exposto com token de página e docs OpenAPI públicos.
- **Cockpit/plugin operacional**: bloqueado até mitigação ou isolamento.

Mitigação recomendada antes de continuar cockpit/plugin:

1. Restringir/remover exposição pública do dashboard por Traefik/Cloudflare Access/VPN/Tailscale/allowlist.
2. Proteger ou desabilitar `/docs`, `/redoc` e `/openapi.json` em produção pública.
3. Remover token de sessão estático/injetado em HTML público; exigir autenticação server-side forte.
4. Garantir autorização robusta para rotas mutantes e endpoints de logs/sessões/config.
5. Revalidar que `/api/config`, `/api/sessions`, `/api/logs` e `/api/skills` retornam `401/403` para visitante público.

## 8. Status do card F2-004

F2-004 está concluído como classificação + revalidação read-only, e a revisão específica do dashboard público foi registrada separadamente.

Resultado final atualizado:

- API default: **host-local / não pública por evidência Docker atual**.
- Webhook default: **público via Traefik/Cloudflare**.
- Dashboard: **público separado via Traefik com risco alto enquanto exposto com token de página, docs OpenAPI públicos e endpoints sensíveis acessíveis via token público do frontend**.
- Próxima ação segura: approval packet separado para fechar/proteger o dashboard público antes de cockpit/plugin operacional.
