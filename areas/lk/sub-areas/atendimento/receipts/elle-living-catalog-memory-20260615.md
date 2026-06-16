# Receipt — Elle memória viva de catálogo sem estoque

- Data/hora UTC: 2026-06-15T16:29Z
- Área: LK / Atendimento / Elle / Chatwoot
- Solicitação Lucas: criar “memória viva” para produtos/coleções da LK, sem transformar estoque em conhecimento fixo da IA.

## O que foi criado

Camada local de catálogo vivo para Elle:

- Cache persistente: `/data/catalog_cache.json` dentro do container, montado em `/opt/elle-chatwoot/data/catalog_cache.json` no host.
- Fonte read-only pública:
  - `https://lksneakers.com.br/products.json`
  - `https://lksneakers.com.br/collections.json`
- Campos salvos:
  - tipo (`product`/`collection`);
  - título;
  - handle;
  - URL;
  - vendor/marca quando existir;
  - product_type;
  - tags;
  - resumo curto limpo do HTML;
  - texto normalizado para busca.
- Campos propositalmente excluídos:
  - estoque;
  - inventário;
  - disponibilidade;
  - quantidade;
  - preço como fonte decisória.

## Comportamento

- A Elle usa o cache para responder perguntas de catálogo, marca, produto e coleção com link verificado.
- Se o cache existir e ficar velho, a Elle usa o cache atual e atualiza em background.
- Se o cache não existir, a Elle sincroniza a primeira vez.
- TTL configurável: `ELLE_CATALOG_TTL_SECONDS`, default 6h.
- Fallback preservado: se a memória viva não encontra resultado, ainda tenta o `search/suggest.json` do site.
- Health agora expõe status sanitizado do catálogo:
  - `catalog_cache_present`;
  - `catalog_products_count`;
  - `catalog_collections_count`;
  - `catalog_age_seconds`;
  - `catalog_stock_included`.

## Regra de estoque preservada

A memória viva **não** responde estoque/pronta entrega/tamanho disponível/loja física/reserva.

Esses casos continuam sendo:

- `category=stock_handoff`;
- `handoff=true`;
- transbordo para Larissa/lk-stock;
- sem link de produto usado como promessa de disponibilidade.

## Ajustes de copy

- Coleção/marca: `Sim, trabalhamos com <coleção>. Segue o link da coleção: <url>`.
- Produto: `Encontrei esse produto no nosso site: <título> — <url>. Você pode abrir a página para ver os detalhes e seguir a compra por lá.`
- Evita prometer pronta entrega, disponibilidade, grade, reserva ou preço.

## Verificação local antes do deploy

- `python3 -m py_compile app.py`: OK.
- Sync local/smoke:
  - `products_count=1802`;
  - `collections_count=180`;
  - `stock_included=false`.
- Busca:
  - `lululemon` → collection `Lululemon`, `/collections/lululemon`;
  - `Salomon XT-6 Vanilla Ice` → product `Tênis Salomon XT-6 Vanilla Ice Oxford Tan Bege Bege`;
  - query nonsense com termo solto não gera falso positivo.
- Classificador:
  - `Vocês vendem Lululemon?` → `product_clear`, sem handoff, link coleção;
  - `Vocês têm Salomon XT-6 Vanilla Ice?` → `product_clear`, sem handoff, link produto;
  - `Vocês têm pronta entrega o Salomon XT-6 Vanilla Ice tamanho 39?` → `stock_handoff`, `handoff=true`, sem link produto na resposta.

## Deploy e verificação em produção

- Container `elle-chatwoot` rebuildado e recriado.
- Cache pré-aquecido dentro do container.
- Smoke runtime:
  - `products_count=1802`;
  - `collections_count=180`;
  - `stock_included=false`;
  - `lululemon_ok=true`;
  - `salomon_product_ok=true`;
  - `pronta_entrega_handoff_ok=true`.
- Health público:
  - `ok=true`;
  - `write_enabled=true`;
  - `kill_switch=false`;
  - `public_reply_enabled=true`;
  - `ai_enabled=true`;
  - `ai_model=google/gemini-2.5-flash`;
  - `ai_secret_present=true`;
  - `debounce_enabled=true`;
  - `debounce_seconds=15.0`;
  - `catalog_cache_present=true`;
  - `catalog_products_count=1802`;
  - `catalog_collections_count=180`;
  - `catalog_stock_included=false`.

## Rollback

- Backup app.py: `/opt/elle-chatwoot/backups/lucas-living-catalog-20260615T162416Z/app.py`.
- Para rollback: restaurar backup, `python3 -m py_compile app.py`, rebuild/recreate `elle-chatwoot`.
- Cache `/opt/elle-chatwoot/data/catalog_cache.json` pode ser removido sem afetar estoque ou pedidos.

## Segurança

- Não foi consultado Tiny.
- Não foi consultado/alterado estoque.
- Não houve alteração Shopify/Tiny.
- Única fonte externa lida foi catálogo público do site/Shopify.
- Sem impressão de tokens, secrets, PII ou dados de cliente.
