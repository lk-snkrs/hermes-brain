# Decisions and Guardrails — LK Collection Sort Automation

## Decisões

- Arquitetura Brain OS C: hub na área dona + índice central.
- Onda 7 prioriza frentes LK com alto volume de reports/scripts e risco de confundir preview, apply, receipt e produção.

## Guardrails

- Não executar ordenação Shopify sem aprovação escopada atual, snapshot, rollback e readback.
- Distinguir dry-run, preview, apply e repair; não tratar receipt como autorização futura.
- `LKGOC decide padrão/scorecard; Shopify executa superfície quando aprovado.`
- Preservar todos os receipts e snapshots; este hub indexa, não apaga nem compacta evidência.
