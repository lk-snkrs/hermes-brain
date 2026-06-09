# LK Growth — D+7 impact & QA review — coleções/guias publicados em 2026-06-01

Gerado em 2026-06-08. Read-only; sem writes em Shopify/theme/GMC/ads/Klaviyo/canais externos.

## Status executivo
- **Principal achado:** as 3 coleções estão públicas com HTTP 200, title/meta/canonical e imagens de produto; porém os 3 guias dedicados `/pages/guia-*` estão **404** e não existem no Shopify Admin por handle.
- **Impacto:** há sinais direcionais de tráfego em GA4/GSC, mas o review fica **não decision-grade para impacto comercial** porque as páginas-guia não estão live e pedidos/receita atribuídos por landing page retornaram 0 no Shopify/GA4 para o período.
- **Risco imediato:** CTAs/links para guias nas coleções não aparecem; FAQPage JSON-LD e tabelas dos guias não estão disponíveis publicamente; a camada GEO/AI Search prometida pelos guias não está ativa.

## Evidência por URL
| Grupo | Coleção pública | Guia dedicado | QA público |
|---|---:|---:|---|
| Nike Vomero Premium | 200 | 404 | Coleção com H1, canonical, CollectionPage JSON-LD e 42 imagens de produto. Guia ausente: sem root guide classes, sem FAQPage JSON-LD, sem tabela. Sem link/CTA visível para o guia na coleção. |
| Adidas x Bad Bunny | 200 | 404 | Coleção com H1, canonical, CollectionPage JSON-LD e 36 imagens de produto. Guia ausente: sem root guide classes, sem FAQPage JSON-LD, sem tabela. Sem link/CTA visível para o guia na coleção. |
| Adidas SL 72 | 200 | 404 | Coleção com H1, canonical, CollectionPage JSON-LD e 37 imagens de produto. Guia ausente: sem root guide classes, sem FAQPage JSON-LD, sem tabela. Sem link/CTA visível para o guia na coleção. |

## Dados autenticados direcionais
- **GA4 2026-06-01 a 2026-06-07 vs 2026-05-25 a 2026-05-31**
  - Nike Vomero Premium coleção: 71 sessões vs 45; guia: 1 sessão vs 0; add-to-cart/checkout/purchase/revenue na dimensão pagePath: 0.
  - Adidas x Bad Bunny coleção: 18 sessões vs 34; guia: 0 vs 0; add-to-cart/checkout/purchase/revenue: 0.
  - Adidas SL 72 coleção: 18 sessões vs 16; guia: 0 vs 0; add-to-cart/checkout/purchase/revenue: 0.
- **GSC 2026-05-29 a 2026-06-05 vs 2026-05-22 a 2026-05-28**
  - Nike Vomero Premium coleção: 5 cliques / 550 impressões / posição média ~9,6 vs 3 / 342 / ~12,3.
  - Adidas x Bad Bunny coleção: 12 cliques / 1.035 impressões / posição média ~8,5 vs 10 / 671 / ~8,0.
  - Adidas SL 72 coleção: 0 cliques / 24 impressões / posição média ~6,5 vs 0 / 14 / ~8,7.
  - Guias: 0 linhas em GSC nos 3 casos.
- **Shopify Admin:** coleções encontradas; produtos ativos: Nike 20, Bad Bunny 17, SL 72 18. Pages por handles `guia-*`: não encontradas. Pedidos escaneados Shopify: 77 atuais e 97 anteriores; landing first/last visit dos 6 paths: 0 pedidos / R$0.
- **GMC:** acesso OK; matches amostrais: Nike 4, Bad Bunny 13, SL 72 6; sem item-level issues no sample retornado.
- **DataForSEO/SERP:** acesso OK. LK não apareceu no top 10 orgânico para as queries principais; existe presença de blog LK no top 10 para “adidas x bad bunny”.

## Issues
1. **Crítico:** guias dedicados 404 e ausentes no Admin; isso quebra SEO/GEO/FAQ/table e qualquer CTA esperado.
2. **Crítico:** CTA/link de coleção → guia não visível nas 3 coleções.
3. **SEO:** title de Adidas x Bad Bunny no Admin parece concatenado: `Adidas x Bad Bunny | Collab Exclusiva | LK SneakersAdidas x Bad Bunny - LK`.
4. **Copy operacional antiga:** não apareceu nas coleções Nike; nas coleções Adidas há termos `estoque/fora de estoque` no HTML, provavelmente de labels/estado de produto; nos 404 dos guias aparece meta global antiga com `Envio imediato`, por causa do template 404.
5. **Público/browser:** browser recebeu 503 anti-bot, mas fetch público com User-Agent normal confirmou coleções 200 e guias 404. Isso não parece indisponibilidade real para usuário comum, mas deve ser observado.

## Próxima ação recomendada
- **Pedir aprovação explícita de Lucas para correção em produção**: publicar/republicar as 3 pages de guia com template padrão, FAQPage JSON-LD, tabela e imagens; adicionar/validar CTA das coleções para os guias; corrigir title/meta de Bad Bunny; remover/neutralizar copy operacional antiga onde estiver visível.
- Executar primeiro em preview/dev theme quando houver alteração de theme; depois de aprovado, publicar em produção com rollback snapshot e novo QA imediato + nova revisão D+7.

Artefatos salvos em `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/impact/2026-06-08-d7-collections-guides/`.
