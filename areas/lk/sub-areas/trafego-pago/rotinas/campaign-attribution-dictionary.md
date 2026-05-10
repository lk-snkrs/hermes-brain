# Campaign Attribution Dictionary — LK

Status: rotina documental/read-only v0.1. Não cria campanha, não altera Meta/Google/Shopify/GA4/Klaviyo, não envia mensagem e não muda orçamento.

## Objetivo

Criar o dicionário canônico que liga o nome real das campanhas/anúncios de mídia paga aos sinais comerciais da Shopify/GA4, aos influenciadores e aos produtos esperados.

Sem esse dicionário, `campaign_name` do Meta, `utm_campaign` da Shopify/GA4 e nome de influencer continuam sendo três linguagens diferentes. O resultado é ROAS de plataforma alto, match Shopify baixo e pouca confiança para decidir estoque, criativo ou verba.

## Pergunta que a rotina responde

> Esta campanha/influencer vendeu o quê, para quem, com qual custo, com qual evidência Shopify e com qual consequência de estoque?

## Fontes read-only

- Meta Ads Insights: `campaign_name`, `adset_name`, `ad_name`, spend, impressions, clicks, purchases e attributed value.
- Google Ads/Metricool: campanha, custo e performance quando disponível.
- Shopify: pedidos web, source, landing/referrer, `utm_campaign`, cupom, produto, SKU, variante/tamanho e receita.
- GA4: source/medium/campaign, landing page, sessão e contexto de funil.
- Tiny `LK | CONTROLE ESTOQUE`: estoque operacional por SKU/tamanho para consequência de campanha.
- Brain LK: mapa humano de influencers, handles, cupons, janelas reais e produtos esperados.

## Estrutura canônica do dicionário

Cada linha deve representar uma campanha, influencer ou cluster de criativo suficientemente específico para decisão.

Campos mínimos:

```text
canonical_id
status
influencer_name
influencer_handle
platform
paid_source
meta_campaign_name_patterns
meta_adset_name_patterns
meta_ad_name_patterns
google_campaign_name_patterns
utm_source_expected
utm_medium_expected
utm_campaign_expected
utm_content_expected
coupon_patterns
landing_url_patterns
expected_product_theme
expected_brand
expected_model
expected_skus
expected_size_range
launch_date
end_date
commercial_window
cost_owner
shopify_match_rule
confidence_level
notes
```

## Status possíveis

- `draft`: hipótese inicial ainda sem evidência suficiente.
- `mapped`: padrões de naming/UTM/cupom definidos.
- `validated`: há match razoável entre mídia paga e Shopify/GA4.
- `ambiguous`: existem sinais, mas o mesmo padrão pode capturar campanhas diferentes.
- `deprecated`: campanha antiga mantida apenas para histórico.

## Regras de matching

1. Começar pelo naming pago:
   - Meta: inspecionar `campaign_name`, `adset_name` e `ad_name`, não só um campo.
   - Google: campanha/ad group quando disponível.
2. Cruzar com Shopify apenas por evidência estrita:
   - `utm_campaign` exato ou normalizado quando o padrão for conhecido;
   - cupom do influencer;
   - landing/referrer compatível;
   - produto/SKU/tamanho vendido compatível com o criativo.
3. Evitar matching frouxo por `contains` em campanhas genéricas. Exemplo de risco: `Pareto.Vendas [Masculino]` pode capturar UTMs de Helena/Dia das Mães sem ser a mesma campanha.
4. Separar sempre:
   - `Meta attributed ROAS`;
   - `Google/Metricool attributed performance`;
   - `Shopify evidence revenue`;
   - `operational ROAS` quando houver custo + receita Shopify compatíveis.
5. ROAS operacional só pode ser apresentado como decisão quando houver match entre custo, campanha/influencer, janela comercial e receita Shopify.

## Saída esperada

Relatório read-only com:

1. Campanhas/influencers mapeados.
2. Itens com match Shopify forte.
3. Itens com match ambíguo.
4. Itens sem UTM/cupom/landing confiável.
5. Produtos, marcas, modelos, SKUs e tamanhos vendidos.
6. Consequência de estoque:
   - vendeu estoque livre;
   - gerou ruptura;
   - precisa repor estoque;
   - precisa checar sourcing;
   - não merece ação.
7. Próximas correções de naming/UTM/cupom recomendadas, sempre como preview.

## Aprovação e limites

Livre sem aprovação:

- consultar dados read-only;
- montar dicionário;
- gerar relatório;
- sugerir naming/UTM/cupom futuro;
- sugerir briefing de campanha.

Exige aprovação explícita de Lucas:

- alterar campanha, orçamento, público, criativo ou UTM em Meta/Google;
- publicar campanha ou anúncio;
- enviar Klaviyo/WhatsApp;
- criar cupom real;
- alterar Shopify;
- alterar estoque/preço;
- mandar mensagem para grupo de compras, fornecedor, revendedor ou cliente.

## Template de decisão

```text
Fato: [campanha/influencer/custo/receita Shopify/produto/SKU/tamanho]
Leitura: [o que isso indica]
Confiança: [alta/média/baixa]
Risco: [atribuição ambígua, UTM ausente, cupom compartilhado, janela incompleta]
Consequência de estoque: [sem ação / repor estoque / checar sourcing / preparar campanha]
Recomendação: [ação sugerida]
Aprovação necessária: [sim/não e de quem]
```

## Próximo passo operacional

Preencher a primeira versão do dicionário para Lala Noleto, Silvia Heinz, Helena Lunardelli e campanhas broad/Advantage+/RMKT mais relevantes, usando os relatórios já versionados como base.
