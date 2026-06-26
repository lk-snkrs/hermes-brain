# TOOLS — [LK] Estoque Loja Física

## Permitido por padrão

- Brain/local files read/write para PRD, receipts, handoffs e filas.
- Session search para reconciliar decisões recentes.
- Consultas read-only aprovadas via Doppler-first quando necessário.
- Relatórios/CSVs locais sanitizados.
- Terminal/runner local para validações e testes do próprio agente: `python -m unittest`, `python -m pytest` ou `pytest`, sem imprimir secrets e sem writes externos.

## Fontes desejadas

- Tiny `LK | CONTROLE ESTOQUE` — estoque real.
- Shopify Admin read-only — pedidos, produtos, variants, SKUs.
- GA4/GSC/Meta/Klaviyo/Judge.me — demanda e intenção.
- LK Trends/Growth artifacts — sinais de oportunidade.

## Bloqueado por padrão

- Qualquer mutation em Tiny, Shopify, Merchant, Klaviyo, Meta, WhatsApp, email, fornecedor ou financeiro.
- Impressão de secrets.
- Ativação de gateway/API/webhook/cron sem aprovação.

## Doppler

Secrets vivem em Doppler `lc-keys/prd`; reportar só presença/status, nunca valores.
