# Auditoria de skills — status, risco e verificação — 2026-05-22

Status: **baseline formal criada** para cumprir o padrão Bruno/OpenClaw de owner/status/risco/última revisão/última verificação.

Escopo: skills canônicas versionadas em `skills/*/SKILL.md` no Hermes Brain.

## Critério

- Owner: área responsável por manter a skill.
- Status: ativa, ativa com guardrails, manutenção, pausada ou candidata a revisão.
- Risco:
  - Baixo: local/read-only/documental.
  - Médio: usa credenciais ou prepara artefatos com potencial externo, mas exige aprovação para write.
  - Alto: pode levar a produção, cliente, dinheiro, campanha ou fonte de verdade; precisa gates fortes.
- Última revisão: data desta auditoria quando o arquivo foi incluído no baseline.
- Última verificação: tipo de verificação usada nesta rodada.

## Matriz canônica

| Skill | Caminho | Owner | Status | Risco | Última revisão | Última verificação | Observação |
|---|---|---|---|---|---|---|---|
| Hermes Brain | `skills/hermes-brain/SKILL.md` | Operações Hermes | Ativa | Médio | 2026-05-22 | Health + mapa + secret scan direcionado | Fonte de verdade documental; não substitui fonte viva. |
| Session Start Protocol | `skills/session-start-protocol/SKILL.md` | Operações Hermes | Ativa | Baixo | 2026-05-22 | Presença no índice + health | Usada para boot/checklist de sessão. |
| Brain Sync | `skills/brain-sync/SKILL.md` | Operações Hermes | Ativa com guardrails | Médio | 2026-05-22 | Brain Sync safe dry-run | Deve respeitar allowlist; reports brutos podem ser bloqueados. |
| Lucas Hermes Continuous Improvement | `skills/lucas-hermes-continuous-improvement/SKILL.md` | Operações Hermes | Ativa com guardrails | Médio | 2026-05-22 | Cron ativo + health | Pode propor melhorias; runtime/Docker/externos continuam approval-gated. |
| LK Cross-sell | `skills/lk-crosssell/SKILL.md` | LK CRM | Ativa com aprovação | Alto | 2026-05-22 | Presença no índice + guardrails | Gera oportunidade, mas contato externo exige aprovação e fonte. |
| LK Leads Esfriando | `skills/lk-leads-esfriando/SKILL.md` | LK CRM | Ativa com aprovação | Alto | 2026-05-22 | Presença no índice + guardrails | Reativação/cliente exige fonte e aprovação conforme escopo. |
| LK Shopify Read-only | `skills/lk-shopify-readonly/SKILL.md` | LK Ecommerce | Ativa read-only | Médio | 2026-05-22 | Presença no índice + guardrails | Consultas Shopify sem writes. |
| LK Shopify Product Upload | `skills/lk-shopify-product-upload/SKILL.md` | LK Ecommerce | Ativa com aprovação forte | Alto | 2026-05-22 | Presença no índice + guardrails | Cadastro/produto/produção exige preview, aprovação e verificação. |
| LK SEO Weekly Improvement | `skills/lk-seo-weekly-improvement/SKILL.md` | LK Growth/SEO | Ativa/pausável conforme cron | Alto | 2026-05-22 | Presença no índice + cron inventory | Mudanças SEO/Shopify/externas exigem approval packet. |
| Hermes Browser CDP | `skills/hermes-browser-cdp/SKILL.md` | Operações Hermes/QA | Ativa com guardrails | Médio | 2026-06-13 | Presença no índice + escopo read-only/QA | QA visual/browser deve evitar produção, credenciais e ações externas sem aprovação. |

## Skills de área indexadas

| Skill | Caminho | Owner | Status | Risco | Última revisão | Última verificação | Observação |
|---|---|---|---|---|---|---|---|
| LK Collection Optimizer | `areas/lk/sub-areas/growth/skills/lk-superpowers-collection-optimizer/SKILL.md` | LK Growth / Otimização de Coleções | Ativa com guardrails | Alto | 2026-06-13 | Presença no índice + guardrails LKGOC | Especialista de coleções; Shopify/theme/fonte da verdade continuam approval-gated. |

## Gaps encontrados

1. O índice existia, mas não tinha matriz formal de owner/status/risco/última verificação.
2. Algumas skills têm risco operacional alto porque podem preparar writes externos; o risco é aceitável apenas quando os gates de aprovação são seguidos.
3. Ainda falta automatizar uma auditoria mensal que compare `skills/*/SKILL.md` contra este baseline e marque skills sem owner/status.

## Regra operacional

Antes de usar uma skill para ação externa ou fonte de verdade:

1. Ler a skill atual.
2. Verificar se a fonte viva/API/sistema real confirma o dado.
3. Se houver write externo, apresentar escopo, payload, risco e rollback para aprovação explícita.
4. Registrar receipt/handoff no Brain quando houver decisão, envio, write, aprovação ou aprendizado durável.

## Próxima revisão

Revisar mensalmente ou quando uma skill nova for adicionada/alterada com risco médio/alto.
