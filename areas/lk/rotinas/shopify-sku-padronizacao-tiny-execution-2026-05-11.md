# LK Shopify SKU padronizado para Tiny — execução aprovada — 2026-05-11

Status: **concluído e verificado**. Lucas aprovou explicitamente a alteração via Telegram: “padronize o sku da Shopify idêntico ao do Tiny, pode alterar ok?”.

## Resultado
- Planejados com alta confiança + código Tiny não-vazio: 8
- Alterados na Shopify: 8
- Falhas: 0
- Verificação live pós-write: 8/8 OK
- Itens sem alteração/pulados na Fila B: 25

## Alterações aplicadas
- **Tênis Onitsuka Tiger Mexico 66 Kill Bill Amarelo — tam. 37**: `1183C102751-4` → `1183C102 751-4` — verificado: `1183C102 751-4`
- **Tênis Onitsuka Tiger Mexico 66 Kill Bill Amarelo — tam. 42.5**: `1183C102751-8` → `1183C102 751-8` — verificado: `1183C102 751-8`
- **Tênis Onitsuka Tiger Mexico 66 Kill Bill Amarelo — tam. 40**: `1183C102751-9` → `1183C102 751-9` — verificado: `1183C102 751-9`
- **Tênis Onitsuka Tiger Mexico 66 Chrome Silver Prata — tam. 37**: `1183B566021-4` → `1183B566 021-4` — verificado: `1183B566 021-4`
- **Tênis Onitsuka Tiger Mexico 66 Chrome Silver Prata — tam. 35.5**: `[vazio]` → `1183B566 021-9` — verificado: `1183B566 021-9`
- **Tênis Onitsuka Tiger Mexico 66 Kill Bill Amarelo — tam. 39**: `1183C102751-6` → `1183C102 751-6` — verificado: `1183C102 751-6`
- **Tênis Onitsuka Tiger Mexico 66 Kill Bill Amarelo — tam. 35**: `1183C102751-2` → `1183C102 751-2` — verificado: `1183C102 751-2`
- **Tênis Onitsuka Tiger Mexico 66 Kill Bill Amarelo — tam. 36**: `1183C102751-3` → `1183C102 751-3` — verificado: `1183C102 751-3`

## Itens pulados / sem write
- SKUs que já estavam idênticos ao Tiny não foram alterados.
- Itens cujo Tiny estava com `codigo` vazio não foram alterados.
- Itens onde a variant Shopify não foi encontrada com confiança suficiente não foram alterados.

## Backup e rollback
- Backup completo de `variant_id`, SKU antigo e SKU novo: `reports/lk-shopify-sku-padronizacao-tiny-execution-2026-05-11.json`.
- Resultado REST verificado: `reports/lk-shopify-sku-padronizacao-tiny-rest-result-2026-05-11.json`.
- Rollback possível por `variant_id`, reaplicando `rollback_sku` via Shopify `PUT /variants/{id}.json`.

## Guardrails
- Não alterei preço, estoque, título, handle, produto, imagem, coleção, campanha, Klaviyo, WhatsApp, fornecedor, Tiny ou banco.
- A única escrita externa executada foi o campo SKU de variants Shopify com mapeamento Tiny não-vazio e alta confiança.
- Tiny segue como fonte de verdade de estoque; esta rotina apenas alinhou identificação SKU Shopify↔Tiny.
