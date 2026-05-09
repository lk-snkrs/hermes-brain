# Operações — Mapa

Escopo: brain sync, cronjobs, health checks, integrações, deploys, manutenção e melhoria contínua do Hermes Brain.

Todo cron real deve ter rotina `.md` correspondente. Rotina documentada não prova execução ativa; verificar cron/Hermes/VPS antes de afirmar que roda.

## Rotinas principais

- `rotinas/brain-sync.md` — sincronização/versionamento do Brain.
- `rotinas/brain-health-check.md` — validação técnica de secrets, links, agentes, rotinas e skills.
- `rotinas/material-ingest-to-prd.md` — ingestão segura de material externo até documentação, matriz de decisão e PRD.
- `rotinas/brain-improvement-score.md` — score executivo de saúde/maturidade do Brain.
- `rotinas/retomada-planos-prds.md` — retomada de planos, PRDs, branches e análises pausadas.
- `rotinas/hermes-release-watch.md` — monitoramento de releases Hermes Agent e avaliação de melhorias.
- `rotinas/hermes-runtime-observability.md` — observabilidade read-only do runtime Hermes.

## Templates operacionais

- `templates/matriz-decisao-bruno-hermes.md` — aplicar/adaptar/deferir/rejeitar conceitos externos.
- `templates/prd-hermes-brain-improvement.md` — PRD padrão para melhoria do Brain.

## Projetos

- `projetos/hermes-brain-improvement-system.md` — sistema contínuo para transformar material externo em melhorias seguras do Brain.

## Guardrails

- Secrets sempre via Doppler, apenas nomes em docs.
- Produção, VPS, Docker, Traefik, volumes, redes, deploys, banco, campanhas e mensagens externas exigem aprovação Lucas.
- PR draft é aceitável para documentação; merge em `main` exige aprovação explícita.
