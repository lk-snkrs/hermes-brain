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
