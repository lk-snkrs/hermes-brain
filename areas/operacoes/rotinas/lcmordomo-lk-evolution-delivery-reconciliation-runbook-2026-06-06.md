# LC Mordomo — Runbook aprendido: LK Evolution delivery reconciliation

Data: 2026-06-06
Origem: LK Ops / Atendimento
Destino: LC Mordomo / Operações pessoais de Lucas
Status: conhecimento operacional ensinado ao Mordomo; execução externa continua approval-gated.

## Resumo do que foi feito

LK Ops destravou o fluxo de confirmação de entrega/read receipt da Evolution API para mensagens WhatsApp LK Flagship sem usar n8n.

Arquitetura confirmada:

```text
Evolution API -> hermes-webhooks Vercel -> Hermes Gateway -> reconciler local determinístico -> ledger POS thank-you
```

Resultado final confirmado em teste real interno:

- job: `evo-webhook-finalauto-20260606173057`
- envio Evolution: `HTTP 201`, `PENDING`
- key hash: `5c0dd9fdaf71`
- record hash: `5d139b0581d6`
- Vercel/Hermes: `matched=1`, `updated=1`
- ledger final: `status=delivered`, `updates_count=2`, último status `DELIVERY_ACK`

## O problema raiz

A Evolution pode usar dois IDs diferentes para a mesma mensagem:

1. `key.id` — ID WhatsApp/Baileys retornado pelo `sendText`.
2. `id` — ID interno do registro Evolution usado em muitos `messages.update` reais.

Além disso, os webhooks reais chegam muito rápido. Em testes e fluxos onde o job local é criado logo depois do envio, o ACK pode chegar antes de o ledger persistir os aliases, causando `matched=0` mesmo com webhook válido.

## Correção aplicada

1. O proxy Vercel normaliza `messages.update`:
   - quando o payload não traz `data.key.id`, espelha `data.id`/`messageId`/`keyId` em `data.key.id` antes de assinar e encaminhar ao Hermes.
2. O proxy Vercel aplica atraso curto só para ACKs/update:
   - variável: `EVOLUTION_WEBHOOK_ACK_DELAY_MS`
   - default usado: `5000ms`
3. O sender local salva aliases imediatamente:
   - `evolution_message_id_hash`
   - `evolution_key_message_id_hash`
   - `evolution_record_id_hash`
   - e, por compatibilidade com gateway já carregado, salva o hash do record interno também em `evolution_message_id_hash` quando necessário.
4. Reprocessamento/manual só é usado como fallback de recuperação; conclusão real exige teste novo automático com ledger.

## Como LC Mordomo deve usar este aprendizado

Mordomo deve reconhecer sinais como:

- “Evolution webhook não confirma entrega”
- “WhatsApp LK enviado mas ledger continua pending”
- “matched=0 / updated=0 em `lk-evolution-delivery-reconciliation`”
- “Vercel aponta para Hermes mas não atualiza delivery_updates”

E deve responder/rotear assim:

```text
Isso é conhecimento de infraestrutura operacional LK/Evolution.
Não vou mexer em WhatsApp, Vercel, Evolution nem gateway sem aprovação atual.
Vou consultar o runbook/skill LK Evolution, verificar evidência read-only e preparar handoff para LK Ops/Hermes.
```

## O que Mordomo NÃO deve fazer sozinho

Sem aprovação explícita e escopo atual de Lucas, Mordomo não deve:

- enviar WhatsApp LK para cliente;
- alterar Evolution webhook config;
- fazer deploy Vercel;
- reiniciar Hermes Gateway;
- mutar ledger manualmente para parecer entregue;
- prometer preço, estoque, prazo, reserva ou disponibilidade LK.

Para estoque/disponibilidade/preço LK, Tiny continua fonte de verdade e LK Ops é dono do atendimento operacional.

## Fontes instaladas no perfil Mordomo

Skill copiada para o perfil Mordomo:

`/opt/data/profiles/mordomo/skills/productivity/lk-evolution-webhook-operations/SKILL.md`

Referências copiadas:

- `/opt/data/profiles/mordomo/skills/productivity/lk-evolution-webhook-operations/references/evolution-delivery-reconciliation.md`
- `/opt/data/profiles/mordomo/skills/productivity/lk-evolution-webhook-operations/references/vercel-ack-delay-and-id-normalization-20260606.md`

Receipt canônico LK Ops:

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/atendimento/receipts/lk-evolution-delivery-reconciliation-2026-06-06.md`

## Checklist se o problema reaparecer

1. Confirmar rota pública Evolution → Vercel:
   - `https://hermes-webhooks.lucascimino.com/webhooks/lk-evolution-delivery-reconciliation?secret=[REDACTED]`
2. Verificar logs Vercel/Hermes sanitizados:
   - evento `messages.update`
   - `message_id_hash`
   - `statuses`
   - `matched`
   - `updated`
   - `ledger_status`
3. Verificar ledger local do POS thank-you:
   - `status=delivered` ou `read`
   - `delivery_updates[]` preenchido
4. Se `matched=0`, checar aliases:
   - `key.id` vs `data.id`/record id interno
   - persistência antes/depois do ACK
5. Se precisar mexer em Vercel/Evolution/gateway, preparar approval packet com rollback.

## Frase de handoff recomendada

```text
LK Ops: apareceu anomalia de delivery reconciliation da Evolution. Evidência: [logs sanitizados], ledger: [status], hipótese: [ID alias/race/config]. Não executei write externo. Preciso de confirmação/ação do dono LK Ops se houver deploy, webhook config, restart ou envio WhatsApp.
```
