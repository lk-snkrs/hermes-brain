# LK Growth Ops — triagem diária de receita e fontes

Gerado em: 2026-05-10T21:27:01.546141-03:00 BRT (2026-05-11T00:27:01.546141+00:00 UTC)
Janela: dia em andamento — 2026-05-10T00:00:00-03:00 até 2026-05-10T21:27:01.546141-03:00.
Modo: somente leitura; nenhum write externo; sem PII.

## Resumo executivo
- Shopify, fonte de verdade de venda: 4 pedidos válidos / 4 pagos ou em fluxo pago, R$ 22.009,97 em current_total_price. Houve 1 pedido cancelado/desconsiderado.
- GA4 property 348553567: 2,200 sessões, 3 compras, R$ 19.729,97, conversão 0,14%.
- Reconciliação Shopify x GA4: GA4 está R$ 2.280,00 abaixo do Shopify (10,36%) e 1 compra abaixo no corte.
- Mídia paga: Meta direto R$ 1.381,99 spend / 4 compras atribuídas / R$ 22.209,97 valor atribuído; Google via Metricool R$ 648,88 spend / 1 conversão / R$ 2.799,99 atribuído.
- ROAS operacional contra venda Shopify não deduplicada por canal: receita Shopify ÷ spend Meta+Google = 10.84x; usar como termômetro, não como ROAS oficial por canal.

## Fontes declaradas
- Venda/pedidos: Shopify Admin API, pedidos por created_at na janela BRT, cancelados excluídos, sem dados de cliente.
- Sessões/canais/CRO: GA4 Data API, property LK 348553567.
- Google Ads: Metricool LK userId 4792967 / blogId 6217010, endpoint v2/advertising/campaigns?providers[]=adwords; analytics do mesmo dia retornou vazio, então foi usado fallback read-only de advertising/campaigns.
- Meta Ads: Meta Graph API direto, conta act_1242062509867163, nível campanha, janela 7d_click/1d_view.
- Nota: valores de Meta/Google são atribuídos por plataforma e podem se sobrepor; Shopify continua sendo receita real/source truth.

## Canais GA4
- Paid Social: 1,191 sessões, 2 compras, R$ 17.129,98
- Organic Search: 219 sessões, 0 compras, R$ 0,00
- Paid Shopping: 219 sessões, 0 compras, R$ 0,00
- Cross-network: 195 sessões, 0 compras, R$ 0,00
- Direct: 145 sessões, 1 compras, R$ 2.599,99
- Organic Social: 85 sessões, 0 compras, R$ 0,00
- Paid Search: 81 sessões, 0 compras, R$ 0,00
- Unassigned: 45 sessões, 0 compras, R$ 0,00

## Source / medium GA4
- facebook / paid: 735 sessões, 2 compras, R$ 17.129,98
- google / cpc: 486 sessões, 0 compras, R$ 0,00
- facebook / cpc: 341 sessões, 0 compras, R$ 0,00
- google / organic: 229 sessões, 0 compras, R$ 0,00
- (direct) / (none): 145 sessões, 1 compras, R$ 2.599,99
- tiktok / paid: 99 sessões, 0 compras, R$ 0,00
- l.instagram.com / referral: 77 sessões, 0 compras, R$ 0,00
- (not set): 35 sessões, 0 compras, R$ 0,00

## Meta Ads — campanhas com valor atribuído
- Pareto.lancamento.Jacquemus: spend R$ 316,33, compras 2, valor atribuído R$ 17.129,98, ROAS 54.15x
- [PD][FUNDO] ADV+ (antiga Simples | Vendas Advantage+): spend R$ 388,86, compras 1, valor atribuído R$ 2.799,99, ROAS 7.20x
- [PD] [FUNDO] RMKT (antiga Campanha Simples | Vendas ): spend R$ 179,68, compras 1, valor atribuído R$ 2.280,00, ROAS 12.69x

## Google Ads via Metricool — campanhas principais
- Pareto.Shopping: spend R$ 95,82, conversões 1, valor atribuído R$ 2.799,99, ROAS 29.22x
- [PD] Brasil | Search - Marca: spend R$ 278,06, conversões 0, valor atribuído R$ 0,00, ROAS 0.00x
- [PD][FUNDO] | Performance Max | Todos os Tênis: spend R$ 14,78, conversões 0, valor atribuído R$ 0,00, ROAS 0.00x
- [PD] [MEIO] | Demand Gen | Tráfego: spend R$ 42,90, conversões 0, valor atribuído R$ 0,00, ROAS 0.00x
- [PD][FUNDO] Pmax | Search DSA: spend R$ 59,22, conversões 0, valor atribuído R$ 0,00, ROAS 0.00x

## Produtos/SKUs vendidos na janela (sem PII)
- 1x 1183C102751-4 | Tênis Onitsuka Tiger Mexico 66 Kill Bill Amarelo
- 1x U9060WHT-4 | Tênis New Balance 9060 Sea Salt Moonbeam Branco
- 1x HV8547-601-37 | Tênis Nike Moon Shoe SP Jacquemus Pale Pink Rosa
- 1x 1183C529.101-8 | Tênis Onitsuka Tiger Tsunahiki Slip-On White/Black Branco
- 1x HQ4307-003-10 | Chinelo Slide Nike Mind 001 Light Smoke Grey Cinza
- 1x HV8547-001-7 | Tênis Nike Moon Shoe SP Jacquemus Off Noir Preto

## Diagnóstico
- A venda do dia está concentrada em web/Shopify; GA4 capturou 3 das 4 compras válidas até o corte. O gap é materialmente explicado por 1 compra de aproximadamente R$ 2.280,00 ainda sem match no GA4.
- Paid Social aparece como principal canal de receita no GA4 (2 compras / R$ 17.129,98) e Meta Ads atribui 4 compras / R$ 22.209,97; isso sugere forte peso de Meta, mas há sobreposição e diferença de janelas de atribuição.
- Google teve tráfego relevante no GA4 (google / cpc com 486 sessões) e spend Metricool de R$ 648,88, mas só 1 conversão atribuída em Pareto.Shopping no painel Metricool.
- Não inferi produto por campaign_id/adset_id; produtos listados vieram apenas de SKU/line_items do Shopify.

## Próximo passo registrado
1. Reexecutar a reconciliação amanhã cedo para a data fechada 2026-05-10: o GA4/Metricool podem atrasar no mesmo dia.
2. Se o gap Shopify x GA4 persistir, investigar tecnicamente o evento purchase ausente sem exportar PII: comparar apenas timestamp, valor e source/medium mascarado.
3. Para decisão de tráfego de hoje: manter leitura conservadora — Meta forte em venda atribuída; Google gerando tráfego e 1 compra, mas abaixo de Meta no corte.
