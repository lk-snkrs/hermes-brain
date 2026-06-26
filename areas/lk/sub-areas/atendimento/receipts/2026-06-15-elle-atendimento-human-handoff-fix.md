# Elle — correção de pedido explícito “Atendimento”

Data: 2026-06-15
Área: LK / Atendimento / Elle

## Correção aplicada

Quando o cliente enviar uma mensagem explícita pedindo humano/Larissa, incluindo a mensagem curta `Atendimento`, a Elle agora deve responder publicamente com um aviso curto de transferência para a Larissa, em vez de ficar em silêncio.

Copy validada no smoke:

> Raissa, claro, vou transferir sua conversa para a Larissa, tudo bem? Ela vai te ajudar por aqui.

Sem nome válido, a resposta fica:

> claro, vou transferir sua conversa para a Larissa, tudo bem? Ela vai te ajudar por aqui.

Fora do horário de atendimento, a Elle acrescenta o horário da Larissa e avisa que ela verá ao retornar.

## Guardrails preservados

- Categoria: `human_handoff`.
- Handoff humano: `true`.
- Labels sugeridas: `whatsapp-api`, `humano`, `explicit_human_request`; o fluxo de labels de conversa adiciona `larissa` automaticamente em handoff.
- Não adiciona tag no contato/customer.
- Após handoff, mantém lock para evitar novas respostas automáticas repetidas.
- Permite essa resposta mesmo se a conversa já estiver assinalada ou com lock gerado pela própria Elle (`elle_handoff_assigned` / `human_assignee_existing`), para cobrir o caso em que o cliente responde apenas “Atendimento”. Continua bloqueando se houver lock real de humano digitando/respondendo.

## Arquivo/execução

- Container: `elle-chatwoot`.
- Arquivo no container: `/app/app.py`.
- Backup local antes/depois: `/opt/data/backups/elle-chatwoot/20260615T193309Z/`.
- Ação: `docker cp` do app corrigido para o container + `docker restart elle-chatwoot`.

## Verificação

Comando de smoke dentro do container:

```bash
docker exec elle-chatwoot python -m py_compile /app/app.py
docker exec elle-chatwoot python -c "import app,json; print(app.is_explicit_human_or_larissa_request('Atendimento')); flat={'content':'Atendimento','conversation_id':'__test__','message_id':'test','sender':{'name':'Raissa Dubena'},'event':'message_created','message_type':'incoming'}; r=app.classify(flat); assert r['category']=='human_handoff' and r['handoff'] and 'transferir sua conversa para a Larissa' in r['reply']; print(r['reply'])"
```

Resultado:

```text
True
Raissa, claro, vou transferir sua conversa para a Larissa, tudo bem? Ela vai te ajudar por aqui.
```

Health readback pós-restart:

```json
{"ok": true, "mode": "agentbot_ready", "dry_run": false, "write_enabled": true, "kill_switch": false, "public_reply_enabled": true, "debounce_enabled": true, "ai_enabled": true}
```
