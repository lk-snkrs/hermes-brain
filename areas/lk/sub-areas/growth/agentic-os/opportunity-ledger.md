# Opportunity Ledger — LK Growth OS

Data de criação: 2026-06-05
Status: operacional local/read-only.

## Função

Registrar oportunidades Growth de forma comparável, evitando decisões por feeling ou por relatório genérico. Cada oportunidade deve ter evidência, score 0-100, risco, próximo output e follow-up.

## Score 0-100

- Impacto comercial: 0-25
- Evidência/demanda: 0-20
- Confiança de diagnóstico: 0-15
- Esforço: 0-10, invertido
- Risco operacional: 0-10, invertido
- Clareza de rollback/readback: 0-10
- Aderência a padrão canônico LK: 0-10; se for LKGOC, abrir `CollectionOptimizerHandoff` e não pontuar como execução Growth

## Classificação

- `hot`: 85-100 — levar para decisão/packet prioritário.
- `qualified`: 70-84 — preparar brief/preview.
- `backlog`: 50-69 — manter, pedir evidência ou timing.
- `discarded`: <50 — não acionar Lucas, salvo risco/exceção.

## Template de registro

```yaml
id: GROWTH-OPP-YYYYMMDD-001
created_at: YYYY-MM-DDTHH:MM:SSZ
source_inbox_id: GROWTH-INBOX-YYYYMMDD-001
status: hot | qualified | backlog | discarded | done | blocked
area: SEO | GEO | CRO | GMC | GA4 | GSC | ContentNonLKGOC | PDP | CollectionOptimizerHandoff | Other
object:
  type: product | collection | page | query | issue | segment | theme | other
  identifier: "URL/handle/query/SKU/etc"
hypothesis: "se fizermos X, esperamos Y porque Z"
evidence:
  - source: Shopify | GA4 | GSC | GMC | SERP | DataForSEO | Brain | Browser | Other
    summary: "evidência curta"
    link: null
score:
  commercial_impact: 0
  evidence_demand: 0
  diagnostic_confidence: 0
  effort_inverse: 0
  operational_risk_inverse: 0
  rollback_readback_clarity: 0
  canonical_fit: 0
  total: 0
risk_level: A0 | A1 | A2 | A3 | A4
next_output: brief | preview | approval_packet | handoff_shopify | handoff_ops | impact_review | no_action
approval_needed: true | false
handoff_target: none | lk-shopify | lk-ops | lk-trends | hermes-geral
follow_up_metric: "CTR/conversão/receita/issues/etc"
review_due: YYYY-MM-DD | null
links:
  brief: null
  preview: null
  packet: null
  receipt: null
  impact_review: null
notes: []
```

## Regras de uso

1. O ledger não substitui fonte viva; ele aponta para a fonte.
2. O score precisa ser rebaixado se faltarem GA4/GSC/GMC/Shopify quando eles forem essenciais.
3. Oportunidade com write externo vira approval packet antes de execução.
4. Oportunidade concluída com alteração aprovada precisa impact review D+7/D+14/D+30 quando mensurável.

## Entradas atuais

Sem entradas novas nesta criação. Usar no próximo fluxo real.
