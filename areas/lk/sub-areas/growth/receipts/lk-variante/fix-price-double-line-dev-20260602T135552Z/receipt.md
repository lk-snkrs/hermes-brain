# Fix linha dupla após preço — Curadoria LK dev

Data UTC: `2026-06-02T13:55:58.898811+00:00`

## Mudança
- Removido `border-top` do bloco `.lk-variante` no CSS do tema dev.
- Mantida apenas a linha inferior/separadora do bloco.
- Ajustado respiro superior para não criar duas linhas depois do preço.

## QA
- Readback CSS match: `True`
- CSS tem `border-top:0`: `True`
- Preview status: `200`
- Blocos LK Variante na Jaqueta Lululemon: `1`
- Itens: `5`
- Liquid errors: `0`
- Preview: https://www.lksneakers.com.br/products/jaqueta-lululemon-define-nulu?preview_theme_id=155065450718&lkv_linefix=1

## Rollback
- Backup: `before__lk-variante.css`

## Não feito
- Não toquei production.
- Não toquei produto/preço/estoque/campanhas/apps.
