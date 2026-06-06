# Inbox Growth — LK Growth OS

Data de criação: 2026-06-05
Status: operacional local/read-only; não aciona writes externos por si só.

## Função

Fila única de entradas para o agente-funcionário **LK Growth**. Tudo que chega aqui deve virar uma decisão operacional clara: descartar, pedir evidência, gerar score, preparar brief, preparar approval packet, rotear para LK Shopify/LK Ops/LK Trends, ou registrar como backlog.

## Regra central

Nenhum item de inbox autoriza ação externa. A inbox só organiza trabalho local/read-only/documental até existir aprovação escopada quando necessária.

## Estados

- `new`: entrada bruta ainda não classificada.
- `triaged`: contexto, risco e fonte necessária definidos.
- `evidence-needed`: falta dado vivo/fonte para ser decision-grade.
- `scored`: oportunidade pontuada 0-100.
- `briefing`: virando brief/diagnóstico.
- `approval-packet`: precisa decisão de Lucas para write/produção/externo.
- `handoff-shopify`: precisa preview/QA/readback do LK Shopify.
- `handoff-ops`: depende de preço, estoque, Tiny, atendimento ou promessa comercial.
- `blocked`: bloqueado por risco, falta de fonte ou aprovação.
- `done`: concluído com output/receipt.

## Campos obrigatórios por item

```yaml
id: GROWTH-INBOX-YYYYMMDD-001
created_at: YYYY-MM-DDTHH:MM:SSZ
source: Lucas | LK Growth cron | LK Shopify | LK Trends | LK Ops | Hermes Geral | external-signal
request: "descrição curta"
context: SEO | GEO | CRO | GMC | GA4 | GSC | ContentNonLKGOC | PDP | Reviews | PaidSignal | CollectionOptimizerHandoff | Other
risk_level: A0 | A1 | A2 | A3 | A4
status: new
owner: lk-growth
source_of_truth_needed:
  - Shopify read-only
  - GA4
  - GSC
  - GMC
  - SERP/DataForSEO
  - Brain
  - Other
initial_hypothesis: "hipótese inicial"
required_output: diagnosis | score | brief | preview | approval_packet | handoff | receipt | backlog
approval_needed_before_write: true | false
handoff_target: none | lk-shopify | lk-ops | lk-trends | hermes-geral
links:
  evidence: null
  score: null
  packet: null
  receipt: null
notes: []
```

## Critérios de triagem

### Vai para LK Growth

- problema/oportunidade de tráfego, SEO, GEO, CRO, GMC, GSC, GA4;
- FAQ/schema/source page não-LKGOC; quando for LKGOC, coleção otimizada ou guia de coleção, rotear para `[LK] Otimização de Coleções`;
- priorização por impacto comercial ou demanda.

### Vai para LK Shopify

- aplicar em Shopify;
- produto, coleção, page, theme/dev theme, menu, tag, metafield, SEO field, SKU/variant;
- snapshot, preview técnico, readback, rollback.

### Vai para LK Ops/Tiny

- estoque, preço, disponibilidade, promessa comercial, pedido, cliente, Tiny.

## Output mínimo por status

- `triaged`: contexto + risco + fonte necessária.
- `scored`: score 0-100 + justificativa curta.
- `approval-packet`: item exato + diff/preview + risco + rollback + readback.
- `handoff-shopify`: hipótese Growth + objeto Shopify + resultado esperado + risco.
- `done`: link de report/receipt + próxima revisão de impacto quando aplicável.

## Primeira fila operacional

Ainda sem itens ativos nesta criação. Próximo passo: usar esta inbox para a primeira demanda real de Growth/GMC/CRO/SEO não-LKGOC. Demandas LKGOC vão para `[LK] Otimização de Coleções`.
