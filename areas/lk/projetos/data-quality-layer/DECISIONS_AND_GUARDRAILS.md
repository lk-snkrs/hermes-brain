# Decisions and Guardrails — LK Data Quality Layer

## Decisões

- Arquitetura Brain OS C: hub na área dona + índice central.
- Onda 5 prioriza sistemas transversais LK que governam execução, dados, relatórios e aprendizado.

## Guardrails

- Não corrigir fonte viva sem approval packet, snapshot, readback e rollback.
- `Tiny continua verdade de estoque; Shopify é superfície/evento.`
- Materialização local não substitui dados vivos.
- Não publicar relatórios decisórios sem indicar fonte, data e incerteza.
