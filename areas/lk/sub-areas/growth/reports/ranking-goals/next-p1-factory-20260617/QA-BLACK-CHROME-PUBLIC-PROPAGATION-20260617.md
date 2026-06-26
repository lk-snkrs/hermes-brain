# QA público — Nike Mind 001 Black Chrome — 2026-06-17

Status: Admin OK / público ainda com propagação mista.

## Resultado da rechecagem

Foram feitos 8 fetches públicos cache-busted do PDP:

`/products/slide-nike-mind-001-black-chrome-preto`

Resultado:

- HTTP 200 em 8/8.
- Produto renderiza em 8/8.
- Versão nova completa — title/meta/copy/FAQ — em 2/8.
- Versão antiga ainda servida em 6/8.
- `application/ld+json`: 4 blocos detectados nos fetches.

## Interpretação

A mutation está correta no Admin Shopify, mas o storefront ainda está servindo HTML misto por propagação/cache/replicação. Não há evidência de falha no write; há evidência de inconsistência pública temporária.

## Decisão operacional

- Não fazer rollback agora.
- Não aplicar lote 2 em produção enquanto a propagação do Black Chrome não estiver consistente.
- Preparar apenas approval packet/read-only para Pearl Pink.
- Revalidar público antes de qualquer novo write.

values_printed=false
