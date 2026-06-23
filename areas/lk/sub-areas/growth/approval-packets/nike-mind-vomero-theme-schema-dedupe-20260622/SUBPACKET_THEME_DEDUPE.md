# Sub-packet — Theme/dev preview para deduplicar FAQ/schema Mind + Vomero — 2026-06-22

**Status:** necessário após QA público pós-cleanup.  
**Gerado em:** 2026-06-22T15:29:14.354104+00:00  
**Writes externos deste sub-packet:** 0.  
**values_printed:** false.

## Por que este sub-packet existe

Lucas aprovou aplicar cleanup de conteúdo/schema em collections/pages, com a condição explícita:

> se a duplicação de schema exigir theme, parar e trazer sub-packet/dev preview.

Após aplicar somente `descriptionHtml` nas collections `nike-mind-001` e `nike-vomero-premium`, o Admin readback ficou OK e o novo conteúdo aparece publicamente. Porém o HTML público ainda mostra duplicidade causada por blocos de theme/runtime, não pelo body editável da collection/page.

## Evidência pós-aplicação

### `/collections/nike-mind-001`

- HTTP 200.
- H1 único.
- Novo conteúdo aprovado aparece: `escolha por uso, não por hype`.
- Ainda restam:
  - `FAQPage` parsed blocks: 2, com 4 e 5 perguntas.
  - dois blocos visuais/runtimes:
    - `section#lk-guia-nike-mind-001-002` / `lk-guide-standard-panel--nike-mind-redo`;
    - `section#lk-nike-mind-ai-visibility-v7-citable` / `lk-goc-nike-mind-v7`.

### `/pages/guia-nike-mind-001-002`

- Admin body não contém o bloco final duplicado que aparece no HTML público; por isso não foi alterado.
- HTML público ainda injeta `section#lk-nike-mind-ai-visibility-v7-citable`.
- `FAQPage` permanece 1, então o problema principal aqui é visual/GEO duplicate, não schema duplicate.

### `/collections/nike-vomero-premium`

- HTTP 200.
- H1 único.
- Novo conteúdo aprovado aparece: `ZoomX, Air Zoom aparente e máximo amortecimento`.
- Ainda restam:
  - `FAQPage` parsed blocks: 2, com 2 e 5 perguntas; `FAQPage` string count 3 porque há também microdata/itemtype.
  - blocos visuais/runtimes:
    - early JSON-LD FAQ com 2 perguntas no head/theme;
    - `section#lk-guia-nike-vomero-premium` / `lk-vomero-premium-guide-panel`;
    - `section#lk-vomero-premium-ai-visibility-v7-citable` / `lk-goc-vomero-premium-v7`.

## Diagnóstico

O cleanup de conteúdo editável foi aplicado, mas a duplicidade restante está em theme/snippets/sections/scripts que injetam blocos adicionais nas páginas foco.

Não deve ser corrigido direto em produção. Próximo passo correto:

1. localizar o asset/snippet/section que injeta:
   - `lk-nike-mind-ai-visibility-v7-citable`;
   - `lk-vomero-premium-ai-visibility-v7-citable`;
   - `lk-guia-nike-mind-001-002` quando duplicado em collection;
   - `lk-guia-nike-vomero-premium` quando duplicado em collection;
2. preparar dev theme preview removendo apenas duplicatas para esses handles;
3. garantir que reste uma fonte canônica por página;
4. validar mobile/desktop e schema;
5. trazer approval packet separado para production theme.

## Escopo permitido no próximo dev preview

- Dev theme only.
- Apenas handles:
  - `/collections/nike-mind-001`;
  - `/pages/guia-nike-mind-001-002`;
  - `/collections/nike-vomero-premium`.
- Remover/inibir blocos duplicados, não alterar produtos, preço, estoque, ordem, imagens, menus, checkout, GMC/feed, campaigns ou Klaviyo.
- Preservar um bloco canônico de guia/FAQ por página.

## QA de aceite do dev preview

| Página | Critério |
|---|---|
| Mind collection | HTTP 200; H1 1; 1 bloco guia; 1 bloco citável; 1 FAQPage; sem Liquid error |
| Mind guide | HTTP 200; H1 1; sem bloco auto-linkado duplicado; FAQPage 1 |
| Vomero collection | HTTP 200; H1 1; 1 guia; 1 FAQ/schema; sem head FAQ duplicado |

## Aprovação sugerida para criar preview DEV

> Aprovo criar apenas um dev preview para deduplicar blocos de theme/schema nas páginas `/collections/nike-mind-001`, `/pages/guia-nike-mind-001-002` e `/collections/nike-vomero-premium`, sem publicar em produção e sem mexer em preço, estoque, produtos, ordenação, GMC/feed, campanhas, checkout ou Klaviyo. Trazer preview, diff, QA e rollback antes de qualquer production theme write.
