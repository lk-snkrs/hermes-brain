# LK Chatwoot Shopify integration / population audit

Data: 2026-06-03 14:14 UTC
Status: `shopify_integration_enabled_context_only_no_bulk_sync`

## Pedido

Lucas pediu para confirmar:

1. se a integração Shopify no Chatwoot está habilitada;
2. se ela apenas mostra pedidos/contexto ou se existe rotina de sync;
3. se a meta for popular Chatwoot, definir caminho seguro de export/import;
4. não depender dessa tela para WhatsApp/recuperação.

## Fontes consultadas

- Chatwoot health: `https://chat.lkskrs.online/api`
- Chatwoot Rails read-only via VPS/container
- Chatwoot source dentro do container (`api/v1/accounts/integrations/shopify_controller.rb`, `webhooks/shopify_controller.rb`)
- Shopify Admin read-only count endpoint via Doppler-held token, sem expor valores

## Resultado Chatwoot

Health público:

```text
version: 4.14.1
queue_services: ok
data_services: failing
HTTP 200
```

Conta LK:

```text
account_id: 1
account_name: LK Sneakers
```

Integração Shopify:

```text
feature_shopify: true
client_id_present: true
app_record_present: true
app_active: true
app_enabled: true
hook_count: 1
hook_status: enabled
reference_id: lk-sneakerss.myshopify.com
```

Contatos/conversas/inbox:

```text
Chatwoot contacts_count: 0
Chatwoot conversations_count: 0
Inbox existente: Shopify Carrinho Abandonado / Channel::Api
Times: suporte, atendimento whatsapp
Labels: 13
```

Shopify customers count read-only:

```text
customers_count: 28995
```

## Comportamento da integração nativa Shopify

O código Chatwoot indica que a integração nativa é **contexto on-demand**, não bulk sync.

Fluxo observado no controller:

1. recebe `contact_id` do Chatwoot;
2. valida que o contato tem e-mail ou telefone;
3. consulta Shopify `customers/search.json` com e-mail/telefone do contato;
4. consulta Shopify `orders.json` por `customer_id`;
5. retorna pedidos/contexto para a tela.

Webhook Shopify nativo observado no Chatwoot:

- trata `shop/redact` para remoção de hook;
- não há rotina evidente de importação/sync contínuo de clientes Shopify para contatos Chatwoot.

## Veredito

A integração Shopify no Chatwoot está habilitada e conectada ao domínio correto, mas ela não popula automaticamente o CRM do Chatwoot com clientes Shopify. No estado observado, o Chatwoot tem 0 contatos enquanto Shopify tem 28.995 clientes.

## Se a meta for popular Chatwoot

Precisa de fluxo separado e aprovado, com LGPD/anti-disparo:

1. Exportar clientes Shopify por Admin API read-only em lotes/paginação.
2. Normalizar:
   - nome;
   - e-mail;
   - telefone E.164 quando possível;
   - tags relevantes;
   - Shopify customer id em `additional_attributes`/custom attributes.
3. Deduplicar por telefone normalizado, e-mail lowercase e Shopify customer id.
4. Importar/criar contatos no Chatwoot por API em lote idempotente.
5. Não criar conversa pública automaticamente.
6. Não enviar mensagem automática.
7. Marcar origem/consentimento e manter trilha de auditoria.
8. Rodar primeiro em dry-run com amostra e relatório de quantos seriam criados/atualizados/pulados.

## WhatsApp/recuperação

Para WhatsApp/recuperação, a tela Shopify do Chatwoot não basta. O contato precisa estar identificável e contactável no pipeline operacional: telefone/e-mail confiável, opt-out/supressão respeitada, compra rechecada, cooldown/quiet hours/kill-switch, e evidência segura em dry-run/internal-only antes de qualquer envio real.

## Ações não feitas

- Nenhum export bulk de PII foi executado.
- Nenhum contato foi criado/alterado no Chatwoot.
- Nenhuma mensagem foi enviada.
- Nenhum write em Shopify/Chatwoot/secrets foi feito.
