
## pending = Receita Real — AntiFraude LK (20/04/2026)
- LK tem antifraude com delay entre `pending` e `paid`
- **Não filtrar só `paid`** — inclui `pending` no faturamento
- Query correta: `financial_status IN ('paid','pending')`
- Ticket médio: usar só `paid` (pending não confirmado)
- Corrigido em `lk_morning_briefing.py` — todas as queries de ontem, mensal e média 7 dias
- skill `lk-data-debug` atualizada com este padrão
