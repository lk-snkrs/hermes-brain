# Curadoria LK — Batch 3 aplicado no Dev

Timestamp UTC: 20260602T145716Z

## Aprovação recebida

Lucas aprovou aplicar no dev o Batch 3 com:

- Gazelle
- Air Jordan 4
- Taekwondo Mei Ballet
- Handball Spezial

Restrições aprovadas: separar collab quando fizer sentido; sem mexer em production/produtos/preço/estoque/apps.

## Tema e asset

- Tema dev: `lk-new-theme/dev`
- Theme ID: `155065450718`
- Role verificado antes do write: `unpublished`
- Asset alterado: `snippets/lk-variante-top30-visited.liquid`

## Backups / rollback

Backups antes do write:

- `snippets__lk-variante-top30-visited.liquid.before`
- `sections__lk-pdp.liquid.before`
- `assets__lk-variante.css.before`

Rollback: re-upload do arquivo `snippets__lk-variante-top30-visited.liquid.before` no mesmo tema dev `155065450718`.

## Readback

- Before SHA256: registrado em `qa_asset_synthetic_summary.json`
- After/readback SHA256: registrado em `qa_asset_synthetic_summary.json`
- Readback contém os 4 markers novos:
  - `top30-adidas-gazelle`
  - `top30-air-jordan-4-regular`
  - `top30-adidas-taekwondo-mei`
  - `top30-adidas-handball-spezial`

## Grupos aplicados

### Adidas Gazelle Indoor regular

Critério: excluí collabs/cápsulas óbvias quando havia grupo regular suficiente.

Handles:

- `tenis-adidas-gazelle-indoor-maroon-almost-yellow-marrom`
- `tenis-adidas-gazelle-indoor-cream-white-preloved-teal-branco`
- `tenis-adidas-gazelle-indor-beam-pink-solar-red-rosa`
- `tenis-adidas-gazelle-indoor-better-scarlet-cloud-white-vermelho`
- `tenis-adidas-gazelle-indoor-collegiate-green-verde`
- `tenis-adidas-gazelle-indoor-alumina-black-bege`
- `tenis-adidas-gazelle-indoor-blue-fusion-gum-azul`
- `tenis-adidas-gazelle-indoor-clear-sky-rose-tone-rosa`

### Air Jordan 4 regular

Critério: excluí SB, Off-White, Travis/Nigel/Undefeated quando o grupo regular tinha opções suficientes.

Handles:

- `tenis-air-jordan-4-retro-metallic-gold-branco`
- `tenis-nike-air-jordan-4-retro-black-cat-preto`
- `air-jordan-4-frozen-moments`
- `tenis-nike-air-jordan-4-retro-tex-worn-blue-denim-azul`
- `air-jordan-4-craft-medium-olive`
- `tenis-air-jordan-4-retro-se-paris-we-cement-cinza`
- `tenis-air-jordan-4-retro-military-blue-branco`
- `tenis-air-jordan-4-retro-og-nike-white-cement-couro`

### Adidas Taekwondo Mei Ballet

Critério: mantive apenas produtos Adidas Taekwondo Mei claros; excluí o handle estranho com `onitsuka` apesar de o título aparecer como Adidas, para evitar ruído semântico.

Handles:

- `adidas-taekwondo-mei-ballet-branco-e-preto`
- `tenis-adidas-taekwondo-mei-ballet-preto`
- `adidas-taekwondo-mei-ballet-preto-e-branco`
- `tenis-adidas-taekwondo-mei-ballet-branco-e-prata`
- `tenis-adidas-wmns-taekwondo-mei-white-scarlet-gum-couro`
- `tenis-adidas-taekwondo-mei-ballet-cream-white-branco`
- `tenis-wmns-taekwondo-mei-ballet-adidas-camurca-slip-on-azul`
- `tenis-wmns-taekwondo-mei-ballet-adidas-couro-prata-metalico`

### Adidas Handball Spezial regular

Critério: excluí Sporty & Rich como collab porque havia grupo regular suficiente.

Handles:

- `tenis-adidas-handball-spezial-earth-strata-gum-marrom`
- `tenis-adidas-handball-spezial-bordo`
- `tenis-adidas-handball-spezial-lt-collegiate-green-cream-white-verde`
- `tenis-adidas-handball-spezial-green-pink-velvet-verde`
- `tenis-adidas-handball-spezial-clear-sky-white-warm-sandstone-azul`
- `tenis-adidas-handball-spezial-cream-white-blue-warm-sandstone-branco`
- `tenis-adidas-handball-spezial-lt-preloved-brown-cream-white-marrom`
- `tenis-adidas-handball-spezial-lucid-blue-pink-azul`

## QA

Como os requests públicos sem autenticação estão redirecionando/removendo `preview_theme_id`, a validação do Dev seguiu a referência LK: Asset API readback + simulação determinística do render.

Resultado:

- 4 markers novos presentes no readback do Dev.
- Section `lk-pdp` contém render do snippet depois do preço.
- Para 2 amostras de cada grupo:
  - produto atual reconhecido no grupo;
  - 5 alternativas renderizáveis;
  - 5 imagens disponíveis;
  - produto atual excluído;
  - sem copy `best seller` / `mais vendido`.
- Production control: snippet production não contém os markers do Batch 3.

Detalhes em:

- `batch3_groups.json`
- `qa_asset_synthetic_summary.json`
- `snippets__lk-variante-top30-visited.liquid.readback`

## Não-ações

Não houve:

- write em production;
- produto/tag/metafield write;
- preço;
- estoque;
- checkout;
- app;
- GMC/feed;
- Klaviyo;
- Meta;
- Tiny;
- WhatsApp/campanha/envio.


## Hotfix Dev — imagens quebradas Batch 3 (2026-06-02T15:13:44Z)

### Causa raiz
As URLs de imagem do Batch 3 foram materializadas com scheme duplicado: `https:https://cdn.shopify.com...`.
Isso quebrou os thumbnails no preview do Dev.

### Aprovação
Lucas aprovou no Telegram: `Aprovado: corrigir agora no Dev`.

### Escopo executado
- Tema: `lk-new-theme/dev` / `155065450718` / `unpublished`
- Asset: `snippets/lk-variante-top30-visited.liquid`
- Mudança: normalização de URL somente (`https:https://cdn.shopify.com` → `https://cdn.shopify.com`)
- Ocorrências corrigidas: `32`

### Verificação
- Readback bate com o arquivo preparado: `True`
- Ocorrências malformadas restantes: `0`
- Markers Batch 3 preservados: `True`
- CDN sample checks: 12 imagens testadas, todas com status 200/206 e content-type image
- Production control: `lk-new-theme/production` / `155065417950` / `main` permaneceu sem markers Batch 3: `True`

### Rollback
- Backup imediatamente antes do hotfix: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/lk-variante/dev-batch3-curadoria-20260602T145716Z/snippets__lk-variante-top30-visited.liquid.before-fix-broken-images`
- Readback pós-hotfix: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/lk-variante/dev-batch3-curadoria-20260602T145716Z/snippets__lk-variante-top30-visited.liquid.after-fix-readback`

### Não-ações
Não mexeu em Production, produtos, preço, estoque, checkout, apps, GMC/feed, Klaviyo, Meta, Tiny ou campanhas.


## Auditoria/correção geral de imagens Dev (2026-06-02)

Lucas pediu para corrigir todos os outros thumbnails quebrados. Escopo mantido em Dev.

- Tema: `lk-new-theme/dev` / `155065450718` / `unpublished`
- Asset: `snippets/lk-variante-top30-visited.liquid`
- Write executado nesta auditoria: `False`
- Padrões malformados antes: `{'https:https://cdn.shopify.com': 0, 'https://https://cdn.shopify.com': 0, 'http:https://cdn.shopify.com': 0, '//https://cdn.shopify.com': 0}`
- Padrões malformados depois: `{'https:https://cdn.shopify.com': 0, 'https://https://cdn.shopify.com': 0, 'http:https://cdn.shopify.com': 0, '//https://cdn.shopify.com': 0}`
- URLs CDN únicas verificadas: `147`
- URLs malformadas restantes: `0`
- Checks CDN ruins restantes: `0`
- Production permaneceu sem markers Batch 3: `True`
- Relatório: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/lk-variante/dev-batch3-curadoria-20260602T145716Z/all-images-fix-audit-report.json`


## Auditoria ampliada — todos os assets LK Variante/Curadoria no Dev (2026-06-02)

Após Lucas apontar que o bug poderia afetar todas as coleções/grupos, foi auditado o conjunto de assets do tema Dev que contém `lk-variante`, `Curadoria LK`, `data-lk-variante` ou markers `top30-`.

- Tema: `lk-new-theme/dev` / `155065450718` / `unpublished`
- Assets do tema listados: `427`
- Assets LK Variante/Curadoria auditados: `10`
- Assets auditados: `assets/lk-variante.css, sections/lk-cart.liquid, sections/lk-collection.liquid, sections/lk-geo-source-pages-packet-d.liquid, sections/lk-pdp.liquid, snippets/lk-nike-mind-collection-hero.liquid, snippets/lk-variante-air-jordan-1-low-travis.liquid, snippets/lk-variante-air-jordan-1-low.liquid, snippets/lk-variante-samba-jane.liquid, snippets/lk-variante-top30-visited.liquid`
- Writes corretivos adicionais nessa auditoria: `[]`
- Padrões malformados totais antes: `0`
- Padrões malformados totais depois: `0`
- URLs CDN verificadas nos assets auditados: `208`
- URLs com formato ruim após auditoria: `0`
- Checks CDN ruins após auditoria: `8`
- Production permaneceu sem Batch 3 no top30: `True`
- Relatório JSON: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/lk-variante/dev-batch3-curadoria-20260602T145716Z/all-curadoria-assets-image-audit-20260602T1519Z/report.json`


## Hotfix Dev — imagens 404 Lululemon/apparel inline em lk-pdp (2026-06-02)

Após auditoria ampliada dos assets LK Variante/Curadoria, foram encontrados 8 thumbnails 404 no bloco inline Lululemon de `sections/lk-pdp.liquid`. As imagens foram substituídas por URLs atuais lidas do próprio produto via Shopify Admin GET por handle.

- Tema: `lk-new-theme/dev` / `155065450718` / `unpublished`
- Asset: `sections/lk-pdp.liquid`
- Handles Lululemon tratados: `jaqueta-lululemon-define-nulu, jaqueta-lululemon-define-luon-white-branco, jaqueta-lululemon-define-nulu-black-gold-preto, jaqueta-lululemon-define-nulu-black-plum-gold-roxo, define-cropped-jacket-nulu, short-lululemon-shake-it-out-high-rise-running-2-5, calca-lululemon-daydrift-regular, camiseta-lululemon-hold-tight-henley, short-lululemon-hotty-hot-high-rise-lined-4, pullover-lululemon-heavyweight-fleece-tennis-club`
- Replacement image checks: `10` OK
- URLs CDN na section verificadas após hotfix: `28`
- URLs CDN ruins restantes na section: `0`
- Production permaneceu sem Batch 3 no top30: `True`
- Backup rollback: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/lk-variante/dev-batch3-curadoria-20260602T145716Z/lulu-inline-images-fix-20260602T1528Z/sections__lk-pdp.liquid.before`
- Relatório: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/lk-variante/dev-batch3-curadoria-20260602T145716Z/lulu-inline-images-fix-20260602T1528Z/report.json`


## Auditoria final pós-hotfix — todos assets LK Variante/Curadoria Dev (2026-06-02)

- Assets auditados: `10`
- URLs CDN verificadas: `208`
- URLs CDN ruins restantes: `0`
- Schemes malformados restantes: `0`
- Relatório: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/lk-variante/dev-batch3-curadoria-20260602T145716Z/post-lulu-fix-full-curadoria-image-audit-20260602T1530Z/report.json`
