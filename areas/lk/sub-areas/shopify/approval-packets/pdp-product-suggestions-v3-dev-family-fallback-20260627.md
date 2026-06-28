# Approval packet — PDP Product Suggestions v3 DEV — family fallback + Stock eligibility contract

- Data/hora: 2026-06-27T11:00:00Z
- Agente/profile: lk-shopify
- Superfície: Shopify DEV theme / PDP `Você também pode gostar`
- Escopo: Product Suggestions v3 em DEV, sem Production merge
- Writes executados até agora: 0
- Consulta direta de estoque: 0
- values_printed=false

## Histórico verificado

- v2 publicado em Production: `areas/lk/sub-areas/shopify/receipts/pdp-product-suggestions-v2-production-merge-20260626.md`
- Packet v3/PRD: `areas/lk/sub-areas/shopify/prds/prd-pdp-product-suggestions-v3-motor-lk-20260627.md`
- Packet read-only v3 candidatos: `areas/lk/sub-areas/shopify/reports/pdp-product-suggestions-v3-readonly-candidates-20260627.md`
- Fonte família ALD hats: `areas/lk/sub-areas/shopify/reports/pdp-product-suggestions-v3-ald-hats-family-source-20260627.md`
- Handoff Stock: `areas/lk/sub-areas/stock/handoffs/2026-06-27-product-suggestions-v3-eligibility-from-lk-shopify.md`

## O que foi feito nos passos 1–3

### 1. LK Stock / elegibilidade

Handoff funcional atualizado com Reminder OS:

- owner: `lk-stock`
- próxima ação: responder contrato sanitizado de elegibilidade/campos disponíveis;
- status esperado: `eligible`, `ineligible`, `unknown`, `needs_reconciliation`;
- restrição: lk-shopify não consulta estoque diretamente.

**Status atual:** pendente do `lk-stock`. Para DEV visual, a implementação pode marcar eligibility como `unknown` e não prometer disponibilidade.

### 2. Fonte família / Curadoria para acessórios ALD hats

Foi criada uma fonte read-only `ald-hats` a partir de:

- Shopify public search suggest;
- product.js público;
- snippet Curadoria LK existente `lk-variante-ald-hats-saint-george-20260626`.

Candidatos adicionais após dedupe da Curadoria atual:

| handle | papel |
|---|---|
| `bone-aime-leon-dore-unisphere-preto` | fallback família ALD hats |
| `bone-6-panel-aime-leon-dore-cycling-logo-azul` | fallback família ALD hats |
| `bone-5-panel-aime-leon-dore-unisphere-azul` | fallback família ALD hats |
| `bone-5-panel-aime-leon-dore-unisphere-branco` | fallback família ALD hats |
| `bone-aime-leon-dore-washed-script-jet-black-preto` | fallback família ALD hats |
| `bone-aime-leon-micro-logo-hat-jet-black-preto` | fallback família ALD hats |
| `bone-aime-leon-dore-x-porsche-colorblock-logo-pristine-off-white` | fallback família ALD hats |

### 3. Approval packet DEV v3

Este documento é o approval packet DEV. Nenhuma alteração foi aplicada ainda.

## Problema que o v3 resolve

No PDP Saint George:

`bone-aime-leon-dore-saint-george-logo-hat-bege-marrom`

O v2 filtra corretamente, mas depois de:

- excluir o produto atual;
- deduplicar Curadoria LK;
- bloquear camisetas/moletom/apparel;
- bloquear cross-type;

sobram **0 candidatos fortes** para o bloco inferior.

Com o fallback família `ald-hats`, o v3 passa a ter candidatos de boné ALD adicionais sem depender de camiseta/apparel e sem duplicar a Curadoria atual.

## Implementação DEV proposta

Arquivo provável:

- `sections/lk-pdp.liquid`

Mudanças DEV:

1. Manter Product Suggestions v2 como base.
2. Adicionar `data-lk-related-v3="family-fallback-20260627"` no wrapper do bloco.
3. Adicionar mapa leve de famílias, inicialmente:

```json
{
  "ald-hats": [
    "bone-aime-leon-dore-unisphere-preto",
    "bone-6-panel-aime-leon-dore-cycling-logo-azul",
    "bone-5-panel-aime-leon-dore-unisphere-azul",
    "bone-5-panel-aime-leon-dore-unisphere-branco",
    "bone-aime-leon-dore-washed-script-jet-black-preto",
    "bone-aime-leon-micro-logo-hat-jet-black-preto",
    "bone-aime-leon-dore-x-porsche-colorblock-logo-pristine-off-white"
  ]
}
```

4. Ativar fallback de família somente quando:
   - produto atual for detectado como `ald-hats`;
   - Recommendations API filtrada + dedupe tiver menos de 2 candidatos;
   - candidato não estiver na Curadoria LK detectável;
   - candidato não for produto atual;
   - candidato tiver tipo/família compatível.
5. Eligibility inicial no DEV: `unknown/pending_lk_stock`, sem texto público de disponibilidade.
6. Esconder bloco se, mesmo após family fallback, houver menos de 2 candidatos.

## Critérios de aceite DEV

### PDP Saint George

- HTTP `200`.
- Liquid errors `0`.
- JS exceptions `0`.
- `data-lk-related-v3="family-fallback-20260627"` presente.
- Bloco inferior mostra bonés ALD adicionais.
- Não mostra camiseta/moletom/apparel como sugestão de boné.
- Não duplica handles já exibidos na Curadoria LK.
- Não promete estoque/disponibilidade.

### PDPs de controle

- Air Jordan 1 Low Panda: continua com AJ1 Low coerentes.
- Onitsuka Mexico 66: continua com Mexico 66 coerentes.
- NB9060 Quartz Grey: mantém regras históricas/co-compra quando aplicável.
- Vomero Premium: continua com Vomero Premium coerentes.

## Risco

| Risco | Nível | Mitigação |
|---|---:|---|
| Duplicar Curadoria LK | Médio | dedupe por handles detectados no DOM/snippet |
| Sugerir cross-type ruim | Médio | bloqueio por tipo/família antes de renderizar |
| Candidato público sem elegibilidade Stock | Médio | DEV visual com eligibility `unknown`; Production só após contrato Stock ou aceite explícito desse risco |
| Regressão em PDPs de tênis | Médio | QA com AJ1, Onitsuka, NB9060, Vomero |

## Rollback DEV

- Restaurar snapshot DEV anterior de `sections/lk-pdp.liquid`.
- Remover marker `data-lk-related-v3` e mapa `ald-hats`.
- Voltar ao Product Suggestions v2 já publicado.

## Fora de escopo

- Sem Production merge.
- Sem Shopify produto/metafield/preço/estoque.
- Sem Tiny.
- Sem GMC/Klaviyo/ads/WhatsApp/email.
- Sem promessa de disponibilidade.
- Sem consulta direta de estoque pelo lk-shopify.

## Aprovação necessária para aplicar em DEV

> Aprovo DEV Product Suggestions v3 no PDP com fallback família ALD hats, eligibility Stock como pending/unknown, sem Production merge.

## Reminder OS

- loop needed: yes
- owner: lk-shopify
- next action: aguardar aprovação DEV ou retorno do lk-stock; se aprovado, aplicar só em DEV e validar os PDPs acima
- review trigger: resposta de Lucas com aprovação DEV ou resposta do lk-stock ao handoff
- evidence: este approval packet + packets read-only v3
