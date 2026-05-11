# LK OS — Data Spine Read-only, 2026-05-11

Status: v0.1 documental operacional + primeiro snapshot read-only multi-fonte executado. Nenhum write, cron, campanha, banco de produção, Shopify/Tiny/Klaviyo/Notion/Meta/Google/n8n ou envio externo foi executado nesta etapa.

## Objetivo

Criar a espinha dorsal de dados do LK Operating System para que todo relatório futuro consiga responder três perguntas antes de recomendar ação:

1. De onde veio este número?
2. Qual é a fonte da verdade para este tipo de dado?
3. O número é fato operacional, sinal de plataforma ou inferência?

## Decisão de arquitetura

O Data Spine da LK começa como camada **read-only + SQLite local operacional**.

- Fontes vivas continuam sendo fonte da verdade.
- SQLite local é cache/espelho de trabalho e histórico de execução do Hermes, não fonte oficial.
- Dados pessoais ficam fora do Brain; quando necessários para execução local, ficam em `/opt/data/hermes_bruno_ingest/local_sql/` ou `private_exports/` com permissão restrita.
- Dados externos voláteis de StockX/GOAT/Droper/KicksDev são on-demand para compra/reposição/subida, não full sync permanente de preço.

## Inventário de fontes v0.1

### Shopify

- Função: vendas, clientes, pedidos, produtos, variants, SKUs, source/canal, tags e catálogo.
- Fonte da verdade para: pedido, receita Shopify, cliente comercial, produto publicado/draft, SKU canônico da variant.
- Não usar como verdade final de estoque.
- Permissão padrão: read-only GET/query.
- Writes: exigem preview, backup/rollback e aprovação Lucas.

### Tiny, depósito `LK | CONTROLE ESTOQUE`

- Função: estoque operacional por produto/variação/tamanho.
- Fonte da verdade para: estoque livre, reservado e disponibilidade real.
- Regra: disponibilidade precisa ser variante/tamanho, não produto genérico.
- Writes: qualquer `codigo`, estoque, preço ou cadastro exige aprovação explícita e rollback.

### Supabase LK

- Função: espelho/tabelas analíticas existentes de pedidos, itens, produtos, clientes e RFM.
- Fonte da verdade: não substitui Shopify/Tiny, mas acelera análise read-only quando as tabelas estão atualizadas.
- Regra: verificar freshness/contagem antes de usar como base de decisão.

### GA4 / Shopify Analytics

- Função: sessões, canais, funil, páginas, conversão, comportamento.
- Fonte da verdade para: tráfego e leitura de conversão por canal quando reconciliada.
- Regra: GA4 mostra canal/funil; não deve ser usado sozinho como receita operacional por produto.

### Google Ads / Meta Ads / Metricool

- Função: custo, campanhas, criativos, ad_id, compras atribuídas por plataforma e sinais de performance.
- Fonte da verdade para: gasto e atribuição de plataforma.
- Não é fonte final para receita real ou produto vendido.
- Regra: separar `Pareto-compatible`, plataforma e `Lucas-operational`.

### Klaviyo

- Função: campanhas online, templates, listas, profiles e resultado de e-mail.
- Fonte da verdade para: estado de campanha/lista/template no Klaviyo.
- Regra: Draft/list/template são writes externos seguros apenas quando aprovados; envio/agendamento/flow sempre exige aprovação final.

### Evolution / WhatsApp

- Função: loja física, concierge e relacionamento 1:1.
- Fonte da verdade para: status de envio/telefone quando validado pela API.
- Regra: qualquer mensagem real a cliente/time/fornecedor exige aprovação explícita.

### Notion LK

- Função: compras, encomendas e fila operacional aprovada.
- Fonte da verdade para: intenção operacional aprovada quando registrada pela equipe.
- Regra: criar item de compra/encomenda é write operacional e exige aprovação.

### Judge.me

- Função: reviews e prova social.
- Uso inicial: enriquecer PDP/CRO e SEO com sinal de confiança.
- Regra: read-only até existir playbook de uso recorrente.

### Frenet

- Função: frete, prazo e possíveis gargalos de checkout.
- Uso inicial: diagnóstico de conversão e experiência logística.
- Regra: read-only até existir rotina específica.

### Google Search Console / Merchant Center

- GSC: queries, páginas, CTR, posição, oportunidades orgânicas.
- Merchant Center: feed, reprovação, disponibilidade, preço, Shopping.
- Regra: SEO/GMC gera fila de melhoria; alterações em feed/PDP/Shopify exigem aprovação.

## Matriz de credenciais esperadas no Doppler

Verificação de nomes executada em 2026-05-11 via Doppler HTTP API, sem imprimir valores.

- OK `SHOPIFY_STORE_URL`.
- OK `SHOPIFY_ACCESS_TOKEN`.
- OK `SUPABASE_LK_URL`.
- OK `SUPABASE_LK_SERVICE_KEY`.
- OK `KLAVIYO_API_KEY`.
- OK `GOOGLE_ADS_CUSTOMER_ID`.
- OK `GA4_PROPERTY_ID`.
- OK `META_ACCESS_TOKEN`.
- OK `N8N_API_KEY`.
- OK `NOTION_API_KEY`.
- OK `TINY_API_TOKEN`.
- OK `TINY_CLIENT_ID`.
- OK `TINY_CLIENT_SECRET`.
- OK `FRENET_TOKEN`.
- OK `JUDGEME_API_TOKEN`.
- OK `METRICOOL_API_TOKEN`.
- OK `METRICOOL_USER_ID`.
- OK `GOOGLE_SERVICE_ACCOUNT_JSON`.
- MISSING antigo esperado `TINY_TOKEN`, substituído por `TINY_API_TOKEN`.
- MISSING antigo esperado `METRICOOL_USER_TOKEN`, substituído por `METRICOOL_API_TOKEN`.

## Dicionário canônico de entidades

### Pedido

- Chave primária preferida: Shopify order ID.
- Campos mínimos: data, status financeiro, status fulfillment, source/canal, tags, total, cliente, itens.
- Uso: vendas, recompra, RFM, produtos vendidos, source de canal.

### Cliente

- Chave operacional: Shopify customer ID quando existir; email normalizado apenas para matching interno privado.
- Saída pública/Telegram: mascarada ou agregada.
- Uso: RFM, histórico, recompra, VIP, loja física/online.

### Produto

- Chave: Shopify product ID + handle.
- Campos: título, vendor, tipo, tags, status, URL, imagem principal.
- Uso: catálogo, SEO, conteúdo, Shopify Operations.

### Variante / tamanho

- Chave: Shopify variant ID.
- SKU canônico: Shopify SKU.
- Campos: tamanho, preço, SKU, produto pai, status comercial.
- Uso: estoque, recomendação, disponibilidade, campanha.

### SKU

- Shopify SKU é canônico para matching comercial.
- Tiny `codigo` deve espelhar Shopify quando possível, mas Tiny é a fonte de estoque.
- Divergência vira fila de saneamento, não decisão comercial automática.

### Estoque

- Chave: Tiny product/variation ID + SKU/tamanho mapeado.
- Métrica: saldo, reservado, livre estimado.
- Uso: Stock Intelligence, CRM, sourcing, campanha.

### Campanha / influencer / criativo

- Chaves: Meta ad_id, ad_name, campaign_name, UTM, cupom quando houver.
- Regra Maicon: influencer vem primeiro de `ad_name`; somar todos os ad_ids do mesmo influencer normalizado; separar Marias.
- Uso: Paid & Influencer Intelligence, consequência de estoque.

### UTM / cupom

- Uso: ponte entre plataforma, Shopify, GA4 e CRM.
- Sem ponte segura, status é sinal/ambíguo, não atribuição operacional confirmada.

### Aprovação / ação

- Chave: ID interno de ação no Brain/local SQL.
- Status recomendado: `needs_data`, `needs_preview`, `approved`, `rejected`, `executed`, `held`, `blocked`.
- Uso: Learning Loop e Approval Manager.

## Regras de reconciliação

### Shopify vs GA4

- Shopify responde “vendeu quanto, qual pedido, qual produto, qual cliente”.
- GA4 responde “veio de onde, como navegou, qual funil/canal”.
- Receita executiva por canal deve explicar se vem de Shopify, GA4 ou reconciliação.

### Shopify vs Meta/Google

- Meta/Google respondem gasto e atribuição de plataforma.
- Shopify confirma pedido/produto/receita real.
- ROAS de plataforma não é ROAS operacional final quando não há ponte segura com Shopify.

### Shopify vs Tiny

- Shopify SKU identifica a variant comercial.
- Tiny confirma estoque livre.
- Se Shopify vendeu mas Tiny não mapeia, a ação correta é saneamento SKU, não campanha/reposição automática.

### Klaviyo vs Shopify

- Klaviyo mostra campanha/list/profile/resultado de e-mail.
- Shopify confirma se a venda aconteceu e qual produto foi comprado.
- Campanha não deve ser julgada só por abertura/clique.

### CRM loja física vs online

- Curadoria/concierge de alto toque deve começar por compra âncora POS/LK Flagship.
- Online escala via Klaviyo; loja física usa WhatsApp/Evolution quando aprovado.
- Não misturar base online em ação de concierge física sem aprovação explícita.

## Lacunas e riscos atuais

- Tiny precisa de rotina estável de freshness/estoque por variação antes de automação recorrente.
- Merchant Center ainda precisa diagnóstico próprio.
- Judge.me e Frenet têm credenciais, mas ainda não têm rotina LK recorrente documentada.
- Notion LK está mapeado como destino operacional aprovado, mas writes seguem bloqueados.
- Klaviyo Draft P1 existe, mas link de UI não deve ser inferido por ID; localizar pelo painel.
- PII deve ficar fora do Brain e do Telegram; exports privados precisam chmod restrito.
- Relatórios semanais precisam rotular claramente: plataforma, GA4, Shopify confirmado e inferência.

## Contrato de saída para scripts read-only futuros

Todo script do Data Spine deve gerar JSON/MD com:

- `generated_at`.
- janela analisada.
- fonte consultada.
- credenciais usadas por nome, sem valor.
- contagem de registros lidos.
- freshness máxima/mínima.
- campos sensíveis omitidos ou mascarados.
- status `read_only=true`.
- lista explícita de writes/envios que não foram feitos.
- lacunas e próximos passos.

## Snapshot read-only v0.1 executado

Script: `scripts/lk_os_data_spine_snapshots_20260511.py`.

Relatório público sanitizado: `reports/lk-os-data-spine-snapshot-2026-05-11.md` e `.json`.

Arquivo privado auditável, fora do Git: `/opt/data/hermes_bruno_ingest/local_sql/lk_data_spine_snapshots/` com permissão restrita.

Fontes lidas com sucesso em 2026-05-11:

- Shopify: `fact_shopify`, 2.279 produtos, 89 pedidos na janela de 7 dias, freshness de pedido até 2026-05-11.
- Tiny: `fact_tiny_stock`, amostra de estoque validou o depósito `LK | CONTROLE ESTOQUE` em 6/6 checks.
- GA4: `fact_ga4`, 12 canais retornados na janela 2026-05-04 a 2026-05-10.
- Meta Ads: `platform_signal`, conta ativa `act_1242062509867163`, último 7 dias lido.
- Metricool/Google Ads: `platform_signal`, brand `LK Sneakers`, blog `6217010`, 21 linhas de Google Ads na janela.
- Klaviyo: `platform_signal`, listas e campaigns lidas via API; campanha P1 segue `Draft`, sem send_time.

Regra: os números de Meta, Google/Metricool e Klaviyo continuam sendo sinal de plataforma até reconciliação explícita com Shopify/GA4.

## Próximo passo técnico

Depois do snapshot consolidado v0.1, separar em módulos menores ou evoluir para freshness report recorrível:

1. `lk_data_spine_shopify_snapshot.py`.
2. `lk_data_spine_tiny_stock_snapshot.py`.
3. `lk_data_spine_ga4_channels_snapshot.py`.
4. `lk_data_spine_paid_snapshot.py`.
5. `lk_data_spine_klaviyo_snapshot.py`.
6. `lk_data_spine_freshness_report.py`.

Nenhum desses scripts deve escrever em sistemas externos. A primeira versão pode escrever apenas JSON/MD local em `reports/` e, se houver PII, em `private_exports/` com permissão restrita.
