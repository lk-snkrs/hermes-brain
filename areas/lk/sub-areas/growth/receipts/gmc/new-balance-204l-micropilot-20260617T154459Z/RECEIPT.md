# Receipt — Merchant New Balance 204L micro-piloto — 2026-06-17T15:54:06.392565+00:00

**Approval:** Lucas Telegram: “Aprovo” em resposta ao packet Merchant New Balance 204L.

## Resultado
- Landing errors avaliados por produto/URL: 3
- Landing errors patchados: 0
- Color targets após safety: 20
- Patches `color` OK: 20
- Patches `color` falha: 0
- Readback imediato no produto processado: 0 / 20 — esperado lag do Merchant.
- Readback 90s no produto processado: 20 / 20 confirmado.

## Rescan do cluster 204L após patch
- Itens 204L no Merchant: 228
- `missing_item_attribute_for_product_type`: caiu de 260 para 160 instâncias.
- `missing_color_count`: caiu de 67 para 47.
- `mhlsf_full_missing_valid_link_template`: 66 — fora do escopo deste micro-piloto.
- `landing_page_error`: 17 instâncias — não patchadas porque os produtos verificados estão DRAFT/sem Online Store URL.

## Escopo preservado
- Sem Shopify product write.
- Sem preço, estoque ou disponibilidade.
- Sem campanha, theme, checkout, Klaviyo/WhatsApp.
- Sem GTIN/MPN.
- Sem LIA/link_template.

## Landing-page errors
Não patchados: Admin Shopify mostrou produtos DRAFT/sem Online Store URL. Publicar produto, remover oferta do feed ou mexer na origem Simprosys fica fora do escopo aprovado e exige decisão separada.

## Rollback
- Antes em `backup-before.json`.
- Patches em `patch-results.json`.
- Readbacks em `readback-immediate.json`, `readback-delayed-90s.json` e `cluster-rescan-after.json`.
- Se houver regressão, remover/neutralizar override de `productAttributes.color` nos mesmos ProductInputs com nova aprovação.

values_printed=false
