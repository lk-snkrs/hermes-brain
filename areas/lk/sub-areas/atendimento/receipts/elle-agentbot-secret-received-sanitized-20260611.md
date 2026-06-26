# Elle AgentBot — secret recebido (sanitizado)

Data: 2026-06-11
Origem: Lucas no Telegram.

## Evento

Lucas criou/está criando o AgentBot `Elle` no Chatwoot e informou:

- URL/endpoint informado: `https://elle.lkskrs.online`
- Webhook secret: recebido no chat, **valor não registrado neste arquivo**.

## Segurança

- Valor do segredo não deve ser copiado para Brain, memória, logs ou Telegram.
- Como o segredo foi colado em Telegram, recomendar rotação/regeneração se houver opção no Chatwoot depois que for armazenado corretamente.
- Secret existente esperado no Doppler: `ELLE_CHATWOOT_WEBHOOK_SECRET`.
- URL existente esperada no Doppler: `ELLE_CHATWOOT_WEBHOOK_URL`.

## Próximo passo seguro

Antes de conectar o bot ao inbox real `LK WhatsApp`, validar/religar endpoint Elle e garantir:

- sem comportamento antigo de notas em massa;
- filtros para outgoing/private notes;
- kill switch/rollback;
- public replies limitadas às categorias aprovadas;
- fallback para humano.
