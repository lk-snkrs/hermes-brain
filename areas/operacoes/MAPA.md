# Operações — Mapa

Escopo: brain sync, cronjobs, health checks, integrações, deploys, manutenção e melhoria contínua do Hermes Brain.

Todo cron real deve ter rotina `.md` correspondente. Rotina documentada não prova execução ativa; verificar cron/Hermes/VPS antes de afirmar que roda.

## Base de conhecimento

- `base-conhecimento/bruno-openclaw-segundo-cerebro-crons-consolidacao-diaria-2026-05-19.md` — síntese corrigida do padrão Bruno/OpenClaw para segundo cérebro: workspace documentado, MAPAs, daily notes, `hot.md`, Revisão do Dia, meta-cron e heartbeat de consolidação.
- `base-conhecimento/bruno-openclaw-organograma-agentes-e-brain-2026-05-19.md` — síntese complementar sobre `AGENTS.md` como organograma vivo, multi-agente e subida de execução para o Brain.

## Inventários

- `decisions/` — decisões operacionais canônicas, incluindo política de memória sem provider externo.
- `inventarios/crons-agentes-profiles.md` — inventário vivo de agentes, profiles, bots, crons, conversas/projetos e cobertura do Fechamento Ágil 23h.
- `mordomo/MAPA.md` — ponte canônica mínima para Mordomo/Lucas pessoal, sem criar runtime ou agente novo.

## Rotinas principais

- `rotinas/brain-sync.md` — sincronização/versionamento do Brain.
- `rotinas/brain-health-check.md` — validação técnica de secrets, links, agentes, rotinas e skills.
- `rotinas/material-ingest-to-prd.md` — ingestão segura de material externo até documentação, matriz de decisão e PRD.
- `rotinas/brain-improvement-score.md` — score executivo de saúde/maturidade do Brain.
- `rotinas/retomada-planos-prds.md` — retomada de planos, PRDs, branches e análises pausadas.
- `rotinas/revisao-operacional-multiempresa.md` — leitura executiva sob demanda de LK, Zipper, SPITI e Operações usando Brain versionado.
- `rotinas/memory-hygiene-pendencias.md` — higiene de memória, pendências, decisões e lições.
- `rotinas/security-checkup.md` — revisão de segurança para Brain, integrações, canais, secrets e execução.
- `rotinas/area-skill-subagent-agent-decision.md` — matriz para decidir área, rotina, skill, subagent, cron ou agente/canal permanente.
- `rotinas/hermes-release-watch.md` — monitoramento de releases Hermes Agent e avaliação de melhorias.
- `rotinas/hermes-runtime-observability.md` — observabilidade read-only do runtime Hermes.
- `rotinas/hermes-agent-cron-e-performance-diagnostico.md` — rotina Hermes Agent para auditar crons por fonte primária e diagnosticar lentidão/travamento por camadas antes de limpeza/restart.
- `rotinas/company-decision-memory.md` — protocolo para salvar toda decisão empresarial na memória viva da empresa correspondente.
- `rotinas/protocolo-registro-decisoes-aprovadas-contexto-compactado.md` — regra anti-perda para registrar aprovações de copy/tom/fluxo antes que contexto de chat seja compactado.
- `rotinas/protocolo-handoff-agentes-especialistas.md` — mecanismo de handoff para impedir que especialistas virem ilhas de dados e garantir subida de decisões/receipts ao Hermes Central.
- `rotinas/auditoria-handoff-especialistas.md` — auditoria diária/semanal para confirmar que profiles/bots/especialistas deixaram receipt/handoff no Brain.
- `rotinas/memoria-hot-daily-bruno.md` — rotina da camada `memories/hot.md` + `memories/daily/YYYY-MM-DD.md` no padrão Bruno/OpenClaw.
- `rotinas/auditoria-skills-status-risco.md` — auditoria de skills com owner/status/risco/última revisão.
- `rotinas/fechamento-agil-23h.md` — rotina ativa do Fechamento Ágil 23h: consolidação diária Brain-first, saída local em `reports/daily-consolidation/YYYY-MM-DD.md`, sem Telegram de sucesso normal.
- `rotinas/painel-semanal-brain.md` — painel semanal do que entrou no Brain, bloqueios corretos do Brain Sync e rotinas/MAPAs a promover ou limpar.
- `rotinas/mesa-coo-telegram-quality-audit.md` — auditoria local da próxima Mesa COO real no Telegram: UX limpa, utilidade executiva, botões nativos e ausência de wrapper/job_id/JSON/marker técnico.
- `rotinas/orquestracao-scorecard-semanal.md` — scorecard semanal da orquestração Hermes COO: roteamento, handoff/receipt, approval gates, UX Telegram e aprendizado/skills.
- `rotinas/handoff-completeness-audit-local.md` — auditoria local para detectar outputs materiais sem handoff/receipt central e corrigir apenas gaps documentais verificáveis.
- `rotinas/skills-effectiveness-review.md` — revisão de efetividade de skills para detectar erro repetido, skill inchada/desatualizada e aprendizado no lugar errado.

- `rotinas/brain-operating-layer.md` — camada Hermes-native que transforma o padrão Bruno/OpenClaw em operação viva com receipts, approvals, runtime truth e watchdogs.
- `rotinas/brain-steward-daily.md` — steward diário silent-OK para daily/hot/receipts/decisões/handoffs/skills.
- `rotinas/runtime-truth-reconciler.md` — reconciliação entre documentação e runtime real de crons/profiles/bots.
- `intelligence-map.md` — mapa central de loops 23h/02h/02h30/Mesa COO, fontes, outputs, guardrails e anti-duplicidade.
- `rotinas/cron-control-plane.md` — snapshot governamental dos crons vivos/pausados, owners, delivery, side effects e kill criteria.
- `rotinas/cron-owner-reaudit-semanal.md` — reauditoria semanal/local dos donos de crons x organograma, Task Router, profiles e ruído de entrega.
- `rotinas/decision-inbox-taxonomy.md` — taxonomy canônica da COO Queue/Decision Inbox para reduzir falsos positivos e ruído.
- `../../scripts/operational_docs_guard.py` — scanner de docs operacionais para impedir `/root`, `sshpass`, Mem0 legado e comandos perigosos como instrução viva sem marcador LEGACY/DRY-RUN/DO NOT RUN.
- `rotinas/customer-facing-decision-guard.md` — guard para copy/tom/fluxo/canal/promessa/oferta/customer-facing.
- `rotinas/hot-memory-compiler.md` — compilação segura do `memories/hot.md` a partir de artefatos recentes.
- `rotinas/skill-promotion-engine.md` — promoção de aprendizados recorrentes para drafts/skills verificados.
- `rotinas/approval-ledger.md` — livro-razão de aprovações/correções/autonomia.
- `rotinas/webhooks-to-brain.md` — padrão receipt-first para eventos e webhooks.
- `rotinas/voice-to-brain.md` — áudio Telegram para Brain com confirmação em casos críticos.
- `rotinas/brain-diff-digest.md` — digest pré-sync de alterações, riscos e bloqueios.
- `rotinas/source-confidence.md` — classificação de confiabilidade de fonte.
- `rotinas/mission-control-brain-cockpit.md` — Mission Control como cockpit/decision inbox, não fonte de verdade paralela.
- `rotinas/semantic-recovery-session-search.md` — recuperar sessões antigas e promover achados duráveis ao Brain.
- `rotinas/runtime-profile-channel-inventory-2026-05-19.md` — inventário canônico de profiles, bots, canais, cadência, status documental, silent contract e kill criteria.

## Templates operacionais

- `templates/matriz-decisao-bruno-hermes.md` — aplicar/adaptar/deferir/rejeitar conceitos externos.
- `templates/prd-hermes-brain-improvement.md` — PRD padrão para melhoria do Brain.
- `templates/report-health-executivo.md` — template para transformar checks técnicos em relatório executivo.
- `templates/nova-integracao.md` — checklist antes de conectar/documentar ferramenta nova.
- `templates/novo-canal-agente.md` — decisão antes de criar canal, agente permanente, subagent ou cron.
- `templates/delivery-summary.md` — resumo padrão de entrega com verificações, não alterações e próximos passos.
- `templates/decisao-customer-facing.md` — registro obrigatório de copy, tom, fluxo, canal, segmento ou oferta aprovada para comunicação externa/customer-facing.

- `templates/receipt-operacional.md` — receipt universal para execução relevante, handoff, cron, webhook e especialista.
- `templates/approval-ledger-entry.md` — registro de aprovação/correção/autonomia concedida por Lucas.
- `templates/source-confidence.md` — bloco de confiabilidade de fonte: runtime-verificado, primária, secundária, inferido ou não-verificado.
- `templates/webhook-to-brain-event.md` — receipt para evento/webhook/API/email/WhatsApp antes de qualquer write externo.
- `templates/voice-to-brain-capture.md` — captura de áudio Telegram para daily/hot/decisão/pendência com confirmação em casos críticos.
- `templates/skill-promotion-candidate.md` — rascunho de procedimento candidato a skill.

## Projetos

- `brds/hermes-brain-fechamento-agil-23h-brd-2026-05-19.md` — BRD para aprovação do Fechamento Ágil 23h: consolidação diária Brain-first, multi-agente, sem writes externos e sem ruído Telegram desnecessário.
- `prds/hermes-brain-daily-consolidation-crons-prd-2026-05-19.md` — PRD inicial para implementar o ciclo Bruno/OpenClaw no Hermes Brain: inventário vivo, auditoria 07h, consolidação diária, manutenção de memória e auditoria mensal de MAPAs. Observação: horário do fechamento ajustado no BRD para 23h BRT conforme Lucas.
- `prds/pixel-ai-hub-learning-loop-hermes-agent-2026-05-25.md` — PRD do loop Pixel AI Hub/Brainzinho como melhoria contínua do Hermes Agent central, não ownership do Mordomo.
- `prds/company-decision-memory-prd-2026-05-17.md` — PRD da regra de memória de decisões por empresa.
- `projetos/hermes-brain-improvement-system.md` — sistema contínuo para transformar material externo em melhorias seguras do Brain.
- `projetos/mission-control-prd.md` — PRD do Mission Control Hermes read-only, começando como relatório/protocolo seguro.
- `projetos/mission-control-hermes-native-prd-2026-05-17.md` — PRD completo do novo Mission Control Hermes-native / COO Cockpit construído do zero, abandonando Tenacity OS como base e aproveitando aprendizados do Hermes Workspace com guardrails multiempresa.

- `brds/hermes-brain-operating-layer-brd-2026-05-20.md` — BRD da camada Hermes-native sobre o ecossistema Bruno: receipts, approvals, runtime truth, steward, webhooks e voice-to-brain.

## Reports

- `reports/mission-control-hermes-native-v3-work-kernel-2026-05-17.md` — entrega v3 do Mission Control com kernel local interativo: Goals, Kanban, Decision Packets e Approval States, marker `hermes-native-v3-work-kernel-2026-05-17` em produção.
- `reports/mission-control-hermes-native-v2-interactive-2026-05-17.md` — correção action-first do Mission Control: Decision Inbox com botões, matriz de features Hermes, chat/terminal/goals/kanban e marker `hermes-native-v2-interactive-2026-05-17` em produção.
- `reports/mission-control-hermes-native-v1-deploy-2026-05-17.md` — entrega verificada do Mission Control Hermes-native v1 em `mission.lucascimino.com`, com marker `hermes-native-v1-2026-05-17`.
- `projetos/mission-control-reconciliation-pointer-2026-05-19.md` — ponte documental para a reconciliação futura do Mission Control, sem mexer em repo/UI/runtime.

## Reports

- `../../reports/bruno-atual-hermes-adaptation-audit-2026-05-19.md` — auditoria completa do pacote BRUNO-ATUAL, com adaptação Hermes-native e notas por dimensão.
- `../../reports/brain-improvement-score-2026-05-09.md` — primeira execução manual do Brain Improvement Score.
- `../../reports/brain-health-check-2026-05-09.json` — primeira saída JSON versionada da Rodada G, com `FAIL=0 WARN=0`.
- `../../reports/material-ingest-to-prd-test-2026-05-09.md` — validação do modo leve da rotina Material Ingest to PRD usando PRD antigo.
- `../../reports/revisao-operacional-multiempresa-2026-05-09.md` — primeira revisão operacional multiempresa sob demanda, sem dados vivos ou produção.
- `../../reports/daily-consolidation/2026-05-19.md` — teste manual Fase 1A do Fechamento Ágil 23h, sem cron recorrente e sem writes externos.
- `../../reports/brain-weekly-panel/brain-weekly-panel-2026-05-19.md` — primeiro painel semanal do Brain após ativação do Brain Sync seguro.
- `../../reports/governance/approval-memory-audit-2026-05-20.md` — auditoria Bruno/OpenClaw de registro de aprovações, copy e memória operacional.
- `../../reports/governance/customer-facing-decision-template-healthcheck-2026-05-20.md` — evidência da criação do template obrigatório de decisão customer-facing e do guard de health check.
- `../../reports/governance/bruno-openclaw-gap-closure-2026-05-20.md` — fechamento das lacunas Bruno/OpenClaw restantes: hot/current, daily, handoff, runtime e skills.

- `../../reports/governance/hermes-brain-operating-layer-feature-audit-2026-05-20.md` — auditoria das 15 features Hermes aplicáveis ao ecossistema Bruno e status já faz/não faz/fortalecido.
- `../../reports/governance/hermes-brain-operating-layer-implementation-2026-05-20.md` — registro da implementação documental + automação read-only do Brain Operating Layer.
- `../../reports/governance/top5-melhorias-pos-auditoria-amora-2026-05-25.md` — execução local/read-only das 5 melhorias pós-auditoria Hermes vs Amora: Mesa audit, scorecard semanal, handoff completeness, guardrails read-only e revisão de skills.
- `../../reports/governance/guardrails-readonly-admin-inspection-packet-2026-05-25.md` — packet para separar inspeção administrativa read-only de mutações em guardrails de ferramentas.

## Guardrails

- Secrets sempre via Doppler, apenas nomes em docs.
- Produção, VPS, Docker, Traefik, volumes, redes, deploys, banco, campanhas e mensagens externas exigem aprovação Lucas.
- PRs documentais/Brain de baixo risco podem seguir com merge autônomo se health check, secret scan e mergeability estiverem limpos; produção, infra, secrets, banco e ações externas seguem exigindo aprovação explícita.
