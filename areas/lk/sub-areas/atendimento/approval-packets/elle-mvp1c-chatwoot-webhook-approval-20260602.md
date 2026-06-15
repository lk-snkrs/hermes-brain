# Approval Packet — Elle MVP 1C Chatwoot internal writes

- Data: 2026-06-02
- Sistema: Chatwoot `https://chat.lkskrs.online`
- Account: `LK Sneakers` / ID `1`
- Produto: Elle MVP 1C
- Status: aprovado conceitualmente por Lucas no Telegram; produção ainda depende de webhook receiver/secret/token configurados com segurança.

## Aprovação recebida

Lucas aprovou explicitamente:

```text
Aprovo o MVP 1C da Elle no Chatwoot em modo sem mensagem pública:
- criar notas privadas
- aplicar labels operacionais
- transbordar para o time atendimento whatsapp
- não enviar mensagens públicas ao cliente
- não alterar Shopify/Tiny/WhatsApp/produtos/pedidos/estoque/preço/tema
- usar Shopify só como contexto e Tiny como fonte de estoque
```

## Escopo aprovado

A Elle pode executar, quando o serviço estiver implantado e com kill switch controlado:

1. Criar nota privada em conversas do Chatwoot.
2. Aplicar labels operacionais já existentes.
3. Atribuir/transbordar conversa ao time `atendimento whatsapp`.

## Eventos Chatwoot pretendidos

- `message_created` somente para mensagem `incoming` de cliente.
- Futuro opcional: `conversation_created` para triagem inicial.

Eventos ignorados:

- mensagens outbound;
- notas privadas;
- mensagens/eventos da própria Elle;
- eventos duplicados;
- eventos não previstos.

## Writes explicitamente proibidos

- Mensagem pública ao cliente.
- Fechar/resolver conversa automaticamente.
- Alterar inbox, canal, automação, Captain/IA ou WhatsApp produtivo sem nova aprovação.
- Alterar Shopify, Tiny, produto, pedido, estoque, preço, tema, webhook externo, campanhas ou pagamentos.

## Segurança técnica obrigatória

1. `DRY_RUN=true` por padrão.
2. `CHATWOOT_WRITE_ENABLED=false` por padrão.
3. `ELLE_KILL_SWITCH=true` por padrão.
4. Webhook secret obrigatório.
5. Idempotência por `event_id`/`message_id`.
6. Logs com redaction de token/e-mail/telefone.
7. Nenhum token salvo em Brain/Telegram.
8. Nenhum método de resposta pública implementado no adapter MVP 1C.

## Rollback

1. Ativar kill switch.
2. Desativar webhook no Chatwoot.
3. Revogar token Chatwoot se suspeita de vazamento.
4. Manter operação manual no Chatwoot.

## Bloqueios atuais para ativação produtiva

1. Definir URL pública do webhook receiver da Elle.
2. Configurar segredo do webhook/assinatura.
3. Guardar token Chatwoot em cofre seguro, preferencialmente Doppler, sem repetir em chat.
4. Confirmar ID do time `atendimento whatsapp` via API/Chatwoot.
5. Fazer smoke test em `DRY_RUN=true` antes de habilitar writes internos.

## Evidência local atual

Dry-run local validado com 12 fixtures:

- intent accuracy: 12/12
- labels accuracy: 12/12
- risk accuracy: 12/12
- handoff accuracy: 12/12
- forbidden public actions: 0

Relatório:

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/atendimento/evaluation/reports/elle_mvp1c_dryrun_20260602.md`

## Complemento de completude do approval packet — 2026-06-14

### Decisão solicitada / ação proposta
- Decisão solicitada: Lucas deve aprovar, ajustar ou bloquear explicitamente o packet `Approval Packet — Elle MVP 1C Chatwoot internal writes` antes de qualquer execução sensível.
- Ação proposta: usar este documento apenas como approval packet/preview; execução só pode ocorrer no escopo exato aprovado e com receipt/readback posterior.

### Target / owner
- Target: `Approval Packet — Elle MVP 1C Chatwoot internal writes` no caminho `areas/lk/sub-areas/atendimento/approval-packets/elle-mvp1c-chatwoot-webhook-approval-20260602.md`.
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
