# Onitsuka Mexico 66 — ajuste de imagens do hero por feedback Lucas

Data: 2026-06-05T17:16:54
Ambiente: DEV/unpublished `155065450718`.

Feedback Lucas: trocar imagem principal ruim; imagens de hero precisam mostrar o tênis e ser alinhadas pela base, não pelo centro.

Ajustes feitos em DEV:
- Imagem principal trocada para referência editorial com sneaker visível.
- Três imagens do collage mantidas como referências fashion/on-foot.
- CSS do snippet alterado para `object-position: center bottom`.
- Contrato extra aplicado: `#lk-goc-mexico-66-image-base-align-20260605` com `object-position:center bottom!important` para `.lk-goc-coll-preview--mexico-66`.

QA técnico:
- As 3 imagens carregam (`complete=true`).
- Dimensões naturais retornadas.
- `objectPosition` computado: `50% 100%`.
- Screenshot: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/onitsuka-tiger-mexico-66-lkgoc-full-20260605/dev-mexico66-image-alignment-390.png`.
