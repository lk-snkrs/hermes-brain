# Preview Queue — LK Shopify OS

Data de criação: 2026-06-05
Status: operacional local/read-only; execução externa depende de aprovação escopada.

## Função

Controlar a fila de previews técnicos do LK Shopify. A fila existe para impedir que uma ideia vire write sem snapshot, diff, QA, risco, readback e rollback.

## Estados

- `queued`: item entrou na fila.
- `drafting`: preview em construção.
- `qa-needed`: precisa QA visual/técnico.
- `packet-ready`: approval packet pronto.
- `approved`: aprovado em escopo exato.
- `executed`: execução realizada.
- `readback-ok`: readback verificado.
- `receipt-done`: receipt salvo.
- `blocked`: bloqueado.
- `cancelled`: cancelado.

## Score técnico/risco 0-100

- Escopo exato do objeto: 0-15
- Fonte viva verificada: 0-15
- Preview/diff claro: 0-15
- QA técnico/visual: 0-15
- Risco de impacto em produção: 0-10, invertido
- Rollback pronto: 0-10
- Readback verificável: 0-10
- Aderência a padrão canônico: 0-10

## Template de registro

```yaml
id: SHOPIFY-PREVIEW-YYYYMMDD-001
created_at: YYYY-MM-DDTHH:MM:SSZ
source_inbox_id: SHOPIFY-INBOX-YYYYMMDD-001
originating_agent: lk-shopify | lk-growth | lk-ops | lk-trends | hermes-geral
status: queued
object:
  type: product | variant | collection | page | theme | section | snippet | asset | css | menu | tag | metafield | seo_field | price | promo | cart_drawer | feature | app_config | tracking | other
  identifier: "handle/id/url/theme/etc"
change_summary: "o que mudaria"
preview_type: local_doc | diff | dev_theme | browser_screenshot | payload_preview | other
risk_level: A0 | A1 | A2 | A3 | A4
score:
  object_scope: 0
  live_source_verified: 0
  preview_diff_clarity: 0
  technical_visual_qa: 0
  production_risk_inverse: 0
  rollback_ready: 0
  readback_verifiable: 0
  canonical_fit: 0
  total: 0
approval:
  needed: true
  approved: false
  approved_by: null
  approved_at: null
  exact_scope: null
snapshots:
  before: null
  preview: null
  after_readback: null
rollback:
  artifact: null
  tested: false
qa:
  desktop: not_applicable | pending | pass | fail
  mobile: not_applicable | pending | pass | fail
  technical: pending | pass | fail
links:
  packet: null
  receipt: null
  related_growth_opportunity: null
notes: []
```

## Critério mínimo para pedir aprovação

Antes de pedir aprovação para write, precisa ter:

1. objeto exato;
2. fonte viva ou snapshot before;
3. preview/diff claro;
4. risco declarado;
5. rollback definido;
6. readback verificável;
7. escopo do que **não** está aprovado.

## Entradas atuais

Sem entradas novas nesta criação. Usar no próximo fluxo real.
