# LKGOC — guardrail de implementação

Atualizado: 2026-06-03T13:04:08.010780+00:00

## Regra principal

Quando Lucas pedir uma coleção/página no padrão LKGOC, o correto é seguir a **lógica do LKGOC**, não criar uma página editorial nova nem uma coleção visualmente diferente.

## O que “seguir a lógica do LKGOC” significa

- Usar a arquitetura aprovada do LKGOC/204L como base visual e funcional.
- Manter o fluxo coleção -> guia -> seleção -> FAQ/trust, com aparência e hierarquia compatíveis.
- Adaptar somente conteúdo, naming, fontes e seleção de produtos para o novo modelo.
- Não inventar novo layout, hero, grid, card, bloco editorial ou narrativa visual fora do padrão.
- Se houver dúvida entre “ficar bonito” e “ficar igual à lógica LKGOC”, escolher a lógica LKGOC.
- Primeiro preparar em dev/preview; produção só com aprovação explícita.

## Referências de padrão já encontradas

- Coleção Sambae produção: `receipts/shopify-collections/sambae-collection-production-publish-20260603T122556Z/collection.public.html`
- Página Sambae aprovada: `receipts/shopify-pages/sambae-production-merge-confirm-20260603T122321Z/page.readback-admin.json`
- Dev LKGOC/204L Sambae: `receipts/dev/sambae-from-zero-clean-204l-dev-20260602T222505Z/sections-template-21157673894110__main.html`

## Checklist antes de aplicar qualquer LKGOC futuro

1. Comparar com Sambae aprovado.
2. Confirmar que o layout usa a mesma lógica de classes/componentes/hierarquia.
3. Confirmar que não há página editorial “solta” fora da estrutura.
4. Confirmar que coleção não recebeu bloco visual diferente do padrão LKGOC.
5. Gerar preview e QA visual.
6. Pedir aprovação antes de qualquer write em produção.

## Incidente que originou este guardrail

Em 2026-06-03, o Samba normal foi aplicado de forma errada: página e coleção foram feitas fora da lógica LKGOC. O conteúdo foi revertido e este guardrail foi criado para impedir repetição.
