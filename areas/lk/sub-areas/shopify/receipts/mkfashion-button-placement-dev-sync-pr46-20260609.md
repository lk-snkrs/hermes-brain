# Receipt — mKFashion PDP button placement synced to dev

Data: 2026-06-09
Perfil: LK Shopify
Repo: `lk-snkrs/lk-new-theme`
PR: https://github.com/lk-snkrs/lk-new-theme/pull/46
Base: `dev`
Merge commit: `60e2802 fix: sync mKFashion PDP button placement to dev (#46)`

## Contexto

Lucas corrigiu a regra operacional: mudanças de tema Shopify não devem ser feitas como patch independente direto em `production`. O fluxo correto é passar por `dev` primeiro e depois promover/mergear para `production`.

O hotfix visual do mKFashion já havia sido aplicado em `production` pelo PR #45. Este receipt registra a correção de linhagem: sincronizar o mesmo ajuste para `dev`.

## Execução

- Branch criada a partir de `origin/dev`: `fix/mkfashion-button-placement-dev-sync-20260609`.
- Aplicado o mesmo ajuste de placement do botão mKFashion:
  - âncora em `.pi-actions .shopify-payment-button`;
  - posição `afterend` para ficar entre `Compre já` e Trust Bar;
  - tuner `mk-tryon-button-host`;
  - remoção do ícone padrão errado via shadow root aberto;
  - manutenção do SDK zero-touch.
- PR aberto e mergeado em `dev`.
- Branch remota temporária apagada.

## Arquivos alterados

- `layout/theme.liquid`
- `projetos/lk-new-theme/layout/theme.liquid`
- `projetos/lk-new-theme/dev-theme/layout/theme.liquid`

## Verificações Git

Após fetch de `origin/dev`:

- `layout/theme.liquid`:
  - `sdk`: 1
  - `anchor`: 1
  - `selector`: 3
  - `host`: 1
  - `icon`: 1
  - `old_unpkg`: 0
  - `old_snippet`: 0
- `projetos/lk-new-theme/layout/theme.liquid`:
  - `sdk`: 1
  - `anchor`: 1
  - `selector`: 3
  - `host`: 1
  - `icon`: 1
  - `old_unpkg`: 0
  - `old_snippet`: 0
- `projetos/lk-new-theme/dev-theme/layout/theme.liquid`:
  - `sdk`: 1
  - `anchor`: 1
  - `selector`: 3
  - `host`: 1
  - `icon`: 1
  - `old_unpkg`: 0
  - `old_snippet`: 0

Final:

```text
PASS origin/dev static verification
```

Local `dev` foi resetado/sincronizado para `origin/dev` em `60e2802`.

## Shopify DEV readback

Read-only Admin readback do tema DEV/unpublished:

- theme id: `155065450718`
- name: `lk-new-theme/dev`
- role: `unpublished`
- `new_sdk_count`: 1
- `anchor_config_count`: 1
- `payment_anchor_count`: 3
- `host_tuner_count`: 1
- `icon_removal_selector`: true
- old refs:
  - `unpkg`: false
  - `mkfashion_tryon`: false

## Guardrails

- Nenhum Shopify Admin/API theme upload manual foi executado nesta sincronização.
- Nenhum novo merge em `production` foi feito nesta etapa.
- Secrets usados via Doppler sem impressão de valores.

## Regra operacional registrada

Para tema Shopify LK, mesmo quando Lucas pedir produção, o fluxo deve ser:

1. branch de trabalho;
2. PR/merge em `dev`;
3. validação/readback/QA em `dev`;
4. promoção de `dev` para `production`;
5. validação/readback/QA em `production`.

Hotfix independente direto em `production` só com exceção emergencial explicitamente nomeada por Lucas.

## Rollback

Rollback de dev via PR revertendo:

- `60e2802`

Rollback de production do hotfix visual anterior via PR revertendo:

- `46693d5`
