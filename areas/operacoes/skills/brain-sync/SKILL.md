---
name: brain-sync
description: Bidirectional sync between local memories and VPS Hermes Brain + Mem0 write-through
tags: [memory, brain, sync, vps]
---

# Brain Sync — Sincroniza todas as fontes de memória

Executa sync bidirecional entre:
1. `/root/.hermes/memories/` (local)
2. `/root/hermes-brain/` (VPS)
3. Mem0 vector DB

## Quando Usar
- **Fim de cada sessão** — obrigatório, junto com CURRENT_WORK.md update
- Após mudanças importantes (pendências resolvidas, decisões tomadas, lições aprendidas)
- Quando sentir que "o sistema não lembra"

## Arquitetura Real — 3 Fontes

| Fonte | Local | O que tem | Via |
|-------|-------|-----------|-----|
| Mem0 vector DB | cloud | 89 memories indexadas, busca semântica | `mem0_search` |
| Brain local | `/root/.hermes/` | pending, lessons, decisions, user | filesystem |
| Brain VPS | `/root/hermes-brain/` | mesmo + agentes, empresa, docs | git push |

**Regra**: pending.md e lessons.md vivem em AMBOS local e VPS. Sync é obrigatório após cada sessão.

## Armadilhas Descobertas (19/04/2026)

1. **sshpass + `cat` via SSH é instável** → usar `scp` direto funciona, `ssh "cat > file"` não
2. **Git push não é automático** → após sync, fazer `git add + commit + push` senão fica só no filesystem
3. **HOME=/root** → scripts que usam `$HOME/.hermes` precisam de caminho absoluto

## Script — 3-pass approach

```bash
# PASS 1: Push local → VPS (scp direto)
sshpass -p 'password' scp /root/.hermes/memories/{pending,lessons,decisions,lk,zipper,spiti}.md \
    root@72.60.150.124:/root/hermes-brain/memories/

# PASS 2: Pull VPS → local (mesmo scp)
sshpass -p 'password' scp root@72.60.150.124:/root/hermes-brain/memories/{pending,lessons}.md \
    /root/.hermes/memories/

# PASS 3: Git commit + push (só no brain local /root/hermes-brain/, não no VPS)
cd /root/hermes-brain && git add -A && git commit -m "sync $(date)" && git push origin main
```

**Script completo**: `/root/.hermes/scripts/brain_sync.sh` (testado 19/04 ✅)

## Checklist Pós-Sessão (obrigatório)

Antes de fechar qualquer sessão:
- [ ] `bash /root/.hermes/scripts/brain_sync.sh` executado
- [ ] `git push` feito (verificar saída — deve dizer "main -> main")
- [ ] Fatos novos salvos no Mem0 via `mem0_conclude`
- [ ] `CURRENT_WORK.md` atualizado com estado da sessão

## Uso

```bash
bash /root/.hermes/scripts/brain_sync.sh
```

**Frequência**: Fim de cada sessão + quando resolver pendências + quando sentir que "o sistema não lembra".

## Mem0 Write-Through

Após sync, persistir fatos importantes no Mem0:

```python
mem0_conclude(conclusion="<fato importante descoberto durante a sessão>")
```

Use para: decisões de arquitetura, bugs corrigidos, insights de negócio.
