# LK-TRENDS — Gmail/Himalaya enablement plan

Status: partially enabled in live runtime.

Update 2026-05-31:
- Terminal is available.
- Himalaya v1.2.0 installed locally in the `lk-trends` profile.
- Config file created in both `/opt/data/home/.config/himalaya/config.toml` and the active profile home config path.
- Account `lk` is visible to Himalaya.
- Doppler has OAuth credentials for `lk@lksneakers.com.br` (`GMAIL_REFRESH_TOKEN_LK` verified by Gmail profile API), but the installed Himalaya binary lacks the `oauth2` cargo feature.
- Existing `GMAIL_APP_PASSWORD` exists but does not authenticate against `lk@lksneakers.com.br` via IMAP (`Invalid credentials`).
- Safe next path: either generate/store a Gmail App Password specifically for `lk@lksneakers.com.br`, install/build Himalaya with OAuth2 support, or use Gmail API OAuth for sending instead of Himalaya.
- Gmail API fallback executed after Lucas approval: message `19e7fc45424047f6`, verified `multipart/alternative`, HTML marker found, zero secret-pattern hits. Receipt: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/trends/newsletters/lk-trends-email-send-receipt-2026-05-31.md`.

## Goal
Send LK-TRENDS newsletters as visual HTML in the email body via Gmail SMTP/IMAP using Himalaya.

## Required inputs

1. Gmail account/sender to use. Proposed: `lk@lksneakers.com.br`.
2. Gmail App Password for this mailbox, or another secure secret source already available to the runtime.
3. Terminal/tool access in the Hermes runtime to install/check `himalaya`, write protected config, chmod secret file, send test, and verify MIME.

## Staged files

- Template: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/trends/newsletters/himalaya-gmail-setup-lk.template.toml`
- Email payload: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/trends/newsletters/lk-trends-email-send-payload-2026-05-31.json`
- Newsletter HTML: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/trends/newsletters/lk-trends-mapa-calor-newsletter-fonte-universo-2026-05-31.html`

## Commands to run once terminal is available

```bash
mkdir -p /opt/data/home/.config/himalaya
cp /opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/trends/newsletters/himalaya-gmail-setup-lk.template.toml /opt/data/home/.config/himalaya/config.toml
chmod 700 /opt/data/home/.config/himalaya
# Put Gmail app password into /opt/data/home/.config/himalaya/lk-gmail-app-password via secure secret channel, never chat/logs.
chmod 600 /opt/data/home/.config/himalaya/config.toml /opt/data/home/.config/himalaya/lk-gmail-app-password
himalaya account list
himalaya --account lk envelope list --page-size 1
```

## Send command pattern

Himalaya can send a piped MIME/template. For visual HTML body, construct a proper MIME message with `Content-Type: text/html; charset=utf-8`, then send via `himalaya template send`. After sending, verify the Sent message raw MIME includes the HTML body marker `LK-TRENDS — Mapa de calor internacional`.

## Guardrail

Do not send unless Lucas has approved recipient and payload in the current turn. Current approval exists for: `lk@lksneakers.com.br`, subject `LK-TRENDS — Mapa de Calor Internacional`, visual HTML body.
