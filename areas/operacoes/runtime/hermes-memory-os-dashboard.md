# Dashboard local — Hermes Memory OS v1

Atualizado: 2026-06-09T17:41:00Z  
Status: verde local/silent-OK com v1.1 event-aware + scorecard, v1.2 hook local, v1.3 protocolos, v1.4 wrapper, v1.5 rotinas frequentes, v1.6 linter de adoção, v1.7 checker+linter integrado, v1.8 auto-heal local limitado, v1.9 observabilidade semanal/local, v1.10 recuperação de contexto e v1.11 maturação/ciclos reais. Rotina semanal local/silent ativada. Mission Control/card visual: pendente.

## Escopo

Painel documental local da memória Hermes/Brain. Não é UI Mission Control, não substitui o Brain e não prova runtime sensível além do cron local/no_agent verificado.

## Componentes v1

- PRD: `areas/operacoes/prds/hermes-memory-os-v1-prd-2026-06-09.md`
- Rotina: `areas/operacoes/rotinas/hermes-memory-os-v1.md`
- Plano: `/opt/data/.hermes/plans/2026-06-09-hermes-memory-os-v1-implementation-plan.md`
- Watchdog boot memory: `/opt/data/scripts/hermes_memory_hygiene_watchdog.py`
- Checker/router diurno: `/opt/data/scripts/hermes_memory_os_daytime_checker.py`
- Hook local por evento: `/opt/data/scripts/hermes_memory_os_event_hook.py`
- Wrapper local de receipt: `/opt/data/scripts/hermes_memory_os_receipt_writer.py`
- Linter local de adoção: `/opt/data/scripts/hermes_memory_os_adoption_linter.py`
- Probe local de recuperação de contexto: `/opt/data/scripts/hermes_memory_os_context_recovery_probe.py`
- Probe local de maturação/ciclos reais: `/opt/data/scripts/hermes_memory_os_cycle_maturity_probe.py`
- Observabilidade semanal local/silent: `/opt/data/scripts/hermes_memory_os_weekly_observability.py`
- Latest noturno/boot: `reports/memory-hygiene/latest.json`
- Latest diurno: `reports/memory-hygiene/daytime-latest.json`
- Scorecard v1.1: `reports/memory-hygiene/scorecard-latest.json`
- Eventos recentes v1.1: `reports/memory-hygiene/events-latest.json`
- Hook latest v1.2: `reports/memory-hygiene/hook-latest.json`
- Hook log v1.2: `reports/memory-hygiene/hook-events.jsonl`
- Receipt writer latest v1.4: `reports/memory-hygiene/receipt-writer-latest.json`
- Receipt writer log v1.4: `reports/memory-hygiene/receipt-writer-events.jsonl`
- Adoption linter v1.6: `reports/memory-hygiene/adoption-latest.json`
- Adoption baseline v1.6: `reports/memory-hygiene/adoption-baseline.json`
- Observabilidade semanal v1.9: `reports/memory-hygiene/weekly-observability-latest.{json,md}`
- Maturação/ciclos reais v1.11: `reports/memory-hygiene/cycle-maturity-latest.{json,md}`
- Coverage: `areas/operacoes/runtime/hermes-profile-memory-coverage.md`
- Hot: `memories/hot.md`
- Daily: `memories/daily/2026-06-09.md`

## Estado atual

- `latest.json.status`: `ok`
- `daytime-latest.status`: `ok`
- Boot memories checadas: 28
- Over-limit: 0
- Near saturation: 0
- Template coverage missing: 0
- Provider externo de memória ativo: false
- Secret locator em memória: 0
- `hot.md`: current em 2026-06-09
- Daily 2026-06-09: curada, não skeleton
- Scorecard v1.1: 100/100, `failed_checks=[]`
- Event-aware scan: 40 artefatos recentes classificados como `approval_packet`, `handoff` ou `receipt` sem despejo de conteúdo
- Hook v1.2 testado em receipt real: `status=ok`, evento `receipt`, checker `ok`, stdout vazio quando verde
- Wrapper v1.4+ testado em receipt real: `status=ok`, campos mínimos válidos, hook/checker `ok`, stdout vazio quando verde
- Rotinas v1.10 reforçadas: receipt operacional novo deve preferir `receipt_writer`; hook é fallback para handoff, approval packet e artefatos legados/excepcionais
- Checklist Memory-vs-Brain-vs-skill codificado em protocolos canônicos: `USER.md` para preferência, `MEMORY.md` para guardrail, `hot.md` para current, daily para decisão do dia, Brain para evidência/report/receipt, skill/rotina para procedimento, fonte real para dado vivo e `session_search` para conversa antiga antes de promover
- Linter v1.6/v1.7: integrado ao checker; `daytime-latest.json.adoption_linter.status=ok`, `gap_count=0`, stdout vazio quando verde
- Auto-heal v1.8: `daytime-latest.json.adoption_auto_heal` registra tentativas locais limitadas de hook; teste sintético curou 1 gap e manteve stdout vazio
- Observabilidade v1.9: `weekly-observability-latest.json` gerado localmente; último run manual marcou `attention` por drift local `hook-only receipt` (29 receipts novos via hook em vez de `receipt_writer`), sem Telegram porque `deliver=local`/no_agent. Quando esse drift zerar, rotina volta a stdout vazio em OK.
- Recuperação de contexto v1.10: probe local/read-only disponível; verifica ponteiros hot/daily/reports/PRD/rotina/dashboard/skill sem mutação e com stdout vazio quando verde
- Maturação v1.11: `cycle-maturity-latest.json` status ok, maturidade `pilot_real_cycles`, score 100, 3/3 ciclos reais do checker diurno `bc96bb03d2b0` com envelope `silent (empty output)`; lê apenas reports sanitizados e headers/status de `/opt/data/cron/output`.
- Rotina semanal local/silent: cron `e4c6b7c9b6dc` ativo (`Hermes Memory OS weekly observability local/silent`, `45 12 * * 1`, `deliver=local`, `no_agent=true`, script `hermes_memory_os_weekly_observability.py`). Sem Telegram em OK.
- Mission Control/card visual: pendente por decisão de Lucas; sem fonte `mission-memory-os` ativa no repo local após rollback.
- Auto-compactação segura adicional: `profiles/mordomo/memories/MEMORY.md` 2015→963 chars com backup local

## Cron local/no_agent

- Daytime checker/router:
  - Nome: Hermes Memory OS daytime checker/router
  - Job ID: `bc96bb03d2b0`
  - Schedule: every 2h
  - Delivery: local
  - Script: `hermes_memory_os_daytime_checker.py`
  - Contrato: stdout vazio quando verde; stdout apenas para alerta acionável.
- Weekly observability:
  - Nome: Hermes Memory OS weekly observability local/silent
  - Job ID: `e4c6b7c9b6dc`
  - Schedule: `45 12 * * 1`
  - Delivery: local
  - Script: `hermes_memory_os_weekly_observability.py`
  - Contrato: local/no_agent, stdout vazio quando verde; sem Telegram em OK.

## Guardrails preservados

- Nenhum Docker/VPS/Traefik/gateway/container/restart.
- Nenhum provider externo/Mem0/Honcho ativado.
- Nenhum write em Shopify/Tiny/GMC/Klaviyo/Meta/WhatsApp/e-mail/banco.
- Nenhum secret impresso ou copiado.
- Telegram permanece silent-OK; Lucas só recebe exceção/decisão/falha/resumo solicitado.
- Sem Telegram de OK técnico: wrapper/hook/linter/checker verdes ficam locais; alertas só quando acionáveis.

## Próxima evolução possível

- v1.1 executada: scan event-aware local + scorecard JSON, sem Telegram em sucesso.
- v1.2 executada: hook local explícito por artifact path, chamável por agentes/rotinas após receipts/handoffs materiais.
- v1.3 executada: templates/protocolos canônicos de receipt/handoff instruem a chamada do hook.
- v1.4 executada: wrapper/gerador local de receipt valida campos mínimos, salva o receipt e chama hook automaticamente.
- v1.5 executada: wrapper integrado nas rotinas frequentes de receipt/handoff para virar caminho padrão operacional.
- v1.6 executada: linter local mede adoção real e aponta receipts/handoffs/approval-packets recentes sem wrapper/hook.
- v1.7 executada: linter integrado ao checker diurno/cron local existente, sem mudar schedule/delivery.
- v1.8 executada: auto-heal local limitado para gaps vencidos, com supressão de recursão e sem conteúdo de artefato.
- v1.9 executada: relatório semanal/local de tendência e adoção, sem cron novo e sem Telegram.
- Mission Control/card visual: pendente; retomar somente em rodada dedicada.
- Próximo: operar por ciclos reais; Mission Control/card visual read-only fica pendente e fora do escopo atual.

## v1.13 — ativação local 30min + alertas acionáveis + todos agentes/workers (2026-06-09)

Decisão Lucas:
- Memory OS daytime checker ativo a cada 30 minutos.
- OK permanece silencioso.
- Quando houver problema, o watcher tenta auto-heal local primeiro.
- Se corrigir, avisa Lucas com resumo curto: problema detectado, corrigido, nenhuma ação necessária.
- Se não corrigir e precisar de decisão humana, pergunta a Lucas o que fazer.
- Todos os `AGENTS.md` do Brain receberam contrato v1.13: receipts novos via `hermes_memory_os_receipt_writer.py`; workers legados devem usar `hermes_memory_os_worker_receipt_guard.py`/`--register-existing`; handoffs/approval packets seguem via hook.
- Mission Control não será usado como superfície operacional do Memory OS.

Estado de ativação:
- cron `bc96bb03d2b0`: `every 30m`, `deliver=origin`, `no_agent=true`, script `hermes_memory_os_daytime_alerting_watchdog.py`; stdout vazio = sem Telegram; stdout não vazio = alerta acionável.
- cron `e4c6b7c9b6dc`: observabilidade semanal local/silent mantida.
- helper worker: `/opt/data/scripts/hermes_memory_os_worker_receipt_guard.py`.

