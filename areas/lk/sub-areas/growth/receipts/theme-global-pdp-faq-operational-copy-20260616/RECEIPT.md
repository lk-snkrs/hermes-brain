# Receipt — Correção FAQ global PDP

Executado em: 2026-06-16T18:48:18.787487+00:00

## Status
- Aprovação recebida: sim, no turno atual.
- Theme production alterado: sim, asset `sections/lk-pdp.liquid`.
- Escopo do patch: troca de texto em 2 ocorrências — FAQ visual + JSON-LD FAQ.
- Shopify product fields/feed/campanhas/Klaviyo: não alterados.
- Secrets: não impressos (`values_printed=false`).

## Texto removido
`Itens confirmados são preparados com agilidade. O prazo varia conforme sua região. Produtos sob encomenda: 4 a 6 semanas.`

## Texto aplicado
`Itens confirmados são preparados com cuidado e o prazo varia conforme a região e a confirmação do pedido. Se houver qualquer dúvida antes da compra, a equipe LK orienta pelo chat.`

## Evidência
- Backup asset: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/theme-global-pdp-faq-20260616/apply-20260616T184514Z/sections__lk-pdp.before.liquid`
- Asset local after: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/theme-global-pdp-faq-20260616/apply-20260616T184514Z/sections__lk-pdp.after.local.liquid`
- Apply result: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/theme-global-pdp-faq-20260616/apply-20260616T184514Z/apply-result.json`
- Asset readback QA: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/theme-global-pdp-faq-20260616/apply-20260616T184514Z/asset-readback-qa.json`
- Public final QA 10 PDPs: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/theme-global-pdp-faq-20260616/apply-20260616T184514Z/public-final-10-qa.json`
- Rollback script: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/theme-global-pdp-faq-20260616/apply-20260616T184514Z/rollback_sections_lk_pdp_from_backup.py`

## QA
- Asset readback: OK — old_count=0, new_count=2.
- Public HTML amostra 10 PDPs: 8/10 já propagados.
- Ainda em cache antigo no último fetch:
  - `tenis-new-balance-9060-mushroom-arid-stone-camurca`
  - `tenis-onitsuka-tiger-mexico-66-sd-kill-bill-amarelo`

## Interpretação
A alteração está salva e confirmada no asset production. A divergência remanescente é propagação/cache de HTML público por PDP/edge, porque o readback do asset já não contém o texto antigo.

## Rollback
Rollback preparado usando o backup anterior do asset. Executar somente com aprovação explícita ou falha crítica.

## Próximo controle
Recheck público em D0/D1 até 10/10 PDPs não mostrarem mais `sob encomenda`/`4 a 6 semanas`.