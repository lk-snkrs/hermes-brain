# Playbook — Feature Shopify: cart drawer / minicart / fluxo de compra

Data: 2026-06-05
Status: template operacional local/read-only até aprovação escopada.

## Quando usar

Use para cart drawer, minicart, quick add, quick view, sticky add-to-cart, barra de frete grátis, upsell/cross-sell, trust blocks, shipping estimator, size guide, busca/filtro ou feature que mexa no fluxo de compra.

## Workers

1. Shopify Surface Mapper
2. Theme/Feature Architect
3. CRO/UX Reviewer
4. App/Integration/Tracking Checker
5. Preview/Diff Builder
6. Shopify QA Visual Worker
7. Rollback/Risk Reviewer
8. Readback/Receipt Verifier — só após execução aprovada

## Fluxo

1. **Objetivo e escopo**
   - Feature:
   - Dor que resolve:
   - Página/fluxo afetado:
   - Métrica de sucesso esperada:

2. **Arquitetura segura**
   - Dev theme obrigatório por padrão.
   - Arquivos prováveis: sections/snippets/assets/templates/config.
   - Dependências: app, script, pixel, analytics, Klaviyo, Meta, GMC, Judge.me, frete.
   - Eventos afetados: view_item, add_to_cart, begin_checkout, checkout, purchase.

3. **CRO/UX**
   - Hipótese:
   - Risco de fricção:
   - Mobile-first:
   - Microcopy/CTA:
   - Estado vazio/erro/loading:

4. **Preview/diff**
   - Antes/depois visual.
   - Componentes criados/alterados.
   - Campos/settings configuráveis.
   - O que fica fora do escopo.

5. **QA obrigatório**
   - Mobile: abrir, adicionar produto, alterar quantidade, remover, fechar, checkout.
   - Desktop: mesmo fluxo.
   - Produto com e sem variante/tamanho.
   - Produto indisponível, se aplicável.
   - Tracking não duplicado.

6. **Rollback**
   - Reverter theme assets/settings.
   - Desativar bloco/section sem quebrar checkout.
   - Voltar ao cart atual.

## Bloqueios

- App install, webhook, pixel novo, Klaviyo/Meta/GMC write e produção live exigem packet específico.
- Não decidir preço, frete, estoque, desconto ou promessa comercial.
- Se virar coleção editorial/LKGOC, rotear dono para `[LK] Otimização de Coleções`.

## Aprovação sugerida

> Aprovo LK Shopify implementar a feature [nome] no [dev theme/live] exatamente com os arquivos/campos listados, QA mobile/desktop, tracking check, readback e rollback. Não aprovo app/webhook/pixel/campanha/preço/estoque fora do escopo.
