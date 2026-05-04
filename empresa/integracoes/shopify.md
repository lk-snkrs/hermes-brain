# Integração — Shopify LK

## Escopo

Shopify é a fonte operacional de e-commerce da LK Sneakers: pedidos, clientes, produtos, coleções e parte do contexto de CRM/compras.

## Secrets Doppler

- `SHOPIFY_STORE_URL`
- `SHOPIFY_ACCESS_TOKEN`

## Read-only

- Consultar pedidos, clientes, produtos, variantes, tags, coleções e metadados.
- Cruzar dados com Supabase LK para análise de RFM, cross-sell e atendimento.
- Verificar status de syncs e inconsistências, sem alterar Shopify.

## Write

- Criar ou atualizar tags internas, notas operacionais e metadados quando houver processo documentado.
- Atualizar dados de cliente apenas se a fonte e intenção forem claras.

## External-send

- Qualquer comunicação com cliente via Shopify, automação conectada, email/SMS/WhatsApp derivado de dados Shopify exige preview Lucas.

## Admin/destructive

- Alterar apps, permissões, temas, domínios, checkout, pagamentos, frete, produtos em massa ou webhooks exige aprovação explícita e rollback.

## Verificação segura

- Executar consultas com limite pequeno primeiro.
- Registrar apenas IDs, contagens e status; não salvar dados pessoais desnecessários no Brain.

## Escala de permissões

- Read-only: consultar metadados, status, listas, métricas e registros sem alterar dados.
- Write: criar/atualizar dados internos, tags, notas, segmentos ou configurações não destrutivas.
- External-send: enviar mensagem, email, campanha, notificação ou contato com cliente/lead/parceiro. Exige preview e aprovação de Lucas.
- Admin/destructive: apagar dados, alterar credenciais, webhooks, domínios, billing, permissões, deploys, containers, produção ou integrações críticas. Exige aprovação explícita, plano de backup e rollback.

Regra de secrets: este arquivo lista apenas nomes de secrets no Doppler `lc-keys/prd`; valores reais nunca entram no GitHub.
