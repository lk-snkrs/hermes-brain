# Approval Packet — GMC Product Data P1 micro-pilot — 2026-06-22

**Status:** read-only/approval packet; nenhum write externo.  
**Gerado:** 2026-06-22T17:50:07.989491+00:00  
**Fonte:** Merchant/Product Data Ranking Review 2026-06-18, hub GMC, receipts históricos.  
**values_printed:** false.

## Veredito

GMC continua sendo a terceira frente porque mexe em elegibilidade comercial, mas deve ser tratado separado de SEO/CRO. Próxima ação não deve ser correção em massa; deve ser **read-only current-state + micro-piloto** no surface correto: Shopify → Simprosys → GMC.

## Evidência 2026-06-18

- Merchant lido: 23.744 products/statuses.
- Shopping aprovado/reprovado: 12.181 / 11.563.
- LocalSurfaces aprovado/reprovado: 986 / 10.582.
- `mhlsf_full_missing_valid_link_template`: 11.267 offers.
- `missing_item_attribute_for_product_type`: 2.530 produtos / 5.314 instâncias.
- `local_stores_lack_inventory`: 10.582 produtos — **não consultar estoque por este agente**; qualquer reconciliação vai para `lk-stock`.

## Risco conhecido

- Link template/local LIA pode ser sobrescrito por Simprosys/dataSource se corrigido no surface errado.
- Atributos de produto devem ser Shopify-first quando o dado base é produto/variante/metafield.
- Não inventar GTIN; se GTIN real existir, preencher fonte correta; se não, usar política `identifier_exists` com aprovação.

## Próxima ação recomendada

1. Rodar current-state read-only GMC atualizado.
2. Cruzar issues com focos comerciais: Mind 002, Onitsuka, Vomero, 204L.
3. Montar micro-piloto de 10–20 ofertas/produtos:
   - link_template: apenas se confirmar surface certo;
   - category/identifier: Shopify-first;
   - missing attributes: high-confidence apenas.
4. Não usar `fetchNow`/reprocessamento sem aprovação.

## Aprovação necessária para write futuro

Qualquer Shopify metafield/ProductInput/GMC/Simprosys write exige aprovação escopada, backup/readback/rollback e validação pós-processamento.
