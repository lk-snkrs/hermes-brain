# Memória quente — contexto current

Atualizado: 2026-06-01
Status: camada Bruno/OpenClaw/Hermes COO ativa para evitar perda por compactação, orientar handoffs e reconciliar runtime/Brain sem ruído.

## Política current de memória

- Memória curta/injetada do Hermes (`MEMORY.md`/`USER.md`) = boot mínimo curado: identidade, preferências, guardrails e ponteiros.
- Memória rica = Brain/daily notes/`hot.md`/context files/skills/session_search/reports/archive e, se aprovado, provider externo.
- Fonte canônica: `memories/politica-memoria-hermes.md`.
- Relatório de validação web: `/opt/data/reports/hermes-memory-best-practices-web-validation-20260601.md`.
- Profiles especialistas compactados em 2026-06-01; receipt: `reports/governance/hermes-memory-profile-compact-receipt-2026-06-01.md`.
- Conteúdo rico removido foi auditado e classificado em `reports/governance/hermes-memory-rich-content-migration-backlog-2026-06-01.md`; provider externo fica somente como spike futuro em `reports/governance/hermes-memory-provider-spike-criteria-2026-06-01.md`.
- `MEMORY.md` ricos do Brain também foram revisados para reduzir localizador sensível/estado longo; receipt: `reports/governance/hermes-brain-rich-memory-hygiene-receipt-2026-06-01.md`.
- Política canônica ganhou índice operacional de roteamento de memória e o `AGENTS.md` raiz aponta para ela; resumo canônico agora está explícito em `memories/politica-memoria-hermes.md`, `memories/MAPA.md` e `AGENTS.md`: Brain = fonte rica; `MEMORY.md`/`USER.md` = boot mínimo; daily/hot/reports/receipts = continuidade/evidência/current; skills = procedimentos; `session_search` = histórico; provider externo = atualmente rejeitado/off; Brain é fonte rica. Receipt: `reports/governance/hermes-memory-policy-context-routing-receipt-2026-06-01.md`.
- PRD provider externo + Hermes Brain criado em `areas/operacoes/prds/hermes-memzero-brain-memory-prd-2026-06-01.md`; recomendação current: não ativar provider externo em produção, apenas spike canário/sintético se aprovado.
- Spike de provider externo preparado até Tarefa 3: queries de avaliação e approval packet local em `reports/governance/provider_external_spike-eval-queries-2026-06-01.md` e `reports/governance/provider_external_canary-approval-packet-2026-06-01.md`; provider ainda não ativado.
- Reauditoria de memória vs Bruno/OpenClaw e docs oficiais Hermes concluída: `reports/governance/hermes-memory-reaudit-bruno-docs-2026-06-01.md`. Estado current: arquitetura correta; P1 recomendado é compactar `USER.md` default, hoje alto (~89,7%), sem mexer em runtime/provider.

## Prioridades current

1. Manter o Hermes Brain como fonte de verdade, não o chat.
2. Garantir que decisões customer-facing aprovadas por Lucas virem arquivo vivo, MAPA/índice e evidência de verificação.
3. Manter o Fechamento Ágil 23h + Brain Sync seguro como rotina de consolidação silenciosa/local.
4. Evitar ruído no Telegram: sucesso normal fica local/Brain; Lucas recebe decisão, exceção, falha ou pedido de aprovação.
5. Orquestrador Hermes/Fase 8: manter Mesa COO/decisões com UX limpa, sem wrapper/metadados, e handoff obrigatório para outputs materiais de especialistas.
6. Prioridade operacional atual: LK OS/especialistas LK em modo governado. LK Shopify/Trends/Ops estão ativos como especialistas esperados; round-trip final depende de Lucas responder nos chats. Writes Shopify/Tiny/GMC/Meta/Klaviyo continuam bloqueados sem aprovação escopada.
7. Hermes runtime: v0.15.1 saiu em 2026-05-29; tratar como oportunidade/decisão de upgrade com plano e rollback, nunca como auto-update de Docker/gateway.

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


## Memória Hermes P1–P4 — 2026-06-01

- P1 aplicado: `/opt/data/memories/USER.md` default compactado com backup em `/opt/data/backups/memory_hygiene_20260601/`.
- P2 preparado: monitor diário/silent-OK de higiene de memória via script local; mensal foi corrigido por ser lento demais para um Brain vivo.
- P3 consolidado: Bruno/OpenClaw é benchmark metodológico; Brain é fonte rica canônica; `MEMORY.md`/`USER.md` são boot mínimo.
- P4 decidido: Lucas não quer usar provider externo de memória; provider externo fica off e artefatos de canário são históricos/rejeitados.
- Receipt: receipt P1–P4 de memória em `reports/governance/`.

- P2 runtime local: cron `f9a1d43caf48` ajustado para rodar junto do ciclo 02h BRT, com folga de 15 minutos para o ciclo 02h concluir (`15 5 * * *` = 02:15 BRT), `deliver=local` e `no_agent`; script silent-OK validado com stdout vazio.
