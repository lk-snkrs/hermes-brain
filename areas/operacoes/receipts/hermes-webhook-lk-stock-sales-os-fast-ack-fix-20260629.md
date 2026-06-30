# Receipt — Hermes webhook `lk-stock-shopify-sales-os` fast-ack containment

- Data: 2026-06-29
- Dono: Operações Hermes / LK Stock
- Classificação: local-runtime-script fix + produção webhook route containment
- Pedido/gatilho: Lucas trouxe diagnóstico do Codex: Telegram gateway travou; restart limpou; logs apontavam timeouts repetidos no webhook `lk-stock-shopify-sales-os` executando `/opt/data/scripts/lk_shopify_sales_os_webhook_ingest.py`.

## Evidência antes

- Gateway principal estava vivo após restart do container: Telegram connected, API health 200, webhook health 200.
- Logs locais confirmaram repetidos:
  - `script timeout route=lk-stock-shopify-sales-os script=/opt/data/scripts/lk_shopify_sales_os_webhook_ingest.py`
  - timeout do subprocess após 60s.
- `ps` mostrou processos órfãos do filho pesado:
  - `/opt/data/profiles/lk-stock/scripts/lk_shopify_sales_os_supabase_direct.py`
  - alguns com `--_doppler_injected`.
- Root cause: o wrapper do webhook chamava sincronização completa Shopify Admin GraphQL -> Supabase de forma síncrona; essa rotina pode levar minutos e era acionada por eventos Shopify frequentes.

## O que foi alterado

- Backup criado em:
  - `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/stock/backups/sales-os-webhook-runaway-20260629T143336Z/`
- Script alterado:
  - `/opt/data/scripts/lk_shopify_sales_os_webhook_ingest.py`
- Novo comportamento:
  - webhook consome stdin e registra apenas trigger local compacto (`payload_sha256`, bytes, rota, evento, delivery id);
  - retorna JSON em segundos (`fast_ack_background_refresh`);
  - sync completo roda somente em runner background com lock e cooldown;
  - evita múltiplos reconciles concorrentes;
  - relatório/log sanitizados em `/opt/data/profiles/lk-stock/runtime/`.
- Processos órfãos do sync antigo foram terminados por correspondência exata de comando.
- Skill `webhook-subscriptions` atualizada com referência reutilizável:
  - `references/hermes-webhook-script-runaway-fast-ack.md`.

## Guardrails

- Não houve Docker/VPS/Traefik/compose change.
- Não houve restart adicional do gateway/container por este agente.
- Não houve mutation Shopify/Tiny.
- Teste local foi feito com background desabilitado para não disparar reconcile externo manual.
- `values_printed=false`; nenhum token/secret/HMAC/payload sensível impresso.

## Verificações executadas

- `python3 -m py_compile /opt/data/scripts/lk_shopify_sales_os_webhook_ingest.py` passou.
- Teste local com `LK_SHOPIFY_SALES_OS_WEBHOOK_DISABLE_BACKGROUND=1` retornou `status=accepted` e `mode=fast_ack_background_refresh`.
- Após contenção, `ps` retornou `no_direct_sync_processes` para o script pesado.
- Após espera superior ao intervalo anterior de timeout, logs não tiveram novas linhas `lk-stock-shopify-sales-os` desde o patch.

## Rollback

Restaurar backup:

```bash
cp /opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/stock/backups/sales-os-webhook-runaway-20260629T143336Z/lk_shopify_sales_os_webhook_ingest.py.before /opt/data/scripts/lk_shopify_sales_os_webhook_ingest.py
chmod 0755 /opt/data/scripts/lk_shopify_sales_os_webhook_ingest.py
python3 -m py_compile /opt/data/scripts/lk_shopify_sales_os_webhook_ingest.py
```

Rollback reintroduz o risco de timeout síncrono; usar só se o fast-ack quebrar a rota.

## Próximos passos recomendados

1. Observar o próximo evento real Shopify ou o próximo ciclo de sync para confirmar runner background/cron saudável.
2. Se houver nova falha, manter rota fast-ack e corrigir o direct sync/cron separadamente, sem bloquear Telegram.
3. Em etapa posterior, considerar separar definitivamente: webhooks só enfileiram triggers; cron/worker dedicado consome fila e atualiza Supabase.
