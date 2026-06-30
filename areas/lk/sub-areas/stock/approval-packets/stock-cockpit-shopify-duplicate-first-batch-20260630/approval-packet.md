# Stock Cockpit — Shopify duplicate first batch approval — 2026-06-30

- generated_at_utc: `2026-06-30T15:03:20.629200+00:00`
- values_printed: false
- external_writes: 0
- live_write_allowed: false

## Proposta de decisão

- `tenis-onitsuka-tiger-mexico-66-sd-kill-bill-amarelo` size `40` variant `45968992993502`: `183A872` → `183A872` · action `keep_current` · write `false`
  - rationale: sequência parcial 34–39 = 183A872-1..6, 40 mantém base, 43 = 183A872-9
- `tenis-onitsuka-tiger-mexico-66-sd-kill-bill-amarelo` size `41` variant `45968993911006`: `183A872` → `183A872-7` · action `set_target_sku` · write `true`
  - rationale: sequência parcial 34–39 = 183A872-1..6, 40 mantém base, 43 = 183A872-9
- `tenis-onitsuka-tiger-mexico-66-sd-kill-bill-amarelo` size `42` variant `45968993943774`: `183A872` → `183A872-8` · action `set_target_sku` · write `true`
  - rationale: sequência parcial 34–39 = 183A872-1..6, 40 mantém base, 43 = 183A872-9
- `tenis-air-jordan-1-low-se-legend-coffee-marrom` size `42` variant `47604797472990`: `FJ3453-200` → `FJ3453-200-8` · action `set_target_sku` · write `true`
  - rationale: sequência parcial 34–40 = FJ3453-200-1..7; proposta mínima: 41 mantém base, 42 vira -8
- `tenis-air-jordan-1-low-se-legend-coffee-marrom` size `41` variant `47604798357726`: `FJ3453-200` → `FJ3453-200` · action `keep_current` · write `false`
  - rationale: sequência parcial 34–40 = FJ3453-200-1..7; proposta mínima: 41 mantém base, 42 vira -8

## Aprovação necessária

Para destravar este primeiro lote, Lucas/Júlio precisa responder aprovando exatamente estes targets ou corrigindo algum target:

`Aprovo lote Shopify duplicate first batch: aplicar apenas rows write=true do packet first_batch_proposed_targets.json; sem alterar preço, estoque, título, imagem, coleção, Tiny ou Supabase; com rollback/readback por variant_id.`
