# LK OS Fase 5 — CRM/RFM/Recompra — preview read-only — 2026-05-11

## Escopo

Preview analítico para segmentar base, janelas de recompra e filas de ação. Não cria campanha, não envia mensagem, não escreve em Supabase/Shopify/Klaviyo/WhatsApp.

## Fonte e janela

- Fonte: Supabase LK read-only REST: orders/order_items; no DB writes, no campaigns, no customer messages
- Pedidos pagos válidos: 4369
- Clientes com e-mail: 3633
- Primeiro pedido: 2023-02-02T08:01:01+00:00
- Último pedido: 2026-04-16T20:13:58+00:00
- Receita bruta estimada na base: R$ 10,998,128.92

## Segmentos RFM

- Alto valor esfriando: 1689 clientes
- Reativação fria: 1394 clientes
- Base nurturing: 188 clientes
- Novo alto potencial: 163 clientes
- Leal/recorrente: 103 clientes
- Champions/VIP: 96 clientes

## Cohorts comerciais

- Lançamento High-End: 2500 clientes
- Core Sneaker: 782 clientes
- Essential/Entrada: 351 clientes

## Janela de recompra observada

- Amostras de recompra: 736
- Mediana entre pedidos: 34.0 dias
- P25/P75: 6.0 / 105.0 dias

## Fila de ação sugerida — sem envio automático

- Reativação personalizada / wishlist / novidade da mesma família: 1689 clientes
- Winback leve com curadoria, separar de VIP: 1394 clientes
- Nurturing editorial segmentado por marca/tamanho: 291 clientes
- Pós-compra editorial + prova social + convite para segunda compra em 21-45 dias: 163 clientes
- VIP drop preview / concierge, sem desconto agressivo: 96 clientes

## Produtos mais presentes nos pedidos

- Tênis Onitsuka Tiger Mexico 66 Kill Bill Amarelo: 137
- Jason Markk Repel Spray Impermeabilizante: 128
- Tênis New Balance 9060 Sea Salt Moonbeam Branco: 102
- Tênis New Balance 204L Mushroom Arid Stone Marrom: 93
- Jason Markk Essential Kit de Limpeza: 88
- Tênis Adidas Samba OG Crochet Pack Sand Strata Bege: 79
- Tênis adidas Samba OG White Black Gum Branco: 67
- Tênis New Balance 204L Arid Timberwolf Bege: 64
- Tênis Onitsuka Tiger Mexico 66 SD Beige Beet Juice Bege: 63
- Tênis Onitsuka Tiger Mexico 66 SD Cream Birch Bege: 61
- Tênis Onitsuka Tiger México 66 Birch Peacoat Bege: 60
- Tênis Nike Dunk Low Cacao Wow Marrom: 54
- Tênis Onitsuka Tiger Mexico 66 SD Cream Black Orange Bege: 47
- Tênis Onitsuka Tiger Mexico 66 White Black Branco: 46
- Tênis Nike Moon Shoe SP Jacquemus Alabaster Amarelo: 46

## Amostra anonimizada para QA

- `a4d09aa408`: Champions/VIP / Lançamento High-End — RFM 525, 24d, 2 pedidos, R$ 4,199.98 — VIP drop preview / concierge, sem desconto agressivo
- `40b6095477`: Champions/VIP / Lançamento High-End — RFM 525, 25d, 2 pedidos, R$ 5,599.98 — VIP drop preview / concierge, sem desconto agressivo
- `b44fd40506`: Novo alto potencial / Lançamento High-End — RFM 515, 25d, 1 pedidos, R$ 6,299.99 — Pós-compra editorial + prova social + convite para segunda compra em 21-45 dias
- `8cdd2ed03b`: Novo alto potencial / Lançamento High-End — RFM 515, 25d, 1 pedidos, R$ 5,599.98 — Pós-compra editorial + prova social + convite para segunda compra em 21-45 dias
- `f5f7b35b10`: Novo alto potencial / Lançamento High-End — RFM 515, 25d, 1 pedidos, R$ 5,999.99 — Pós-compra editorial + prova social + convite para segunda compra em 21-45 dias
- `4b22a2955e`: Novo alto potencial / Lançamento High-End — RFM 514, 25d, 1 pedidos, R$ 2,799.99 — Pós-compra editorial + prova social + convite para segunda compra em 21-45 dias
- `8095fe2111`: Champions/VIP / Lançamento High-End — RFM 535, 26d, 3 pedidos, R$ 25,113.74 — VIP drop preview / concierge, sem desconto agressivo
- `994600f0cd`: Champions/VIP / Essential/Entrada — RFM 524, 26d, 2 pedidos, R$ 3,269.97 — VIP drop preview / concierge, sem desconto agressivo
- `62398c69a3`: Novo alto potencial / Lançamento High-End — RFM 514, 26d, 1 pedidos, R$ 3,199.99 — Pós-compra editorial + prova social + convite para segunda compra em 21-45 dias
- `972f47d744`: Novo alto potencial / Lançamento High-End — RFM 514, 26d, 1 pedidos, R$ 3,199.99 — Pós-compra editorial + prova social + convite para segunda compra em 21-45 dias
- `cae9bfa784`: Champions/VIP / Lançamento High-End — RFM 535, 26d, 3 pedidos, R$ 6,929.99 — VIP drop preview / concierge, sem desconto agressivo
- `46dddf5222`: Champions/VIP / Lançamento High-End — RFM 525, 26d, 2 pedidos, R$ 9,250.00 — VIP drop preview / concierge, sem desconto agressivo

## Guardrails

- Sem PII no relatório; amostras usam hash curto.
- Sem writes em banco, Shopify, Tiny, Klaviyo, WhatsApp ou Telegram externo.
- Antes de campanha real: cruzar disponibilidade por tamanho no Tiny, gerar copy/preview e pedir aprovação explícita.

## Próximos passos

1. Transformar estes segmentos em filas operacionais: VIP, alto valor esfriando, segunda compra e nurturing.
2. Criar regras de sugestão por família/produto: High-End, Core Sneaker, Essential.
3. Preparar preview de mensagens por segmento, sem disparar.
4. Se aprovado futuramente, criar automação/lista em Klaviyo/WhatsApp com rollback e opt-out.
