# Approval Packet — GMC Missing Color Micro-pilot — 2026-06-08

Status: preview only / sem write GMC

Candidatos high-confidence: 50

Regra usada: preencher `color` apenas quando a cor aparece explicitamente no último token do title em português.

## Guardrails

- Não alterar preço, estoque, disponibilidade, GTIN ou título.
- Não executar ProductInput/feed write sem aprovação explícita.
- Antes de write: snapshot/readback de cada offerId e rollback por patch do valor anterior.

## Amostra de candidatos

- `JI3185-7`
  - title: Tênis Adidas Samba OG Cream White Cardboard Creme
  - color atual: None
  - color proposto: creme

- `u1906lbn3`
  - title: Tênis New Balance 1906L Preto Couro Mesh Preto
  - color atual: None
  - color proposto: preto

- `HV0823-100-5`
  - title: Tênis Nike Air Jordan 4 Retro Forget Me Not Azul
  - color atual: None
  - color proposto: azul

- `BQ6472104-1`
  - title: Tênis Nike Air Jordan 1 Mid Kentucky Blue Azul
  - color atual: None
  - color proposto: azul

- `1183C468200-2`
  - title: Onitsuka Tiger Mexico 66 SD Metallic Series Desert Camp Cream Dourado
  - color atual: None
  - color proposto: dourado

- `u1906lbn6`
  - title: Tênis New Balance 1906L Preto Couro Mesh Preto
  - color atual: None
  - color proposto: preto

- `ONI-0995678-35`
  - title: Tênis Onitsuka Tiger Mexico 66 Fringe Mocha Brown/Dark Brown Marrom
  - color atual: None
  - color proposto: marrom

- `HV0823-100-6`
  - title: Tênis Nike Air Jordan 4 Retro Forget Me Not Azul
  - color atual: None
  - color proposto: azul

- `u9060aga-8`
  - title: Tênis New Balance 9060 Grey Day 2025 Cinza
  - color atual: None
  - color proposto: cinza

- `ALO-2441950-39`
  - title: Tênis Alo Yoga Alo Runner Pink Rosa
  - color atual: None
  - color proposto: rosa

- `HQ4309-610-40`
  - title: Chinelo Slide Nike Mind 001 Pearl Pink Rosa
  - color atual: None
  - color proposto: rosa

- `1183A201-126-5`
  - title: Tênis Onitsuka Tiger Mexico 66 White Black Branco
  - color atual: None
  - color proposto: branco

- `3MG10844970-40`
  - title: Tênis On Running x Kith ON K-Tech 2 Spirulina Barley Verde
  - color atual: None
  - color proposto: verde

- `YZY-2566238-43`
  - title: Tênis Adidas Yeezy Boost 350 V2 Earth Marrom
  - color atual: None
  - color proposto: marrom

- `U204L6A6-34`
  - title: Tênis New Balance 204L Reflection Bege
  - color atual: None
  - color proposto: bege

- `U204L2SZ-36`
  - title: Tênis New Balance 204L Sea Salt Linen Bege
  - color atual: None
  - color proposto: bege

- `JI0073-3`
  - title: Tênis Adidas Gazelle R Disney Pixar Toy Story Laranja
  - color atual: None
  - color proposto: laranja

- `FZ5042-041-44`
  - title: Tênis Nike Air Jordan 1 Low SE Repaired Denim Swoosh Azul
  - color atual: None
  - color proposto: azul

- `IQ7604-104`
  - title: Tênis Nike Air Jordan 1 Retro Low OG SP Travis Scott Sail Tropical Pink Rosa
  - color atual: None
  - color proposto: rosa

- `OXV-3513694-405`
  - title: Tênis Onitsuka Tiger x Versace TAI-CHI Sakura Suede Têniss Blue Azul
  - color atual: None
  - color proposto: azul

- `ST75`
  - title: Shorts Saint Studio Everywear Caqui Bege
  - color atual: None
  - color proposto: bege

- `JR1639-4`
  - title: Tênis Adidas SL 72 Og Court Green Cow Print Bege
  - color atual: None
  - color proposto: bege

- `ALO-2441950-43`
  - title: Tênis Alo Yoga Alo Runner Pink Rosa
  - color atual: None
  - color proposto: rosa

- `HV0823-100-2`
  - title: Tênis Nike Air Jordan 4 Retro Forget Me Not Azul
  - color atual: None
  - color proposto: azul

- `43774078387710`
  - title: Tênis Adidas Samba Jane White Blue Gum Branco
  - color atual: None
  - color proposto: branco

## Approval necessário

Para executar: “Aprovo micro-piloto GMC color 2026-06-08 nos candidatos do preview, com snapshot/readback/rollback.”