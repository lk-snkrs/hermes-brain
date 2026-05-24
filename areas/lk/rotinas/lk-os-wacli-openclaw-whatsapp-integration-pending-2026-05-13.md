# LK OS — Pendência: wacli/OpenClaw WhatsApp Integration

Status: `contract_ready_for_review_no_external_action`
Data: 2026-05-13
Escopo: LK Sneakers / LK OS / WhatsApp / wacli OpenClaw

## Objetivo

Incorporar o `wacli`/OpenClaw ao universo operacional da LK como camada de WhatsApp multi-conta, começando por leitura/sync e preparação de previews, sem envio automático.

## Contas conectadas/planejadas

- `pessoal` — Lucas pessoal; conectado para validação técnica do wacli multi-conta.
- `lk-compras` — WhatsApp Business LK Compras; conectado em 2026-05-13 e em sync inicial.
- `lk-loja` — WhatsApp Business loja física; planejado para etapa futura, ainda não conectado.

## Uso pretendido no LK OS

1. Capturar sinais operacionais de WhatsApp relevantes para compras, sourcing, ruptura, pedidos especiais e follow-ups.
2. Transformar mensagens em filas internas/preview: stockout, Droper, StockX/GOAT fallback, Notion/Júlio task.
3. Apoiar CRM/concierge apenas com preview e aprovação, nunca com envio automático por padrão.
4. Registrar aprendizado/correções de Lucas em Brain/skills para reduzir repetição de erros.

## Guardrails

- Nenhuma mensagem WhatsApp deve ser enviada sem aprovação explícita atual de Lucas.
- Nenhum contato com fornecedor, cliente ou grupo externo sem preview inline e aprovação.
- Nenhuma compra, reserva, sourcing real ou escolha de logística/importador por Hermes.
- Dados pessoais e conversas ficam fora de relatórios públicos/Telegram; usar agregados, hashes ou resumos sanitizados.
- `lk-compras` deve ser tratado como canal operacional sensível; leitura/sync é permitido para diagnóstico e modelagem quando aprovado no escopo, mas envio é A4.
- A rotina deve separar conta/canal: `pessoal`, `lk-compras`, `lk-loja` e futuros grupos.

## Próximo bloco seguro

- Contrato LK OS x wacli criado em `areas/lk/rotinas/lk-os-wacli-openclaw-whatsapp-contract-2026-05-13.md`.
- Próxima ação recomendada: aprovar ou ajustar um watch/read-only manual de 24h para `lk-compras`, com contagens por categoria e no máximo 3 exemplos sanitizados; sem cron, sem envio, sem nomes/telefones/texto literal.
- Depois validar com Lucas antes de qualquer automação de leitura recorrente, envio ou integração com tarefas externas.

## Não executado

- envio de WhatsApp;
- contato com grupo de compras;
- contato com cliente/fornecedor;
- automação recorrente/cron;
- write em Shopify, Tiny, banco, Klaviyo, Meta, Google ou Notion.
