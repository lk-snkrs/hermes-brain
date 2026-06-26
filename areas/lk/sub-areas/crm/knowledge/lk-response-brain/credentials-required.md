# LK Response Brain — credenciais Crisp/Hugo necessárias

Atualizado: 2026-05-21
Fonte de verdade: Doppler `lc-keys/prd`

> Este arquivo lista apenas nomes e finalidade. Não contém valores secretos.

## Já encontrados no Doppler

- `CRISP_LK_WEBSITE_ID` — Website ID LK no Crisp.
- `CRISP_LK_REST_TOKEN_ID` — token ID REST/API Crisp LK.
- `CRISP_LK_REST_TOKEN_KEY` — token key REST/API Crisp LK.
- `CRISP_LK_REST_TIER` — tier/header usado nas chamadas REST Crisp.

Validação segura em 2026-05-21:

- existência dos 4 secrets: OK.
- chamada read-only de lista de conversas Crisp: HTTP 206, indicando credencial REST utilizável para leitura paginada.
- chamada de website profile retornou HTTP 401; não bloquear o projeto por isso, pois endpoint/tier pode exigir escopo diferente e a listagem de conversas funcionou.

## Faltando para Crisp/Hugo MCP

Adicionar quando disponíveis:

- `HUGO_LK_WEBSITE_TOKEN` — Bearer token usado para Hugo MCP Server e Workflow API (`Authorization: Bearer ...`).
- `HUGO_LK_MCP_SIGNING_SECRET` — secret `mcp_sec_...` gerado na integração MCP do Hugo para verificar `X-Crisp-Signature`.
- `HUGO_LK_MCP_BEARER_TOKEN` — token que o Hugo usará para autenticar no nosso MCP server LK, se configurarmos Bearer além de assinatura.
- `HUGO_LK_HANDOFF_WORKFLOW_ID` — workflow/scenario ID para transbordo Larissa.
- `HUGO_LK_AGENT_TRIGGER_ENABLED` — flag operacional para permitir `POST /api/agent/trigger/` após testes.

## Faltando para aprendizado Larissa 21h

- `CRISP_LK_LARISSA_OPERATOR_ID` — identificador da Larissa no Crisp, para filtrar mensagens humanas dela.
- `CRISP_LK_LARISSA_EMAIL_HASH_OR_LABEL` — alternativa não sensível se o operador ID não estiver disponível.

## Convenção de segurança

- Não salvar valores no Brain.
- Não imprimir valores em logs.
- Scripts devem buscar valores no Doppler em tempo de execução.
- Qualquer resposta sobre sob encomenda/status pedido/entrega deve transbordar para Larissa, mesmo se houver dados disponíveis via Crisp/Hugo.

## Helper seguro para salvar valores quando Lucas fornecer

Script preparado, sem valores embutidos:

- `/opt/data/scripts/lk_hugo_doppler_upsert_secrets.py`

Uso: passar os valores apenas por variáveis de ambiente e informar os nomes permitidos. O script faz upsert no Doppler e imprime somente `UPSERTED NOME_DO_SECRET`.
