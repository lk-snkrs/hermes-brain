# Chatwoot WhatsApp Template Builder — Implementation Plan

> **For Hermes:** This plan is a safe implementation handoff. Do not deploy or mutate production Chatwoot without explicit Lucas approval, backup/rollback, and a controlled test inbox. Use code branch/fork first.

**Goal:** Add a safe Chatwoot UI/API for creating WhatsApp Business API templates directly from Chatwoot, submitting them to Meta for approval, syncing status, and making approved templates available to existing Chatwoot campaign/reply flows.

**Architecture:** Reuse Chatwoot's existing WhatsApp Cloud provider config and CSAT template creation path. Add a generic Rails service/controller with tests, then a settings UI/modal that calls the new API. Creation is an external Meta/WABA write, but it does not send customer messages.

**Tech Stack:** Chatwoot 4.14.x, Ruby on Rails, HTTParty, Vue dashboard, Vuex inbox store, Meta WhatsApp Business Management API.

---

## Current code evidence

Observed on LK Chatwoot self-hosted:

- `config/routes.rb`
  - existing nested inbox routes include `post :sync_templates` and `resource :csat_template`.
- `app/javascript/dashboard/api/inboxes.js`
  - existing methods: `syncTemplates`, `createCSATTemplate`, `getCSATTemplateStatus`.
- `app/javascript/dashboard/store/modules/inboxes.js`
  - existing getters/actions for WhatsApp template sync/listing.
- `app/services/whatsapp/csat_template_service.rb`
  - already posts to `#{business_account_path}/message_templates`.
- `app/services/whatsapp/providers/whatsapp_cloud_service.rb`
  - `sync_templates` fetches `/{business_account_id}/message_templates` and updates `channel.message_templates`.
  - `send_template` sends approved templates via phone number ID.
- `app/controllers/api/v1/accounts/inbox_csat_templates_controller.rb`
  - existing pattern for inbox-scoped template creation.

## Production gates

Before implementation touches production:

1. Confirm exact Chatwoot source/image strategy:
   - fork/source branch; or
   - custom Docker image; or
   - local monkey patch (not recommended).
2. Backup:
   - current compose/env redacted snapshot;
   - DB backup;
   - current image tag/version;
   - rollback command.
3. Confirm WhatsApp Cloud inbox exists and token permissions include template management. Likely permission needed: `whatsapp_business_management` in addition to send/read permissions.
4. Use an internal/test WABA or test inbox if possible.
5. Do not create customer-visible campaigns or send messages.

---

## Task 1 — Create backend request spec for validation failures

**Objective:** Define expected API behavior before implementation.

**Files:**

- Create: `spec/requests/api/v1/accounts/inbox_whatsapp_templates_controller_spec.rb`

**Steps:**

1. Add specs for:
   - rejects non-WhatsApp inbox;
   - rejects WhatsApp inbox whose provider is not `whatsapp_cloud`;
   - rejects missing name/category/language/body;
   - rejects invalid template name;
   - rejects variables without examples.
2. Use existing Chatwoot factories for account/user/inbox/channel.
3. Expected statuses:
   - `400` for invalid channel/provider;
   - `422` for invalid template payload;
   - `401/403` follows existing auth patterns.

**Verification:**

```bash
bundle exec rspec spec/requests/api/v1/accounts/inbox_whatsapp_templates_controller_spec.rb
```

Expected: failing tests before implementation.

---

## Task 2 — Add generic WhatsApp template creation service

**Objective:** Generalize the existing CSAT-only template creation into a generic reusable service.

**Files:**

- Create: `app/services/whatsapp/template_creation_service.rb`
- Test: `spec/services/whatsapp/template_creation_service_spec.rb`

**Service responsibilities:**

- Initialize with `whatsapp_channel`.
- Validate:
  - `Channel::Whatsapp`;
  - provider `whatsapp_cloud`;
  - `provider_config['api_key']` present;
  - `provider_config['business_account_id']` present.
- Build Meta payload:
  - `name`;
  - `category`;
  - `language`;
  - `parameter_format`, default `positional`;
  - `components`.
- POST to:

```ruby
"#{api_base_path}/v23.0/#{business_account_id}/message_templates"
```

- Use headers:

```ruby
{
  'Authorization' => "Bearer #{api_key}",
  'Content-Type' => 'application/json'
}
```

- Return normalized result:

```ruby
{
  success: true,
  template_id: response['id'],
  template_name: response['name'] || payload[:name],
  status: response['status'] || 'PENDING',
  language: payload[:language]
}
```

- On failure, return:

```ruby
{
  success: false,
  error: 'Template creation failed',
  response_body: redacted_response_body
}
```

**Important:** never log or return API token.

**Verification:**

```bash
bundle exec rspec spec/services/whatsapp/template_creation_service_spec.rb
```

Expected: service specs pass with stubbed HTTParty.

---

## Task 3 — Add payload validator/builder

**Objective:** Keep template payload construction deterministic and testable.

**Files:**

- Create: `app/services/whatsapp/template_payload_builder.rb`
- Test: `spec/services/whatsapp/template_payload_builder_spec.rb`

**MVP fields:**

```ruby
{
  name: 'lk_carrinho_abandonado_v1',
  category: 'MARKETING',
  language: 'pt_BR',
  parameter_format: 'positional',
  body: {
    text: 'Oi {{1}}, você deixou {{2}} no carrinho.',
    examples: ['Lucas', 'Nike Dunk Low']
  },
  footer: {
    text: 'LK Sneakers'
  },
  buttons: [
    {
      type: 'URL',
      text: 'Ver carrinho',
      url: 'https://lksneakers.com.br/cart/{{1}}',
      examples: ['abc123']
    }
  ]
}
```

**Builder output:**

```ruby
{
  name: 'lk_carrinho_abandonado_v1',
  category: 'MARKETING',
  language: 'pt_BR',
  parameter_format: 'positional',
  components: [
    {
      type: 'BODY',
      text: 'Oi {{1}}, você deixou {{2}} no carrinho.',
      example: { body_text: [['Lucas', 'Nike Dunk Low']] }
    },
    { type: 'FOOTER', text: 'LK Sneakers' },
    {
      type: 'BUTTONS',
      buttons: [
        {
          type: 'URL',
          text: 'Ver carrinho',
          url: 'https://lksneakers.com.br/cart/{{1}}',
          example: ['abc123']
        }
      ]
    }
  ]
}
```

**Validation rules:**

- name regex: `/\A[a-z0-9_]{1,512}\z/`
- category in `%w[MARKETING UTILITY AUTHENTICATION]`
- language present; default may be `pt_BR`.
- body text present.
- positional variables must be sequential from `{{1}}`.
- every variable needs one example.
- URL button variable needs example.

**Verification:**

```bash
bundle exec rspec spec/services/whatsapp/template_payload_builder_spec.rb
```

Expected: all builder specs pass.

---

## Task 4 — Add Rails controller and routes

**Objective:** Expose inbox-scoped API endpoints that mirror existing Chatwoot patterns.

**Files:**

- Create: `app/controllers/api/v1/accounts/inbox_whatsapp_templates_controller.rb`
- Modify: `config/routes.rb`

**Route shape:**

Inside `resources :inboxes ... do`:

```ruby
resource :whatsapp_templates, only: [:show, :create], controller: 'inbox_whatsapp_templates' do
  post :sync, on: :collection
end
get 'whatsapp_templates/:template_name/status', to: 'inbox_whatsapp_templates#status'
```

**Controller actions:**

- `show`: list cached templates from `@inbox.channel.message_templates`.
- `create`: validate, call `Whatsapp::TemplateCreationService`, trigger sync when possible, return created template result.
- `sync`: call existing `@inbox.channel.provider_service.sync_templates`.
- `status`: query Meta for one template or filter cached templates.

**Controller safety:**

- `before_action :fetch_inbox`.
- `authorize @inbox, :show?` or stricter policy if available.
- Validate `@inbox.channel.is_a?(Channel::Whatsapp)` and provider `whatsapp_cloud`.
- Do not expose provider_config.

**Verification:**

```bash
bundle exec rspec spec/requests/api/v1/accounts/inbox_whatsapp_templates_controller_spec.rb
```

Expected: request specs pass.

---

## Task 5 — Add frontend API methods

**Objective:** Give Vue components a clean API surface.

**Files:**

- Modify: `app/javascript/dashboard/api/inboxes.js`
- Test: `app/javascript/dashboard/api/specs/inboxes.spec.js`

**Add methods:**

```js
getWhatsappTemplates(inboxId) {
  return axios.get(`${this.url}/${inboxId}/whatsapp_templates`);
}

createWhatsappTemplate(inboxId, template) {
  return axios.post(`${this.url}/${inboxId}/whatsapp_templates`, { template });
}

syncWhatsappTemplates(inboxId) {
  return axios.post(`${this.url}/${inboxId}/whatsapp_templates/sync`);
}
```

**Verification:**

```bash
yarn test app/javascript/dashboard/api/specs/inboxes.spec.js
```

Expected: API tests pass.

---

## Task 6 — Add Vuex actions

**Objective:** Integrate template create/sync API with existing inbox store patterns.

**Files:**

- Modify: `app/javascript/dashboard/store/modules/inboxes.js`
- Test: `app/javascript/dashboard/store/modules/specs/inboxes/actions.spec.js`

**Add actions:**

- `createWhatsappTemplate({ inboxId, template })`
- `getWhatsappTemplates({ inboxId })`
- `syncWhatsappTemplates(inboxId)`

On create success, call sync or return result and let UI prompt refresh.

**Verification:**

```bash
yarn test app/javascript/dashboard/store/modules/specs/inboxes/actions.spec.js
```

Expected: store tests pass.

---

## Task 7 — Add UI MVP in Settings/Inboxes

**Objective:** Let admins create templates from the Chatwoot UI without entering the conversation composer.

**Files:**

Exact route file should be confirmed in source tree before editing. Candidate files:

- Create: `app/javascript/dashboard/routes/dashboard/settings/inbox/components/WhatsappTemplateBuilder.vue`
- Modify existing inbox settings component for WhatsApp channel.

**MVP UI fields:**

- Name.
- Category.
- Language default `pt_BR`.
- Body text.
- Body variable examples.
- Footer optional.
- One URL button optional.
- URL button example optional/required if variable exists.

**UI copy:**

- Warning for marketing category:
  - “Templates de marketing exigem consentimento/opt-in e aprovação Meta. Criar template não envia mensagem.”
- Warning for LK stock/promise:
  - “Não prometa estoque, prazo, preço ou desconto no template sem validação operacional.”

**Verification:**

- Manual in dev/staging:
  - invalid name blocks submit;
  - missing variable examples blocks submit;
  - successful API call returns pending status;
  - template appears after sync.

---

## Task 8 — Add audit table for submissions

**Objective:** Keep a safe audit trail for external Meta template asset creation.

**Files:**

- Create migration: `db/migrate/*_create_whatsapp_template_submissions.rb`
- Create model: `app/models/whatsapp_template_submission.rb`
- Test: model/request specs.

**Columns:**

- `account_id: bigint`
- `inbox_id: bigint`
- `user_id: bigint`
- `template_name: string`
- `language: string`
- `category: string`
- `status: string`
- `meta_template_id: string`
- `request_payload: jsonb`
- `response_payload: jsonb`
- timestamps

**Indexes:**

- `account_id, inbox_id`
- `template_name, language`

**Safety:**

- request/response payloads must not include `provider_config`, `api_key`, access tokens, or headers.

**Verification:**

```bash
bundle exec rails db:migrate RAILS_ENV=test
bundle exec rspec spec/models/whatsapp_template_submission_spec.rb
```

Expected: migration/model specs pass.

---

## Task 9 — End-to-end staging test

**Objective:** Prove creation works without customer-visible sends.

**Prerequisites:**

- Real or test WhatsApp Cloud inbox connected.
- Token with template management permission.
- Internal-only approval from Lucas for template asset creation.

**Test payload:**

```json
{
  "name": "lk_template_smoke_test_v1",
  "category": "UTILITY",
  "language": "pt_BR",
  "parameter_format": "positional",
  "body": {
    "text": "Olá {{1}}, este é um teste operacional da LK.",
    "examples": ["Lucas"]
  }
}
```

**Expected:**

- Meta returns template id/name/status.
- Status likely `PENDING`.
- No `/messages` API call occurs.
- No campaign created.
- No customer receives anything.

---

## Task 10 — Production deployment packet

**Objective:** Only deploy after code is tested and rollback exists.

**Packet must include:**

- branch/commit/image tag;
- files changed;
- tests passed;
- DB migration yes/no;
- backup commands/results;
- rollback commands;
- external effects:
  - creates template assets in Meta only when user submits UI;
  - no message sends;
- first controlled template and approval scope.

**Do not proceed to deploy until Lucas explicitly approves this packet.**

---

## Recommended MVP cut

For speed and safety, implement MVP as:

1. Backend API + tests.
2. No campaign sending.
3. Minimal Settings UI.
4. Only text BODY + optional footer + one URL button.
5. Audit row.
6. Controlled Meta submission of one internal/test template.

Avoid in MVP:

- media headers;
- named parameter support;
- authentication OTP templates;
- multi-language bulk creation;
- automatic campaign creation;
- automatic customer sending.

## Suggested first LK template copy

Use conservative wording, no stock/prazo/desconto promise:

```text
Oi {{1}}, vimos que você deixou alguns itens no carrinho da LK. Posso te ajudar a finalizar ou tirar alguma dúvida?
```

Suggested category: `MARKETING` unless legal/template policy determines it can be utility.

Suggested name: `lk_carrinho_ajuda_v1`

Suggested language: `pt_BR`
