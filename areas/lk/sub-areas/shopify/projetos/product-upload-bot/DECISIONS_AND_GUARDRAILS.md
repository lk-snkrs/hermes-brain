# Decisions and Guardrails — LK Shopify Product Upload / Bot

## Decisões

- Arquitetura Brain OS C: hub na área dona + índice central.
- Criado em modo local/documental, preservando originais.

## Guardrails

- Nenhum produto, variant, imagem, preço, estoque, metafield, tag ou coleção é alterado sem aprovação escopada.
- `Tiny é verdade de estoque; Shopify é superfície/gatilho quando documentado.`
- `Todo write Shopify exige backup/rollback/readback/receipt.`
- Hub não ativa bot, profile, cron ou gateway.
