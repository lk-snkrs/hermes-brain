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

## Projeto canônico — Chatwoot / Elle / WhatsApp

- Pasta canônica: `projetos/chatwoot/` — hub do projeto Chatwoot da LK Atendimento.
- Começar por: `projetos/chatwoot/README.md` e `projetos/chatwoot/CURRENT_STATE.md`.
- Inventário completo: `projetos/chatwoot/ARTIFACT_INDEX.md` e `projetos/chatwoot/manifest.json`.
- Guardrail: Chatwoot pode receber contexto/nota interna quando aprovado; mensagens externas/WhatsApp/campanhas/writes seguem aprovação escopada, fonte viva, snapshot, readback e receipt.

## Projetos Brain OS

- `projetos/chatwoot/` — hub canônico Brain OS Onda 4 para Atendimento/Chatwoot/Elle e recovery engine assistido.
- `projetos/whatsapp-integration-platform/` — hub canônico Brain OS Onda 6 para LK WhatsApp Integration Platform.
