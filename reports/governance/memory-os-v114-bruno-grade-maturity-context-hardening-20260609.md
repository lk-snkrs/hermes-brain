# Memory OS v1.14 — Bruno-grade recorrente, ciclos reais, context recovery e hardening legado

Gerado: 2026-06-09T19:59:50.412814+00:00

## Escopo executado

Lucas pediu executar em paralelo quatro frentes:

1. maturar por ciclos reais;
2. criar score Bruno-grade recorrente;
3. persistir melhor context recovery;
4. endurecer scripts legados para não depender só do auto-heal.

## Resultado executivo

- **Bruno-grade recorrente:** implementado no weekly observability com score 0–10 contra 7 blocos Bruno/OpenClaw.
- **Score atual:** 10/10, status `ok`.
- **Context recovery persistido:** implementado; `context-recovery-latest.json` e `context-recovery-events.jsonl` agora são atualizados a cada probe.
- **Ciclos reais:** implementado ledger persistente; não foram fabricados ciclos.
- **Estado atual de maturação:** `pilot_real_cycles`, score 100, 4 ciclos reais consecutivos silent-OK, faltam 17 para `mature`.
- **Scripts legados:** 4 scripts com escrita manual de receipt foram endurecidos para registrar evidência via writer/guard após escrever; 1 script já estava correto; candidatos ambíguos ficaram listados para revisão manual futura.

## Evidência viva pós-execução

- Weekly observability: `status=ok`, `findings=0`, `bruno_grade.score=10`, `bruno_grade.status=ok`.
- Context recovery: `status=ok`; latest persistido em `reports/memory-hygiene/context-recovery-latest.json`.
- Cycle maturity: `status=ok`, `level=pilot_real_cycles`, `score=100`, `consecutive_silent_ok_cycles=4`, `cycles_remaining_to_mature=17`.
- Adoption final pós-auto-heal: `status=ok`, `gap_count=0`, `drift_receipt_count=0`.
- Daytime: `status=ok`, `routes=0`, adoption gaps finais `0`.
- Alert wrapper: rc=0 e stdout 0 bytes quando saudável.

## O que mudou tecnicamente

### 1. Maturação por ciclos reais

Arquivo principal:

- `/opt/data/scripts/hermes_memory_os_cycle_maturity_probe.py`

Mudanças:

- adiciona `reports/memory-hygiene/cycle-maturity-ledger.json`;
- conta cada ciclo real por envelope de output do cron daytime;
- não cria ciclos sintéticos;
- usa 21 ciclos reais consecutivos silent-OK como critério de `mature`;
- integra ledger ao report `cycle-maturity-latest.json` e `.md`.

Também atualizado:

- `/opt/data/scripts/hermes_memory_os_daytime_alerting_watchdog.py`

Mudança:

- a cada execução de 30min, atualiza o probe/ledger de maturação sem imprimir nada quando OK.

### 2. Score Bruno-grade recorrente

Arquivo:

- `/opt/data/scripts/hermes_memory_os_weekly_observability.py`

Mudança:

- adiciona bloco `bruno_grade` ao `weekly-observability-latest.json`;
- score 0–10 por 7 blocos:
  1. caso real de negócio;
  2. segundo cérebro antes da autonomia;
  3. separação contexto/skills/rotinas;
  4. memória como continuidade, não dump;
  5. repetição promovida a skill/template/rotina;
  6. identidade/contrato de agentes;
  7. governança de permissões, secrets, crons, supervisão e alertas.

### 3. Context recovery persistido

Arquivo:

- `/opt/data/scripts/hermes_memory_os_context_recovery_probe.py`

Mudanças:

- grava sempre `reports/memory-hygiene/context-recovery-latest.json`;
- append em `reports/memory-hygiene/context-recovery-events.jsonl`;
- preserva silent-OK: sem stdout quando verde; `--json` imprime JSON parseável.

### 4. Hardening de scripts legados

Scripts endurecidos:

- `/opt/data/scripts/lk_trends_cloudflare_email.py`;
- `areas/lk/sub-areas/growth/receipts/gmc/missing-color-batch2-20260608T/finalize_readback.py`;
- `areas/lk/sub-areas/growth/receipts/gmc/missing-color-batch3-20260608T/run_batch3_api_input_only.py`;
- `areas/lk/sub-areas/growth/receipts/gmc/missing-color-batch4-20260608T/run_batch4_api_input_only.py`.

Já estava correto:

- `areas/lk/sub-areas/stock/scripts/gate_b2_run_remaining_shards.py`.

Candidatos deixados para revisão manual, sem patch automático:

- scripts que escrevem `ROLLBACK.md` dentro de diretórios de receipt;
- scripts que escrevem `receipt.json`, fora do contrato `.md` do writer;
- report `.md` com nome `*-receipt.md` fora de segmento `receipts/`.

## Limite honesto do item 1

A maturidade `mature` exige tempo real. O sistema agora conta ciclos reais automaticamente, mas não seria correto transformar 4 ciclos em 21 por execução manual. A próxima mudança de estado acontecerá naturalmente após novos ciclos do cron de 30min.

## Não-ações

- Sem Mission Control.
- Sem Docker/VPS/Traefik/gateway/restart.
- Sem provider externo/Mem0.
- Sem writes externos em Shopify/Tiny/GMC/Klaviyo/Meta/WhatsApp/e-mail/banco.
- Sem leitura/dump de conteúdo de receipts/handoffs/approval packets para score.
- Sem secrets impressos.
