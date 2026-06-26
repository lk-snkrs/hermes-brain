# Receipt DEV — LKGOC P0 Nike Mind 001/002

Data UTC: 2026-06-06T00:02:10.339781+00:00
Tema DEV: `155065450718` (`unpublished` verificado)
Coleção: `nike-mind-001` / Nike Mind
Collection ID: `463377826014`

## Fonte de priorização

P0 por score LK + fenômeno:

- Nike é marca #1 em receita 90 dias.
- Nike Mind foi classificado como P0 após Moon Shoe por score real da família e fenômeno comercial/cultural.
- Dados operacionais lidos no setup: 18 produtos na coleção.

## Implementação DEV

Arquitetura:

- Componente único: `snippets/lk-goc-collection.liquid`
- Section principal: `sections/lk-collection.liquid`
- Sem criação de snippet estrutural novo por coleção.

Mudanças:

- Adicionado branch `hero` para `nike-mind-001` no componente genérico LKGOC.
- Adicionado branch `guide` para `nike-mind-001` no componente genérico LKGOC.
- Section passou a renderizar `lk-goc-collection` para hero e guide de Nike Mind.
- Renders legados `lk-nike-mind-collection-hero` e `lk-nike-mind-guide-panel` deixam de ser usados para esta coleção.

## Regras aplicadas

- Imagens hero: pessoas usando produto / campanha oficial, não packshot.
- Crop: `object-position: center bottom` em todas as imagens.
- Desktop: “Ler mais” oculto.
- Desktop: collage alinhada ao topo de breadcrumbs (`deltaTop = 0`).
- Guide: padrão `lk-guide-standard-*`.
- FAQ: única e dentro do guia editorial.
- Production não alterado.

## QA DEV desktop

- Hero LKGOC: true
- Guide LKGOC: true
- Guide standard: true
- FAQ dentro do guia: true
- Perguntas/details dentro do guia: 4
- Details visíveis fora do guia: 0
- FAQ legada visível fora do guia: 0
- Imagens hero: 3
- `object-position`: `50% 100%`, `50% 100%`, `50% 100%`
- Packshot/product-only: false
- “Ler mais” desktop: false
- `deltaTop`: 0
- Legacy hero: false
- `.coll-rich-content`: false
- Liquid error: false
- Something went wrong: false
- H2: `Conforto sensorial, presença futurista.`

## QA DEV mobile

- Hero LKGOC: true
- Guide LKGOC: true
- FAQ dentro do guia: true
- Perguntas/details dentro do guia: 4
- Details visíveis fora do guia: 0
- Imagens hero: 3
- `object-position`: `50% 100%`, `50% 100%`, `50% 100%`
- Packshot/product-only: false
- “Ler mais” mobile: true
- Liquid error: false
- Something went wrong: false
- `.coll-rich-content`: false

## Preview

`https://lk-sneakerss.myshopify.com/collections/nike-mind-001?preview_theme_id=155065450718`

## Próximo passo

Aguardar validação visual e aprovação explícita do Lucas para Production.


## Ajuste solicitado — guia refeito + respiro produto/guia

Data UTC: 2026-06-06T01:36:23.526089+00:00

Pedido Lucas: corrigir falta de espaço entre grid de produtos e guia; refazer guia Nike Mind do zero.

Executado em DEV/unpublished `155065450718`:

- Guia Nike Mind refeito no branch `part: 'guide'` do `snippets/lk-goc-collection.liquid`.
- Novo H2: `Nike Mind 001/002: conforto sensorial com leitura de design`.
- Nova estrutura: resumo rápido, escolha Mind 001, escolha Mind 002, cores/presença, ajuste/compra segura, FAQ.
- FAQ ampliada para 5 perguntas.
- Espaçamento adicionado no guia: `margin-top: clamp(34px,5vw,72px)`.
- Medição desktop QA: gap entre último produto detectado e guia = `73px`; computed margin-top = `72px`.
- Section `lk-collection.liquid` confirmada renderizando `lk-goc-collection` para hero e guide de `nike-mind-001`.

QA pós-ajuste:

- Desktop: hero true, guide true, guide standard true, details = 5, FAQ fora do guia = 0, packshot hero false, delta breadcrumbs = 0, Liquid error false.
- Mobile: hero true, guide true, details = 5, product-only false, Liquid error false.

Production segue intocada.
