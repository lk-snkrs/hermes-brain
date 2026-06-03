# LK Curadoria PDP — Batch 10 revisado após checagem de markers existentes

Gerado em UTC: 2026-06-02T19:35:13.705748+00:00

## Resultado da checagem pré-upload

Nenhum upload foi feito.

Durante o preflight do Dev theme, o snippet já tinha markers antigos/dinâmicos que não apareceram no primeiro regex de `data-lk-variante`:

- `top30-vomero-premium` — já cobre Nike Vomero Premium.
- `top30-sb-dunk-low` — já cobre Nike SB Dunk Low.
- `top30-lululemon-define-line` — já cobre Lululemon Define.

Por segurança, esses grupos saíram do Batch 10 para evitar bloco duplicado na PDP.

## Escopo revisado proposto para Dev

1. `top30-air-jordan-1-low-regular` — Air Jordan 1 Low regular, sem OG/Travis/collab pesada.
   - Base read-only: 59 handles públicos/disponíveis/imagem OK no refinamento.
   - Sinal 180d nos públicos: 27 unidades / 27 pedidos.

2. `top30-air-jordan-1-low-og-regular` — Air Jordan 1 Low OG regular, separado do AJ1 Low comum e de Travis/collabs.
   - Base inicial validada: 12 handles públicos/disponíveis/imagem OK.
   - Sinal 180d nos escolhidos: 17 unidades / 17 pedidos.

3. `top30-adidas-sambae-regular` — Adidas Sambae regular.
   - Base inicial validada: 10 handles públicos/disponíveis/imagem OK.
   - Sinal 180d nos escolhidos: 1 unidade / 1 pedido.

## Bloqueios mantidos

- Yeezy Slide: ficou com 5 disponíveis/imagem OK; precisa >5 para renderizar 5 alternativas excluindo o produto atual.
- Lululemon Define: já existe marker antigo e também ficou no limite de 5 em validação inicial.
- Nike Vomero Premium e Nike SB Dunk Low: já existem no snippet, então não duplicar.

## Próxima decisão

Aprovar upload somente no Dev theme `155065450718` / role `unpublished`, adicionando apenas os 3 grupos revisados acima. Production continua intocada.
