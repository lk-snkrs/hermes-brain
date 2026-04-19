# SESSION START PROTOCOL — Executar em cada nova sessão

## REGRA: Hermes Brain é a fonte de verdade. Se não tá no brain, não sabe.

---

## PASSO 1: Verificar CURRENT_WORK.md
```bash
cat /root/.hermes/CURRENT_WORK.md
```
Se existir e dizer "[COMPLETO]" → trabalho anterior terminou. Se disser "[EM ANDAMENTO]" → continuar de onde parou.

---

## PASSO 2: Verificar pendentes
```bash
cat /root/.hermes/memories/pending.md
```
Itens com `[URGENTE]` ou `[ALTA]` → listar primeiro.

---

## PASSO 3: Resumo do sistema
- Brain sync: `bash /root/.hermes/scripts/brain_sync.sh` (se sessão anterior teve mudanças)
- Cron status: `cronjob list` (se há crons com falha)
- Decisions: `cat /root/.hermes/memories/decisions.md` (últimas decisões)
- Lessons: `cat /root/.hermes/memories/lessons.md` (lições recentes)

---

## PASSO 4: Se nada urgente e trabalho anterior completo
"Bom dia! Trabalho anterior completo. O que vamos fazer hoje?"

## PASSO 5: Se trabalho em andamento
"Retomando trabalho anterior: [resumo do CURRENT_WORK]. O que vamos fazer?"

## PASSO 6: Se há itens urgentes
"Sistema com itens urgentes pendentes: [lista]. Vamos resolver esses primeiro?"

---

## REGRA: Ao final de toda sessão — Checklist de 5 minutos
1. `bash /root/.hermes/scripts/brain_sync.sh`
2. `cd /root/hermes-brain && git add -A && git commit -m "Session end: $(date +%Y-%m-%d)" && git push`
3. pending.md → atualizar
4. lessons.md → adicionar se houve insight
5. CURRENT_WORK.md → marcar completo ou manter EM ANDAMENTO
