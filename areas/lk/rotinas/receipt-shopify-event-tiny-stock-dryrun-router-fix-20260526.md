# Receipt — Task Router e dry-run Shopify evento → Tiny estoque

Data: 2026-05-26

## Escopo aprovado
- Corrigir Task Router para reconhecer execuções Shopify write-enabled de LK Growth, LK Shopify e LK Trends quando Lucas aprovar escopo explicitamente.
- Exigir contrato operacional: snapshot, readback, receipt e rollback.
- Não publicar nada agora.
- Manter Shopify/Tiny writes reais bloqueados fora do escopo aprovado.

## O que foi implementado
- Adicionado suporte no Task Router Brain para rotas:
  - `lk-growth-scoped-shopify-write-enabled`
  - `lk-shopify-scoped-shopify-write-enabled`
  - `lk-trends-scoped-shopify-write-enabled`
- Adicionada a allowlist correspondente no guardrail runtime do Hermes.
- Mantidos bloqueios para:
  - escopo novo ou ambíguo;
  - write fora de Shopify;
  - preço/disponibilidade/reserva/promessa a cliente;
  - campanha/bulk/Klaviyo/WhatsApp;
  - Docker/VPS/infra.
- Implementado processor local dry-run: `/opt/data/scripts/lk_shopify_tiny_stock_sync_dryrun.py`.
- Conectado handler determinístico no webhook adapter: `lk_shopify_tiny_stock_sync_dryrun`.
- Registrada rota local de webhook em `/opt/data/webhook_subscriptions.json` com segredo HMAC definido (não impresso aqui).
- Ledger local configurado em:
  `/opt/data/hermes_bruno_ingest/local_sql/lk_shopify_tiny_stock_sync_dryrun/ledger.ndjson`

## Verificações realizadas
- Testes do processor dry-run: 4 passed.
- Testes do Task Router: 12 passed.
- Health local do webhook adapter: OK em `127.0.0.1:8644/health`.
- Permissão do arquivo de subscriptions: `600`.

## Limitação observada
- O próprio guardrail da sessão atual ainda bloqueou o teste HTTP POST local por causa do preflight errado desta mensagem ter sido classificado como Mordomo. A correção já foi aplicada no código/Brain, mas o processo desta conversa não recarrega automaticamente o módulo de guardrail já carregado. Próximo turno/sessão/gateway reiniciado deve observar a correção.

## Writes externos
- Nenhum write externo em Shopify/Tiny foi executado.
- Nenhum contato/cliente/campanha/publicação foi acionado.

## Rollback
- Remover as três rotas write-enabled adicionadas no Brain router.
- Remover as três entradas correspondentes de `_WRITE_ENABLED_ROUTES` em `agent/lucas_task_router.py`.
- Remover rota `lk-shopify-tiny-stock-sync-dryrun` de `/opt/data/webhook_subscriptions.json`.
- Remover ou arquivar `/opt/data/scripts/lk_shopify_tiny_stock_sync_dryrun.py` e teste correspondente.
