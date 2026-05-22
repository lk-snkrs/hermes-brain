# Receipt — Crisp Marketplace credentials saved — 2026-05-21

## Evento

Lucas enviou credenciais do app/plugin Crisp Marketplace para conectar Hermes/Hugo/inteligência do Crisp Chat e pediu para salvar como "Crisp Marketplace".

## Onde foi salvo

Fonte de verdade: Doppler `lc-keys/prd`.

Secret names criados/atualizados:

- `CRISP_MARKETPLACE_IDENTIFIER`
- `CRISP_MARKETPLACE_KEY`
- `CRISP_MARKETPLACE_SIGNING_SECRET`
- `CRISP_MARKETPLACE_PLUGIN_ID`
- `CRISP_MARKETPLACE_PLUGIN_URN`

## Documentação de referência

- Crisp REST API Authentication: `https://docs.crisp.chat/guides/rest-api/authentication/`

## Verificação

- Escrita via Doppler API: HTTP 200.
- Verificação por nome: ambos os secrets existem em `lc-keys/prd`.
- Valores não foram impressos neste receipt.

## Guardrails

- Nenhum token/chave foi salvo em arquivo local versionável.
- Nenhum valor secreto foi impresso no Telegram ou neste Brain receipt.
- Nenhuma alteração foi feita em Docker/VPS/gateway/Crisp Marketplace/app/plugin runtime.
- Nenhum webhook, endpoint público, callback URL ou integração produtiva foi ativado ainda.

## Próximo passo seguro

Quando Lucas pedir para avançar no app/plugin Crisp Marketplace, usar apenas os secret names acima, buscar os valores em processo via Doppler e montar plano/PRD de integração antes de qualquer publicação no Marketplace ou conexão produtiva.

## Relação com Hugo / Workflow API

Isto salva as credenciais de Marketplace/App. Ainda fica separada a pendência de obter o token Hugo / Workflow API no painel Crisp/Hugo, se necessário para acionar workflows por API.
