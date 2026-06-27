# Receipt — Onitsuka Tiger Gymnarina — SEO/FAQ/schema publicado

- Data/hora: 2026-06-26T15:48:45.865605+00:00
- Agente/profile/cron: lk-collection-optimizer / LKGOC via lk-growth runtime
- Empresa/área: LK / collection-optimizer
- Responsável humano: Lucas + Hermes
- Pedido original: Melhorar a nova coleção Onitsuka Tiger Gymnarina pensando em SEO, performance, JSON FAQ e padrão aplicado nas outras coleções.
- Classificação: external-write
- Fontes usadas:
- Shopify Admin GraphQL read/write; storefront público; DataForSEO SERP mobile Brasil; Hypebae release; Brain LKGOC/Onitsuka receipts.
- O que foi feito:
- Snapshot Admin antes; body_html reestruturado com intro, bloco citável LK, como escolher e FAQ; SEO title/description definidos; FAQPage JSON-LD único inserido; readback Admin e público executados.
- Output/artefato:
- Workdir: /opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/work/onitsuka-tiger-gymnarina-20260626; URL: https://lksneakers.com.br/collections/onitsuka-tiger-gymnarina; SEO title: Onitsuka Tiger Gymnarina Original | LK Sneakers; public readback confirmou meta nova, FAQPage=1, CollectionPage/ItemList, canonical OK, sem Liquid error.
- Aprovação: Aprovação operacional no turno atual: Lucas pediu explicitamente 'preciso que faça e aprimore os pontos citados' para a coleção recém-criada. Escopo limitado à collection object SEO/body/schema; não houve tema main, preço, estoque, GMC, campanha ou Klaviyo.
- Envio/publicação: Sem envio externo/customer outreach; alteração publicada na coleção Shopify.
- Writes externos: Shopify collection gid://shopify/Collection/1128965603550: descriptionHtml e seo title/description.
- Riscos/bloqueios: CDN/storefront apresentou propagação variável nos primeiros polls; último poll com cache-buster confirmou versão nova. Theme parece renderizar parte do description como texto limpo/strip_html no banner, mas JSON-LD está presente e FAQ textual é encontrável. Não foram feitos ajustes de source map llms.txt/agents.md nesta rodada.
- Rollback/mitigação: Restaurar snapshot-before-admin.json via collectionUpdate para descriptionHtml e SEO null/anteriores. Snapshot em workdir/snapshot-before-admin.json.
- Próximos passos: D+7: revisar GSC/GA4/Search Console quando houver dados; opcional: incluir Gymnarina em llms.txt/agents.md/source map após aprovação específica para theme/source map; QA visual mobile/desktop se o tema precisar renderizar headings do guia como HTML.
- Onde foi documentado no Brain: Brain receipt criado por receipt_writer; workdir contém candidate-body.html, candidate-seo.json, apply-result.json, admin-readback-after.json, public-readback-success-summary.json e polls.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
