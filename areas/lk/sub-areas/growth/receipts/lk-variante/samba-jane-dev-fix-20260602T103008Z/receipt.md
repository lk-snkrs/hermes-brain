# LK Variante Samba Jane — Dev Fix Receipt

Data UTC: 2026-06-02T10:30:20.387496+00:00

## Escopo
Correções solicitadas por Lucas no preview dev:

1. Remover escrito de best seller/mais vendido.
2. Não mostrar o produto atual dentro da lista.
3. Mostrar apenas 5 produtos.
4. Bloco/lista com 90% da largura do container.

## Tema alvo
- Theme ID: `155065450718`
- Escopo: dev/unpublished preview only

## Assets alterados
- `snippets/lk-variante-samba-jane.liquid`
- `assets/lk-variante.css`

## Readback Asset API
- `snippets/lk-variante-samba-jane.liquid`: readback_match `True`, sha `d32054abeca76d3b`, size `2574`
- `assets/lk-variante.css`: readback_match `True`, sha `cc35d0f814b5070b`, size `2363`

## QA preview

### white_black
- status: `200`
- marker: `1`
- items: `5`
- badge/best seller/mais vendido count: `4`
- title 'Outras variações': `1`
- labels: `Cream Black Gum, White Blue Gum, Black White Gum, Scarlet Gum, Green White Gum`
- liquid errors: `0`

### cream_black
- status: `200`
- marker: `1`
- items: `5`
- badge/best seller/mais vendido count: `4`
- title 'Outras variações': `1`
- labels: `White Black, White Blue Gum, Black White Gum, Scarlet Gum, Green White Gum`
- liquid errors: `0`

### production_control
- status: `200`
- marker: `0`
- items: `0`
- badge/best seller/mais vendido count: `4`
- title 'Outras variações': `0`
- labels: ``
- liquid errors: `0`

## QA adicional escopado ao bloco LK Variante

URL testada:
`https://www.lksneakers.com.br/products/tenis-adidas-samba-jane-white-black-branco?preview_theme_id=155065450718&lkv_fix_scope=1`

Resultado dentro do `<section class="lk-variante">`:

- bloco encontrado: `true`
- itens no bloco: `5`
- texto `best seller` / `mais vendido` no bloco: `false`
- link do produto atual `white-black` dentro da lista: `false`
- labels renderizadas: `Cream Black Gum`, `White Blue Gum`, `Black White Gum`, `Scarlet Gum`, `Green White Gum`
- Liquid errors: `0`

## Rollback
Backups pré-upload estão neste diretório como `before__...`. Reupar os assets anteriores para reverter o preview dev.
