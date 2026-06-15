# Hermes Nightly Operations Audit OS — Matrix

Snapshot inicial: 2026-06-14/15  
Status: ativo como camada noturna 02h50 BRT, com Brain OS health/scanner às 02h25 BRT  
values_printed: false

## Matriz de auditoria

- **Memory OS**
  - Evidência: crons Memory OS, `reports/memory-hygiene/latest.json`, Memory OS daytime/weekly artifacts.
  - Bom: silent-OK, sem saturação/secret/provider issue não resolvido.
  - Ruim: over-limit, template coverage missing, stdout ruidoso sem ação, stale artifacts.
  - Autoheal A0/A1: compactação de escopo aprovado, refresh de `hot.md`/daily, receipts locais.
  - Aprovação: provider externo, restart, secrets.

- **Brain OS**
  - Evidência: Brain health, operational docs guard, scanner/hub reports, receipts.
  - Bom: health/docs green, hubs/indexes coerentes.
  - Ruim: FAIL/WARN real, docs ativos conflitantes, receipt inválido.
  - Autoheal A0/A1: índice/MAPA/routine local, receipt, JSON/report hygiene.
  - Aprovação: GitHub push fora de escopo, runtime, produção.

- **Mordomo OS**
  - Evidência: profile `mordomo` cron registry, scripts do profile, last_status, delivery.
  - Bom: watchers locais OK, origin apenas para alertas/digests aprovados.
  - Ruim: jobs origin ruidosos, auth externa quebrando canal independente, script ausente.
  - Autoheal A0/A1: correção local de parser/script seguro, artifacts/receipts.
  - Aprovação: WhatsApp pairing, envio, negociação, fornecedor, reclamação, preço/disponibilidade.

- **Stock OS / LK Stock**
  - Evidência: profile `lk-stock`, jobs Gate B, Tiny sync, Shopify Sales OS.
  - Bom: sync/reconcile fresh e read-only.
  - Ruim: `last_status=None` persistente, freshness stale, identity ambígua.
  - Autoheal A0/A1: diagnóstico local, report/receipt, fallback read-only permitido ao `lk-stock` quando aplicável.
  - Aprovação: Tiny/Shopify write.

- **LK Growth / SEO / GEO / Ranking**
  - Evidência: profile `lk-growth` crons, delivery watchdog, reports.
  - Bom: reports semanais/dia certos OK.
  - Ruim: origin delivery sem ação, jobs pausados com substituto não documentado.
  - Autoheal A0/A1: documentação, receipts, dedupe local.
  - Aprovação: Ads, GMC writes, Shopify writes, deploy.

- **LK Shopify / Product / PDP**
  - Evidência: profile `lk-shopify`, scripts, crons curator/reviews.
  - Bom: read-only monitors OK.
  - Ruim: jobs sem sucesso após janela esperada, script/path drift.
  - Autoheal A0/A1: path/script contract local e docs.
  - Aprovação: Shopify Admin write/theme/product mutation.

- **LK Ops / Atendimento / POS**
  - Evidência: profile `lk-ops`, POS canary/reconciler, Elle reports.
  - Bom: canary/reports dentro da janela, sem duplicação externa.
  - Ruim: origin spam, last_status None após janela real.
  - Autoheal A0/A1: relatório local, parser, idempotency local.
  - Aprovação: mensagens reais, reclamações, logística, negociação.

- **LK Content / Klaviyo**
  - Evidência: profile `lk-content`, planejamentos/radar/Klaviyo sent watchdog.
  - Bom: reports e watchdogs OK.
  - Ruim: sent watchdog não diferencia falha fonte vs script.
  - Autoheal A0/A1: local HTML/preview/doc/skill.
  - Aprovação: Klaviyo send/flow activation.

- **LK Trends**
  - Evidência: profile `lk-trends`, news/email delivery.
  - Bom: weekly news OK, email local/delivery OK.
  - Ruim: auth/delivery falha ou fallback indevido.
  - Autoheal A0/A1: report local, sanitizer, source refresh.
  - Aprovação: external send/new channel.

- **SPITI / SPITI Atendimento**
  - Evidência: profile crons/gateways, Brain/Hub docs.
  - Bom: no unexpected local productive crons unless approved.
  - Ruim: profile online/offline mismatch, unowned cron.
  - Autoheal A0/A1: docs/index/receipt.
  - Aprovação: customer/account external action.

- **Zipper OS**
  - Evidência: Zipper sales report, post-PDF watchdog, Mordomo/Zipper intake jobs.
  - Bom: email/WhatsApp channel separation, local artifacts.
  - Ruim: WhatsApp auth aborting email, duplicate lead follow-up, noisy origin.
  - Autoheal A0/A1: channel-local partial status, local receipts, parser fixes.
  - Aprovação: sending/contact/proposal/logistics.

- **Gateway/runtime watchdogs**
  - Evidência: `hermes_all_gateway_watchdog.py`, profile latency, runtime watchdog.
  - Bom: silent-OK, exact `HERMES_HOME`, API/webhook off where expected.
  - Ruim: missing required profile, wrong identity, stdout noise.
  - Autoheal A0/A1: allowlist/doc parity only when already approved and verified.
  - Aprovação: restart/activation/token/secrets.

## Daily scoring

- `ok`: no critical/attention; watchlist only.
- `attention`: active non-ok/stale or expected artifact missing.
- `action_required`: registry unreadable, script missing for active job, or sensitive boundary requiring Lucas.

## Digest integration

O digest das 03h deve ler `reports/nightly-ops-audit/latest.md` e incluir:

- status geral da auditoria;
- bom/ruim em linguagem humana;
- autoheal executado;
- decisões Lucas, se houver;
- sem job IDs/logs brutos no Telegram.
