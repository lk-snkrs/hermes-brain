# LK-TRENDS — KicksDev market intelligence contract

Data: 2026-05-26
Status: base local/read-only para cron de tendência; sem cron ativo ainda.

## Correção de arquitetura

KicksDev/KicksDB deve ser a fonte primária programática do LK-TRENDS para dados de StockX e GOAT.

O radar não deve depender de snippets de Google quando a API estiver disponível. Snippets continuam permitidos apenas como fallback ou sanity-check.

## Por que KicksDev entra no centro

- API unificada para StockX, GOAT, Flight Club e lojas Shopify suportadas.
- Busca por SKU, nome, slug e identificadores.
- Dados estruturados de produto: marca, modelo, colorway, SKU, slug, rank, weekly_orders, preço médio/mín/máx, variantes e imagens.
- Histórico de vendas StockX e GOAT, incluindo endpoints diários agregados.
- Evita scraping direto de StockX/GOAT.
- Permite rotina rápida e repetível para cron.

## Endpoints documentados relevantes

Base: `https://api.kicks.dev`
Autenticação: header `Authorization: Bearer <TOKEN_KICKSDEV>`
Secret aceito no runtime: `KICKS_DEV_API_KEY`, `KICKS_API_KEY` ou `KICKSDB_API_KEY`.
Nunca imprimir o valor do secret.

### StockX

- Buscar produto:
  - `GET /v3/stockx/products?query=<sku_ou_nome>`
- Obter produto por id/slug:
  - `GET /v3/stockx/products/<id_or_slug>`
- Histórico de vendas:
  - `GET /v3/stockx/products/<id_or_slug>/sales`
- Histórico diário agregado:
  - `GET /v3/stockx/products/<id_or_slug>/sales/daily`

### GOAT

- Buscar produto:
  - `GET /v3/goat/products?query=<sku_ou_nome>`
- Obter produto por id/slug:
  - `GET /v3/goat/products/<id_or_slug>`
- Histórico de vendas:
  - `GET /v3/goat/products/<id>/sales`
- Histórico diário agregado:
  - `GET /v3/goat/products/<id>/sales/daily`

### Unified API

- Cruzar múltiplas plataformas por SKU/ID/slug:
  - `GET /v3/unified/products/<identifier>`

## Campos que o cron deve usar

### Identidade

- title/name
- brand
- model
- gender
- sku
- slug
- product_type
- category
- colorway/secondary_title
- release_date quando existir
- source platform

### Liquidez

- weekly_orders
- sales daily orders 7d / 30d / 90d
- total de vendas por janela
- média de preço por janela
- rank, quando disponível

### Preço e assimetria

- min_price
- max_price
- avg_price
- lowest_ask por variante
- highest_bid quando disponível
- retail_price quando disponível
- moeda e mercado
- estimativa LK import: `(USD + custo_trazer) * (FX * 1.05)`
- ideal mínimo LK: `custo * 2`, salvo decisão manual

### Variantes e tamanho

- variant_id
- size US Men/US Women
- lowest_ask
- availability
- conversion_status para LK/BR/EU

## Régua para decisão

### Colorway/modelo vira candidato de sourcing apenas se tiver

- 150+ vendas/90d em StockX/GOAT; ou
- 15%+ da líder da família/modelo; ou
- 50+ vendas/90d com preço assimétrico forte; ou
- collab forte com escassez real; ou
- pedido/fit BR comprovado.

### Watchlist

- 50–149 vendas/90d sem gap claro;
- 5%–15% da líder;
- collab promissora mas sem validação BR;
- volume alto fora, mas LK já tem cobertura boa.

### Ignorar

- abaixo de 50 vendas/90d e sem collab/assimetria;
- colorway ausente, mas com liquidez irrelevante contra a líder;
- modelo genericamente hypado mas sobrando no retail;
- produto com histórico ruim para LK/Brasil, salvo exceção validada.

## Pipeline do cron LK-TRENDS

1. Entrada de seeds:
   - modelos manuais aprovados por Lucas;
   - termos de busca BR em aceleração;
   - lançamentos editoriais relevantes;
   - fila de watchlist anterior;
   - produtos LK com coleção ativa.
2. Resolver identidade por KicksDev:
   - StockX search;
   - GOAT search;
   - Unified API por SKU/slug quando houver.
3. Calcular liquidez:
   - weekly_orders;
   - vendas diárias 7/30/90d;
   - comparar contra líder da família.
4. Cruzar Brasil:
   - Google Ads/DataForSEO;
   - Droper/retail BR;
   - sinal de retail sobrando ou escassez.
5. Cruzar LK:
   - coleção/PDP pública e, quando permitido, dados read-only internos;
   - LK tem/não tem;
   - gap real apenas se o volume for material.
6. Classificar:
   - Sourcing para Júlio;
   - Watchlist;
   - Catálogo-preview;
   - Conteúdo/PDP downstream;
   - Ignorar.
7. Emitir relatório:
   - Markdown/HTML local;
   - fila JSON de oportunidades;
   - zero ação externa sem aprovação.

## Guardrails

Permitido sem aprovação:

- chamadas read-only KicksDev;
- pesquisa read-only;
- geração de relatórios locais;
- documentação Brain;
- preview de pacote Júlio.

Bloqueado sem aprovação atual:

- contato com fornecedor/Júlio;
- compra/reserva/negociação;
- criação/edição Shopify/Tiny/Merchant/Klaviyo/ads;
- publicação de conteúdo;
- promessa de preço, estoque, prazo ou disponibilidade.

## Implementação local

Script base:

- `scripts/lk_trends_kicksdev_market_probe_20260526.py`

Saídas padrão:

- `areas/lk/sub-areas/trends/reports/kicksdev-probes/*.json`
- `areas/lk/sub-areas/trends/reports/kicksdev-probes/*.md`

O script é read-only, não imprime secrets e falha de forma segura se a chave não existir.
