# Diagnóstico — LK POS restock WhatsApp desligado

Data: 2026-06-05
Escopo: read-only/local + probes seguros não-POS; sem envio WhatsApp real, sem Notion card, sem writes Shopify/Tiny/Vercel/gateway.

## Função recuperada da memória

A função criada em maio/2026 é: quando há venda em loja física/POS na Shopify, Hermes deve perguntar no grupo `[LK] Team` se quer repor/recomprar o item vendido. O fluxo aprovado é 1/N por item vendido:

- entrada por webhook Shopify, não polling;
- filtrar pedido pago, não cancelado, de POS (`source_name=pos` ou app POS);
- enviar alerta interno no WhatsApp `[LK] Team` com produto/SKU/tamanho/quantidade/pedido;
- aceitar `sim`/`não` no grupo;
- `sim` cria card interno Notion `[LK] Encomenda` com título `[LOJA ESTOQUE] Nome - SKU - Tamanho`;
- não compra, não reserva, não avisa fornecedor, não altera Shopify/Tiny/estoque/preço.

Arquivos principais:

- `/opt/data/scripts/lk_store_sale_restock_alert.py`
- `/opt/data/scripts/lk_hermes_whatsapp_responder.py`
- `/opt/data/scripts/tests/test_lk_store_sale_restock_webhook.py`

Docs/memória:

- `areas/lk/rotinas/lk-pos-sale-restock-whatsapp-notion-2026-05-23.md`
- `areas/lk/rotinas/lk-pos-restock-public-webhook-2026-05-23.md`

## Evidência atual

### OK

- Script local compila e teste de restock passa: `python3 -m py_compile ... && python3 /opt/data/scripts/tests/test_lk_store_sale_restock_webhook.py` → `ok`.
- Responder WhatsApp está rodando: `python3 /opt/data/scripts/lk_hermes_whatsapp_responder.py --port 8787`.
- `wacli --account hermes auth status --json` retorna `authenticated:true` para o número Hermes.
- `wacli --account hermes sync --follow ... --webhook http://127.0.0.1:8787/wacli` está rodando.
- Webhook platform local está saudável: `GET http://127.0.0.1:8644/health` → `200`.
- Rota local `/webhooks/lk-shopify-pos-restock` existe pelo menos como rota HTTP: GET retorna `405 Method Not Allowed`.
- Shopify Admin tem webhook `orders/paid` apontando para `https://hermes-webhooks.vercel.app/webhooks/lk-shopify-pos-restock`.

### Quebra observada

- State de POS restock não mostra processamento recente: `/opt/data/hermes_bruno_ingest/local_sql/lk_store_sale_restock/state.json` tem `last_webhook_at` em `2026-05-23T21:45:10.309564+00:00`.
- Probe público seguro não-POS assinado com o segredo local disponível retornou `401 invalid_shopify_signature` em `https://hermes-webhooks.vercel.app/webhooks/lk-shopify-pos-restock`.
- Probe direto no upstream `https://crisp-hooks.srv1331756.hstgr.cloud/webhooks/lk-shopify-pos-restock` com header Shopify também retornou `401 Invalid signature`.
- Logs atuais registram `Invalid signature for route lk-shopify-pos-restock` nos probes de 2026-06-05.
- A versão ativa do gateway (`/opt/data/hermes-0.15.1-venv/.../gateway/platforms/webhook.py`) tem processador determinístico especial apenas para `kind=lk_shopify_tiny_stock_sync_dryrun`; não há dispatch determinístico para `kind=lk_shopify_pos_restock` chamando `/opt/data/scripts/lk_store_sale_restock_alert.py`.

## Diagnóstico provável

A função não está “desligada” porque o responder WhatsApp caiu; o responder e a conta Hermes estão vivos.

O ponto quebrado está no caminho Shopify → proxy/Vercel → Hermes Gateway → processor POS:

1. O webhook Shopify ainda aponta para o endpoint público antigo `hermes-webhooks.vercel.app`.
2. A validação de assinatura no proxy/gateway não está alinhada com o segredo efetivo (`invalid_shopify_signature` / `Invalid signature`).
3. Mesmo corrigindo a assinatura, a rota `lk_shopify_pos_restock` precisa ser ligada ao processor determinístico POS; a versão ativa do gateway hoje não chama diretamente `lk_store_sale_restock_alert.py` para esse kind.

## Plano seguro para religar

Requer aprovação explícita porque envolve Vercel/env/gateway/webhook/possível WhatsApp interno/Notion:

1. Alinhar segredo sem expor valor:
   - verificar envs `SHOPIFY_WEBHOOK_SECRET` e `HERMES_WEBHOOK_SECRET` do projeto Vercel `hermes-webhooks`;
   - comparar fingerprint não reversível com o segredo efetivo do gateway/Shopify;
   - corrigir somente se necessário.
2. Implementar/ativar dispatch determinístico para `kind=lk_shopify_pos_restock` no gateway ativo:
   - validar Shopify HMAC ou aceitar apenas chamada reassinada pelo proxy, conforme desenho final escolhido;
   - chamar `process_shopify_order_webhook(raw_payload, delivery_id, topic)` de `/opt/data/scripts/lk_store_sale_restock_alert.py`;
   - manter filtros POS/pago/não cancelado e dedupe;
   - retorno sanitizado.
3. Testar sem efeito externo:
   - POST seguro não-POS assinado → `ignored/not_paid_active_pos_order`, sem WhatsApp/Notion;
   - teste offline multi-item → fila 1/N correta.
4. Teste real controlado somente após aprovação:
   - usar payload POS sintético ou venda POS real combinada;
   - enviar no `[LK] Team` apenas se o evento passar nos filtros;
   - `sim` cria card Notion; `não` só avança/encerra.
5. Rollback:
   - restaurar backup do arquivo gateway/config;
   - remover/pausar webhook Shopify POS se necessário;
   - deixar responder WhatsApp rodando para consultas normais.

## Aprovação sugerida

“Aprovo religar LK POS restock: alinhar secrets Vercel/Hermes e ativar dispatch determinístico da rota `lk-shopify-pos-restock` para o processor local, com testes não-POS primeiro, sem alterar Shopify/Tiny/estoque/preço, sem contato fornecedor/cliente, e com WhatsApp interno/Notion apenas no fluxo já aprovado de reposição.”
