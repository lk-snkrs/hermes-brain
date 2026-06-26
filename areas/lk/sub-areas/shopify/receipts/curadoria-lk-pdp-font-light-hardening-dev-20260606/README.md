# Receipt — Curadoria LK PDP font-light hardening DEV — 2026-06-06

## Status
DEV aplicado e validado. Nenhum write em Production.

## Escopo aprovado
- Tema DEV: `155065450718`
- Asset: `assets/lk-variante.css`
- Alteração: hardening de tipografia do bloco `Outras variações` para `font-weight: 300`.

## Mudança aplicada
- Base `.lk-variante__title`: `500 → 300`
- Base `.lk-variante__item.is-current .lk-variante__label`: `500 → 300`
- Override final mantido/canonizado:

```css
.lk-variante__title,
.lk-variante__label,
.lk-variante__item.is-current .lk-variante__label,
.lk-variante .lk-variante__item[href^="/products/"] .lk-variante__label:after {
  font-weight: 300 !important;
}
```

## Readback DEV
- CDN DEV validado: `https://lksneakers.com.br/cdn/shop/t/92/assets/lk-variante.css?v=146918974967942648421780762757`
- Regra base do título no CSS DEV: `font-weight:300`
- Regra base do label atual no CSS DEV: `font-weight:300`
- Override final no CSS DEV: presente

## QA visual DEV via CDP
Amostras com `preview_theme_id=155065450718`:

### New Balance 530
- PDP: `new-balance-530-white-natural-indigo-1`
- Marker: `top30-nb-530`
- Título: `Outras variações`
- `titleWeight`: `300`
- `labelWeights`: `300, 300, 300, 300, 300`
- Labels: `Turtledove`, `Silver Cream`, `Silver White`, `Steel Grey`, `Silver Blue`

### Adidas Superstar special
- PDP: `tenis-adidas-superstar-x-clot-chinese-new-year-preto`
- Marker: `top30-adidas-superstar-special`
- Título: `Outras variações`
- `titleWeight`: `300`
- `labelWeights`: `300, 300`
- Labels: `Korn 30th`, `Wales Bonner`

## Backup
Backup pré-write DEV:

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/receipts/curadoria-lk-pdp-font-light-hardening-dev-20260606/20260606T161916Z-dev-theme-155065450718-assets__lk-variante.before.css`

## Observação operacional
O primeiro receipt JSON automático registrou `status: updated_dev`, mas o readback imediato ainda mostrou SHA anterior. Revalidação com API `2024-10` confirmou a convergência correta:
- `readback_title500`: `0`
- `readback_title300`: `1`
- hardening canonical: `1`

## Risco
Baixo: CSS localizado no bloco da Curadoria LK PDP. O destaque do item atual permanece por borda/cor, não por peso de fonte.

## Rollback
Restaurar o backup DEV acima no asset `assets/lk-variante.css` do tema `155065450718`.

## Próxima decisão
Se o visual em DEV estiver aprovado: criar PR/merge para Production via GitHub, sem write direto no tema live.
