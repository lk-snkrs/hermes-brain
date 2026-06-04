# Batch 19 — approval packet para preview Dev (read-only)

- timestamp UTC: `2026-06-03T16:29:59.856239+00:00`
- source SHA live base: `6d127babb763`
- operação até aqui: read-only; sem Shopify write; sem upload de tema
- decisão necessária: aprovar ou não o preview Dev/unpublished

## Recomendação
Preparar **Batch 19** com três expansões seguras de grupos existentes/semânticos:

### Nike SB Dunk Low
- marker proposto: `top30-nike-sb-dunk-low`
- marker já existe no source: `False`
- adicionar no preview: `8`

- `tenis-nike-sb-dunk-low-pro-triple-white-branco` — Pro Triple White
- `tenis-nike-sb-dunk-low-trocadero-gardens-marrom` — Trocadéro Gardens
- `nike-sb-dunk-low-pro-iso-dark-russet` — Pro ISO Dark Russet
- `nike-sb-dunk-low-pro-classic-green` — Pro Classic Green
- `nike-sb-dunk-low-prm-paisley-brown` — PRM Paisley Brown
- `nike-sb-dunk-low-prm-phillies` — PRM Phillies
- `nike-sb-dunk-low-club-58-gulf` — Club 58 Gulf
- `nike-sb-dunk-low-vx-1000-camcorder` — VX 1000 Camcorder

### Onitsuka Mexico 66 SD
- marker proposto: `top30-mexico66-sd`
- marker já existe no source: `True`
- adicionar no preview: `8`

- `tenis-onitsuka-tiger-mexico-66-sd-exposed-black-black-preto` — Exposed Black/Black
- `tenis-onitsuka-tiger-mexico-66-sd-clay-canyon-marrom` — Exposed Clay Canyon
- `tenis-onitsuka-tiger-mexico-66-sd-exposed-foam-jade-verde` — Exposed Foam Jade
- `tenis-onitsuka-tiger-mexico-66-sd-exposed-foam-peacoat-azul` — Exposed Foam Peacoat
- `tenis-onitsuka-tiger-mexico-66-sd-white-rose-gold-branco` — White/Rose Gold
- `tenis-onitsuka-tiger-mexico-66-sd-vin-mantle-green-ivory-verde` — Vin Mantle Green Ivory
- `tenis-onitsuka-tiger-mexico-66-sd-metallic-series-pale-mint-cream-azul-1` — Metallic Series Pale Mint Crea
- `onitsuka-tiger-mexico-66-sd-metallic-series-jade-cream-verde` — Metallic Series Jade Cream

### New Balance 530
- marker proposto: `top30-nb-530`
- marker já existe no source: `True`
- adicionar no preview: `5`

- `tenis-new-balance-530-white-green-matcha-verde` — White Green Matcha
- `tenis-new-balance-530-white-chrome-blue-branco` — White Chrome Blue
- `tenis-new-balance-530-sea-salt-white-marsh-green-branco` — Sea Salt White Marsh Green
- `tenis-new-balance-530-white-light-crome-blue-branco` — White Light Crome Blue
- `tenis-new-balance-530-stoneware-line-branco` — Stoneware Line

## QA read-only
- produtos/imagens checados: `21`
- OK: `21`
- problemas: `0`

## Risco / bloqueios evitados
- Não usei Onitsuka Mexico 66 regular porque o scan misturava adulto e kids; isso precisa split separado.
- Nike SB Dunk Low é separado de Nike Dunk Low regular para não misturar SB com regular.
- Preview ainda é write em tema unpublished e exige aprovação explícita.

## Texto de aprovação
Para eu aplicar só no preview/unpublished:

`Aprovo preview Batch 19: SB Dunk Low + Mexico 66 SD + NB 530`
