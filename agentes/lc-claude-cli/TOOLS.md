# TOOLS — [LC] Claude Cli

## Modelo

- Primário: Claude via proxy local `claude-max-api`/Claude CLI.
- Endpoint configurado: `http://127.0.0.1:3456/v1`.
- Slug configurado: `claude-opus-4`.

## Toolsets previstos

- CLI: `clarify`, `file`, `memory`, `session_search`, `skills`, `todo`, `web`.
- Telegram futuro: `clarify`, `file`, `memory`, `session_search`, `skills`, `todo`, `web`.

## Superfícies bloqueadas por padrão

- Sem `terminal` no Telegram por padrão.
- Sem API Server e webhook no profile.
- Sem token Telegram até Lucas fornecer/definir canal.
- Sem cron ativo.

## Verificação

Antes de chamar operacional:

1. Confirmar proxy Claude saudável (`/health`).
2. Confirmar `hermes profile list` mostra o profile.
3. Confirmar `.env` sem API/webhook/token herdado.
4. Rodar uma pergunta curta via `lc-claude-cli chat -q` quando precisar validar o modelo.
