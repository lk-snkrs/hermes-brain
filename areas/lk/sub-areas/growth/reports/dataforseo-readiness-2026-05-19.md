# DataForSEO Readiness — LK Growth

Data: 2026-05-19
Área: LK / Growth / SEO-CRO-GEO
Modo: Read-only / credencial API paga

## Resumo executivo

- Status da credencial: OK.
- Status Doppler: OK, credenciais salvas em `lc-keys/prd`.
- Status API DataForSEO: OK via endpoint de conta `appendix/user_data`.
- Status MCP Hermes/Claude SEO: pendente de configuração/instalação do server DataForSEO MCP; as credenciais já existem para conexão.

## Secrets salvos no Doppler

Valores não documentados neste arquivo.

- `DATAFORSEO_LOGIN`
- `DATAFORSEO_PASSWORD`
- `DATAFORSEO_AUTH_B64`
- `DATAFORSEO_API_LOGIN`
- `DATAFORSEO_API_PASSWORD`

## Validação executada

Endpoint: `GET https://api.dataforseo.com/v3/appendix/user_data`

Resultado:

- HTTP: 200
- DataForSEO status_code: 20000
- Status message: Ok.
- Login conferido contra credencial: match.
- Campos de conta retornados: money/rates presentes.

## Guardrails

- DataForSEO é API paga/creditada; consultas live SERP, keyword volume, backlink, AI visibility e on-page devem ser usadas com parcimônia.
- Antes de rodar consultas em lote, estimar custo e pedir aprovação se houver volume relevante.
- Não rodar crawls, exports grandes ou listas extensas sem aprovação explícita.
- Não registrar valores de login/senha/base64 no Brain, logs ou relatórios.

## Próximo passo técnico

- Configurar/instalar DataForSEO MCP server no perfil LK Growth/Claude SEO quando disponível no runtime.
- Depois do MCP ativo, rodar um smoke test controlado e barato, por exemplo:
  - 1 live SERP Brasil/pt-BR para uma keyword LK;
  - 1 keyword volume para lista curta;
  - 1 AI/GEO check simples;
  - registrar custo e evidência.

## Status para decisão

DataForSEO saiu de bloqueado por credencial para: `API CREDENTIAL OK / MCP PENDENTE`.
