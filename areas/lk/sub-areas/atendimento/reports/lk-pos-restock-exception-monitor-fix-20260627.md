# LK POS restock/recompra — exception monitor fix

Data: 2026-06-27
Status: done
values_printed=false

## Pedido
Lucas respondeu "Corrigir" ao alerta do monitor:
- Gateway health: `process_missing`
- Noop assinado rota POS restock: `skipped_cli_first_no_raw_post`

## Diagnóstico
O gateway real estava saudável:
- `http://127.0.0.1:8644/health` retornou HTTP 200 `{"status":"ok","platform":"webhook"}`.
- Porta 8644 aberta.

Causa do falso alerta:
1. O monitor não chamava o health endpoint; fazia `pgrep` por strings (`lk_store_sale_restock|lk-shopify-pos-restock|8644`) que não aparecem no comando real do gateway.
2. O noop assinado estava desativado no código (`skipped_cli_first_no_raw_post`) mas o próprio monitor tratava isso como erro.
3. Primeiro teste com Shopify HMAC local retornou 401; confirmação mostrou que o gateway local espera assinatura genérica Hermes (`X-Webhook-Signature` + `HERMES_WEBHOOK_SECRET`). A assinatura Shopify nativa pertence à camada proxy/borda.

## Correção
Arquivo alterado:
`/opt/data/profiles/lk-ops/scripts/lk_pos_restock_exception_monitor.py`

Mudanças:
- `http_json()` agora faz GET real em `/health`.
- `signed_noop()` agora envia payload seguro não-POS (`source_name=web`) para a rota local com assinatura Hermes.
- O handler aceita e ignora o noop, sem fila/envio cliente.
- `ensure_doppler()` exige `SHOPIFY_ACCESS_TOKEN` + `HERMES_WEBHOOK_SECRET` para o monitor local.

## Evidência

Execução manual após patch:
```text
py_compile=ok
Status: ok
Shopify POS pagos janela: 0
Último POS pago: sem registro
Último restock handler: 27/06 08:35 BRT
Gateway health: 200
Noop assinado rota POS restock: 200
Sem ação necessária. Sucesso fica local/silencioso.
values_printed=false
```

Modo cron/silent-OK:
```text
silent_stdout_bytes=0
silent_stderr_bytes=0
```

JSON mais recente:
```json
{
  "gateway_health_ok": true,
  "gateway_health_status": 200,
  "signed_noop_ok": true,
  "signed_noop_status": 200,
  "recent_paid_pos_count": 0,
  "issues": [],
  "values_printed": false
}
```

## Escopo / não feito
- Sem estoque/Tiny.
- Sem WhatsApp/backfill.
- Sem secrets impressos.
- Sem alteração Shopify/Vercel/proxy.

## Backup / rollback
Backup:
`/opt/data/backups/lk-pos-restock-exception-monitor-fix/20260627T113217Z`

Rollback:
Restaurar `lk_pos_restock_exception_monitor.py` do backup e, se necessário, `jobs.json`.
