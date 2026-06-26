# Diagnóstico — Hermes Brain x GitHub (`lk-snkrs/hermes-brain`)

Data UTC: 2026-06-26T09:35–09:45Z

## Veredito

O Hermes Brain está sendo salvo principalmente no clone local:

```text
/opt/data/hermes_bruno_ingest/hermes-brain
```

O sync automático existe e está rodando, mas publica no branch atual do clone local:

```text
consolidation/brain-filesystem-git-hygiene-20260516
```

Portanto, o GitHub **está recebendo commits em um branch de consolidação**, mas o branch padrão `main` do repositório `lk-snkrs/hermes-brain` não está sendo atualizado desde 2026-06-11.

## Evidência

- Remote configurado no clone local: `https://github.com/lk-snkrs/hermes-brain.git`.
- Branch local ativo: `consolidation/brain-filesystem-git-hygiene-20260516`.
- Head local: `78a2ce70dea09a5d8702ae02538a1f601e032593`.
- Head remoto do branch de consolidação: `78a2ce70dea09a5d8702ae02538a1f601e032593`.
- Head remoto de `main`: `72818e3173f2dc4d82fcba2ebdf9fd908e83ec88`.
- Último commit visível em `main`: 2026-06-11 — `docs: improve Brain OS hub quality guardrails (#148)`.
- Último commit no branch de consolidação: 2026-06-26 — `docs: sync Brain improvement score 2026-06-26`.
- Divergência medida localmente: branch de consolidação tem 254 commits que não estão em `origin/main`; `main` tem 7 commits que não estão no branch de consolidação.

## Diagnóstico técnico

A rotina canônica `areas/operacoes/rotinas/brain-sync.md` aponta para:

```text
/opt/data/scripts/brain_sync_safe.py --push
```

O script detecta o branch atual com:

```text
git branch --show-current
```

e empurra para:

```text
git push origin HEAD:<branch-atual>
```

Como o clone operacional está estacionado em `consolidation/brain-filesystem-git-hygiene-20260516`, o sync diário continua alimentando esse branch, não `main`.

## Cron vivo

Cron ativo identificado:

- Nome: `Hermes Brain Fechamento Ágil 01h + Brain Sync`
- ID: `3fc45b0830c6`
- Schedule: `0 4 * * *` UTC
- Delivery: `local`
- Último status: `ok`
- Último run observado: `2026-06-26T04:08:30Z`

## Estado de hoje após o cron

O cron de 04:00 UTC já rodou. Mudanças criadas depois dele, incluindo artefatos LKGOC/Mesa desta sessão, ainda estão locais e entram no próximo dry-run do sync.

Dry-run atual do Brain Sync mostrou:

- `allowed_files`: 53
- `skipped_files`: 25.690

Os arquivos da revisão D+7 e NB740 aparecem entre os allowlisted/salváveis no próximo sync.

## Conclusão operacional

- Brain local: ativo e recebendo escrita.
- GitHub branch de consolidação: ativo e recebendo sync.
- GitHub `main`: desatualizado.
- Causa provável: o clone operacional ficou em branch de consolidação; o script faz push para o branch atual, não para `main`/PR.

## Próximos passos seguros recomendados

1. Não fazer push direto para `main` sem reconciliação: há divergência bilateral (`254 ahead`, `7 behind`).
2. Criar um pacote de reconciliação GitHub seguro:
   - fetch/reset controlado em worktree separado;
   - comparar `main` vs branch de consolidação;
   - abrir PR ou plano de merge protegido;
   - preservar allowlist/secret scan;
   - verificar remote head pós-push.
3. Considerar alterar o Brain Sync para falhar/alertar quando o branch operacional não for o branch canônico esperado, em vez de continuar publicando silenciosamente em branch antigo.

## Não-ações

- Nenhum push GitHub foi feito neste diagnóstico.
- Nenhum secret foi impresso.
- Nenhum runtime, cron, Docker, VPS, Shopify, Tiny ou outro sistema externo foi alterado.
