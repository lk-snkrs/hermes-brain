# Feature — LK reposição automática pós-venda POS via WhatsApp + Notion

Data: 2026-05-23
Status: `implemented_preview_not_activated`

## Pedido de Lucas

Quando vender um tênis em loja física/POS, o Hermes deve perguntar no WhatsApp do LK Team se deve repor. Exemplo:

```text
ALERTA DE REPOSIÇÃO

Novo produto vendido em loja: New Balance 9060 Moon Beam U9060WHT tamanho 37

Devemos repor? Digite sim ou não.
```

Se alguém responder `sim`, Hermes deve criar um novo pedido/card de compra no Notion usando o padrão aprendido de LK Estoque / Júlio:

```text
[LOJA ESTOQUE] Nome do Produto - SKU - Tamanho
```

## Implementação local feita

### 1. Entrada correta: webhook Shopify, não polling

Script/módulo local:

```text
/opt/data/scripts/lk_store_sale_restock_alert.py
```

Regra corrigida por Lucas: **produção deve usar webhook da Shopify; nunca cron/script consultando Shopify periodicamente para buscar produtos/pedidos novos**.

Comportamento:

- É chamado pela rota do Gateway `kind=lk_shopify_pos_restock` após validação HMAC Shopify.
- Usa o payload do webhook como fonte do evento.
- Não consulta Shopify Admin para descobrir pedido novo.
- Filtra pedidos pagos/não cancelados de loja física/POS:
  - `source_name == pos`; ou
  - `app_id == 129785`.
- Lê line items vendidos do payload.
- Deduplica por `order_id:line_item_id` e por delivery/webhook id.
- Gera mensagem para o grupo `[LK] Team` (`120363367222855384@g.us`).
- CLI de produção/polling foi desativada; sem `--send` por cron.
- Registra fila pendente em state local para o responder processar o `sim`/`não`.

Mensagem gerada:

```text
ALERTA DE REPOSIÇÃO

Novo produto vendido em loja: {nome} {sku} tamanho {tamanho}
Pedido Shopify/POS: {pedido}

Devemos repor? Digite sim ou não.
```

### 2. Responder WhatsApp atualizado

Arquivo alterado:

```text
/opt/data/scripts/lk_hermes_whatsapp_responder.py
```

Novo comportamento:

- Se houver alerta de reposição POS pendente no `[LK] Team`, aceita `sim`/`não` sem precisar mencionar Hermes.
- Se o pedido tiver **1 item**:
  - `sim` → cria card no Notion `[LK] Encomenda` usando função existente `create_notion_stock_purchase`.
  - `não` → remove a pendência e não cria card.
- Se o pedido tiver **mais de 1 item**:
  - Hermes envia apenas o **Item 1/N**.
  - Após `sim`/`não`, processa aquele item e avança automaticamente para o **Item 2/N**.
  - Continua 1/N até acabar.
  - Não pede `sim SKU`/`não SKU` como fluxo principal; a decisão é sempre sequencial.

### 3. Padrão Notion reutilizado

A criação usa a função já existente:

```python
create_notion_stock_purchase(item)
```

Database:

```text
[LK] Encomenda / 2b127dc9-e033-805b-81b6-f62f5467ce77
```

Propriedades principais:

- `Nome`: `[LOJA ESTOQUE] {produto} - {sku} - {tamanho}`
- `Status da Compra`: `Aguardando Aprovação`
- `Fornecedor`: `Júlio / compra para reposição de estoque loja`
- `Origem`: `Nacional`
- `Pedido # ID`: `LOJA ESTOQUE`
- `Avisar Fornecedor`: `Não`
- `Programar Pagamento`: `Não`

Guardrail preservado: Hermes cria card; não compra, não reserva, não avisa fornecedor e não programa pagamento.

## Verificações executadas

```bash
python3 -m py_compile /opt/data/scripts/lk_store_sale_restock_alert.py /opt/data/scripts/lk_hermes_whatsapp_responder.py /opt/data/scripts/lk_hermes_whatsapp_responder_selftest.py /opt/data/scripts/tests/test_lk_store_sale_restock_webhook.py
python3 /opt/data/scripts/lk_hermes_whatsapp_responder_selftest.py
python3 /opt/data/scripts/tests/test_lk_store_sale_restock_webhook.py
python3 /opt/data/scripts/lk_store_sale_restock_alert.py
```

Resultados:

- py_compile: OK.
- selftest responder: OK / silent success.
- webhook 1/N test: OK.
- CLI sem sample: retorna `webhook_only`; polling de produção fica desativado.

## Ativação pendente

Para virar automação real, falta Lucas aprovar/confirmar a rota webhook Shopify e activation do envio externo.

Direção correta:

- criar/usar webhook Shopify `orders/create` e/ou `orders/paid` apontando para a rota Hermes `kind=lk_shopify_pos_restock`;
- validar HMAC Shopify no Gateway;
- sem cron polling Shopify;
- WhatsApp enviado somente quando webhook real de venda POS chegar;
- `deliver` do webhook é JSON/HTTP, sem relatório Telegram em cada evento.

## Limites

Permitido após ativação:

- enviar alerta interno no WhatsApp `[LK] Team` para venda POS;
- criar card Notion de reposição quando alguém responder `sim`.

Bloqueado:

- compra automática;
- reserva automática;
- contato com fornecedor;
- pagamento;
- alteração em Shopify/Tiny/estoque/preço;
- envio para cliente;
- qualquer write externo fora do card Notion aprovado.
