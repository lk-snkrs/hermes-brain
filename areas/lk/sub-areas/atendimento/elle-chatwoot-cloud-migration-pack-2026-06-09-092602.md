# Elle → Chatwoot Cloud Migration Pack — 2026-06-09-092602 -03

## Status executivo

A Elle/L não precisa começar do zero. Já existe um MVP 1C funcional em dry-run, criado para o Chatwoot self-hosted da LK. O trabalho agora é adaptar esse núcleo para o Chatwoot Cloud que Lucas está configurando.

Este pacote é documental/preparatório. Nenhuma alteração foi feita no Chatwoot Cloud, no Chatwoot self-hosted, em webhooks, Docker, WhatsApp, Shopify, Tiny ou produção.

## Artefatos existentes reaproveitáveis

### Policies / base operacional

- `policies/elle_intents.yaml`
- `policies/elle_guardrails.yaml`
- `policies/elle_private_note_template.md`

Esses arquivos já cobrem intents iniciais:

- saudação
- pedido
- prazo
- estoque
- produto
- troca
- devolução
- reclamação
- financeiro
- VIP
- encomenda/preorder
- ambíguo

Guardrails atuais:

- `public_replies_allowed: false`
- estoque/pronta entrega: Tiny/`lk-stock`
- Shopify: contexto, não estoque truth
- handoff obrigatório para reclamação, financeiro, devolução, encomenda e ambíguo
- bloqueio de WhatsApp/public reply/Shopify write/Tiny write/product/order/price/stock/theme changes

### Código já existente

- `scripts/elle_dryrun_classifier.py`
  - classificador determinístico conservador
  - filtra evento `message_created`
  - aceita apenas mensagem incoming
  - ignora nota privada, outbound e evento da própria Elle
  - idempotência por `event_id`/`message_id`
  - gera intents, labels, risco, fontes necessárias, handoff e nota privada

- `scripts/chatwoot_internal_actions.py`
  - adapter internal-only
  - funções: `create_private_note`, `apply_labels`, `assign_team`
  - não implementa resposta pública por design
  - defaults: `dry_run=true`, `write_enabled=false`, `kill_switch=true`

- `scripts/elle_mvp1c_dryrun.py`
  - dry-run local com fixtures

### Testes existentes

Executados novamente em 2026-06-09-092602 -03:

```text
test_elle_classifier OK
test_elle_idempotency OK
test_chatwoot_internal_actions OK
elle_mvp1c_dryrun: 12 fixtures
intent_ok: 12/12
labels_ok: 12/12
risk_ok: 12/12
handoff_ok: 12/12
forbidden_action_count: 0
```

### Receiver/deploy anterior

- Serviço anterior: `/opt/elle-chatwoot` no VPS `72.60.150.124`
- URL pública: `https://elle.lkskrs.online`
- Health observado em 2026-06-09: `ok=true`, `dry_run=true`, `write_enabled=false`, `kill_switch=true`
- Webhook self-hosted observado: `message_created` para `elle.lkskrs.online`

Esse receiver pode ser reaproveitado como endpoint público também para Chatwoot Cloud, desde que sejam separados os secrets/configs por ambiente.

## Mudança principal: self-hosted → Chatwoot Cloud

O Chatwoot Cloud terá novos identificadores e credenciais. O núcleo da Elle continua igual, mas o adapter precisa usar dados do Cloud:

- `CHATWOOT_CLOUD_BASE_URL`
- `CHATWOOT_CLOUD_ACCOUNT_ID`
- `CHATWOOT_CLOUD_API_TOKEN`
- `CHATWOOT_CLOUD_TEAM_ID` para equipe de atendimento
- `CHATWOOT_CLOUD_WHATSAPP_INBOX_ID` quando WhatsApp Cloud estiver conectado
- `ELLE_CHATWOOT_CLOUD_WEBHOOK_SECRET` ou secret/path dedicado
- flags próprias de modo:
  - `ELLE_CLOUD_DRY_RUN=true`
  - `ELLE_CLOUD_WRITE_ENABLED=false`
  - `ELLE_CLOUD_KILL_SWITCH=true`

Não misturar token/self-hosted com token/cloud.

## Dados que Lucas precisa pegar no Chatwoot Cloud

### 1. URL base

Exemplo:

```text
https://app.chatwoot.com
```

ou o domínio exato fornecido pelo Chatwoot Cloud para a conta.

### 2. Account ID

No Chatwoot, normalmente aparece na URL:

```text
/app/accounts/<ACCOUNT_ID>/...
```

Precisamos do número.

### 3. Access Token do perfil

Caminho típico:

```text
Profile Settings → Access Token
```

Esse token deve ir para Doppler, não para Brain/chat. Se Lucas colar no Telegram, tratar como sensível e recomendar rotação depois.

### 4. Team ID

Equipe desejada para transbordo, idealmente algo como:

```text
Atendimento WhatsApp
```

Precisamos do ID via API ou URL.

### 5. Inbox ID do WhatsApp Cloud

Quando Lucas terminar de conectar WhatsApp no Chatwoot Cloud, precisamos do ID da inbox real de WhatsApp.

Importante: API inbox/Shopify/internal não substitui WhatsApp Cloud inbox.

### 6. Webhook

Precisamos criar/configurar no Chatwoot Cloud um webhook para:

```text
message_created
```

Endpoint sugerido:

```text
https://elle.lkskrs.online/webhooks/chatwoot-cloud/<secret>
```

ou rota equivalente separada do self-hosted.

## Fases de migração

### Fase A — Inventário Cloud read-only

Objetivo: confirmar conta, labels, teams e inboxes no Chatwoot Cloud.

Sem writes.

Checks:

- account name/ID
- labels existentes
- teams existentes
- inboxes existentes
- webhook support disponível
- WhatsApp Cloud inbox presente ou pendente

### Fase B — Duplicar config segura da Elle para Cloud

Objetivo: preparar runtime sem escrever.

- criar/registrar secret names no Doppler, sem valores no Brain
- adicionar suporte a `CHATWOOT_TARGET=cloud|self_hosted` ou config separada
- manter `dry_run=true`, `write_enabled=false`, `kill_switch=true`
- gerar rota separada para Cloud

### Fase C — Webhook Cloud em dry-run

Requer aprovação explícita porque cria webhook no Chatwoot Cloud.

Escopo seguro:

```text
Aprovo criar webhook Chatwoot Cloud -> Elle em dry-run para evento message_created, sem notas, sem labels, sem assignment e sem mensagem pública.
```

Validação:

- health da Elle
- POST sintético assinado/secret path
- evento real de teste chegando no log
- action status = dry_run_or_kill_switch

### Fase D — Copiloto interno Cloud

Requer aprovação explícita para writes internos no Chatwoot Cloud.

Escopo:

- criar nota privada
- aplicar labels
- atribuir equipe
- sem resposta pública
- sem WhatsApp send

Flags:

- `ELLE_CLOUD_KILL_SWITCH=false`
- `ELLE_CLOUD_WRITE_ENABLED=true`
- `ELLE_CLOUD_DRY_RUN=false`

Apenas depois de smoke test e rollback claro.

### Fase E — Resposta automática allowlisted

Fase futura. Não ativar agora.

Requer:

- base de conhecimento validada
- lista de intents auto-respondíveis
- kill switch
- auditoria
- cooldown/idempotência
- políticas WhatsApp template/window
- confirmação de que estoque/prazo/preço sensível não será prometido

## Base de conteúdo / conhecimento

A base deve começar em arquivos versionados no Brain, antes de virar painel.

Sugestão:

```text
areas/lk/sub-areas/atendimento/knowledge/
  faq-operacional.yaml
  politicas-troca-devolucao.md
  formas-pagamento.md
  horarios-enderecos.md
  shipping-prazos-guardrails.md
  produtos-faq.md
  macro-respostas-aprovadas.yaml
  forbidden-claims.yaml
```

### Formato recomendado para macro aprovada

```yaml
- id: horario_atendimento
  intent: saudacao
  public_reply_allowed: true
  risk: baixo
  required_sources: [brain]
  text: "Oi! Somos a LK Sneakers. Como posso te ajudar?"
  blocked_if_contains:
    - estoque
    - prazo
    - reclamação
```

Nada vira resposta pública sem `public_reply_allowed: true` e revisão humana.

## Intents autoatendíveis no futuro

Candidatas de baixo risco, depois de validação:

- saudação
- horário/endereço
- formas de pagamento genéricas
- política básica de troca sem caso específico
- pedido: apenas confirmação de que vai verificar/encaminhar, não status final sem fonte

Sempre humano/sem auto-resposta final:

- estoque/disponibilidade/pronta entrega/tamanho
- reclamação
- financeiro
- devolução/reembolso
- troca complexa
- atraso
- desconto/reserva/negociação
- VIP/condição especial
- encomenda/preorder
- mensagem ambígua

## Contrato esperado do evento Chatwoot

O classificador atual espera uma normalização com campos:

```json
{
  "event": "message_created",
  "event_id": "...",
  "message_id": "...",
  "conversation_id": 123,
  "message_type": "incoming",
  "private": false,
  "content": "texto do cliente",
  "sender": {"name": "..."}
}
```

Se o payload do Chatwoot Cloud divergir do self-hosted, criar um normalizador antes do classificador.

## Critérios de aceite do próximo passo técnico

Para declarar a migração Cloud pronta em dry-run:

1. Secrets Cloud existem no Doppler por nome, `values_printed=false`.
2. API Cloud responde account/labels/teams/inboxes read-only.
3. Elle aceita webhook sintético Cloud e registra `dry_run`.
4. Nenhuma função de public reply existe no adapter ativo.
5. Testes locais passam.
6. Evento real de uma conversa de teste no Chatwoot Cloud chega na Elle.
7. Nenhuma nota/label/assignment é escrita enquanto kill switch estiver ativo.

## Próxima decisão de Lucas

Escolher uma das opções:

1. Só preparar secrets/config e inventário read-only do Chatwoot Cloud.
2. Aprovar criação do webhook Cloud em dry-run.
3. Aguardar Lucas terminar WhatsApp Cloud e só depois conectar Elle.

## Guardrails finais

- Sem resposta pública agora.
- Sem prometer estoque/preço/prazo/reserva.
- Tiny/`lk-stock` segue dono obrigatório de disponibilidade.
- Chatwoot Cloud é superfície de atendimento; base/guardrails ficam no Brain/Elle.
- Qualquer write no Chatwoot Cloud precisa aprovação escopada.
