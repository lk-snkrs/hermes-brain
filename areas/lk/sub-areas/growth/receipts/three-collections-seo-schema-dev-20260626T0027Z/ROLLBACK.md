# Rollback — Adidas Taekwondo + Adidas Tokyo + Puma Speedcat

Data: 20260626T003626Z

## Taekwondo SEO rollback

Restaurar SEO fields de `/collections/adidas-taekwondo` a partir de:
`areas/lk/sub-areas/growth/work/three-collection-dev-20260626/adidas-taekwondo-admin-before.json`

Antes:
- SEO title: `Adidas Taekwondo - LK`
- Meta: `Compre Adidas Taekwondo na LK Sneakers. 100% originais · Parcele em 10x · Frete grátis · Loja Jardins SP.`

## Taekwondo DEV rollback

Restaurar asset DEV `snippets/lk-goc-guide-contract.liquid` no tema `155065450718` a partir de:
`areas/lk/sub-areas/growth/work/three-collection-dev-20260626/dev-snippet-before.liquid`

## Tokyo/Speedcat schema rollback

Opção A — remover render do section:
Restaurar `sections/lk-collection.liquid` production a partir de:
`areas/lk/sub-areas/growth/work/three-collection-dev-20260626/prod-section-before-schema-extra-render.liquid`

Opção B — manter render mas esvaziar/remover snippet:
Remover ou esvaziar `snippets/lk-goc-schema-extra.liquid` no tema production `155065417950`.

Validar depois:
- `/collections/adidas-tokyo` sem FAQPage extra;
- `/collections/puma-speedcat` sem FAQPage extra;
- ASICS/Lululemon/Samba continuam com FAQPage preservado;
- sem Liquid error.

Não tocar preço, estoque, produtos, GMC, campanhas, Klaviyo ou checkout.
