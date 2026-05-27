# LK Atendimento / Ops — Mapa

Status: categoria operacional/documental ativa; runtime dedicado ainda não aprovado.

## Loop operacional

```text
Base conhecimento → dúvida/evento → consulta fonte viva quando necessário → resposta/rascunho/alerta → humano valida quando sensível → handoff/FAQ/lesson
```

Começar assistido, não bot público autônomo.

## Escopo

- Atendimento e WhatsApp LK.
- Loja/vendas operacionais.
- Relatórios comerciais.
- Estoque, preço, disponibilidade, reserva e status quando houver fonte viva.
- Tiny/Shopify operacional, sempre com approval boundary para writes.

## Fonte de verdade de estoque

- Tiny é a fonte de verdade do estoque.
- Shopify é gatilho/evento e superfície de publicação, não controle de estoque.
- Venda/cancelamento Shopify deve levar a consulta do saldo real no Tiny antes de qualquer atualização no Shopify.
- Nunca usar delta local do estoque Shopify como verdade.

## Documentos canônicos

- `contrato-operacional-lk-ops-atendimento-2026-05-26.md` — contrato LK Ops/Atendimento, guardrails, handoff e critério para runtime futuro.
- `areas/lk/templates/handoff-padrao-lk.md` — template canônico de handoff/receipt para LK Ops, LK Trends e LK Shopify.

## Limite com LK Growth

LK Growth cuida de SEO/GEO/CRO/GMC/conteúdo/analytics. LK Ops/Atendimento cuida de atendimento, WhatsApp, vendas operacionais, estoque, preço, disponibilidade e loja.
