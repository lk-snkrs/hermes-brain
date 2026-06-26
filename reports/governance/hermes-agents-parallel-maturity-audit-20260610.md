# Hermes / Agentes — auditoria paralela de maturidade e backlog

Data: 2026-06-10
Gerado em: 2026-06-10T14:13:27Z
Escopo: local/read-only + documentação Brain. Não houve Docker, VPS, gateway restart, alteração de cron vivo, provider, token, Telegram, Shopify, Tiny, GMC, Klaviyo, WhatsApp, e-mail ou banco.

## Frentes executadas em paralelo

1. **Matriz de agentes/perfis** — profiles, gateways vivos via `HERMES_HOME`, cron/watchdog coverage, toolsets e gaps.
2. **Mesa COO / Decision Sequence** — análise do bug recorrente `1/N -> resposta Lucas -> próximo item` e desenho de ledger transacional local.
3. **Hermes capabilities** — fast lane/deep work, watchdogs, model routing, dashboard/cockpit e configured-vs-active.

## Resultado executivo

O maior ganho agora não é criar mais agentes. É tornar os agentes existentes mais determinísticos:

- persistir sequência de decisões da Mesa antes de enviar `1/N`;
- manter scorecard vivo `configured vs active vs verified`;
- padronizar modo operacional por pedido: fast lane, deep work, no_agent watchdog, approval packet, handoff/delegation;
- reconciliar docs que ficaram atrás do runtime real;
- consolidar cockpit read-only com status de agentes, crons, watchdogs, memória, decisões e receipts.

## Matriz resumida por agente/perfil

- **default / Hermes Geral**: maturidade alta; gateway vivo; crons fortes; Telegram/toolsets amplos. Gap: alto poder no chat exige guardrails e ledger de decisões.
- **mordomo**: maturidade alta, mas complexa; gateway vivo; 16 crons enabled no perfil. Gap: risco de sobreposição/ruído e side effects pessoais/WhatsApp/email.
- **lk-growth**: maturidade alta; gateway vivo; 9 crons enabled; escopo Growth/GMC/SEO/CRO/GEO. Gap: manter trabalhos pesados fora do Telegram e classificar duplicidade de profile em home.
- **lk-collection-optimizer / LKGOC**: runtime vivo e domínio bem documentado. Gap: cron próprio não visível; confirmar status intencional vs preparado.
- **lk-shopify**: maturidade média-alta; gateway vivo; cron quinzenal; guardrails fortes. Gap: alto risco por produção Shopify; sempre preview/snapshot/approval/readback.
- **lk-ops**: maturidade média; gateway vivo; pós-venda/canary sensível. Gap: fast lane de atendimento e separação rígida de estoque/disponibilidade para `lk-stock`.
- **lk-stock**: gateway e cron vivos. Gap crítico: docs de roteamento ainda diziam preparado/parado; precisa reconciliation documental.
- **lk-trends**: maturidade média-alta; gateway vivo; 2 crons. Gap: tendências não autorizam compra/reposição; handoff obrigatório.
- **lk-content**: gateway vivo; 6 crons. Gap: runtime existe, mas documentação canônica/organograma ainda incompleta.
- **spiti**: profile vivo, sem crons locais; coerente com silêncio/baixo risco. Gap: heartbeat só quando houver evento/leilão/fonte estável.
- **zipper**: documental/read-only; sem profile próprio. Gap: automações Zipper espalhadas em default/mordomo, ownership difuso.
- **lc-claude-cli**: preparado/experimental; gateway parado. Gap: validar proxy/canal/watchdog antes de promover.
- **brain-process / hermes-ops-readonly / lk-analyst-readonly / lk-content-reviewer**: auxiliares estreitos, não-live; manter como workers/read-only até haver caso real.

## Scorecard Hermes capabilities

- Fast lane / deep work: **4/10** — política ainda documental; Telegram default tem prompt/toolset pesado.
- Watchdogs: **8/10** — maturidade forte, silent-OK e Runtime Truth Reconciler verdes; falta cockpit único.
- Model routing: **5.5/10** — provider/model robustos, mas sem política operacional por classe de tarefa.
- Dashboard/cockpit: **6.5/10** — v0.16 documenta dashboard e plugins; cockpit executivo ainda parcial.
- Configured-vs-active verification: **8/10** — Reconciler bom; falta matriz única por profile/platform/model/toolset/cron.

## P0 local/documental executado agora

- Criado contrato canônico do **Decision Sequence Ledger**: `empresa/contexto/decision-sequence-ledger.md`.
- Criado registro inicial da Mesa 2026-06-10 em `empresa/contexto/decision-sequences/2026-06-10.jsonl` e resumo `.md`, marcando as duas decisões como `declined` após Lucas responder `não`.
- Criada rotina **Agent Operating Modes — fast lane/deep work**: `areas/operacoes/rotinas/agent-operating-modes-fast-deep.md`.
- Criada rotina **Configured vs Active Scorecard**: `areas/operacoes/rotinas/configured-vs-active-scorecard.md`.

## P0 pendente local/documental

1. Reconciliar docs de `lk-stock` e `lk-content` com runtime vivo real.
2. Criar scorecard JSON/Markdown gerado por script local sanitizado.
3. Criar template de cockpit cards read-only: agentes, crons, watchdogs, model active/configured, prompt-size, Memory OS, approvals, receipts.
4. Marcar Zipper como documental/read-only com ownership explícito de automações distribuídas default/mordomo.

## Requer aprovação escopada futura

- Alterar prompt vivo do cron Mesa COO em `/opt/data/cron/jobs.json`.
- Criar/alterar crons recorrentes.
- Restart/reload de gateway ou profiles.
- Mudar toolsets Telegram ativos.
- Trocar default/fallback model em profiles vivos.
- Expor dashboard/API/cockpit publicamente ou alterar runtime.

## Guardrails preservados

- Nenhum segredo foi impresso.
- Nenhuma integração externa foi chamada para write.
- Nenhum runtime foi reiniciado.
- Artefatos são locais/documentais no Brain.
