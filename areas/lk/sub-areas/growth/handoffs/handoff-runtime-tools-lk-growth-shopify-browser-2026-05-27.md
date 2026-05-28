# Handoff — adicionar Shopify write e browser operacional ao runtime LK Growth Telegram

Data: 2026-05-27
Origem: Lucas Cimino / Telegram
Status: solicitação de ajuste de runtime

## Problema observado

Durante a tentativa de publicar correções aprovadas na coleção `New Balance 204L`, o profile atual (`lk-growth` via Telegram) conseguiu:

- usar browser público;
- ler/validar página live;
- escrever Brain/skills/approval packet;

mas não conseguiu:

- executar Shopify Admin API write;
- usar terminal/curl/Doppler para PATCH/PUT via API;
- operar Shopify Admin UI via browser porque Cloudflare bloqueou a sessão (`Just a moment...`).

## Decisão de Lucas

Lucas pediu adicionar Shopify e browser “aqui”, ou seja, no runtime/profile operacional usado neste chat, para não depender de handoff quando houver aprovação explícita de produção.

## Requisito funcional

O profile LK Growth Telegram precisa conseguir, quando houver aprovação explícita no turno atual:

1. Consultar Doppler `lc-keys/prd` sem imprimir secrets.
2. Chamar Shopify Admin REST/GraphQL com escopo de write limitado.
3. Ler e escrever assets/theme settings/collection fields quando o approval packet autorizar.
4. Fazer backup/readback/hash/receipt local antes/depois.
5. Usar browser público para QA visual live com cachebuster.
6. Manter browser Admin UI como fallback apenas quando passar Cloudflare; API deve ser o caminho principal.

## Toolsets necessários

- `browser`: já aparece disponível neste runtime e funcionou para storefront público; manter habilitado.
- `terminal`: necessário para Doppler/curl/scripts de Shopify Admin API.
- `file`: já disponível para backup/receipt.
- `skills`, `memory`, `session_search`: manter.
- Opcional: MCP/custom tool `shopify_admin` para encapsular chamadas GET/mutation com guardrails e logs.

## Guardrails obrigatórios

- Não liberar write genérico sem aprovação escopada.
- Shopify production write só com:
  - escopo exato aprovado por Lucas;
  - backup local;
  - rollback path;
  - readback API;
  - QA storefront público;
  - receipt no Brain.
- Nunca imprimir `SHOPIFY_ACCESS_TOKEN` ou credenciais Doppler.
- Não tocar preço, estoque, produto, campanha, checkout, Klaviyo, GMC ou Meta se o approval não cobrir explicitamente.

## Implementação recomendada

1. No profile/runtime Telegram LK Growth, habilitar `terminal` e manter `browser`:
   - `hermes tools enable terminal`
   - `hermes tools enable browser`
   - reiniciar gateway ou iniciar nova sessão para refletir toolsets.
2. Verificar se o gateway está usando o profile correto (`lk-growth`) e não outro profile sem toolset.
3. Confirmar existência dos secrets sem imprimir valores:
   - `SHOPIFY_STORE_URL`
   - `SHOPIFY_ACCESS_TOKEN`
   - Doppler token/local helper.
4. Criar/instalar um helper seguro para Shopify theme hotfixes, se ainda não existir:
   - lista themes;
   - valida `lk-new-theme/production` role `main`;
   - fetch asset;
   - backup;
   - patch mínimo;
   - PUT asset;
   - readback hash/substrings;
   - receipt JSON/MD.
5. Após restart/nova sessão, reexecutar o hotfix da coleção 204L aprovado.

## Correção pendente bloqueada por runtime

Coleção: https://lksneakers.com.br/collections/new-balance-204l

Escopo aprovado:

- H1 +3pt;
- kicker `CURADORIA LK` sem repetir `NEW BALANCE 204L`;
- paginação 20 produtos por página.

Documento de execução: `areas/lk/sub-areas/growth/handoffs/handoff-shopify-production-204l-correcoes-2026-05-27.md`.
