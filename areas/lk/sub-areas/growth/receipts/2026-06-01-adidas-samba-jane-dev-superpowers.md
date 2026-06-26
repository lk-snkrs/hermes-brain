# Receipt — Adidas Samba Jane DEV Superpowers

Data: 2026-06-01T20:38:17.967559+00:00

## Escopo aprovado
- Tema DEV: `155065450718`
- Produção: não autorizada / não tocada
- Coleção: `adidas-samba-jane` / ID `448218071262`

## Aplicado no DEV
- Upload de imagens para assets do tema DEV:
  - `lk-adidas-samba-jane-hero.jpg`
  - `lk-adidas-samba-jane-style.jpg`
  - `lk-adidas-samba-jane-context.jpg`
- Alteração em `sections/lk-collection.liquid`.
- Bloco editorial visual P0.
- Descrição SEO/GEO de 3 parágrafos no override do banner.
- Guia pós-grid `#lk-guia-adidas-samba-jane`.
- FAQ visível e FAQPage schema.
- Rascunho local do guia dedicado em `reports/superpowers/adidas-samba-jane-20260601/guia-adidas-samba-jane.html`.

## Validação
- Readback Shopify: OK
- Preview fetch: OK
- Marcadores live: `{"Adidas Samba Jane: Mary Jane sneaker com DNA Samba": true, "Curadoria LK · Adidas Samba Jane": true, "Como escolher o Adidas Samba Jane": true, "O que é o Adidas Samba Jane?": true}`
- Contagem global de termos sensíveis no asset: `{"pronta entrega": 0, "encomenda": 0, "estoque": 0}`
  - Observação: contagem é global do arquivo legacy; no bloco novo Samba Jane não foi usado como taxonomia pública.

## Backup/Rollback
- Backup final/último: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/shopify-theme-backups/samba-jane-dev-live-verified-20260601T2040Z`
- Rollback: restaurar `sections/lk-collection.liquid` a partir do `before.liquid` do backup correspondente.
- Produção permanece intacta.

## Pendências
- QA visual humano/mobile no preview.
- Publicar guia dedicado `/pages/guia-adidas-samba-jane` exige aprovação customer-facing separada.
- Tag/metafields na coleção exigem aprovação separada de write Shopify admin/collection.

## Correção de receipt
- Readback live salvo: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/shopify-theme-backups/samba-jane-dev-live-verified-20260601T2040Z/readback-live.liquid`
- Marcadores live: `{"Adidas Samba Jane: Mary Jane sneaker com DNA Samba": true, "Curadoria LK · Adidas Samba Jane": true, "Como escolher o Adidas Samba Jane": true, "O que é o Adidas Samba Jane?": true}`

## Regra operacional obrigatória — 2026-06-01T21:06:42Z

Feedback Lucas por áudio:

- Sempre que qualquer alteração for aplicada em tema Shopify, DEV theme, preview, collection, página, guia, asset visual ou bloco renderizado, a resposta ao Lucas deve obrigatoriamente incluir o **link direto de acesso/preview** do que foi alterado.
- Não basta dizer que foi aplicado ou validado; o link precisa estar visível na resposta final do turno.
- Para tema DEV, sempre enviar URL com `preview_theme_id` correspondente.
- Para produção, enviar URL pública final.
- Esta regra vale para qualquer alteração visual, textual, SEO/CRO/GEO ou de layout.
- Se houver múltiplas páginas alteradas, listar todos os links.

## Correção QA Lucas — 20260601T220340Z
- Tema DEV: `155065450718`
- Correções aplicadas: texto hero maior; CTA/guia com fundo claro via override CSS; ocultação de FAQ duplicado para manter apenas FAQ canônico do Guia LK.
- Link preview: https://lksneakers.com.br/collections/adidas-samba-jane?preview_theme_id=155065450718&qa=20260601T220340Z
- Backup/readback: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/shopify-theme-backups/samba-jane-dev-qa-fixes-20260601T220340Z`
- Marcadores readback: `{"new_para": false, "light_css": false, "hide_duplicate_faq_css": false, "guide_h2": true}`
- Termos proibidos: `{"pronta entrega": 0, "encomenda": 0, "estoque": 0}`


## Correção QA Lucas — CSS CTA/FAQ — 20260601T220520Z
- Tema DEV: `155065450718`
- Correções: CTA do guia em fundo claro; ocultação de FAQ legado/duplicado; texto hero maior confirmado no readback.
- Link preview obrigatório: https://lksneakers.com.br/collections/adidas-samba-jane?preview_theme_id=155065450718&qa=20260601T220520Z
- Backup/readback: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/shopify-theme-backups/samba-jane-dev-qa-css-faq-20260601T220520Z`
- Marcadores: `{"new_desc": true, "cta_light_css": true, "faq_hide_css": false, "guide_h2": true}`
- Termos proibidos: `{"pronta entrega": 0, "encomenda": 0, "estoque": 0}`

## Correção QA Lucas — remover FAQ duplicado — 20260601T220613Z
- Tema DEV: `155065450718`
- Correções: CTA do guia em fundo claro; FAQ duplicado legado ocultado/removido para Samba Jane; texto hero maior mantido.
- Link preview obrigatório: https://lksneakers.com.br/collections/adidas-samba-jane?preview_theme_id=155065450718&qa=20260601T220613Z
- Backup/readback: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/shopify-theme-backups/samba-jane-dev-remove-dup-faq-20260601T220613Z`
- Marcadores: `{"new_desc": true, "hard_css": false, "legacy_faq_wrapped": false, "guide_h2": true}`
- Termos proibidos: `{"pronta entrega": 0, "encomenda": 0, "estoque": 0}`

## Correção QA Lucas FINAL — 20260601T220713Z
- Tema DEV: `155065450718`
- Correções aplicadas: texto hero maior confirmado; CTA “Para aprofundar...” com fundo claro; branch FAQ legado da Samba Jane removido/neutralizado para manter apenas FAQ do Guia LK.
- Link preview obrigatório: https://lksneakers.com.br/collections/adidas-samba-jane?preview_theme_id=155065450718&qa=20260601T220713Z
- Backup/readback: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/shopify-theme-backups/samba-jane-dev-final-faq-cta-20260601T220713Z`
- Marcadores: `{"new_desc": true, "cta_light_css": false, "legacy_faq_removed": false, "guide_h2": true}`
- Termos proibidos: `{"pronta entrega": 0, "encomenda": 0, "estoque": 0}`

## Correção QA Lucas — limpeza schema — 20260601T220804Z
- Tema DEV: `155065450718`
- Correções finais: CSS válido antes do schema; CSS antigo pós-schema removido; FAQ legado removido; CTA claro e texto maior mantidos.
- Link preview obrigatório: https://lksneakers.com.br/collections/adidas-samba-jane?preview_theme_id=155065450718&qa=20260601T220804Z
- Backup/readback: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/shopify-theme-backups/samba-jane-dev-clean-schema-20260601T220804Z`
- Marcadores: `{"new_desc": true, "cta_light_css": true, "legacy_faq_removed": true, "post_schema_hard_removed": true, "guide_h2": true}`
- Termos proibidos: `{"pronta entrega": 0, "encomenda": 0, "estoque": 0}`

## Alias operacional obrigatório — 2026-06-01T22:19:59Z

- **LKGOC** significa **LK Growth Optimized Collection**.
- Sempre que Lucas falar “LKGOC”, interpretar como o padrão/skill/processo **LK Growth Optimized Collection**.
- O termo se refere ao pacote completo de otimização de coleção: texto hero robusto, layout editorial, imagens editoriais, guia pós-grid, Guia LK, FAQ único canônico, CTA claro, schema, QA, ledger/tag/metafields quando aplicável e link obrigatório de preview após qualquer alteração.
- Regra de comunicação: responder usando o contexto LKGOC sem pedir esclarecimento quando Lucas usar essa sigla.

## Correção emergencial CSS renderizado — 20260601T234314Z
- Tema DEV: `155065450718`
- Problema: bloco CSS LKGOC Samba Jane estava fora de `<style>` e renderizando como texto no topo da página.
- Correção: bloco CSS envelopado em `<style>` antes do render.
- Link preview obrigatório: https://lksneakers.com.br/collections/adidas-samba-jane?preview_theme_id=155065450718&qa=20260601T234314Z
- Backup/readback: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/shopify-theme-backups/samba-jane-dev-emergency-css-wrap-20260601T234314Z`
- Marcadores: `{"pilot_css_wrapped": true, "new_desc": true, "legacy_faq_removed": true, "cta_light_css": true, "guide_h2": true}`
- Termos proibidos: `{"pronta entrega": 0, "encomenda": 0, "estoque": 0}`

## Correção emergencial — remover comentários CSS visíveis — 20260601T234415Z
- Tema DEV: `155065450718`
- Correção: removidos comentários CSS LKGOC/QA que apareciam no render textual; CSS mantido dentro de `<style>`.
- Link preview obrigatório: https://lksneakers.com.br/collections/adidas-samba-jane?preview_theme_id=155065450718&qa=20260601T234415Z
- Backup/readback: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/shopify-theme-backups/samba-jane-dev-remove-visible-css-comments-20260601T234415Z`
- Marcadores: `{"no_css_comments": true, "raw_media_wrapped": true, "new_desc": true, "legacy_faq_removed": true, "cta_light_css": true}`
- Termos proibidos: `{"pronta entrega": 0, "encomenda": 0, "estoque": 0}`

## Correção LKGOC CTA — 20260601T234823Z
- Tema DEV: `155065450718`
- Correções: bloco “Para aprofundar...” com fundo claro igual ao card editorial acima; link/botão “ABRIR GUIA COMPLETO” com texto branco.
- Link preview obrigatório: https://lksneakers.com.br/collections/adidas-samba-jane?preview_theme_id=155065450718&qa=20260601T234823Z
- Backup/readback: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/shopify-theme-backups/samba-jane-dev-lkgoc-cta-color-20260601T234823Z`
- Marcadores: `{"lkgoc_cta_fix": true, "media_bg_light": true, "cta_button_white": true, "no_css_comments_visible_markers": true, "new_desc": true, "legacy_faq_removed": true}`
- Termos proibidos: `{"pronta entrega": 0, "encomenda": 0, "estoque": 0}`

## Correção LKGOC mobile CTA — 20260602T001146Z
- Tema DEV: `155065450718`
- Correção: override específico mobile para o bloco “Para aprofundar...” usar o mesmo fundo claro do card acima; botão “ABRIR GUIA COMPLETO” com texto branco no mobile.
- Link preview obrigatório: https://lksneakers.com.br/collections/adidas-samba-jane?preview_theme_id=155065450718&qa=20260602T001146Z
- Backup/readback: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/shopify-theme-backups/samba-jane-dev-lkgoc-mobile-cta-bg-20260602T001146Z`
- Marcadores: `{"mobile_media_override": true, "mobile_bg_light": true, "button_white": true, "new_desc": true, "legacy_faq_removed": true, "no_css_visible_comments": true}`
- Termos proibidos: `{"pronta entrega": 0, "encomenda": 0, "estoque": 0}`

## Correção LKGOC Guia LK novo — 20260602T001617Z
- Tema DEV: `155065450718`
- Correções: Guia LK Samba Jane atualizado para padrão novo com divisor desktop; divisor superior mobile; card “Para aprofundar...” em fundo branco igual aos cards internos; botão “ABRIR GUIA COMPLETO” com texto branco.
- Link preview obrigatório: https://lksneakers.com.br/collections/adidas-samba-jane?preview_theme_id=155065450718&qa=20260602T001617Z
- Backup/readback: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/shopify-theme-backups/samba-jane-dev-lkgoc-new-guide-divider-20260602T001617Z`
- Marcadores: `{"desktop_divider": true, "canonical_grid": true, "media_bg_white": true, "cta_white_text": true, "new_desc": true, "legacy_faq_removed": true}`
- Termos proibidos: `{"pronta entrega": 0, "encomenda": 0, "estoque": 0}`
