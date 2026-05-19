# LK Growth connectors validation — 2026-05-19

## Resumo

Validação/correção read-only dos conectores Growth após ativação de PageSpeed/CrUX e revisão de GA4, Klaviyo e Meta.

## GA4

- Status final: `OK`.
- Antes: `GA4_LK_PROPERTY_ID` apontava para uma propriedade inacessível pelas service accounts disponíveis; retornava HTTP 403 e não aparecia em `accountSummaries`.
- Achado: `GOOGLE_ANALYTICS_PROPERTY_ID` já apontava para uma propriedade funcional e acessível.
- Correção feita: `GA4_LK_PROPERTY_ID` foi padronizado no Doppler para a propriedade funcional já acessível.
- Verificação pós-correção: GA4 Data API `runReport` via `GA4_LK_PROPERTY_ID` retornou métricas `sessions` e `totalUsers`.
- Guardrail: correção foi apenas em secret/config do Doppler; nenhuma alteração feita no GA4 Admin/UI.
- Rollback: valor anterior foi identificado por hash no terminal e pode ser restaurado se Lucas informar/confirmar o ID antigo; não registrar property IDs sensíveis em relatório público.

## Klaviyo

- Status final: `OK` para leitura básica.
- Secret usado sem exposição: `KLAVIYO_API_KEY`.
- Testes read-only:
  - `GET /api/accounts/`: HTTP 200, 1 conta.
  - `GET /api/lists/`: HTTP 200, 1 lista.
  - `GET /api/metrics/`: HTTP 200, 135 métricas.
- Guardrail: nenhum send, campaign/flow/list/profile mutation ou ação customer-facing.

## Meta Ads / Paid signals

- Status final: `OK` para leitura básica.
- Secrets usados sem exposição: `META_ACCESS_TOKEN`, `META_ADS_ACCOUNT_ID`, `META_APP_ID`, `META_APP_SECRET`.
- Testes read-only:
  - `GET /me`: HTTP 200.
  - `GET /act_<account_id>`: HTTP 200; ad account ativa e moeda BRL.
  - `GET /campaigns?limit=1`: HTTP 200, retornou 1 campanha.
  - `GET /insights?date_preset=last_7d`: HTTP 200, retornou 1 linha.
- Observação: `debug_token` com o app secret disponível falhou por mismatch de app; a validação prática é pelas chamadas reais de leitura.
- Guardrail: nenhuma campanha, budget, creative, audience, pixel config ou send sem aprovação explícita atual.

## Ahrefs / DataForSEO

- Ahrefs: `OK` via `AHREFS_API_TOKEN`; teste API v3 de domain rating para LK retornou HTTP 200.
- DataForSEO: `NÃO CONECTADO`; sem credenciais Doppler e sem MCP server configurado.

## Inventário atualizado

Arquivo atualizado:

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/CONNECTORS-READONLY-INVENTORY.md`
