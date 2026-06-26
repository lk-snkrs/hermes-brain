# Elle Chatwoot Cloud — execution status from existing info — 2026-06-09-095323 -03

## Pedido atual

Lucas disse: “você tem todas as informações”.

## Checagem feita

Foram verificadas fontes locais e Doppler sem imprimir secrets.

### O que existe confirmado

- Núcleo Elle MVP1C já implementado e testado.
- Policies, intents, guardrails e template de nota privada existem.
- Adapter Chatwoot internal-only existe.
- Receiver `https://elle.lkskrs.online` existe e está online em modo seguro.
- Secrets atuais no Doppler:
  - `CHATWOOT_BASE_URL`
  - `CHATWOOT_ACCOUNT_ID`
  - `CHATWOOT_LK_API_TOKEN`
  - `CHATWOOT_TEAM_ID`
  - `CHATWOOT_WRITE_ENABLED`
  - `ELLE_CHATWOOT_WEBHOOK_SECRET`
  - `ELLE_CHATWOOT_WEBHOOK_URL`
  - `ELLE_DRY_RUN`
  - `ELLE_KILL_SWITCH`
  - `ELLE_WEBHOOK_BASE_URL`
- Diagnóstico atual desses secrets aponta para o Chatwoot self-hosted `https://chat.lkskrs.online`, account `1`, não para um tenant Cloud novo.

### O que não apareceu em Doppler/Brain

Não foram encontrados secrets Cloud específicos, como:

- `CHATWOOT_CLOUD_BASE_URL`
- `CHATWOOT_CLOUD_ACCOUNT_ID`
- `CHATWOOT_CLOUD_API_TOKEN`
- `CHATWOOT_CLOUD_TEAM_ID`
- `CHATWOOT_CLOUD_WHATSAPP_INBOX_ID`

## Interpretação

Lucas está correto que as informações operacionais da Elle já existem. O que não está confirmado é se o Chatwoot Cloud usa exatamente as mesmas credenciais/IDs ou se ainda precisa de um token/API/account diferente.

A migração pode seguir com dois trilhos:

1. **Trilho local/arquitetural imediato** — permitido sem Cloud token:
   - preparar código/config para suportar target `cloud` separado;
   - manter dry-run/kill-switch;
   - preparar webhook URL e smoke synthetic local;
   - preparar pacote de secrets esperados.

2. **Trilho live Cloud** — bloqueado até haver credencial/tenant Cloud real:
   - validar API Cloud;
   - listar labels/teams/inboxes;
   - criar webhook Cloud;
   - receber evento real;
   - escrever nota privada/labels.

## Próxima execução segura recomendada

Criar uma camada de configuração dual-target para Elle:

```text
CHATWOOT_TARGET=self_hosted|cloud
```

E deixar os secrets Cloud opcionais, sem quebrar o self-hosted. O target `cloud` só ativa quando os secrets Cloud existirem.

## Critério de aceite

- Testes antigos continuam passando.
- Config target `self_hosted` continua usando os secrets atuais.
- Config target `cloud` falha fechado se faltar `CHATWOOT_CLOUD_API_TOKEN`.
- Nenhuma resposta pública é implementada.
- Nenhum write externo é feito.
