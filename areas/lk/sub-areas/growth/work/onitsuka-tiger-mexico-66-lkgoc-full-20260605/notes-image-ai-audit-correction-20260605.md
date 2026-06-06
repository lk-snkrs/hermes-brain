# Onitsuka Mexico 66 — Correção após auditoria visual IA

Data: 2026-06-05T17:21:29

Lucas apontou corretamente que uma imagem do hero não tinha nenhum tênis visível. Auditoria visual confirmou: a imagem mostrava torso/bolsa/texto, sem sneaker no crop.

Correção em DEV:
- Removidas imagens externas Vogue do hero da Mexico 66.
- Substituídas por imagens do próprio catálogo LK com tênis inteiro visível:
  - Mexico 66 Kill Bill amarelo.
  - Mexico 66 White Black.
  - Mexico 66 SD Cream Birch.
- CSS da coleção alterado para evitar crop:
  - `object-fit: contain`.
  - `object-position: center bottom`.
- QA Playwright confirmou mobile e desktop:
  - imagens carregadas;
  - `objectFit = contain`;
  - `objectPosition = 50% 100%`;
  - desktop: 3 imagens visíveis;
  - mobile: imagem principal visível e demais ocultas até interação conforme padrão do hero.

Regra criada: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/rules/REGRA-LKGOC-AUDITORIA-VISUAL-HERO-TENIS.md`.
