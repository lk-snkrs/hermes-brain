# Índice de Skills — Hermes Brain

Skills são processos repetíveis com entrada, passos, saída e verificação. Este índice aponta skills canônicas e navegação por área.

## Skills canônicas versionadas

| Skill | Caminho | Área | Função |
|-------|---------|------|--------|
| Hermes Brain | `skills/hermes-brain/SKILL.md` | Operações | Uso do Brain como fonte de verdade |
| Session Start Protocol | `skills/session-start-protocol/SKILL.md` | Operações | Boot/checklist de sessão |
| Brain Sync | `skills/brain-sync/SKILL.md` | Operações | Sincronização do Brain |
| LK Cross-sell | `skills/lk-crosssell/SKILL.md` | LK CRM | Oportunidades de cross-sell pós-pedido |
| LK Leads Esfriando | `skills/lk-leads-esfriando/SKILL.md` | LK CRM | Reativação/risco de churn |
| LK Shopify Read-only | `skills/lk-shopify-readonly/SKILL.md` | LK Ecommerce | Consultas seguras no Shopify LK sem writes, envios ou alterações de produção |
| LK Shopify Product Upload | `skills/lk-shopify-product-upload/SKILL.md` | LK Ecommerce | Cadastro seguro de produtos Shopify com GOAT, pesquisa histórica, SEO, preview e aprovação |
| LK SEO Weekly Improvement | `skills/lk-seo-weekly-improvement/SKILL.md` | LK SEO/CRO | Processo semanal de nota Claude SEO, metas e fila de melhoria de páginas/PDPs |
| Lucas Hermes Continuous Improvement | `skills/lucas-hermes-continuous-improvement/SKILL.md` | Operações | Varredura contínua de melhorias Hermes/LK em modo seguro, read-only/local por padrão |

## Navegação por área

| Skill de área | Caminho | Fonte canônica |
|---------------|---------|----------------|
| Cross-sell LK | `areas/lk/sub-areas/crm/skills/cross-sell/SKILL.md` | `skills/lk-crosssell/SKILL.md` |
| Leads Esfriando LK | `areas/lk/sub-areas/crm/skills/leads-esfriando/SKILL.md` | `skills/lk-leads-esfriando/SKILL.md` |
| Brain Sync Operações | `areas/operacoes/skills/brain-sync/SKILL.md` | `skills/brain-sync/SKILL.md` |
| Shopify Read-only LK | `skills/lk-shopify-readonly/SKILL.md` | `skills/lk-shopify-readonly/SKILL.md` |
| Shopify Product Upload LK | `skills/lk-shopify-product-upload/SKILL.md` | `skills/lk-shopify-product-upload/SKILL.md` |
| SEO/CRO Weekly LK | `skills/lk-seo-weekly-improvement/SKILL.md` | `skills/lk-seo-weekly-improvement/SKILL.md` |

## Templates

- Template de skill de negócio: `empresa/skills/_templates/HERMES-BUSINESS-SKILL-TEMPLATE.md`.

## Regras

- Não duplicar lógica operacional sem atualizar a skill canônica.
- Toda skill que usa credenciais deve listar nomes de secrets Doppler, nunca valores.
- Toda skill que produz ação externa deve explicitar aprovação necessária.
- Se um workflow virar recorrente, documentar como skill ou rotina.
