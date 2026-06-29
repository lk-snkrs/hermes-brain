# Honcho Nightly Intelligence Enforcement cron — 2026-06-29

## Pedido

Lucas pediu: adicionar no cron da madrugada um audit no Honcho e forçar todos os dias os agentes a usarem a inteligência dele.

## Implementação

Criado cron agent-driven diário:

- Job ID: `e3af978c6af6`
- Nome: `Honcho Nightly Intelligence Enforcement Audit — 02h35 BRT`
- Schedule: `35 5 * * *` UTC (`02h35 BRT`)
- Deliver: `local`
- Workdir: `/opt/data/hermes_bruno_ingest/hermes-brain`
- Skills carregadas:
  - `honcho-memory-operations`
  - `lucas-hermes-continuous-improvement`
  - `multiempresa-routing-lucas`
- Toolsets: `terminal`, `file`, `skills`, `session_search`, `memory`, `cronjob`
- Próxima execução: `2026-06-29T05:35:00+00:00`

## O que o cron força diariamente

1. O próprio cron deve usar Honcho antes de decidir, via contexto/busca/raciocínio de memória.
2. Audita `configured`, `active`, `functioning`, `protocol_aware` e `useful`.
3. Verifica todos os profiles em `/opt/data` e `/opt/data/profiles/*`:
   - `memory.provider=honcho`;
   - `honcho.json`;
   - skill local `honcho-memory-operations`;
   - blocos `HONCHO_USAGE_PROTOCOL_ENFORCEMENT` em `AGENTS.md`/`SOUL.md`;
   - session/AI peer/política sem expor IDs crus.
4. Roda auditorias sanitizadas:
   - all-agents Honcho audit se disponível;
   - quality auditor;
   - semantic contamination auditor;
   - cleanup candidate exporter;
   - gateway health;
   - contagem de erros recentes em logs Honcho sem imprimir logs crus.
5. Se algum profile perdeu protocolo, pode reparar localmente skill/AGENTS/SOUL com backup.
6. Não reinicia gateway/Docker/VPS/Traefik automaticamente; se precisar, gera approval packet.
7. Silent-OK: report local; Telegram só deve receber falha acionável em outro fluxo, não ruído.

## Guardrails

- Sem secrets, tokens, raw IDs, PII, raw content ou logs crus.
- Sem external writes.
- Sem delete Honcho.
- Sem restart automático sensível.
- Não agenda novos crons dentro do cron.

## Artefatos esperados por execução

- `reports/governance/honcho-nightly-intelligence-enforcement-YYYY-MM-DD.md`
- `reports/memory-hygiene/honcho-nightly-intelligence-enforcement-latest.json`
- Receipt local se houver correção material.

## Verificação

O job foi criado e está enabled/scheduled. `values_printed=false`.
