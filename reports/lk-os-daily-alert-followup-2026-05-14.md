# LK OS Daily Alert Follow-up — 2026-05-14

Gerado em: `2026-05-15T11:31:40.005187+00:00`.
Fonte: `/opt/data/hermes_bruno_ingest/local_sql/lk_data_spine_snapshots/lk_os_daily_sales_brief_20260514_110130Z.json`.

## Resultado executivo

- P0 ruptura vendida/Tiny zero: `5` cards de preview criados.
- P1 cobertura baixa: `2` cards de revisão criados.
- P1 mapeamento desconhecido: `3` cards de saneamento criados.

## A. P0 — reposição/sourcing preview-only

1. **Tênis New Balance 9060 Triple White Branco**
   - SKU/tamanho: `U9060NRJ-43` / `43`
   - Vendido Shopify: `1`; Tiny oficial: `0.0`; Tiny ID: `1066638968`; match: `exact_norm_sku`
   - Preço atual LK local: `R$ 2.799,99`
   - Próxima correção segura: criar payload de decisão para Júlio/Notion **sem escrever Notion** e validar Droper primeiro; StockX/GOAT só como fallback exato se Droper não servir.

2. **Tênis Onitsuka Tiger Mexico 66 Black and White Preto**
   - SKU/tamanho: `1183C10200-4` / `37`
   - Vendido Shopify: `1`; Tiny oficial: `0.0`; Tiny ID: `1060293859`; match: `exact_norm_sku`
   - Preço atual LK local: `R$ 2.399,99`
   - Próxima correção segura: criar payload de decisão para Júlio/Notion **sem escrever Notion** e validar Droper primeiro; StockX/GOAT só como fallback exato se Droper não servir.

3. **Tênis Onitsuka Tiger Mexico 66 White Black Branco**
   - SKU/tamanho: `1183A201-126-2` / `35`
   - Vendido Shopify: `1`; Tiny oficial: `0.0`; Tiny ID: `1062980804`; match: `exact_norm_sku`
   - Preço atual LK local: `R$ 2.399,99`
   - Próxima correção segura: criar payload de decisão para Júlio/Notion **sem escrever Notion** e validar Droper primeiro; StockX/GOAT só como fallback exato se Droper não servir.

4. **Crocs Classic Clog x The Cars Lightning McQueen Vermelho**
   - SKU/tamanho: `205759 610-4` / `37`
   - Vendido Shopify: `1`; Tiny oficial: `0.0`; Tiny ID: `1056614644`; match: `exact_norm_sku`
   - Preço atual LK local: `n/d`
   - Próxima correção segura: criar payload de decisão para Júlio/Notion **sem escrever Notion** e validar Droper primeiro; StockX/GOAT só como fallback exato se Droper não servir.

5. **Livro Taschen The Ultimate Tênis Book 15 x 21**
   - SKU/tamanho: `9783836597982` / `sem tamanho informado`
   - Vendido Shopify: `1`; Tiny oficial: `0.0`; Tiny ID: `1067021253`; match: `exact_norm_sku`
   - Preço atual LK local: `R$ 329,99`
   - Próxima correção segura: criar payload de decisão para Júlio/Notion **sem escrever Notion** e validar Droper primeiro; StockX/GOAT só como fallback exato se Droper não servir.

## B. P1 — cobertura baixa

1. **Tênis Nike Moon Shoe SP Jacquemus Pale Pink Rosa**
   - SKU/tamanho: `HV8547-601-37.5` / `37.5`
   - Vendido Shopify: `1`; Tiny oficial: `1.0`; preço LK local: `R$ 4.999,99`
   - Próxima correção segura: monitorar/repor só após confirmar disponibilidade por canal; sem compra automática.

2. **Calça Alo Yoga Suit Up Trouser (Regular) Preto**
   - SKU/tamanho: `w51432r_01-2` / `XS/PP`
   - Vendido Shopify: `1`; Tiny oficial: `1.0`; preço LK local: `R$ 1.549,99`
   - Próxima correção segura: monitorar/repor só após confirmar disponibilidade por canal; sem compra automática.

## C. P1 — saneamento Shopify SKU ↔ Tiny

1. **Camiseta Manga Longa Pace Relaxed Waffle Knit Preto**
   - SKU/tamanho Shopify vendido: `PAC-5181790-L` / `G/L`
   - Evidência local: Shopify variant rows `0`; Tiny exact-code rows `0`; Daily Brief match `no_safe_candidate`
   - Próxima correção segura: fila humana de saneamento; não criar campanha/reposição automática enquanto Tiny não tiver candidato seguro/saldo legível.

2. **The Peptide Lip Tints Rhode Multicolor**
   - SKU/tamanho Shopify vendido: `LIP` / `Vanilla`
   - Evidência local: Shopify variant rows `4`; Tiny exact-code rows `1`; Daily Brief match `no_safe_candidate`
   - Próxima correção segura: fila humana de saneamento; não criar campanha/reposição automática enquanto Tiny não tiver candidato seguro/saldo legível.

3. **Camiseta Saint Studio Boxy SUPIMA Vermeer Off White**
   - SKU/tamanho Shopify vendido: `SST-9563614-L` / `G/L`
   - Evidência local: Shopify variant rows `0`; Tiny exact-code rows `0`; Daily Brief match `no_safe_candidate`
   - Próxima correção segura: fila humana de saneamento; não criar campanha/reposição automática enquanto Tiny não tiver candidato seguro/saldo legível.

## Guardrails

- No Shopify/Tiny/Notion/GMC/Klaviyo/WhatsApp/supplier write.
- No purchase, reservation, supplier contact or campaign.
- Sourcing cards remain preview-only; exact Droper/StockX/GOAT prices need a separately verified source step before purchase decisions.
- Tiny full stock snapshot remains the catalog-level blocker for final commercial state.
