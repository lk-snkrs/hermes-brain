# Hermes System Audit + Webhook Alignment — 2026-06-25

- generated_at_utc: `2026-06-25T10:34:53.321708+00:00`
- status geral: **ok com atenção controlada**
- values_printed: `false`
- writes externos/envios/deploys/restarts: `0`

## Escopo aprovado por Lucas

Lucas pediu `fazer 1 2 e 4`:
1. corrigir/alinha as 4 rotas webhook com problema de assinatura;
2. rodar smoke leve dos especialistas;
4. rodar auditoria sistêmica completa read-only.

## Resultado 1 — Webhooks

- Status final: **pass**
- Rotas testadas: `14`
- Pass: `14`
- Attention: `0`
- Escritas externas/envios: `0`

### Mudança aplicada

- `lk-shopify-tiny-stock-sync`: removido segredo literal legado e usado `secret_doppler: HERMES_WEBHOOK_SECRET`.
- `lk-shopify-tiny-stock-sync-dryrun`: removido segredo literal legado e usado `secret_doppler: HERMES_WEBHOOK_SECRET`.
- `lk-stock-shopify-order-paid`: alinhado ao segredo de rota LK Stock usado pelo proxy.
- `lk-stock-shopify-product-update`: alinhado ao segredo de rota LK Stock usado pelo proxy.

Observação de governança: as duas rotas LK Stock ainda exigiram literal local na subscription porque o runtime atual não injeta `LK_STOCK_HERMES_ROUTE_SECRET` no processo do gateway como env resolvível por `secret_doppler`. O valor veio do Doppler em processo curto, não foi impresso, e deve ser migrado para `secret_doppler` em uma próxima melhoria de launcher/runtime injection.

Backups criados:
- `/opt/data/backups/webhook_subscriptions_20260625T103017Z_pre_4route_secret_alignment.json`
- `/opt/data/backups/webhook_subscriptions_20260625T103104Z_pre_lk_stock_secret_alignment.json`
- `/opt/data/backups/webhook_subscriptions_20260625T103208Z_pre_lk_stock_literal_alignment.json`


Artefato final de certificação:
- `/opt/data/tmp/hermes_webhooks_14_route_certification_final_20260625.json`

## Resultado 2 — Smoke leve dos especialistas

- Perfis/gateways vivos testados: `12`
- Bot API `getMe`: `12/12 OK`
- Especialistas com API Server fechado: `11/11`
- Especialistas com Webhook fechado: `11/11`
- `DOPPLER_TOKEN` no env dos filhos: `0`

Perfis observados:
- default: `@HermesLC_botbot`
- mordomo: `@Clawdio_HostingerBot`
- lk-growth: `@LKGrowth_HermesBot`
- lk-ops: `@LKOps_HermesBot`
- lk-shopify: `@LKShopify_HermesBot`
- lk-trends: `@LKTrends_HermesBot`
- lk-collection-optimizer: `@lk_otimizacaodecolecao_bot`
- lk-stock: `@lk_contentbot` — mapeamento conhecido/ambíguo por nome, mas documentado em skill runtime.
- lk-finance: `@lkfinance_hermesbot`
- lk-content: `@hermes_lk_producaodeconteudo_bot`
- spiti: `@SPITI_HermesBot`
- spiti-atendimento: `@spitiatendimento_hermesbot`

## Resultado 4 — Auditoria sistêmica read-only

### Runtime / Gateway

- Gateway principal: vivo.
- API local: OK.
- Webhook local: OK.
- Webhook público: OK.
- Versão ativa/source: Hermes Agent v0.17.0 (2026.6.19), upstream `ba6ffd4f`, up to date.

### Crons / Brain / Memory

- Cron registry local: `44` jobs; `40` ativos; `4` pausados; `nonok=0`.
- Nightly Ops: `100/100`, critical=0, attention=0, watch=0.
- Brain Health: FAIL=0, WARN=0.
- Memory Hygiene: status `ok`, Honcho governado, alert_count=0, saturation=0, possible_secret_locator=0.

### Host

- RAM disponível: ~17.7 GB / 31.3 GB.
- Disco livre: ~186 GB / 386 GB.
- Load médio: normal para o host.

### CLI integrations smoke

- `cloudflare_wrangler`: `ok`
- `github`: `ok` HTTP `200`
- `google_workspace`: `ok` HTTP `200`
- `klaviyo`: `ok` HTTP `200`
- `linear`: `failed` HTTP `401`
- `notion`: `ok` HTTP `200`
- `sentry`: `ok` HTTP `200`
- `shopify_lk`: `ok` HTTP `200`
- `supabase`: `ok`
- `vercel`: `ok`


Ponto de atenção: `linear` retornou `401` no smoke. As demais integrações testadas ficaram OK. Isso é integração operacional, não pane do Hermes core.

## Gaps / Watchlist

1. Migrar as duas rotas LK Stock de literal local para `secret_doppler` quando o launcher/gateway injetar `LK_STOCK_HERMES_ROUTE_SECRET` em runtime.
2. Investigar/atualizar credencial Linear se a integração for necessária; atualmente smoke `401`.
3. Manter warnings de rede Telegram em watchlist; getMe e processos estão OK, então não classifica como incidente.
4. Se Lucas quiser “round-trip real” por especialista, enviar probes controlados em janela separada; este smoke evitou spam e usou `getMe`.

## Verificação

- Certificação webhook final: `14/14 pass`, exit code `0`.
- Smoke Bot API: `12/12 getMe OK`.
- CLI integrations: execução read-only; `values_printed=false`.
- Secrets/signatures/token previews: não impressos.
