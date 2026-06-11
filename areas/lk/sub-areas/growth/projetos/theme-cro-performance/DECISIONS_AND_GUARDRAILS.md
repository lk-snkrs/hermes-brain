# Decisions and Guardrails — Theme / CRO Performance

## Decisões

- Arquitetura Brain OS C: hub na área dona + índice central.
- Criado em modo local/documental, preservando originais.

## Guardrails

- `Theme/CRO visível sempre primeiro em preview/dev theme; produção exige aprovação escopada.`
- `Não publicar tema, alterar layout, H1/body, schema ou PDP sem rollback/readback.`
- `Relatório sem dados de vendas/sessões/conversão/GSC/CTR deve ser marcado não decision-grade.`
- `Hub não altera Vercel/Shopify/theme/runtime.`
