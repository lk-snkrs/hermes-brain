# Receipt — Chatwoot API token saved in Doppler

- Data: 2026-06-02
- Sistema: Chatwoot `https://chat.lkskrs.online`
- Account: LK Sneakers / ID `1`
- Escopo: validar token API informado por Lucas e salvar no Doppler.

## Resultado

Token validado com sucesso sem exposição do valor.

Checks read-only realizados:

- `GET /api/v1/accounts/1` → 200
- `GET /api/v1/accounts/1/teams` → 200
- `GET /api/v1/accounts/1/labels` → 200

## Doppler

Projeto/config: `lc-keys/prd`

Segredos confirmados/salvos:

- `CHATWOOT_LK_API_TOKEN`
- `CHATWOOT_TEAM_ID`
- `CHATWOOT_BASE_URL`
- `CHATWOOT_ACCOUNT_ID`

Valores não sensíveis:

- `CHATWOOT_BASE_URL=https://chat.lkskrs.online`
- `CHATWOOT_ACCOUNT_ID=1`
- `CHATWOOT_TEAM_ID=2`

## Guardrails

Nenhuma mensagem pública enviada.
Nenhum webhook criado/ativado.
Nenhuma alteração em Shopify, Tiny, WhatsApp, produto, pedido, estoque, preço ou tema.
Token não foi escrito no Brain, em Git ou em arquivo local comum.
