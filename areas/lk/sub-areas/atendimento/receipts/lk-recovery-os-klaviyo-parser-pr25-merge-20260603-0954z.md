---
title: LK Recovery OS — PR/merge parser Klaviyo identity_hints
date: 2026-06-03T09:54:00Z
area: lk/atendimento
system: recovery-os
github_pr: https://github.com/lk-snkrs/lk-recovery-os/pull/25
status: merged
---

# Resumo

Lucas pediu: "Seguir abrir o commit e merge" após o deploy aprovado do Worker Recovery OS.

Foi criado commit rastreável, aberto PR e feito merge para `main`.

# GitHub

- Branch: `fix/klaviyo-identity-hints-parser`
- Commit local/branch: `98d9e509a2b5e7746cf11d30aa3440139bc830c9`
- PR: https://github.com/lk-snkrs/lk-recovery-os/pull/25
- Merge method: squash
- Commit em `main`: `8d615311ce89c44dd0e0c58143286bc180dcd34d`
- Remote branch: deletada após merge
- Local branch: deletada após sync

# Mudança

- `workers/recovery-os/src/klaviyo.ts`
  - Parser passou a ler Klaviyo cookie/profile/email/phone/kx também em `identity_hints`.
- `workers/recovery-os/tests/klaviyo.test.ts`
  - Regressão para payload live shape `identity_hints.kla_cookie` / `identity_hints.__kla_id`.

# Verificações

Antes do commit:

```text
git diff --check
npm test
Test Files: 8 passed
Tests: 49 passed
```

PR/CI:

```text
PR mergeable_state: clean
Vercel status: success
GitHub Actions CI: completed / success
```

Após merge e sync local de `main`:

```text
git status: ## main...origin/main
HEAD: 8d615311ce89c44dd0e0c58143286bc180dcd34d
git diff --check HEAD~1..HEAD: ok
npm test: Test Files 8 passed; Tests 49 passed
```

# Observações

- O deploy de produção já havia sido feito antes do PR, com Version ID `dae2afe0-0f27-4de2-8ed9-9b78487b5942`.
- Este PR fecha a rastreabilidade Git do hotfix já implantado.
- Envios ao cliente permaneceram desligados durante todo o processo.
