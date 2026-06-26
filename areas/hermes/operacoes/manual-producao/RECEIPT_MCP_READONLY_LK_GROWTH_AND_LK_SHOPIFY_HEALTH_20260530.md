# Receipt — MCP read-only LK Growth + LK Shopify health probe

Gerado em: 2026-05-30T23:21:30+00:00  
Status: **executado com aprovação verbal `Aprovo`**  
Escopo aplicado: configurar e ativar `metricool_readonly` e `meta_ads_readonly` no profile `lk-growth`; verificar LK Shopify reportado como offline.

## 1. LK Shopify

Resultado: **não estava offline no momento da verificação**.

Evidência:

- processo live encontrado com `HERMES_HOME=/opt/data/profiles/lk-shopify`;
- `API_SERVER_ENABLED=false`;
- `WEBHOOK_ENABLED=false`;
- token Telegram presente sem exposição de valor;
- `gateway_state.json`: Telegram `connected`;
- logs recentes indicaram `Connected to Telegram (polling mode)`;
- logs recentes indicaram inbound de Lucas e resposta do profile;
- Bot API `getMe` validou `@LKShopify_HermesBot`;
- probe enviado para Lucas via bot: `message_id=844`.

Ação feita:

- não reiniciei LK Shopify porque o profile já estava conectado e respondendo;
- enviei um probe curto de saúde pelo próprio bot.

## 2. MCPs criados

Foram criados dois wrappers locais read-only no profile `lk-growth`:

- `/opt/data/profiles/lk-growth/mcp-servers/metricool-readonly/server.py`
- `/opt/data/profiles/lk-growth/mcp-servers/meta-ads-readonly/server.py`

Ambos buscam secrets por nome via Doppler `lc-keys/prd` no runtime e não persistem valores em config.

### metricool_readonly

Tools expostas:

- `metricool_brand_profile`
- `metricool_google_ads_campaigns`
- `metricool_meta_ads_campaigns`

Teste ad-hoc via `mcporter`:

- tool discovery: OK, 3 tools;
- `metricool_brand_profile`: OK, brand `LK Sneakers`, `blogId=6217010`, timezone `America/Sao_Paulo`, Ads conectados no Metricool.

### meta_ads_readonly

Tools expostas:

- `meta_me`
- `meta_ad_accounts`
- `meta_campaigns`
- `meta_insights`

Teste ad-hoc via `mcporter`:

- tool discovery: OK, 4 tools;
- `meta_me`: OK, token validado contra Meta Graph.

## 3. Config ativada

Profile configurado:

- `/opt/data/profiles/lk-growth/config.yaml`

Backup antes da mudança:

- `/opt/data/backups/mcp-activation/20260530T232030Z/lk-growth-config.yaml.bak`

Config adicionada:

- `mcp_servers.metricool_readonly`
- `mcp_servers.meta_ads_readonly`
- `sampling.enabled=false` nos dois

Validação:

- `hermes config check`: OK
- `hermes mcp list`: dois servers enabled
- `hermes mcp test metricool_readonly`: connected, 3 tools discovered
- `hermes mcp test meta_ads_readonly`: connected, 4 tools discovered

## 4. Restart controlado

Foi reiniciado apenas o profile `lk-growth` para carregar os MCPs.

Evidência pós-restart:

- novo PID live: `9251`;
- `HERMES_HOME=/opt/data/profiles/lk-growth`;
- `API_SERVER_ENABLED=false`;
- `WEBHOOK_ENABLED=false`;
- `API_SERVER_KEY` ausente;
- logs: `Starting Hermes Gateway`, `Active profile: lk-growth`, `Connected to Telegram`, `Gateway running with 1 platform(s)`.

Observação: ao tentar iniciar manualmente, o profile já havia sido reerguido automaticamente como PID `9251`; a tentativa manual detectou `Gateway already running` e não criou duplicidade.

## 5. Guardrails preservados

- Nenhum Docker/VPS/Traefik alterado.
- Nenhum secret impresso.
- Nenhum MCP write externo exposto.
- Nenhuma ferramenta de create/update/delete/send/budget/stock/campaign foi criada.
- Meta/Klaviyo/Tiny genéricos não foram instalados porque expõem muitas mutations.
- Tiny e Klaviyo permanecem em roadmap/approval separado.

## Rollback

Para remover os MCPs:

1. Restaurar backup:
   - `/opt/data/backups/mcp-activation/20260530T232030Z/lk-growth-config.yaml.bak`
2. Reiniciar apenas `lk-growth`.
3. Confirmar `hermes mcp list` sem os dois servers.
