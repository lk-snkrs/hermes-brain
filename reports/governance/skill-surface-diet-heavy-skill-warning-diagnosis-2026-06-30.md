# Skill Surface Diet — diagnóstico de heavy-skill warnings — 2026-06-30

- generated_at_utc: `2026-06-30T12:39:11Z`
- Origem: Mesa COO 2026-06-30 Decisão 3/4 (`Fazer`)
- Escopo aprovado: diagnóstico e proposta de curadoria por profile/skill
- Escopo não aprovado: patch em skill/profile, disable, restart, gateway/runtime mutation, cron mutation
- values_printed: false

## Resultado executivo

O recurring Skill Surface Diet está sem `issues`, mas mantém **8 warnings** de `enabled_heavy_skill`.

A causa é concentrada: **2 skills únicas** geram os warnings, não uma regressão ampla do sistema.

| Skill | Warnings | Maior tamanho observado | Profiles afetados |
|---|---:|---:|---|
| `lk-operational-intelligence` | 7 | 104,229 | lk-collection-optimizer, lk-growth, lk-ops, lk-shopify, lk-stock, lk-trends, mordomo |
| `lk-stock` | 1 | 105,586 | lk-stock |

## Profiles afetados

| Profile | Warnings | Skills |
|---|---:|---|
| `lk-collection-optimizer` | 1 | `lk-operational-intelligence` |
| `lk-growth` | 1 | `lk-operational-intelligence` |
| `lk-ops` | 1 | `lk-operational-intelligence` |
| `lk-shopify` | 1 | `lk-operational-intelligence` |
| `lk-stock` | 2 | `lk-stock`, `lk-operational-intelligence` |
| `lk-trends` | 1 | `lk-operational-intelligence` |
| `mordomo` | 1 | `lk-operational-intelligence` |

## Readback dos arquivos de skill

| Skill | Arquivo | Tamanho atual | Nº references | Exemplos de references |
|---|---|---:|---:|---|
| `lk-operational-intelligence` | `/opt/data/skills/productivity/lk-operational-intelligence/SKILL.md` | 87,093 | 151 | lk-sales-report-ordering-sellers-brand-share-20260517.md, gmc-p2b-p2c-title-seo-20260513.md, market-trends-patterns.md, gmc-brain-safe-continuation-20260522.md, gmc-p1-core-attributes-root-cause-approval-packet-20260512.md, data-spine-patterns.md, absorbed-lk-content-operations, lk-sales-report-email-newsletter-standard-20260516.md |

## Classificação

1. **Não é incidente crítico.** `issues=[]` e `protected_disabled=[]` no relatório recurring.
2. **É dívida de manutenção/contexto.** Skills >100KB no caminho always-on aumentam custo, latência e risco de contexto irrelevante.
3. **Não deve ser resolvido com auto-disable.** Lucas já aprovou que Skill Diet recorrente diagnostica; apply/restart/disable por cron continuam bloqueados.

## Proposta de curadoria

### P0 — `lk-operational-intelligence`

Impacto: resolve a maior parte dos warnings porque aparece em múltiplos profiles.

Recomendação segura:

- transformar o `SKILL.md` em **router curto** com gatilhos, guardrails e links;
- mover conteúdo longo para `references/` por tema;
- preservar o nome da skill e compatibilidade de chamadas atuais;
- não desabilitar automaticamente nos profiles nesta etapa.

Motivo: como a skill é usada por LK Growth, Ops, Shopify, Trends, LKGOC, Mordomo e Stock, desabilitar por profile pode quebrar contexto operacional. A primeira melhoria deve reduzir peso da skill, não remover capacidade.

### P1 — `lk-stock`

Impacto: 1 warning, mas no profile correto (`lk-stock`) e provavelmente é core.

Recomendação segura:

- manter habilitada no `lk-stock`;
- criar packet de split `SKILL.md` curto + `references/` por tópicos: Tiny truth, Shopify surface, Stock Cockpit, SKU/tamanho, Supabase read model, approval/write gates;
- qualquer mudança deve ter backup/readback e QA, mas não precisa restart se for só skill file local até a próxima carga.

### P2 — profile enablement audit

Depois do split P0/P1, reexecutar recurring audit. Só se warnings persistirem:

- revisar profile por profile se `lk-operational-intelligence` precisa ficar always-on ou virar lente sob demanda;
- preservar `lk-stock` no stock owner;
- nunca aplicar disable/restart sem approval packet.

## Próximo approval recomendado

Se Lucas quiser aplicar, o próximo pacote deve ser:

**Aprovar P0:** curar `lk-operational-intelligence` em modo local/documental, com backup, split para references, readback, secret scan, brain health e receipt; sem restart/gateway/cron/external writes.

## Evidências

- `reports/governance/skill-surface-diet-recurring/latest.json`
- `reports/daily-consolidation/2026-06-30.md`
- Task OS card: `t_c16fc3bf`
