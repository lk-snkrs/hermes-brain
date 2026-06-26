# LK Variante Samba Jane — Dev Crop Fix Receipt

Data UTC: 2026-06-02T11:08:38.657057+00:00

## Correção
Ajuste visual no dev para evitar corte do quinto produto (`Green White Gum`) no mobile.

## Asset alterado
- `assets/lk-variante.css`

## CSS aplicado
- rail virou grid de 5 colunas: `repeat(5,minmax(0,1fr))`
- itens passaram a ocupar a coluna inteira, sem largura fixa
- thumbnail mobile limitado a `58px` para caber dentro dos 90%
- overflow do rail: `visible`

## Readback
- readback_match: `True`
- sha: `f207cbbcf6760437`
- size: `2554`

## QA HTML preview
- URL: `https://lksneakers.com.br/products/tenis-adidas-samba-jane-white-black-branco?lkv_crop_fix=1`
- bloco encontrado: `True`
- itens no bloco: `5`
- labels: `Cream Black Gum, White Blue Gum, Black White Gum, Scarlet Gum, Green White Gum`
- Liquid errors: `0`
- CSS grid 5 colunas presente: `True`
- CSS mobile 58px presente: `True`
- CSS overflow visible presente: `True`

## Rollback
Backup pré-upload: `before__assets__lk-variante.css` neste diretório.
