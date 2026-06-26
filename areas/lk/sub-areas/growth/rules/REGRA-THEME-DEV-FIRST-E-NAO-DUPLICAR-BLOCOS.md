# Regra Growth LK — Theme dev-first e não duplicar blocos existentes

Atualizado: 2026-06-07T14:20:51.011697+00:00

## Regra obrigatória

1. **Nunca implementar diretamente em theme production.**
   - Qualquer alteração de layout/theme/CRO deve ir primeiro para `lk-new-theme/dev` ou outro theme de desenvolvimento explicitamente escolhido.
   - Production só recebe merge/promoção depois de QA/readback e aprovação explícita de merge.

2. **Não criar bloco novo quando já existe bloco canônico para a função.**
   - Antes de adicionar hero/top block/CTA/guia, localizar a estrutura existente da página.
   - Se a página já tem `Guia LK` depois do grid, melhorias de conteúdo/SEO/GEO devem ser propostas ali, não duplicadas no topo.
   - Topo/hero deve continuar produto-first quando esse for o padrão da collection.

3. **Fluxo correto para collection com guia existente**
   - Auditar estrutura atual.
   - Identificar bloco canônico existente: hero, grid, guide panel, FAQ, schema.
   - Propor alteração pontual no bloco correto.
   - Implementar no dev.
   - Validar preview visual + Admin readback.
   - Só então pedir aprovação de merge para production.

## Incidente que originou esta regra

Na Nike Mind, foi criado indevidamente um bloco CRO/topo duplicado no theme production e depois no dev, apesar de já existir um Guia LK pós-grid. Isso foi corrigido com rollback de production e remoção dos blocos extras do dev.

## Estado corrigido

- Production theme rollback realizado e validado.
- Dev theme sem bloco duplicado no topo.
- Bloco extra no Guia LK removido.
- Production permaneceu limpo após a correção.

## Receipts relacionados

- Rollback production: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/shopify-production/nike-mind-approved-3-20260607T123858Z/ROLLBACK_IMMEDIATE_THEME_PRODUCTION_20260607T131542Z`
- Reversão dev do bloco extra: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/theme-dev/nike-mind-revert-guide-extra-block-20260607T140403Z`
