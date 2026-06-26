# Approval Packet — GMC Residual Manual Enrichment Batch 8 — 2026-06-08

Status: review packet / sem write

## Summary
- manual_review_count: `148`

## Escopo

Itens API-input residuais onde ainda há `missing_item_attribute_for_product_type`, mas a inferência automática de `color`/atributos não é segura.

## Decisão recomendada

Não executar patch automático agora. O próximo passo correto é preencher uma planilha/JSON de revisão manual com `proposed_color` e, quando aplicável, `size`, `ageGroup`, `gender`. Depois disso gero um batch write só para linhas revisadas.

## Risco

- Alto se automatizar: muitos nomes têm cores compostas/termos em inglês/modelos que podem parecer cor.
- Médio se revisar manualmente: exige consistência, mas é controlado por snapshot/readback.

## Como aprovar a próxima etapa

Aprovar criação de planilha de revisão enriquecível ou enviar os valores revisados. Write no GMC só depois de aprovação do arquivo preenchido.

## Amostra dos primeiros 50

- `DA6672-700-38` — Tenis Nike Craft General Purpose Shoe Tom Sachs Archive Dark Sulfur
  - handle: tenis-nike-craft-general-purpose-shoe-tom-sachs-archive-dark-sulfur
  - issue_attrs: ['color', 'color', 'color', 'color', 'color']
  - current_color: None

- `OXV-2733022-36` — Tênis Onitsuka Tiger x Versace TAI-CHI Sakura Suede Têniss Green
  - handle: tenis-onitsuka-tiger-x-versace-tai-chi-sakura-suede-sneakers-green
  - issue_attrs: ['color', 'color', 'color', 'color', 'color']
  - current_color: None

- `OXV-2733022-35` — Tênis Onitsuka Tiger x Versace TAI-CHI Sakura Suede Têniss Green
  - handle: tenis-onitsuka-tiger-x-versace-tai-chi-sakura-suede-sneakers-green
  - issue_attrs: ['color', 'color', 'color', 'color', 'color']
  - current_color: None

- `JS0297-3` — Tênis Adidas Taekwondo Mei Cow Print (Women's) Animal Print
  - handle: tenis-adidas-taekwondo-mei-cow-print-womens-animal-print
  - issue_attrs: ['color', 'color', 'color', 'color', 'color']
  - current_color: None

- `DA6672-700-39` — Tenis Nike Craft General Purpose Shoe Tom Sachs Archive Dark Sulfur
  - handle: tenis-nike-craft-general-purpose-shoe-tom-sachs-archive-dark-sulfur
  - issue_attrs: ['color', 'color', 'color', 'color', 'color']
  - current_color: None

- `JH7370-4` — Tênis Adidas Gazelle Indoor Liberty London Floral Embroidery Stripes Multi-Color
  - handle: tenis-adidas-gazelle-indoor-liberty-london-floral-embroidery-stripes-multi-color
  - issue_attrs: ['color', 'color', 'color', 'color', 'color']
  - current_color: None

- `JRD-5205470-40` — Tênis Nike Air Jordan 1 Retro High OG SP Union LA Chicago Shadow
  - handle: tenis-nike-air-jordan-1-retro-high-og-sp-union-la-chicago-shadow
  - issue_attrs: ['color', 'color', 'color', 'color', 'color']
  - current_color: None

- `IO7847-001-35` — Tênis Jordan 1 Retro High OG SP Fragment x Union LA Sport Royal
  - handle: tenis-jordan-1-retro-high-og-sp-fragment-x-union-la-sport-royal
  - issue_attrs: ['color', 'color', 'color', 'color', 'color']
  - current_color: None

- `HQ7978-103-44` — Tênis Jordan 5 Retro White Metallic (2026) Metalizado
  - handle: tenis-jordan-5-retro-white-metallic-2026-metalizado
  - issue_attrs: ['color', 'color', 'color', 'color', 'color']
  - current_color: None

- `JS0297-5` — Tênis Adidas Taekwondo Mei Cow Print (Women's) Animal Print
  - handle: tenis-adidas-taekwondo-mei-cow-print-womens-animal-print
  - issue_attrs: ['color', 'color', 'color', 'color', 'color']
  - current_color: None

- `HQ7978-103-37` — Tênis Jordan 5 Retro White Metallic (2026) Metalizado
  - handle: tenis-jordan-5-retro-white-metallic-2026-metalizado
  - issue_attrs: ['color', 'color', 'color', 'color', 'color']
  - current_color: None

- `IO7847-001-43` — Tênis Jordan 1 Retro High OG SP Fragment x Union LA Sport Royal
  - handle: tenis-jordan-1-retro-high-og-sp-fragment-x-union-la-sport-royal
  - issue_attrs: ['color', 'color', 'color', 'color', 'color']
  - current_color: None

- `JS0297-7` — Tênis Adidas Taekwondo Mei Cow Print (Women's) Animal Print
  - handle: tenis-adidas-taekwondo-mei-cow-print-womens-animal-print
  - issue_attrs: ['color', 'color', 'color', 'color', 'color']
  - current_color: None

- `DA6672-200-35` — Tenis Nike Craft General Purpose Shoe Tom Sachs
  - handle: tenis-nike-craft-general-purpose-shoe-tom-sachs
  - issue_attrs: ['color', 'color', 'color', 'color', 'color']
  - current_color: None

- `IR1888-700-44` — Tenis Nike SB Dunk Low Pro Muni Lightning Denim Turquoise Turquesa
  - handle: tenis-nike-sb-dunk-low-pro-muni-lightning-denim-turquoise-turquesa
  - issue_attrs: ['color', 'color', 'color', 'color', 'color']
  - current_color: None

- `fz8117-204` — Tênis Nike Travis Scott x Jordan Jumpman Jack TR Dark Mocha Nobuck Lona
  - handle: tenis-travis-scott-x-jordan-jumpman-jack-tr-dark-mocha-nobuck-lona
  - issue_attrs: ['color', 'color', 'color', 'color', 'color']
  - current_color: None

- `OXV-2733022-355` — Tênis Onitsuka Tiger x Versace TAI-CHI Sakura Suede Têniss Green
  - handle: tenis-onitsuka-tiger-x-versace-tai-chi-sakura-suede-sneakers-green
  - issue_attrs: ['color', 'color', 'color', 'color', 'color']
  - current_color: None

- `JP5309-3` — Tênis Adidas Gazelle Indoor Liberty London Floral Embroidery Multi-Color
  - handle: tenis-adidas-gazelle-indoor-liberty-london-floral-embroidery-multi-color
  - issue_attrs: ['color', 'color', 'color', 'color', 'color']
  - current_color: None

- `HV6417-001-6` — Tênis Nike Zoom Vomero 5 Metallic Silver Platinum Violet Prateado/Violeta
  - handle: tenis-nike-zoom-vomero-5-metallic-silver-platinum-violet-prateado-violeta
  - issue_attrs: ['color', 'color', 'color', 'color', 'color']
  - current_color: None

- `OXV-2733022-40` — Tênis Onitsuka Tiger x Versace TAI-CHI Sakura Suede Têniss Green
  - handle: tenis-onitsuka-tiger-x-versace-tai-chi-sakura-suede-sneakers-green
  - issue_attrs: ['color', 'color', 'color', 'color', 'color']
  - current_color: None

- `HV6417-001-2` — Tênis Nike Zoom Vomero 5 Metallic Silver Platinum Violet Prateado/Violeta
  - handle: tenis-nike-zoom-vomero-5-metallic-silver-platinum-violet-prateado-violeta
  - issue_attrs: ['color', 'color', 'color', 'color', 'color']
  - current_color: None

- `IO7847-001-38` — Tênis Jordan 1 Retro High OG SP Fragment x Union LA Sport Royal
  - handle: tenis-jordan-1-retro-high-og-sp-fragment-x-union-la-sport-royal
  - issue_attrs: ['color', 'color', 'color', 'color', 'color']
  - current_color: None

- `JRD-5205470-38` — Tênis Nike Air Jordan 1 Retro High OG SP Union LA Chicago Shadow
  - handle: tenis-nike-air-jordan-1-retro-high-og-sp-union-la-chicago-shadow
  - issue_attrs: ['color', 'color', 'color', 'color', 'color']
  - current_color: None

- `IO7847-001-34` — Tênis Jordan 1 Retro High OG SP Fragment x Union LA Sport Royal
  - handle: tenis-jordan-1-retro-high-og-sp-fragment-x-union-la-sport-royal
  - issue_attrs: ['color', 'color', 'color', 'color', 'color']
  - current_color: None

- `DA6672-200-39` — Tenis Nike Craft General Purpose Shoe Tom Sachs
  - handle: tenis-nike-craft-general-purpose-shoe-tom-sachs
  - issue_attrs: ['color', 'color', 'color', 'color', 'color']
  - current_color: None

- `HF8022300-11` — Yuto Horigome x Dunk Low SB Matcha
  - handle: yuto-horigome-x-dunk-low-sb-matcha
  - issue_attrs: ['color', 'color', 'color', 'color', 'color']
  - current_color: None

- `NB-0058078-44` — Tênis New Balance 990v6 Made in USA 'Triple Black'
  - handle: 990v6-made-in-usa-triple-black
  - issue_attrs: ['color', 'color', 'color', 'color', 'color']
  - current_color: None

- `IO7847-001-37` — Tênis Jordan 1 Retro High OG SP Fragment x Union LA Sport Royal
  - handle: tenis-jordan-1-retro-high-og-sp-fragment-x-union-la-sport-royal
  - issue_attrs: ['color', 'color', 'color', 'color', 'color']
  - current_color: None

- `DA6672-200-40` — Tenis Nike Craft General Purpose Shoe Tom Sachs
  - handle: tenis-nike-craft-general-purpose-shoe-tom-sachs
  - issue_attrs: ['color', 'color', 'color', 'color', 'color']
  - current_color: None

- `NB-0058078-41` — Tênis New Balance 990v6 Made in USA 'Triple Black'
  - handle: 990v6-made-in-usa-triple-black
  - issue_attrs: ['color', 'color', 'color', 'color', 'color']
  - current_color: None

- `IR1888-700-37` — Tenis Nike SB Dunk Low Pro Muni Lightning Denim Turquoise Turquesa
  - handle: tenis-nike-sb-dunk-low-pro-muni-lightning-denim-turquoise-turquesa
  - issue_attrs: ['color', 'color', 'color', 'color', 'color']
  - current_color: None

- `OXV-2733022-395` — Tênis Onitsuka Tiger x Versace TAI-CHI Sakura Suede Têniss Green
  - handle: tenis-onitsuka-tiger-x-versace-tai-chi-sakura-suede-sneakers-green
  - issue_attrs: ['color', 'color', 'color', 'color', 'color']
  - current_color: None

- `JS0297-6` — Tênis Adidas Taekwondo Mei Cow Print (Women's) Animal Print
  - handle: tenis-adidas-taekwondo-mei-cow-print-womens-animal-print
  - issue_attrs: ['color', 'color', 'color', 'color', 'color']
  - current_color: None

- `LLM-2319326-XS` — Jaqueta Lululemon Define Cropped Nulu Light Ivory/Gold/Gold Off White
  - handle: define-cropped-jacket-nulu
  - issue_attrs: ['color', 'color', 'color', 'color', 'color']
  - current_color: None

- `JRD-5205470-35` — Tênis Nike Air Jordan 1 Retro High OG SP Union LA Chicago Shadow
  - handle: tenis-nike-air-jordan-1-retro-high-og-sp-union-la-chicago-shadow
  - issue_attrs: ['color', 'color', 'color', 'color', 'color']
  - current_color: None

- `OXV-2733022-37` — Tênis Onitsuka Tiger x Versace TAI-CHI Sakura Suede Têniss Green
  - handle: tenis-onitsuka-tiger-x-versace-tai-chi-sakura-suede-sneakers-green
  - issue_attrs: ['color', 'color', 'color', 'color', 'color']
  - current_color: None

- `NB-0058078-39` — Tênis New Balance 990v6 Made in USA 'Triple Black'
  - handle: 990v6-made-in-usa-triple-black
  - issue_attrs: ['color', 'color', 'color', 'color', 'color']
  - current_color: None

- `IR1888-700-43` — Tenis Nike SB Dunk Low Pro Muni Lightning Denim Turquoise Turquesa
  - handle: tenis-nike-sb-dunk-low-pro-muni-lightning-denim-turquoise-turquesa
  - issue_attrs: ['color', 'color', 'color', 'color', 'color']
  - current_color: None

- `HV6417-001-5` — Tênis Nike Zoom Vomero 5 Metallic Silver Platinum Violet Prateado/Violeta
  - handle: tenis-nike-zoom-vomero-5-metallic-silver-platinum-violet-prateado-violeta
  - issue_attrs: ['color', 'color', 'color', 'color', 'color']
  - current_color: None

- `LLM-2319326-S` — Jaqueta Lululemon Define Cropped Nulu Light Ivory/Gold/Gold Off White
  - handle: define-cropped-jacket-nulu
  - issue_attrs: ['color', 'color', 'color', 'color', 'color']
  - current_color: None

- `NB-0058078-34` — Tênis New Balance 990v6 Made in USA 'Triple Black'
  - handle: 990v6-made-in-usa-triple-black
  - issue_attrs: ['color', 'color', 'color', 'color', 'color']
  - current_color: None

- `JRD-5205470-34` — Tênis Nike Air Jordan 1 Retro High OG SP Union LA Chicago Shadow
  - handle: tenis-nike-air-jordan-1-retro-high-og-sp-union-la-chicago-shadow
  - issue_attrs: ['color', 'color', 'color', 'color', 'color']
  - current_color: None

- `DA6672-700-37` — Tenis Nike Craft General Purpose Shoe Tom Sachs Archive Dark Sulfur
  - handle: tenis-nike-craft-general-purpose-shoe-tom-sachs-archive-dark-sulfur
  - issue_attrs: ['color', 'color', 'color', 'color', 'color']
  - current_color: None

- `HF8022300-7` — Yuto Horigome x Dunk Low SB Matcha
  - handle: yuto-horigome-x-dunk-low-sb-matcha
  - issue_attrs: ['color', 'color', 'color', 'color', 'color']
  - current_color: None

- `HQ7978-103-41` — Tênis Jordan 5 Retro White Metallic (2026) Metalizado
  - handle: tenis-jordan-5-retro-white-metallic-2026-metalizado
  - issue_attrs: ['color', 'color', 'color', 'color', 'color']
  - current_color: None

- `JI3098-6` — Tênis Adidas Samba OG x Disney Pixar Toy Story
  - handle: tenis-adidas-samba-og-x-disney-pixar-toy-story
  - issue_attrs: ['color', 'color', 'color', 'color', 'color']
  - current_color: None

- `LLM-2319326-L` — Jaqueta Lululemon Define Cropped Nulu Light Ivory/Gold/Gold Off White
  - handle: define-cropped-jacket-nulu
  - issue_attrs: ['color', 'color', 'color', 'color', 'color']
  - current_color: None

- `IR1888-700-35` — Tenis Nike SB Dunk Low Pro Muni Lightning Denim Turquoise Turquesa
  - handle: tenis-nike-sb-dunk-low-pro-muni-lightning-denim-turquoise-turquesa
  - issue_attrs: ['color', 'color', 'color', 'color', 'color']
  - current_color: None

- `OXV-2733022-435` — Tênis Onitsuka Tiger x Versace TAI-CHI Sakura Suede Têniss Green
  - handle: tenis-onitsuka-tiger-x-versace-tai-chi-sakura-suede-sneakers-green
  - issue_attrs: ['color', 'color', 'color', 'color', 'color']
  - current_color: None

- `LK-3733854-L` — Define Jacket Nulu Rose/Gold
  - handle: define-jacket-nulu-rose-gold
  - issue_attrs: ['color', 'color', 'color', 'color', 'color']
  - current_color: None

## Files

- Review items JSON: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/approval-packets/gmc-residual-manual-enrichment-batch8-20260608/manual_review_items.json`