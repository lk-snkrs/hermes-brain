# Approval packet — ativação live LK POS pós-venda 30min via Evolution / LK Flagship

Data UTC: 2026-06-05

## Estado atual confirmado

- Shopify já possui webhook `orders/paid` ativo para `https://hermes-webhooks.vercel.app/webhooks/lk-shopify-pos-restock`.
- Esse webhook foi criado em `2026-05-23T17:52:30-03:00` e não foi criado/alterado nesta etapa.
- O código local do processador Hermes foi alterado para criar fila dry-run local `pos_thankyou_queue.json` para pedidos POS pagos/não cancelados.
- Teste real manual pela Evolution API / instância `LK Flagship` funcionou após correção de formatação.

## O que ainda NÃO está live

- Envio automático para clientes ainda não está ativo.
- Não existe scheduler/worker aprovado rodando para consumir a fila e enviar mensagens reais.
- O job atual registra preview/dry-run com `send_executed: false`.
- Nenhum webhook Shopify novo foi criado.
- n8n não foi desabilitado por Hermes.

## Por que Evolution retornou PENDING

O endpoint `/message/sendText/{instance}` retorna status inicial/assíncrono. `PENDING` no HTTP 201 não significa necessariamente falha; Lucas recebeu a mensagem, então o teste prático de entrega foi OK. Para produção, o ideal é registrar status inicial e, se houver webhook/status update da Evolution, reconciliar depois.

## Ativação segura recomendada

Fase 1 — canary live limitado:

- Alterar processador para permitir `dry_run=false` apenas quando `LK_POS_POSTPURCHASE_LIVE_SEND=1`.
- Consumir somente jobs vencidos (`send_after <= now`).
- Enviar via Evolution API, instância `LK Flagship`.
- Dedupe por `order_id` e `phone_e164`.
- Respeitar bloqueios: sem telefone => não envia; pedido não POS/pago/cancelado => não envia.
- Kill switch: remover/desativar `LK_POS_POSTPURCHASE_LIVE_SEND` volta para dry-run.
- Primeiro canary: no máximo 1–3 envios reais, depois auditoria.

## Aprovação necessária para executar live

Frase sugerida:

```text
Aprovo ativar canary live do pós-venda POS 30min via Evolution API / LK Flagship, usando o webhook Shopify orders/paid já existente, com limite inicial de 3 envios reais, kill switch, dedupe por pedido/telefone, sem n8n e sem alterar Shopify/Tiny/Chatwoot.
```

## Sobre desabilitar n8n

Recomendação: não desabilitar n8n antes de observar pelo menos 1 venda POS real entrando no ledger Hermes e 1 canary real enviado com sucesso pela Evolution/LK Flagship. Depois disso, pode desabilitar o workflow n8n antigo com rollback claro.

## Complemento de completude do approval packet — 2026-06-14

### Decisão solicitada / ação proposta
- Decisão solicitada: Lucas deve aprovar, ajustar ou bloquear explicitamente o packet `Approval packet — ativação live LK POS pós-venda 30min via Evolution / LK Flagship` antes de qualquer execução sensível.
- Ação proposta: usar este documento apenas como approval packet/preview; execução só pode ocorrer no escopo exato aprovado e com receipt/readback posterior.

### Target / owner
- Target: `Approval packet — ativação live LK POS pós-venda 30min via Evolution / LK Flagship` no caminho `areas/lk/sub-areas/atendimento/approval-packets/lk-pos-postpurchase-live-activation-packet-20260605.md`.
- Owner operacional: LK Atendimento / LK Operações, com governança Hermes Geral e aprovação final Lucas.

### Escopo permitido
- Escopo permitido somente após aprovação explícita: executar apenas os itens, IDs, fluxos, mensagens, campos ou rotinas descritos neste packet, sem ampliar alvo por inferência.
- Pode fazer localmente sem nova aprovação: validação documental, preview, auditoria read-only, receipt e classificação de blockers.

### O que continua bloqueado
- Não pode fazer mensagem a cliente, contato externo, WhatsApp/e-mail, mudança de atendimento humano, Chatwoot/webhook/runtime, preço, disponibilidade, reembolso, reserva, negociação ou logística sem approval packet específico.
- Aprovação genérica como `seguir`, `fazer tudo` ou contexto antigo não amplia escopo; novo alvo exige novo approval packet.

### Risco
- Risco principal: transformar preview/packet em autorização ampla e executar ação sensível fora do escopo exato.
- Mitigação: fail-closed, approval textual específica, backup/snapshot quando aplicável, readback e receipt com contagens.

### Verificação / readback
- Verificação obrigatória: readback do sistema de atendimento/Chatwoot quando aplicável, ledger/receipt local, amostragem de conversas/contatos afetados e confirmação de zero envio externo não aprovado.
- Se houver divergência de identidade, fonte, escopo ou aprovação, bloquear execução e registrar causa sanitizada.

### Opções de aprovação
- Aprovar exatamente o escopo descrito neste packet.
- Aprovar apenas preview/dry-run/read-only.
- Ajustar alvo/limite antes de executar.
- Bloquear execução e manter como histórico/rascunho.

### Secret hygiene
- Usar credenciais somente via Doppler/wrapper seguro quando houver integração; não imprimir tokens, refresh tokens, passwords, service-account JSON, API keys ou connection strings.
- Relatórios e receipts devem manter `values_printed=false` e redigir qualquer valor sensível como `[REDACTED]`.
