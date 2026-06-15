# Approval packet — LK POS pós-compra / próximo lote Evolution

Data: 2026-06-09T16:17:04Z
Área: LK / Atendimento / Pós-compra / Evolution API LK Flagship
Status: aguardando aprovação explícita para envio externo.

## Contexto

O canário real único anterior foi bem-sucedido:

- pedido: `#147694`
- Evolution aceitou `201/PENDING`
- reconciliação local confirmou `server_ack` e `delivered` com `matched=1 updated=1`

## Pedido atual do Lucas

Lucas disse “Seguir”. Pela regra operacional deste perfil, “seguir” permite continuar o fluxo seguro, mas não autoriza novo write externo/produção. Portanto este pacote prepara o próximo passo sem executar envios.

## Proposta de próximo lote

Enviar lote pequeno de 3 mensagens reais via Evolution API LK Flagship Store.

Próximos candidatos, apenas por número de pedido:

- `#147695`
- `#147697`
- `#147698`

Todos estão atualmente:

- `status=scheduled`
- `dry_run=true`
- `send_executed=false`
- `external_write_executed=false`
- com telefone presente
- com mensagem preparada

## Estado da fila antes de eventual aprovação

- jobs `scheduled` pendentes: 9
- lote recomendado: 3
- remanescentes após lote de 3: 6

## Guardrails para execução se aprovado

Se Lucas aprovar explicitamente, executar com wrapper temporário de limite rígido, não com worker genérico permanente:

1. criar backup pré-envio;
2. selecionar apenas os 3 pedidos listados;
3. chamar Evolution `sendText` no máximo 3 vezes;
4. após cada envio, atualizar ledger local;
5. verificar webhook de reconciliação `server_ack`/`delivered`;
6. parar se houver erro HTTP ou status inesperado;
7. não alterar Doppler, cron, Shopify, Tiny, Chatwoot ou Vercel.

## Frase de aprovação necessária

Para executar o próximo lote real, pedir aprovação explícita como:

> Aprovo enviar 3 mensagens reais de pós-compra pela Evolution LK Flagship para os pedidos #147695, #147697 e #147698.

Sem essa aprovação, não enviar.

## Complemento de completude do approval packet — 2026-06-14

### Decisão solicitada / ação proposta
- Decisão solicitada: Lucas deve aprovar, ajustar ou bloquear explicitamente o packet `Approval packet — LK POS pós-compra / próximo lote Evolution` antes de qualquer execução sensível.
- Ação proposta: usar este documento apenas como approval packet/preview; execução só pode ocorrer no escopo exato aprovado e com receipt/readback posterior.

### Target / owner
- Target: `Approval packet — LK POS pós-compra / próximo lote Evolution` no caminho `areas/lk/sub-areas/atendimento/approval-packets/lk-pos-postpurchase-next-batch-approval-2026-06-09.md`.
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

### Rollback
- Rollback obrigatório: reverter somente a alteração aprovada usando backup/snapshot/artefato anterior quando aplicável; se a ação foi apenas preview/read-only, rollback é manter sem execução e registrar o bloqueio.
- Qualquer rollback que toque sistema externo exige o mesmo escopo aprovado, readback e receipt.

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
