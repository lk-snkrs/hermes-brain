# LK Shopify Event → Tiny Stock Truth Sync — PRD

Status: decisão operacional registrada; implementação/ativação bloqueada até aprovação explícita de writes.
Data: 2026-05-26.

## Decisão de Lucas

Shopify **não** deve ser controle de estoque da LK.

Shopify deve servir como gatilho/evento: quando houver venda ou cancelamento, o Hermes deve identificar exatamente o produto/variante vendido/cancelado, buscar o estoque verdadeiro no Tiny e então atualizar o estoque da variante correspondente no Shopify com o valor correto vindo do Tiny.

## Objetivo

Manter o estoque exibido/operado no Shopify alinhado ao Tiny após eventos de pedido, sem usar o estoque Shopify como fonte de verdade.

## Regra central

- Fonte de evento: Shopify.
- Fonte de estoque: Tiny, depósito `LK | CONTROLE ESTOQUE`.
- Fonte de identidade comercial do pedido: Shopify order/line item.
- Atualização permitida somente após resolver variante exata e ler Tiny com confiança alta.

## Eventos cobertos

V1 deve cobrir:

1. Venda/pedido pago
   - Tópicos candidatos: `orders/paid` e/ou evento interno equivalente já validado.
   - Ação: para cada line item, resolver Shopify variant → SKU/tamanho → Tiny produto/variação; ler estoque Tiny; atualizar estoque Shopify para o número oficial Tiny.

2. Cancelamento
   - Tópico candidato: `orders/cancelled`.
   - Ação: não “devolver” manualmente pelo payload. Apenas usar o evento como gatilho para consultar Tiny novamente e espelhar o saldo oficial no Shopify.

Eventos futuros:

- refund/partial refund;
- edição de pedido;
- troca/devolução;
- POS offline.

## Invariantes

1. Nunca calcular o novo saldo Shopify por `saldo atual Shopify - quantidade vendida`.
2. Nunca calcular cancelamento por `saldo atual Shopify + quantidade cancelada`.
3. Sempre consultar Tiny depois do evento.
4. Se Tiny falhar, rate-limit ou ambiguidade: não atualizar Shopify.
5. Se SKU/tamanho estiver ambíguo: não atualizar Shopify.
6. Se múltiplas variações Tiny baterem no mesmo SKU: não atualizar Shopify.
7. Se Shopify variant não tiver inventory item resolvido: não atualizar Shopify.
8. Toda execução deve ser idempotente por evento + line item + variant.

## Fluxo técnico proposto

### Entrada

Webhook Shopify assinado:

- `orders/paid` / venda;
- `orders/cancelled` / cancelamento.

Campos mínimos:

- order id;
- order name;
- event topic;
- event delivery id;
- line item id;
- product id;
- variant id;
- sku;
- title;
- variant title/tamanho;
- quantity.

### Resolução

Para cada line item:

1. Usar `variant_id` como chave primária Shopify.
2. Confirmar SKU e tamanho no Shopify Admin read-only se o payload estiver incompleto.
3. Resolver SKU canônico e tamanho.
4. Buscar no Tiny por SKU exato/código canônico.
5. Validar que a resposta Tiny é única, da variação correta e no depósito `LK | CONTROLE ESTOQUE`.
6. Extrair saldo oficial Tiny.
7. Preparar update Shopify InventoryLevel para a location correta.

### Update Shopify

Somente quando todos os gates passarem:

- escrever estoque Shopify da variante para o saldo Tiny;
- registrar receipt com before/after, fonte Tiny, variant id, inventory item id, location id, evento e idempotency key;
- não alterar preço, SKU, produto, tags, coleção, título, tema ou Tiny.

## Idempotência

Chave sugerida:

```text
shopify:{topic}:{delivery_id}:{order_id}:{line_item_id}:{variant_id}
```

Se `delivery_id` não existir, usar hash do raw body + tópico.

Manter ledger local:

- received_at;
- processed_at;
- status;
- topic;
- order id/name;
- line item id;
- variant id;
- sku;
- tiny id/código;
- tiny stock read;
- shopify inventory before;
- shopify inventory after;
- error/block reason.

## Gates de bloqueio

Bloquear e alertar sem write quando:

- Tiny API rate-limit/erro;
- SKU ausente;
- tamanho ausente quando necessário;
- SKU interno/número sem alias confiável;
- múltiplos candidatos Tiny;
- Tiny retorna sem saldo do depósito correto;
- Shopify variant/inventory item/location não resolvido;
- diferença muito grande e inesperada entre Shopify before e Tiny after;
- evento duplicado;
- evento de pedido não pago/não confirmado.

## Saída para Lucas

Silent-OK por padrão.

Notificar Telegram somente quando:

- bloqueio que exige correção SKU/Tiny;
- diferença grande/risco operacional;
- falha recorrente;
- aprovação necessária;
- resumo de ativação/rollback.

## Não escopo

- Não escrever no Tiny.
- Não alterar preço.
- Não alterar SKU.
- Não prometer disponibilidade a cliente.
- Não enviar WhatsApp/e-mail/campanha.
- Não comprar/reposicionar automaticamente.

## Aprovação necessária para ativar

A implementação real exige aprovação explícita porque envolve:

- webhook Shopify;
- write de estoque no Shopify;
- ledger operacional;
- possível gateway/webhook runtime.

Frase de aprovação recomendada:

> Aprovo implementar e ativar o sync Shopify evento → Tiny estoque → Shopify inventory, limitado a `orders/paid` e `orders/cancelled`, com Tiny como fonte única de estoque, idempotência, dry-run primeiro, rollback e sem writes em Tiny/preço/SKU/cliente.

## Sequência segura

1. Fase A — Dry-run local:
   - receber payloads/samples;
   - resolver produto/variant/SKU/tamanho;
   - consultar Tiny;
   - calcular o update proposto;
   - registrar ledger;
   - **não escrever Shopify**.

2. Fase B — Webhook read-only/dry-run:
   - criar rota/evento com validação HMAC;
   - processar eventos reais em dry-run;
   - comparar com Tiny;
   - gerar relatório de bloqueios.

3. Fase C — Write piloto:
   - ativar Shopify inventory write só para escopo limitado;
   - começar com poucos eventos ou uma location;
   - verificar readback Shopify após cada update.

4. Fase D — Produção silent-OK:
   - sem Telegram em sucesso;
   - alertas apenas para falha/bloqueio/risco.

## Rollback

- Desativar webhook/rota.
- Pausar script/scheduler/gateway route.
- Reverter Shopify inventory pelos snapshots before salvos no ledger, se necessário.
- Manter Tiny intocado.
