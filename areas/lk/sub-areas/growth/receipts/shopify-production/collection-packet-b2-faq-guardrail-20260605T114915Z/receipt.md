# Receipt — Packet B2 FAQ/corpo guardrail

- Timestamp UTC: 20260605T114915Z
- Aprovação: Lucas Cimino via Telegram — “Aprovo b2”
- Escopo: limpeza de linguagem operacional em mais 25 collections priorizadas, alterando somente `descriptionHtml`/FAQ.
- Excluído: produto, preço, estoque, campanhas, GMC, Klaviyo, checkout e theme production.
- Critério de priorização: maior `products` no lote candidato, excluindo B1.
- Collections alteradas (25): ultimos-lancamentos-2, sneakers, roupas, sale, camiseta-1, air-jordan, todos-special-collections, nike-dunk, onitsuka-tiger-todos-os-modelos, athleisure, acessorios, new-balance-todos-os-modelos, alo-yoga-1, moletom-1, onitsuka-tiger-mexico-66, nude-project, samba, aime-leon-dore, bone-streetwear, saint-studio, acessorios-best-sellers, pace, cloud-dancer, calca-streetwear, collectibles
- Admin QA: 25/25 sem termos-alvo no `descriptionHtml`.
- Backup: `backup-before.json`
- Readback: `readback-after.json`
- Rollback: reaplicar `rollback-payload.json` via `collectionUpdate(descriptionHtml)`
- Revisão de impacto: D+7 usando GA4/GSC/Shopify quando disponível.


## QA público

- Public QA: 24/25 limpas no HTML público para os termos-alvo.
- Resíduo: `collectibles` com `Pronta entrega` apenas na meta description pública.
- Diagnóstico read-only: Admin SEO/metafield global `description_tag` de `collectibles` contém `Pronta entrega`.
- Não alterado porque o escopo aprovado do B2 foi somente `descriptionHtml`/FAQ, sem SEO/meta.
- Public QA salvo em `public-qa.json` e HTMLs por handle.
