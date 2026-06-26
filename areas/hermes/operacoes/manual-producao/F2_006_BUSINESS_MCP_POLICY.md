# F2-006 — Política MCP de negócio

Gerado em: 2026-05-30T22:29:07+00:00  
Status: **política v0.1 / local-documental**  
Escopo: regras para ativar MCPs de negócio no ecossistema Lucas/LK/Zipper/SPITI/Hermes.  
Guardrail: este documento **não autoriza** instalar pacote, editar `config.yaml`, reiniciar profile, criar token, executar write externo ou expor MCP publicamente.

## Tese operacional

MCP é útil quando reduz scripts avulsos e padroniza consultas. Mas MCP de negócio também vira uma superfície de produção: pode ler dados sensíveis, gastar créditos, alterar campanhas, enviar mensagens, atualizar estoque/produtos ou tocar clientes.

Portanto, a regra é:

1. **read-only primeiro**;
2. **sampling off por padrão**;
3. **secrets via Doppler**;
4. **profile isolado por domínio/empresa quando possível**;
5. **whitelist de tools permitidas**;
6. **writes externos só com approval por payload e rollback**.

## Classes de risco MCP

### M0 — Local/tooling sem credencial

Exemplos:

- Playwright local em preview;
- filesystem restrito a diretório temporário;
- docs/context MCP sem segredo.

Permitido:

- descoberta/listagem;
- uso local sem produção;
- documentação.

Bloqueado:

- login/click em produção sem approval;
- filesystem amplo em `/opt/data` sem escopo.

### M1 — Read-only externo gratuito/baixo risco

Exemplos:

- APIs públicas;
- crawling pontual de URL pública;
- docs/search.

Permitido:

- consultas pontuais;
- output local/Telegram curto.

Bloqueado:

- scraping em massa;
- rotina recorrente sem limite.

### M2 — Read-only externo com credencial/custo

Exemplos:

- DataForSEO;
- Supabase com role read-only;
- Metricool analytics;
- Meta Ads insights;
- Klaviyo analytics/list read;
- n8n status/executions read.

Permitido após approval/política:

- list/get/query/report;
- consultas pequenas;
- whitelisted tools.

Bloqueado:

- batch amplo;
- loops recorrentes sem orçamento;
- ferramentas de create/update/delete/send/run.

### M3 — Banco/CRM/cliente sensível

Exemplos:

- Supabase Zipper/SPITI/LK;
- Crisp/Hugo;
- WhatsApp/Mordomo data;
- Gmail/Calendar;
- Shopify customers/orders.

Permitido:

- read-only com profile e escopo por empresa;
- mascaramento de PII quando possível;
- output mínimo necessário.

Bloqueado:

- contato externo automático;
- alteração de cliente/conversa/follow-up;
- criação de evento/email/WhatsApp sem escopo aprovado;
- mistura Zipper/SPITI/LK.

### M4 — External write / produção / dinheiro / estoque / campanha

Exemplos:

- Shopify product/order/customer/inventory writes;
- Tiny estoque/pedidos/notas;
- Klaviyo sends/campaign/list mutation;
- Meta/Google Ads budget/campaign/creative changes;
- n8n run/activate/update/delete;
- Stripe/payments;
- Supabase mutations em produção.

Permitido apenas com:

- approval packet específico;
- payload exato;
- snapshot/readback;
- rollback;
- receipt;
- escopo temporal/quantitativo.

## Padrão de configuração

Para cada MCP candidato, documentar antes de ativar:

- Nome do server.
- Profile dono.
- Empresa/domínio.
- Pacote/URL.
- Fonte dos secrets no Doppler: nomes apenas, nunca valores.
- Scopes/roles usados.
- Tools permitidas.
- Tools bloqueadas.
- Sampling: `enabled: false` por padrão.
- Timeout/connect timeout.
- Plano de teste.
- Rollback.
- Quem recebe o receipt.

## Política por integração sugerida por Lucas

Lucas sugeriu conectar Meta Ads, Klaviyo, Tiny e Metricool por MCP. A classificação segura é:

### Meta Ads MCP

Valor:

- alta utilidade para leitura de spend, ROAS, campanhas e criativos;
- ajuda LK Growth sem depender só de relatórios manuais;
- pode cruzar com Metricool/Shopify/Tiny.

Risco:

- alto se expuser mutations de campanhas, orçamento, status, creative ou audiences.

Política:

- profile: `lk-growth` ou futuro `lk-analyst-readonly`;
- permitido inicialmente: insights/read/list campaigns/adsets/ads/accounts;
- bloqueado: create/update/pause/enable/budget/audience/creative;
- pacote candidato observado: `@cesteral/meta-mcp` versão `1.1.0`;
- Doppler contém nomes relevantes: `META_ACCESS_TOKEN`, `META_ADS_ACCOUNT_ID`, `META_APP_ID`, `META_APP_SECRET`, `META_PIXEL_ID`.

Status: **candidato bom, mas read-only estrito**.

### Klaviyo MCP

Valor:

- leitura de listas, perfis, segmentos, campanhas, flows e métricas;
- ajuda CRM/LK Growth.

Risco:

- muito alto para sends, campaign mutations, list/profile updates e automações.

Política:

- permitido inicialmente: read analytics/list campaigns/flows/segments/profiles limitado;
- bloqueado: send, create/update campaign, update profile/list/subscription, trigger flow;
- pacote candidato observado: `klaviyo-mcp` versão `1.0.0`;
- Doppler contém nomes relevantes: `KLAVIYO_API_KEY`, `KLAVIYO_CONNECTION_ID`, `KLAVIYO_PUBLIC_KEY`.

Status: **candidato útil, depois de Meta/Metricool ou em paralelo com whitelist forte**.

### Tiny MCP

Valor:

- altíssimo para LK Ops: produtos, estoque, pedidos, depósitos, categorias;
- Tiny é fonte da verdade de estoque.

Risco:

- crítico: estoque/pedido/nota/contas são produção operacional;
- qualquer mutation errada quebra loja/operação.

Política:

- permitido inicialmente: somente consultar produto/estoque/pedido por ID/SKU/tamanho;
- bloquear tudo que altere estoque, pedido, nota, preço, contas, cadastro;
- não usar MCP para delta de estoque; Tiny continua fonte, Shopify gatilho/superfície;
- pacote candidato observado: `@codespar/mcp-tiny` versão `0.2.1`;
- Doppler contém nomes relevantes: `TINY_API_TOKEN`, `TINY_CLIENT_ID`, `TINY_CLIENT_SECRET`.

Status: **alto valor, mas não deve ser piloto geral; criar wrapper/whitelist local antes de expor ao Telegram**.

### Metricool MCP

Valor:

- leitura consolidada de social/ads/performance;
- já é útil para LK Growth e relatórios.

Risco:

- menor se read-only analytics;
- risco aumenta se permitir postagens/campaign actions.

Disponibilidade:

- não foi encontrado pacote MCP específico/maduro chamado Metricool via npm neste inventário;
- já existe skill/API operacional `metricool-api-analytics`.

Política:

- criar MCP próprio/local fino se for necessário, expondo apenas tools read-only:
  - `metricool_list_brands`
  - `metricool_get_ads_campaigns`
  - `metricool_get_social_analytics`
  - `metricool_get_campaign_summary`
- bloquear posts, scheduling, campaign writes;
- Doppler contém nomes relevantes: `METRICOOL_USER_ID`, `METRICOOL_BLOG_ID`, `METRICOOL_API_TOKEN`, `METRICOOL_API_KEY`.

Status: **melhor caminho é MCP wrapper próprio, não pacote genérico**.

## Política para Supabase MCP

Valor:

- melhor próximo MCP para Zipper/SPITI;
- reduz scripts avulsos;
- permite schema discovery e queries pequenas.

Risco:

- banco/CRM/cliente sensível;
- precisa separar empresas/projetos;
- service role é perigoso se não houver wrapper/role read-only.

Política:

- criar um approval packet por empresa/projeto;
- preferir role/token read-only;
- bloquear mutations;
- output com mínimo de PII;
- nunca misturar Zipper Vendas, Zipper CRM/Main, SPITI e LK no mesmo profile/tool sem prefixos/escopo claro.

## Política para DataForSEO MCP

Status:

- já configurado em `lk-shopify` e `lk-trends`;
- piloto pequeno executado com sucesso em `F2_007_DATAFORSEO_MCP_PILOT_RECEIPT.md`.

Permitido:

- queries pontuais de keyword/intent/SERP/onpage por URL específica.

Bloqueado:

- scans/batch amplos;
- rotina recorrente sem orçamento;
- tratar dado como decisão automática.

## Aprovação mínima para ativar novo MCP real

A frase de aprovação deve conter:

- profile alvo;
- MCP alvo;
- modo `read-only` ou write específico;
- secrets permitidos por nome;
- se pode editar `config.yaml`;
- se pode reiniciar o profile;
- rollback aceito.

Exemplo seguro:

> Aprovo configurar `meta_ads` MCP read-only no profile `lk-growth`, usando secrets Doppler `META_ACCESS_TOKEN` e `META_ADS_ACCOUNT_ID`, sampling off, sem writes, com backup de config e restart apenas do `lk-growth`. Rollback: remover o server do config e reiniciar `lk-growth`.

Sem isso, o trabalho permitido é documentação, discovery de pacotes, verificação de secret names e testes ad-hoc que não alterem runtime.

## Ordem recomendada de adoção

1. DataForSEO — já existente, consultas pequenas.
2. Metricool MCP wrapper próprio read-only — baixo risco e já temos skill/API.
3. Meta Ads MCP read-only — útil, mas bloquear mutations.
4. Supabase MCP read-only por projeto — alto valor para Zipper/SPITI.
5. Tiny MCP read-only — alto valor, alto risco; só com wrapper/whitelist.
6. Klaviyo MCP read-only — útil, mas sends/mutations bloqueados.
7. Shopify MCP read-only — depois; não usar para estoque/write.

## Não autorizado por esta política

- Instalar MCP em runtime produtivo.
- Editar `config.yaml` de profiles.
- Reiniciar gateway/profile.
- Criar/alterar secrets.
- Fazer writes externos.
- Expor MCP via endpoint público.
