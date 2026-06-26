# LK Recovery OS — contact stitching patch deploy + PR27

Data: 2026-06-03
Status: `worker_deployed_pr_merged_sends_disabled_waiting_live_contact_stitch_evidence`

## Aprovação

Lucas aprovou: implementar e deployar patch de stitching `cart_token → Klaviyo profile → telefone`, mantendo dry-run/internal_only e sem ativar envios ao cliente.

## Escopo executado

- Patch no Worker para propagar contato recuperado (`phone_hash`, `phone_e164`, `email_hash`) para linhas do mesmo cluster:
  - `identity_links`
  - `identity_events`
  - `raw_events`
  - `recovery_candidates` pendentes/agendados
- Teste TDD novo:
  - `workers/recovery-os/tests/contact_propagation.test.ts`
- Métrica local/read-only do funil phone capture:
  - `scripts/lk_recovery_os_phone_capture_audit.py`
  - `tests/test_phone_capture_audit_script.py`
- Plano salvo:
  - `docs/plans/2026-06-03-phone-lead-capture-plan.md`

## Deploy

- Worker: `lk-recovery`
- Domínio: `https://recovery.lucascimino.com`
- Version ID: `ee1bed27-8183-4c9e-b5af-08a0e05a38ac`
- Schedule preservado: `*/10 * * * *`
- Shopify theme não alterado.
- Shopify/Klaviyo/Chatwoot/WhatsApp não alterados.

## Segurança pós-deploy

- `LK_RECOVERY_DRY_RUN=true`
- `LK_CHATWOOT_INTERNAL_ONLY=true`
- `LK_LIVE_SEND_ENABLED=false`
- `LK_WHATSAPP_SEND_ENABLED=false`
- `LK_EMAIL_SEND_ENABLED=false`
- `recovery_messages_total=0`
- `non_dry_run_messages=0`

Health verificado via curl:

- Worker `/healthz`: HTTP 200
- DB fallback `/healthz`: HTTP 200

## Verificação local

Antes e depois do commit/merge:

```bash
npm test
python3 tests/test_phone_capture_audit_script.py
git diff --check HEAD~1..HEAD
```

Resultado final em `main`:

- Worker tests: 10 arquivos / 52 testes passed.
- Python local audit test: `Ran 2 tests` / `OK`.
- Git status: `main...origin/main` clean.

## PR / merge

- Branch: `fix/phone-capture-stitching`
- Commit local: `c4cd0a8648e32729a1efeafa17cb0df68cbebf67`
- PR: `https://github.com/lk-snkrs/lk-recovery-os/pull/27`
- Combined status: success via Vercel.
- Check-runs endpoint retornou 403 para o PAT, então checks detalhados não foram listados via API; usei status combinado + gates locais.
- Merge: squash.
- Commit em `main`: `ce7601612a061990538e514be9e3f5fba7c209b9`
- Branch remota deletada via API; branch local deletada.

## Reaudit imediato pós-deploy

Como esperado, ainda não houve prova de novo join live após o deploy:

- `cart_clusters_with_phone_24h=0`
- `candidates_with_phone_24h=0`
- `candidates=125`
- `recovery_messages_total=0`

Interpretação: patch está implantado e testado, mas a métrica depende de novos eventos live onde telefone/klaviyo/cart caiam no mesmo cluster. Próxima validação deve aguardar novos eventos ou rodar um replay/backfill controlado separado, que exigiria aprovação por ser write de DB.

## Próximo gate recomendado

Monitorar por 30–120 min ou até novo evento relevante:

```bash
python3 scripts/lk_recovery_os_phone_capture_audit.py --hours 24 --run-ssh
```

Critério de avanço:

- `cart_clusters_with_phone > 0`
- `candidates_with_phone > 0`
- live sends ainda desligados até aprovação separada.
