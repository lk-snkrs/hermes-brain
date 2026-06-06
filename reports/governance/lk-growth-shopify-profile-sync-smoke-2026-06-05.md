# LK Growth / LK Shopify profile-local sync smoke — 2026-06-05

Timestamp: 2026-06-05T20:34:39+00:00

## Scope

Read-only/local documentation and skill synchronization only. No Shopify, Tiny, GMC, theme, cron, bot, Docker, VPS, customer or external write was executed.

## Smoke prompts and expected routing

### 1. LK Growth — GMC/Product Data packet

Prompt: `crie um packet GMC/Product Data da LK`

Expected:
- owner agent: LK Growth;
- playbook: GMC/Product Data;
- workers: Data Scout + GMC/Product Data Analyst + Governor/Critic, plus only necessary specialists;
- all workers: no, only minimum subset;
- approval: no GMC/Shopify/feed/price/stock write without scoped approval;
- handoff: LK Shopify only if a Shopify-surface execution packet is needed.

### 2. LK Shopify — cart drawer/minicart

Prompt: `corrigir cart drawer/minicart da LK`

Expected:
- owner agent: LK Shopify;
- playbook: cart drawer/minicart/site feature;
- workers: Surface Mapper + Theme/Feature Architect + CRO/Purchase Flow + Preview/Diff + QA/Rollback as needed;
- all workers: no, only minimum subset;
- approval: no dev/prod Shopify theme write without scoped approval; production approval is separate;
- handoff: Growth only for hypothesis/impact; LKGOC only for collection-optimizer scope.

### 3. Mixed Growth → Shopify

Prompt: `hipótese CRO para PDP que exige mudar o tema Shopify`

Expected:
- LK Growth owns hypothesis/evidence/scoring/packet;
- LK Shopify owns Shopify-surface preview/QA/readback/rollback/execution after handoff and approval;
- Hermes Geral/default must not create the final operational packet by convenience.

### 4. LKGOC boundary

Prompt: `otimizar coleção LKGOC Adidas Samba Jane`

Expected:
- owner agent: `[LK] Otimização de Coleções` / `lk-collection-optimizer`;
- LK Growth and LK Shopify do not claim ownership;
- LK Shopify only re-enters if the collection optimizer hands back a scoped Shopify-surface execution packet.

## Files synchronized

LK Growth profile:
- `/opt/data/profiles/lk-growth/skills/productivity/lk-growth-operations/SKILL.md`
- `/opt/data/profiles/lk-growth/skills/productivity/lk-seo-weekly-improvement/SKILL.md`
- `/opt/data/profiles/lk-growth/skills/productivity/lk-growth-operations/references/lk-growth-agent-worker-playbooks-20260605.md`
- `/opt/data/profiles/lk-growth/skills/productivity/lk-seo-weekly-improvement/references/lk-growth-agent-worker-playbooks-20260605.md`

LK Shopify profile:
- `/opt/data/profiles/lk-shopify/skills/productivity/lk-shopify-readonly/SKILL.md`
- `/opt/data/profiles/lk-shopify/skills/productivity/lk-shopify-cart-drawer/SKILL.md`
- `/opt/data/profiles/lk-shopify/skills/productivity/lk-growth-operations/SKILL.md`
- `/opt/data/profiles/lk-shopify/skills/productivity/lk-shopify-readonly/references/lk-shopify-agent-worker-playbooks-20260605.md`
- `/opt/data/profiles/lk-shopify/skills/productivity/lk-shopify-cart-drawer/references/lk-shopify-agent-worker-playbooks-20260605.md`

## Verification criteria

Static verification checks:
- all profile-local files exist;
- owner/handoff markers are present;
- canonical Brain playbook indexes exist;
- no new credential values are stored in the new reference docs;
- smoke prompt expected outputs are explicitly represented in profile-local skills/references.

Runtime note:
- Profile gateways were not restarted and no live Telegram round-trip was triggered in this step.
- CLI one-shot model smoke is not treated as authoritative unless the exact profile-local skill resolution is proven; the durable source of truth is the profile-local skill content above plus future Telegram/profile round-trip.
