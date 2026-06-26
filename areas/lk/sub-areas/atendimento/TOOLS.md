# TOOLS — LK Ops / Atendimento

## Toolsets recomendados

- file/search: Brain, FAQ, receipts, approval packets e handoffs.
- terminal limitado: validações locais, scripts read-only e checks sem secrets impressos.
- skills/session_search: histórico e procedimentos recorrentes.
- web/browser apenas para fontes públicas ou verificação não sensível.
- messaging somente quando houver autorização clara para envio externo permitido.

## Evitar por padrão

- cronjob sem rotina/cadência/kill criteria aprovados;
- writes API em Shopify/Tiny/CRM/WhatsApp/n8n sem approval packet;
- terminal destrutivo;
- exposição de tokens, cookies, dados de cliente ou credenciais;
- consultas amplas quando o pedido exige SKU/tamanho/item específico.

## Regra de fonte viva

Ferramenta local e memória não substituem fonte operacional. Para disponibilidade, preço, reserva, status, troca, pedido, prazo ou estoque, consultar a fonte viva autorizada antes de afirmar.
