# Decisions and Guardrails — Shopify Growth OS / LK Growth

## Decisão de criação

Brain OS Onda 14 criou este hub para fechar lacuna de scanner/cobertura canônica sem duplicar ou mover os artefatos originais.

## Guardrails

- No Shopify product, collection, theme, SEO field, metafield, price, inventory, or production write without explicit scoped approval
- DEV/theme preview is not production truth
- Do not infer current Shopify state from backups, reports, or historical receipts

## Escopo preservado

Local/documental apenas: sem runtime, cron, gateway, Docker/VPS, produção, integrações externas, mensagens, campanhas, compras, fornecedores ou secrets.
