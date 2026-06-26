# LK Financeiro — MAPA

Sub-área canônica para o agente/perfil `[LK] Financeiro` (`lk-finance`).

## Escopo

- Gastos, recebimentos, contas a pagar/receber, caixa e conciliação.
- Leitura/extração local de comprovantes, notas, boletos, extratos e PDFs financeiros.
- Receipts e evidências de categorização financeira local/read-only.
- Pacotes de decisão para divergências, pagamentos, transferências, cobrança, fornecedor/contador ou mudanças em fonte de verdade.

## Guardrails

- Padrão é read-only/local/preview.
- Bloqueados sem aprovação explícita escopada: pagamentos, transferências, banking/payment/accounting writes, contato com fornecedor/contador/cliente, mutation em banco/sistema financeiro, automações recorrentes novas, Docker/runtime/cron/secrets.
- Doppler `lc-keys/prd` é fonte de credenciais; documentar nomes/status apenas, nunca valores.

## Artefatos

- `receipts/` — recibos operacionais locais de OCR, categorização, readback e auditorias financeiras.

## Relações

- LK Stock continua dono de estoque/disponibilidade/pronta entrega.
- LK Shopify continua dono de superfície Shopify.
- LK Growth continua dono de Growth/SEO/GEO/CRO.
- Financeiro pode consumir evidências desses agentes, mas não assume seus writes nem suas fontes de verdade.
