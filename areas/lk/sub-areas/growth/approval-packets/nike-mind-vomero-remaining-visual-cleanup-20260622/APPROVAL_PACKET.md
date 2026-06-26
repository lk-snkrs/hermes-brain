# Approval Packet — Nike Mind/Vomero remaining visual cleanup — 2026-06-22

**Status:** read-only concluído; nenhum novo write externo executado.  
**Gerado:** 2026-06-22T17:24:51.640504+00:00  
**Theme production investigado:** `155065417950`  
**values_printed:** false.

## 1. Contexto

O merge production aprovado dos 4 snippets resolveu o objetivo principal de schema:

- `/collections/nike-mind-001`: `FAQPage = 1`, H1 único, HTTP 200, sem Liquid error.
- `/pages/guia-nike-mind-001-002`: `FAQPage = 1`, H1 único, HTTP 200, sem Liquid error.
- `/collections/nike-vomero-premium`: `FAQPage = 1`, H1 único, HTTP 200, sem Liquid error.

Ainda restaram blocos visuais editoriais legacy, vindos de assets fora dos 4 snippets já aprovados.

## 2. Asset map read-only

| Asset | Sinais encontrados |
|---|---|
| `sections/lk-nike-mind-ai-visibility-v7.liquid` | `lk-nike-mind-ai-visibility-v7-citable`, `lk-goc-nike-mind-v7`, `lk-nike-mind-ai-visibility-v7` |
| `sections/lk-vomero-premium-ai-visibility-v7.liquid` | `lk-vomero-premium-ai-visibility-v7-citable`, `lk-goc-vomero-premium-v7`, `lk-vomero-premium-ai-visibility-v7` |
| `templates/collection.nike-mind-ai-v7.json` | `lk-nike-mind-ai-visibility-v7` |
| `templates/collection.vomero-premium-ai-v7.json` | `lk-vomero-premium-ai-visibility-v7` |
| `templates/page.nike-mind-ai-v7.json` | `lk_nike_mind_page_ai_v7`, `lk-nike-mind-ai-visibility-v7` |
| `templates/page.vomero-premium-ai-v7.json` | `lk_vomero_premium_page_ai_v7`, `lk-vomero-premium-ai-visibility-v7` |

## 3. Diagnóstico

Os blocos visuais restantes são renderizados por **sections de AI visibility v7** incluídas em templates específicos:

- Nike Mind:
  - `sections/lk-nike-mind-ai-visibility-v7.liquid`
  - `templates/collection.nike-mind-ai-v7.json`
  - `templates/page.nike-mind-ai-v7.json`

- Vomero Premium:
  - `sections/lk-vomero-premium-ai-visibility-v7.liquid`
  - `templates/collection.vomero-premium-ai-v7.json`
  - `templates/page.vomero-premium-ai-v7.json`

Esses assets explicam por que o schema já ficou limpo, mas alguns blocos visuais ainda aparecem no HTML público.

## 4. Recomendações

### Opção A — Mais conservadora, recomendada

Criar **DEV preview** desativando somente as duas sections visuais v7:

1. `sections/lk-nike-mind-ai-visibility-v7.liquid`
2. `sections/lk-vomero-premium-ai-visibility-v7.liquid`

Estratégia: substituir o conteúdo por comentário/no-op no DEV theme, sem alterar templates nem assignments.

**Por que é mais segura:**

- Menor superfície de mudança.
- Mantém templates e estrutura Shopify intactos.
- Rollback simples: restaurar 2 sections.
- Evita tocar em template JSON que pode estar atribuído a páginas/collections.

### Opção B — Mais estrutural

Remover as sections dos templates JSON:

- `templates/collection.nike-mind-ai-v7.json`
- `templates/page.nike-mind-ai-v7.json`
- `templates/collection.vomero-premium-ai-v7.json`
- `templates/page.vomero-premium-ai-v7.json`

**Risco:** maior, porque muda composição de template e pode afetar páginas atribuídas.

## 5. Escopo proposto para próximo DEV preview

Aplicar somente no DEV theme `155065450718`:

- `sections/lk-nike-mind-ai-visibility-v7.liquid` → no-op/comment.
- `sections/lk-vomero-premium-ai-visibility-v7.liquid` → no-op/comment.

Não alterar:

- production theme;
- templates JSON;
- snippets já aplicados;
- produtos;
- preço;
- estoque/disponibilidade;
- ordenação;
- desconto;
- PDPs;
- GMC/feed;
- campanhas;
- Klaviyo/WhatsApp;
- checkout.

## 6. QA esperado do DEV preview

URLs com `preview_theme_id=155065450718`:

- `/collections/nike-mind-001`: HTTP 200, H1 1, FAQPage 1, `Guia editorial LK` sem duplicidade, sem `lk-nike-mind-ai-visibility-v7-citable`, sem Liquid error.
- `/pages/guia-nike-mind-001-002`: HTTP 200, H1 1, FAQPage 1, sem bloco final duplicado, sem `lk-nike-mind-ai-visibility-v7-citable`, sem Liquid error.
- `/collections/nike-vomero-premium`: HTTP 200, H1 1, FAQPage 1, sem `lk-vomero-premium-ai-visibility-v7-citable`, sem Liquid error.

## 7. Aprovação necessária para executar DEV preview

> Aprovo aplicar no **Shopify DEV theme `155065450718`** somente o preview que desativa as duas sections visuais legacy `sections/lk-nike-mind-ai-visibility-v7.liquid` e `sections/lk-vomero-premium-ai-visibility-v7.liquid`, sem mexer em production, templates JSON, snippets já aplicados, produtos, preço, estoque, ordenação, descontos, PDPs, GMC/feed, campanhas, Klaviyo/WhatsApp ou checkout, com backup, readback, QA público e rollback.

## 8. Evidência local

- Asset map: `growth/work/nike-mind-vomero-remaining-visual-blocks-20260622/asset-map-readonly.json`
- Assets com hit salvos no mesmo workdir para auditoria local.
