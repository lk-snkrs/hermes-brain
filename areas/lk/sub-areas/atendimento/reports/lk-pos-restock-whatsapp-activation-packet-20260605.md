# Approval packet — Religar LK POS restock WhatsApp

Data UTC: 2026-06-05T15:46:53Z
Responsável: LK Ops / Atendimento
Escopo executado até aqui: read-only/local + POST local seguro não-POS; sem envio WhatsApp real, sem Notion card, sem alteração Shopify/Tiny/Vercel/gateway.

## Objetivo

Reativar com segurança a função: venda POS/loja física na Shopify (`orders/paid`) gera alerta interno no grupo WhatsApp `[LK] Team` perguntando se deseja repor/recomprar o item vendido. Resposta `sim` cria card interno Notion `[LK] Encomenda`; resposta `não` encerra. O fluxo não compra, não reserva, não avisa fornecedor, não altera estoque/preço/Shopify/Tiny.

## Situação revalidada agora

### OK local/gateway

- Scripts locais compilam e teste passa:
  - `python3 -m py_compile /opt/data/scripts/lk_store_sale_restock_alert.py /opt/data/scripts/lk_hermes_whatsapp_responder.py`
  - `python3 /opt/data/scripts/tests/test_lk_store_sale_restock_webhook.py` → `ok`.
- Webhook local responde saúde em `127.0.0.1:8644/health` → `200 {"status":"ok","platform":"webhook"}`.
- Rota dinâmica atual contém `lk-shopify-pos-restock`:
  - `events`: `orders/paid`
  - `kind`: `lk_shopify_pos_restock`
  - `script`: `/opt/data/scripts/lk_store_sale_restock_alert.py`
  - `deliver`: `log`
  - secret presente `[REDACTED]`, tamanho 64.
- POST local assinado com o segredo da rota e payload **não-POS** foi aceito e ignorado com segurança:
  - resposta: `{"status":"ignored","reason":"not_paid_active_pos_order","topic":"orders/paid","write_executed":false}`
  - não acionou WhatsApp/Notion.

### Ainda pendente/provável quebra externa

- State do fluxo POS restock continua antigo:
  - `/opt/data/hermes_bruno_ingest/local_sql/lk_store_sale_restock/state.json`
  - `last_webhook_at`: `2026-05-23T21:45:10.309564+00:00`.
- Diagnóstico anterior encontrou falha de assinatura no caminho público:
  - Vercel/proxy público retornando `invalid_shopify_signature` em probe seguro.
  - Upstream Hermes retornando `Invalid signature` quando chamado sem assinatura Hermes válida.
- Como a rota local agora existe e processa payload assinado, o próximo gargalo provável é **alinhamento de segredo/assinatura entre Shopify → Vercel proxy → Hermes Gateway** ou ausência de evento Shopify real recente chegando no proxy.

## Ações bloqueadas sem aprovação explícita

Não executar sem aprovação escopada:

- alterar env/secrets no Vercel;
- alterar webhook Shopify;
- reiniciar gateway/containers;
- alterar gateway runtime/código produtivo;
- enviar WhatsApp real de teste no `[LK] Team`;
- criar card Notion real;
- alterar Shopify/Tiny/estoque/preço.

## Plano de reativação proposto

### Fase 1 — Diagnóstico externo read-only/secret-safe

1. Inspecionar projeto Vercel `hermes-webhooks` apenas para confirmar presença de envs, sem imprimir valores:
   - `SHOPIFY_WEBHOOK_SECRET`
   - `HERMES_WEBHOOK_SECRET`
2. Confirmar qual segredo Shopify o webhook `orders/paid` usa atualmente e comparar apenas fingerprint não reversível/presença, nunca valor.
3. Confirmar se `https://hermes-webhooks.vercel.app/webhooks/lk-shopify-pos-restock` está recebendo eventos recentes ou só probes.

### Fase 2 — Correção mínima, se aprovada

1. Se `SHOPIFY_WEBHOOK_SECRET` do Vercel estiver desalinhado, atualizar somente esse env no projeto Vercel aprovado.
2. Se `HERMES_WEBHOOK_SECRET` do Vercel estiver desalinhado com o secret da rota Hermes, atualizar somente esse env.
3. Não alterar rota/script se o dispatch local continuar passando.
4. Evitar restart/container salvo se necessário para ativar config; se necessário, fazer snapshot + plano de rollback antes.

### Fase 3 — Testes controlados

1. Teste não-POS via Vercel com HMAC Shopify correto:
   - esperado: aceito pelo proxy, aceito pelo Hermes, ignorado como `not_paid_active_pos_order`, sem WhatsApp/Notion.
2. Teste POS sintético ou venda POS combinada:
   - esperado: alerta interno no `[LK] Team` para item vendido.
3. Teste de resposta controlada:
   - `não`: encerra sem Notion.
   - `sim`: cria card Notion `[LK] Encomenda` apenas se Lucas aprovar esse teste.

## Rollback

- Reverter env Vercel para snapshot anterior, se alterado.
- Remover/pausar webhook Shopify POS apenas se ele for alterado durante a intervenção.
- Restaurar backup de config/rota caso haja alteração local.
- Manter responder WhatsApp normal rodando.

## Critério de aceite

- Evento não-POS via Vercel é ignorado com `write_executed:false`.
- Evento POS válido gera apenas alerta interno aprovado no grupo `[LK] Team`.
- State `last_webhook_at` atualiza com evento de teste.
- Não há writes em Shopify/Tiny/estoque/preço.
- Card Notion só é criado após resposta `sim` no teste aprovado.

## Aprovação necessária

Frase segura sugerida:

> Aprovo religar LK POS restock no escopo deste packet: diagnosticar secrets Vercel/Shopify/Hermes sem imprimir valores, corrigir somente envs desalinhados do proxy `hermes-webhooks` se necessário, testar primeiro payload não-POS sem WhatsApp/Notion, depois teste POS controlado no `[LK] Team`; sem alterar Shopify/Tiny/estoque/preço, sem fornecedor/cliente, e com rollback registrado.
