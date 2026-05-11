# Shopify Product Upload Skill Operationalization — 2026-05-11

## Why this exists

Lucas challenged whether the newly created Shopify product upload skill was really “100%”. The learning: for Lucas/Hermes Brain, a business workflow skill is not operational just because it exists in the runtime skill library. It must also be versioned, indexed, checked, merged, and synced.

## Verified standard used

Before reporting “100% installed/operational” for `lk-shopify-product-upload`, verify:

- Runtime library: `skill_view('lk-shopify-product-upload')` loads.
- Hermes Brain canonical copy: `skills/lk-shopify-product-upload/SKILL.md` exists.
- Brain index: `empresa/skills/_index.md` references the skill in canonical skills and navigation.
- Related routing: `lk-shopify-readonly` points product-upload/GOAT/`!subir` cases to this skill instead of treating them as read-only Shopify analysis.
- Checks:
  - `python3 scripts/brain_health_check.py` → all checks passed.
  - `git diff --check` → passed.
  - changed-file secret scan → no real secrets; Shopify header examples must use env placeholders only.
- GitHub lifecycle: branch/PR created, merged, and local `main` reset/synced to `origin/main`.
- Safety statement: no Shopify/Tiny writes, no stock/price/campaign/customer action unless explicitly approved.

## Session implementation detail

The session created and merged Hermes Brain PR #63:

- PR: `https://github.com/lk-snkrs/hermes-brain/pull/63`
- Merge commit: `0ef4d48`
- Local post-merge verification: `brain_health_check.py` passed and `main...origin/main` clean.

## Reporting pattern to Lucas

Use a short Portuguese status:

- “Sim — agora está 100% instalada, versionada, indexada e operacional no Brain.”
- List exact artifacts touched.
- List checks passed.
- Explicitly say what was not done: no real Shopify product write/publication, no Tiny write, no campaign/send.

## Pitfall

Avoid saying “100%” after only creating a local runtime skill. Lucas expects the operating system/Brain to learn, which means persistent memory + versioned Brain docs/skills + verification.
