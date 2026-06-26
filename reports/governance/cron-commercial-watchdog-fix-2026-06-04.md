# Receipt — correção dos watchdogs comerciais LK/Zipper

Data: 2026-06-04
Escopo: correção local dos scripts de entrega comercial que marcavam `last_status=error` quando o WhatsApp (`wacli hermes`) estava não autenticado.

## Jobs afetados

- LK 09h previous-day sales report external delivery (`e3279babbc4a`)
- LK Pulso Comercial 16h read-only delivery (`c3bb587519d2`)
- LK 19h30 physical store close external delivery (`a2ead305eab2`)
- Zipper OS vendas 09h WhatsApp/email (`357d40a5863e`)

## Causa raiz

Os quatro jobs falhavam antes de concluir a entrega por causa de `wacli account hermes not authenticated` / `wacli hermes not authenticated`.

O problema não era geração dos relatórios nem sintaxe dos wrappers: os artefatos eram gerados, mas a camada de entrega abortava no WhatsApp antes de permitir o canal email/receipt.

## Correção aplicada

Arquivos alterados:

- `/opt/data/scripts/lk_report_external_delivery.py`
- `/opt/data/scripts/zipper_sales_report_external_delivery.py`

Mudança:

- Se WhatsApp estiver não autenticado, o job não aborta inteiro.
- O email aprovado continua sendo processado/verificado.
- O status passa a ser `partial_sent_email_only_whatsapp_unauthenticated` quando email OK e WhatsApp indisponível.
- Estado/idempotência agora é por canal, para permitir enviar WhatsApp depois que Lucas reconectar o `wacli`, sem reenviar email duplicado.
- Erros diferentes de WhatsApp não autenticado continuam falhando.

## Segurança

- Não foi feito pareamento WhatsApp.
- Não houve envio manual real durante a correção/verificação.
- Não houve Docker/VPS/Traefik/SSH/secrets/produção.
- Testes de caminho `--send` foram feitos com mocks locais para evitar write externo.

## Verificação

- `python3 -m py_compile` OK nos scripts alterados e wrappers.
- Dry-run real de geração/readiness OK.
- Teste mockado do caminho parcial OK: WhatsApp unauth → email mock OK → exit 0 → estado por canal preservado.

## Pendência externa

Para voltar a enviar WhatsApp, Lucas precisa estar presente para reautenticar `wacli hermes`. Até lá, os jobs devem parar de falhar por esse motivo e registrar status parcial quando o email for concluído.
