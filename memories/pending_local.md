# Pending — Grupo Cimino (Atualizado 2026-04-18)

## ✅ DONE

### 2026-04-18 — Correções Críticas
- [x] Bug tuple em `refund_records` — `lk_shopify_sync.py` linha 398. Corrigido (tupla → string formatada)
- [x] Token MGMT `sbp_d37e...` revogado — 25 scripts corrigidos na VPS (token `sbp_2297055c...`)
- [x] Token Shopify `shpat_1a35f...` salvo no Doppler
- [x] `lk_briefing.py` e `lk_briefing_night.py` — token corrigido
- [x] Faturamento 17/04: R$ 0 → R$ 27.078,99 (sync quebrado)
- [x] GA4 backfill 12-18/Abr — 7 dias inseridos via API direta
- [x] Full sync testado — Shopify/Meta/Klaviyo/JudgeMe OK
- [x] lk_briefing_night.py — timezone SP corrigido (CURRENT_DATE UTC bug)
- [x] lk_briefing_night.py — "novos clientes" agora = clientes únicos (não newsletter Klaviyo)

### 2026-04-15-17 — Histórico
- [x] Hermes brain criado com sync diário
- [x] Mem0 instalado e ativo
- [x] Cron heartbeat 3x/dia (8h, 14h, 20h)
- [x] Skills session-start-protocol, heartbeat-rotativo, post-task-reflection

## ❌ AWAITING LUCAS
- Gmail OAuth Spiti — token expirou (refresh_token inválido). Link de re-autenticação gerado mas não autorizado
- Meta Ads — token Facebook invalidado. Precisa reconectar conta Business

## ⚠️ PARCIALMENTE CORRIGIDO
- Frenet sync — último sync 15/04 (3 dias atrás). Script OK, só precisa rodar

## 📋 CRONS STATUS
| Cron | Job ID | Status |
|------|--------|--------|
| heartbeat-rotativo | e7a3b5ee145e | ativo |
| LK Full Sync (6h) | - | ativo |
| LK Morning Briefing 8h | b4c584055fd6 | ativo |
| LK Night Summary 20h | 9a2feb2c705f | ativo |
| Hermes Brain Sync 6h | 227f3cc47955 | ativo |
| Hermes Weekly Follow-Up | bbad8c23494c | ativo |
| LK Frenet Daily 9h | d1985bbe0c74 | ativo |

## 🗺️ Estrutura Skills (local ~/.hermes/skills/)
Skills ativos em produção (não todos no brain):
- lk/lk-intel-sync-debug ✅
- lk/lk-email-draft-automation ✅
- lk/lk-email-draft-system ✅
- lk/lk-morning-briefing-format ✅
- session-start-protocol ✅
- heartbeat-rotativo ✅
- decisoes-rastreadas ✅
- sazonalidade-check ✅
- feedback-track ✅
- mem0-company-memories ✅
- superpowers-* (14 skills) ✅

---
*Atualizado: 2026-04-18 22:30*
