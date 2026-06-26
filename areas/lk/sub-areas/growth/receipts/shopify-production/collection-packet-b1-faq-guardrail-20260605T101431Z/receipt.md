# Receipt — Packet B1 FAQ/corpo guardrail

- Timestamp UTC: 20260605T101431Z
- Aprovação: Lucas Cimino via Telegram — “Aprovo b1”
- Escopo: alterar somente `descriptionHtml`/FAQ das 10 collections piloto.
- Excluído: produto, preço, estoque, campanhas, GMC, Klaviyo, checkout e theme production.
- Collections alteradas: lancamentos, nike-todos-os-modelos, adidas-todos-os-modelos, air-jordan-1, new-balance-9060, nike-dunk-sb, yeezy, fear-of-god, jacquemus, nike-air-force-1
- Backup: `backup-before.json`
- Readback: `readback-after.json`
- Rollback: reaplicar `rollback-payload.json` via `collectionUpdate(descriptionHtml)`
- Revisão de impacto: D+7 usando GA4/GSC/Shopify quando disponível.


## QA pós-write

### Admin readback

- 10/10 collections atualizadas via Shopify Admin API.
- 10/10 `descriptionHtml` batem exatamente com o candidato aprovado.
- 10/10 sem os termos-alvo no `descriptionHtml` após readback: `Produtos em estoque`, `Pronta entrega`, `Entrega SP`, `Sujeito a encomenda`, `Estoque limitado`, `rodar`.

### Público / CDN

- Public QA salvo em `public-qa.json` + HTMLs por handle.
- Observação: parte do público ainda serviu versão antiga/edge cache em alguns handles e também há termo logístico vindo de bloco estático do tema (`Envio em até 2 dias úteis para produtos em estoque`), fora do escopo B1 aprovado porque envolve theme production.
- Não fiz alteração de theme production.

### Itens que ainda podem aparecer no público

- Bloco estático do tema: `Envio em até 2 dias úteis para produtos em estoque` em algumas páginas.
- Cache/edge antigo em alguns handles com FAQ anterior (`roda/rodar`). Admin já está limpo; acompanhar propagação antes de novo write.


## Continuação após “Seguir”

- Recheck público feito: 8/10 limpas.
- Cache nudge/reaplicação no escopo B1 feito para `nike-todos-os-modelos` e `new-balance-9060`.
- `nike-todos-os-modelos` limpou no público.
- `new-balance-9060` segue com render antigo no público, apesar de Admin/metafields SEO limpos.
- Próximo packet salvo: `reports/collection-audits/2026-06-05-packet-b2-next-actions-after-b1.md`.
