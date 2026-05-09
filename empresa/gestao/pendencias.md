# Pendências executivas — Hermes Brain

Última revisão: 2026-05-09
Rotina aplicada: `areas/operacoes/rotinas/memory-hygiene-pendencias.md`

## Estado executivo

Esta página substitui a lista antiga de 2026-04-19, que misturava bugs corrigidos, crons históricos, pendências vencidas e registros de auditoria. O histórico útil foi preservado nas seções de concluídos/arquivados e nas fontes citadas.

Critério: manter aqui somente pendências acionáveis ou bloqueios que mudam a operação. Detalhes longos pertencem a `areas/`, `empresa/integracoes/`, `reports/`, `CHANGELOG.md` ou `memories/lessons.md`.

## Ativos

- [ ] **Evoluir LK Daily Brief v0.3 para padrão operacional de atribuição paga/influencers** — LK/Analytics/Tráfego Pago — próxima ação: padronizar UTM/cupom por influencer e reconciliar Meta Ads plataforma × GA4 × Shopify antes de qualquer recomendação de escala/pausa. Evidência/base: relatório real agregado/read-only `reports/lk-paid-attribution-brief-real-2026-05-08-v03.md`; Meta Ads Insights read-only funcionou, mas compras/ROAS da plataforma exigem cautela e validação com Shopify.
- [ ] **Mapear funcionários LK, funções e roteamento de relatórios** — LK/Governança — próxima ação: criar matriz de destinatários por relatório/módulo antes de crons ou envios. Dado inicial: Renan cuida de design e SEO; relatórios de design/SEO devem ir para ele. Evidência/base: feedback de Lucas em 2026-05-09.
- [ ] **Aplicar Hermes Learning Loop global** — Operações/Governança — próxima ação: usar `empresa/gestao/hermes-learning-loop.md` para registrar aprovações/correções duráveis em Brain, skills, PRDs ou memória, evitando repetir erros corrigidos. Evidência/base: aprovação explícita de Lucas em 2026-05-09.

- [ ] **Completar subdocs de integrações não recorrentes quando virarem fluxo real** — Operações/Integrações — próxima ação: documentar Judge.me, Frenet, Tiny ERP, Email/Google Workspace, LeiloesBR, Railway, Vercel, Notion/NocoDB e Metricool somente quando houver necessidade operacional concreta. Evidência/base: `ROADMAP-30-DIAS-HERMES.md`, Rodada B.

## Bloqueados — exigem decisão/aprovação Lucas

- [ ] **Rotação de senha root da `lc.vps`, se desejado** — Tecnologia/Segurança — bloqueio: ação sensível em infra; exige aprovação explícita e plano de rollback. Evidência/base: `ROADMAP-30-DIAS-HERMES.md`, Rodada A.
- [ ] **Decidir se a chave SSH dedicada da VPS permanece ou será removida** — Tecnologia/Segurança — bloqueio: decisão de acesso/infra. Evidência/base: `ROADMAP-30-DIAS-HERMES.md`, Rodada A.
- [ ] **Correção ativa do alerta/divergência Gateway Hermes** — Tecnologia — bloqueio: qualquer restart/update/mudança Docker/VPS exige aprovação explícita; diagnóstico read-only já documentado. Evidência/base: `areas/operacoes/rotinas/hermes-gateway-readonly-diagnostic-2026-05-04.md` e `areas/operacoes/rotinas/hermes-gateway-remediation-plan.md`.
- [ ] **Mission Control visual ou cron recorrente** — Operações — bloqueio: virar UI, cron, automação ou runtime exige aprovação de escopo/cadência. Evidência/base: `areas/operacoes/projetos/mission-control-prd.md`.
- [ ] **Qualquer contato externo/campanha/mensagem em massa** — LK/Zipper/SPITI — bloqueio: segue exigindo preview e aprovação do Lucas/Osmar/equipe responsável conforme o caso. Evidência/base: `seguranca/acoes-sensiveis.md` e playbooks das áreas.

## Aguardando data/evento

- [ ] **Hermes release watch** — Operações — próximo evento: cron semanal `Hermes release watch` agendado para 2026-05-11 09:00 UTC; post-check one-shot às 09:15 UTC. Evidência: `cronjob list` em 2026-05-09.
- [ ] **Revisão mensal/arquivamento de pendências antigas** — Governança — próximo check recomendado: 2026-05-26, conforme consolidação de 2026-04-28. Evidência: `memories/consolidation_weekly/2026-04-28.md`.
- [ ] **SPITI email poller / monitor de leilão** — SPITI — aguardando novo leilão ou necessidade operacional; sem auction previsto até agosto/2026 nos registros antigos. Evidência: `memories/decisions.md` e `ROADMAP-30-DIAS-HERMES.md`.

## Concluídos nesta revisão

- **Rotina de revisão operacional multiempresa** — concluído: `areas/operacoes/rotinas/revisao-operacional-multiempresa.md` criado; primeiro relatório gerado em `reports/revisao-operacional-multiempresa-2026-05-09.md`. Decisão operacional: usar sob demanda para priorização LK/Zipper/SPITI/Operações; não criar cron, não consultar produção e não acionar ações externas por padrão.
- **Script local/read-only de retomada de planos/PRDs** — concluído: `scripts/retomada_planos_prds.py` criado; relatório gerado em `reports/retomada-planos-prds-2026-05-09.md` e JSON em `reports/retomada-planos-prds-2026-05-09.json`. Decisão operacional: não criar cron semanal agora; usar sob demanda quando Lucas disser “seguir”, “retomar” ou “onde paramos”.
- **Script executivo para `brain-improvement-score.md`** — concluído: `scripts/brain_improvement_score.py` criado como ferramenta local/read-only; relatório gerado em `reports/brain-improvement-score-2026-05-09-script.md` e JSON em `reports/brain-improvement-score-2026-05-09-script.json`. Cron/UI/Telegram recorrente continuam bloqueados por aprovação explícita.
- **Teste de `material-ingest-to-prd.md` em PRD antigo** — concluído: rotina validada em modo leve usando `areas/operacoes/projetos/mission-control-prd.md`; artefatos locais gerados fora do repo e relatório versionado em `reports/material-ingest-to-prd-test-2026-05-09.md`. Próxima decisão: script executivo de score antes de qualquer cron/UI.
- **Rodada G — Health checks do Brain** — concluído: `scripts/brain_health_check.py` agora cobre secrets, links/anchors markdown, arquivos estruturais obrigatórios, arquivos de agentes, MAPA por área/subárea, rotinas indexadas e skills canônicas; relatório JSON gerado em `reports/brain-health-check-2026-05-09.json`. Evidência: health check `FAIL=0 WARN=0`.
- **Mission Control / Bruno** — concluído: extração, adaptação Hermes-native e PRD documental foram feitos; UI/cron continuam fora de escopo sem aprovação. Evidência: `areas/operacoes/projetos/mission-control-prd.md`, `CHANGELOG.md` 2026-05-09.
- **Hermes Brain Improvement System P0** — concluído e mergeado no `main`. Evidência: PR #2, merge commit `bb7d16d`, arquivos em `areas/operacoes/rotinas/` e templates.
- **Guardrails P1 de memória, segurança e entrega** — concluído e mergeado no `main`. Evidência: PR #4, merge commit `3ce75f3`, `areas/operacoes/rotinas/memory-hygiene-pendencias.md` e `security-checkup.md`.
- **Meta Ads token** — pendência antiga resolvida em 2026-04-25 segundo consolidação semanal; não manter como urgente atual sem nova evidência de falha. Evidência: `memories/consolidation_weekly/2026-04-28.md`.
- **Data gap Supabase LK e 52 pedidos Shopify em falta** — corrigidos em 2026-04-25 segundo consolidação semanal. Evidência: `memories/consolidation_weekly/2026-04-28.md`.

## Arquivados / históricos preservados

- **Lista “Sistema 100% Auditado” de 2026-04-19** — arquivada como histórico; não é estado atual. Manter como contexto em `memories/lessons.md` e consolidações, não como fila ativa.
- **Tabela antiga de 11 crons ativos e 2 falhas** — arquivada por estar desatualizada e misturar crons externos/antigos. Estado atual de crons Hermes verificado em 2026-05-09: `Hermes release watch` e `Hermes release watch post-check` agendados.
- **`memories/pending_local.md` 2026-04-18** — arquivado como histórico local; duplicava pendências já resolvidas ou reclassificadas.

## Promovidos para decisão/lição

- **Autonomia documental de baixo risco** — decisão: Lucas autoriza merges autônomos em PRs documentais/Brain de baixo risco quando checks passarem; produção, infra, secrets, banco, ações externas ou risco destrutivo continuam exigindo aprovação explícita. Destino: `memories/decisions.md` e `empresa/decisoes/decisoes-permanentes.md`.
- **Pendência não é log de sessão** — lição operacional já formalizada pela rotina `memory-hygiene-pendencias.md`: pendências precisam ter status, próxima ação, bloqueio e evidência.

## Verificação da revisão

- Fontes lidas: `empresa/gestao/pendencias.md`, `memories/pending.md`, `memories/pending_local.md`, `memories/decisions.md`, `memories/lessons.md`, `memories/consolidation_weekly/2026-04-28.md`, `ROADMAP-30-DIAS-HERMES.md`, `CHANGELOG.md`, `empresa/gestao/memory-system.md`.
- Crons Hermes atuais: 2 jobs agendados via `cronjob list` em 2026-05-09.
- Nenhum token/segredo foi escrito; nomes de secrets podem aparecer, valores não.
