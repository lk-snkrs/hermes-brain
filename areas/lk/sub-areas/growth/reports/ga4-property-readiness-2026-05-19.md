# GA4 property readiness — 2026-05-19

## Status

- GA4 está operacional para LK Growth via `GOOGLE_ANALYTICS_PROPERTY_ID`.
- O segredo canônico `GA4_LK_PROPERTY_ID` ainda está `PARCIAL` porque retorna HTTP 403 com as service accounts disponíveis.

## Teste read-only executado

- Fonte de credenciais: Doppler `lc-keys/prd`, sem imprimir valores.
- Service accounts testadas:
  - `GA4_LK_SERVICE_ACCOUNT`
  - `GOOGLE_SERVICE_ACCOUNT_JSON`
- Propriedades testadas:
  - `GA4_LK_PROPERTY_ID`: falhou com HTTP 403 / permissão insuficiente.
  - `GOOGLE_ANALYTICS_PROPERTY_ID`: respondeu OK com métricas presentes via GA4 Data API `runReport`.

## Configuração Claude SEO

- `~/.config/claude-seo/google-api.json` existe.
- `ga4_property_id` está apontando para a propriedade funcional (`GOOGLE_ANALYTICS_PROPERTY_ID`).
- `service_account_path` existe.
- `api_key` segue ausente, portanto PageSpeed/CrUX continuam separados do status GA4.

## Decisão operacional

Até normalizar o canônico, relatórios Growth devem:

1. Usar `GOOGLE_ANALYTICS_PROPERTY_ID` para leitura GA4 quando precisar de dados práticos.
2. Declarar a property usada no relatório.
3. Marcar `GA4_LK_PROPERTY_ID` como `PARCIAL/403`.
4. Não misturar séries/propriedades sem evidência.

## Correção definitiva

Uma das duas opções:

1. Conceder Viewer/Analyst na propriedade `GA4_LK_PROPERTY_ID` à service account operacional.
2. Se `GOOGLE_ANALYTICS_PROPERTY_ID` for confirmada como a LK produção correta, padronizar Doppler para que `GA4_LK_PROPERTY_ID` aponte para ela.

## Guardrail

Nenhuma alteração foi feita em GA4, GSC, Google Cloud, Doppler ou Shopify. Apenas leitura/testes e documentação no Brain.
