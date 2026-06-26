# Approval Packet — continuar SEMrush após Taekwondo/Tokyo/Speedcat

Data: 20260626T004746Z
Status: read-only concluído; nenhum write novo executado neste packet.

## O que já está em medição

- Adidas Taekwondo: SEO title/meta production + guia/FAQ/schema em DEV.
- Adidas Tokyo: schema-only production.
- Puma Speedcat: schema-only production.

## Próximos 3 recomendados

### 1) Adidas Sambae — correção urgente + higiene SEO/CRO

URL: `/collections/adidas-sambae`
Collection id: `430079344862`
Produtos Admin: 12 / público: 10
Demanda: `adidas sambae` ~246.000 buscas/mês BR.

Readback público:
- HTTP 200;
- title atual: `Adidas Sambae - LK Sneakers`;
- FAQPage: 0;
- **Liquid error público:** `Could not find asset snippets/lk-sambae-204l-guide.liquid`;
- Admin marcou description com termo operacional antigo/ruído (`has_forbidden=true`).

Recomendação:
- corrigir o Liquid error sem mexer em produto/preço/estoque;
- remover/neutralizar copy operacional antiga se estiver na description;
- ajustar SEO title/meta para padrão premium;
- adicionar schema/guia se necessário, preferindo primeiro DEV/preview para parte visual.

Risco: médio por envolver theme/snippet/description e bug visível. Fazer com backup/readback.

### 2) Adidas Handball Spezial — schema-only production

URL: `/collections/adidas-handball-spezial`
Collection id: `445699653854`
Produtos Admin: 15 / público: 13
Demanda: `adidas handball spezial` ~4.400 buscas/mês, tendência anual +83%.

Readback público:
- HTTP 200;
- title/meta já bons;
- FAQ textual existe;
- **FAQPage schema = 0**;
- sem Liquid error.

Recomendação:
- aplicar schema-only condicional, sem mudança visual, usando `snippets/lk-goc-schema-extra.liquid` ou asset equivalente;
- manter title/meta/description visual.

Risco: baixo.

### 3) New Balance 740 / ASICS Gel NYC — handoff Shopify antes de Growth

Demanda:
- `new balance 740` ~27.100 buscas/mês, tendência anual +235%.
- `asics gel nyc` ~60.500 buscas/mês.

Readback:
- handles `/collections/new-balance-740` e `/collections/asics-gel-nyc` não existem como collections no Admin;
- as URLs públicas retornam 200 por fallback/genérico, com title de coleção geral (`New Balance Todos os Modelos`, `Asics | Todos os Modelos`), o que não é superfície canônica decision-grade.

Recomendação:
- abrir handoff para LK Shopify validar/criar collections canônicas usando produtos ativos já existentes, sem consultar/alterar estoque;
- depois Growth prepara guia/FAQ/schema em DEV.

## Escopo negativo para todos

Não alterar:
- preço;
- estoque/Tiny/inventory;
- produtos;
- ordenação;
- GMC;
- campanhas;
- Klaviyo;
- checkout.

## Aprovação sugerida

`Aprovo fazer os próximos 3: (1) corrigir em produção o Liquid error da collection Adidas Sambae e higienizar apenas SEO/copy/schema necessário, com backup/readback/rollback, sem alterar produtos, preço, estoque, ordenação, GMC, campanhas, Klaviyo ou checkout; (2) aplicar schema-only condicional em produção para Adidas Handball Spezial, sem alteração visual nem SEO title/meta; (3) abrir handoff para LK Shopify validar/criar collections canônicas New Balance 740 e ASICS Gel NYC usando apenas produtos ativos já existentes, sem consultar ou alterar estoque, preço ou campanhas; depois Growth prepara guia/FAQ/schema em DEV antes de qualquer produção.`

## Observação

Sambae deve vir primeiro por ser bug público em coleção de altíssima demanda.
