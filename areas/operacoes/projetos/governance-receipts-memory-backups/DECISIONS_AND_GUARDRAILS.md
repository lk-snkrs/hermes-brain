# Decisions and Guardrails — Governance Receipts / Memory Backups

## Decisões

- Onda 11 cria hub de evidência e backups de governança para não confundir receipts/backups antigos com estado ativo atual.

## Guardrails

- Backup não é fonte viva; usar como rollback/evidência histórica, não como estado atual.
- Status active/online/offline exige evidência runtime fresca.
- Memória boot deve ficar compacta; detalhes ricos permanecem no Brain/skills/reports.
- Sem restart, cron, gateway, provider ou Telegram runtime nesta onda.
