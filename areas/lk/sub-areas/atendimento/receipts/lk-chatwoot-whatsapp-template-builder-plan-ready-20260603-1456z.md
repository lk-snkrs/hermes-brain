# LK Chatwoot — WhatsApp template builder follow-up

Data: 2026-06-03 14:56 UTC
Status: `implementation_plan_ready_no_prod_change`

## Pedido

Lucas respondeu `sim, seguir` após o PRD para implementar no Chatwoot uma opção de criar templates WhatsApp Business API diretamente pelo Chatwoot.

## Interpretação segura

Pelo guardrail LK, `seguir` autoriza continuação do fluxo seguro, não deploy/alteração de produção sensível. Como mexer no Chatwoot/proxy/Docker/produção e criar assets externos na Meta exige aprovação explícita, foi feito:

- inspeção read-only adicional do Chatwoot;
- plano de implementação detalhado;
- nenhum deploy;
- nenhum template criado na Meta;
- nenhuma campanha/envio/contato alterado.

## Evidências técnicas adicionais

Inspeção read-only confirmou:

- `config/routes.rb` já tem rota nested de inbox para:
  - `post :sync_templates`
  - `resource :csat_template`
- `app/javascript/dashboard/api/inboxes.js` já tem:
  - `syncTemplates`
  - `createCSATTemplate`
  - `getCSATTemplateStatus`
- `app/javascript/dashboard/store/modules/inboxes.js` já tem getters/actions para WhatsApp templates.

## Artefatos criados

PRD:

```text
/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/atendimento/prds/lk-chatwoot-whatsapp-template-builder-prd-20260603.md
```

Plano de implementação:

```text
/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/atendimento/plans/lk-chatwoot-whatsapp-template-builder-implementation-plan-20260603.md
```

## Próximo gate

Para implementar de verdade, precisa aprovação explícita de escopo:

1. criar branch/fork/custom image do Chatwoot;
2. implementar backend + UI + testes;
3. não deployar produção até approval packet com backup/rollback;
4. não criar template real na Meta até autorização de WABA/inbox/template específico.
