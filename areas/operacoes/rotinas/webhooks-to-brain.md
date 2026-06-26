# Webhooks/Eventos → Brain

## Função

Padrão receipt-first para eventos de Shopify, GitHub, Vercel, Notion, Klaviyo, WhatsApp, email e APIs.

## Quando usar

- Sempre que execução, decisão, evento, áudio, webhook, cron ou especialista produzir conhecimento que Lucas pode precisar novamente.
- Sempre que documentação afirmar algo sobre runtime: verificar evidência viva antes de declarar ativo.
- Sempre que um sistema externo precisar enviar webhook para Hermes — por exemplo Shopify, Evolution, GitHub, Vercel, Notion, Klaviyo, WhatsApp, email ou APIs.

## Ingresso público canônico

Quando um agente precisar receber webhooks externos para Hermes, o padrão preferido é usar o projeto público `hermes-webhooks` no Vercel como camada de borda/proxy antes do Hermes Gateway:

```text
Sistema externo -> hermes-webhooks Vercel -> Hermes Gateway webhook route -> processor determinístico/agente -> Brain/receipt/output
```

Projeto/URL canônicos conhecidos:

- projeto local: `/opt/data/hermes-webhooks`
- URL operacional preferida: `https://hermes-webhooks.lucascimino.com/webhooks/<route>`
- alias técnico Vercel: `https://hermes-webhooks.vercel.app/webhooks/<route>`
- o custom domain `hermes-webhooks.lucascimino.com` já passou health + probes assinados Shopify/Evolution; novos custom domains só viram canônicos depois de teste end-to-end com a mesma assinatura do provedor.

Regra para todos os agentes:

1. Não inventar n8n/Railway/Zapier/túnel novo quando o caso é receber webhook externo e `hermes-webhooks` já cobre ou pode cobrir a classe de provedor.
2. Usar branches provider-specific no Vercel: Shopify valida `X-Shopify-Hmac-Sha256` sobre o raw body; Evolution valida secret de proxy; outros provedores devem ter validação/normalização próprias.
3. Separar segredos por fronteira: segredo de entrada do provedor, segredo de assinatura da rota Hermes e token Vercel/deploy. Nunca imprimir valores; registrar só nomes/presença.
4. Reassinar o payload para Hermes com o secret da rota correta e preencher evento em header/campo que o Hermes Gateway filtre corretamente.
5. Para Shopify, preservar raw body, validar HMAC Shopify, mapear `X-Shopify-Topic` para o evento aceito pela rota Hermes e só então encaminhar/reassinar.
6. Para fluxo operacional, `202 accepted` genérico prova só que a requisição chegou ao Hermes; não prova ação de negócio. Verificar resposta determinística, ledger/receipt/estado downstream.
7. Qualquer deploy Vercel, alteração de env, configuração upstream do provedor ou write externo continua exigindo aprovação escopada, backup/rollback e verificação.

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
