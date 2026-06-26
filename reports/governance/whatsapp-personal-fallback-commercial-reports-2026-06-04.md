# Receipt — fallback para WhatsApp pessoal nos relatórios comerciais

Data: 2026-06-04

## Decisão Lucas

Lucas pediu que, quando o WhatsApp Hermes (`wacli --account hermes`) estiver offline/unauthenticated, os relatórios comerciais aprovados usem o WhatsApp pessoal (`wacli --account pessoal`) como fallback.

## Escopo aplicado

Relatórios comerciais aprovados:

- LK 09h previous-day sales report
- LK 16h pulso comercial/financeiro
- LK 19h30 fechamento loja física
- Zipper 09h vendas

## Estado read-only observado

- `wacli --account hermes auth status`: unauthenticated
- `wacli --account pessoal auth status`: authenticated
- Nenhum pareamento foi iniciado.
- Nenhuma mensagem real foi enviada durante a correção/verificação.

## Correção aplicada

Arquivos alterados:

- `/opt/data/scripts/lk_report_external_delivery.py`
- `/opt/data/scripts/zipper_sales_report_external_delivery.py`
- `/opt/data/scripts/lk_previous_day_09h_sales_report_watchdog.py`
- `/opt/data/scripts/lk_financial_pulse_16h_watchdog.py`
- `/opt/data/scripts/lk_store_close_1930_watchdog.py`
- `/opt/data/scripts/zipper_weekday_sales_report_watchdog.py`
- `/opt/data/hermes_bruno_ingest/hermes-brain/config/lk-report-delivery-targets.json`

Comportamento novo:

1. Tenta WhatsApp pelo account primário `hermes`.
2. Se `hermes` estiver offline/unauthenticated, tenta `pessoal`.
3. Mantém os JIDs allowlisted já aprovados; não escolhe contato/grupo dinamicamente.
4. Registra `whatsapp_account` e `fallback_used` em state/receipts.
5. Se ambos os WhatsApps estiverem indisponíveis, preserva o comportamento de email parcial quando possível.

## Segurança

- Sem Docker/VPS/Traefik/SSH.
- Sem leitura/persistência de conversas.
- Sem secrets no receipt.
- Sem envio real durante teste.
- Sem auto-pair: se uma conta desconectar, pareamento ainda requer Lucas presente.

## Verificação

- Testes mockados confirmaram: `hermes` offline → `pessoal` autenticado → send chamado no account `pessoal` para o JID allowlisted.
- Teste mockado confirmou: nenhum account autenticado → erro WhatsApp local, permitindo fallback de email no caller.
- `py_compile` OK.
- Dry-run real OK.
- Brain health check OK.
