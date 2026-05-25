# Memória quente — contexto current

Atualizado: 2026-05-25
Status: camada Bruno/OpenClaw/Hermes COO criada para evitar perda por compactação e orientar handoffs.

## Prioridades current

1. Manter o Hermes Brain como fonte de verdade, não o chat.
2. Garantir que decisões customer-facing aprovadas por Lucas virem arquivo vivo, MAPA/índice e evidência de verificação.
3. Manter o Fechamento Ágil 23h + Brain Sync seguro como rotina de consolidação silenciosa/local.
4. Evitar ruído no Telegram: sucesso normal fica local/Brain; Lucas recebe decisão, exceção, falha ou pedido de aprovação.
5. Orquestrador Hermes/Fase 8: validar a próxima Mesa COO real no Telegram sem wrapper/metadados e manter handoff obrigatório para outputs materiais de especialistas.
6. Prioridade operacional atual: LK/GMC continua em modo read-only até confirmação visual das Data Sources e aprovação explícita para qualquer write externo.

## Decisões abertas do COO

- Mesa COO v2: aguardar próxima entrega real no Telegram. Se vier limpa, marcar P8.3 como validada; se vazar wrapper/metadata, corrigir scheduler/gateway com teste antes de novo prompt tweak.
- Handoff completeness: outputs materiais em `reports/`, `areas/**/receipts/`, `areas/**/decisions/` ou approval packets precisam de registro localizável no Brain quando afetarem especialista, decisão, risco, aprovação ou write. Auditoria 2026-05-25 encontrou gap real em LK Growth; correção documental criada em `areas/lk/sub-areas/growth/reports/2026-05-25-handoff-retroativo-receipts-theme.md`, sem inferir aprovação além dos receipts.
- Amora/Bruno benchmark: não copiar 60+ crons nem multi-canal por padrão; preservar identidade profunda, silêncio útil, MAPA vivo, skills para repetição e rotina com receipts.
- Pós-auditoria Amora 2026-05-25: top 5 melhorias executadas em modo local/read-only. Item 2 ficou **semanal** via `areas/operacoes/rotinas/orquestracao-scorecard-semanal.md`; sem cron novo até provar utilidade manual/local.

## Decisões recentes que não podem sumir

- Decisões de copy/tom/fluxo customer-facing precisam ser registradas imediatamente usando `areas/operacoes/templates/decisao-customer-facing.md`.
- Decisão viva prevalece sobre playbook antigo quando houver conflito.
- Reports brutos continuam bloqueados; apenas evidência curada entra em `reports/governance/`.
- Especialista pode executar dentro do escopo, mas precisa deixar handoff/receipt para o Hermes Central.

## Links quentes

- `areas/operacoes/rotinas/protocolo-registro-decisoes-aprovadas-contexto-compactado.md`
- `areas/operacoes/templates/decisao-customer-facing.md`
- `areas/operacoes/rotinas/brain-sync.md`
- `areas/operacoes/rotinas/fechamento-agil-23h.md`
- `areas/operacoes/rotinas/protocolo-handoff-agentes-especialistas.md`
- `areas/operacoes/rotinas/auditoria-handoff-especialistas.md`
- `reports/governance/handoff-completeness-check-2026-05-25.md`
- `reports/governance/hermes-orquestrador-vs-amora-audit-2026-05-25.md`
- `reports/governance/`

## Bloqueios/guardrails current

- Não alterar Docker/VPS/Traefik/volumes/redes/containers sem aprovação explícita e plano de rollback.
- Não executar writes externos em Shopify/GMC/WhatsApp/e-mail/banco/campanhas sem fonte e aprovação adequada ao escopo.
- Não expor tokens, secrets ou payloads sensíveis em Telegram ou docs versionáveis.
- Documentação de rotina não prova execução ativa; crons/canais precisam de evidência runtime quando afirmados como ativos.

## Próxima revisão

Atualizar no fechamento diário ou sempre que Lucas corrigir prioridade/decisão que afete execução contínua.
