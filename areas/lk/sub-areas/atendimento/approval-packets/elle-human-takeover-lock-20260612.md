# Approval Packet — Elle Human Takeover Lock

Data: 2026-06-12T14:56:58Z
Área: LK / Atendimento / Chatwoot / Elle
Status: aguardando aprovação explícita para deploy/restart em produção

## Objetivo

Implementar regra obrigatória: quando um agente humano começar a atuar em uma conversa, a Elle para de responder naquela conversa.

## Diagnóstico read-only confirmado

Arquivo live inspecionado: `/opt/elle-chatwoot/app.py` no VPS.

Estado atual observado:

- Elle aceita POSTs AgentBot/legacy e filtra apenas eventos que não sejam `message_created` + `incoming`.
- Eventos `outgoing`, `conversation_typing_on`, `conversation_updated` hoje são ignorados pelo `event_filter` sem criar trava.
- `apply_actions()` envia resposta pública se `PUBLIC_REPLY_ENABLED=true` e não há checagem de lock imediatamente antes do envio.
- Flags atuais seguem seguras: dry-run/kill-switch impedem resposta pública, mas o bloqueio precisa existir antes de liberar public reply.

## Mudança proposta

Adicionar Human Takeover Lock local por `conversation_id`, persistido em arquivo JSON, com TTL.

### Novas variáveis sugeridas

- `ELLE_HUMAN_LOCK_PATH=/data/human_locks.json`
- `ELLE_HUMAN_LOCK_TTL_SECONDS=86400`
- `ELLE_TYPING_LOCK_TTL_SECONDS=600`

### Eventos que criam lock

1. `message_created` com `message_type=outgoing`, `private=false`, `sender.type=user`
   - Motivo: `human_outgoing_message`
   - TTL: 24h

2. `conversation_typing_on` com usuário/agente humano
   - Motivo: `human_typing_on`
   - TTL: 10min

3. `conversation_updated` com `assignee_id` atual preenchido ou `meta.assignee` humano
   - Motivo: `human_assignee`
   - TTL: 24h

### Checagem antes de responder

Antes de `chatwoot('POST' ... messages ...)`, executar:

- limpar locks expirados;
- verificar se `conversation_id` tem lock ativo;
- se sim, não enviar resposta e logar `blocked_by_human_takeover`.

### Comportamento esperado

- Cliente manda mensagem e ninguém humano toca: Elle pode classificar normalmente (ainda respeitando flags e categorias).
- Agente começa a digitar: Elle trava a conversa por 10min e cancela resposta.
- Agente envia qualquer resposta pública: Elle trava por 24h.
- Agente assume conversa: Elle trava por 24h.
- Handoff humano continua prioritário.

## Patch conceitual

Inserir funções:

```python
HUMAN_LOCK_PATH = Path(os.environ.get('ELLE_HUMAN_LOCK_PATH', '/data/human_locks.json'))
HUMAN_LOCK_TTL_SECONDS = int(os.environ.get('ELLE_HUMAN_LOCK_TTL_SECONDS', '86400'))
TYPING_LOCK_TTL_SECONDS = int(os.environ.get('ELLE_TYPING_LOCK_TTL_SECONDS', '600'))


def load_human_locks() -> dict:
    try:
        data = json.loads(HUMAN_LOCK_PATH.read_text())
        now = time.time()
        locks = {str(k): v for k, v in data.get('locks', {}).items() if float(v.get('expires_at', 0)) > now}
        if locks != data.get('locks', {}):
            save_human_locks(locks)
        return locks
    except Exception:
        return {}


def save_human_locks(locks: dict) -> None:
    HUMAN_LOCK_PATH.parent.mkdir(parents=True, exist_ok=True)
    HUMAN_LOCK_PATH.write_text(json.dumps({'locks': locks}, ensure_ascii=False))


def set_human_lock(conversation_id, reason: str, ttl: int) -> dict:
    if not conversation_id:
        return {'locked': False, 'reason': 'missing_conversation_id'}
    locks = load_human_locks()
    cid = str(conversation_id)
    lock = {'reason': reason, 'created_at': time.time(), 'expires_at': time.time() + ttl}
    locks[cid] = lock
    save_human_locks(locks)
    return {'locked': True, 'conversation_id': cid, **lock}


def get_human_lock(conversation_id) -> dict | None:
    if not conversation_id:
        return None
    return load_human_locks().get(str(conversation_id))
```

Estender `flatten()` para extrair:

- `sender.type`
- `assignee_id`
- `meta.assignee.id`
- `changed_attributes`

Adicionar antes do filtro atual:

```python
lock_event = detect_human_takeover(flat, payload)
if lock_event:
    log_event({'ts': time.time(), 'status': 'human_lock_set', **lock_event})
    return self._send(202, {'ok': True, 'status': 'human_lock_set'})
```

Adicionar em `apply_actions()` antes de resposta pública:

```python
lock = get_human_lock(cid)
if lock:
    outputs.append({'public_reply_skipped': 'blocked_by_human_takeover', 'lock_reason': lock.get('reason')})
    result['reply'] = ''
```

## Testes obrigatórios antes de ativar resposta pública

1. Healthcheck segue 200.
2. POST sintético `message_created incoming` em dry-run processa e não escreve.
3. POST sintético `conversation_typing_on` cria lock.
4. POST sintético `message_created incoming` após lock retorna processado/ignorado sem `reply_allowed` efetivo.
5. POST sintético `message_created outgoing` cria lock de 24h.
6. Logs mostram `human_lock_set` e/ou `blocked_by_human_takeover` sem conteúdo sensível.
7. Container reiniciado e persistência em `/data/human_locks.json` confirmada.

## Rollback

- Restaurar backup de `/opt/elle-chatwoot/app.py` criado antes do patch.
- Recriar container/serviço `elle-chatwoot`.
- Verificar `/healthz`.
- Manter `ELLE_KILL_SWITCH=true` durante rollback.

## Aprovação necessária

Para executar o patch live, preciso de aprovação explícita do Lucas com escopo, por exemplo:

> Aprovo aplicar o Human Takeover Lock na Elle no VPS, com backup, sem ativar resposta pública, reiniciar apenas o serviço elle-chatwoot e testar em dry-run.

## Complemento de completude do approval packet — 2026-06-14

### Decisão solicitada / ação proposta
- Decisão solicitada: Lucas deve aprovar, ajustar ou bloquear explicitamente o packet `Approval Packet — Elle Human Takeover Lock` antes de qualquer execução sensível.
- Ação proposta: usar este documento apenas como approval packet/preview; execução só pode ocorrer no escopo exato aprovado e com receipt/readback posterior.

### Target / owner
- Target: `Approval Packet — Elle Human Takeover Lock` no caminho `areas/lk/sub-areas/atendimento/approval-packets/elle-human-takeover-lock-20260612.md`.
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
