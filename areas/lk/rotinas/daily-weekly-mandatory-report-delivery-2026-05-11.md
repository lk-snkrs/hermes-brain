# LK Daily + Weekly Mandatory Report Delivery, 2026-05-11

## Correção Lucas

Lucas corrigiu a interpretação: os reports Daily e Weekly devem ser enviados obrigatoriamente nas respectivas cadências aprovadas, não apenas quando houver P0/P1.

## Novo contrato

- Daily Sales Brief: enviar diariamente às 08:00 BRT.
- Weekly CEO Review: enviar semanalmente às segundas 09:00 BRT.
- Se o script falhar, o cron envia alerta de falha.
- Se gerar report corretamente, sempre há stdout e, portanto, entrega ao Telegram/origin.

## O que P0/P1 significa

- P0: assunto urgente, deve aparecer com destaque porque pode exigir ação no mesmo dia. Exemplos: ruptura de SKU vendido, fonte/API quebrada, dado crítico inconsistente.
- P1: assunto importante, não necessariamente incêndio, mas precisa entrar no radar para decisão ou acompanhamento. Exemplos: baixo estoque, SKU sem mapeamento seguro, queda de conversão relevante.

P0/P1 agora são somente rótulos de prioridade dentro do report. Eles não controlam se o report será enviado.

## Estado operacional

- Job Daily mantido: `7c688553e293`, `0 11 * * *`, `/opt/data/scripts/lk_daily_sales_brief_watchdog.py`.
- Job Weekly mantido: `953b9055458e`, `0 12 * * 1`, `/opt/data/scripts/lk_weekly_ceo_review_watchdog.py`.
- Scripts ajustados para entrega obrigatória, com footer explicando P0/P1.

## Segurança preservada

- Sem n8n.
- Sem campanhas.
- Sem envio para cliente/fornecedor.
- Sem write em Shopify/Tiny/Merchant/GSC.
- Apenas entrega do report read-only no Telegram/origin.
