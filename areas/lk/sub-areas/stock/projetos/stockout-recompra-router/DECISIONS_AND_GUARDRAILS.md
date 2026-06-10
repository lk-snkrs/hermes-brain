# Decisions and Guardrails — LK Stockout / Recompra Router

## Decisões

- Arquitetura Brain OS C: hub na área dona + índice central.
- Onda 8 prioriza loops de compra/sourcing/ads com risco de confundir preview documental com ação externa.

## Guardrails

- Tiny continua fonte da verdade de estoque; snapshots locais não substituem readback vivo.
- `Não acionar Júlio/fornecedor/WhatsApp/Notion ou comprar sem aprovação escopada atual.`
- `Não tratar ranking histórico como disponibilidade/preço atual.`
- Toda sugestão de reposição deve citar fonte, janela temporal e incerteza.
