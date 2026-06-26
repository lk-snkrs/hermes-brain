# Evolution API -> Chatwoot guidance — LK Flagship

Timestamp: 2026-06-02 19:25:01 UTC

Context:
- Lucas asked how to connect Evolution API with Chatwoot to monitor conversations from instance `LK Flagship`.
- Screenshot shows Evolution API admin page: Integrations -> Chatwoot, with fields Chatwoot URL, Account ID, Token, Name Inbox, Organization, Logo, and toggles.
- Lucas pasted an Evolution API key in chat. Secret value intentionally not recorded here.

Guidance provided:
- Use Chatwoot URL `https://chat.lkskrs.online`.
- Use Chatwoot account ID `1` for LK Sneakers.
- Token field should be a Chatwoot user Application API access token from Chatwoot Profile Settings, not the Evolution API key.
- Recommended inbox name: `LK Flagship WhatsApp`.
- Recommended organization: `LK Sneakers`.
- Keep human-first guardrails: no IA/auto-replies/customer-visible automation by this integration alone.

External writes/actions:
- None executed by Hermes.

Open items:
- Lucas needs to paste the Chatwoot user access token into Evolution UI or provide explicit approval/scope for Hermes to configure it.
- After saving, verify that a Chatwoot inbox appears and a controlled inbound test message creates/updates a conversation.
