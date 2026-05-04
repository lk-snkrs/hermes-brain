# Rotina — Outcomes Tracker LK

## O que roda

Acompanhamento das sugestões geradas pelo Hermes para LK: pendentes, aceitas, rejeitadas e implementadas.

Script relacionado:

- `scripts/outcomes_tracker.py`

## Quando roda

Documentação histórica do script: segunda 10:00.
Confirmar cron real na VPS antes de afirmar execução ativa.

## Loop Hermes

```text
sugestão → Lucas revisa → status → resultado → lesson → ajuste de skill/rotina
```

## Ferramentas e dados

- Supabase LK `cnjimxglpktznenpbail`.
- Tabela `lk_intel.hermes_suggestions`.
- Telegram para relatório.

## Credenciais

Buscar em Doppler `lc-keys/prd`; nunca versionar valores.

- `SUPABASE_ACCESS_TOKEN` ou `SUPABASE_MANAGEMENT_TOKEN`.
- `TELEGRAM_BOT_TOKEN`.

## Verificação

1. Rodar via Doppler.
2. Conferir contagem por status.
3. Conferir relatório entregue ao Lucas.
4. Registrar qualquer decisão/learning aplicável.
