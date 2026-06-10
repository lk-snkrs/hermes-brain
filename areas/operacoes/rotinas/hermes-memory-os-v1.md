# Rotina — Hermes Memory OS v1

Status: PRD/R&D aprovado; Fases 1–4 + v1.1 event-aware/scorecard + v1.2 hook local + v1.3 protocolos + v1.4 wrapper + v1.5 rotinas frequentes + v1.6 linter de adoção + v1.7 integração ao checker diurno + v1.8 auto-heal local limitado + v1.9 observabilidade semanal/local + v1.10 probe de recuperação de contexto + v1.11 maturação/probe de ciclos reais executados em escopo seguro/local, com checker diurno no_agent local ativo e rotina semanal local/silent ativada. Mission Control/card visual permanece pendente.  
Owner: LC Hermes / Hermes Agent central.  
Criado em: 2026-06-09.

## Função

Manter a memória Hermes viva durante o dia, não apenas no fechamento noturno.

A rotina fecha o loop:

`evento → roteamento de memória → camada correta → compactação preventiva → daily/hot → receipt_writer/hook → verificação → Telegram só se acionável`.

## Artefatos canônicos

- PRD: `areas/operacoes/prds/hermes-memory-os-v1-prd-2026-06-09.md`
- Plano: `/opt/data/.hermes/plans/2026-06-09-hermes-memory-os-v1-implementation-plan.md`
- Política: `memories/politica-memoria-hermes.md`
- Hot current: `memories/hot.md`
- Daily: `memories/daily/YYYY-MM-DD.md`
- Watchdog atual: `/opt/data/scripts/hermes_memory_hygiene_watchdog.py`
- Checker/router diurno: `/opt/data/scripts/hermes_memory_os_daytime_checker.py`
- Hook local por evento: `/opt/data/scripts/hermes_memory_os_event_hook.py`
- Wrapper local de receipt: `/opt/data/scripts/hermes_memory_os_receipt_writer.py`
- Linter local de adoção: `/opt/data/scripts/hermes_memory_os_adoption_linter.py`
- Probe local de recuperação de contexto: `/opt/data/scripts/hermes_memory_os_context_recovery_probe.py`
- Probe local de maturação/ciclos reais: `/opt/data/scripts/hermes_memory_os_cycle_maturity_probe.py`
- Observabilidade semanal local/silent: `/opt/data/scripts/hermes_memory_os_weekly_observability.py`
- Latest report: `reports/memory-hygiene/latest.json`
- Daytime latest: `reports/memory-hygiene/daytime-latest.json`
- Scorecard v1.1: `reports/memory-hygiene/scorecard-latest.json`
- Eventos v1.1: `reports/memory-hygiene/events-latest.json`
- Hook latest v1.2: `reports/memory-hygiene/hook-latest.json`
- Hook log v1.2: `reports/memory-hygiene/hook-events.jsonl`
- Receipt writer latest v1.4: `reports/memory-hygiene/receipt-writer-latest.json`
- Receipt writer log v1.4: `reports/memory-hygiene/receipt-writer-events.jsonl`
- Adoption linter v1.6: `reports/memory-hygiene/adoption-latest.json`
- Adoption baseline v1.6: `reports/memory-hygiene/adoption-baseline.json`
- Observabilidade semanal v1.9: `reports/memory-hygiene/weekly-observability-latest.{json,md}` e `reports/memory-hygiene/weekly-observability-events.jsonl`
- Maturação/ciclos reais v1.11: `reports/memory-hygiene/cycle-maturity-latest.{json,md}` e `reports/memory-hygiene/cycle-maturity-events.jsonl`
- Coverage: `areas/operacoes/runtime/hermes-profile-memory-coverage.md`
- Dashboard local: `areas/operacoes/runtime/hermes-memory-os-dashboard.md`

## Gatilhos

- Boot memory > 80%: registrar risco local e avaliar compactação.
- Boot memory > 85% com template seguro: backup + compactação local.
- Boot memory over-limit: corrigir antes de alertar, se seguro.
- Profile com memory file sem template: abrir gap e criar template mínimo quando local/seguro.
- `hot.md` stale ou com claim operacional falso: refresh.
- Daily skeleton após evento material: curar daily.
- Lucas corrige regra/memória/roteamento: promover para política, daily/hot, skill ou PRD.
- Receipt operacional novo: preferir `/opt/data/scripts/hermes_memory_os_receipt_writer.py` para salvar no Brain, validar campos mínimos e chamar o hook em uma única operação local.
- Handoff/approval-packet/artefato legado recente: chamar `/opt/data/scripts/hermes_memory_os_event_hook.py <path>` após criar/editar, para classificar localmente como evento de contexto e validar se hot/daily continuam coerentes.
- Rotinas frequentes de receipt/handoff devem apontar explicitamente para wrapper/hook, para evitar que subagentes fechem trabalho material sem Memory OS.
- Linter de adoção deve verificar artefatos recentes após baseline v1.6 e apontar gap local se algum receipt/handoff/approval-packet não tiver evidência de wrapper/hook.

## Checklist canônico de roteamento de memória

Aplicar antes de gravar contexto novo:

- Preferência durável do usuário/Lucas → `USER.md` curto do profile relevante.
- Guardrail global, regra de segurança ou política de boot → `MEMORY.md` curto, com ponteiro para Brain se precisar de detalhe.
- Prioridade, bloqueio ou estado current → `memories/hot.md`.
- Decisão, entrega ou pendência do dia → `memories/daily/YYYY-MM-DD.md`.
- Evidência, relatório, auditoria, receipt ou output material → Brain receipt/report/área dona.
- Procedimento reutilizável ou rotina repetível → skill, referência de skill ou rotina canônica.
- Dado vivo → fonte real primeiro; Brain guarda ponteiro, receipt/report e timestamp/incerteza.
- Conversa antiga → `session_search`; promover somente se for durável/reutilizável.

Anti-drift: `USER.md`/`MEMORY.md` são boot mínimo, `hot.md` é current, daily é continuidade do dia, Brain é memória rica/evidência, skills são procedimento e fonte viva continua fora do Brain.

## Contrato de segurança

Permitido automaticamente:

- docs Brain locais;
- backups locais de memory files;
- compactação local de boot memory com template seguro;
- receipts sanitizados;
- scans/parse/py_compile;
- daily/hot refresh local.

Bloqueado sem aprovação escopada:

- Docker/VPS/Traefik/gateway/restart;
- cron produtivo novo ou alteração de delivery;
- provider externo de memória;
- Shopify/Tiny/GMC/Klaviyo/Meta/WhatsApp/e-mail/banco;
- secrets ou credential injection.

## Telegram

Silent-OK. Enviar para Lucas apenas quando:

- a correção local falhou;
- há over-limit sem template seguro;
- provider externo apareceu ativo;
- há secret locator;
- precisa de decisão para agendar/alterar runtime.

## Execução atual — 2026-06-09T13:49:20Z

- Fase 1: templates/compactação/cobertura concluídos.
- Fase 2: checker/router diurno local criado com `--dry-run`, modo auto-heal local e contrato silent-OK.
- Fase 3: cron local/no_agent a cada 2h criado com `deliver=local`; stdout vazio em sucesso.
- Fase 4: dashboard local documental criado; Mission Control UI permanece futuro, sem runtime/UI deploy.
- v1.1: event-aware scan + scorecard local adicionados; scorecard atual 100/100, sem failed checks.
- v1.2: hook local explícito criado; teste em receipt real retornou `status=ok`, `checker=ok`, stdout vazio quando verde.
- v1.3: templates/protocolos canônicos de receipt/handoff agora exigem chamada do hook após artefato material.
- v1.4: wrapper local de receipt criado; valida campos mínimos, salva no Brain, chama hook e mantém evidência `receipt-writer-latest.json`.
- v1.5: protocolos/checklists/templates frequentes de receipt/handoff agora apontam para wrapper como caminho preferencial e hook como fallback obrigatório.
- v1.6: linter local de adoção criado; gaps recentes detectados foram fechados localmente com hook; linter usa graça padrão de 5 minutos contra corrida com artefatos ainda ativos e voltou a silent-OK.
- v1.7: checker diurno chama linter em modo baseline, propaga gaps como rota local e permanece stdout vazio quando verde.
- v1.8: checker fecha gaps vencidos seguros rodando hook local limitado; teste sintético confirmou `healed=1`, linter verde e stdout final vazio.
- v1.9: relatório semanal/local resume saúde atual, histórico de gaps, hooks, wrapper e áreas top; verde não imprime stdout nem envia Telegram.
- v1.10: probe local/read-only de recuperação de contexto criado em `/opt/data/scripts/hermes_memory_os_context_recovery_probe.py`; verifica se um agente pós-perda de contexto consegue reidratar Memory OS por ponteiros de `hot.md`, daily do dia, `reports/memory-hygiene/*latest.json`, PRD/rotina/dashboard e skill, sem mutação runtime/externa e com stdout vazio quando verde.
- v1.11: probe local/read-only de maturação/ciclos reais criado em `/opt/data/scripts/hermes_memory_os_cycle_maturity_probe.py`; lê apenas reports sanitizados e envelopes locais de cron (`/opt/data/cron/output/bc96bb03d2b0/*.md`) para provar ciclos reais. Resultado atual: `pilot_real_cycles`, 3/3 ciclos diurnos silent-OK, score 100, rotina semanal local/silent ativada no cron `e4c6b7c9b6dc` (`45 12 * * 1`, `deliver=local`, `no_agent=true`).
- v1.11: `/opt/data/scripts/hermes_memory_os_weekly_observability.py` agora refresca o probe de maturação após gerar a observabilidade semanal; permanece local/no_agent e não envia Telegram em OK.
- Pendente: Mission Control/card visual read-only para Memory OS foi retirado do escopo atual por Lucas; retomar apenas em rodada dedicada.

## Scorecard

Verde quando:

- `latest.json.status=ok`;
- over-limit count = 0;
- near saturation count = 0 ou justificável;
- missing template coverage = 0;
- `hot.md` current;
- daily do dia curada se houve evento material;
- provider externo off;
- focused secret scan = 0;
- `scorecard-latest.json.status=ok` e score >= 90;
- eventos recentes classificados sem despejo bruto de conteúdo;
- hook local por evento retorna `status=ok` e stdout vazio quando verde;
- wrapper local de receipt retorna `status=ok`, campos mínimos válidos e stdout vazio quando verde;
- rotinas frequentes de receipt/handoff apontam para `receipt_writer` como caminho preferencial para receipt novo e hook como fallback para handoff/approval-packet/legado, reduzindo drift de adoção;
- Linter v1.6 retorna `status=ok`, `gap_count=0` e stdout vazio quando verde.
- Checker v1.7 incorpora o linter e grava `adoption_linter` no `daytime-latest.json`; o scorecard inclui `adoption_linter_ok`.
- Checker v1.8 tenta auto-heal local limitado de gaps vencidos com hook, sem ler conteúdo, com supressão de recursão e `--adoption-auto-heal-limit`.
- Observabilidade v1.9 gera relatório local semanal em `reports/memory-hygiene/weekly-observability-latest.{json,md}` a partir de logs sanitizados.
- Probe v1.10 retorna `status=ok`, `missing_paths=[]`, `attention=[]`, ponteiros essenciais presentes e stdout vazio sem `--json`; saída JSON sanitizada disponível com `--json`.
- Probe v1.11 retorna `status=ok`, maturidade `pilot_real_cycles` ou superior, ciclos reais recentes em `bc96bb03d2b0` com envelope `silent (empty output)`, reports core sanitizados verdes e rotina semanal `deliver=local/no_agent`; saída padrão vazia quando não houver finding acionável.

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



## v1.18 — Readiness pós-rollout profile-local

- Após `Seguir o PRD`, executar readiness audit read-only/sanitizada antes de qualquer runtime mutation.
- Se o checker apontar drift local corrigível (`hot.md` stale, daily ausente/skeleton), corrigir localmente antes de alertar Lucas.
- Não classificar profiles explicitamente excluídos do watchdog como managed failure.
- Próximo estado verde volta para maturação por ciclos reais; restart/gateway/Docker/VPS/Traefik/Mission Control exigem aprovação separada.
