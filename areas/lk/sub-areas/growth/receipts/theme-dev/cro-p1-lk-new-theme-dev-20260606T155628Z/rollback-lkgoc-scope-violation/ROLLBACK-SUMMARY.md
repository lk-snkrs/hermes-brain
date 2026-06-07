# Rollback — CRO P1 removido do DEV por escopo LKGOC

## Status
- Status: `rolled_back`
- Produção alterada: `false`

## Tema
- `lk-new-theme/dev` / `155065450718` / `unpublished`

## O que foi revertido
- `layout/theme.liquid` restaurado ao snapshot anterior.
- `snippets/lk-cro-p1-growth-preview.liquid` removido.

## Verificação Shopify readback
- Layout restaurado: `True`
- Marker ausente: `True`
- Snippet ausente: `True`

## QA Playwright DEV
- https://lksneakers.com.br/products/slide-nike-mind-001-black-chrome-preto: status=200, block_count=0, liquid_error=False
- https://lksneakers.com.br/collections/new-balance-204l: status=200, block_count=0, liquid_error=False

## Aprendizado / regra
- LK Growth não deve alterar superfície visual de PDP/collection/Guia quando isso entrar no domínio LKGOC.
- Growth pode diagnosticar GSC/CRO e preparar brief/approval packet, mas implementação visual deve ser roteada ao LKGOC/Collection Optimizer ou LK Shopify conforme escopo.
- Antes de qualquer write de theme, consultar `LKGOC-THEME-TARGET-CONTEXT.md` e confirmar ownership do domínio.
