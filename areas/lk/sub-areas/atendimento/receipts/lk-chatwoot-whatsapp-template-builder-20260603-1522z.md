# LK Chatwoot — WhatsApp Template Builder local customization

Data UTC: 2026-06-03 15:22Z
Workspace: `/opt/data/lk-chatwoot-prod-source`
Branch: `lk/whatsapp-template-builder`
Status: local implementation verified; no production deploy.

## Escopo aprovado

Lucas aprovou seguir com a customização local do Chatwoot para criar um MVP de gerenciamento/criação de templates WhatsApp Cloud dentro de Settings/Inboxes.

## O que foi implementado

Backend:
- `app/services/whatsapp/template_payload_builder.rb`
  - monta payload para Meta WhatsApp Business Management API;
  - valida nome, categoria, idioma, body, variáveis posicionais sequenciais e exemplos.
- `app/services/whatsapp/template_creation_service.rb`
  - chama `POST https://graph.facebook.com/v23.0/{business_account_id}/message_templates`;
  - usa `provider_config['api_key']` e `provider_config['business_account_id']`;
  - redige token em erro.
- `app/controllers/api/v1/accounts/inbox_whatsapp_templates_controller.rb`
  - `show`, `create`, `sync`;
  - restringe operações a `Channel::Whatsapp` com provider `whatsapp_cloud`.
- `config/routes.rb`
  - rotas account/inbox para `whatsapp_templates`.

Frontend/API/store:
- `app/javascript/dashboard/api/inboxes.js`
  - `getWhatsAppTemplateStatus`, `createWhatsAppTemplate`, `syncWhatsAppTemplates`.
- `app/javascript/dashboard/store/modules/inboxes.js`
  - actions Vuex correspondentes.
- Specs atualizadas para API/store.

Frontend UI mínima:
- `app/javascript/dashboard/routes/dashboard/settings/inbox/settingsPage/ConfigurationPage.vue`
  - seção visível apenas para WhatsApp Cloud;
  - formulário MVP com nome, categoria, idioma, body, exemplos, footer e botão URL opcional;
  - botão para enviar template para aprovação na Meta;
  - botão para sincronizar/listar templates carregados.

## Verificações realizadas

Backend syntax + testes auxiliares em container `chatwoot/chatwoot:latest`:
- `ruby -c app/services/whatsapp/template_payload_builder.rb` → Syntax OK
- `ruby -c app/services/whatsapp/template_creation_service.rb` → Syntax OK
- `ruby -c app/controllers/api/v1/accounts/inbox_whatsapp_templates_controller.rb` → Syntax OK
- `ruby -c config/routes.rb` → Syntax OK
- `ruby test_whatsapp_template_payload_builder.rb` → 3 runs, 11 assertions, 0 failures
- `ruby test_whatsapp_template_creation_service.rb` → 2 runs, 13 assertions, 0 failures

Rails routes:
- `GET /api/v1/accounts/:account_id/inboxes/:inbox_id/whatsapp_templates`
- `POST /api/v1/accounts/:account_id/inboxes/:inbox_id/whatsapp_templates`
- `POST /api/v1/accounts/:account_id/inboxes/:inbox_id/whatsapp_templates/sync`

Frontend:
- `corepack pnpm install --frozen-lockfile` concluído; warning de engine Node esperado (`package.json` pede Node 24.x; host tinha Node 20.19.2).
- `corepack pnpm exec vitest run app/javascript/dashboard/api/specs/inboxes.spec.js app/javascript/dashboard/store/modules/specs/inboxes/actions.spec.js` → 2 files passed, 30 tests passed.
- `corepack pnpm exec eslint app/javascript/dashboard/api/inboxes.js app/javascript/dashboard/api/specs/inboxes.spec.js app/javascript/dashboard/store/modules/inboxes.js app/javascript/dashboard/store/modules/specs/inboxes/actions.spec.js app/javascript/dashboard/routes/dashboard/settings/inbox/settingsPage/ConfigurationPage.vue` → exit 0.

Warnings observados:
- Vite CJS API deprecated.
- Browserslist/caniuse-lite outdated.
- Rails secrets deprecation warnings durante `rails routes`.

## Segurança / não feito

Não foi feito:
- deploy em produção;
- rebuild/restart do Chatwoot produtivo;
- alteração no container produtivo;
- criação real de template na Meta/WABA;
- envio de WhatsApp;
- alteração em inbox/credenciais externas.

## Próximos passos antes de produção

1. Commit local da implementação.
2. Approval packet para build/deploy de imagem customizada, incluindo rollback.
3. Teste manual em ambiente controlado antes de produção, porque o botão `Enviar para aprovação na Meta` é write externo real quando a UI estiver deployada.
4. Só criar template real com aprovação explícita do texto/categoria/variáveis e do WABA/inbox alvo.
