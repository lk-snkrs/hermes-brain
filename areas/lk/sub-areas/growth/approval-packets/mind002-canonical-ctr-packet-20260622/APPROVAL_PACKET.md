# Approval Packet — Nike Mind 002 canonical/CTR — 2026-06-22

**Status:** pronto para aprovação; nenhum write executado.  
**Gerado:** 2026-06-22T20:03:22.110950+00:00  
**values_printed:** false.

## Veredito

O problema de Mind 002 **não é canonical quebrado**. As URLs parametrizadas de Shopping retornam canonical/OG/Product schema para a URL limpa. O gargalo principal é **CTR/posicionamento em queries Mind 002**, com baixa padronização de title/meta em alguns PDPs e sinal ainda fragmentado entre PDPs e guia.

## Evidência verificada

### GSC últimos 28 dias

| Grupo | Cliques | Impressões | CTR | Posição |
|---|---:|---:|---:|---:|
| Queries Mind 002 | 12 | 2.516 | 0,48% | 9,68 |
| PDPs Mind 002 | 14 | 1.972 | 0,71% | 9,60 |
| Hub Mind 001/002 | 128 | 9.107 | 1,41% | 7,43 |

Maior gargalo:

- `nike mind 002` → PDP Black Hyper Crimson: **1.121 impressões / CTR 0,09% / posição 10,6**.

### QA canonical/schema público

- URLs com `currency`, `country`, `variant`, `utm_source`, `utm_medium`, `utm_campaign`, `stkn` retornam canonical limpo.
- `og:url` também aponta para URL limpa.
- Product schema `url` aponta para URL limpa.
- H1 único, Product schema único e FAQPage único nos PDPs amostrados.
- Sem Liquid error.

### Shopify Admin read-only

- 7 PDPs Mind 002 ativos mapeados dentro da collection `nike-mind-001`.
- Admin `descriptionHtml` dos PDPs não tem link explícito para o hub/guia, mas o tema público já insere pelo menos link para guia em páginas amostradas.
- Não usei estoque/availability como critério de decisão.

## Escopo proposto — fase 1

Aplicar somente SEO fields em **4 PDPs Mind 002**, sem tocar body, theme, collection, produto comercial, preço, estoque, ordenação ou checkout.

| Handle | Campo | Atual | Proposto |
|---|---|---|---|
| `tenis-nike-mind-002-black-hyper-crimson-preto` | SEO title | Nike Mind 002 Black Hyper Crimson Original no Brasil \| LK | Tênis Nike Mind 002 Black Hyper Crimson Original \| LK |
| `tenis-nike-mind-002-black-hyper-crimson-preto` | SEO description | Nike Mind 002 Black Hyper Crimson original no Brasil: sneaker escultural Nike Mind com curadoria exclusiva LK, autenticidade e atendimento humano. | Tênis Nike Mind 002 Black Hyper Crimson original: sneaker fechado da linha Nike Mind com design escultural, autenticidade e curadoria LK. |
| `tenis-nike-mind-002-light-khaki-bege` | SEO title | Tênis Nike Mind 002 Light Khaki Bege \| LK Sneakers | Nike Mind 002 Light Khaki Original no Brasil \| LK |
| `tenis-nike-mind-002-light-khaki-bege` | SEO description | Nike Mind 002 Light Khaki Bege original. Design escultural Nike, curadoria LK, atendimento humano e compra segura em até 10x sem juros. | Nike Mind 002 Light Khaki original no Brasil: tênis fechado da linha Mind com design escultural, curadoria LK e atendimento humano. |
| `tenis-nike-mind-002-thunder-blue-azul` | SEO title | Tênis Nike Mind 002 Thunder Blue \| LK Sneakers | Nike Mind 002 Thunder Blue Original no Brasil \| LK |
| `tenis-nike-mind-002-thunder-blue-azul` | SEO description | Nike Mind 002 Thunder Blue original. Modelo lifestyle Nike com design escultural, curadoria LK, compra segura e até 10x sem juros. | Nike Mind 002 Thunder Blue original no Brasil: sneaker fechado Nike Mind com leitura escultural, curadoria LK e atendimento humano. |
| `tenis-nike-mind-002-light-smoke-grey-cinza` | SEO title | Tênis Nike Mind 002 Light Smoke Grey \| LK Sneakers | Nike Mind 002 Light Smoke Grey Original no Brasil \| LK |
| `tenis-nike-mind-002-light-smoke-grey-cinza` | SEO description | Nike Mind 002 Light Smoke Grey original. Design escultural Nike, curadoria LK, atendimento humano e compra segura em até 10x sem juros. | Nike Mind 002 Light Smoke Grey original no Brasil: tênis Nike Mind fechado com design escultural, autenticidade e curadoria LK. |

## Fora do escopo

- Não criar `/collections/nike-mind-002` agora.
- Não alterar product body/descriptionHtml.
- Não alterar custom FAQ/metafields.
- Não mexer em theme/templates/snippets.
- Não mexer em preço, estoque, disponibilidade, ordenação, descontos, GMC/feed, campanhas, Klaviyo/WhatsApp ou checkout.

## Risco

Baixo/médio:

- São alterações de snippet/CTR em SEO fields de PDP.
- Pode levar dias/semanas para Google reprocessar title/meta.
- Black Hyper Crimson já tinha title forte; a mudança torna o snippet mais literal para `tênis nike mind 002` e reduz linguagem menos buscada como “sneaker escultural” no começo.

## Rollback

Antes do write:

1. Backup dos 4 produtos via Shopify Admin read-only.
2. Aplicar ProductUpdate somente nos campos `seo.title` e `seo.description` dos 4 produtos.
3. Readback Admin dos 4 produtos.
4. QA público head/canonical/schema dos 4 PDPs.
5. Rollback script restaura os SEO fields anteriores se houver regressão.

## Review de impacto

D+7 e D+14:

- query `nike mind 002`;
- PDP Black Hyper Crimson;
- PDPs Mind 002 agregados;
- hub Mind 001/002;
- CTR, impressões, posição e cliques.

## Aprovação necessária

> Aprovo aplicar em produção no Shopify somente os SEO fields `seo.title` e `seo.description` dos 4 PDPs Nike Mind 002 listados no packet `mind002-canonical-ctr-packet-20260622`, sem mexer em body/descriptionHtml, theme, templates, snippets, collection, produtos além desses campos, preço, estoque, ordenação, descontos, GMC/feed, campanhas, Klaviyo/WhatsApp ou checkout, com backup, readback, QA público e rollback.
