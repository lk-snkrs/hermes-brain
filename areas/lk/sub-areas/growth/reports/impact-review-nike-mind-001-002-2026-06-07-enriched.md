# Revisão de impacto (~7 dias) — Guia Nike Mind 001/002 + coleção Nike Mind 001

Data UTC: 2026-06-07T12:05Z  
Escopo: read-only, sem writes externos.

## Status executivo
- Status geral: OK / monitorar.
- Diagnóstico público: páginas acessíveis em HTTP 200, indexáveis, com conteúdo Nike Mind refeito presente, FAQPage JSON-LD único no guia e coleção com grid/linkagem de produtos.
- Dados autenticados disponíveis: Shopify Admin, GA4 REST, GSC, GMC e DataForSEO foram consultados via Doppler/read-only.
- Decision-grade: parcial. Há GA4/GSC/Shopify/GMC, mas conversão/receita atribuída às páginas no GA4 está zerada no período e o guia ainda tem base pequena; portanto, bom para diagnóstico e monitoramento, ainda fraco para decisão comercial de escala.

## Evidências principais
### Público / técnico
- Guia: 200, final `https://lksneakers.com.br/pages/guia-nike-mind-001-002`, title `Nike Mind 001 e 002: Guia LK de Escolha`, H1 `Nike Mind 001/002: conforto sensorial, design e escolha certa`, 1 FAQPage JSON-LD, 2 blocos JSON-LD, 9 links únicos para produtos, 1 link único para a coleção.
- Coleção: 200, final `https://lksneakers.com.br/collections/nike-mind-001`, title `Nike Mind 001 Original na LK Sneakers`, H1 `Nike Mind 001/002`, 1 FAQPage JSON-LD, 4 blocos JSON-LD, 19 links únicos para produtos, 22 links únicos internos/filtros da coleção.
- Marcadores de conteúdo encontrados nas duas páginas: `Nike Mind 001`, `Nike Mind 002`, `conforto sensorial`, `autenticidade`, `curadoria`, `atendimento`.

### Shopify Admin
- Coleção `nike-mind-001`: OK, título `Nike Mind`, 18 produtos, status consultado em read-only.

### GA4 — 2026-05-31 a 2026-06-06 vs 2026-05-24 a 2026-05-30
- Coleção: 158 sessões vs 141 (+12,1%); 146 usuários vs 137 (+6,6%); 177 views vs 154 (+14,9%).
- Guia: 13 sessões vs 2 (+550%); 10 usuários vs 1 (+900%); 18 views vs 4 (+350%).
- Ecommerce por pagePath: coleção e guia com 0 ecommercePurchases, R$0 purchaseRevenue, R$0 totalRevenue no período atual. Coleção tinha 4 addToCarts no período anterior e 0 no atual; checkout 0 nos dois períodos.

### GSC — 2026-05-28 a 2026-06-04 vs 2026-05-21 a 2026-05-27
- Coleção: 80 cliques vs 43 (+86,0%); 8.792 impressões vs 3.216 (+173,4%); CTR 0,91% vs 1,34% (queda relativa de ~31,9%); posição média 7,65 vs 7,41 (leve piora de 0,24).
- Guia: 3 cliques, 529 impressões, CTR 0,57%, posição média 8,85; período anterior sem linha agregada para a URL.
- Queries do guia já aparecem com posições úteis mas sem clique em várias linhas: `nike mind 001` posição ~11,3 / 14 impressões; `chinelo nike mind 002` posição ~10,5 / 13 impressões; `mind 001 nike` posição ~9,9 / 10 impressões; `nike mind 001 como funciona` posição ~9,8 / 5 impressões.
- Queries da coleção: `mind 001` 18 cliques / 899 impressões / pos. 5,55; `nike mind 001` 6 cliques / 1.039 impressões / pos. 10,46; `nike mind 001 onde comprar` 4 cliques / 98 impressões / pos. 7,34; `tenis nike mind 001` 4 cliques / 130 impressões / pos. 5,08.

### GMC
- Merchant consultado: OK. Amostra de 250 itens retornou 1 match Nike Mind; sem `destinationStatuses`/`itemLevelIssues` reportados no item retornado.

### DataForSEO / SERP
- Keyword `nike mind 001`, Google BR desktop: LK aparece no top 10 com PDP `Chinelo Slide Nike Mind 001 Black Chrome Preto - LK Sneakers` na posição orgânica 9.
- Top SERP dominada por Nike, Instagram, Mercado Livre, JR Tênis, Droper, Farfetch e Dunk; oportunidade é melhorar CTR/snippet e consolidar coleção/guia como páginas de apoio, sem canibalizar PDPs fortes.

## Riscos
- CTR da coleção caiu mesmo com forte ganho de impressões; risco de expansão para termos mais amplos com snippet pouco competitivo.
- Guia ainda tem baixo volume absoluto; evolução percentual é boa, mas não sustenta decisão comercial sozinha.
- Conversão/receita por pagePath no GA4 está zerada; pode ser efeito real ou limitação de atribuição por página. Impacto comercial ainda inconclusivo.
- GSC mostrou URLs com parâmetros de Shopping aparecendo em queries orgânicas; monitorar canônicos/parametrização para evitar dispersão de sinais.
- GMC retornou apenas 1 match na amostra; não é auditoria completa de feed Nike Mind.

## Recomendações
1. Manter guia e coleção publicados: não há regressão técnica pública; sinais iniciais de descoberta orgânica são positivos.
2. Próxima otimização com maior impacto provável: melhorar CTR da coleção para `nike mind 001`, `mind 001 nike` e `onde comprar`, ajustando title/meta/copy acima do grid com linguagem premium e intenção comercial.
3. Fortalecer linkagem contextual guia → coleção → PDPs prioritários e coleção → guia, preservando tom premium e evitando taxonomia operacional pública.
4. Monitorar por mais 7–14 dias antes de declarar impacto comercial, com foco em: GSC CTR/posição por query, GA4 addToCart/checkouts/purchases, e receita assistida por produto.
5. Fazer auditoria GMC completa dos SKUs Nike Mind se a coleção continuar ganhando impressão orgânica/paga, especialmente GTIN/barcode e issues por item.

## Aprovação necessária
- Sem aprovação: continuar monitoramento read-only, novo relatório em 7–14 dias, auditoria GMC/GA4/GSC read-only e preparação de propostas.
- Precisa aprovação explícita de Lucas: qualquer alteração de title/meta, copy visível, schema, theme, feed/GMC, campanhas, Klaviyo/WhatsApp, preço, estoque ou publicação em produção.
