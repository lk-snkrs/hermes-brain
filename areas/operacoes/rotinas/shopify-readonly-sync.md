# Rotina — Shopify LK Read-only Sync

Objetivo: consultar Shopify LK para auditoria de pedidos, clientes, produtos e sinais de CRM sem alterar a loja.

## Integração

- Doc: `empresa/integracoes/shopify.md`.
- Secrets: `SHOPIFY_STORE_URL`, `SHOPIFY_ACCESS_TOKEN`.
- Área principal: `areas/lk/`.

## Permissões

- Read-only: consultar pedidos, clientes, produtos, tags e metadados.
- Write: alterar cliente, tags, pedido, produto ou nota interna exige aprovação contextual.
- External-send: qualquer mensagem ao cliente exige preview e aprovação Lucas.
- Admin/destructive: apps, webhooks, permissões, billing, deletes e temas exigem aprovação explícita + rollback.

## Procedimento read-only

1. Confirmar secrets com `hermes_doppler.sh exists SHOPIFY_STORE_URL SHOPIFY_ACCESS_TOKEN`.
2. Definir objetivo da consulta: pedido, cliente, SKU, segmento ou janela de datas.
3. Consultar somente endpoints GET/Admin GraphQL query.
4. Cruzar achado com Supabase LK quando necessário.
5. Registrar conclusão em rotina/relatório sem dados sensíveis desnecessários.

## Verificação

- Não usar mutações GraphQL.
- Não usar endpoints POST/PUT/PATCH/DELETE.
- Não exportar PII fora do contexto necessário.
- Não afirmar receita/cliente sem fonte viva.
