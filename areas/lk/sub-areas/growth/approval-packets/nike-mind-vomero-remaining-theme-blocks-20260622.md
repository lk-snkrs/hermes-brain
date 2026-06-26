# Follow-up packet — remaining runtime visual blocks after production merge — 2026-06-22

**Status:** preparado; nenhum novo write executado.  
**Gerado:** 2026-06-22T17:05:59.422347+00:00  
**Contexto:** production merge aprovado dos 4 snippets foi aplicado, mas QA público mostrou que o schema foi deduplicado enquanto alguns blocos visuais ainda vêm de outros assets/sections/templates não cobertos pela aprovação.

## Resultado do merge aprovado

- `/collections/nike-mind-001`: `FAQPage` agora = 1; H1 = 1; sem Liquid error.
- `/pages/guia-nike-mind-001-002`: `FAQPage` = 1; H1 = 1; sem Liquid error.
- `/collections/nike-vomero-premium`: `FAQPage` agora = 1; H1 = 1; sem Liquid error.

## Pendência

- Mind ainda contém `lk-nike-mind-ai-visibility-v7-citable` visual/runtime em algumas superfícies, embora sem duplicar schema.
- Vomero ainda contém `lk-vomero-premium-ai-visibility-v7-citable` e `lk-guia-nike-vomero-premium` visual/runtime, embora o schema esteja em 1 FAQPage.

## Diagnóstico provável

Os blocos restantes vêm de sections/templates ou do snippet genérico `lk-goc-collection`, não dos 4 snippets aprovados e alterados.

## Próximo passo recomendado

Fazer read-only asset map e, se confirmado, preparar DEV preview + approval packet específico para remover somente os blocos visuais restantes. Não executar direto em produção sem nova aprovação escopada.
