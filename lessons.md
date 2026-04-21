
## pending = Receita Real — AntiFraude LK (20/04/2026)
- LK tem antifraude com delay entre `pending` e `paid`
- **Não filtrar só `paid`** — inclui `pending` no faturamento
- Query correta: `financial_status IN ('paid','pending')`
- Ticket médio: usar só `paid` (pending não confirmado)
- Corrigido em `lk_morning_briefing.py` — todas as queries de ontem, mensal e média 7 dias
- skill `lk-data-debug` atualizada com este padrão

## 2026-04-21 — Bug de Timeout e Token no lk_trend_alert_v2

### Problema 1: Script Timeout (120s)
- **Causa**: `last30days` rodava 8 queries SEQUENCIAIS, cada subprocess com timeout 120s → total >120s
- **Solução**: StockX como fonte primária (5s), last30days como fallback
- **Verificação**: `ps aux | grep last30days` mostrava processo orphan de 2h rodando

### Problema 2: 0 produtos da LK (401 Unauthorized)
- **Causa**: `sys.path.insert(0, '/root/.hermes/scripts')` seguido de `try/except` com fallback de token errado
- **Bug sutil**: `/usr/bin/python3` = Python 3.12, `python3` = Python 3.11 (symlinks diferentes)
  - python3.11 via uv → tinha `__pycache__/_hermes_config.cpython-311.pyc` (token real)
  - python3.12 (usr/bin) → lia fallback (token fake) → 401
- **Diagnóstico**: Testar EXATAMENTE como o cron executa: `cd /root/.hermes/scripts && python3 script.py`
- **Solução**: Remover fallback, importar direto de `_hermes_config`

### Lição: Sempre testar a linha de comando exata do cron

## 2026-04-21 — Supabase: Dois Formatos de Token para Duas APIs

### Descoberta Crítica
- **REST API** (`supabase.co/rest/v1/`): usa JWT `eyJ...` como `apikey` + `Authorization: Bearer`
- **Management API** (`api.supabase.com/v1/projects/{id}/database/query`): usa `sbp_v0_...` service role key
- `_hermes_config.py` expõe só `PAT` (JWT) → scripts que usam MGMT API quebram

### Bug: lk_morning_briefing.py
- `KeyError: 'receita'` → script recebia `[]` da MGMT API (401 JWT inválido)
- **Fix:** hardcoded `sbp_v0_945f5093a614064ba967fd4ac5e1d77dad212e75` no HEADER
- Briefing executou com sucesso após fix

### Diagnóstico Correto
```python
# Testar ambos formatos na MGMT API
for token, label in [('eyJ...', 'JWT'), ('sbp_v0_...', 'sbp_v0')]:
    r = requests.post(url, headers={'Authorization': f'Bearer {token}', ...})
    print(f'{label}: {r.status_code}')  # sbp_v0 = 201, JWT = 401
```

### Lição: Sempre testar o formato exato que a API espera
- Mesmo dentro do mesmo provedor (Supabase), APIs diferentes podem exigir formatos diferentes
- Não assumir que o mesmo token funciona em todas as APIs
