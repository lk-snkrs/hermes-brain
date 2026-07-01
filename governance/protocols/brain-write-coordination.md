# Protocolo — Coordenação de Escrita no Hermes Brain

Status: canônico · Criado: 2026-07-01

Regras para múltiplos escritores atualizarem o Hermes Brain **sem sobreposição, sem perda de update e sem clone desatualizado**.

## Modelo mental

O Hermes Brain não é o HERMES nem o CLAUDE. O Brain é **`lk-snkrs/hermes-brain` @ GitHub, branch `main`** — a única fonte de verdade.

Todos os escritores são apenas **janelas** (clones) para esse `main`, e só se comunicam entre si **através do GitHub**:

```text
                 ┌─────────────────────────────┐
                 │  GitHub main (fonte única)  │
                 └──────────────┬──────────────┘
             pull/PR/push │            │ pull/rebase/push
        ┌─────────────────┘            └─────────────────┐
   CLAUDE (Mac, interativo)        HERMES (VPS /opt/data, runtime)
   branch → PR → merge             direto no main (pull-before-push)
```

O problema nunca é *armazenamento* (já é um só). É **coordenação de escrita** e **staleness de clone**.

## Regra de ouro

**Ninguém afirma estado nem escreve sem `git pull` antes.** `main` é a verdade; o clone local é um snapshot.

## Duas faixas de escrita

| | HERMES (automático) | CLAUDE (interativo) |
|---|---|---|
| Como escreve | direto no `main` | branch → PR → **merge** |
| Proteção obrigatória | usar **`scripts/brain-safe-push.sh`** (pull --rebase --autostash antes de todo push + retry) em vez de `git push` cru | GitHub bloqueia o merge se houver conflito (rede de segurança) |
| Nunca | `git add -A` cego em clone compartilhado; `--force` no main | commitar direto no main; `--force` no main |

## Território (reduz superfície de colisão)

Cada faixa é dona preferencial de arquivos diferentes, para os dois não editarem o mesmo arquivo na mesma janela:

- **HERMES:** `memories/daily/`, `memories/hot.md`, `memories/current.md`, `memories/pending.md`, `memories/lessons.md`, `receipts/`, `reports/`, `CHANGELOG.md`, consolidação diária e runtime.
- **CLAUDE:** `.claude/agents/`, `skills/`, `governance/`, docs/protocolos, áreas que autora sob demanda.
- **Compartilhado (cuidado):** `AGENTS.md`, `areas/**`, `empresa/**` — coordenar; preferir **arquivo novo por registro** (um receipt/nota por arquivo) a editar um arquivão.

Princípio: **append-only / um-arquivo-por-registro** leva o conflito para perto de zero. O Brain já favorece isso em `receipts/` e `daily/`; estender a disciplina.

## Higiene de clone

- Clones de trabalho separados: o sync automático e o trabalho interativo **não devem compartilhar working dir**, senão um `git add -A` sweep captura o WIP do outro.
- `git add` sempre **escopado** aos arquivos pretendidos. Nunca `git add -A` em clone compartilhado.
- Nunca `push --force` no `main`. Force-push só em branch de PR própria, com `--force-with-lease`.

## Resolução de conflito

Quando um push/merge conflita:

1. `git pull --rebase --autostash origin main` (ou rebase da branch do PR sobre o main).
2. **Inspecionar antes de sobrescrever.** Se o conteúdo remoto contradiz o que ia escrever, isso é sinal, não obstáculo — não dar clobber no trabalho do outro escritor.
3. Reaplicar a mudança sobre o estado novo e repetir o push.
4. Se não resolver automaticamente, parar e escalar para Lucas com o diff — nunca `--force` para "resolver".

## Checklist de escrita (CLAUDE)

1. `git checkout main && git pull --ff-only`
2. `git checkout -b <branch>`
3. editar → **secret scan** (`possible_secrets 0`, só nomes de secret, nunca valores)
4. `git add <escopado>` → commit (inglês, conventional, autor `lk@lksneakers.com.br`)
5. `git push -u origin <branch>`
6. `gh pr create` → `gh pr merge --merge --delete-branch`
7. `git checkout main && git pull` → reportar PR + commit de merge

## Primitiva canônica de push

Todo escritor automático que empurra direto no `main` deve usar **`scripts/brain-safe-push.sh`** em vez de `git push origin main` cru:

```bash
scripts/brain-safe-push.sh -m "brain sync $(date '+%F %H:%M')" memories/ receipts/
```

Ela faz: staging escopado (nunca `git add -A`) → `git pull --rebase --autostash` → push com retry → para e pede resolução manual em conflito real (nunca `--force`).

## Decisão: coordenação manual (2026-07-01)

Investigação read-only (VPS + Mac) concluiu que o escritor automático "Hermes Brain Sync" **não roda no VPS nem no Mac de Lucas** — não há clone `hermes-brain` em nenhum dos dois. É um scheduler externo (provável "Cron MiniMax", citado no `sync_hermes.sh` legado) que clona, consolida e empurra pro `main`. Commits são unsigned local-git (não API/Action). **Não é alcançável a partir dos ambientes que operamos.**

Como não dá para corrigir o código do escritor externo daqui, a coordenação passa a ser **manual, do lado que controlamos (CLAUDE)**, apoiada na rede de segurança nativa do GitHub:

1. **CLAUDE sempre `git pull` antes de escrever** e **`branch → PR → merge`** — o GitHub **rejeita o merge se houver conflito**, então CLAUDE nunca sobrescreve o trabalho do escritor externo.
2. **Re-sincronizar imediatamente antes do merge** (o externo pode ter empurrado durante o trabalho): garantir a branch em cima do `main` mais novo.
3. **Nunca `--force` no `main`.**
4. **Conflito → parar e mostrar a Lucas** o diff; nunca resolver com force. Inspecionar antes de sobrescrever.
5. **Não** há branch protection server-side nem patch no VPS por ora (decisão de simplicidade). Reabrir só se aparecer perda de dado real.

Risco aceito: se o escritor externo fizer `git push --force` (fora do nosso alcance), pode reescrever histórico. Até hoje não há evidência disso; se surgir, escalar para habilitar branch protection no `main`.

`sync_hermes.sh` (legado, `/root/cerebro-cimino`) já está fail-safe (guard + git seguro) e não faz parte do runtime atual.
