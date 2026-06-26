# SEMrush Ideas — Execution status LK

Data UTC: 2026-06-26T09:30:35Z

## Executado

1. **Shopify x GA4 Salomon XT-6 reconciliado**
   - Shopify: 2 pedidos pagos Salomon XT-6 encontrados, ambos com sinais Google/paid.
   - GA4 item-level: 2 itemsPurchased e R$ 4.799,98 itemRevenue.
   - Conclusão: o sinal comercial está confirmado.

2. **SEMrush XLSX lido e classificado**
   - 78 ideias.
   - Grupos: bounce/time, internal links, schema/rating, cannibalization, backlinks.

3. **Internal links executado em produção/dev**
   - Adicionado hub server-rendered no footer para reforçar links internos comerciais.
   - Links: Salomon XT-6, NB 204L, Onitsuka Mexico 66, Onitsuka todos, Nike Mind 001/002, Vomero Premium, Nike x Jacquemus, Nike Dunk, Dunk SB e Nike Panda.
   - Readback: presente em PDP Nike Panda e collection Nike Dunk SB; alguns shards/home/collection ainda em cache.

4. **Schema/reviews validado**
   - Judge.me/`jdgm` presente.
   - AggregateRating já aparece no HTML em páginas testadas.
   - Nenhum rating falso foi criado.

5. **GMC/Merchant read-only executado**
   - Catálogo lido: 21.673 produtos/status.
   - Issue relevante para Salomon: `image_link_internal_error` em variantes Cloudburst `L49154600`.
   - Mitigação já feita antes: arquivos de imagem antigos do Guia foram restaurados no Shopify Files e retornam HTTP 200. Próximo ciclo GMC deve confirmar se issue cai.

## Não executado por guardrail

- Nenhum outreach/backlink externo enviado.
- Nenhuma campanha Google/Meta criada/alterada.
- Nenhum schema AggregateRating inventado.
- Nenhuma consulta de estoque/disponibilidade.

## Próximos checks

- Revalidar cache público do footer hub em home/Salomon em algumas horas.
- Reexecutar GMC para confirmar queda de `image_link_internal_error` em Cloudburst.
- Impact review D+7: GSC/GA4/SERP para Salomon XT-6 e páginas linkadas.

Reminder OS loop needed: yes
Reminder OS owner: lk-growth
Reminder OS next action: revalidar cache público e GMC Cloudburst image issue no próximo ciclo.
Reminder OS review trigger: 24h ou D+7 após execução.
Reminder OS evidence: receipts em `areas/lk/sub-areas/growth/receipts/semrush-ideas-20260626/` e report SEMrush reconciliation.
