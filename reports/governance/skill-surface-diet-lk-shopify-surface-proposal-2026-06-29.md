# Skill Surface Diet — LK Shopify surface proposal

Data: 2026-06-29T11:39:39Z
Status QA: **corrigido após QA independente**.
Modo: **documental/read-only**. Nenhuma alteração aplicada em profile/config/runtime.

## Decisão de escopo

Depois de LKGOC e LK Trends, o próximo P0 de maior impacto é `lk-shopify`: profile de alto risco operacional porque combina leitura Shopify, produto/upload, tema/CRO, GitHub, QA e integrações. A dieta precisa ser conservadora: reduzir ruído no Telegram sem remover capacidade de preview, approval, readback, rollback e PR/GitHub seguro.

## Princípio

**LK Shopify = superfície operacional Shopify first.** Não é Growth amplo, não é estoque/Tiny truth, não é Trends/sourcing, não é LKGOC. O profile deve carregar primeiro o que ajuda a preparar preview/approval/readback/rollback de superfície Shopify, mantendo qualquer write bloqueado por aprovação escopada.

## Core mínimo proposto para Telegram

| Skill | Por quê |
|---|---|
| `lk-shopify-readonly` | leitura Shopify/Admin/catálogo/pedido/produto sem mutação |
| `lk-shopify-product-upload` | produto novo/listagem/draft/preview; dono lógico de upload |
| `lk-shopify-theme-cro` | tema, Liquid/CSS/JS, DEV/Production, QA visual/readback |
| `lk-shopify-cart-drawer` | cart/minicart/cross-sell/upsell quando a superfície é Shopify |
| `lk-shopify-variant-thumbnails` | variante/imagem/thumb específica de PDP/Shopify |
| `multiempresa-routing-lucas` | evita rotas multiempresa erradas |
| `verification-before-completion` | não declarar write/QA concluído sem readback |
| `superpowers` | modo operacional proporcional para PRD/plan/risco/execução |

## Lentes sob demanda protegidas

| Lente | Skills ativas preservadas |
|---|---|
| Governança/auth/runtime | `honcho-memory-operations`, `doppler-secrets-operations`, `hermes-central-integration-auth-broker`, `hermes-agent` |
| Planejamento/execução | `brainstorming`, `executing-plans` |
| GitHub/theme source of truth | `github-operations`, `doppler-github-pr-safe`, `codebase-inspection` |
| Rollback/dev workflow | `systematic-debugging`, `using-git-worktrees`, `finishing-a-development-branch`, `receiving-code-review`, `requesting-code-review`, `test-driven-development` |
| QA visual/public storefront | `dogfood` + browser/tooling quando disponível. `playwright-cli`/`playwright-trace` não existem como skills ativas neste profile; não são prometidas como preservadas. |
| LK context/handoff | `lk-operational-intelligence`, `lk-growth-operations` |
| SEO/content downstream | `seo-content`, `seo-ecommerce`, `seo-page`, `seo-google`, `blog-brief`, `blog-write`, `blog-rewrite` |
| Workspace/docs | `google-workspace` |
| Trends/social/context | `last30days`, `xurl`, `youtube-content` |
| MCP/webhook suporte | `mcp-connections`, `native-mcp`, `webhook-subscriptions` somente quando a tarefa envolver essas superfícies |

## Handoffs obrigatórios

- Estoque, disponibilidade, grade, ruptura, Tiny e divergência SKU/Tiny/Shopify → `lk-stock`.
- SEO/GEO/CRO hipótese, impacto, GMC/analytics/campanha/conteúdo estratégico → `lk-growth`.
- Tendência/sourcing/oportunidade de compra → `lk-trends`.
- LKGOC/coleções/Guia LK/source pages de coleção → `lk-collection-optimizer`, com retorno para LK Shopify só por packet de superfície.
- Compras, negociação, fornecedor, reserva ou preço sem fonte aprovada → Lucas/Compras.

## Dry-run preliminar — se aplicado depois

- Skills ativas únicas: `194`; arquivadas únicas: `37`.
- Habilitadas propostas no Telegram: `40`.
- Desabilitadas propostas no Telegram: `154`.
- Escopo sugerido: `skills.platform_disabled.telegram` apenas; manter CLI/global amplo.

## Missing/arquivadas relevantes

- Missing ativas: nenhuma
- Arquivadas/não ativas: `github-pr-workflow`

## Correções aplicadas após QA independente

- removed non-existent playwright skills from protected enabled list; stated QA visual via dogfood/browser/tooling
- replaced archived github-pr-workflow with active doppler-github-pr-safe plus github-operations
- added rollback/dev workflow lens: systematic-debugging, using-git-worktrees, finishing-a-development-branch, receiving/requesting-code-review, test-driven-development
- added runtime/webhook/MCP support lens as on-demand, not core

## Fora do core / candidatos a ocultar no Telegram

Categorias típicas: ads amplos, ML/MLOps, gaming, Apple/iMessage, creative/media gen, academic research, unrelated devops, personal productivity, broad blog/SEO strategy not tied to Shopify surface, autonomous coding agents salvo quando GitHub/theme exigir.

Amostra:
`ads`, `ads-amazon`, `ads-apple`, `ads-attribution`, `ads-audit`, `ads-budget`, `ads-competitor`, `ads-create`, `ads-creative`, `ads-dna`, `ads-generate`, `ads-google`, `ads-landing`, `ads-linkedin`, `ads-math`, `ads-meta`, `ads-microsoft`, `ads-photoshoot`, `ads-plan`, `ads-server-side-tracking`, `ads-test`, `ads-tiktok`, `ads-youtube`, `ai-audio-music-production`, `airtable`, `apple-ecosystem-automation`, `arxiv`, `ascii-media`, `axolotl`, `baoyu-visual-storytelling`, `blog`, `blog-analyze`, `blog-audio`, `blog-audit`, `blog-calendar`, `blog-cannibalization`, `blog-chart`, `blog-cluster`, `blog-factcheck`, `blog-flow`, `blog-geo`, `blog-google`, `blog-image`, `blog-locale-audit`, `blog-localize`, `blog-multilingual`, `blog-notebooklm`, `blog-outline`, `blog-persona`, `blog-repurpose`, `blog-schema`, `blog-seo-check`, `blog-strategy`, `blog-taxonomy`, `blog-translate`, `blogwatcher`, `browser-design-artifacts`, `bruno-openclaw-hermes-brain-adaptation`, `clip`, `coding-agent-delegation`, `comfyui`, `dispatching-parallel-agents`, `dspy`, `evaluating-llms-harness`, `excalidraw`, `find-nearby`, `fine-tuning-with-trl`, `gguf-quantization`, `gif-search`, `godmode`, `grpo-rl-training`, `guidance`, `hermes-council`, `himalaya`, `hostinger-vps-api-ssh-access`, `huggingface-hub`, `humanizer`, `ideation`, `impeccable`, `jupyter-live-kernel`

## Guardrail antes de aplicar

Para aplicar de verdade: (1) validar dry-run recalculado, (2) provar skills protegidas habilitadas, (3) backup de `AGENTS.md`, skill principal e `config.yaml`, (4) patch scoped em `skills.platform_disabled.telegram`, (5) readback helper, (6) restart local apenas `lk-shopify`, (7) receipt. Qualquer Shopify/GitHub/Tiny/Klaviyo write continua bloqueado por aprovação própria.

## Não-ações desta etapa

- no AGENTS patch
- no skill patch
- no config.yaml patch
- no gateway restart
- no Shopify/Tiny/GitHub/Klaviyo writes
- no credential access values printed

## Caveat

`lk-shopify/config.yaml` ainda aparece em `_config_version: 23` no readback. Migração de config v23→v30 não está incluída nesta etapa documental; se Lucas aprovar aplicação futura, pode ser migrada como etapa separada com backup/restart local.