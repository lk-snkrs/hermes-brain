# Addendum — status LK “temos vs não temos” — pacote feminino 2026-06-16

Correção de Lucas: todo pacote LK-TRENDS precisa mostrar explicitamente o que a LK não tem. Isso é obrigatório para transformar tendência em oportunidade.

## Fonte consultada

- Shopify Admin GraphQL read-only, via Doppler/hermes helper, perfil `lk-shopify`.
- Operação: somente `query products(first:10, query:$q)`, sem mutation.
- values_printed=false.
- Não foi consultado estoque, grade, disponibilidade ou prazo.

## Resultado por oportunidade

### Temos ativo / rota é impulsionar ou curar cor

- NB 204L Sea Salt Linen — encontrado ativo: `tenis-new-balance-204l-sea-salt-linen-bege`.
- NB 9060 Rosa/Rose — encontrados ativos, incluindo `Moonbeam Vintage Rose Lime`, `Rose Sugar Angora`, etc.
- NB 9060 Sea Salt — encontrados ativos, incluindo `Sea Salt Concrete`, `Sea Salt Moonbeam`, `Bisque Sea Salt`, etc.
- adidas SL 72 Marrom — encontrados ativos, incluindo `Maroon Almost Yellow`, `Earth Strata Warm Vanilla`, `Snakeskin Preloved Brown`.
- Salomon XT-6 Pink/Icy Pink — encontrado ativo: `tenis-salomon-xt-6-cloudburst-icy-pink...`.
- Salomon XT-Whisper — encontrado ativo: `Salomon XT-Whisper x Sandy Liang Fairy Tale Rosa`.

### Temos, mas não ativo

- NB 204L Rosewood Rosa — encontrado como `ARCHIVED`. Não tratar como descoberta nova; rota é avaliar reativação/listagem/posição, não “não temos”.

### Não encontramos no catálogo/página Shopify read-only

- AURALEE x New Balance 204L — zero matches para `AURALEE 204L`.
- New Balance 204L Animal Print — zero matches para `204L Animal Print`.
- HOKA — zero matches para `HOKA`.
- Ray BEAMS x Salomon XT-Whisper “Blueberry Cheesecake” — existe XT-Whisper Sandy Liang, mas não Ray BEAMS; tratar Ray BEAMS como lacuna específica.

## Regra atualizada

Todo próximo radar deve separar:

1. **Temos:** produto/família/página confirmada.
2. **Não temos:** lacuna exata de catálogo/página/produto.
3. **Temos mas não ativo:** archived/draft/inativo quando aparecer na busca.
4. **Não confirmado:** quando a checagem de catálogo não foi feita.

Nunca usar “não temos” como sinônimo de estoque. Estoque/grade/disponibilidade é com LK Stock.
