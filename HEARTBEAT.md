# HEARTBEAT.md — Pulso Proativo do Hermes

> O que Hermes checa periodicamente sem ser perguntado.
> Regra: Menos é mais — só avisar se ALGO mudou.

---

## 🔴 Checklist (A Cada Heartbeat — 8h / 14h / 20h)

**Tempo estimado:** 2-3 min
**Modelo:** MiniMax-M2.1 (cheap routing) ou MiniMax-M2.7

### 1. Pendências (pending.md)
- [ ] Há algo pendente há >7 dias?
- [ ] Algum item novo que precisa de ação?
- **Ação:** Se SIM → avisar. Se NÃO → próximo check.

### 2. Anomalias de Negócio (Supabase LK)
- [ ] Vendas caíram >20% vs ontem?
- [ ] Pedido travado >6h sem processamento?
- [ ] Estoque crítico (<5 unidades)?
- **Ação:** Se SIM → avisar com % de impacto

### 3. Saúde de Automações (Cron)
- [ ] Algum cron falhou recentemente?
- [ ] Cron atrasado >30min?
- [ ] Supabase ou Evolution offline?

### 4. Auto-Remediação (antes de reportar erro)
- [ ] Erro detectado é known_type (SSH refused, cron failed, script error)?
- [ ] `hermes_remediate.sh <tipo> [args]` foi executado?
- **Resultado:** RESOLVED → loga esilêncio | FAILED → reporta com contexto

### 5. Projetos Ativos
- [ ] Algo que Lucas pediu ficou >48h parado?
- [ ] Pendência aguardando resposta do Lucas?
- **Ação:** Se SIM → avisar estado atual

### 6. Git Activity (hermes-brain)
```bash
cd /root/hermes-brain && git log --oneline --since="8 hours ago"
```
- [ ] Algum commit novo no hermes-brain?
- [ ] Sync com cerebro-cimino rodou?
- **Ação:** Se mudança relevante → registrar. Se não → silêncio.

---

## 📅 Semanal (Segunda 9h)

### Consolidação de Memory
- [ ] Extrair lições da semana → `lessons.md`
- [ ] Atualizar decisões → `decisions.md`
- [ ] Limpar sessions antigos
- **Ação:** Fazer silenciosamente

### Projetos + Prioridades
- [ ] Projeto parado? Por quê?
- [ ] Backlog >1 semana?
- **Ação:** Se SIM → incluir no briefing

---

## 🔇 Horários de Silêncio

| Horário | Por quê | Exceção |
|---------|---------|---------|
| **06:00–08:00** | Manhã | ❌ Nenhuma |
| **18:30–20:00** | Noite | ❌ Nenhuma |
| **22:00–07:00** | Dorme | 🔴 Só erro crítico |

**Regra:** Urgência durante silêncio → aguarda próxima janela.

---

## 📊 Regras de Notificação

| Nível | O que | Ação |
|-------|-------|------|
| 🔴 **Urgente** | Service down, erro crítico | Avisar AGORA |
| 🟡 **Importante** | Anomalia >20%, projeto parado | Avisar no próximo horário |
| 🟢 **OK** | Tudo normal | HEARTBEAT_OK |

**Regra de Ouro:**
- ✅ Se encontra algo → avisa
- ❌ Se não encontra → silêncio total
- ❌ NÃO enviar "tudo ok" diário

---

## ⚙️ Cron Jobs

| Cron | Horário | O que |
|------|---------|-------|
| heartbeat-rotativo | 8h, 14h, 20h | Checks acima |
| lk-daily-briefing | 7h seg-sex | Briefing matinal |
| lk-trends | seg/qui | Monitor tendências |
| cross-sell | 3x/dia | Monitor cross-sell |
| hermes-brain-sync | diária | Sync + commit |

---

## ✅ Implementação

- [x] HEARTBEAT.md criado
- [x] Heartbeat-rotativo skill
- [ ] Cron jobs 3x/dia ATIVADOS
- [ ] Integrar com pending.md state

---

*Criado em: 2026-04-14 — baseado no HEARTBEAT.md do CWC*
