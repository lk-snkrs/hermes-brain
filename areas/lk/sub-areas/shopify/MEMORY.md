# MEMORY — LK Shopify

## Regras duráveis

- Tiny é fonte de verdade para estoque.
- Shopify é superfície de publicação/gatilho, não ledger de estoque.
- LK Shopify é especialista próprio dentro do LK OS, separado de LK Growth.
- Writes Shopify/Tiny exigem aprovação escopada, snapshot, preview, readback, receipt e rollback.
- Tema Shopify production/live nunca recebe write direto para Liquid/CSS/JS/section/snippet/asset. Mudanças de tema devem ir por dev theme/branch → GitHub PR/review → merge/deploy/readback/QA/receipt. Produto/coleção/catálogo é outra classe de write e segue playbook/aprovação próprios.
- Quando a tarefa envolver preço, disponibilidade ou promessa comercial, validar com LK Ops.
