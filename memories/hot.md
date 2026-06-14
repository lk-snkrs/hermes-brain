# Memória quente — contexto current

Atualizado: 2026-06-14
Status: camada current compacta. Histórico/evidência fica em reports/receipts/daily, não aqui.

## Política de memória em vigor

- Fonte canônica: `memories/politica-memoria-hermes.md`.
- `MEMORY.md`/`USER.md` = boot mínimo; Brain/daily/hot/reports/receipts/skills/session_search = memória rica/continuidade.
- Provider externo/Mem0 = off até novo PRD/spike explícito.
- Dado vivo fica na fonte real; Brain guarda ponteiro, receipt/report e timestamp/incerteza.

## Prioridades current

1. Operar **Hermes Memory OS v1.18** em modo local/readiness/silent-OK: corrigir drift local antes de alertar Lucas.
2. Manter o checker `bc96bb03d2b0` a cada 30min com `deliver=origin` apenas porque o wrapper imprime stdout só quando há alerta acionável.
3. Receipts novos via `hermes_memory_os_receipt_writer.py`; workers legados via `hermes_memory_os_worker_receipt_guard.py` ou `--register-existing`; handoffs/approval packets via hook.
4. Aguardar maturação real de ciclos; não fabricar ciclos nem promover `mature` antes de 21/21 silent-OK reais.
5. Mission Control/card visual permanece fora do Memory OS e pendente para rodada dedicada.

## Bloqueios e guardrails current

- Sem Docker/VPS/Traefik/SSH/containers/volumes/gateway/restart sem aprovação escopada, backup/rollback e verificação.
- Sem writes externos em Shopify/Tiny/GMC/Klaviyo/Meta/WhatsApp/e-mail/banco/campanhas sem fonte e aprovação adequada.
- Sem tokens, secrets, payloads sensíveis ou localizadores de credencial em Telegram/docs versionáveis.
- Documentação de rotina não prova execução ativa; runtime precisa de evidência viva.

## Estado operacional quente

- Memory OS v1.17 concluído: contrato profile-local aplicado nos 9 especialistas vivos com backup e sem restart/runtime.
- Memory OS v1.18 em andamento/concluído nesta rodada: readiness read-only pós-rollout, com correção local de hot/daily após virada para 2026-06-10.
- Latest artefatos a consultar: `reports/memory-hygiene/latest.json`, `daytime-latest.json`, `scorecard-latest.json`, `adoption-latest.json`, `weekly-observability-latest.json`, `cycle-maturity-latest.json`.
- Readiness v1.18: `reports/governance/memory-os-v118-post-rollout-readiness-audit-20260609.md` e `reports/memory-hygiene/memory-os-v118-post-rollout-readiness-latest.json`.

## Links quentes

- Política: `memories/politica-memoria-hermes.md`
- PRD: `areas/operacoes/prds/hermes-memory-os-v1-prd-2026-06-09.md`
- Rotina: `areas/operacoes/rotinas/hermes-memory-os-v1.md`
- Daily atual: `memories/daily/2026-06-14.md`
- Watchdog latest: `reports/memory-hygiene/latest.json`
- Daytime latest: `reports/memory-hygiene/daytime-latest.json`
- Scorecard: `reports/memory-hygiene/scorecard-latest.json`
- Adoption linter: `reports/memory-hygiene/adoption-latest.json`
- Observabilidade semanal: `reports/memory-hygiene/weekly-observability-latest.json`
- Ciclos/maturidade: `reports/memory-hygiene/cycle-maturity-latest.json`
- Dashboard local/documental: `areas/operacoes/runtime/hermes-memory-os-dashboard.md`

## Próxima revisão

Se readiness v1.18 permanecer verde, o PRD volta para maturação por ciclos reais. Qualquer restart/gateway/Docker/VPS/Traefik/Mission Control/externo continua exigindo aprovação separada.
