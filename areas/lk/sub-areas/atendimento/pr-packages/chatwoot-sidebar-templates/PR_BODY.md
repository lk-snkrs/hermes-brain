# PR — Chatwoot Sidebar Templates WhatsApp/META

## Summary

- Adds a top-level **Templates** item to the Chatwoot sidebar.
- Adds `/app/accounts/:accountId/templates` route and page.
- Lists WhatsApp Cloud templates grouped by inbox/WABA source.
- Exposes reload and Meta sync actions using the existing WhatsApp template endpoints.
- Includes a guarded new-template form that submits templates for Meta approval but does not create campaigns or send customer messages.
- Adds EN/PT translations for sidebar and page copy.

## Changed files

- `app/controllers/api/v1/inboxes/whatsapp_templates_controller.rb`
- `app/javascript/dashboard/api/inboxes.js`
- `app/javascript/dashboard/components-next/sidebar/Sidebar.vue`
- `app/javascript/dashboard/i18n/locale/en/settings.json`
- `app/javascript/dashboard/i18n/locale/pt/settings.json`
- `app/javascript/dashboard/routes/dashboard/dashboard.routes.js`
- `app/javascript/dashboard/routes/dashboard/settings/inbox/settingsPage/ConfigurationPage.vue`
- `app/javascript/dashboard/routes/dashboard/templates/TemplatesPage.vue`
- `app/javascript/dashboard/routes/dashboard/templates/templates.routes.js`
- `app/javascript/dashboard/store/modules/inboxes.js`
- `config/routes.rb`
- backend/frontend specs for template API/actions

## Verification

Executed locally in `/opt/data/lk-chatwoot-prod-source`:

```bash
corepack pnpm exec eslint app/javascript/dashboard/routes/dashboard/templates/TemplatesPage.vue app/javascript/dashboard/routes/dashboard/templates/templates.routes.js app/javascript/dashboard/routes/dashboard/dashboard.routes.js app/javascript/dashboard/components-next/sidebar/Sidebar.vue
```

Result: exit code 0.

```bash
corepack pnpm exec vite build
```

Result: exit code 0. Build succeeded; only standard large chunk warnings.

```bash
git diff --check b961e64..HEAD
```

Result: exit code 0.

## Safety / guardrails

- No production deploy included.
- No live Meta API call executed during implementation.
- No WhatsApp send or campaign creation.
- No Shopify/Tiny writes.
- Template creation is an external Meta/WABA asset write and should remain approval-gated in operations.

## Notes

This local source snapshot currently has no Git remote configured, so no GitHub push/PR was executed from Hermes. Patch package was generated locally for review/application in the canonical repository.
