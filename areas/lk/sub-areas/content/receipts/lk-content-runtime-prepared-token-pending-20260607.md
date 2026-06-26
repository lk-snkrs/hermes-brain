# Receipt — LK Content runtime preparado; gateway pendente token

Data UTC: 2026-06-07
Escopo aprovado: ativar/preparar perfil local `lk-content` sem tocar Docker/VPS/Traefik/Main Hermes.

## Resultado

Perfil Hermes local `lk-content` foi criado/preparado em:

- `/opt/data/profiles/lk-content`

Estado atual:

- profile existe;
- config profile-local criada;
- `.env` criado com permissão restrita;
- API Server desativado;
- Webhook desativado;
- token Telegram dedicado ausente;
- gateway não iniciado por ausência de token;
- modelo do perfil validado por smoke local (`ok`).

## Backups

Backups/pre-state criados em:

- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/content/receipts/runtime-backups/20260607T015129Z/`
- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/content/receipts/runtime-backups/20260607T015203Z/`

## Configuração aplicada

- `agent.max_turns: 60`
- `model.default: gpt-5.5`
- `model.provider: openai-codex`
- `platform_toolsets.telegram` restrito para LK Content:
  - skills;
  - memory;
  - session_search;
  - web/search;
  - file;
  - messaging;
  - clarify;
  - cronjob;
  - delegation;
  - image_gen;
  - vision.

## Segurança

Não executado:

- nenhum Docker/VPS/Traefik;
- nenhum restart do Main Hermes;
- nenhum write externo;
- nenhum Klaviyo/Shopify/Tiny/Calendar;
- nenhum cron real;
- nenhum gateway `lk-content`, porque não há token dedicado.

Token hygiene:

- token não foi impresso;
- token não foi salvo porque está ausente;
- `.env` contém a chave de token Telegram vazia, sem valor sensível;
- `.env` permissão `0600`.

## Evidência operacional

- `hermes profile list` mostrou `lk-content gpt-5.5 stopped`.
- Smoke local do modelo no perfil retornou `ok`.
- Validação Telegram `getMe`: `skipped_no_token`.

## Próximo passo necessário

Para concluir a ativação Telegram:

1. Lucas envia o token BotFather dedicado do `@hermes_lk_producaodeconteudo_bot` em canal seguro; ou rotaciona e envia novo token.
2. Validar `getMe` sem imprimir token.
3. Confirmar username esperado.
4. Gravar token só em `/opt/data/profiles/lk-content/.env`.
5. Iniciar apenas gateway do perfil `lk-content`, com API/webhook off.
6. Verificar `/proc` e logs.
7. Lucas e Renan enviam mensagem de teste ao bot.
