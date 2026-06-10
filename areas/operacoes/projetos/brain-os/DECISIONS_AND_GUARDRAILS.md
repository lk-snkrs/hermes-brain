# Brain OS — Decisions and Guardrails

## Decisões de arquitetura

1. O modelo é híbrido: hubs ficam na área dona; Brain OS mantém índice central.
2. Hubs são camada de leitura/organização, não migração destrutiva.
3. Histórico é preservado; decisões antigas podem ser marcadas como superseded, mas não apagadas.
4. Fonte viva sempre vence documento histórico.
5. Manifest é obrigatório para hubs canônicos.
6. Estado atual deve ficar separado de timeline/histórico.
7. Guardrails devem ser explícitos e lidos antes de qualquer ação externa.
8. Scanner é local/read-only por padrão.

## Guardrails permanentes

- Não copiar secrets, tokens, senhas, service accounts, refresh tokens ou payloads sensíveis.
- Não executar writes externos sem aprovação escopada.
- Não tocar Docker/VPS/gateway/runtime/cron sem aprovação escopada.
- Não transformar histórico em fonte atual sem evidência viva.
- Não apagar/mover arquivos históricos na v1.
- Não usar GitHub push como sinônimo de Brain local completo.
- Diferenciar: local criado, Git tracked, commitado, pushado.

## Fonte da verdade

- LK estoque: Tiny é fonte viva; Shopify é superfície/evento, salvo evidência contrária.
- Shopify/GMC/Meta/Klaviyo: APIs/contas vivas vencem docs antigos.
- Chatwoot/atendimento: hub canônico indexa Brain; estado vivo externo exige consulta aprovada/fonte.
- Memory OS: scripts/reports atuais vencem chat summaries.
- Mesa COO: ledger/decisões atuais vencem contexto compactado.
