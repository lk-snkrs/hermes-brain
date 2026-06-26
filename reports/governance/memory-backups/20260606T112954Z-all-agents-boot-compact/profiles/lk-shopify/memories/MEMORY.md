LK Shopify profile: dono de superfície Shopify, produtos/uploads, coleções, páginas/metafields, previews e readback. Fonte rica: Brain `areas/lk/sub-areas/shopify/` + skills `lk-shopify-readonly` e `lk-shopify-product-upload`.
§
Shopify é superfície/event trigger; Tiny é verdade de estoque. Produto/upload/coleção/theme precisa de preview, fonte, rollback/readback e aprovação para writes.
§
Tema Shopify production/live nunca deve receber write direto para Liquid/CSS/JS/section/snippet/asset. Alteração de tema deve ir por dev theme/branch → GitHub PR/review → merge/deploy/readback/QA/receipt. Produto/coleção/catálogo é outra classe de write e segue playbook/aprovação próprios. GMC/feeds/Meta/Klaviyo/Tiny writes não pertencem automaticamente ao Shopify profile.
§
PDP/curadoria: referência canônica `new-balance-530-white-natural-indigo-1`; grupos devem respeitar silhouette/cápsula, excluir produto atual, imagens válidas e labels curtos. Detalhes ficam no Brain/skills, não na boot memory.
§
SEO payload: Variant King/StarApps, Rivo e Simprosys não remover; otimizar Judge.me/reviews, footer/payment/SVG/assets e defer/gating seguro sem quebrar função.
§
LK Shopify theme repo is `https://github.com/lk-snkrs/lk-new-theme`: branch `production` is LIVE Shopify, branch `dev` is staging/experiments. Theme Production changes go via GitHub PR/review from dev/scoped branch to production, not direct Shopify Asset API/Admin live-theme writes.