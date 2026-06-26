# Approval Packet Refresh — Onitsuka Tiger CTR/GEO — 2026-06-22

**Status:** approval-ready, mas recomendo execução cuidadosa; nenhum write feito agora.  
**Gerado:** 2026-06-22T17:50:07.989491+00:00  
**Fonte:** packets de 2026-06-08/17, Ranking Command Center 2026-06-22, DataForSEO, QA público.  
**values_printed:** false.

## Veredito

Onitsuka é a maior frente comercial/SEO do próximo bloco, mas já foi trabalhada antes. Não é caso de reescrever theme/visual; é ajuste fino de **title/meta/descriptionHtml** da collection broad `/collections/onitsuka-tiger-todos-os-modelos` para CTR e intenção `original / Brasil / Mexico 66`.

## Evidência

- Ranking Command Center: collection todos modelos com 30.932 impressões para `onitsuka tiger`, CTR 0,36%, posição 7,9; receita combinada alta.
- Packet 2026-06-17: GSC 861 cliques / 66.479 impressões / CTR 1,30% / posição 6,8; query principal CTR 0,35% / posição 8,2.
- DataForSEO: `onitsuka tiger` 33.100 buscas/mês, transacional; `onitsuka tiger mexico 66` 8.100 buscas/mês, transacional.
- QA público atual: collection HTTP 200, H1 único, conteúdo rico, mas fetch público mostra **dois blocos “Guia editorial LK”**/citáveis. Antes de write, validar se isso é intencional ou duplicação residual.

## Mudança já proposta no packet existente

Packet base: `approval-packets/onitsuka-tiger-improvement-20260617/APPROVAL-PACKET.md`

Escopo: somente:

1. `seo.title`
2. `seo.description`
3. `descriptionHtml`

Não mexer em theme, produtos, preço, estoque, feed/GMC, campanhas, Klaviyo/WhatsApp, desconto ou checkout.

## Minha recomendação agora

Antes de aplicar o packet 2026-06-17, fazer **QA read-only de duplicidade Onitsuka**:

- contar `FAQPage`, `Guia editorial LK`, H1 e blocos citáveis na broad collection e Mexico 66;
- confirmar se a duplicação vem de descriptionHtml + theme, como aconteceu em Mind/Vomero;
- se estiver duplicado, preparar cleanup primeiro em DEV/preview, não aplicar descriptionHtml direto.

## Aprovação para executar depois

Se QA confirmar que não há duplicação crítica, usar aprovação escopada do packet 2026-06-17. Se houver duplicação, abrir sub-packet de cleanup semelhante ao Mind/Vomero.
