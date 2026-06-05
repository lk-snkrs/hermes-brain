# Simulation Source — LK Growth Weekly Command Center 2026-06-01

Source: `/opt/data/profiles/lk-growth/cron/output/738d3deabaeb/2026-06-01_13-08-15.md`
Mode: extracted final actionable section for local/read-only simulation.

---

## SERP / demanda viva

### New Balance 204L

- Volume Brasil: 9.900.
- Competição: alta.
- Intent: transactional.
- Tendência anual reportada: +404.900%.
- SERP mobile dominada por New Balance oficial.
- LK aparece em Popular Products como seller para NB 204L Mushroom.

**Leitura:** LK tem presença comercial/merchant card, mas precisa ganhar autoridade textual com coleção/source page para termos como “onde comprar”, “original”, “feminino”, “bege”.

### Onitsuka Tiger Mexico 66

- Volume Brasil: 6.600.
- Intent: transactional.
- LK rankeia #1 orgânico para `onitsuka tiger mexico 66 original brasil`.
- PAA inclui “Onde comprar Onitsuka Tiger original no Brasil?” e dúvidas de autenticidade/diferença Asics vs Onitsuka.

**Leitura:** essa página já é ativo vencedor. Deve ser protegida e melhorada com cuidado, sem reescrita agressiva.

---

## 18 tópicos — cobertura

| Tópico | Status | Observação |
|---|---:|---|
| GA4 | Parcial verificado | GA4 LK OK; relatórios PDP/coleções usam GA4. Funil completo não reextraído. |
| GSC | Parcial/pendente | Não houve extração live nesta execução. CTR/query por URL não decision-grade. |
| GMC | Verificado | Relatório 2026-05-31 com 21.338 products/statuses. |
| Shopify SEO | Parcial verificado | PDPs/coleções lidos read-only; nenhum write. |
| Shopify CRO/theme | Parcial | Auditoria mobile/visual pública; sem dev/prod write. |
| GEO/AI Search | Parcial | `llms.txt` OK; SERP DataForSEO; sem ChatGPT/Perplexity live. |
| PageSpeed/CrUX/CWV | Parcial | Lighthouse bom; PageSpeed timeout; CrUX 404. |
| Schema | Parcial | PDP forte; coleções com FAQ sem FAQPage. |
| Reviews/prova social | Parcial | PDP exemplo OK; Judge.me catálogo não rechecado. |
| Paid media | Parcial verificado | Meta Ads direto OK; Metricool falhou/parcial. |
| Influencer/social demand | Parcial | Sinais SERP/social; FHITS não reconsultado. |
| Concorrência/SERP | Parcial verificado | SERP para 204L e Onitsuka. |
| Google Business/local | Pendente/parcial | Local inventory GMC sim; GBP não auditado. |
| Klaviyo/CRM | Pendente | Não reconsultado. |
| Catálogo/product data quality | Verificado | GMC + Shopify/PDP reports. |
| Conteúdo/taxonomia comercial | Parcial | Coleções/PDPs priorizados; menu/taxonomia completa não auditada ponta a ponta. |
| Mensuração/QA eventos | Parcial | Meta/GA4 OK parcialmente; tracking precisa reconciliação. |
| Impact review/experimentação | Parcial/pendente | Packets precisam D+7/D+14 quando aprovados. |

---

## Pacotes de decisão sugeridos

1. **Packet A — PDP Top 5 CRO/SEO preview**  
   Title/meta, decisão mobile, FAQ, schema/alt.  
   Não autoriza Shopify/theme write.

2. **Packet B — 3 coleções GEO/FAQPage preview**  
   New Balance, Lançamentos, Air Jordan ou Lululemon.  
   Não autoriza publicação.

3. **Packet C — GMC local `link_template` investigation**  
   Read-only primeiro; nenhum ProductInput/feed/fetchNow.

4. **Packet D — Paid landing reconciliation**  
   Meta Ads → landing/PDP/coleção → GA4/Shopify.  
   Não autoriza campanha/budget.

5. **Packet E — Semântica global low-risk em dev**  
   OG home, H1 cart, parser HTML, alt prioritário.  
   Dev/produção só com aprovação.

---

## Próximos passos seguros

1. Preparar Packet A dos 5 PDPs prioritários.
2. Preparar Packet B para 3 coleções.
3. Rodar investigação read-only do GMC `link_template`.
4. Reconciliar Meta Ads com Shopify/GA4.
5. Revalidar PageSpeed/CrUX em execução separada.

## O que não fiz

- Não alterei Shopify.
- Não alterei GMC/feed.
- Não alterei tema/dev/prod.
- Não alterei Ads, orçamento ou campanhas.
- Não mexi em preço, estoque, checkout, Klaviyo, WhatsApp ou e-mail.
- Não publiquei copy, FAQ, schema ou SEO fields.
