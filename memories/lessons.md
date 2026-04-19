# Lições Aprendidas

## 19/04/2026

### 1. Timezone Bug — LK Intel
**Problema**: `CURRENT_DATE` no Postgres = UTC.Scripts comparavam `order_created_at >= CURRENT_DATE` achando que era BRT.
Depois das 12h BRT (15h UTC), `CURRENT_DATE` já era "amanhã" no Brasil.

**Fix**: `WHERE (order_created_at AT TIME ZONE 'America/Sao_Paulo') >= CURRENT_DATE`
Aplicado em: `lk_anomaly_check.py`, `lk_anomaly_deepdive.py`, `lk_morning_briefing.py`

**Regra**: TODO acesso a datas no Supabase LK → sempre usar `AT TIME ZONE 'America/Sao_Paulo'`

---

### 2. Auto-healing Architecture
**Problema**: Mesmo erro se repete (token revocada, crons quebrando, etc)

**Solução**: Stack de 3 camadas:
1. `hermes_remediate.sh` — conserta DETERMINISTIC errors (VPS refused, rate limits, etc)
2. `hermes_health_check.py` — previne AUDITANDO antes do erro (PAT válida? scripts no lugar certo?)
3. Crons com fail-safe — se health check detecta problema → pausa cron → notifica Telegram

**Regra**: Quando consertar algo manualmente → pergunte: "Isso pode acontecer de novo?"Se sim → criar preventor automático.

---

### 3. /tmp vs /root Scripts
**Problema**: Subagent criou scripts em `/tmp` com tokens placeholders. Cron apontava para `/tmp`.

**Arquitetura nova**:
- `/root/.hermes/scripts/` — canonical, versionado, Backup-ok
- `/tmp` — só scripts ativos que o cron EXECUTA ( cópiados do /root )
- Regra: após editar script em qualquer lugar → sincronizar ambos

**Script de sync**:
```bash
# Após editar /root/.hermes/scripts/lk_*.py
cp /root/.hermes/scripts/lk_*.py /tmp/
```

---

### 4. Revoked PAT Detection
**Problema**: 23 scripts em `/tmp` tinham token antigo `sbp_2297055c...` (revogado).

**Prevenção**: `hermes_health_check.py` escaneia TODOS os scripts em `/tmp` e `/root/.hermes/scripts/` antes de cada sessão.

**Regra**: Após renovar PAT → rodar `hermes_health_check.py` para auditar todos os scripts.

---

### 5. Context Survival (M2.7)
**Problema**: Compressão de contexto pode perder estado crítico entre turnos.

**Solução**:
- `CURRENT_WORK.md` — criado no início de cada sessão, atualizado antes de fechar
- Ler SEMPRE no início: se existir → ler primeiro
- Antes de fechar sessão: salvar estado + decisões + pendências

**Arquivo**: `/root/.hermes/CURRENT_WORK.md`

---

### 6. NameError em Scripts — Import Faltando
**Problema**: `lk_morning_briefing.py` usava `datetime.now(timezone.utc)` mas só importava `from datetime import date, timedelta`. `datetime` e `timezone` estavam undefined.

**Fix**: `from datetime import date, timedelta, datetime, timezone`

**Regra**: Todo script que usa `datetime.now`, `timezone.utc`, `timedelta` → verificar se todos estão no import.
