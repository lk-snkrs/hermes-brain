# Rotina — RFM semanal LK

## O que roda

Cálculo de segmentação RFM de clientes LK e relatório semanal para Lucas.

Scripts relacionados:

- `scripts/compute_rfm.py`
- `scripts/rfm_report.py`

## Quando roda

Documentação histórica dos scripts:

- `compute_rfm.py`: domingo 23:00.
- `rfm_report.py`: segunda 09:00.

Observação: o `cronjob list` local deste Hermes retornou 0 jobs em 2026-05-04; confirmar crons reais na VPS antes de afirmar execução ativa.

## Ferramentas e dados

- Supabase Management API para o projeto LK `cnjimxglpktznenpbail`.
- Tabelas `lk_intel.orders` e `lk_intel.customer_rfm`.
- Telegram para entrega do relatório.

## Credenciais

Buscar em Doppler `lc-keys/prd`; nunca versionar valores.

- `SUPABASE_ACCESS_TOKEN` ou `SUPABASE_MANAGEMENT_TOKEN`.
- `TELEGRAM_BOT_TOKEN`.

## Verificação

1. Rodar scripts via Doppler.
2. Confirmar saída sem erro.
3. Confirmar atualização da tabela RFM.
4. Confirmar mensagem entregue no Telegram.

## Falha comum

Se `Missing SUPABASE_ACCESS_TOKEN/SUPABASE_MANAGEMENT_TOKEN`, rodar via Doppler:

```bash
doppler run --project lc-keys --config prd -- python3 scripts/compute_rfm.py
```
