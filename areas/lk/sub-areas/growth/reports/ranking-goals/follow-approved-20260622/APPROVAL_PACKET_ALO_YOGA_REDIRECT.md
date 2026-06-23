# Approval packet — Alo Yoga canonical redirect sem retrabalho

- Criado UTC: 2026-06-22T17:21:57.363778+00:00
- Modo: read-only packet; writes externos até aqui: 0; values_printed=false.
- Objetivo: corrigir perda de intenção em `/collections/alo-yoga` sem retrabalhar a collection já otimizada `/collections/alo-yoga-1`.

## Anti-retrabalho

- `/collections/alo-yoga-1` está em quarentena por ter sido trabalhada na Onda C1+C2 em 2026-06-19.
- Este packet **não propõe alterar copy, SEO, descrição, FAQ ou tema** de `/collections/alo-yoga-1`.
- Proposta limitada: corrigir rota/canonicalização de `/collections/alo-yoga` que hoje cai na home.

## Evidência

### Público

- `/collections/alo-yoga` → `301` para `/`.
- Final URL: home, HTTP 200.
- Canonical final: `https://lksneakers.com.br/`.
- H1 final: `LK Sneakers — Curadoria de Sneakers e Lifestyle Premium | São Paulo`.
- Sem `CollectionPage` da Alo nesse caminho.

### Shopify Admin read-only

- Collection `handle:alo-yoga`: **não encontrada**.
- Collection `handle:alo-yoga-1`: encontrada.
  - title: `Alo Yoga`
  - products: `116`
  - SEO title: `Alo Yoga | LK Sneakers`
  - description_len: `13418`
  - já contém FAQ/copy rica.

## Interpretação

A URL limpa `/collections/alo-yoga` está desperdiçando intenção de marca ao redirecionar para a home, enquanto a collection real vive em `/collections/alo-yoga-1`.

DataForSEO Brasil/pt para `alo yoga`:
- SV: `27.100`/mês.
- Maio 2026: `33.100`.
- Tendência YoY: `+83%`.

## Opção recomendada

Criar redirect production:

`/collections/alo-yoga` → `/collections/alo-yoga-1`

## Impacto esperado

- Recuperar intenção direta de marca/collection.
- Evitar usuário/Google cair na home quando busca Alo Yoga.
- Não mexe no conteúdo já otimizado da Onda C.

## Risco

- Baixo: redirect específico de uma URL atualmente sem collection real.
- Risco principal: se houver plano futuro de renomear handle para `/collections/alo-yoga`, o redirect deve ser removido antes.

## Rollback

- Remover o URL redirect criado.
- Revalidar `/collections/alo-yoga` voltando ao comportamento anterior.

## Aprovação necessária

Write customer-facing em Shopify URL redirect exige aprovação explícita.

Frase segura:

> aprovado redirect Alo Yoga /collections/alo-yoga para /collections/alo-yoga-1
