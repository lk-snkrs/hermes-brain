# Playbook — GMC/Product Data LK Growth

Data: 2026-06-05
Status: template operacional local/read-only até aprovação escopada.

## Quando usar

Use para Merchant Center, feed, atributos, `link_template`, landing errors, missing color, preço, GTIN, product data quality e diagnósticos API/feed.

## Workers

- Growth Data Scout
- GMC/Product Data Analyst
- SEO/GEO Analyst, se a questão envolver landing/search demand
- Growth Governor/Critic
- LK Shopify handoff, se a causa estiver na superfície Shopify/theme/PDP

## Fluxo

1. **Classificar issue**
   - Tipo: preço / color / link_template / landing / GTIN / availability / outro:
   - Offer IDs/SKUs afetados:
   - Fonte GMC:
   - Fonte Shopify/Admin/read-only:

2. **Evidência mínima**
   - GMC product/status export:
   - Shopify `.js`/Admin read-only:
   - URL pública/variant URL:
   - Histórico/packet anterior:
   - Limitações:

3. **Diagnóstico**
   - Feed/API vs landing/theme vs lag/reprocessamento:
   - Risco de bulk:
   - Se `price_updated`, separar final price, salePrice, compare_at ou falso positivo/lag.
   - Se missing color, rejeitar evidência fraca baseada só em tamanho/SKU.

4. **Packet**
   - Micro-pilot ou read-only investigation:
   - Campos/offer IDs exatos:
   - Snapshot/rollback necessário:
   - Readback esperado:
   - Stop condition:

5. **Handoff**
   - Para LK Shopify se a correção exigir theme/PDP/variant visible signal.
   - Para Lucas se exigir Product API/feed/fetchNow/supplemental write.

## Aprovação sugerida

> Aprovo LK Growth preparar/executar somente o packet GMC descrito para [offer IDs/SKUs/campo], com snapshot, rollback, readback e sem bulk fora do escopo. Não aprovo alterações em preço/estoque/theme/Shopify fora deste packet.

## Bloqueios

- Não bulk patch.
- Não inventar GTIN/cor.
- Não repetir write quando Merchant/Automatic Item Updates sobrescreve readback.
- Não publicar/suprimir produto DRAFT automaticamente.
