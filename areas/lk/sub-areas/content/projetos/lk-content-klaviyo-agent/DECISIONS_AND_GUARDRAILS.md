# Decisions and Guardrails — LK Content / Klaviyo Agent

## Decisões

- Arquitetura Brain OS C: hub na área dona + índice central.
- LK Content fica em `areas/lk/sub-areas/content/projetos/lk-content-klaviyo-agent/`.
- Dashboard, Klaviyo e calendário são trilhas do mesmo domínio enquanto não houver volume que justifique hubs separados.

## Guardrails

- Não enviar campanha, e-mail, SMS, WhatsApp ou webhook externo sem aprovação escopada e fonte viva verificada.
- `Não salvar tokens, API keys, webhook secrets ou payload sensível no Brain; apenas nomes/status sanitizados.`
- `Diferenciar draft/test/preview/send real; não inferir envio ou performance sem receipt/fonte primária.`
- `Runtime do agente/perfil/crons exige aprovação separada; hub não ativa nem altera runtime.`
- `Klaviyo/Shopify/Calendar writes e deploys seguem approval gates e rollback documentado.`
