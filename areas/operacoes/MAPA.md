# Operações — Mapa

Escopo: brain sync, cronjobs, health checks, integrações, deploys, manutenção e melhoria contínua do Hermes Brain.

Todo cron real deve ter rotina `.md` correspondente. Rotina documentada não prova execução ativa; verificar cron/Hermes/VPS antes de afirmar que roda.

## Base de conhecimento

- `base-conhecimento/bruno-openclaw-segundo-cerebro-crons-consolidacao-diaria-2026-05-19.md` — síntese corrigida do padrão Bruno/OpenClaw para segundo cérebro: workspace documentado, MAPAs, daily notes, `hot.md`, Revisão do Dia, meta-cron e heartbeat de consolidação.
- `base-conhecimento/bruno-openclaw-organograma-agentes-e-brain-2026-05-19.md` — síntese complementar sobre `AGENTS.md` como organograma vivo, multi-agente e subida de execução para o Brain.

## Inventários

- `inventarios/crons-agentes-profiles.md` — inventário vivo de agentes, profiles, bots, crons, conversas/projetos e cobertura do Fechamento Ágil 23h.

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
- `rotinas/company-decision-memory.md` — protocolo para salvar toda decisão empresarial na memória viva da empresa correspondente.
- `rotinas/fechamento-agil-23h.md` — rotina ativa do Fechamento Ágil 23h: consolidação diária Brain-first, saída local em `reports/daily-consolidation/YYYY-MM-DD.md`, sem Telegram de sucesso normal.

## Templates operacionais

- `templates/matriz-decisao-bruno-hermes.md` — aplicar/adaptar/deferir/rejeitar conceitos externos.
- `templates/prd-hermes-brain-improvement.md` — PRD padrão para melhoria do Brain.
- `templates/report-health-executivo.md` — template para transformar checks técnicos em relatório executivo.
- `templates/nova-integracao.md` — checklist antes de conectar/documentar ferramenta nova.
- `templates/novo-canal-agente.md` — decisão antes de criar canal, agente permanente, subagent ou cron.
- `templates/delivery-summary.md` — resumo padrão de entrega com verificações, não alterações e próximos passos.

## Projetos

- `brds/hermes-brain-fechamento-agil-23h-brd-2026-05-19.md` — BRD para aprovação do Fechamento Ágil 23h: consolidação diária Brain-first, multi-agente, sem writes externos e sem ruído Telegram desnecessário.
- `prds/hermes-brain-daily-consolidation-crons-prd-2026-05-19.md` — PRD inicial para implementar o ciclo Bruno/OpenClaw no Hermes Brain: inventário vivo, auditoria 07h, consolidação diária, manutenção de memória e auditoria mensal de MAPAs. Observação: horário do fechamento ajustado no BRD para 23h BRT conforme Lucas.
- `prds/company-decision-memory-prd-2026-05-17.md` — PRD da regra de memória de decisões por empresa.
- `projetos/hermes-brain-improvement-system.md` — sistema contínuo para transformar material externo em melhorias seguras do Brain.
- `projetos/mission-control-prd.md` — PRD do Mission Control Hermes read-only, começando como relatório/protocolo seguro.
- `projetos/mission-control-hermes-native-prd-2026-05-17.md` — PRD completo do novo Mission Control Hermes-native / COO Cockpit construído do zero, abandonando Tenacity OS como base e aproveitando aprendizados do Hermes Workspace com guardrails multiempresa.

## Reports

- `reports/mission-control-hermes-native-v3-work-kernel-2026-05-17.md` — entrega v3 do Mission Control com kernel local interativo: Goals, Kanban, Decision Packets e Approval States, marker `hermes-native-v3-work-kernel-2026-05-17` em produção.
- `reports/mission-control-hermes-native-v2-interactive-2026-05-17.md` — correção action-first do Mission Control: Decision Inbox com botões, matriz de features Hermes, chat/terminal/goals/kanban e marker `hermes-native-v2-interactive-2026-05-17` em produção.
- `reports/mission-control-hermes-native-v1-deploy-2026-05-17.md` — entrega verificada do Mission Control Hermes-native v1 em `mission.lucascimino.com`, com marker `hermes-native-v1-2026-05-17`.
- `../../reports/brain-improvement-score-2026-05-09.md` — primeira execução manual do Brain Improvement Score.
- `../../reports/brain-health-check-2026-05-09.json` — primeira saída JSON versionada da Rodada G, com `FAIL=0 WARN=0`.
- `../../reports/material-ingest-to-prd-test-2026-05-09.md` — validação do modo leve da rotina Material Ingest to PRD usando PRD antigo.
- `../../reports/revisao-operacional-multiempresa-2026-05-09.md` — primeira revisão operacional multiempresa sob demanda, sem dados vivos ou produção.
- `../../reports/daily-consolidation/2026-05-19.md` — teste manual Fase 1A do Fechamento Ágil 23h, sem cron recorrente e sem writes externos.

## Guardrails

- Secrets sempre via Doppler, apenas nomes em docs.
- Produção, VPS, Docker, Traefik, volumes, redes, deploys, banco, campanhas e mensagens externas exigem aprovação Lucas.
- PRs documentais/Brain de baixo risco podem seguir com merge autônomo se health check, secret scan e mergeability estiverem limpos; produção, infra, secrets, banco e ações externas seguem exigindo aprovação explícita.
