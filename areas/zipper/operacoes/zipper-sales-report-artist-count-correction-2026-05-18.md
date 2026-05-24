# Zipper OS — quantidade de obras por artista no report de vendas (2026-05-18)

## Correção de Lucas

Lucas pediu que o report de vendas do mês mostre a quantidade de obras de cada artista.

## Mudança aplicada

Arquivo alterado:

- `/opt/data/scripts/zipper_sales_report_external_delivery.py`

Mudanças:

- WhatsApp mudou de `Artistas: Nome, Nome...` para `Artistas/obras: Nome (N obras), ...`.
- A lista do WhatsApp agora mostra todos os artistas consolidados no período MTD, não apenas os 4 primeiros.
- HTML/e-mail: tabela `Resumo por artista` agora usa coluna `Obras`, com pluralização `1 obra` / `N obras`.
- Nenhum envio externo foi feito nesta correção porque o pedido veio em `/background`; apenas dry-run/artefatos foram validados.

## Preview validado

Período: `2026-05-01..2026-05-17`

WhatsApp corrigido:

```text
Zipper OS · Vendas do mês — 01/05 a 17/05/2026

• Total vendido: R$ 373.500,00
• Vendas/linhas: 6 · pedidos: 6
• Ticket médio: R$ 74.700,00
• Artistas/obras: Janaina Mello Landini (2 obras), Flávia Junqueira (1 obra), Ivan Grilo (1 obra), Dani Shirozono (1 obra), Laura Villarosa (1 obra)
• Origem/canal: Art Advisor (4), Galeria (2)

Destaque: Maior destaque: Janaina Mello Landini (R$ 278.000,00).
Qualidade dos dados: 1 sem valor
```

## Validação

- `python3 -m py_compile /opt/data/scripts/zipper_sales_report_external_delivery.py /opt/data/scripts/zipper_weekday_sales_report_watchdog.py`: OK.
- `/opt/data/scripts/zipper_sales_report_external_delivery.py`: dry-run OK.
- `/opt/data/scripts/zipper_weekday_sales_report_watchdog.py --dry-run`: OK, nenhum WhatsApp/e-mail enviado.
- Artefatos visíveis: 0 secret hits.
- HTML contém marker `zipper-os-sales-report-v1-2026-05-18`.
