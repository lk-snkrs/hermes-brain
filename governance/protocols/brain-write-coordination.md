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

## Pendências fora deste repo

- **Runtime HERMES no VPS** (`/opt/data`, commits "Hermes Brain Sync"): trocar o `git push origin main` cru pelo `scripts/brain-safe-push.sh` (ou pelo mesmo padrão pull-before-push). Aplicação exige acesso ao VPS com backup/rollback e aprovação escopada de Lucas. Enquanto não aplicado, esse lado ainda pode empurrar cego.
- `sync_hermes.sh` (legado, `/root/cerebro-cimino`) já está fail-safe: guard de deprecação + padrão git seguro; não faz parte do runtime atual.
