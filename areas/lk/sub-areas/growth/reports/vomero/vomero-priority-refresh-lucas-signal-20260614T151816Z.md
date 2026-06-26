# Vomero Premium — priority refresh after Lucas signal

Generated UTC: 2026-06-14 15:18:16 UTC  
Owner: LK Growth  
Status: read-only / decision packet. No external write executed.

## Trigger
Lucas sinalizou por voz que a LK provavelmente vem girando mais de **Vomero Premium** do que de **Samba Jane** ou **Terrada**. Growth deve corrigir priorização e seguir com Vomero acima dessas frentes até prova contrária por dados autenticados.

## Evidence collected now

### Public demand / SERP
- DataForSEO Keyword Overview, Brazil/pt: `nike vomero premium` = **22.200 buscas/mês**, competição HIGH, intenção transacional; pico recente: **49.500/mês** em 2026-03 e 2026-04.
- AI search volume: `vomero premium` = **19/mês**, `nike vomero premium` = **10/mês**, ambos com tendência crescente no histórico disponível.
- Google mobile SERP for `Nike Vomero Premium`:
  - Nike oficial aparece em #1 orgânico.
  - Popular Products inclui LK Sneakers Apparels com múltiplos SKUs Vomero Premium.
  - PAA mostra perguntas de intenção consultiva: o que é, serve para corrida, diferença Plus/Premium.
- Google mobile SERP for `LK Sneakers Vomero Premium`:
  - Popular Products abre com SKUs LK.
  - LK aparece com homepage e guia `Nike Vomero Premium | Guia LK`.
  - Google reviews: LK 4.9 / 412 avaliações no painel local.

### LK public assets verified
- Collection: `https://lksneakers.com.br/collections/nike-vomero-premium`
  - Fetch OK.
  - Copy atual forte para curadoria: amortecimento máximo, ZoomX, Air Zoom, super trainer, lifestyle premium.
  - FAQ presente, mas primeira resposta menciona `Vomero 5` dentro da coleção `Vomero Premium`, risco de confusão de intenção.
  - Collection exibe 20 itens no fetch público; reports anteriores tinham meta com `15 modelos`, risco de contagem envelhecida no snippet.
- Guide: `https://lksneakers.com.br/pages/nike-vomero-premium-guia`
  - Fetch OK.
  - Conteúdo editorial bom para GEO/AI Search: Vogue, Highsnobiety, Nike Newsroom, bloco citável, FAQ textual.
  - Auditoria anterior indicava falta de FAQPage schema no guia; existe draft JSON-LD no Brain.
- PDP sample: `tenis-nike-vomero-premium-black-volt-preto`
  - Fetch OK.
  - Copy técnica/comercial boa, mas ainda contém termos operacionais como `sob encomenda` em FAQ/prazo; isso depende de handoff `lk-stock`, não deve ser alterado por Growth sozinho.

### Revenue-informed context already in Brain
Source: `reports/ranking-goals/revenue-informed-priority-clusters-20260613.md` — Shopify Admin read-only orders last 90d, values_printed=false.
- Top product list inclui `Tênis Nike Vomero Premium Sail Coconut Milk Branco`: **R$ 26.999,94**, qty 6, orders 6.
- Top product list inclui `Tênis Adidas Samba Jane White Black Branco`: **R$ 11.099,99**, orders 2.
- Atenção: o ranking agrupado atual agrega Nike/Jordan/Travis e Adidas Samba/Jane; ainda não isola o cluster Vomero inteiro. Portanto a conclusão comercial completa precisa de extração por handle/modelo.


### Shopify read-only validation executed after refresh
Source: `reports/vomero/vomero-vs-samba-terrada-shopify-readonly-20260614T151816Z.json` — Shopify Admin GraphQL read-only, `created_at:>=2026-03-16`, orders_considered=1210, pages=5, values_printed=false.

Cluster results:
- `vomero_premium`: **R$ 173.999,60**, qty 40, orders 31.
- `samba_jane`: **R$ 15.998,91**, qty 10, orders 9.
- `samba_jjjjound`: **R$ 0,00**, qty 0, orders 0.
- `terrada_terrace_terrex`: **R$ 0,00**, qty 0, orders 0, by title/handle regex used.

Top Vomero products in sample:
- Nike Vomero Premium Black Volt Preto: R$ 31.499,93, qty 7, orders 6.
- Nike Vomero Premium Sail Coconut Milk Branco: R$ 31.499,93, qty 7, orders 7.
- Nike Vomero Premium Flat Stout Marrom: R$ 25.999,94, qty 6, orders 6.
- Nike Vomero Premium Barely Volt Verde: R$ 15.999,96, qty 4, orders 4.
- Nike Vomero Premium White Bright Crimson Branco: R$ 15.999,96, qty 4, orders 4.

Interpretation: Lucas signal is confirmed by Shopify order data in the read-only sample. Vomero Premium materially outperforms Samba Jane and the queried Samba JJJJound/Terrada terms in revenue and orders for the last 90d window.

## Updated priority decision

**Decision:** Promover **Nike Vomero Premium** para a próxima frente prioritária de Growth, acima de Samba Jane/Terrada. A validação read-only de Shopify confirma a hipótese comercial no recorte dos últimos 90 dias.

Próxima execução recomendada: **approval packet para produção** com ajustes de collection/guia/PDPs, snapshot e rollback. Antes de write final, completar GA4/GSC/GMC para estimar impacto e risco de tráfego/conversão.

## Recommended actions

### P0 — Read-only validation, sem aprovação externa
- Shopify read-only: concluído para últimos 90d por handles/títulos contendo `vomero premium`, `samba jane`, `samba jjjjound`, `terrada/terrex/terrace`.
- GA4/GSC read-only: sessões, receita, conversão, impressões, cliques, CTR e posição por collection/guide/PDPs.
- GMC read-only: checar reprovações/warnings e divergência de preço/cor dos SKUs Vomero Premium.
- SERP/GEO: consolidar queries PAA e oportunidades de snippets para coleção e guia.

### P1 — Quick wins propostos, exigem approval antes de produção
- Collection SEO meta: remover contagem dinâmica envelhecida (`15 modelos`) e reforçar `Original`, `ZoomX`, `Air Zoom`, `curadoria LK`, `atendimento humano`.
- Collection FAQ: corrigir resposta que mistura `Vomero 5` com `Vomero Premium`; manter o hub transacional focado em Premium.
- Guia: publicar/ativar FAQPage JSON-LD já draftado, se template permitir, após QA.
- PDPs prioritários: padronizar metas curtas sem preço no title, revisar cor/slug e remover termos operacionais apenas depois de validação/handoff `lk-stock`.
- Internal links: guia -> collection; PDPs -> guia/collection; blog -> collection no primeiro terço.

## Risks / guardrails
- Não falar publicamente em pronta entrega/estoque/encomenda como taxonomia comercial. Termos operacionais dependem de `lk-stock`.
- Não alterar Shopify production sem aprovação explícita atual de Lucas.
- Competição de preço é agressiva; LK deve defender premium por autenticidade, curadoria, atendimento humano, Jardins/SP e segurança — não por preço.

## 18-topic checkpoint
- GA4: not collected in this refresh; needed before production write to estimate traffic/conversion impact.
- GSC: not collected in this refresh; needed for decision-grade.
- GMC: not collected now; prior notes show possible price/data quality history for Vomero.
- Shopify SEO: public collection/guide/PDP checked; Shopify orders read-only validated commercial priority.
- Shopify CRO: public content checked; mobile UX not fully audited now.
- GEO/AI Search: demand and guide citability checked.
- PageSpeed/CrUX/CWV: not collected now.
- Schema: prior audit + current guide reviewed; FAQPage gap on guide remains candidate.
- Reviews/proof: Google local reviews observed in SERP, product ratings observed in SERP.
- Paid media: not collected now.
- Influencer/social demand: SERP short videos indicate social/video demand; not deeply audited.
- Concorrência/SERP: checked for `Nike Vomero Premium` and `LK Sneakers Vomero Premium`.
- Google Business/local: LK panel/reviews observed in SERP.
- Klaviyo/CRM signals: not collected now.
- Catálogo/product data quality: collection count mismatch and color/slug issues flagged from prior packet.
- Conteúdo/taxonomia comercial: collection/guide/blog/PDP cluster active; needs alignment.
- Mensuração/QA eventos: not collected now.
- Impact review/experimentation: required after any approved production write.

## Next approval needed
Approval is NOT needed for read-only validation. Approval will be needed before any Shopify SEO/content/theme production write.
