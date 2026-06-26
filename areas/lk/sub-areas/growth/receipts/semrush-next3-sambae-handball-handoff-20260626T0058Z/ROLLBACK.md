# Rollback — Sambae + Handball + Handoff

Data: 20260626T010009Z

## Sambae

Restaurar collection `/collections/adidas-sambae` a partir de:
- `areas/lk/sub-areas/growth/work/semrush-next3-sambae-handball-handoff-20260626/adidas-sambae-admin-before.json`
- `areas/lk/sub-areas/growth/work/semrush-next3-sambae-handball-handoff-20260626/adidas-sambae-description-before.html`

Campos anteriores:
- SEO title: `Adidas Sambae - LK Sneakers`
- Meta: `Adidas Sambae: Samba com plataforma elevada. Feminino e estiloso · 100% original · 10x sem juros · Loja Jardins SP.`

Snippet:
- Para voltar ao estado anterior exato, remover `snippets/lk-sambae-204l-guide.liquid` do tema production `155065417950`.
- Atenção: isso reintroduz o Liquid error enquanto `sections/lk-collection.liquid` renderizar esse snippet para Sambae. Rollback recomendado se necessário: restaurar junto o `sections/lk-collection.liquid` anterior ao render ou manter snippet vazio seguro.

## Handball

Restaurar `snippets/lk-goc-schema-extra.liquid` production a partir de:
`areas/lk/sub-areas/growth/work/semrush-next3-sambae-handball-handoff-20260626/prod__snippets__lk-goc-schema-extra-before-handball.liquid`

Validar depois:
- `/collections/adidas-handball-spezial` HTTP 200;
- sem Liquid error;
- schema Handball removido se rollback total.

## Handoff

Card Kanban `t_5db8be73` pode ser bloqueado/arquivado se Lucas cancelar a criação das collections NB740/Gel NYC.

Não tocar preço, estoque, produtos, GMC, campanhas, Klaviyo ou checkout.
