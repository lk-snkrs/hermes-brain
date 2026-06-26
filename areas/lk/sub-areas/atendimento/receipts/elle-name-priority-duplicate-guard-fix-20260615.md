# Receipt — Elle nome Shopify prioritário + anti-duplicidade

- Data/hora: 2026-06-15T13:47:37Z
- Área: LK / Atendimento / Elle / Chatwoot
- Responsável humano: Lucas Cimino
- Classificação: produção com aprovação explícita do Lucas (“corrigir e já colocar live”)
- PII/secrets: não registrados; exemplo mantido somente como padrão sanitizado de handle sem sentido.

## Pedido
Corrigir comportamento da Elle quando o nome do contato WhatsApp é um handle sem sentido, como `crimson-log-317`, mas o contexto Shopify mostra um nome humano válido. Regra desejada:

1. Se houver nome Shopify válido, ele tem prioridade.
2. Se não houver Shopify, tentar nome do contato WhatsApp somente se fizer sentido como nome humano.
3. Se o nome do WhatsApp for handle/placeholder, não chamar pelo “primeiro nome”.
4. Colocar live.

## Causa provável
A Elle usava o primeiro token do `sender.name` do Chatwoot de forma direta em vários fluxos (`first_name(...)`). Isso fazia um handle gerado do WhatsApp/Chatwoot virar saudação nominal indevida.

Também havia risco de duplicidade porque a resposta pública não checava se a mesma mensagem já tinha acabado de ser enviada na conversa; além disso, conversas de handoff continuavam elegíveis para novas respostas antes do humano assumir.

## Alterações aplicadas
Arquivo alterado em produção: `/opt/elle-chatwoot/app.py`.

Patch aplicado:

- Adicionado `is_placeholder_person_name(...)` para rejeitar nomes com padrão de handle/placeholder, incluindo números com hífen/underscore/ponto.
- Adicionado `safe_first_name(...)` para só retornar primeiro nome se parecer humano.
- Adicionado `resolve_customer_name(...)`:
  - prioridade para nomes de contexto Shopify/metadados do Chatwoot;
  - fallback para nome válido do contato;
  - retorno vazio quando só houver handle/placeholder.
- `build_ai_prompt(...)` e regras determinísticas passaram a usar `resolve_customer_name(...)` em vez de `first_name(sender.name)`.
- Adicionado `was_same_public_reply_recently_sent(...)` para não publicar resposta idêntica recente na mesma conversa.
- Em `apply_actions(...)`, handoff agora cria lock local `elle_handoff_assigned` antes/com a resposta, reduzindo repetição depois de transferir para Larissa/Gisélia.
- Ajustado texto sem nome para começar com maiúscula (“Para...”, “Entendi...”, “Sobre...”, “Pelo...”).

## Deploy
- Backup criado no servidor antes do patch: `/opt/elle-chatwoot/backups/lucas-dup-name-hotfix-20260615T134251Z/`
- Compile: `python3 -m py_compile app.py elle_followup_worker.py` OK.
- Rebuild/recreate: `docker compose up -d --no-deps --build --force-recreate elle-chatwoot` OK.

## Verificação live
Health público retornou:

```json
{"ok": true, "mode": "agentbot_ready", "dry_run": false, "write_enabled": true, "kill_switch": false, "public_reply_enabled": true, "ai_enabled": true, "observer_enabled": true}
```

Container:

```text
elle-chatwoot|Up 3 minutes
```

Smoke/regressão dentro do container:

```json
{
  "placeholder_name_not_used": true,
  "placeholder_reply_starts_uppercase": true,
  "shopify_name_priority": true,
  "shopify_reply_uses_rodrigo": true,
  "duplicate_guard": true
}
```

Readback de guards no código live:

```json
{
  "placeholder_guard": true,
  "resolve_customer_name": true,
  "duplicate_public_reply_guard": true,
  "handoff_lock": true
}
```

## Writes externos
- Houve write de produção no serviço Elle (`/opt/elle-chatwoot/app.py`) e restart/rebuild do container, conforme aprovação explícita.
- Não houve envio WhatsApp manual/teste para cliente.
- Não houve alteração em Shopify, Tiny, Meta, Klaviyo ou banco do Chatwoot.

## Rollback
Restaurar backup:

```bash
cd /opt/elle-chatwoot
cp backups/lucas-dup-name-hotfix-20260615T134251Z/app.py app.py
python3 -m py_compile app.py elle_followup_worker.py
docker compose up -d --no-deps --build --force-recreate elle-chatwoot
```
