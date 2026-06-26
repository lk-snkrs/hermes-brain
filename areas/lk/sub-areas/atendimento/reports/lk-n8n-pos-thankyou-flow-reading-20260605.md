# Leitura read-only — n8n workflow `LK POS → WhatsApp Thank You`

Data: 2026-06-05
Área: LK Ops / Atendimento
Status: leitura read-only, sem alteração no n8n
Workflow: `VLOygUcX6xbQYQif`
URL: `https://n8n.lucascimino.com/workflow/VLOygUcX6xbQYQif`

## Resultado

Foi possível acessar o workflow via API interna do n8n no VPS, de forma read-only, usando credencial n8n existente em Doppler. Nenhum node/workflow foi alterado.

## Identidade do workflow

- ID: `VLOygUcX6xbQYQif`
- Nome: `LK POS → WhatsApp Thank You`
- Active: `true`
- Created at: `2026-05-04T23:02:49.776Z`
- Updated at: `2026-05-20T14:41:46.943Z`
- Node count: `15`

## Fluxo aprendido

1. `POS Order Received`
   - Webhook POST
   - Path: `lk-pos-thankyou`
2. `Validate HMAC`
   - HMAC real desabilitado no code node.
   - Valida apenas presença de sinal Shopify: HMAC header, topic Shopify ou user-agent Shopify.
3. `Is POS Order?`
   - Filtro POS.
4. `Dedup Check`
   - Usa workflow static data global.
   - Dedup por `order.body.id`.
   - Limpeza de histórico após 7 dias.
5. `Extract & Format Phone`
   - Usa `order.customer.phone` ou `order.billing_address.phone`.
   - Normaliza telefone BR para `55...`.
   - Exige 13 dígitos e celular com nono dígito.
6. `Has Valid Phone?`
7. `30 Min Delay`
   - Wait node: 30 minutos.
8. `Check Time SP`
   - Janela de envio São Paulo: 09h–22h.
9. `Is Daytime?`
10. `Calc Wait Until 9AM`
    - Se fora da janela, calcula espera até 09h.
11. `Wait Until Morning`
12. `Build Message`
    - Usa `order.customer.first_name`.
    - Extrai vendedor por regex `/Vendedor:\s*(.+?)(?:,|$)/`.
    - Monta mensagem de agradecimento.
13. `Send WhatsApp`
    - HTTP POST para Evolution API.
14. `Extract Order Data`
    - Extrai dados do pedido, cliente, vendedor, itens, mensagem enviada e resposta Evolution.
15. `Log to Supabase`
    - HTTP POST para Supabase.

## Execuções recentes vistas

Últimas execuções retornadas pela API eram success/webhook, principalmente em 2026-05-26 e última em 2026-05-27T00:33:37Z. Não havia execução recente no momento da leitura.

## Leitura Shopify webhooks

Também foi feita leitura read-only dos webhooks Shopify relevantes (`orders/paid` e `orders/create`). Não encontrei webhook Shopify apontando para o path n8n `lk-pos-thankyou`.

Webhooks relevantes encontrados:

- `orders/paid` → `https://hermes-webhooks.vercel.app/webhooks/lk-shopify-pos-restock`
- `orders/paid` → `https://lucascimino.com/webhook/shopify`
- `orders/create` → `https://lucascimino.com/webhook/shopify`
- `orders/paid` → `https://crisp-hooks.srv1331756.hstgr.cloud/webhooks/lk-shopify-tiny-stock-sync`
- `orders/create` → `https://recovery.lucascimino.com/shopify/orders/create`

## Pontos de atenção

1. O workflow está marcado como `active: true`, mas as últimas execuções vistas são de 26/05–27/05.
2. A causa mais provável de não disparar hoje: **Shopify não está mais chamando o webhook n8n `lk-pos-thankyou`**.
3. Outras possíveis causas secundárias:
   - eventos POS não estão chegando nesse endpoint;
   - filtro `Is POS Order?` está ignorando payloads novos;
   - telefone inválido/ausente causa saída silenciosa;
   - dedupe staticData já marcou algum order_id, mas isso só afetaria duplicados.
4. O code pasted por Lucas está correto na versão real do n8n porque usa template literals com crase. A cópia no Telegram perdeu crases em alguns trechos.
5. Regex atual é case-sensitive para `Vendedor:`. Para robustez, recomendar `/vendedor:\s*([^,]+)/i`.
6. HMAC real está desabilitado no node `Validate HMAC`, o que é um risco operacional se o endpoint for público.
7. Dedupe em static data global é simples, mas pode ser frágil para auditoria; melhor persistir em DB/local state para projeto Hermes.
8. Log to Supabase pode falhar se Supabase estiver instável; se falhar após envio, pode registrar execução como erro apesar de mensagem já ter sido enviada.

## Recomendação técnica

Para religar/validar com segurança:

1. Confirmar webhook Shopify ativo apontando para `/webhook/lk-pos-thankyou` no n8n.
2. Rodar teste dry-run/controlado com payload POS real anonimizável antes de envio externo.
3. Ajustar regex de vendedor para case-insensitive e compatível com `vendedor:nome`.
4. Revisar node `Is POS Order?` para aceitar `source_name == pos` e/ou `app_id == 129785`.
5. Reativar HMAC real ou mover o gatilho para o padrão Vercel/Hermes já validado.
6. Decidir se este fluxo permanece no n8n ou se será migrado para Hermes scheduler com receipts no Brain.

## Sem alterações realizadas

- Não ativei/desativei workflow.
- Não editei nodes.
- Não enviei WhatsApp.
- Não alterei Shopify, Supabase ou Evolution API.
