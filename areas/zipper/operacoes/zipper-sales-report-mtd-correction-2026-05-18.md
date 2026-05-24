# Zipper OS — correção do período do report de vendas (2026-05-18)

## Correção de Lucas

Lucas corrigiu que o report de vendas da Zipper deve ser sempre de **vendas do mês**, não apenas D-1 ou fim de semana.

## Regra atual

- Fonte: Supabase Zipper Vendas / `vendas_tango`.
- Período padrão: mês corrente até ontem.
- Em 09h BRT, o dia corrente ainda está aberto e não entra no report.
- `--date YYYY-MM-DD` permanece apenas como override explícito de auditoria/debug.

## Alterações aplicadas

- `/opt/data/scripts/zipper_sales_report_external_delivery.py`
  - `period_for()` alterado para mês corrente até ontem.
  - WhatsApp agora usa título `Zipper OS · Vendas do mês`.
  - E-mail agora usa assunto `Zipper OS · Report de vendas do mês`.
  - `period_mode` no receipt: `month_to_date`.

- `multiempresa-routing-lucas/references/zipper-sales-report-automation-20260518.md`
  - Regra de período atualizada para MTD.

- Memória operacional atualizada:
  - Zipper OS sales report usa Supabase `vendas_tango` e sempre mês corrente até ontem.

## Validação

- `python3 -m py_compile`: OK.
- Dry-run script principal: OK.
- Dry-run watchdog: OK.
- Artefatos visíveis: zero secret hits.
- WhatsApp preview corrigido:
  - `Zipper OS · Vendas do mês — 01/05 a 17/05/2026`
- Período corrigido: `2026-05-01..2026-05-17`.
- Total corrigido no teste: R$ 373.500,00 em 6 linhas/pedidos.

## Envio de teste corrigido

- WhatsApp `[ZPR] IA Bot`: enviado.
  - message id: `3EB0F7EB26BFA9D3D0FE1C`
- E-mail: enviado para Lucas/Osmar/Fabio.
  - Gmail message id: `19e3cb58c7591629`
  - subject: `Zipper OS · Report de vendas do mês — 01/05 a 17/05/2026`
- Verificação Gmail:
  - destinatários OK;
  - subject OK;
  - marker OK;
  - HTML/text OK;
  - secret hits: 0.
- Anti-duplicidade pós-envio: OK (`skipped_duplicate`).
