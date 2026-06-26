# Fase 1 — LK agents identity/docs realignment (2026-06-25)

Generated at: `2026-06-25T18:19:16.029508+00:00`

## Pedido aprovado

Lucas aprovou a opção 1: realinhar docs/SOUL/MAPA/MEMORY dos agentes LK com backup e smoke read-only, sem restart nem writes externos.

## Escopo executado

Profiles cobertos:

```text
lk-growth
lk-shopify
lk-collection-optimizer
lk-stock
lk-trends
lk-finance
lk-content
lk-ops
lk-analyst-readonly
lk-content-reviewer
```

## Mudanças feitas

1. Backup timestamped criado:

```text
/opt/data/backups/lk-agents-identity-realignment-20260625T180713Z
```

2. `lk-collection-optimizer/SOUL.md` corrigido:

Antes:

```text
# LK Growth OS — Hermes Specialist
```

Depois:

```text
# [LK] Otimização de Coleções / LKGOC — Hermes Specialist
```

3. `MAPA.md` root criado/normalizado nos 10 profiles LK.
4. `MEMORY.md` root criado como ponteiro para `memories/MEMORY.md`, para evitar confusão com stubs legados.
5. `memories/MEMORY.md` recebeu uma linha de identidade quando faltava ponteiro claro.
6. Skill LKGOC dentro de `lk-growth` corrigida para **handoff-only**, porque ela estava carregando LKGOC como se Growth pudesse executar/possuir LKGOC.

## Verificação estrutural

| Profile | SOUL heading | AGENTS Task OS | SOUL Task OS | MAPA normalizado | MEMORY pointer | Growth contamination LKGOC |
|---|---|---:|---:|---:|---:|---:|
| `lk-growth` | `# LK Growth OS — Hermes Specialist` | 1 | 1 | True | True | False |
| `lk-shopify` | `# LK Shopify Hermes` | 1 | 1 | True | True | False |
| `lk-collection-optimizer` | `# [LK] Otimização de Coleções / LKGOC — Hermes Specialist` | 1 | 1 | True | True | False |
| `lk-stock` | `# SOUL — [LK] Estoque Loja Física` | 1 | 1 | True | True | False |
| `lk-trends` | `# LK Trend OS — Hermes Specialist` | 1 | 1 | True | True | False |
| `lk-finance` | `# LK Finance — Hermes Specialist` | 1 | 1 | True | True | False |
| `lk-content` | `# LK Content — Hermes Specialist` | 1 | 1 | True | True | False |
| `lk-ops` | `# LK Ops Hermes Bot — SOUL` | 1 | 1 | True | True | False |
| `lk-analyst-readonly` | `# LK Analyst Readonly` | 1 | 1 | True | True | False |
| `lk-content-reviewer` | `# LK Content Reviewer` | 1 | 1 | True | True | False |

## Smoke read-only

Smokes CLI foram usados como evidência comportamental parcial, mas o CLI Hermes em alguns profiles respondeu corretamente e depois encerrou com `Aborted/core dumped` (`exit 134`). Portanto, o conteúdo da resposta é útil, mas o status do processo revela uma lacuna separada do CLI/smoke harness.

Resultados críticos:

- `lk-growth`: após patch da skill LKGOC para handoff-only, respondeu como **LK Growth** e não como LKGOC.
- `lk-collection-optimizer`: respondeu como **[LK] Otimização de Coleções / LKGOC**.
- `lk-stock`, `lk-finance`, `lk-content`, `lk-ops`: responderam com identidade correta nos smokes anteriores.
- `lk-analyst-readonly` e `lk-content-reviewer`: smoke bloqueado por `HTTP 401 token_expired`; não foram alteradas credenciais nesta fase.

## Validações finais

- Brain health: `FAIL=0 WARN=0`.
- Secret scan high-confidence nos arquivos tocados: `0`.
- Writes externos: `0`.
- Restart/gateway: `0`.
- Docker/VPS/Traefik/secrets/env: `0`.

## Limitações / próximos passos

1. Gateways vivos não foram reiniciados por escopo; os novos `SOUL.md`/docs valem para novas sessões/runs e após restart futuro.
2. O `exit 134/core dumped` do Hermes CLI após respostas de smoke precisa de investigação separada se quisermos usar smoke automático como gate confiável.
3. `lk-analyst-readonly` e `lk-content-reviewer` têm token/auth expirado para CLI smoke; correção de credential pool deve ser approval separado se esses support profiles forem usados ativamente.
4. Próxima fase recomendada: restart controlado dos gateways LK + smoke via canal/profile vivo, depois de Lucas aprovar.

## Conclusão

Fase 1 concluída: o erro crítico do `lk-collection-optimizer` foi corrigido no `SOUL.md`; profiles LK receberam MAPA/MEMORY pointers mínimos; e a contaminação da skill LKGOC em `lk-growth` foi convertida para handoff-only.
