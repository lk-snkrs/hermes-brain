# Receipt — LK Tiny Local Stock DB Phase A Runtime Restart

Timestamp: 2026-05-26T17:56:00+00:00
Owner: LK Ops / Atendimento
Executor: Hermes local
Approval: Lucas aprovou seguir nesta conversa.

## Ação executada

Reiniciado o responder LK WhatsApp/Telegram local para carregar a Fase A do Tiny Local Stock DB.

## Processo

- Processo anterior: PID `239405`, comando `python3 /opt/data/scripts/lk_hermes_whatsapp_responder.py --port 8787`.
- Ação: `kill 239405`.
- Novo processo: PID `246653`, comando `python3 /opt/data/scripts/lk_hermes_whatsapp_responder.py --port 8787`.

## Verificação

1. Syntax check antes do restart:

```bash
python3 -m py_compile /opt/data/scripts/lk_tiny_stock_local_db.py /opt/data/scripts/lk_hermes_whatsapp_responder.py /opt/data/scripts/lk_shopify_tiny_stock_sync_dryrun.py
```

Resultado: exit 0.

2. Processo ativo:

```text
PID 246653 python3 /opt/data/scripts/lk_hermes_whatsapp_responder.py --port 8787
```

3. Health local via POST vazio, sem envio externo:

```text
http://127.0.0.1:8787/ -> status 200, body ok
```

4. Smoke CLI local, sem envio externo:

```bash
python3 /opt/data/scripts/lk_hermes_whatsapp_responder.py --ask '@Hermes cliente quer Onitsuka Tiger Mexico 66 38, o que temos?' --stock-only --json-output
```

Resultado: exit 0. Resposta usou `Tiny local snapshot`, incluiu `Última leitura oficial Tiny: 2026-05-26T17:54:41.199226+00:00`, SKU `1183C102250-5`, saldo 3.

5. Log de runtime:

`events.ndjson` registrou `service_started` em `2026-05-26T17:56:00.910921+00:00` na porta `8787`.

## Guardrails

- Nenhuma escrita em Shopify.
- Nenhuma escrita em Tiny.
- Nenhum webhook/crontab criado.
- Nenhuma mensagem externa enviada manualmente no smoke.
- Serviço existente foi apenas reiniciado com o código local aprovado.

## Rollback

Se houver anomalia operacional:

1. Encerrar PID `246653`.
2. Reverter chamadas novas no responder/processor ou restaurar snapshot de arquivo anterior, se disponível.
3. Reiniciar `python3 /opt/data/scripts/lk_hermes_whatsapp_responder.py --port 8787`.
4. A base local pode ser movida para backup: `/opt/data/hermes_bruno_ingest/local_sql/lk_whatsapp_hermes/lk_tiny_stock_local.sqlite`.
