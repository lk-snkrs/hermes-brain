# Decisions and Guardrails — Pronta Entrega / POS / LK Stock

## Decisão de criação

Brain OS Onda 14 criou este hub para fechar lacuna de scanner/cobertura canônica sem duplicar ou mover os artefatos originais.

## Guardrails

- No availability promise, reservation, transfer, purchase, supplier contact, or Tiny/Shopify write without scoped approval
- Fixtures/probes/test data never feed operational stock scores or P0/P1 recommendations
- Pronta entrega is an internal operational signal, not public SEO taxonomy

## Escopo preservado

Local/documental apenas: sem runtime, cron, gateway, Docker/VPS, produção, integrações externas, mensagens, campanhas, compras, fornecedores ou secrets.
