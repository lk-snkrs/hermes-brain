# Handoff — LK Stock → Product Suggestions v3 / elegibilidade operacional

- Data/hora: 2026-06-27T10:12:16Z
- Origem: lk-shopify
- Destino: lk-stock / Stock OS
- Projeto: PDP Product Suggestions v3 — Motor LK
- Documento base: `areas/lk/sub-areas/shopify/prds/prd-pdp-product-suggestions-v3-motor-lk-20260627.md`
- Status: handoff solicitado/documentado; sem consulta direta de estoque por lk-shopify
- Reminder OS loop needed: yes
- Reminder OS owner: lk-stock
- Reminder OS next action: responder o contrato sanitizado de elegibilidade/campos disponíveis para candidatos PDP v3
- Reminder OS review trigger: retorno do lk-stock ou próxima retomada do Product Suggestions v3
- Reminder OS evidence: este handoff + `areas/lk/sub-areas/shopify/reports/pdp-product-suggestions-v3-readonly-candidates-20260627.md`

## Contexto

Lucas aprovou evoluir o bloco PDP `Você também pode gostar` / `Relacionados` para um motor LK próprio.

O Product Suggestions v2 já está publicado e substituiu o modelo fraco por:

```text
Shopify Recommendations API filtrada + fallback Liquid estrito
```

A próxima versão quer usar sinais melhores, mas respeitando a fronteira:

- `lk-stock` é dono de estoque/disponibilidade/elegibilidade operacional;
- `lk-shopify` não consulta estoque direto;
- ranking visual do PDP continua sendo Shopify/Growth/CRO;
- disponibilidade não deve virar promessa comercial nem ranking principal.

## Pedido ao LK Stock

Responder com um contrato sanitizado de elegibilidade/campos disponíveis para candidatos de recomendação PDP.

Não precisa enviar dados sensíveis nem estoque bruto. O ideal é responder em formato de campos/status.

## Perguntas objetivas

1. Existe campo confiável para `active/sellable` por produto/handle/SKU?
2. Existe status sanitizado de disponibilidade/elegibilidade que possa ser consumido como:
   - `eligible`
   - `ineligible`
   - `unknown`
   - `needs_reconciliation`
3. Existe família/cor/silhouette no Stock OS que possa ajudar agrupamento editorial sem depender de estoque?
4. O Stock OS já possui co-compra ou compra sequencial agregada X→Y?
   - se sim: quais métricas existem? `support`, `confidence`, `lift`, janela 30/90/180 dias?
   - se não: confirmar que isso deve ficar com LK Shopify/Growth em análise agregada de pedidos.
5. Quais caveats devem bloquear um produto como candidato PDP?
   - produto não vendável;
   - divergência Tiny/Shopify;
   - reconciliação pendente;
   - SKU sem mapeamento;
   - outros.

## Formato de resposta sugerido

```json
{
  "scope": "pdp_product_suggestions_v3_eligibility",
  "values_printed": false,
  "fields_available": {
    "sellable_status": true,
    "family": true,
    "color": "unknown",
    "silhouette": "unknown",
    "copurchase_xy": false,
    "sequential_purchase_xy": false
  },
  "eligibility_contract": {
    "key": "handle_or_sku",
    "statuses": ["eligible", "ineligible", "unknown", "needs_reconciliation"],
    "freshness": "describe cadence/source"
  },
  "caveats": [
    "do not promise availability without stock evidence",
    "availability should be final eligibility filter, not PDP ranking score"
  ]
}
```

## Importante

- Não enviar valores de estoque bruto se não for necessário.
- Não expor cliente/pedido/PII.
- Não autoriza qualquer write em Tiny/Shopify.
- Se a evidência não for suficiente, retornar `não confirmado` e indicar reconciliação necessária.

## Próximo passo após retorno

`lk-shopify` monta um packet v3 read-only com:

- candidatos por PDP;
- reason codes;
- separação score vs eligibility;
- QA amostral;
- approval packet DEV antes de qualquer alteração de tema.
