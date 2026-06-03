# LK Variante Samba Jane — Dev Width Align Fix Receipt

Data UTC: 2026-06-02T11:14:28.748209+00:00

## Correção
Lucas corrigiu que o bloco deve ter a mesma largura do grid dos botões de tamanho, não 90%.

## Asset alterado
- `assets/lk-variante.css`

## CSS aplicado
- `.lk-variante`: `width:100%; max-width:none; margin-left/right:0`
- `.lk-variante__rail`: `width:100%`, grid de 5 colunas
- mobile também em `width:100%`

## Readback
- readback_match: `True`
- sha: `db46de01539ba4d8`
- size: `2573`

## QA HTML preview
- URL: `https://lksneakers.com.br/products/tenis-adidas-samba-jane-white-black-branco?lkv_width_align=1`
- bloco encontrado: `True`
- itens no bloco: `5`
- labels: `Cream Black Gum, White Blue Gum, Black White Gum, Scarlet Gum, Green White Gum`
- Liquid errors: `0`
- CSS bloco full-width: `True`
- CSS rail full-width: `True`
- CSS mobile full-width: `True`

## Rollback
Backup pré-upload: `before__assets__lk-variante.css` neste diretório.
