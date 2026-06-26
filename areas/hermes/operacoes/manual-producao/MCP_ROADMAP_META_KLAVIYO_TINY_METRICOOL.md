# MCP Roadmap — Meta Ads, Klaviyo, Tiny e Metricool

Gerado em: 2026-05-30T22:29:07+00:00  
Status: **roadmap técnico / sem ativação runtime**  
Escopo: resposta à sugestão de Lucas de conectar Meta Ads, Klaviyo, Tiny e Metricool por MCP.  
Guardrail: não instala, não edita config, não reinicia profiles, não cria/altera secrets e não faz writes externos.

## Veredito

A sugestão faz sentido, mas eu não conectaria os quatro da mesma forma.

Ordem segura recomendada:

1. **Metricool MCP wrapper próprio read-only** — melhor primeiro desses quatro.
2. **Meta Ads MCP read-only** — alto valor para LK Growth, mas bloquear mutations.
3. **Tiny MCP read-only** — alto valor para estoque/operação, mas risco crítico; precisa whitelist rígida.
4. **Klaviyo MCP read-only** — útil para CRM/flows, mas sends/mutations devem ficar bloqueados.

## Evidência de credenciais disponíveis por nome

Doppler `lc-keys/prd` contém nomes de secrets para os quatro domínios, sem valores expostos:

- Meta: `META_ACCESS_TOKEN`, `META_ADS_ACCOUNT_ID`, `META_APP_ID`, `META_APP_SECRET`, `META_PIXEL_ID`
- Klaviyo: `KLAVIYO_API_KEY`, `KLAVIYO_CONNECTION_ID`, `KLAVIYO_PUBLIC_KEY`
- Tiny: `TINY_API_TOKEN`, `TINY_CLIENT_ID`, `TINY_CLIENT_SECRET`
- Metricool: `METRICOOL_API_KEY`, `METRICOOL_API_TOKEN`, `METRICOOL_BLOG_ID`, `METRICOOL_USER_ID`

## MCPs/pacotes candidatos observados

### Meta Ads

Pacote candidato:

- `@cesteral/meta-mcp`
- versão observada: `1.1.0`
- descrição: Meta Ads MCP Server — campaign entity management and reporting via Meta Graph API

Uso permitido no piloto:

- `list_ad_accounts`
- `get_campaigns`
- `get_adsets`
- `get_ads`
- `get_insights`
- leitura de spend, impressions, clicks, purchases, ROAS

Bloqueado:

- criar/editar campanhas;
- pausar/ativar;
- orçamento;
- audiences;
- creatives;
- pixels/events mutation.

Profile sugerido:

- `lk-growth` ou `lk-analyst-readonly`.

### Klaviyo

Pacote candidato:

- `klaviyo-mcp`
- versão observada: `1.0.0`
- descrição: Model Context Protocol server for Klaviyo email marketing API

Uso permitido no piloto:

- listar campaigns/flows;
- obter métricas;
- listar segmentos/listas de forma resumida;
- leitura limitada de profiles quando necessário.

Bloqueado:

- send;
- create/update campaign;
- update profile/list/subscription;
- trigger flow;
- export de audiência.

Profile sugerido:

- `lk-growth` ou `lk-analyst-readonly`.

### Tiny

Pacote candidato:

- `@codespar/mcp-tiny`
- versão observada: `0.2.1`
- descrição: MCP server for Tiny ERP — products, stock, categories, warehouses, price lists, orders, invoices, accounts payable/receivable

Uso permitido no piloto:

- consultar produto por SKU/código;
- consultar estoque por SKU/tamanho;
- consultar pedido por ID quando necessário;
- listar depósitos/categorias somente para resolver ambiguidade.

Bloqueado:

- alterar estoque;
- criar/editar pedido;
- notas fiscais;
- contas a pagar/receber;
- preço;
- cadastro de produto;
- qualquer delta local.

Regra de ouro:

- Tiny é fonte da verdade; Shopify é gatilho/superfície. MCP Tiny não pode virar automação de delta.

Profile sugerido:

- `lk-ops` ou profile read-only dedicado, não `default`.

### Metricool

Pacote MCP específico:

- não encontrei pacote Metricool MCP maduro/relevante neste inventário.

Caminho recomendado:

- criar **MCP wrapper próprio local** em cima do fluxo já provado pela skill `metricool-api-analytics`.

Tools read-only propostas:

- `metricool_list_brands`
- `metricool_get_brand_connections`
- `metricool_get_google_ads_campaigns`
- `metricool_get_meta_ads_campaigns`
- `metricool_get_social_summary`
- `metricool_get_campaign_summary`

Bloqueado:

- posts;
- scheduling;
- campaign writes;
- alteração de conexões;
- qualquer mutation social/ads.

Profile sugerido:

- `lk-growth` ou `lk-analyst-readonly`.

## Arquitetura segura proposta

### Fase A — wrappers/descoberta sem ativar runtime

- criar scripts/wrappers locais por MCP que buscam secrets via Doppler;
- testar `mcporter list` e tool schemas ad-hoc;
- não editar `config.yaml` ainda;
- não reiniciar profile.

### Fase B — profile read-only

- escolher `lk-analyst-readonly` como sandbox preferencial para Meta/Metricool/Klaviyo;
- escolher `lk-ops` ou `lk-ops-readonly` para Tiny;
- sampling off;
- whitelist documentada.

### Fase C — ativação controlada

- backup config;
- adicionar um MCP por vez;
- restart só do profile alvo;
- verificar discovery/logs;
- executar uma query pequena;
- registrar receipt.

## Ordem operacional sugerida

1. Metricool wrapper próprio read-only.
2. Meta Ads MCP read-only.
3. Tiny MCP read-only, com whitelist e teste por 1 SKU.
4. Klaviyo MCP read-only.

Motivo:

- Metricool e Meta dão visão de performance sem tocar produção.
- Tiny é valiosíssimo, mas qualquer erro tem impacto operacional direto.
- Klaviyo tem risco alto de disparo/CRM; bom para leitura, perigoso para ação.

## Aprovação necessária para conectar de verdade

Para cada MCP real, a aprovação precisa ser individual. Exemplo:

> Aprovo configurar `meta_ads` MCP read-only no profile `lk-analyst-readonly`, usando `META_ACCESS_TOKEN` e `META_ADS_ACCOUNT_ID` do Doppler, sampling off, sem writes, com backup de config, restart apenas desse profile e rollback removendo o server.

Sem aprovação desse nível, a execução fica em discovery, docs e testes ad-hoc sem runtime mutation.
