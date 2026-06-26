# Receipt — Elle dual-target Chatwoot config prepared — 2026-06-09-095712 -03

## Escopo

Lucas disse “seguir” após alinhamento de que a Elle já existe e precisa ser adaptada para Chatwoot Cloud. Execução feita somente local/Brain, sem Chatwoot Cloud write, sem webhook, sem produção, sem Docker/VPS, sem resposta pública.

## Alterações feitas

### Criado

- `areas/lk/sub-areas/atendimento/scripts/chatwoot_target_config.py`
  - carrega configuração por target:
    - `CHATWOOT_TARGET=self_hosted`
    - `CHATWOOT_TARGET=cloud`
  - self-hosted usa os nomes atuais:
    - `CHATWOOT_BASE_URL`
    - `CHATWOOT_ACCOUNT_ID`
    - `CHATWOOT_LK_API_TOKEN`
    - `CHATWOOT_TEAM_ID`
  - cloud usa nomes separados:
    - `CHATWOOT_CLOUD_BASE_URL`
    - `CHATWOOT_CLOUD_ACCOUNT_ID`
    - `CHATWOOT_CLOUD_API_TOKEN`
    - `CHATWOOT_CLOUD_TEAM_ID`
    - `CHATWOOT_CLOUD_WHATSAPP_INBOX_ID`
  - fail-closed: target `cloud` não reutiliza token self-hosted se `CHATWOOT_CLOUD_API_TOKEN` estiver ausente.
  - `values_printed=false` por design; módulo não imprime secrets.

### Criado teste

- `areas/lk/sub-areas/atendimento/evaluation/test_chatwoot_target_config.py`

Cobertura:

- self-hosted usa secret names existentes e defaults seguros.
- cloud usa secret names Cloud quando presentes.
- cloud falha fechado sem `CHATWOOT_CLOUD_API_TOKEN`, mesmo se token self-hosted existir.
- target desconhecido gera erro claro.
- `RuntimeConfig.from_chatwoot_target(...)` integra config ao adapter internal-only.

### Modificado

- `areas/lk/sub-areas/atendimento/scripts/chatwoot_internal_actions.py`
  - adiciona `RuntimeConfig.from_chatwoot_target(...)`.
  - mantém default self-hosted antigo.
  - não adiciona resposta pública.

## TDD / verificação

RED observado:

```text
ModuleNotFoundError: No module named 'chatwoot_target_config'
```

Depois da implementação, GREEN:

```text
test_chatwoot_target_config OK
test_elle_classifier OK
test_elle_idempotency OK
test_chatwoot_internal_actions OK
elle_mvp1c_dryrun:
- count: 12
- intent_ok: 12
- labels_ok: 12
- risk_ok: 12
- handoff_ok: 12
- forbidden_action_count: 0
```

Verificação extra:

- adapter `chatwoot_internal_actions.py` segue sem método de resposta pública.
- endpoint `/messages` é usado apenas por `create_private_note` com payload `{"private": True}`.

## O que NÃO foi feito

- Nenhum webhook criado/alterado no Chatwoot Cloud.
- Nenhum token Cloud criado/salvo.
- Nenhuma API Cloud chamada.
- Nenhum write no Chatwoot self-hosted.
- Nenhuma alteração em VPS/Docker/Traefik/DNS.
- Nenhuma mensagem externa enviada.
- Nenhuma alteração Shopify/Tiny/WhatsApp/produto/pedido/estoque/preço.

## Próximo passo técnico possível

Quando houver secrets Cloud no Doppler ou token Cloud aprovado, rodar inventário read-only com `CHATWOOT_TARGET=cloud`:

- account
- labels
- teams
- inboxes
- webhooks

Mantendo `ELLE_CLOUD_DRY_RUN=true`, `ELLE_CLOUD_WRITE_ENABLED=false`, `ELLE_CLOUD_KILL_SWITCH=true`.
