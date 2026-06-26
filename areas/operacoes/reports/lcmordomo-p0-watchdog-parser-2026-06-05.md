# LC Mordomo OS — P0 Watchdog e Parser `wacli --json`

**Data:** 2026-06-05  
**Escopo:** P0 de blindagem dos crons críticos de follow-up/e-mail e parser robusto para stdout misto do `wacli --json`.  
**Modo:** local/reversível; sem envio externo; sem Docker/VPS/restart/deploy; sem banco de produção.

## 1. Problema fechado

Falhas de cron/follow-up não podiam depender de Lucas perceber stack trace no Telegram. Além disso, scripts que usam `wacli --json` podiam quebrar quando o CLI imprimia logs/diagnósticos junto com o JSON final.

Classe de risco tratada:

- cron crítico pausado/falhando sem aviso limpo;
- `JSONDecodeError` pós-envio ou pós-leitura;
- potencial retry inseguro se stdout misto fosse interpretado como falha de envio;
- alertas técnicos crus em vez de pacote limpo.

## 2. Arquivos alterados/criados

Runtime Mordomo:

- `/opt/data/profiles/mordomo/scripts/mordomo_json_utils.py`
  - helper comum `parse_mixed_json()` e `wacli_data()`;
  - tolera logs antes/depois do JSON;
  - prefere payload top-level com `success` em vez de objeto aninhado `{id: ...}`.

- `/opt/data/profiles/mordomo/scripts/mordomo_whatsapp_global_watch.py`
  - leituras `wacli --json` de chats/mensagens/contexto/mídia passam a usar parser tolerante.

- `/opt/data/profiles/mordomo/scripts/zipper_whatsapp_response_watch.py`
  - leituras `wacli --json` de chats/mensagens passam a usar parser tolerante.

- `/opt/data/profiles/mordomo/scripts/lcmordomo_critical_cron_watchdog.py`
  - novo watchdog local/no-agent;
  - stdout vazio quando OK;
  - stdout limpo apenas se houver auto-correção local ou pendência técnica;
  - report local em `/opt/data/profiles/mordomo/cron/output/lcmordomo_critical_cron_watchdog.json`.

Cron registry:

- `/opt/data/profiles/mordomo/cron/jobs.json`
  - novo job `LC Mordomo OS critical cron watchdog`;
  - `id`: `lcmcw202606`;
  - frequência: every 10m;
  - `no_agent=true`;
  - `deliver=local`;
  - sem Telegram em sucesso rotineiro.

## 3. Crons críticos monitorados

O watchdog verifica:

1. `Mordomo global WhatsApp watcher — Lucas pessoal`
   - ID: `6f4c913082db`;
   - script esperado: `mordomo_whatsapp_global_watch.py`;
   - tolerância de atraso: 20 min.

2. `ZPR Enquiry Form watcher — approval-gated`
   - ID: `871b9bc5617a`;
   - script esperado: `zipper_zpr_enquiry_watcher.py`;
   - tolerância de atraso: 20 min.

3. `Zipper direct main e-mail monitor — zipper@zippergaleria.com.br`
   - ID: `20972b3c7595`;
   - script esperado: `zipper_main_email_monitor.py`;
   - tolerância de atraso: 180 min.

## 4. Self-heal permitido

Permitido automaticamente:

- se job crítico estiver `enabled=false` ou `state!=scheduled`, o watchdog reativa localmente:
  - `enabled=true`;
  - `state=scheduled`;
  - limpa `paused_at`/`paused_reason`;
  - recalcula `next_run_at` pelo intervalo do próprio job.

Não permitido:

- Docker/VPS/restart;
- deploy;
- banco de produção;
- envio WhatsApp/e-mail;
- mudança de script divergente;
- correção de erro funcional sem análise.

Nesses casos, ele gera alerta técnico limpo.

## 5. Verificação executada

Comandos executados:

```bash
python3 -m py_compile \
  /opt/data/profiles/mordomo/scripts/mordomo_json_utils.py \
  /opt/data/profiles/mordomo/scripts/mordomo_whatsapp_global_watch.py \
  /opt/data/profiles/mordomo/scripts/zipper_whatsapp_response_watch.py \
  /opt/data/profiles/mordomo/scripts/zipper_zpr_enquiry_watcher.py \
  /opt/data/profiles/mordomo/scripts/lcmordomo_critical_cron_watchdog.py
```

Resultado: OK.

Fixtures do parser:

- JSON limpo com `success:true`: OK;
- logs antes do JSON final: OK;
- objeto aninhado `{id: ...}` antes do payload `success:true`: OK;
- payload lista com logs antes: OK.

Watchdog dry-run:

- `actions`: `[]`;
- `alerts`: `[]`;
- `changed`: `false`.

Watchdog real-run:

- `actions`: `[]`;
- `alerts`: `[]`;
- `changed`: `false`.

Snapshot dos críticos na verificação:

- WhatsApp watcher pessoal: enabled/scheduled/ok;
- ZPR watcher: enabled/scheduled/ok;
- Zipper e-mail principal: enabled/scheduled/ok.

## 6. Estado final

P0 implementado para:

- blindagem de parada silenciosa dos crons críticos;
- parser comum para stdout misto do `wacli --json` nos watchers ativos;
- contrato silencioso em sucesso;
- alerta técnico limpo em falha real.

## 7. Próximo passo recomendado

Próxima frente: **P1 Zipper MVP runtime → objetos canônicos**.

Objetivo: reduzir dependência de JSON solto e scripts caso-a-caso, promovendo estados para:

- contact;
- lead/enquiry;
- artist_interest;
- followup;
- suppression;
- sent_action;
- decision_packet.
