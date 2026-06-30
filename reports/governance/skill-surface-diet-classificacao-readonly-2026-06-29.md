# Skill Surface Diet — classificação read-only por profile

Data: 2026-06-29T10:15:35Z  
Escopo: local/read-only/documental. Nenhuma skill, toolset, profile, cron ou runtime foi alterado.

## Veredito executivo

O problema **parece ser superfície ampla demais em alguns profiles**, não falta de skills. O maior peso observado está em `lk-collection-optimizer`, `lk-trends`, `lk-shopify`, `lk-stock` e `default`; `spiti` e `mordomo` ficam como P1 importante por volume alto e uso operacional. A próxima ação segura é curadoria por classe, não deleção.

## Ranking de superfície

| Profile | Skills | >=50k | >=90k | skill_view no state | Leitura |
|---|---:|---:|---:|---:|---|
| `lk-collection-optimizer` | 243 | 7 | 4 | 4 | P0 curadoria |
| `lk-trends` | 239 | 6 | 4 | 97 | P0 curadoria |
| `lk-shopify` | 234 | 10 | 5 | 1262 | P0 curadoria |
| `lk-stock` | 232 | 10 | 6 | 1232 | P0 curadoria |
| `default` | 227 | 8 | 3 | 6565 | P0 curadoria |
| `spiti` | 211 | 6 | 3 | 294 | P1 revisar |
| `mordomo` | 201 | 9 | 4 | 2705 | P1 revisar |
| `lk-ops` | 177 | 7 | 4 | 1475 | P1 revisar |
| `brain-process` | 169 | 3 | 2 | 3 | P1 revisar |
| `hermes-ops-readonly` | 169 | 3 | 2 | 5 | P1 revisar |
| `lk-content-reviewer` | 168 | 3 | 2 | 0 | P1 revisar |
| `lk-analyst-readonly` | 167 | 3 | 2 | 10 | P1 revisar |
| `lk-growth` | 159 | 6 | 3 | 1413 | OK/baixo peso |
| `lk-content` | 12 | 1 | 0 | 349 | OK/baixo peso |
| `lk-finance` | 9 | 0 | 0 | 82 | OK/baixo peso |
| `spiti-atendimento` | 8 | 0 | 0 | 61 | OK/baixo peso |
| `lc-claude-cli` | 4 | 0 | 0 | 0 | OK/baixo peso |

## Uso observado via `skill_view` em state.db

Esta é uma aproximação: conta chamadas registradas em `state.db` por profile; não prova inutilidade de skills sem uso recente.

## Limitações da heurística

- `skill_view` mede chamadas registradas, não utilidade real completa.
- Baixo uso pode significar profile novo, baixa atividade recente ou uso indireto por prompt/skill obrigatória.
- Tamanho em bytes é proxy imperfeito para custo de contexto; o custo real depende de quando a skill é carregada.
- “Candidata a baixar prioridade/escopo” significa **proposta documental**, não remoção, edição, desativação ou mudança de profile sem aprovação.
- “Profile-specific exemplos” é heurístico e precisa revisão humana antes de virar whitelist.

| Skill | Chamadas observadas |
|---|---:|
| `verification-before-completion` | 1335 |
| `hermes-agent` | 1134 |
| `doppler-secrets-operations` | 939 |
| `lk-shopify-readonly` | 756 |
| `multiempresa-routing-lucas` | 673 |
| `lucas-chief-of-staff` | 555 |
| `lk-stock` | 481 |
| `wacli-whatsapp-cli` | 447 |
| `lk-operational-intelligence` | 425 |
| `test-driven-development` | 411 |
| `lk-growth-operations` | 402 |
| `customer-chat-operations` | 387 |
| `lk-whatsapp-crm-automation` | 341 |
| `hermes-brain-governance` | 339 |
| `systematic-debugging` | 317 |
| `lk-seo-weekly-improvement` | 297 |
| `github-pr-workflow` | 290 |
| `lucas-hermes-continuous-improvement` | 271 |
| `google-workspace` | 267 |
| `lucas-runtime-operations` | 249 |

## Recomendações por profile foco


### `lk-collection-optimizer` — P0 curadoria (243 skills)

**Manter/proteger primeiro:** `lk-superpowers-collection-optimizer`, `brainstorming`, `doppler-secrets-operations`, `executing-plans`, `hermes-agent`, `hermes-central-integration-auth-broker`, `honcho-memory-operations`, `mcp-connections`, `native-mcp`, `verification-before-completion`

**Profile-specific exemplos heurísticos:** `blog`, `blog-analyze`, `blog-audio`, `blog-audit`, `blog-brief`, `blog-calendar`, `blog-cannibalization`, `blog-chart`, `blog-cluster`, `blog-factcheck`, `blog-flow`, `blog-geo`

**Candidatas a proposta de split SKILL.md curto + references:**

- `pytorch-fsdp` — 160,170 bytes — `mlops/training/pytorch-fsdp/SKILL.md`
- `research-paper-writing` — 103,375 bytes — `.archive/research/research-paper-writing/SKILL.md`
- `lk-operational-intelligence` — 100,458 bytes — `productivity/lk-operational-intelligence/SKILL.md`
- `lk-seo-weekly-improvement` — 98,163 bytes — `productivity/lk-seo-weekly-improvement/SKILL.md`
- `bruno-openclaw-hermes-brain-adaptation` — 88,352 bytes — `productivity/bruno-openclaw-hermes-brain-adaptation/SKILL.md`

**Candidatas a baixar prioridade/escopo, não remover:** `airtable`, `apple-notes`, `apple-reminders`, `architecture-diagram`, `arxiv`, `ascii-art`, `ascii-video`, `audiocraft-audio-generation`, `axolotl`, `baoyu-article-illustrator`, `baoyu-comic`, `baoyu-infographic`, `bruno-openclaw-hermes-brain-adaptation`, `claude-code`, `claude-design`


### `lk-trends` — P0 curadoria (239 skills)

**Manter/proteger primeiro:** `lk-trends-product-intelligence`, `google-workspace`, `doppler-secrets-operations`, `hermes-agent`, `lk-shopify-readonly`, `himalaya`, `lk-growth-operations`, `design-md`, `last30days`, `lk-operational-intelligence`

**Profile-specific exemplos heurísticos:** `ads`, `ads-amazon`, `ads-apple`, `ads-attribution`, `ads-audit`, `ads-budget`, `ads-competitor`, `ads-create`, `ads-creative`, `ads-dna`, `ads-generate`, `ads-google`

**Candidatas a proposta de split SKILL.md curto + references:**

- `pytorch-fsdp` — 160,170 bytes — `mlops/training/pytorch-fsdp/SKILL.md`
- `research-paper-writing` — 103,375 bytes — `.archive/research/research-paper-writing/SKILL.md`
- `lk-operational-intelligence` — 100,458 bytes — `productivity/lk-operational-intelligence/SKILL.md`
- `lk-seo-weekly-improvement` — 93,941 bytes — `productivity/lk-seo-weekly-improvement/SKILL.md`
- `bruno-openclaw-hermes-brain-adaptation` — 88,352 bytes — `productivity/bruno-openclaw-hermes-brain-adaptation/SKILL.md`

**Candidatas a baixar prioridade/escopo, não remover:** `airtable`, `apple-notes`, `apple-reminders`, `architecture-diagram`, `arxiv`, `ascii-art`, `ascii-video`, `audiocraft-audio-generation`, `axolotl`, `baoyu-article-illustrator`, `baoyu-comic`, `baoyu-infographic`, `blogwatcher`, `bruno-openclaw-hermes-brain-adaptation`, `claude-code`


### `lk-shopify` — P0 curadoria (234 skills)

**Manter/proteger primeiro:** `lk-shopify-readonly`, `lk-growth-operations`, `verification-before-completion`, `lk-shopify-variant-thumbnails`, `doppler-secrets-operations`, `github-pr-workflow`, `lk-shopify-theme-cro`, `lk-shopify-cart-drawer`, `doppler-github-pr-safe`, `lk-seo-weekly-improvement`

**Profile-specific exemplos heurísticos:** `ads-amazon`, `ads-apple`, `ads-creative`, `ads-photoshoot`, `ai-audio-music-production`, `airtable`, `apple-ecosystem-automation`, `architecture-diagram`, `blog`, `blog-analyze`, `blog-audio`, `blog-audit`

**Candidatas a proposta de split SKILL.md curto + references:**

- `pytorch-fsdp` — 160,170 bytes — `mlops/training/pytorch-fsdp/SKILL.md`
- `research-paper-writing` — 103,375 bytes — `research/research-paper-writing/SKILL.md`
- `lk-operational-intelligence` — 101,044 bytes — `productivity/lk-operational-intelligence/SKILL.md`
- `lk-seo-weekly-improvement` — 98,764 bytes — `productivity/lk-seo-weekly-improvement/SKILL.md`
- `lk-shopify-readonly` — 97,647 bytes — `productivity/lk-shopify-readonly/SKILL.md`

**Candidatas a baixar prioridade/escopo, não remover:** `apple-notes`, `apple-reminders`, `arxiv`, `ascii-art`, `ascii-video`, `audiocraft-audio-generation`, `axolotl`, `baoyu-article-illustrator`, `baoyu-comic`, `baoyu-infographic`, `blogwatcher`, `claude-code`, `claude-design`, `clip`, `codebase-inspection`


### `lk-stock` — P0 curadoria (232 skills)

**Manter/proteger primeiro:** `lk-stock`, `verification-before-completion`, `impeccable`, `test-driven-development`, `doppler-secrets-operations`, `vercel-deployments`, `superpowers`, `systematic-debugging`, `brainstorming`, `executing-plans`

**Profile-specific exemplos heurísticos:** `blog-taxonomy`, `hermes-central-integration-auth-broker`, `hostinger-vps-api-ssh-access`, `lk-gmc-operations`, `lk-inventory-hub`, `lk-operational-intelligence`, `lk-seo-weekly-improvement`, `lk-shopify-product-upload`, `lk-shopify-readonly`, `lk-stock`, `shopify`, `supabase-security-audit`

**Candidatas a proposta de split SKILL.md curto + references:**

- `pytorch-fsdp` — 160,170 bytes — `mlops/training/pytorch-fsdp/SKILL.md`
- `lk-operational-intelligence` — 104,229 bytes — `productivity/lk-operational-intelligence/SKILL.md`
- `research-paper-writing` — 103,375 bytes — `research/research-paper-writing/SKILL.md`
- `lk-stock` — 103,330 bytes — `productivity/lk-stock/SKILL.md`
- `bruno-openclaw-hermes-brain-adaptation` — 101,514 bytes — `productivity/bruno-openclaw-hermes-brain-adaptation/SKILL.md`

**Candidatas a baixar prioridade/escopo, não remover:** `airtable`, `apple-notes`, `apple-reminders`, `architecture-diagram`, `arxiv`, `ascii-art`, `ascii-video`, `audiocraft-audio-generation`, `axolotl`, `baoyu-article-illustrator`, `baoyu-comic`, `baoyu-infographic`, `blog`, `blog-analyze`, `blog-audio`


### `mordomo` — P1 revisar (201 skills)

**Manter/proteger primeiro:** `verification-before-completion`, `multiempresa-routing-lucas`, `lucas-chief-of-staff`, `wacli-whatsapp-cli`, `whatsapp-business-operations`, `test-driven-development`, `google-workspace`, `hermes-agent`, `doppler-secrets-operations`, `executing-plans`

**Profile-specific exemplos heurísticos:** `doppler-secrets-operations`, `google-workspace`, `himalaya`, `linear`, `lk-operational-intelligence`, `lk-report-delivery`, `maps`, `notion`, `pixel-ai-hub-learning-digest`, `popular-web-designs`, `seo-google`, `seo-maps`

**Candidatas a proposta de split SKILL.md curto + references:**

- `pytorch-fsdp` — 160,170 bytes — `mlops/training/pytorch-fsdp/SKILL.md`
- `research-paper-writing` — 103,375 bytes — `research/research-paper-writing/SKILL.md`
- `lk-operational-intelligence` — 102,461 bytes — `productivity/lk-operational-intelligence/SKILL.md`
- `bruno-openclaw-hermes-brain-adaptation` — 90,608 bytes — `productivity/bruno-openclaw-hermes-brain-adaptation/SKILL.md`
- `wacli-whatsapp-cli` — 73,056 bytes — `.archive/wacli-whatsapp-cli/SKILL.md`

**Candidatas a baixar prioridade/escopo, não remover:** `airtable`, `apple-notes`, `apple-reminders`, `architecture-diagram`, `arxiv`, `ascii-art`, `ascii-video`, `audiocraft-audio-generation`, `axolotl`, `baoyu-article-illustrator`, `baoyu-comic`, `baoyu-infographic`, `blog`, `blog-analyze`, `blog-audio`


### `spiti` — P1 revisar (211 skills)

**Manter/proteger primeiro:** `spiti-hub-pr-workflow`, `doppler-secrets-operations`, `spiti-operations`, `verification-before-completion`, `systematic-debugging`, `vercel-deployments`, `spiti-captacao-obras-intake`, `development-workflows`, `spiti-chatwoot-intelligence`, `spiti-os-readonly-status`

**Profile-specific exemplos heurísticos:** `codebase-inspection`, `doppler-github-pr-safe`, `github-auth`, `github-code-review`, `github-issues`, `github-pr-workflow`, `github-repo-management`, `github-workflows`, `google-workspace`, `hermes-council`, `linear`, `lucas-chief-of-staff`

**Candidatas a proposta de split SKILL.md curto + references:**

- `pytorch-fsdp` — 160,170 bytes — `mlops/training/pytorch-fsdp/SKILL.md`
- `lk-operational-intelligence` — 100,458 bytes — `productivity/lk-operational-intelligence/SKILL.md`
- `research-paper-writing` — 94,446 bytes — `.archive/research/research-paper-writing/SKILL.md`
- `bruno-openclaw-hermes-brain-adaptation` — 88,798 bytes — `productivity/bruno-openclaw-hermes-brain-adaptation/SKILL.md`
- `mission-control-development` — 58,449 bytes — `software-development/mission-control-development/SKILL.md`

**Candidatas a baixar prioridade/escopo, não remover:** `airtable`, `apple-notes`, `apple-reminders`, `architecture-diagram`, `arxiv`, `ascii-art`, `ascii-video`, `audiocraft-audio-generation`, `axolotl`, `baoyu-article-illustrator`, `baoyu-comic`, `baoyu-infographic`, `blog`, `blog-analyze`, `blog-audio`


### `lk-ops` — P1 revisar (177 skills)

**Manter/proteger primeiro:** `customer-chat-operations`, `verification-before-completion`, `lk-operations-suite`, `doppler-secrets-operations`, `lk-shopify-readonly`, `lk-operational-intelligence`, `systematic-debugging`, `wacli-whatsapp-cli`, `hostinger-vps-api-ssh-access`, `vercel-deployments`

**Profile-specific exemplos heurísticos:** `blog-taxonomy`, `customer-chat-operations`, `google-workspace`, `himalaya`, `lk-operational-intelligence`, `lk-operations-suite`, `lk-seo-weekly-improvement`, `lk-shopify-product-upload`, `lk-shopify-readonly`

**Candidatas a proposta de split SKILL.md curto + references:**

- `pytorch-fsdp` — 160,170 bytes — `mlops/training/pytorch-fsdp/SKILL.md`
- `lk-operational-intelligence` — 101,980 bytes — `productivity/lk-operational-intelligence/SKILL.md`
- `bruno-openclaw-hermes-brain-adaptation` — 101,515 bytes — `productivity/bruno-openclaw-hermes-brain-adaptation/SKILL.md`
- `customer-chat-operations` — 93,626 bytes — `productivity/customer-chat-operations/SKILL.md`
- `hermes-agent` — 69,265 bytes — `autonomous-ai-agents/hermes-agent/SKILL.md`

**Candidatas a baixar prioridade/escopo, não remover:** `airtable`, `architecture-diagram`, `ascii-art`, `ascii-video`, `audiocraft-audio-generation`, `axolotl`, `baoyu-article-illustrator`, `baoyu-comic`, `baoyu-infographic`, `blog`, `blog-analyze`, `blog-audio`, `blog-audit`, `blog-brief`, `blog-calendar`


### `lk-growth` — P2/baixo peso relativo (159 skills)

**Manter/proteger primeiro:** `lk-growth-operations`, `doppler-secrets-operations`, `lk-seo-weekly-improvement`, `lk-collection-patterns`, `seo-geo`, `lk-shopify-readonly`, `lk-collection-guide-patterns`, `hermes-agent`, `n8n-workflow-automation`, `verification-before-completion`

**Profile-specific exemplos heurísticos:** `ads`, `ads-amazon`, `ads-apple`, `ads-attribution`, `ads-audit`, `ads-budget`, `ads-competitor`, `ads-create`, `ads-creative`, `ads-dna`, `ads-generate`, `ads-google`

**Candidatas a proposta de split SKILL.md curto + references:**

- `pytorch-fsdp` — 160,170 bytes — `mlops/training/pytorch-fsdp/SKILL.md`
- `lk-operational-intelligence` — 101,044 bytes — `productivity/lk-operational-intelligence/SKILL.md`
- `lk-seo-weekly-improvement` — 98,196 bytes — `productivity/lk-seo-weekly-improvement/SKILL.md`
- `bruno-openclaw-hermes-brain-adaptation` — 88,938 bytes — `productivity/bruno-openclaw-hermes-brain-adaptation/SKILL.md`
- `mission-control-development` — 54,958 bytes — `.archive/mission-control-development/SKILL.md`

**Candidatas a baixar prioridade/escopo, não remover:** `audiocraft-audio-generation`, `axolotl`, `clip`, `dispatching-parallel-agents`, `evaluating-llms-harness`, `find-nearby`, `fine-tuning-with-trl`, `finishing-a-development-branch`, `gguf-quantization`, `godmode`, `grpo-rl-training`, `guidance`, `hermes-central-integration-auth-broker`, `hermes-council`, `himalaya`


### `hermes-ops-readonly` — P1 revisar (169 skills)

**Manter/proteger primeiro:** `hermes-agent`, `lucas-hermes-continuous-improvement`, `doppler-secrets-operations`, `hermes-central-integration-auth-broker`, `honcho-memory-operations`, `native-mcp`

**Profile-specific exemplos heurísticos:** _não classificado automaticamente_

**Candidatas a proposta de split SKILL.md curto + references:**

- `pytorch-fsdp` — 160,170 bytes — `mlops/training/pytorch-fsdp/SKILL.md`
- `research-paper-writing` — 103,375 bytes — `research/research-paper-writing/SKILL.md`
- `bruno-openclaw-hermes-brain-adaptation` — 77,022 bytes — `productivity/bruno-openclaw-hermes-brain-adaptation/SKILL.md`

**Candidatas a baixar prioridade/escopo, não remover:** `airtable`, `apple-notes`, `apple-reminders`, `architecture-diagram`, `arxiv`, `ascii-art`, `ascii-video`, `audiocraft-audio-generation`, `axolotl`, `baoyu-comic`, `baoyu-infographic`, `blog`, `blog-analyze`, `blog-audio`, `blog-audit`


### `brain-process` — P1 revisar (169 skills)

**Manter/proteger primeiro:** `lucas-hermes-continuous-improvement`, `hermes-agent`, `doppler-secrets-operations`, `hermes-central-integration-auth-broker`, `honcho-memory-operations`, `native-mcp`

**Profile-specific exemplos heurísticos:** _não classificado automaticamente_

**Candidatas a proposta de split SKILL.md curto + references:**

- `pytorch-fsdp` — 160,170 bytes — `mlops/training/pytorch-fsdp/SKILL.md`
- `research-paper-writing` — 103,375 bytes — `research/research-paper-writing/SKILL.md`
- `bruno-openclaw-hermes-brain-adaptation` — 77,022 bytes — `productivity/bruno-openclaw-hermes-brain-adaptation/SKILL.md`

**Candidatas a baixar prioridade/escopo, não remover:** `airtable`, `apple-notes`, `apple-reminders`, `architecture-diagram`, `arxiv`, `ascii-art`, `ascii-video`, `audiocraft-audio-generation`, `axolotl`, `baoyu-comic`, `baoyu-infographic`, `blog`, `blog-analyze`, `blog-audio`, `blog-audit`


### `lk-content-reviewer` — P1 revisar (168 skills)

**Manter/proteger primeiro:** `doppler-secrets-operations`, `hermes-agent`, `hermes-central-integration-auth-broker`, `honcho-memory-operations`, `native-mcp`

**Profile-specific exemplos heurísticos:** _não classificado automaticamente_

**Candidatas a proposta de split SKILL.md curto + references:**

- `pytorch-fsdp` — 160,170 bytes — `mlops/training/pytorch-fsdp/SKILL.md`
- `research-paper-writing` — 103,375 bytes — `research/research-paper-writing/SKILL.md`
- `bruno-openclaw-hermes-brain-adaptation` — 77,022 bytes — `productivity/bruno-openclaw-hermes-brain-adaptation/SKILL.md`

**Candidatas a baixar prioridade/escopo, não remover:** `airtable`, `apple-notes`, `apple-reminders`, `architecture-diagram`, `arxiv`, `ascii-art`, `ascii-video`, `audiocraft-audio-generation`, `axolotl`, `baoyu-comic`, `baoyu-infographic`, `blog`, `blog-analyze`, `blog-audio`, `blog-audit`


### `lk-analyst-readonly` — P1 revisar (167 skills)

**Manter/proteger primeiro:** `doppler-secrets-operations`, `metricool-api-analytics`, `google-workspace`, `lucas-chief-of-staff`, `hermes-agent`, `hermes-central-integration-auth-broker`, `honcho-memory-operations`, `native-mcp`

**Profile-specific exemplos heurísticos:** _não classificado automaticamente_

**Candidatas a proposta de split SKILL.md curto + references:**

- `pytorch-fsdp` — 160,170 bytes — `mlops/training/pytorch-fsdp/SKILL.md`
- `research-paper-writing` — 103,375 bytes — `research/research-paper-writing/SKILL.md`
- `bruno-openclaw-hermes-brain-adaptation` — 77,022 bytes — `productivity/bruno-openclaw-hermes-brain-adaptation/SKILL.md`

**Candidatas a baixar prioridade/escopo, não remover:** `airtable`, `apple-notes`, `apple-reminders`, `architecture-diagram`, `arxiv`, `ascii-art`, `ascii-video`, `audiocraft-audio-generation`, `axolotl`, `baoyu-comic`, `baoyu-infographic`, `blog`, `blog-analyze`, `blog-audio`, `blog-audit`


### `lk-content` — P2/baixo peso (12 skills)

**Manter/proteger primeiro:** `lk-content-klaviyo-campaign-operations`, `doppler-secrets-operations`, `lk-content-editorial-calendar`, `lk-content-dashboard-product-ui`, `ui-ux-pro-max`, `vercel-next-security-deploy-fix`, `hermes-specialist-profile-setup`, `specialist-profile-activation`, `hermes-central-integration-auth-broker`, `honcho-memory-operations`

**Profile-specific exemplos heurísticos:** _não classificado automaticamente_

**Candidatas a proposta de split SKILL.md curto + references:**

- `lk-content-klaviyo-campaign-operations` — 88,827 bytes — `operations/lk-content-klaviyo-campaign-operations/SKILL.md`


### `lk-finance` — P2/baixo peso (9 skills)

**Manter/proteger primeiro:** `lk-finance`, `lk-stock-ops-automation`, `doppler-secrets-operations`, `lk-operational-automations`, `lk-ops-whatsapp-automation`, `lk-tiny`, `hermes-central-integration-auth-broker`, `honcho-memory-operations`

**Profile-specific exemplos heurísticos:** _não classificado automaticamente_


### `spiti-atendimento` — P2/baixo peso (8 skills)

**Manter/proteger primeiro:** `spiti-chatwoot-intelligence`, `doppler-secrets-operations`, `hostinger-vps-api-ssh-access`, `verification-before-completion`, `hermes-central-integration-auth-broker`, `spiti-captacao-obras-intake`, `honcho-memory-operations`

**Profile-specific exemplos heurísticos:** _não classificado automaticamente_


### `lc-claude-cli` — P2/baixo peso (4 skills)

**Manter/proteger primeiro:** `doppler-secrets-operations`, `hermes-central-integration-auth-broker`, `honcho-memory-operations`

**Profile-specific exemplos heurísticos:** _não classificado automaticamente_


### `default` — P0 curadoria, mas como orquestrador central (227 skills)

**Manter/proteger primeiro:** `hermes-agent`, `verification-before-completion`, `multiempresa-routing-lucas`, `hermes-brain-governance`, `doppler-secrets-operations`, `lk-operational-intelligence`, `lucas-hermes-continuous-improvement`, `lucas-chief-of-staff`, `lk-shopify-readonly`, `bruno-openclaw-hermes-brain-adaptation`

**Profile-specific exemplos heurísticos:** _não classificado automaticamente_

**Candidatas a proposta de split SKILL.md curto + references:**

- `bruno-openclaw-hermes-brain-adaptation` — 100,652 bytes — `productivity/bruno-openclaw-hermes-brain-adaptation/SKILL.md`
- `research-paper-writing` — 94,446 bytes — `research/research-paper-writing/SKILL.md`
- `hermes-agent` — 92,317 bytes — `autonomous-ai-agents/hermes-agent/SKILL.md`
- `lucas-hermes-continuous-improvement` — 87,529 bytes — `devops/lucas-hermes-continuous-improvement/SKILL.md`
- `lk-operational-intelligence` — 87,093 bytes — `productivity/lk-operational-intelligence/SKILL.md`

**Candidatas a baixar prioridade/escopo, não remover:** `airtable`, `apple-notes`, `apple-reminders`, `arxiv`, `ascii-art`, `ascii-video`, `audiocraft-audio-generation`, `axolotl`, `baoyu-article-illustrator`, `baoyu-comic`, `baoyu-infographic`, `blog-analyze`, `blog-audio`, `blog-audit`, `blog-calendar`


## QA independente

QA independente inicial marcou **FAIL antes de patch** por: inconsistências P0/P1/risco, claims fortes demais e necessidade de explicitar limitações da heurística.

Correções aplicadas antes do fechamento:

- taxonomia normalizada para P0/P1/P2 nas seções;
- `default` explicitado como P0/orquestrador central;
- `spiti` e `mordomo` mantidos como P1 importante, não P0;
- claims fortes suavizados para “parece/observado/proposta documental”;
- seção “Limitações da heurística” adicionada;
- wording reforçado: nenhuma edição/deleção/desativação/profile change sem aprovação.


## Plano de ação seguro

1. **Não deletar nada agora.**  
2. Para cada profile P0, produzir **proposta documental** de 20–40 skills candidatas a “visíveis por default” e restante sob demanda; não aplicar no profile sem approval.  
3. Skills gigantes: propor split em `SKILL.md` curto + `references/`; implementação exige aprovação específica se alterar skills. Bytes são proxy, não medição direta de custo de prompt.  
4. Duplicadas/sobrepostas: consolidar só após diff e approval específico.  
5. Toolsets: apenas reportar candidatos; nenhuma mudança sem approval runtime/profile.


## Próxima onda recomendada

Começar por `lk-collection-optimizer`, porque é o maior surface observado e tem fronteira operacional clara no Brain/AGENTS como LKGOC. Produzir uma proposta documental de whitelist/always-on + on-demand, sem editar o profile ainda.


## Não realizado

- Nenhuma skill editada/movida/deletada.
- Nenhum toolset/profile config alterado.
- Nenhum cron/gateway/Docker/VPS tocado.
- Nenhuma credencial lida ou impressa.
- Nenhum write externo ou mutação de produção.
