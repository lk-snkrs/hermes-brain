# Receipt — n8n checkout abandonado 30min/24h/72h com cupom

Data UTC: 2026-05-20T17:28:24Z  
Data BRT: 2026-05-20T14:28:24-0300  
Área: LK CRM / WhatsApp / Crisp / n8n / Shopify

## Pedido

Lucas aprovou implementar no fluxo n8n a sequência consolidada de checkout abandonado:

- T1: 30min
- T2: 24h
- T3: 72h com cupom personalizado de 10% válido por 24h
- HEADER image do produto em todos os touchpoints
- CTA Meta: `Finalizar compra`

## Templates Meta verificados antes do write

WABA: `1478026007140488`

- `lk_checkout_abandonado_30min_v4` — `APPROVED` — Marketing — `pt_BR`
- `lk_checkout_abandonado_24h_v1` — `APPROVED` — Marketing — `pt_BR`
- `lk_checkout_abandonado_72h_cupom10_v1` — `APPROVED` — Marketing — `pt_BR`

## Workflow alterado

- ID: `kWQbmEMuvdipcGjd`
- Nome anterior: `LK - Checkout Abandonado 30min Polling GraphQL - Crisp (ATIVO)`
- Nome atual: `LK - Checkout Abandonado 30min/24h/72h Polling GraphQL - Crisp (ATIVO)`
- Status pós-write: `active: true`
- `versionId`: `4228953e-e994-42d1-a058-fe8250653703`
- `activeVersionId`: `4228953e-e994-42d1-a058-fe8250653703`
- `triggerCount`: `1`

## Implementação aplicada

### Fonte / polling

- Mantido polling Shopify GraphQL a cada 5 minutos.
- Consulta `abandonedCheckouts` aumentada de `first: 50` para `first: 100`.
- Mantido cutoff de migração `2026-05-20T14:15:00Z` para evitar blast histórico.

### Elegibilidade e sequência

O nó `Filtrar elegíveis + dedup` agora:

- escolhe um único próximo touchpoint por checkout/telefone;
- bloqueia com `staticData.sent[dedupKey].status = pending` antes do envio;
- trata `pending` e `sent` como já processados;
- exige sequência:
  - `24h` só após `30min` marcado como `sent`;
  - `72h` só após `24h` marcado como `sent`;
- mantém dedup por touchpoint:
  - `30min:<checkoutId>:<phone>`
  - `24h:<checkoutId>:<phone>`
  - `72h:<checkoutId>:<phone>`
- mantém validações de segurança:
  - não envia sem `createdAt`;
  - não envia antes do cutoff;
  - não envia se `completedAt` existir;
  - não envia sem telefone BR normalizado em E.164;
  - não envia sem recovery URL/token;
  - não usa fallback aleatório para dedup principal;
  - usa `sua seleção` quando houver múltiplos itens.

### Cupom T3

Adicionado nó `Shopify Cupom 72h / Gate`:

- Para `30min` e `24h`: executa apenas query no-op Shopify, sem write comercial.
- Para `72h`: cria cupom via Shopify GraphQL `discountCodeBasicCreate`.
- Código gerado em padrão determinístico: `LK10-<checkoutIdCurto>-<finalTelefone>`.
- Desconto: 10%.
- Validade: 24h a partir do momento de criação.
- Limite de uso: 1.
- `appliesOncePerCustomer: true`.

### Payload Crisp/WhatsApp

Adicionado nó `Preparar payload Crisp`:

- escolhe template por touchpoint;
- mantém HEADER image com `$json.productImage` em todos os templates;
- mantém CTA URL com token de checkout;
- usa shape LK validado para Crisp Inbox:
  - `crisp_options.as = text`
  - `crisp_options.type = text`
  - `crisp_options.new_session = false`
  - `BODY.text` fallback humano.

Templates roteados:

- `30min` → `lk_checkout_abandonado_30min_v4`
- `24h` → `lk_checkout_abandonado_24h_v1`
- `72h` → `lk_checkout_abandonado_72h_cupom10_v1`

### Mark sent / dedup

O nó `Marcar enviado no dedup` agora:

- usa `Preparar payload Crisp` como fonte original;
- valida cardinalidade `responses.length === originals.length`;
- marca `sent` apenas se Crisp retornar:
  - `error === false`
  - `reason === request_accepted`
  - `data.request_id` presente;
- marca falhas em `staticData.failed` e mantém status `failed` quando a resposta não confirma aceite.

## Backups locais restritos

Snapshots salvos fora do Brain, com permissão local restrita:

- `/opt/data/hermes_bruno_ingest/.secrets/n8n_backups/kWQbmEMuvdipcGjd-pre-3touchpoint-coupon-impl-20260520T172718Z.json`
- `/opt/data/hermes_bruno_ingest/.secrets/n8n_backups/kWQbmEMuvdipcGjd-pre-rename-3touchpoints-20260520T172815Z.json`

Não registrar conteúdo desses snapshots no Brain, pois workflows podem conter headers/autenticação.

## Verificações pós-write

Readback n8n confirmou:

- workflow ativo: sim;
- `activeVersionId == versionId`: sim;
- templates 30min/24h/72h presentes no workflow: sim;
- mutation Shopify `discountCodeBasicCreate` presente: sim;
- shape híbrido Crisp `as:text` + `type:text`: presente;
- nodes esperados presentes:
  - `A cada 5 min`
  - `Shopify GraphQL abandonedCheckouts`
  - `Filtrar elegíveis + dedup`
  - `Shopify Cupom 72h / Gate`
  - `Preparar payload Crisp`
  - `Crisp Send checkout touchpoint`
  - `Marcar enviado no dedup`
- syntax check local dos Code nodes via `node --check`: OK para os 3 Code nodes.
- callback/logging workflow ativo: `LK - Crisp WhatsApp Callback Capture (ATIVO)` (`8heG4ZyRp85p0MQj`).

## O que não foi feito

- Nenhum envio manual de WhatsApp foi disparado.
- Nenhum replay/backfill histórico foi executado.
- Nenhum cupom foi criado manualmente fora da lógica do fluxo.
- Nenhuma alteração de template Meta foi feita neste passo.

## Rollback / kill switch

Rollback rápido:

1. Desativar workflow `kWQbmEMuvdipcGjd` no n8n se houver anomalia.
2. Restaurar snapshot pré-implementação:
   - `/opt/data/hermes_bruno_ingest/.secrets/n8n_backups/kWQbmEMuvdipcGjd-pre-3touchpoint-coupon-impl-20260520T172718Z.json`
3. Alternativa parcial: reverter conexões para o fluxo antigo `30min` e o nó Crisp `lk_checkout_abandonado_30min_v4`.

## Monitoramento recomendado

Nas próximas 24–72h:

- monitorar execuções do workflow e `staticData.failed`;
- validar callbacks Crisp/WhatsApp pelo workflow `LK - Crisp WhatsApp Callback Capture (ATIVO)`;
- não declarar entrega com base apenas em `request_accepted`;
- se Lucas reportar não-recebimento, comparar payload atual com o último payload confirmado antes de reenviar.
