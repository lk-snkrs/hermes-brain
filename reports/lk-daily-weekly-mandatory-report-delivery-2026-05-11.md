# LK Daily + Weekly Mandatory Report Delivery, 2026-05-11

Lucas corrigiu a regra de entrega: Daily e Weekly devem ser enviados obrigatoriamente de acordo com a cadência aprovada.

## Contrato corrigido

- Daily: enviar todo dia às 08:00 BRT.
- Weekly: enviar toda segunda às 09:00 BRT.
- P0/P1 não são gatilhos de envio. São apenas prioridades dentro do relatório.
- O report é enviado mesmo se estiver tudo normal.
- Falha de script continua gerando alerta de falha.

## P0/P1 em linguagem simples

- P0 = urgente hoje, pode afetar venda/operação se não olhar.
- P1 = importante, acompanhar ou decidir, mas não necessariamente incêndio.

## Jobs mantidos

- Daily: `7c688553e293`, script `/opt/data/scripts/lk_daily_sales_brief_watchdog.py`.
- Weekly: `953b9055458e`, script `/opt/data/scripts/lk_weekly_ceo_review_watchdog.py`.

## Verificação

Os dois scripts foram alterados para sempre imprimir stdout quando o relatório é gerado, garantindo entrega pelo cron `no_agent`.
