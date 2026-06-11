# Telegram Delivery / UX Governance

Hub canônico Brain OS Onda 13 para Hub canônico para governança de alertas Telegram, silent-OK, ruído, botões, Decision Inbox e qualidade de entrega executiva.

## Escopo

Telegram é a superfície executiva do Lucas. Sem hub próprio, rotinas locais e crons podem gerar ruído, wrappers técnicos ou alertas sem ação.

Este hub é documental/local. Ele organiza evidência e guardrails sem mover, apagar ou substituir os artefatos originais.

## Não-escopo

- Não altera runtime, cron, gateway, bot, MCP server, toolset, canal Telegram ou perfil Hermes.
- Não executa writes externos nem publica mensagens/campanhas/customer-facing.
- Não expõe nem copia secrets.
- Não prova estado vivo sem verificação primária no runtime/fonte.

## Arquivos do hub

- `README.md`
- `CURRENT_STATE.md`
- `DECISIONS_AND_GUARDRAILS.md`
- `ARTIFACT_INDEX.md`
- `TIMELINE.md`
- `NEXT_STEPS.md`
- manifest.json
