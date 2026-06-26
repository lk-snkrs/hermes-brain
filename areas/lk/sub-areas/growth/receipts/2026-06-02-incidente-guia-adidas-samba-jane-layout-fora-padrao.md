# Incidente — Guia Adidas Samba Jane fora do padrão LK

Data: 2026-06-02T10:31:28Z
Origem: feedback direto Lucas via Telegram.

## Problema confirmado

A página pública `https://lksneakers.com.br/pages/guia-adidas-samba-jane` foi publicada como corpo textual simples (`article.lk-guide-page`) e **não seguiu o padrão visual/editorial canônico de Guia LK**.

Falha: foi validado conteúdo/SEO/readback textual, mas não foi validado shell visual premium contra o padrão Moon Shoe nem preview/screenshot antes de production.

## Padrão correto que deveria ter sido usado

- Guia editorial/source page independente: padrão visual/editorial **Nike x Jacquemus Moon Shoe**.
- Coleção produto-first: padrão **New Balance 204L**.
- Fontes canônicas:
  - `PADRAO-GUIAS-EDITORIAIS-LK.md`
  - `PADRAO-CANONICO-GUIA-E-COLECAO-LK.md`
  - `rules/REGRA-PRODUCTION-GUIAS-COLECOES-LK.md`
  - snapshot Moon Shoe: `references/moon-shoe-jacquemus-canonical-guide-pattern.html`

## Ação necessária

1. Conter a página errada: rollback/deletar page ID `127553700062` se Lucas aprovar write Shopify production.
2. Refazer primeiro em DEV/preview usando shell Moon Shoe completo, não texto corrido.
3. Incluir hero editorial, imagem contextual, tipografia/spacing editorial, tabela comparativa, fontes externas com cards/links, blocos citáveis, FAQ e CTA discreto.
4. Enviar preview/screenshot para aprovação explícita antes de qualquer nova publicação production.

## Guardrail reforçado

Para guia dedicado `/pages/guia-*`, checklist obrigatório passa/falha:

- Se o HTML começa como `<article class="lk-guide-page...">` sem shell editorial Moon Shoe, **bloquear publicação**.
- Se não há validação visual desktop/mobile contra Moon Shoe, **bloquear publicação**.
- Se não há aprovação explícita atual de Lucas para production, **bloquear write Shopify**.
