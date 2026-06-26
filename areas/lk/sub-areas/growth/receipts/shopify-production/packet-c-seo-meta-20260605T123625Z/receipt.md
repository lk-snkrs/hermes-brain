# Receipt — Packet C SEO/GEO title-meta

- Timestamp UTC: 20260605T123625Z
- Aprovação: Lucas Cimino via Telegram — “Aprovo packet 3”
- Escopo: aplicar exatamente os title/meta propostos no Packet C.
- Alterado: Shopify collection `seo.title`, `seo.description` e metafields legados `global.title_tag`/`global.description_tag` quando existentes.
- Excluído: descriptionHtml, produto, preço, estoque, theme, campanhas, GMC, Klaviyo e checkout.
- Collections alteradas (8): new-balance-204l, samba, onitsuka-tiger-mexico-66, collectibles, labubu, pop-mart, nike-dunk, air-jordan-1
- Backup: `backup-before.json`
- Readback: `readback-after.json`
- Rollback: `rollback-payload.json`
- Revisão de impacto: D+7 com GSC/GA4/Shopify quando disponível.


## Public QA

- QA público inicial: 7/8 com meta description exata já propagada.
- `onitsuka-tiger-mexico-66` retornou uma versão antiga em uma edge pública, apesar de Admin/readback estar correto.
- Cache nudge/reaplicação dentro do escopo aprovado executado para `onitsuka-tiger-mexico-66`.
- Pós-nudge: resposta pública alternou entre versão nova e versão antiga, indicando cache/edge intermitente.
- Nenhuma alteração fora do escopo foi feita.

## Monitoramento

- Rechecar público em janela curta para `onitsuka-tiger-mexico-66`.
- Revisão D+7: GSC/GA4/Shopify para CTR, impressões, posição e tráfego das 8 collections alteradas.
