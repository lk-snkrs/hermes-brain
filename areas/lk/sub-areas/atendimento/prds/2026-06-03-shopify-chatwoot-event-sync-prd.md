# PRD — Shopify → Chatwoot Event Sync / CRM inteligente

Data: 2026-06-03
Área: LK Sneakers / Atendimento / Chatwoot / Shopify
Status: rascunho para decisão — Lucas escolheu backfill inicial somente de clientes com telefone válido; ainda sem autorização de write externo

## 1. Contexto

A integração nativa Shopify do Chatwoot está conectada, mas não faz sincronização em massa de clientes para contatos do Chatwoot. No código atual do Chatwoot, a integração Shopify:

- conecta via OAuth;
- busca cliente Shopify por `email` ou `phone_number` de um contato Chatwoot existente;
- busca pedidos desse customer para exibir contexto na conversa;
- não cria automaticamente contatos Chatwoot a partir de todos os clientes Shopify;
- o endpoint nativo de webhook Shopify do Chatwoot trata basicamente eventos de privacidade como `shop/redact`, não lifecycle operacional de clientes/pedidos.

Conclusão: para popular Chatwoot de forma inteligente, LK precisa de uma camada própria de eventos/sincronização usando webhooks Shopify e API do Chatwoot.

## 2. Objetivo

Criar um sistema seguro e auditável que alimente o Chatwoot com:

1. contatos Shopify identificáveis;
2. eventos de pedido;
3. contexto de carrinho/checkout abandonado;
4. labels e atributos operacionais;
5. notas internas para atendimento;
6. base pronta para campanhas/WhatsApp, sem envio automático sem aprovação.

## 3. Não objetivos

- Não usar Chatwoot como fonte de estoque. Tiny continua fonte de verdade.
- Não enviar WhatsApp automaticamente no MVP.
- Não importar contato sem telefone/e-mail útil para atendimento, salvo decisão explícita.
- Não replicar todo Shopify no Chatwoot como ERP.
- Não prometer disponibilidade/preço/prazo a partir desses dados.

## 4. Evidência pesquisada

### Shopify

- Shopify webhooks são assinados com `X-Shopify-Hmac-SHA256`; validação deve usar HMAC SHA256 sobre o corpo raw do request e comparação segura.
- WebhookSubscription é um objeto persistente com `topic`, `uri`, `format`, `includeFields`, etc.
- REST Admin expõe customers e orders; Orders podem ser listados por `status=any`; Customers exigem escopo apropriado.

### Chatwoot

- `ContactsController#create/update` aceita `name`, `identifier`, `email`, `phone_number`, `additional_attributes`, `custom_attributes`.
- Labels podem ser aplicadas em contatos/conversas via endpoints de labels.
- Conversas podem ser criadas vinculadas a `inbox_id`, `contact_id`, `source_id`.
- Mensagens/notas internas podem ser criadas em conversas; isso deve ser usado no MVP antes de qualquer mensagem pública.
- Integração Shopify nativa busca pedidos a partir de contato já existente, não backfill de contatos.

## 5. Arquitetura recomendada

```text
Shopify webhooks + backfill inicial
→ LK Event Hub / Recovery OS
→ valida HMAC + dedupe + normaliza payload
→ persiste evento bruto mínimo + estado normalizado
→ upsert Chatwoot contact
→ aplica labels/custom attributes
→ cria/atualiza conversa interna quando necessário
→ adiciona private note com pedido/carrinho/contexto
→ opcional futuro: WhatsApp template aprovado via Chatwoot
```

Preferência: reaproveitar/ampliar o LK Recovery OS como Event Hub, porque ele já lida com Shopify events, identidade, abandoned cart, dry-run, kill switches e Chatwoot internal-only.

## 6. Webhooks/eventos propostos

### Cliente / identidade

- `customers/create`
- `customers/update`
- `customers/delete`
- `customers/redact`
- `customers_marketing_consent/update` se disponível/necessário no plano atual

### Pedido

- `orders/create`
- `orders/updated`
- `orders/paid`
- `orders/fulfilled`
- `orders/cancelled`
- `refunds/create` se for útil para atendimento financeiro/troca

### Checkout/carrinho

- `checkouts/create`
- `checkouts/update`
- `orders/create` como conversão/supressão de recovery
- eventos storefront/Klaviyo já existentes no Recovery OS para visitante anônimo/cookie/cart token

## 7. Modelo de dados no Chatwoot

### Contact

Campos principais:

- `name`: nome Shopify quando existir;
- `email`: email normalizado;
- `phone_number`: E.164 quando possível;
- `identifier`: `shopify_customer:<id>` quando seguro;
- `custom_attributes`:
  - `shopify_customer_id`
  - `shopify_customer_gid`
  - `shopify_tags`
  - `shopify_orders_count`
  - `shopify_total_spent`
  - `last_order_id`
  - `last_order_name`
  - `last_order_at`
  - `last_financial_status`
  - `last_fulfillment_status`
  - `marketing_consent_sms/email` se decidido
  - `lk_identity_source`

Labels iniciais:

- `shopify`
- `cliente-shopify`
- `comprou`
- `lead-shopify`
- `carrinho-abandonado`
- `pedido-em-aberto`
- `pedido-pago`
- `pedido-enviado`
- `pedido-cancelado`
- `vip` quando regra aprovada

### Conversation / private note

Para eventos relevantes, criar ou atualizar conversa interna no inbox API/operacional, com private note:

- pedido número/nome;
- status financeiro;
- status fulfillment;
- valor;
- itens resumidos;
- link admin Shopify;
- risco/ação sugerida;
- alerta Tiny quando envolver disponibilidade.

## 8. Idempotência e dedupe

Chaves:

- Shopify webhook delivery ID quando disponível;
- `topic + shop_domain + resource_id + updated_at` como fallback;
- Chatwoot `source_id` estável por contato/inbox, por exemplo `shopify_customer_<id>`;
- tabela/ledger local para eventos processados e efeitos Chatwoot executados.

Reprocessamento deve ser seguro: atualizar contato, não duplicar; acrescentar nota só quando evento novo ou mudança material.

## 9. Backfill inicial

Fase controlada antes dos webhooks:

1. dry-run Shopify customers count;
2. classificar todos os clientes, incluindo telefone válido, e-mail only e sem canal útil;
3. normalizar telefone para E.164;
4. dedupe por telefone, e-mail e Shopify customer ID;
5. simular labels/atributos;
6. gerar relatório de amostra;
7. só depois, com aprovação, criar/atualizar contatos Chatwoot em lotes.

Decisão Lucas 2026-06-03: o backfill alvo é todos os ~29k clientes Shopify, não apenas os com telefone. Isso exige labels/atributos que separem contatos WhatsApp-ready de contatos apenas informacionais. Nem todo contato importado será elegível para outbound.

## 10. MVPs

### MVP 0 — Auditoria/dry-run

- Mapear campos reais Shopify.
- Contar clientes com telefone, e-mail, consentimento e pedidos.
- Simular o payload Chatwoot para 100 exemplos.
- Zero writes externos.

### MVP 1 — Backfill de contatos elegíveis

- Criar/atualizar contatos Chatwoot para clientes com telefone válido.
- Labels básicas `shopify`, `cliente-shopify`.
- Sem conversas, sem mensagens.

### MVP 2 — Webhook cliente/pedido → Chatwoot

- Receber `customers/*` e `orders/*`.
- Atualizar contato e atributos.
- Criar private note interna em conversa API para eventos de pedido material.

### MVP 3 — Carrinho/checkout abandonado internal-only

- Webhook checkout + delayed recheck.
- Se abandonado e contactável: contato + label + private note.
- Sem envio ao cliente.

### MVP 4 — WhatsApp assistido

- Exige inbox WhatsApp Cloud real no Chatwoot.
- Exige templates Meta aprovados.
- Agente humano dispara template aprovado.

### MVP 5 — Automação controlada

- Só com aprovação explícita.
- Kill switch, consentimento, cooldown, opt-out, ledger de envio, limite diário, auditoria.

## 11. Regras de segurança LK

- Tiny é fonte de estoque; Shopify/Chatwoot não autorizam promessa de disponibilidade.
- Sem envio externo no MVP 0-3.
- Reclamação, atraso, troca/devolução, financeiro, desconto, reserva e prazo exigem humano.
- Qualquer Shopify/Tiny/Chatwoot write real exige aprovação de escopo.
- Webhook deve responder rápido e processar async com retry/dead-letter.
- Não salvar PII bruta desnecessária no Brain/logs.

## 12. Métricas de sucesso

- % clientes Shopify com telefone válido importável.
- Contatos Chatwoot criados/atualizados.
- Eventos Shopify recebidos, dedupados e processados.
- Tempo webhook → atualização Chatwoot.
- Conversas/notas internas úteis criadas.
- Zero duplicação relevante de contatos.
- Zero mensagens externas não aprovadas.
- Para recovery: candidatos contactáveis chegando no Chatwoot internal-only.

## 13. Decisões abertas

1. Escopo do backfill: todos os clientes ou apenas com telefone válido? **Decidido: todos os ~29k clientes Shopify.**
2. O Chatwoot deve receber uma conversa por pedido, por cliente ou só private notes na conversa ativa?
3. Devemos armazenar histórico completo de pedidos no Chatwoot ou só último pedido + link Shopify?
4. Consentimento LGPD/WhatsApp: qual regra de elegibilidade vamos aplicar?
5. Usar Recovery OS como Event Hub ou criar serviço separado?
6. Qual inbox Chatwoot será o destino operacional até existir WhatsApp Cloud real?

## 14. Recomendação

Construir como extensão do LK Recovery OS, começando por MVP 0 dry-run + PRD aprovado. Depois fazer MVP 1 com backfill só de clientes com telefone válido, sem criar mensagens. Em seguida ativar webhooks de `customers/*` e `orders/*` para manter Chatwoot atualizado.

Essa rota resolve o problema real: Chatwoot vira base viva de atendimento alimentada por Shopify, sem depender de uma importação manual estática e sem confundir Chatwoot com estoque/ERP.

## 15. Decisão recebida

Lucas escolheu a **Opção 1: importar inicialmente somente clientes com telefone válido**.

Implicação:

- MVP 0 deve auditar Shopify em read-only e gerar somente métricas agregadas/anonimizadas;
- MVP 1, se aprovado depois, fará backfill controlado no Chatwoot apenas de clientes com telefone E.164 válido;
- clientes somente com e-mail ficam fora do primeiro lote;
- nenhum envio WhatsApp/campanha está autorizado por essa decisão.

## 16. Resultado MVP 0 dry-run agregado

Execução autorizada por Lucas para escaneamento read-only agregado, sem writes externos e sem salvar PII bruta.

Relatório: `areas/lk/sub-areas/atendimento/reports/2026-06-03-shopify-chatwoot-mvp0-phone-dryrun.json`

Resumo:

- clientes Shopify escaneados: 29.003;
- páginas REST lidas: 117;
- clientes com telefone válido: 6.564;
- telefones BR válidos: 6.559;
- telefones não-BR E.164-like: 5;
- clientes com telefone válido + e-mail: 5.934;
- clientes com telefone válido sem e-mail: 630;
- clientes com telefone válido e pelo menos 1 pedido: 4.959;
- clientes com telefone válido sem pedido: 1.605;
- telefones normalizados únicos: 6.312;
- grupos de telefone duplicado: 242;
- clientes dentro de grupos duplicados: 494;
- máximo de clientes no mesmo telefone: 4;
- SMS subscribed observado: 147;
- Shopify writes: 0;
- Chatwoot writes: 0;
- envios externos: 0.

Próximo gate: aprovação separada para MVP 1 antes de qualquer criação/atualização de contatos no Chatwoot.

## 17. Resultado MVP 1 backfill Chatwoot

Lucas aprovou o MVP 1 com escopo: criar/atualizar contatos no Chatwoot apenas para clientes Shopify com telefone válido, sem conversas, sem mensagens e sem envios externos.

Relatório: `areas/lk/sub-areas/atendimento/reports/2026-06-03-shopify-chatwoot-mvp1-phone-backfill-result.json`

Resumo verificado:

- clientes Shopify escaneados: 29.004;
- clientes com telefone válido: 6.565;
- telefones normalizados únicos selecionados: 6.313;
- contatos Chatwoot antes: 0;
- contatos Chatwoot criados: 6.313;
- contatos Chatwoot atualizados: 0;
- labels aplicadas/atualizadas: 6.313;
- erros: 0;
- contatos Chatwoot após: 6.313;
- label `shopify-phone-valid`: 6.313 contatos;
- label `shopify-duplicate-review`: 242 contatos/grupos;
- Shopify writes: 0;
- Chatwoot conversations/messages/private notes: 0 pelo escopo do script;
- envios WhatsApp/e-mail/Klaviyo: 0.

Labels criadas no MVP 1:

- `cliente-shopify`;
- `shopify-phone-valid`;
- `shopify-duplicate-review`.

Próximo gate: aprovação separada para conversas, notas internas, webhooks, inbox WhatsApp Cloud, campanhas ou qualquer mensagem visível ao cliente.
