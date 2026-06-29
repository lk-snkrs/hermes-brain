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

## Memory OS v1.20 — contrato anti-recorrência auto-heal

- Auto-heal recorrente não deve virar normalidade invisível: se a mesma rota/reason cura `>= 3` vezes em 7 dias, registrar `auto-heal-generator-findings-latest.json` e corrigir o gerador local/documental quando seguro.
- Rotas recorrentes atuais: adoption_auto_heal, daily_curator.
- Escopo automático permitido: L0/L1 local/documental com backup/ledger/verificação; L2 requer aprovação; L3 é proibido automático.
- Telegram permanece silencioso se o estado final ficou verde; alertar Lucas apenas quando sobrar problema acionável ou decisão L2.
## Memory OS v1.30 — Context Intelligence Layer

- Objetivo: transformar higiene de memória em roteamento determinístico de contexto por pergunta/tarefa antes de responder ou delegar.
- Entregas locais/documentais aprovadas: Context Router, `context/current/*.md`, testes sintéticos de recall e `context/packs/*.json` para subagentes.
- Script: `/opt/data/scripts/hermes_memory_os_context_intelligence.py`.
- Relatório live/documental: `reports/memory-hygiene/context-intelligence-latest.json`.
- Testes sintéticos: `reports/memory-hygiene/context-recall-tests-v130.json` e `/opt/data/tests/test_memory_os_context_intelligence_v130.py`.
- Regra de uso: perguntas críticas (`qual 2/2?`, `está ativo?`, `já aprovou?`, `o que ficou pendente?`, `pode executar?`) devem passar pelo Context Router e consultar ledger/current/report antes de resposta final.
- Guardrail: v1.30 não autoriza runtime, gateway, cron, provider, Telegram delivery, Docker/VPS ou writes externos; é camada local de contexto e teste.

## Memory OS v1.40 — Evidence & Sufficiency Layer

- Objetivo: impedir respostas confiantes com contexto insuficiente, especialmente em perguntas `está ativo?`, `qual 2/2?`, `já aprovou?`, `pode executar?` e fatos vivos de negócio.
- Entregas locais/documentais aprovadas: Evidence Ladder, Context Sufficiency Score, TTL por classe de fonte e classes de erro operacional aprendíveis.
- Script: `/opt/data/scripts/hermes_memory_os_context_intelligence.py` agora retorna `evidence_ladder`, `context_sufficiency`, `ttl_policy` e `operational_error_classes` junto do plano de contexto.
- Relatório live/documental: `reports/memory-hygiene/context-intelligence-latest.json`, versão `v1.40`.
- Testes sintéticos: `reports/memory-hygiene/context-recall-tests-v140.json` e `/opt/data/tests/test_memory_os_evidence_sufficiency_v140.py`.
- Evidence Ladder canônica: runtime/live quando a pergunta é status ativo; ledger/receipt para decisões e N/M; current state como ponte; Brain MAPA/skills/session history/chat summary apenas em ordem decrescente de confiança.
- TTL: status runtime e fatos vivos exigem evidência fresca; política/guardrail é durável; chat summary/prompt memory é apenas pista, nunca verdade final.
- Guardrail: v1.40 é local/documental + testes; não ativa provider externo, não altera gateway/runtime/crons/Telegram e não executa writes em Shopify/Tiny/GMC/Klaviyo/WhatsApp/e-mail/banco.

## Memory OS v1.50 — Contradiction Detector + Current State TTL Enforcement

- Objetivo: detectar conflitos explícitos entre current/runtime/reports e bloquear claims de estado atual quando a evidência está vencida.
- Entregas locais/documentais aprovadas: detector de contradições por claim marker, enforcement de TTL para evidências voláteis, fixture `context-ttl-tests-v150.json` e relatório `context-contradictions-latest.json`.
- Script: `/opt/data/scripts/hermes_memory_os_context_intelligence.py` agora expõe `detect_context_contradictions(brain)` e `enforce_ttl_for_plan(plan, evidence)`.
- Relatório live/documental: `reports/memory-hygiene/context-intelligence-latest.json`, versão `v1.50`, com `contradiction_scan.status=ok` quando não há conflito explícito.
- Testes: `/opt/data/tests/test_memory_os_contradiction_ttl_v150.py` cobre conflito `active/offline`, ausência de falso positivo em context pointer, runtime stale bloqueado e runtime fresco permitido.
- Regra de uso: claims `active/online/offline`, preço/estoque/status vivo e health atual devem passar por TTL enforcement antes de resposta final; se bloqueado, responder com necessidade de evidência fresca, não com certeza.
- Guardrail: v1.50 não autoriza runtime, gateway, cron, provider, Telegram delivery, Docker/VPS ou writes externos; é camada local/documental + testes.

## Memory OS v1.60 — Decision Continuity Ledger

- Objetivo: preservar continuidade de decisões sequenciais (`1/N`, `2/N`, “Fazer”, “Não fazer”, “APROVO”) sem depender de chat summary ou memória compactada.
- Entregas locais/documentais aprovadas: helpers de ledger JSONL append-only, normalização de resposta Lucas, resolução determinística de `N/M`, gate anti-approval-scope-drift e fixture `decision-continuity-tests-v160.json`.
- Script: `/opt/data/scripts/hermes_memory_os_context_intelligence.py` agora expõe `write_decision_sequence_ledger`, `resolve_decision_sequence_query`, `record_lucas_decision_response`, `approval_scope_gate` e `load_decision_sequence_state`.
- Relatório live/documental: `reports/memory-hygiene/context-intelligence-latest.json`, versão `v1.60`, com entregas `decision_continuity_ledger` e `approval_scope_gate`.
- Testes: `/opt/data/tests/test_memory_os_decision_continuity_v160.py` cobre criação append-only de sequência, resolução `2/2` via ledger, “não fazer” limitado ao item aberto, bloqueio de aprovação genérica/high-risk e bootstrap v1.60.
- Regra de uso: perguntas Mesa COO `qual N/M?` devem ler ledger primeiro; “APROVO”/“Fazer” só vale para o item atual e ação escopada; produção/runtime/external write continua bloqueado sem aprovação específica.
- Guardrail: v1.60 não autoriza runtime, gateway, cron, provider, Telegram delivery, Docker/VPS ou writes externos; é camada local/documental + testes.

## Memory OS v1.70 — Subagent Context Contract v2

- Objetivo: padronizar o pacote de contexto entregue a subagentes para evitar prompt gigante, fonte errada, chat summary como verdade, claims runtime sem evidência e execução fora do approval scope.
- Entregas locais/documentais aprovadas: `build_subagent_context_contract`, `validate_subagent_context_contract`, `create_subagent_handoff_packet`, fixture `subagent-context-contract-tests-v170.json` e report `context-intelligence-latest.json` versão `v1.70`.
- Contrato v2: orçamento máximo de fontes/tokens, `current_state` obrigatório, `never_do` explícito, gates `return_evidence_paths`, `do_not_claim_runtime_without_live_evidence`, `approval_scope_check` e output schema mínimo.
- Handoff packet: inclui truth policy (`chat_summary=hint_only`, runtime/live source required), stop conditions e expected output com evidências/incertezas/ações não tomadas.
- Testes: `/opt/data/tests/test_memory_os_subagent_context_contract_v170.py` cobre contrato budgetado, validação de guardrails, bloqueio de A3/A4 sem approval packet, handoff sem raw chat summary e bootstrap v1.70.
- Regra de uso: antes de delegar trabalho sensível/operacional a subagente, montar contrato v2 e bloquear se faltarem current state, guardrails, evidence return ou approval packet para A3/A4.
- Guardrail: v1.70 não autoriza runtime, gateway, cron, provider, Telegram delivery, Docker/VPS ou writes externos; é camada local/documental + testes.

## Memory OS v1.80 — Silent-OK Self-Test Contract

- Objetivo: permitir um self-test diário/no_agent que valide a saúde local do Memory OS sem gerar ruído quando tudo está verde.
- Entregas locais/documentais aprovadas: `run_memory_os_self_test`, `format_memory_os_self_test_stdout`, CLI `--self-test`, fixture `self-test-contract-v180.json` e report `context-intelligence-latest.json` versão `v1.80`.
- Contrato silent-OK: se `status=ok`, stdout é exatamente vazio; se houver falha local, stdout contém alerta sanitizado/actionable com nomes dos checks e ação sugerida.
- Checks atuais: `context_intelligence_latest`, `contradiction_scan_ok`, `ttl_fixture`, `decision_continuity_fixture`, `subagent_contract_fixture`, `recall_fixture`, `current_state_memory_os`.
- Testes: `/opt/data/tests/test_memory_os_selftest_silent_ok_v180.py` cobre self-test saudável silencioso, alerta quando fixture falta, formatador stdout e CLI `--self-test` silencioso.
- Regra de uso: qualquer cron/no_agent futuro deve usar esse contrato; sucesso fica silencioso e falha imprime somente causa sanitizada e ação local, sem secrets e sem logs brutos.
- Guardrail: v1.80 não agenda cron, não muda delivery Telegram e não autoriza runtime/gateway/provider/Docker/VPS/writes externos; é camada local/documental + testes.

## Memory OS v1.90 — Operational Regression Registry

- Objetivo: transformar erros operacionais recorrentes em entradas auditáveis de regressão e plano de prevenção, sem depender de memória de chat ou alerta solto.
- Entregas locais/documentais aprovadas: `register_operational_regression`, `build_regression_prevention_plan`, fixture `operational-regression-tests-v190.json`, recall `context-recall-tests-v190.json` e report `context-intelligence-latest.json` versão `v1.90`.
- Registry JSONL: `operational-regression-registry.jsonl` é append-only, sanitiza sintomas, registra `error_class`, `prevention_test`, `evidence_paths`, `risk_level`, `autoheal_status` e flags `external_writes=false`/`runtime_changes=false`.
- Fail-closed: auto-heal L1 só pode apontar para allowlist local/documental; ações L2/L3 como Docker/runtime/gateway/provider/Telegram/cron/writes externos viram `approval_required` e `approval_packet_required`.
- Plano: `build_regression_prevention_plan` agrupa itens abertos por classe de erro, lista testes obrigatórios e separa itens que exigem aprovação.
- Testes: `/opt/data/tests/test_memory_os_regression_registry_v190.py` cobre sanitização, bloqueio L2/L3, agrupamento do plano e bootstrap v1.90.
- Regra de uso: quando um erro operacional for encontrado, registrar classe + teste preventivo antes de encerrar; não resolver via lembrança solta ou só resumo de chat.
- Guardrail: v1.90 não executa auto-heal real, não agenda cron, não muda runtime/gateway/Telegram/provider/Docker/VPS/writes externos; é camada local/documental + testes.

## Memory OS v2.0 — Local QA Gate

- Objetivo: consolidar a verificação completa do Memory OS em um plano local determinístico, sem depender de checklist manual ou claims de sucesso sem evidência fresca.
- Entregas locais/documentais aprovadas: `build_memory_os_qa_gate_plan`, `validate_memory_os_qa_gate_plan`, `format_memory_os_qa_gate_plan`, CLI `--qa-plan`, fixture `local-qa-gate-v200.json`, recall `context-recall-tests-v200.json` e report `context-intelligence-latest.json` versão `v2.0`.
- Plano v2.0: lista testes v1.20-v2.0, bootstrap, self-test silent-OK, contradiction scan, Brain health, operational docs guard e focused secret scan.
- Segurança: `validate_memory_os_qa_gate_plan` bloqueia comandos com Docker/SSH/curl/wget/kubectl/systemctl/restart/Telegram/provedores/writes externos; plano declara `local_only=true`, `external_writes=false`, `runtime_changes=false`.
- CLI: `--qa-plan` imprime JSON do plano e não executa checks; success real exige rodada fresca dos comandos e receipt pós-verificação.
- Testes: `/opt/data/tests/test_memory_os_local_qa_gate_v200.py` cobre completude do plano, bloqueio de comandos runtime/network, CLI plan-only, formatação sem claim de execução e bootstrap v2.0.
- Regra de uso: ao fechar pacote Memory OS, usar o QA gate como checklist canônico; se receipt/report mudar depois da verificação, rerodar o gate relevante antes de responder.
- Guardrail: v2.0 não executa runtime/gateway/provider/Docker/VPS/Telegram/cron/writes externos; é plano/contrato local + testes.

## Memory OS v2.1 — Coverage & Drift Matrix

- Objetivo: cobrir frentes/agentes reais com matriz local de cobertura, evitando buracos silenciosos entre `default`, Mordomo, LK, SPITI, Zipper e Mesa COO.
- Entregas locais/documentais: `build_memory_os_coverage_matrix`, `validate_memory_os_coverage_matrix`, fixture `memory-os-coverage-matrix-v210.json`, latest report com `coverage_drift_matrix` e `coverage_matrix_fixture`.
- Campos por frente: `front`, `status`, `evidence_paths`, `current_state`, `context_pack`, `skill_routine`, `owner`, `logical_source`.
- Status permitidos: `covered`, `partial`, `missing`, `stale`; evidências ficam repo-relativas/sanitizadas.
- Teste: `/opt/data/tests/test_memory_os_coverage_matrix_v210.py`.
- Guardrail: matriz apenas lê evidências locais/documentais; sem runtime, sem rede, sem writes externos.

## Memory OS v2.2 — Receipt Writer Adoption Gate

- Objetivo: garantir adoção contínua do padrão de receipts/writer/linter em rotinas críticas, sem depender de memória solta.
- Entregas locais/documentais: `build_receipt_adoption_gate`, `validate_receipt_adoption_gate`, fixture `receipt-adoption-gate-v220.json`, latest report com `receipt_writer_adoption_gate`.
- Targets cobertos: writer core, fallback hook, adoption linter, rotinas de checagem, template, diretórios de governance receipts, latest/events logs.
- Validação: classifica missing/stale/partial/drift e bloqueia quando há `missing_receipt_adoption_coverage`, `stale_receipt_adoption_coverage` ou `partial_receipt_writer_adoption`.
- Teste: `/opt/data/tests/test_memory_os_receipt_adoption_v220.py`.
- Guardrail: gate local/documental; não cria/edita receipts automaticamente e não toca cron/runtime/Telegram.

## Memory OS v2.3 — Replay Simulator

- Objetivo: simular perguntas/decisões históricas críticas contra o contrato do Memory OS para prevenir regressões de raciocínio operacional.
- Entregas locais/documentais: `build_memory_os_replay_suite`, `run_memory_os_replay_simulator`, fixture `replay-simulator-v230.json`, latest report com `memory_os_replay_simulator` e `replay_simulator_cases`.
- Casos obrigatórios: Mesa 2/2 ledger-first, runtime ativo exige evidência viva, approval-scope drift bloqueado, `não fazer` bloqueia writes externos, chat summary é hint-only, self-test OK é silencioso.
- Teste: `/opt/data/tests/test_memory_os_replay_simulator_v230.py`.
- Guardrail: simulador não executa ações reais; só compara rotas/evidências/bloqueios esperados em fixture local.

## Memory OS v2.3 — Atualização do QA Gate

- `build_memory_os_qa_gate_plan` agora inclui os testes v2.1, v2.2 e v2.3 no plano.
- `context-intelligence-latest.json` reporta `version=v2.3` e inclui `coverage_drift_matrix`, `receipt_writer_adoption_gate` e `memory_os_replay_simulator` em `deliveries`.
- Regra de fechamento: sucesso só pode ser claimado após testes v1.20-v2.3, bootstrap, self-test silent-OK, contradiction scan, Brain health, docs guard e secret scan frescos.

## Memory OS × Reminder OS v1 — continuidade de próximos passos

- Quando Memory OS encontrar handoff/receipt/daily/hot com `Próximo passo` aberto, deve classificar se há loop Reminder OS necessário antes de encerrar o ciclo.
- Spec canônica: `areas/operacoes/reminder-os/memory-os-integration-v1.md`.
- Dedupe canônico: owner + next action + evidence; não criar duplicata para artefato já coberto por loop ativo.
- Sucesso permanece silent-OK; criação de loop por si só não vira Telegram. Alerta só via watchdog/2h quando houver `waiting_lucas`, vencimento ou risco real.
- Fase atual é documental/local: não muda hook Memory OS, cron, gateway, runtime, provider ou writes externos sem fase de ativação separada.
