# Hermes Webhooks — Shopify POS restock route secret alignment — 2026-06-24

## Resultado

Correção aplicada no escopo aprovado por Lucas.

- Rota: `lk-shopify-pos-restock`
- Config alterada: `secret_doppler: WEBHOOK_SECRET` → `secret_doppler: HERMES_WEBHOOK_SECRET`
- Runtime verificado: gateway default reiniciado e webhook/API saudáveis
- Probe Shopify no-op: `HTTP 200`, `status=ignored`, `reason=not_paid_active_pos_order`, `topic=orders/paid`
- Writes externos/deploys/providers: `0`
- Secrets impressos: `0`; `values_printed=false`

## Evidência de verificação

- `hermes config check`: OK
- `py_compile`: OK para handler POS, probes temporários, adaptador webhook instalado e entrypoint do Hermes venv
- Health local: `http://127.0.0.1:8644/health` OK e `http://127.0.0.1:8642/health` OK
- Log runtime: gateway voltou com 3 plataformas e webhook conectado
- Probe assinado Shopify via Vercel custom domain: `HTTP 200` / `ignored`
- Fila POS thank-you: `probe_jobs_count=0`

## Observações de runtime

Durante a ativação apareceu drift entre fonte Hermes e pacote instalado no venv ativo: o adaptador instalado não tinha ainda suporte efetivo a `secret_doppler` por rota nem `run_script` no caminho ativo. Para cumprir o escopo aprovado e deixar a rota operando, foi aplicado patch local no runtime instalado, com backups.

Backups criados em:

- `/opt/data/backups/hermes-webhooks-shopify-route-secret-alignment-20260624T233018Z/`
- `/opt/data/backups/hermes-webhooks-shopify-runtime-injection-retry-20260624T233648Z/`

## Rollback

Se necessário, restaurar:

1. `/opt/data/config.yaml` a partir do backup `config.yaml.before`;
2. `/opt/data/hermes-0.15.1-venv/bin/hermes` a partir de `hermes-bin.before`;
3. `/opt/data/hermes-0.15.1-venv/lib/python3.13/site-packages/gateway/platforms/webhook.py` a partir de `site-webhook.py.before`;
4. reiniciar/verificar gateway default;
5. repetir health check e probe no-op.

## Escopo preservado

Não houve deploy Vercel, alteração Shopify Admin/webhooks, alteração de secrets/env no Doppler/Vercel, envio WhatsApp/e-mail/campanha ou write externo.
