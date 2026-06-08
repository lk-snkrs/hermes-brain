# LK Content Telegram group config attempt — 2026-06-07

## Scope

Lucas approved configuring Telegram group `[LK] Produção de Conteúdo` as the shared LK Content chat.

## Target

- Group: `[LK] Produção de Conteúdo`
- chat_id: `-5235114444`
- Profile: `/opt/data/profiles/lk-content`

## Intended config

- `telegram.allowed_chats`: include `-5235114444`
- `telegram.group_allowed_chats`: include `-5235114444`
- `telegram.free_response_chats`: include `-5235114444`
- `telegram.require_mention`: `false`

## Result

Status: blocked/incomplete.

The config mutation was not applied because Hermes profile config and `.env` are protected security-sensitive files in this tool surface. Direct edits were refused by guardrails and no terminal/Hermes CLI execution tool was available in the active session/delegated worker.

## Non-actions

- No secrets read or printed.
- No profile config changed.
- No `.env` changed.
- No gateway restart performed.
- No external content/Klaviyo/Shopify/Tiny/Calendar/ads writes performed.

## Commands needed on host

Run with lk-content profile only:

```bash
export HERMES_HOME=/opt/data/profiles/lk-content
hermes config set telegram.allowed_chats '[-5235114444]'
hermes config set telegram.group_allowed_chats '[-5235114444]'
hermes config set telegram.free_response_chats '[-5235114444]'
hermes config set telegram.require_mention false
hermes gateway restart
```

Then verify:

```bash
export HERMES_HOME=/opt/data/profiles/lk-content
hermes config get telegram.allowed_chats
hermes config get telegram.group_allowed_chats
hermes config get telegram.free_response_chats
hermes config get telegram.require_mention
hermes gateway status
```

## External Telegram requirement

For ordinary group messages to reach Hermes, BotFather Privacy Mode must be off or the bot must be a group admin. If Privacy Mode is changed, remove and re-add the bot to the group.
