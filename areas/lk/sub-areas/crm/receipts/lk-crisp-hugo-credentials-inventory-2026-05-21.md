# Receipt — Inventário inicial credenciais Crisp/Hugo LK Response Brain

Data: 2026-05-21
Escopo: etapa 1 do projeto LK Crisp/Hugo Response Brain — localizar credenciais existentes e mapear faltantes.

## Ações executadas

- Carregado skill seguro de Doppler.
- Verificado ambiente: Doppler CLI ausente, token local autorizado presente, helper presente mas dependente do CLI.
- Consultado Doppler `lc-keys/prd` via API sem imprimir valores.
- Listados apenas nomes de secrets relacionados a Crisp/Hugo/MCP/Workflow.
- Validada existência/shape dos secrets Crisp LK sem revelar valores.
- Testada chamada read-only no Crisp para confirmar credencial REST de conversas.

## Secrets relacionados encontrados

- `CRISP_LK_REST_TIER`
- `CRISP_LK_REST_TOKEN_ID`
- `CRISP_LK_REST_TOKEN_KEY`
- `CRISP_LK_WEBSITE_ID`
- `N8N_MCP_ACCESS_TOKEN`
- `WORKFLOW_LOG_API_URL`

## Validação segura

- Total de nomes de secrets em `lc-keys/prd`: 240.
- Secrets Crisp LK REST presentes: OK.
- `CRISP_LK_WEBSITE_ID`: presente, comprimento compatível com UUID.
- `CRISP_LK_REST_TOKEN_ID`: presente, comprimento compatível com UUID.
- `CRISP_LK_REST_TOKEN_KEY`: presente.
- Chamada Crisp listagem de conversas: HTTP 206.
- Chamada Crisp website profile: HTTP 401; não usado como bloqueador porque a listagem de conversas funcionou e o endpoint pode exigir escopo/tier específico.

## Lacunas identificadas

Ainda não encontrei no Doppler nomes explícitos para Hugo/MCP:

- `HUGO_LK_WEBSITE_TOKEN`
- `HUGO_LK_MCP_SIGNING_SECRET`
- `HUGO_LK_MCP_BEARER_TOKEN`
- `HUGO_LK_HANDOFF_WORKFLOW_ID`
- `CRISP_LK_LARISSA_OPERATOR_ID`

## Arquivo atualizado

- `knowledge/lk-response-brain/credentials-required.md`
- Helper seguro criado: `/opt/data/scripts/lk_hugo_doppler_upsert_secrets.py`

## Próximo passo seguro

Obter no Crisp/Hugo:

1. Hugo Website Token / API token.
2. Secret MCP `mcp_sec_...` da integração MCP.
3. Workflow ID de transbordo para Larissa.
4. Identificador da Larissa no Crisp.

Depois salvar no Doppler `lc-keys/prd` usando apenas nomes de secrets, sem registrar valores no Brain.
