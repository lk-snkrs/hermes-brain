# LK OS — Data Spine v0.1

Este arquivo resume o contrato de dados canônico do LK Operating System. A rotina detalhada está em `../rotinas/data-spine-readonly-2026-05-11.md`.

## Regra máxima

Nenhum número executivo deve aparecer sem rótulo de fonte.

Use uma destas classes:

- `fact_shopify`: pedido, produto, cliente ou receita confirmados na Shopify.
- `fact_tiny_stock`: estoque livre/reservado/indisponível confirmado no Tiny.
- `fact_ga4`: tráfego, canal, sessão, página ou conversão do GA4.
- `platform_signal`: Meta, Google Ads, Metricool, Klaviyo ou outra plataforma reportando atribuição própria.
- `derived_reconciliation`: cálculo do Hermes cruzando fontes, com regra explícita.
- `manual_approval`: decisão/aprovação humana de Lucas/equipe.
- `unknown`: dado ausente ou não confiável.

## Fonte da verdade por pergunta

- Vendeu? Shopify.
- Quem comprou? Shopify, com PII minimizada.
- Qual produto/variant/SKU foi vendido? Shopify.
- Tem estoque livre? Tiny `LK | CONTROLE ESTOQUE`.
- De onde veio o tráfego? GA4 e Shopify source, reconciliados quando possível.
- Quanto gastou em mídia? Meta/Google/Metricool.
- Qual influencer performou? Meta `ad_name` + ponte Shopify/UTM/cupom quando houver.
- Qual campanha de e-mail existe/está em draft? Klaviyo.
- Quem pode receber WhatsApp de concierge? Compra âncora POS/LK Flagship + aprovação + validação Evolution.
- Qual ação foi aprovada? Brain/local SQL/Notion conforme tipo de ação.

## Campos proibidos em relatórios públicos/Telegram

- email completo;
- telefone completo;
- endereço;
- documento;
- token/secret;
- payload completo de API;
- listas brutas de clientes.

## Status de ação recomendado

- `needs_data`: falta dado confiável.
- `needs_preview`: dado existe, falta artefato de revisão.
- `approved`: Lucas aprovou a ação específica.
- `rejected`: Lucas recusou.
- `held`: manter pendente, sem executar.
- `executed`: ação feita e verificada.
- `blocked`: depende de credencial, fonte, estoque, permissão ou decisão.

## Regra de linguagem executiva

Relatórios do LK OS devem separar sempre:

1. fato;
2. leitura;
3. recomendação;
4. risco/confiança;
5. aprovação necessária.
