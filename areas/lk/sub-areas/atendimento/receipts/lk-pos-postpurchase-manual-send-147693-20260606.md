# Receipt — envio manual pós-venda POS #147693

Data/hora UTC: 2026-06-06T14:xxZ

## Pedido de Lucas

Lucas pediu no Telegram para enviar a mensagem de pós-venda agora, para testar o funcionamento, referente à compra POS recém-identificada.

## Escopo

- Pedido: #147693
- Origem: POS
- Ação externa aprovada: envio de 1 mensagem WhatsApp de agradecimento pós-venda para a cliente do pedido.
- Canal usado: Evolution API / instância LK Flagship.

## Fonte viva consultada

- Shopify Admin GraphQL read-only:
  - pedido #147693 encontrado;
  - `sourceName=pos`;
  - `displayFinancialStatus=PAID`;
  - sem cancelamento;
  - telefone presente no pedido/cliente;
  - tag de vendedor resolvida para `Danilo`.

## Mensagem enviada

```text
Oi Thais, tudo bem? Aqui é o Danilo, da LK.

Queria te agradecer pessoalmente pela compra e pela confiança. Receber você na nossa loja foi um prazer!

Estamos à disposição para o que precisar. Fico em contato!

Obrigado e abraços,
Danilo
```

## Execução

1. Tentativa via worker/canary usando credencial `EVOLUTION_LK_FLAGSHIP_KEY`:
   - Resultado: falhou com HTTP 401 Unauthorized.
   - Nenhuma confirmação de envio nessa tentativa.
2. Retry controlado usando `EVOLUTION_API_KEY` na mesma instância `LK Flagship`:
   - HTTP: 201
   - status Evolution: `PENDING`
   - `fromMe=true`
   - `id_present=true`
   - `messageType=conversation`
   - `instanceId_present=true`
   - Job local marcado como `sent` / `send_executed=true` / `external_write_executed=true`.

## Ajuste local aplicado

- Arquivo: `/opt/data/scripts/lk_store_sale_restock_alert.py`
- Função ajustada: `load_evolution_lk_flagship_credentials()`
- Mudança: priorizar `EVOLUTION_API_KEY` / `EVOLUTION_API_TOKEN` antes de `EVOLUTION_LK_FLAGSHIP_KEY` para `sendText`, porque a chave flagship listava instâncias mas retornava 401 no envio.
- Nenhum write em Shopify/Tiny/Chatwoot/n8n.

## Verificação pós-ajuste

Comandos:

```bash
python3 /opt/data/scripts/tests/test_lk_store_sale_restock_webhook.py
python3 -m py_compile /opt/data/scripts/lk_store_sale_restock_alert.py /opt/data/profiles/lk-ops/scripts/lk_pos_postpurchase_canary_worker.py
python3 /opt/data/profiles/lk-ops/scripts/lk_pos_postpurchase_canary_worker.py
```

Resultados:

- Testes: `ok`
- Py compile: exit 0
- Worker pós-envio: sem jobs novos devidos; `prior_live_sends=1`, `sent=0`, `errors=0`, `skipped_not_scheduled=1`.

## Guardrails

- PII minimizada neste receipt; telefone não registrado.
- Envio externo limitado ao pedido #147693.
- Shopify usado só para leitura/validação do pedido.
- Nenhum estoque/preço/disponibilidade prometido.
- Nenhum write em Shopify/Tiny/Chatwoot/n8n.
