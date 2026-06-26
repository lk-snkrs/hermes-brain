# LK Growth — gate read-only de impact review antes de novos writes

- Data: 2026-06-12
- Decisão: Mesa COO 2026-06-12, Decisão 3/3, aprovada por Lucas com “Fazer”.
- Dono: `[LK] Growth OS` / profile `lk-growth`; Hermes Geral apenas governa, registra handoff e roteia.
- Natureza: regra operacional read-only / preview-first.

## Regra

Antes de qualquer novo write Growth relacionado a uma mudança já executada — Shopify SEO fields, `product.descriptionHtml`, collection/page copy, tema/CRO, GMC/feed, schema, Klaviyo/CRM, Ads ou surface pública — LK Growth deve tratar o impact review existente como **gate obrigatório**.

O gate precisa responder, em modo read-only:

1. Qual mudança está sendo avaliada e quando foi aplicada.
2. Quais URLs/handles/produtos/coleções foram afetados.
3. Quais fontes foram consultadas e a janela de dados.
4. O que melhorou, piorou, ficou neutro ou segue inconclusivo.
5. Quais confounders podem explicar o sinal: sazonalidade, campanhas, influencer/social, Klaviyo, estoque, demanda externa, indexação, cache ou instrumentação.
6. Qual próximo passo é seguro: manter, medir de novo, investigar, reverter via packet, ou criar novo approval packet.

## Fontes mínimas

Quando disponíveis, o review deve usar:

- GA4: sessões, usuários, views, conversão/funil e receita por landing/PDP/collection.
- Shopify read-only: objeto afetado, estado atual, products count, Admin/readback e, quando aplicável, vendas/revenue por produto/coleção.
- GSC: cliques, impressões, CTR, posição e queries/páginas afetadas.
- GMC/Merchant: somente quando o write/hipótese toca product data, Shopping visibility ou feed.
- Klaviyo/CRM/Paid/Influencer: apenas como `platform_signal` ou confounder, não como verdade de lift orgânico.
- Público/QA: HTTP 200, title/meta/canonical, schema/JSON-LD, PageSpeed/CrUX quando material.

Se uma fonte estiver ausente ou parcial, marcar explicitamente como `não decision-grade` para aquela dimensão.

## Bloqueio de writes

Este gate **não autoriza**:

- Shopify product/collection/page/theme writes;
- SEO title/meta/schema/description writes;
- GMC/feed/ProductInput/fetch writes;
- Klaviyo, WhatsApp, e-mail ou campanhas;
- preço, estoque, SKU, desconto, checkout;
- cron/runtime/infra changes.

Qualquer ação produtiva posterior exige novo approval packet atual, com escopo exato, rollback, readback e verificação.

## Aplicação imediata — product description operational cleanup

A limpeza ampla de descrições de PDP executada em 2026-06-05 passa a ser o caso canônico inicial deste gate.

- Escopo: `product.descriptionHtml` / REST `body_html` de 2.331 PDPs; remoção de termos operacionais indevidos; preservação de mensagens corretas de encomenda.
- QA técnico final: termos problemáticos zerados; frase neutra nova presente em 2.233 produtos.
- Relatório de review/ledger: `reports/lk-experiment-ledger-2026-06-12.md`.
- Review específico: `reviews/impact-review-product-description-operational-cleanup-20260612.md`.
- Veredito atual: QA técnico concluído; impacto comercial ainda inconclusivo para PDPs pela amplitude da mudança e necessidade de corte por PDP/coleção.

## Leitura do review de 2026-06-12

Sinais já registrados no ledger da semana:

- Onitsuka Tiger: melhorou; GSC clicks +21,7%, impressions +5,5%, GA4 sessions +4,9%; confiança média-alta.
- New Balance 204L: neutro positivo; GSC impressions +18,0%, clicks -3,7%, GA4 users +3,8%; sugere oportunidade de CTR, não regressão técnica.
- Nike Mind: inconclusivo; coleção caiu, mas o guia ganhou impressões e cliques iniciais; medir D+7/D+14 antes de mexer.
- PDP description cleanup: QA técnico concluído; impacto comercial ainda não atribuído; precisa corte por PDP/coleção antes de qualquer nova edição ampla.

## Próximo bloco permitido sem nova aprovação

Sem nova aprovação, LK Growth pode apenas:

1. Preparar briefing/packet read-only para Onitsuka e 204L.
2. Fazer DataForSEO/SERP/AI visibility read-only quando útil.
3. Repetir medição Nike Mind em D+7/D+14.
4. Investigar Klaviyo instrumentation QA em modo read-only.

Tudo que publicar, editar, enviar, alterar feed, mexer em tema ou tocar campanhas exige aprovação separada.

## Non-actions desta decisão

- `external_writes=0`.
- Não alterado: Shopify, tema, product descriptions, SEO fields, GMC/feed, Klaviyo, Ads, WhatsApp/e-mail, preço, estoque, Tiny, cron/runtime, secrets.
- Valores de secrets não impressos (`values_printed=false`).
