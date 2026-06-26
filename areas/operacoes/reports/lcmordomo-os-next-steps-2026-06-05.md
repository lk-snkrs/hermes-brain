# LC Mordomo OS — Próximos passos executivos

**Data:** 2026-06-05
**Status:** após PRD v0.1 + SOUL/registry/protocol drafts

## Entregue nesta rodada

1. PRD v0.1 do LC Mordomo OS.
2. SOUL v0.1 do LC Mordomo Central.
3. Subagent Registry v0.1.
4. Handoff Protocol v0.1.
5. Source Confidence + Approval Ledger v0.1.

## Próxima fase recomendada

### Fase 1 — Consolidar contrato operacional

**Ação:** Lucas valida ou corrige SOUL + registry.

**Critério de pronto:** arquitetura aprovada: agente central + subagentes, com A0-A4, handoff e fonte.

### Fase 2 — MVP Zipper

**Ação:** transformar Zipper em primeiro subagente operacional completo.

**Entregas:**

- Zipper subagent SOUL;
- Zipper CRM object spec;
- artist-interest CRM schema/runbook;
- pós-PDF follow-up engine spec;
- negative-fit suppression rules;
- Decision Packet para preço/disponibilidade/negociação.

**Critério de pronto:** leads Zipper entram em CRM/follow-up estruturado e só sobem para Lucas quando há decisão real.

### Fase 3 — Governança dos crons atuais

**Ação:** auditar crons Mordomo/Zipper/Hermes existentes contra o novo modelo.

**Critério de pronto:** cada cron tem owner, entrega, silent contract, fonte, risco e rotina correspondente.

### Fase 4 — SPITI

**Ação:** criar SPITI subagent SOUL + fonte de verdade de lances.

**Critério de pronto:** nenhum dado sensível de leilão é afirmado sem fonte correta.

### Fase 5 — Calendário/Pessoal

**Ação:** formalizar calendar intake e contact-profile/tone learning.

**Critério de pronto:** compromissos claros viram evento/reminder sem Lucas pedir segunda vez.

### Fase 6 — LK

**Ação:** integrar LK como subagente read-only intelligence primeiro.

**Critério de pronto:** LK entra no LC Mordomo sem virar distração do núcleo Zipper/SPITI.

## Recomendação

Não criar profile/runtime separado ainda para todos. Começar com subagentes lógicos documentados e promover para runtime separado só quando houver volume/risco/isolamento real.
