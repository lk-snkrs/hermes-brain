# Fase 4C — Mesa COO Telegram UX clean delivery

Data: 2026-05-24
Escopo: Hermes Main / Telegram / cron Mesa COO diária

## Problema reportado
Lucas recebeu uma entrega do cron com resíduos técnicos visíveis:
- `Cronjob Response: ...`
- `(job_id: ...)`
- comentário HTML `HERMES_INLINE_BUTTONS:{...}`
- instrução técnica de gerenciamento do job

Isso viola a política UX: Telegram deve mostrar decisão acionável, não metadados de runtime.

## Diagnóstico
1. O wrapper `Cronjob Response` era controlado por `cron.wrap_response`.
2. A config atual em `/opt/data/config.yaml` está correta:
   - `cron.wrap_response: false`
3. O scheduler atual possui parser para `HERMES_INLINE_BUTTONS`, removendo o comentário HTML e convertendo o payload em metadata para o adapter Telegram.
4. Evidência temporal:
   - Gateway Main iniciou em `2026-05-24 11:03:26 UTC`.
   - `cron/scheduler.py` estava atualizado antes desse start (`2026-05-24 10:58:17 UTC`).
   - A mensagem ruim que Lucas colou entrou no gateway às `2026-05-24 10:13 UTC`, antes do restart/carregamento do scheduler corrigido.
5. O run posterior da Mesa (`/opt/data/cron/output/749ee30b51eb/2026-05-24_11-28-57.md`) já gerou resposta sem texto visível de botões e com marcador no formato correto para remoção.

## Correção adicional aplicada em código
Arquivo alterado:
- `/opt/hermes/gateway/platforms/telegram.py`

Mudança:
- No callback dos botões inline (`ib:*`), o evento encaminhado ao gateway deixou de usar `message_id="callback:<button_id>"`.
- Agora usa o `message_id` real da mensagem Telegram original como `message_id` e `reply_to_message_id`.

Motivo:
- Logs mostraram erro após clique em botão: `invalid literal for int() with base 10: 'callback:...'`.
- O path de resposta do gateway pode converter IDs de mensagem para inteiro para reply anchors; IDs sintéticos quebravam esse fluxo.

## Testes executados
Comando:

```bash
/opt/hermes/.venv/bin/python -m pytest \
  tests/cron/test_scheduler.py::TestDeliverResultWrapping::test_delivery_strips_inline_button_marker_and_passes_metadata \
  tests/cron/test_scheduler.py::TestDeliverResultWrapping::test_live_adapter_inline_button_marker_is_cleaned_before_send \
  tests/cron/test_scheduler.py::TestDeliverResultWrapping::test_delivery_skips_wrapping_when_config_disabled -q
```

Resultado:
- `3 passed`

Compile check:

```bash
/opt/hermes/.venv/bin/python -m py_compile /opt/hermes/cron/scheduler.py /opt/hermes/gateway/platforms/telegram.py
```

Resultado:
- OK

## Estado de ativação
- A limpeza do wrapper/marker já deve estar ativa no scheduler carregado pelo gateway Main, pois o gateway iniciou após a atualização do scheduler.
- A correção do callback `ib:*` foi escrita depois do start do gateway; requer restart seguro do gateway Main para entrar em runtime.

## Próximo passo recomendado
Fazer restart seguro apenas do gateway Main Hermes, com rollback simples por não tocar Docker/host/volumes:
1. Confirmar PID Main (`HERMES_HOME=/opt/data`).
2. Encerrar/reiniciar somente esse processo via mecanismo normal do supervisor/runtime Hermes.
3. Verificar que o Telegram voltou a responder.
4. Rodar um teste controlado de entrega ou aguardar a próxima Mesa diária.

Não foi alterado Shopify, GMC, Tiny, Meta, Google Ads, Docker, VPS, banco, WhatsApp, e-mail, cliente ou fornecedor.
