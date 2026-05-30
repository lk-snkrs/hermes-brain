# Operações — Mapa

Escopo: brain sync, cronjobs, health checks, integrações, deploys, manutenção e melhoria contínua do Hermes Brain.

Todo cron real deve ter rotina `.md` correspondente. Rotina documentada não prova execução ativa; verificar cron/Hermes/VPS antes de afirmar que roda.

## Rotinas principais

- `rotinas/brain-sync.md` — sincronização/versionamento do Brain.
- `rotinas/brain-structure-governance-preflight.md` — validação de estrutura antes de mexer em skills, agentes, heartbeats, rotinas ou reorganizações.
- `rotinas/data-boundaries-authorized-summaries.md` — separa Brain/Git para conhecimento, fontes vivas para dados operacionais e hub-and-spoke com resumos autorizados multiempresa.
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
- `rotinas/runtime-profile-channel-inventory-2026-05-19.md` — inventário canônico de profiles, bots, canais, cadência, status documental, silent contract e kill criteria.

## Templates operacionais

- `templates/matriz-decisao-bruno-hermes.md` — aplicar/adaptar/deferir/rejeitar conceitos externos.
- `templates/prd-hermes-brain-improvement.md` — PRD padrão para melhoria do Brain.
- `templates/report-health-executivo.md` — template para transformar checks técnicos em relatório executivo.
- `templates/nova-integracao.md` — checklist antes de conectar/documentar ferramenta nova.
- `templates/novo-canal-agente.md` — decisão antes de criar canal, agente permanente, subagent ou cron.
- `templates/delivery-summary.md` — resumo padrão de entrega com verificações, não alterações e próximos passos.

## Projetos

- `projetos/hermes-brain-improvement-system.md` — sistema contínuo para transformar material externo em melhorias seguras do Brain.
- `projetos/mission-control-prd.md` — PRD do Mission Control Hermes read-only, começando como relatório/protocolo seguro.
- `projetos/mission-control-reconciliation-pointer-2026-05-19.md` — ponte documental para a reconciliação futura do Mission Control, sem mexer em repo/UI/runtime.

## Reports

- `../../reports/bruno-atual-hermes-adaptation-audit-2026-05-19.md` — auditoria completa do pacote BRUNO-ATUAL, com adaptação Hermes-native e notas por dimensão.
- `../../reports/brain-improvement-score-2026-05-09.md` — primeira execução manual do Brain Improvement Score.
- `../../reports/brain-health-check-2026-05-09.json` — primeira saída JSON versionada da Rodada G, com `FAIL=0 WARN=0`.
- `../../reports/material-ingest-to-prd-test-2026-05-09.md` — validação do modo leve da rotina Material Ingest to PRD usando PRD antigo.
- `../../reports/revisao-operacional-multiempresa-2026-05-09.md` — primeira revisão operacional multiempresa sob demanda, sem dados vivos ou produção.

## Guardrails

- Secrets sempre via Doppler, apenas nomes em docs.
- Antes de mexer em skills/agentes/rotinas/heartbeats/reorganização, validar estrutura, dono, riscos, índice/MAPA e aprovação necessária.
- Brain/Git guarda conhecimento estável; dados vivos ficam em APIs/bancos/sistemas e só entram como snapshot datado/minimizado ou resumo autorizado.
- Hermes Geral/Mission Control recebe síntese autorizada das áreas, não dumps brutos de LK, Zipper ou SPITI por conveniência.
- Produção, VPS, Docker, Traefik, volumes, redes, deploys, banco, campanhas e mensagens externas exigem aprovação Lucas.
- PRs documentais/Brain de baixo risco podem seguir com merge autônomo se health check, secret scan e mergeability estiverem limpos; produção, infra, secrets, banco e ações externas seguem exigindo aprovação explícita.
