# Retomada de planos e PRDs — 2026-05-09

## Leitura executiva

Relatório gerado por script local/read-only. Ele resume a fila documentada do Hermes Brain e o estado git local; não consulta produção, VPS, Docker, bancos, APIs, Telegram ou crons reais.

- Ativos: 1
- Bloqueados por aprovação/decisão: 5
- Aguardando data/evento: 3
- Git status local: com alterações no worktree

## Próxima ação recomendada

A próxima ação segura é manter documentação/índices e só completar subdocs de integrações quando virarem fluxo real. Não há justificativa para cron semanal recorrente de retomada agora: a fila ativa está pequena e os itens sensíveis estão corretamente bloqueados.

## Itens retomados

### Completar subdocs de integrações não recorrentes quando virarem fluxo real

- Estado: Ativo
- Último artefato/evidência: `ROADMAP-30-DIAS-HERMES.md`, Rodada B.
- Bloqueio real: Sem bloqueio técnico; evitar burocracia antes de fluxo real.
- Próxima ação segura: documentar Judge.me, Frenet, Tiny ERP, Email/Google Workspace, LeiloesBR, Railway, Vercel, Notion/NocoDB e Metricool somente quando houver necessidade operacional concreta
- Precisa aprovação Lucas: não

### Rotação de senha root da `lc.vps`, se desejado

- Estado: Bloqueado
- Último artefato/evidência: `ROADMAP-30-DIAS-HERMES.md`, Rodada A.
- Bloqueio real: ação sensível em infra
- Próxima ação segura: Preparar escopo, risco e rollback; executar só após aprovação explícita.
- Precisa aprovação Lucas: sim

### Decidir se a chave SSH dedicada da VPS permanece ou será removida

- Estado: Bloqueado
- Último artefato/evidência: `ROADMAP-30-DIAS-HERMES.md`, Rodada A.
- Bloqueio real: decisão de acesso/infra
- Próxima ação segura: Preparar escopo, risco e rollback; executar só após aprovação explícita.
- Precisa aprovação Lucas: sim

### Correção ativa do alerta/divergência Gateway Hermes

- Estado: Bloqueado
- Último artefato/evidência: `areas/operacoes/rotinas/hermes-gateway-readonly-diagnostic-2026-05-04.md` e `areas/operacoes/rotinas/hermes-gateway-remediation-plan.md`.
- Bloqueio real: qualquer restart/update/mudança Docker/VPS exige aprovação explícita
- Próxima ação segura: Preparar escopo, risco e rollback; executar só após aprovação explícita.
- Precisa aprovação Lucas: sim

### Mission Control visual ou cron recorrente

- Estado: Bloqueado
- Último artefato/evidência: `areas/operacoes/projetos/mission-control-prd.md`.
- Bloqueio real: virar UI, cron, automação ou runtime exige aprovação de escopo/cadência
- Próxima ação segura: Preparar escopo, risco e rollback; executar só após aprovação explícita.
- Precisa aprovação Lucas: sim

### Qualquer contato externo/campanha/mensagem em massa

- Estado: Bloqueado
- Último artefato/evidência: `seguranca/acoes-sensiveis.md` e playbooks das áreas.
- Bloqueio real: segue exigindo preview e aprovação do Lucas/Osmar/equipe responsável conforme o caso
- Próxima ação segura: Preparar escopo, risco e rollback; executar só após aprovação explícita.
- Precisa aprovação Lucas: sim

### Hermes release watch

- Estado: Aguardando data/evento
- Último artefato/evidência: `cronjob list` em 2026-05-09.
- Bloqueio real: Sem ação imediata; depende de data/evento.
- Próxima ação segura: Aguardar evento/data e revisar evidência antes de agir.
- Precisa aprovação Lucas: sim

### Revisão mensal/arquivamento de pendências antigas

- Estado: Aguardando data/evento
- Último artefato/evidência: `memories/consolidation_weekly/2026-04-28.md`.
- Bloqueio real: Sem ação imediata; depende de data/evento.
- Próxima ação segura: Aguardar evento/data e revisar evidência antes de agir.
- Precisa aprovação Lucas: não

### SPITI email poller / monitor de leilão

- Estado: Aguardando data/evento
- Último artefato/evidência: `memories/decisions.md` e `ROADMAP-30-DIAS-HERMES.md`.
- Bloqueio real: Sem ação imediata; depende de data/evento.
- Próxima ação segura: Aguardar evento/data e revisar evidência antes de agir.
- Precisa aprovação Lucas: sim

## Git local

Status:

```text
M CHANGELOG.md
 M ROADMAP-30-DIAS-HERMES.md
 M areas/operacoes/projetos/hermes-brain-improvement-system.md
 M areas/operacoes/rotinas/retomada-planos-prds.md
 M empresa/gestao/pendencias.md
 M memories/pending.md
?? reports/brain-health-check-2026-05-09-retomada-script.json
?? reports/retomada-planos-prds-2026-05-09.json
?? reports/retomada-planos-prds-2026-05-09.md
?? scripts/retomada_planos_prds.py
```

Últimos commits:

- `d523732 docs: add Brain improvement score script`
- `37eb33a docs: validate material ingest workflow (#7)`
- `12c1078 docs: expand Brain health checks (#6)`
- `5395637 docs: apply memory hygiene to pending tasks (#5)`
- `3ce75f3 docs: add Brain P1 guardrails (#4)`

## Não alterado

- Nenhum cron foi criado, pausado ou alterado.
- Nenhuma UI/Mission Control visual foi criada.
- Nenhum serviço de produção, VPS, Docker, Traefik, volume ou rede foi tocado.
- Nenhum banco, API, secret, campanha, WhatsApp, email, post ou contato externo foi tocado.
