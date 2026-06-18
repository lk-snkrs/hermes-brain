# Receipt — mm-google-shopping GPC + condition full

- Criado: 2026-06-17T21:06:07.656439+00:00
- Aprovação: Lucas — “fazer 1, 2 e 3”.
- Escopo 1: normalizar `product.mm-google-shopping.google_product_category` removendo `.0`.
- Escopo 2: preencher `google_product_category` dos não-calçados por `productType`.
- Escopo 3: preencher/normalizar `variant.mm-google-shopping.condition = new`.

## Resultado
- Produtos ativos escaneados: 1838
- Product GPC alterações tentadas: 1090
- Product GPC readback OK: 1090
- Product GPC falhas: 0
- Variant condition alterações tentadas: 13347
- Variant condition readback OK: 13347
- Variant condition falhas: 0
- Erros API/batch: 0

## Pós-check
- GPC faltando: 0
- GPC com `.0` restante: 0
- Condition faltando: 0
- Condition diferente de `new`: 0

## Excluído
- preço, estoque, disponibilidade, criação/remoção de produto, SKU, MPN, theme, campanhas, writes diretos no GMC.

## Rollback
- Restaurar via `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/gmc/mm-google-shopping-gpc-condition-full-20260617T205005Z/backup-before.json`.

## Mapa productType → google_product_category
- Beleza: `469`
- Bolsa: `3032`
- Boné: `173`
- Bota: `187`
- Calça: `204`
- Camisa: `212`
- Camiseta: `212`
- Chinelo Slide: `187`
- Colecionável: `6058`
- Jaqueta: `5598`
- Livro: `784`
- Manutenção: `1933`
- Meia: `213`
- Mochila: `100`
- Moletom: `5322`
- Polo: `212`
- Saia: `1581`
- Shorts: `207`
- Suéter: `5322`
- Tenis: `187`
- Top: `212`
- Tênis: `187`
- Vestido: `2271`
- Óculos: `178`