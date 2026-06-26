# Receipt — Sambae page: mídia editorial + ajuste mobile

Data UTC: 2026-06-03T09:59:57.965322+00:00
Página: `/pages/guia-adidas-sambae`
Page ID: `127575949534`
Escopo aprovado no turno: Lucas pediu corrigir 2 pontos — adicionar seção de principais veículos/sites/blogs que publicaram sobre Sambae e ajustar o bloco “Por que entra no radar da curadoria LK” no mobile.

## Alterações aplicadas
- Inserida seção **Radar de mídia** antes de “Sinais editoriais”.
- Veículos/sites adicionados com links externos:
  - WWD — review/editorial sobre Adidas Sambae como premium Samba sneaker.
  - Who What Wear — pauta de celebrity style com Adidas Sambae.
  - Marie Claire — pauta de celebrity style com Adidas Sambae.
  - A Styled Life / Nayla Smith — blog de styling e review prático do Sambae.
- Ajuste CSS mobile no bloco “Por que entra no radar da curadoria LK”:
  - remove `min-height:245px` dos cards no mobile (`min-height:0`);
  - reduz padding dos cards;
  - limita o H2 em mobile para leitura mais limpa;
  - ajusta `em`/rodapé do card para não empurrar conteúdo.

## Evidência
- `page.before.json`: snapshot antes.
- `page.after.json`: snapshot depois.
- `public.render.html`: render público validado.
- `sambae-mobile-after.png`: screenshot mobile pós-ajuste.

## QA markers no render público
- `lk-press-grid`: presente.
- `WWD`, `Who What Wear`, `Marie Claire`, `A Styled Life`: presentes.
- `lk-media-card{min-height:0`: presente.
- `max-width:10.5em`: presente.

## Rollback
- Restaurar `body_html` de `page.before.json` via Admin API `PUT /pages/127575949534.json`.

## Revisão de impacto sugerida
- Em ~7 dias: GSC/GA4 da página `/pages/guia-adidas-sambae`, cliques para `/collections/adidas-sambae`, comportamento mobile e engajamento no bloco de mídia.
