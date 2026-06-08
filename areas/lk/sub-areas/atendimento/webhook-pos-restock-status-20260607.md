# Status — webhook POS restock LK Team

Data: 2026-06-07

## Pergunta
Lucas perguntou se o webhook `lk-shopify-pos-restock` agora está correto para enviar alerta no WhatsApp do grupo LK Team em pedidos POS.

## Verificação read-only/local
- Config em `/opt/data/config.yaml` contém rota `lk-shopify-pos-restock` com `kind: lk_shopify_pos_restock`, evento `orders/paid`, secret e script `/opt/data/scripts/lk_store_sale_restock_alert.py`.
- Código instalado em `/opt/data/hermes-0.15.1-venv/lib/python3.13/site-packages/gateway/platforms/webhook.py` contém branch determinístico para `kind == lk_shopify_pos_restock` chamando `process_shopify_order_webhook`.
- Porém o gateway vivo em `HERMES_HOME=/opt/data` foi iniciado antes/sem carregar esse handler determinístico. Probe local assinado em `127.0.0.1:8644/webhooks/lk-shopify-pos-restock` com evento `orders/paid` retornou `202 {"status":"accepted"...}`, que é o caminho genérico/LLM, não o retorno esperado do handler (`sent_count`, `queued_count`, `order_id`, `reason`).
- Gateway do profile `lk-ops` roda com `WEBHOOK_ENABLED=false`; a porta 8644 aberta pertence ao gateway default `/opt/data`.

## Conclusão operacional
Ainda não está correto para produção futura. Está parcialmente preparado em config/código, mas falta reload/restart controlado do gateway público e reprobe retornando resposta determinística.

## Próximo passo recomendado
Com aprovação explícita: fazer restart/reload seguro do gateway que atende a porta 8644, testar com payload controlado não-POS/sem envio real e só declarar OK quando o retorno deixar de ser `accepted` e passar a incluir campos do handler determinístico.
