# Skill Surface Diet — proposta de superfície LK Trends

Data: 2026-06-29
Escopo: **read-only/documental**. Nenhuma skill, config, toolset, gateway, cron ou runtime foi alterado.

## Veredito executivo

Depois do LKGOC, o próximo P0 natural é `lk-trends`: alto volume de skills e papel bem definido. A dieta recomendada aqui é **radar/sourcing intelligence first**, não SEO/content first. SEO, blog, newsletter e Shopify entram como lentes/handoffs depois que a oportunidade comercial está justificada.

## Tese operacional

- Core de LK Trends = detectar produto/modelo/colorway bombando fora do Brasil, validar sinal Brasil/LK e classificar rota segura.
- Não deve começar por SEO, conteúdo, PDP ou campanha.
- Não compra, reserva, negocia, promete disponibilidade/preço nem publica.
- Handoff obrigatório para `lk-shopify`, `lk-stock`, `lk-growth` ou Lucas/Compras conforme a rota.

## Core mínimo proposto

| Skill | Por quê |
|---|---|
| `lk-trends-product-intelligence` | Skill principal do domínio: radar, sourcing, watchlist, catalog-preview. |
| `last30days` | Recent web/social/editorial freshness para sinais atuais. |
| `lk-shopify-readonly` | Readback LK catálogo/PDP/coleções sem mutação. |
| `lk-operational-intelligence` | Contexto operacional LK quando read-only e relevante. |
| `google-workspace` | Documentos/Sheets/Calendar quando fonte interna aprovada/read-only. |
| `verification-before-completion` | Gate antes de afirmar oportunidade/decisão pronta. |
| `multiempresa-routing-lucas` | Evita misturar LK/Zipper/SPITI/pessoal e força handoff correto. |


## Skills protegidas / não desativar cegamente

Antes de qualquer aplicação em `skills.platform_disabled.telegram`, estas skills devem permanecer disponíveis ou explicitamente justificadas como lente sob demanda protegida:

- `lk-trends-product-intelligence` — domínio principal.
- `superpowers` — regra do próprio profile para PRDs e modo operacional proporcional.
- `verification-before-completion` — gate de fechamento.
- `multiempresa-routing-lucas` — fronteiras multiempresa/handoff.
- `lk-shopify-readonly` — cross-check LK sem mutação.
- `lk-operational-intelligence` — contexto LK read-only quando aplicável.
- `honcho-memory-operations` — obrigatório quando a tarefa envolver Honcho/memória/histórico/política.
- `doppler-secrets-operations` e `hermes-central-integration-auth-broker` — obrigatórios quando houver integração/CLI/auth, sempre sem imprimir valores.

**Importante:** “despriorizar no Telegram” significa reduzir superfície/autocomplete e carga contextual, não apagar, mover, desinstalar ou bloquear uso sob demanda quando a tarefa exige.

## Lentes sob demanda

### Market/social/recent web
`last30days`, `xurl`, `xitter`, `youtube-content`, `blogwatcher`

### Resale/LK read-only
`lk-shopify-readonly`, `lk-operational-intelligence`, `seo-dataforseo`, `google-workspace`

### Content/newsletter downstream
`blog-brief`, `blog-write`, `blog-rewrite`, `blog-schema`, `blog-factcheck`, `seo-content`, `seo-ecommerce`

### Governance/auth/support
`hermes-agent`, `honcho-memory-operations`, `doppler-secrets-operations`, `hermes-central-integration-auth-broker`, `brainstorming`, `executing-plans`

### Handoff profiles
`lk-shopify-product-upload`, `lk-growth-operations`

## Handoffs e bloqueios

| Caso | Dono correto |
|---|---|
| produto/listagem/PDP/Shopify/theme/metafields/publicação | profile `lk-shopify`; skill `lk-shopify-product-upload` só para empacotar contexto/preview, não para write por LK Trends |
| estoque, grade, disponibilidade, ruptura, SKU/Tiny/Shopify divergente | profile `lk-stock` — handoff crítico protegido |
| SEO/GEO/CRO/campanha/conteúdo após decisão comercial | `lk-growth` / `lk-content` conforme caso |
| compra, reserva, negociação, fornecedor, orçamento | Lucas/Compras com aprovação explícita |

## Top uso observado no profile

| Skill | use_count | bytes |
|---|---:|---:|
| `doppler-secrets-operations` | 356 | 18,887 |
| `lk-operational-intelligence` | 295 | 100,458 |
| `lk-seo-weekly-improvement` | 243 | 93,941 |
| `multiempresa-routing-lucas` | 231 | 16,479 |
| `lk-shopify-readonly` | 197 | 34,875 |
| `lucas-chief-of-staff` | 162 | 25,487 |
| `vercel-deployments` | 108 | 21,669 |
| `doppler-github-pr-safe` | 98 | 8,346 |
| `lucas-hermes-continuous-improvement` | 90 | 31,151 |
| `bruno-openclaw-hermes-brain-adaptation` | 88 | 88,352 |
| `mission-control-development` | 77 | 54,999 |
| `verification-before-completion` | 74 | 4,334 |
| `lk-trends-product-intelligence` | 46 | 27,317 |
| `seo-geo` | 30 | 9,778 |

## Skills grandes — candidatas a split/references ou sob demanda

| Skill | bytes | Proposta |
|---|---:|---|
| `pytorch-fsdp` | 160,170 | manter sob demanda; se for carregada com frequência, split SKILL.md curto + references |
| `research-paper-writing` | 103,375 | manter sob demanda; se for carregada com frequência, split SKILL.md curto + references |
| `lk-operational-intelligence` | 100,458 | core mas revisar tamanho se crescer; manter carregável |
| `lk-seo-weekly-improvement` | 93,941 | manter sob demanda; se for carregada com frequência, split SKILL.md curto + references |
| `bruno-openclaw-hermes-brain-adaptation` | 88,352 | manter sob demanda; se for carregada com frequência, split SKILL.md curto + references |
| `mission-control-development` | 54,999 | manter sob demanda; se for carregada com frequência, split SKILL.md curto + references |

## Fora do core — amostra para despriorizar no Telegram

`lk-seo-weekly-improvement`, `lucas-chief-of-staff`, `vercel-deployments`, `doppler-github-pr-safe`, `lucas-hermes-continuous-improvement`, `bruno-openclaw-hermes-brain-adaptation`, `mission-control-development`, `seo-geo`, `n8n-workflow-automation`, `telegram-hermes-docker-troubleshooting`, `seo-google`, `metricool-api-analytics`, `hostinger-vps-api-ssh-access`, `hermes-council`, `seo-page`, `writing-skills`, `seo`, `seo-audit`, `blog`, `spiti-hub-pr-workflow`, `kanban-worker`, `seo-schema`, `blog-google`, `seo-technical`, `dispatching-parallel-agents`, `software-delivery-workflows`, `code-debugging-operations`, `media-content-operations`, `gaming-agent-workflows`, `ads`, `ads-google`, `blog-image`, `seo-backlinks`, `ads-meta`, `whisper`, `seo-plan`, `pytorch-fsdp`, `research-paper-writing`, `claude-code`


## Guardrail antes de aplicar

Se Lucas aprovar aplicação real no `lk-trends`, a próxima etapa deve produzir um dry-run da lista final `enabled/disabled` e provar que nenhuma skill protegida será desativada. Só depois fazer backup, patch de AGENTS/skill principal/config, readback, eventual restart local do profile e receipt.

## Próximo passo se Lucas aprovar aplicação

Preparar e aplicar **camada leve** igual ao LKGOC:

1. backup de `AGENTS.md`, skill principal e `config.yaml`;
2. patch documental de política de tiers;
3. `skills.platform_disabled.telegram` específico para `lk-trends`;
4. readback com `get_disabled_skills`;
5. restart apenas do profile `lk-trends` se Lucas aprovar ativação runtime;
6. receipt + Brain health + secret scan.


## QA independente aplicado

QA independente marcou o primeiro draft como read-only OK e alinhado a LK Trends radar/sourcing-first, mas pediu correções antes de aplicação: proteger `superpowers`, separar core/lentes/despriorização, corrigir handoff profile vs skill, destacar `lk-stock`, e exigir dry-run antes de qualquer config change. Essas correções foram incorporadas neste relatório.

## Não realizado

- no skill edited/moved/deleted.
- no config/toolset/runtime changed.
- no gateway restart.
- no external write.

