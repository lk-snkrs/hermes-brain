# LK Variante Samba Jane — Dev Preview Receipt

Data UTC: 2026-06-02T00:50:13Z

## Escopo aprovado

Lucas aprovou:

> Aprovado criar preview LK Variante Samba Jane no tema dev 155065450718, sem production, sem remover Variant King e sem alterar tags/produtos.

## Tema alvo

- Theme ID: `155065450718`
- Nome: `lk-new-theme/dev`
- Role: `unpublished`

## O que foi alterado

Uploads feitos apenas no tema dev:

- `sections/lk-pdp.liquid`
- `snippets/lk-variante-samba-jane.liquid`
- `assets/lk-variante.css`

## O que o preview faz

- Renderiza um bloco `LK Variante` apenas em PDPs do grupo piloto Samba Jane.
- Mostra miniaturas de variações lógicas/irmãs.
- Ordena por ranking best-seller inicial:
  1. White Black
  2. Cream Black Gum
  3. White Blue Gum
  4. Black White Gum
  5. Scarlet Gum
  6. Green White Gum
- Produto atual fica marcado como selecionado.
- Não usa tags/metafields ainda; é MVP hardcoded para preview visual.

## Readback Asset API

- `sections/lk-pdp.liquid`: readback match `true`, SHA `c98224f4fbd5f3ef`
- `snippets/lk-variante-samba-jane.liquid`: readback match `true`, SHA `d54c781092ad454b`
- `assets/lk-variante.css`: readback match `true`, SHA `4d3c0dbe053464fd`

## QA público/preview

Preview testado:

`https://www.lksneakers.com.br/products/tenis-adidas-samba-jane-white-black-branco?preview_theme_id=155065450718&lkv=1`

Resultado:

- Status: `200`
- Marker `data-lk-variante="samba-jane"`: `1`
- `lk-variante.css`: `1`
- Itens `lk-variante__item`: `6`
- Liquid errors: `0`

Ordem renderizada no preview:

1. White Black
2. Cream Black Gum
3. White Blue Gum
4. Black White Gum
5. Scarlet Gum
6. Green White Gum

Controle não-piloto testado:

`/products/tenis-autry-medalist-low-ll15-branco?preview_theme_id=155065450718&lkv=1`

Resultado:

- Marker LK Variante: `0`
- CSS LK Variante: `0`
- Itens: `0`
- Liquid errors: `0`

Controle production live sem preview:

`/products/tenis-adidas-samba-jane-white-black-branco?lkv_live_check=1`

Resultado:

- Marker LK Variante: `0`
- CSS LK Variante: `0`
- Itens: `0`
- Liquid errors: `0`

## Rollback

Backups pré-upload salvos neste diretório:

- `before__sections__lk-pdp.liquid`
- `before__snippets__lk-variante-samba-jane.liquid.missing`
- `before__assets__lk-variante.css.missing`

Rollback dev:

1. Re-upar `before__sections__lk-pdp.liquid` para `sections/lk-pdp.liquid` no theme dev.
2. Remover `snippets/lk-variante-samba-jane.liquid` se o preview for abandonado.
3. Remover `assets/lk-variante.css` se o preview for abandonado.
4. Verificar preview Samba Jane e não-piloto novamente.

## Não realizado

- Nenhum upload para production.
- Nenhuma publicação de tema.
- Nenhuma remoção/desativação de Variant King/StarApps.
- Nenhuma alteração em tags, produtos, metafields, preço, estoque, checkout, GMC, Klaviyo, Meta, WhatsApp ou e-mail.
