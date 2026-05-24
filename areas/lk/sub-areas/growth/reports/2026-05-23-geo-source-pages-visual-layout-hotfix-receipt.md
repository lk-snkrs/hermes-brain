# Recibo — Hotfix visual Source Pages SEO/GEO LK

Data: 2026-05-23
Status: publicado em Shopify production

## Correção solicitada por Lucas

1. Nenhum post/guia SEO-GEO deve sair sem foto/hero.
2. Os guias devem seguir a mesma lógica visual minimalista/editorial da página de Autenticidade LK.

## Ações executadas

- Atualizado `body_html` das 3 páginas-fonte com layout editorial mobile-first, hero com foto de catálogo LK, cards de pilares, navegação relacionada, CTA e schema.
- Criada seção fallback `sections/lk-geo-source-pages.liquid` e template `templates/page.geo-source.json` para estabilizar o DOM público quando o cache de `page.content` da Shopify alternou entre versões antigas.
- Recriadas as páginas nos mesmos handles após cache persistente, mantendo os URLs finais públicos.
- Atualizada skill `lk-shopify-theme-operations`: hero/foto agora é obrigatório para posts/guias SEO-GEO e source pages.
- Atualizada memória do usuário: publicar sempre link Shopify no Telegram e exigir foto/hero.

## URLs finais para revisão mobile

- Onitsuka Tiger: https://lksneakers.com.br/pages/onitsuka-tiger-original-brasil
- New Balance 204L: https://lksneakers.com.br/pages/new-balance-204l-original-brasil
- Adidas SL 72: https://lksneakers.com.br/pages/adidas-sl-72-og-vs-rs

## Verificação pública

Verificação final via storefront `.com.br` com cache-busting:

- Onitsuka: hero visual OK, imagem OK, bloco SEO interno ausente, termos proibidos ausentes.
- New Balance 204L: hero visual OK, imagem OK, bloco SEO interno ausente, termos proibidos ausentes.
- Adidas SL 72: hero visual OK em retry final, imagem OK, bloco SEO interno ausente, termos proibidos ausentes.

Observação: durante a publicação, a Shopify/CDN alternou temporariamente entre edge caches antigos e novos. A camada Admin e assets do tema leram corretamente; o storefront estabilizou por retry. Se Lucas abrir e ainda vir uma versão antiga por alguns minutos, tratar como propagação de CDN, não falha de conteúdo.

## Backups / rollback

Backups e recibos locais:

- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/shopify-source-pages/visual-layout-hotfix-20260523-100640/`
- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/shopify-source-pages/theme-section-visual-sync-20260523-100820/`
- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/shopify-source-pages/recreate-cache-bust-20260523-101040/`

Rollback: restaurar páginas antigas arquivadas a partir dos JSON `old.before.json`, remover os novos IDs criados, e restaurar os assets `sections/lk-geo-source-pages.liquid` / `templates/page.geo-source.json` a partir dos arquivos `.before`.
