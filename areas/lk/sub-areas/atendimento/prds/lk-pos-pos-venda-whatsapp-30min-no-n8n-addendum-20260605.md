# Addendum — Pós-venda POS 30min sem n8n

Data: 2026-06-05
Área: LK Ops / Atendimento
Status: rascunho técnico, sem execução externa

## Decisão de Lucas

Lucas confirmou que **não quer usar n8n** para o fluxo de pós-venda POS 30min.

Direção: reaproveitar webhook/ingress Shopify já existente para novas vendas e transformar isso em uma rotina Hermes/Recovery/Event Hub, sem criar dependência nova no n8n.

## Evidência consultada

### Brain / Recovery OS

Arquivo consultado:

- `areas/lk/sub-areas/atendimento/receipts/lk-recovery-os-shopify-webhooks-20260603-0039z.md`

Evidência:

- Recovery OS já possui webhook Shopify `orders/create`:
  - `https://recovery.lucascimino.com/shopify/orders/create`
  - criado em 2026-06-02
  - objetivo: lifecycle capture/persistence
  - envios ao cliente permanecem desabilitados
- Também possui:
  - `checkouts/create`
  - `checkouts/update`

### Shopify read-only em 2026-06-05

Webhooks relevantes encontrados:

- `orders/paid` → `https://hermes-webhooks.vercel.app/webhooks/lk-shopify-pos-restock`
- `orders/paid` → `https://lucascimino.com/webhook/shopify`
- `orders/create` → `https://lucascimino.com/webhook/shopify`
- `orders/paid` → `https://crisp-hooks.srv1331756.hstgr.cloud/webhooks/lk-shopify-tiny-stock-sync`
- `orders/create` → `https://recovery.lucascimino.com/shopify/orders/create`

### Hermes local

Config atual contém rota Hermes:

- route: `lk-shopify-pos-restock`
- kind: `lk_shopify_pos_restock`
- event: `orders/paid`
- script: `/opt/data/scripts/lk_store_sale_restock_alert.py`

Essa rota já processa venda POS paga e não cancelada, filtra `source_name == pos` ou `app_id == 129785`, e dispara alerta interno de recompra para o grupo.

## Interpretação

Há pelo menos três superfícies de evento de venda Shopify que podem ser reaproveitadas, sem n8n:

1. **Recovery OS `orders/create`**
   - Melhor como Event Hub geral de lifecycle/CRM.
   - Já documentado no Brain como ponto de ingestão de novas vendas.

2. **Hermes POS restock `orders/paid`**
   - Já é usado especificamente para venda POS/recompra interna.
   - Bom candidato para derivar/emitir também um job de pós-venda POS 30min.

3. **Legacy `lucascimino.com/webhook/shopify`**
   - Existe para `orders/create` e `orders/paid`, mas Brain marca como legacy/non-Recovery e recomenda não tocar sem aprovação separada.

## Arquitetura recomendada sem n8n

```text
Shopify orders/paid ou orders/create
  ↓
Webhook existente Hermes/Recovery
  ↓
Validação HMAC Shopify
  ↓
Event router LK
  ↓
Filtro POS + pago/não cancelado
  ↓
Extrai customer/telefone + tag vendedor:
  ↓
Cria job local delayed_send_at = compra + 30min
  ↓
Scheduler Hermes/worker local processa jobs vencidos
  ↓
Renderiza template aprovado
  ↓
Envia via canal aprovado
  ↓
Ledger/receipt + dedupe
```

## Decisão técnica recomendada

### Preferência: usar `orders/paid`

Para pós-venda 30min, o evento mais seguro é `orders/paid`, porque evita enviar agradecimento para pedido POS criado mas não pago.

Superfície disponível:

- `https://hermes-webhooks.vercel.app/webhooks/lk-shopify-pos-restock`
- route Hermes: `lk-shopify-pos-restock`
- script atual: `/opt/data/scripts/lk_store_sale_restock_alert.py`

Implementação sugerida:

- manter alerta interno de recompra como está;
- adicionar um segundo efeito local/seguro no processor: `enqueue_pos_thankyou_job(order)`;
- esse enqueue não envia nada imediatamente;
- scheduler separado envia só após 30 minutos, com dedupe/kill switch.

### Alternativa: usar Recovery OS `orders/create`

Bom se a visão for centralizar todos os lifecycle events no Recovery OS.

Mas, para pós-venda POS, precisaria revalidar pagamento após delay ou também receber `orders/paid`, para não enviar indevidamente.

## Parser de vendedor recomendado

O n8n usava:

```js
/Vendedor:\s*(.+?)(?:,|$)/
```

Para Hermes, usar regex mais robusta:

```js
/vendedor:\s*([^,]+)/i
```

Regras:

- aceitar `Vendedor: Bruno`, `vendedor:Bruno`, `VENDEDOR: Bruno`;
- usar primeiro nome na mensagem;
- se vendedor ausente, usar fallback `equipe da LK Sneakers`.

## Template base aprovado como referência

```text
Oi {cliente_nome}, tudo bem? Aqui é o {vendedor_nome}, da LK.

Queria te agradecer pessoalmente pela compra e pela confiança. Receber você na nossa loja foi um prazer!

Estamos à disposição para o que precisar. Fico em contato!

Obrigado e abraços,
{vendedor_nome}
```

Fallbacks:

- sem cliente, começa com `Oi, tudo bem?`
- sem vendedor, remetente vira `a equipe da LK Sneakers`
- assinatura fallback: `Um abraço.`

## Dedupe / state

Obrigatório:

- dedupe por `order_id` + tipo `pos_thankyou_30min`;
- registrar `shopify_delivery_id` quando disponível;
- estado local/SQLite em path dedicado;
- status:
  - `received`
  - `ignored_not_pos`
  - `ignored_not_paid`
  - `missing_phone`
  - `scheduled`
  - `sent`
  - `duplicate`
  - `failed_needs_human`
  - `killed_by_switch`

## Guardrails

- Sem n8n.
- Sem criar novo webhook Shopify se for possível reaproveitar evento existente.
- Sem envio WhatsApp até aprovação explícita de canal/remetente/copy/canary.
- Sem prometer desconto, troca, prazo, estoque, reserva ou disponibilidade.
- Tiny continua fonte de estoque, mas este fluxo não promete estoque.
- `lucascimino.com/webhook/shopify` é legado; não tocar sem aprovação específica.

## Próximo approval packet recomendado

Para implementação segura:

> Aprovo implementar em modo dry-run/local o pós-venda POS 30min sem n8n, reaproveitando o webhook Hermes/Recovery de venda Shopify existente, sem envio WhatsApp real, sem alterar Shopify/Tiny/Chatwoot/n8n, apenas criando fila local/dedupe/preview de mensagem e receipts no Brain.

Depois do dry-run:

> Aprovo canary de envio WhatsApp para 1 pedido POS controlado, usando conta/remetente X e template Y, com kill switch e sem campanha em massa.
