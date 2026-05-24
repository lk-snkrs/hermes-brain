# Webhooks/Eventos → Brain

## Função

Padrão receipt-first para eventos de Shopify, GitHub, Vercel, Notion, Klaviyo, WhatsApp, email e APIs.

## Quando usar

- Sempre que execução, decisão, evento, áudio, webhook, cron ou especialista produzir conhecimento que Lucas pode precisar novamente.
- Sempre que documentação afirmar algo sobre runtime: verificar evidência viva antes de declarar ativo.

## Processo mínimo

1. Classificar o evento: informativo, decisão, execução, aprovação, risco, runtime, customer-facing ou aprendizado.
2. Escolher artefato durável: receipt, decisão, daily, hot, approval ledger, skill candidate, report ou rotina.
3. Salvar no Brain no local da empresa/área correta.
4. Atualizar MAPA/índice quando criar novo artefato estrutural.
5. Rodar verificação aplicável: health check, secret scan, runtime check ou dry-run de sync.
6. Usar silent-OK: avisar Lucas só em anomalia, risco, decisão necessária ou entrega relevante.

## Templates relacionados

- `areas/operacoes/templates/receipt-operacional.md`
- `areas/operacoes/templates/approval-ledger-entry.md`
- `areas/operacoes/templates/source-confidence.md`
- `areas/operacoes/templates/webhook-to-brain-event.md`
- `areas/operacoes/templates/voice-to-brain-capture.md`
- `areas/operacoes/templates/skill-promotion-candidate.md`

## Guardrails

- Chat, compactação e resposta do agente não são fonte de verdade.
- Customer-facing, financeiro, fornecedor, preço/disponibilidade, campanha, infra e writes externos exigem fonte/aprovação conforme autonomia vigente.
- Mission Control é cockpit; Brain versionado é fonte durável.
