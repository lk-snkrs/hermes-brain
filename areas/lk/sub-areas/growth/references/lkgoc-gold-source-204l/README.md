# LKGOC Gold Source — New Balance 204L

Status: **aprovado por Lucas como layout perfeito**  
Registrado em UTC: `2026-06-03T18:16:08.331381+00:00`

## Fonte de verdade visual
- URL Production: https://lksneakers.com.br/collections/new-balance-204l
- Tema Production: `lk-new-theme/production` `155065417950` — role `main`
- Tema DEV: `lk-new-theme/dev` `155065450718` — role `unpublished`
- Asset: `sections/lk-collection.liquid`
- Bloco salvo: `gold-source-production-204l-block.liquid`
- SHA256 do bloco: `9a0a8a0efc8f3c1c470cd7bc6ed513e447efd60d09c529076f5a19968325888f`

## Regra LKGOC a partir deste registro
Este layout da coleção **New Balance 204L** é o padrão visual/canônico a ser **copiado e adaptado** para novas collections LKGOC.

Copiar:
- estrutura editorial hero + collage;
- hierarquia de texto: kicker, headline, parágrafo, read more;
- comportamento de collage/modal;
- densidade visual e espaçamento;
- CSS e classes base;
- tom premium/minimalista.

Adaptar apenas:
- handle/collection alvo;
- textos e links;
- imagens/alt text;
- FAQ/schema quando aplicável;
- nuances comerciais da coleção.

Não inventar:
- novo layout;
- nova arquitetura visual;
- novo design system;
- mudanças em Production sem DEV → QA → approval Lucas → merge.

## Namespace
- Preferencial: `lk-goc-*`.
- Compatibilidade visual temporária: aliases `lk-204l-*` podem permanecer enquanto CSS legado ainda depender deles.
- Proibido para novas execuções: `lk-lkgoc-*`.

## Observação de escalabilidade
O layout é escalável como padrão LKGOC, desde que a próxima etapa técnica seja consolidar o CSS comum em asset compartilhado `lk-goc-*`, reduzindo CSS inline por coleção e mantendo aliases legados só durante transição.

## Checks
```json
{
  "production_is_main": true,
  "dev_is_unpublished": true,
  "uses_lk_goc_root": true,
  "has_legacy_aliases_for_visual_compatibility": true,
  "no_lkgoc": true,
  "has_critical_css": true,
  "has_typography_css": true,
  "has_kicker_spacing_css": true,
  "has_body_copy_css": true,
  "public_status_200": true,
  "public_no_liquid": true,
  "public_no_imagem_pendente": true
}
```
