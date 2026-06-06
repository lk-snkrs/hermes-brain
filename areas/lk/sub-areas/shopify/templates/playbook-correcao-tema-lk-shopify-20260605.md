# Playbook — Correção de tema LK Shopify

Data: 2026-06-05
Status: template operacional local/read-only até aprovação escopada.

## Quando usar

Use para correção de tema, Liquid, CSS, section, snippet, asset, PDP, collection, cart, search, header, menu, footer, grid, botão, imagem, spacing ou bug mobile/desktop.

## Workers

1. Shopify Surface Mapper
2. Theme/Feature Architect
3. Preview/Diff Builder
4. Shopify QA Visual Worker
5. Rollback/Risk Reviewer
6. Readback/Receipt Verifier — só após execução aprovada

## Fluxo

1. **Classificar superfície**
   - URL/storefront afetado:
   - Admin/theme/dev theme, se conhecido:
   - Arquivos prováveis: section/snippet/asset/template/CSS:
   - Reproduzível em mobile, desktop ou ambos:

2. **Snapshot antes**
   - Screenshot mobile/desktop quando possível.
   - Estado atual do asset/theme quando houver leitura.
   - Tema live vs dev theme.

3. **Diagnóstico**
   - Problema observado:
   - Causa provável:
   - Risco de tocar superfície errada:
   - Dependências de app/script:

4. **Preview/diff**
   - Mudança proposta:
   - Arquivos/campos afetados:
   - Antes/depois esperado:
   - Caminho obrigatório: dev theme/branch → GitHub PR → merge/deploy/readback. Produção direta no tema live é bloqueada:

5. **QA mínimo**
   - Mobile principal.
   - Desktop principal.
   - CTA/click principal.
   - Regressão em PDP/collection/cart, se afetar compra.

6. **Rollback**
   - Asset anterior salvo ou diff reversível.
   - Como restaurar:
   - Tempo/risco:

## Bloqueios

- Nunca escrever direto no tema Shopify de produção/live para Liquid/CSS/JS/section/snippet/asset. Alteração de tema deve ir por dev theme/branch, GitHub PR, merge para `production`, deploy/readback/QA e receipt.
- Produto/coleção/catálogo é outra classe de write: pode ser permitido somente no playbook próprio, com aprovação escopada, preview, rollback e readback.
- Não instalar app, alterar webhook, pixel ou secret neste playbook.
- Se a mudança vira feature nova, migrar para `playbook-feature-cart-drawer-minicart-20260605.md`.

## Aprovação sugerida

> Aprovo LK Shopify executar a correção de tema exatamente neste alvo: [theme/dev theme/live], [arquivos/campos], [URLs afetadas], com snapshot, QA mobile/desktop, readback e rollback. Não aprovo alterações fora desse escopo.
