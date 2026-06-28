# LK-GOC Standard v1 — `lk-goc-*`

Atualizado em UTC: 20260603T162846Z

## Fonte canônica
A referência visual/editorial inicial do LK Growth Optimized Collections é:

- Collection gold source: New Balance 204L.
- Guide gold source: New Balance 204L Original Brasil — Guia LK.

Este padrão não cria novo layout: ele formaliza o padrão 204L aprovado como contrato reutilizável.

## Namespace oficial
- Padrão novo: `lk-goc-*`.
- Padrão puro exigido em novas/migradas implementações: somente `lk-goc-*` para componentes LKGOC.
- Namespace legado removido do padrão: `lk-204l-*`.
- Namespace transitório/obsoleto: `lk-lkgoc-*`.

## Contrato — Collection optimized block
Classes estruturais esperadas:

- `lk-goc-coll-preview`
- `lk-goc-coll-preview--{ collection_handle }`
- `lk-goc-coll-preview__inner`
- `lk-goc-copy`
- `lk-goc-kicker`
- `lk-goc-headline`
- `lk-goc-body`
- `lk-goc-read-more`
- `lk-goc-collage`
- `lk-goc-card`
- `lk-goc-card--large`
- `lk-goc-open-photo`
- `lk-goc-photo-modal`
- `lk-goc-photo-modal__close`

## Contrato — Guide/editorial page
Classes estruturais esperadas:

- `lk-goc-guide`
- `lk-goc-guide--{ guide_handle }`
- `lk-goc-guide-hero`
- `lk-goc-guide-eyebrow`
- `lk-goc-guide-intro`
- `lk-goc-guide-actions`
- `lk-goc-guide-section`
- `lk-goc-guide-grid`
- `lk-goc-guide-card`
- `lk-goc-guide-media`
- `lk-goc-guide-faq`
- `lk-goc-guide-cta`

## Regra de evolução
Toda melhoria aprovada em uma collection/guide LKGOC deve ser avaliada como melhoria do Standard LK-GOC.

Implicação operacional:
- não tratar patch como isolado por tema;
- manter contrato de classe estável;
- reaplicar melhorias em outros themes/collections otimizados por diff controlado;
- registrar receipt, rollback e impacto;
- nunca escrever em production sem approval explícito de Lucas.

## Gates obrigatórios
1. Tema DEV precisa ter `role: unpublished` verificado por API.
2. Readback API obrigatório.
3. Preview renderizado obrigatório.
4. Bloquear se houver:
   - `Liquid error`;
   - placeholder editorial visível;
   - FAQ/schema duplicado;
   - seletor JS quebrado;
   - guia fora do padrão;
   - imagem vazando/erro visual evidente.
5. Approval Lucas para merge/promoção Production.

## Estado DEV aprovado tecnicamente em 20260603T162846Z
Tema DEV: `156623372510` — `LK Curadoria Force Fix Preview 2026-06-03` — role `unpublished`.

Assets migrados em DEV:
- `sections/lk-collection.liquid`
- `sections/lk-nb204l-guide-lkgoc.liquid`

Checks técnicos de preview:
- Collection 204L: `lk-goc-*` presente; `lk-lkgoc-*` e `lk-204l-*` removidos do bloco renderizado.
- Guia 204L: `lk-goc-guide-*` presente, FAQ schema preservado, `lk-lkgoc-*` removido.
- Sem `Liquid error`.
- Sem `imagem pendente`.

## Atualização — padrão puro sem `lk-204l-*`

Registrado em UTC: 20260603T163131Z

Decisão Lucas: remover `lk-204l-*` do padrão novo e deixar apenas `lk-goc-*` nas áreas LKGOC migradas.

Estado DEV validado:
- Tema DEV: `156623372510`, role `unpublished`.
- Bloco Collection 204L: sem `lk-204l-*` e sem `lk-lkgoc-*` no bloco renderizado.
- JS do bloco Collection 204L: seletores puros `lk-goc-*`.
- Guia 204L: contrato `lk-goc-guide-*` preservado.
- Preview técnico: status 200, sem `Liquid error`, sem `imagem pendente`.

Regra daqui para frente:
- Não criar aliases `lk-204l-*` em novos blocos LKGOC.
- Se algum legado antigo depender de `lk-204l-*`, tratar como débito/migração, não como padrão.

