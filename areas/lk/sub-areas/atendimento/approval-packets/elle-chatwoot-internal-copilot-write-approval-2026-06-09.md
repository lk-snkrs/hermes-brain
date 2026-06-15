# Approval Packet — Elle Chatwoot copiloto interno real

Data: 2026-06-09
Área: LK / Atendimento / Elle / Chatwoot
Tipo: aprovação necessária para write interno real

## Decisão necessária

Autorizar ou não a Elle a sair do dry-run para executar **somente writes internos no Chatwoot**:

1. Criar nota privada.
2. Aplicar labels operacionais.
3. Atribuir/transbordar conversa ao time `atendimento whatsapp`.

Continuam proibidos:

- Mensagem pública ao cliente.
- WhatsApp send.
- Responder reclamação como decisão final.
- Prometer estoque, preço, prazo, reserva ou desconto.
- Alterar Shopify, Tiny, produtos, pedidos, estoque, preço, tema, campanhas, inbox, webhook ou automações públicas.

## Evidência atual

### Estado de segurança atual

Doppler/health indicam:

- `ELLE_DRY_RUN=true`.
- `CHATWOOT_WRITE_ENABLED=false`.
- `ELLE_KILL_SWITCH=true`.
- `CHATWOOT_TEAM_ID`: presente.
- `CHATWOOT_LK_API_TOKEN`: presente.
- `CHATWOOT_BASE_URL`: presente.
- `CHATWOOT_ACCOUNT_ID`: presente.
- `values_printed=false`.

Health público:

- Chatwoot `/api`: HTTP `200`.
- `queue_services=ok`.
- `data_services=ok`.
- Elle `/healthz`: HTTP `200`.
- Elle live flags:
  - `dry_run=True`.
  - `write_enabled=False`.
  - `kill_switch=True`.

### Testes já passados

- Dry-run local Elle MVP1C: `12/12` em intent, labels, risk e handoff.
- Forbidden public actions: `0`.
- Smoke sintético para receiver Elle: HTTP `200`, `status=processed`, sem write detectável.
- Probe read-only de conversa sintética no Chatwoot: HTTP `404`, indicando que o teste não criou conversa real.

## Mudança proposta se aprovada

Alterar somente os flags do runtime da Elle para permitir writes internos:

- `ELLE_DRY_RUN=false`.
- `CHATWOOT_WRITE_ENABLED=true`.
- `ELLE_KILL_SWITCH=false`.

Escopo do adapter permitido:

- `POST /api/v1/accounts/{account_id}/conversations/{conversation_id}/messages` com `private: true`.
- `POST /api/v1/accounts/{account_id}/conversations/{conversation_id}/labels`.
- `POST /api/v1/accounts/{account_id}/conversations/{conversation_id}/assignments` com team `atendimento whatsapp`.

## Validação obrigatória pós-ativação

1. Health da Elle deve mostrar:
   - `dry_run=false`.
   - `write_enabled=true`.
   - `kill_switch=false`.
2. Verificar que o código ainda não possui método de resposta pública.
3. Executar um teste em conversa controlada/não-cliente real, ou aguardar um inbound real e validar somente nota privada/labels/assignment.
4. Conferir via API Chatwoot read-only que:
   - mensagem criada é `private=true`;
   - labels são apenas operacionais;
   - assignment é para `atendimento whatsapp`.
5. Se qualquer write público aparecer, rollback imediato.

## Rollback

Voltar imediatamente para:

- `ELLE_DRY_RUN=true`.
- `CHATWOOT_WRITE_ENABLED=false`.
- `ELLE_KILL_SWITCH=true`.

Verificar:

- Elle `/healthz` reflete dry-run e kill-switch ativos.
- Nenhuma mensagem pública foi enviada.
- Registrar receipt de rollback.

## Aprovação explícita necessária

Para executar a ativação, Lucas precisa responder com escopo explícito, por exemplo:

```text
Aprovo ativar a Elle como copiloto interno no Chatwoot, sem resposta pública, permitindo apenas nota privada, labels e assignment para atendimento whatsapp, com rollback imediato se houver qualquer risco.
```

Sem essa frase/escopo equivalente, manter `dry_run=true`, `write_enabled=false`, `kill_switch=true`.

## Complemento de completude do approval packet — 2026-06-14

### Decisão solicitada / ação proposta
- Decisão solicitada: Lucas deve aprovar, ajustar ou bloquear explicitamente o packet `Approval Packet — Elle Chatwoot copiloto interno real` antes de qualquer execução sensível.
- Ação proposta: usar este documento apenas como approval packet/preview; execução só pode ocorrer no escopo exato aprovado e com receipt/readback posterior.

### Target / owner
- Target: `Approval Packet — Elle Chatwoot copiloto interno real` no caminho `areas/lk/sub-areas/atendimento/approval-packets/elle-chatwoot-internal-copilot-write-approval-2026-06-09.md`.
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
