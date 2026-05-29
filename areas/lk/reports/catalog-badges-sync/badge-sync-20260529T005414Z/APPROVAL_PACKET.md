# Approval Packet — LK Catalog Badges NEW + BEST SELLER

Data: 2026-05-29T00:54:14Z
Modo executado: preview/dry-run, sem write Shopify

## Evidência
- Menu usado: `main-menu`
- Coleções alvo: 48 coleções do menu principal
- Produtos escaneados: 2316
- Produtos com mudança planejada de tag: 485
- GA4: disponível, propriedade `348553567`, 2421 linhas de pagePath de produto lidas
- Shopify vendas: 1022 pedidos válidos pagos/capturados considerados; expurgados pending/cancelled/refunded/partially_refunded
- Snapshot/rollback: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/reports/catalog-badges-sync/badge-sync-20260529T005414Z/rollback-snapshot.json`
- Preview completo: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/reports/catalog-badges-sync/badge-sync-20260529T005414Z/REPORT.md`

## Regra
- `NEW`: produto criado nos últimos 90 dias recebe tag `new`; produtos fora da janela perdem `new` se era tag gerenciada.
- `BEST SELLER`: Top 8 por coleção do menu principal com score híbrido 70% Shopify vendas líquidas/capturadas + 30% GA4 page views.
- Tag contextual: `best-seller--<collection_handle>`.
- Tags genéricas antigas `best-seller`/`bestseller` são removidas pelo sync para evitar badge fora de contexto.

## Resumo das mudanças planejadas
- `new` adicionada: 188 produtos
- `new` removida: 1 produto
- tags contextuais `best-seller--...` adicionadas: 358 ocorrências
- tags genéricas `best-seller`/`bestseller` removidas: 50 ocorrências
- total de produtos alterados: 485

## Exemplo — coleção Pace
Top 8 que receberá `best-seller--pace`:
1. Calça Pace Nomo Tailoring Trousers Preto — score 0.71309 — 2 unidades — R$ 2199.98 — 279 views
2. Camiseta Pace Buero Washed Black Preto — score 0.708704 — 3 unidades — R$ 927.97 — 163 views
3. Camiseta Pace Principles Off White — score 0.683102 — 2 unidades — R$ 416.14 — 445 views
4. Calça Pace Milli Cargo Azul Marinho — score 0.593339 — 2 unidades — R$ 1228.48 — 216 views
5. Calça Pace PF SweatPants Preto — score 0.534151 — 2 unidades — R$ 797.99 — 179 views
6. Camiseta Manga Longa Pace Relaxed Waffle Knit Preto — score 0.524307 — 2 unidades — R$ 419.98 — 209 views
7. Jaqueta Pace Signature Hooded Preto — score 0.51037 — 1 unidade — R$ 665.00 — 419 views
8. Regata Pace Waffle Knit Off White — score 0.49295 — 2 unidades — R$ 313.94 — 175 views

## Risco
- Aplicação de tags é write externo em Shopify Product tags.
- Badge contextual só fica correto visualmente quando o Liquid atualizado estiver no tema em uso.
- Upload de Liquid para tema Shopify é outro write externo e precisa aprovação separada se for dev/prod theme.

## Rollback
- Restaurar tags anteriores usando `rollback-snapshot.json`, campo `changed_products[].current_tags` por product id.
- Nenhum write foi executado neste preview.

## Aprovação necessária
Para aplicar somente as tags nos produtos Shopify, responder exatamente:

`aprovado aplicar tags NEW e BEST SELLER no catálogo Shopify conforme preview 20260529T005414Z`

Para além disso subir o Liquid para um tema Shopify, preciso de aprovação separada indicando o destino:
- `dev theme` para preview seguro; ou
- `production theme` se quiser ir direto para live.
