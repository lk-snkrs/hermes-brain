# Runtime Truth Reconciler — 2026-05-22

Data/hora da execução: 2026-05-22 11:20 UTC  
Escopo: Hermes Brain / crons Hermes / profiles documentados.  
Fonte viva: tentativa de `cronjob list` seguida de fallback canônico `HERMES_HOME=/opt/data /opt/hermes/.venv/bin/hermes cron list --all`.

## Resumo da evidência viva

- Total de jobs observados: **29**.
- Jobs ativos: **23**.
- Jobs pausados: **6**.
- `last_status` não-ok: **0** na listagem atual.
- Erros explícitos de delivery: **0** na listagem atual.
- `cronjob list` não está disponível como comando shell neste runtime; o fallback Hermes CLI funcionou.

## Anomalias e gaps acionáveis

1. **Drift de contagem/documentação**: snapshot anterior documentava `28 jobs / 21 ativos / 7 pausados`; evidência atual mostra `29 jobs / 23 ativos / 6 pausados`.
2. **LK GMC Review mudou de status vivo**: `LK GMC Review read-only mandatory delivery` (`d4c26da4cd48`) aparece **ativo** com último run `ok`, enquanto o inventário anterior ainda o descrevia como pausado em alguns trechos.
3. **Novo/recém-observado sem primeira execução registrada**: `Lembrete GMC Data Sources 10h` (`1d3a188b24f2`) está ativo, one-shot, delivery `origin`, ainda sem `Last run` na listagem.
4. **Job semanal ativo sem primeira execução registrada**: `Lucas Brain weekly Learning Loop report` (`f4c499e85eac`) permanece ativo, delivery `origin`, sem `Last run`; acompanhar após a primeira segunda-feira de execução.
5. **One-shots pausados sem execução registrada**: `Mordomo: confirmar entrega com Seda Embalagens` (`527ee57b3a6b`) e `LK SEO/CRO impact review — SEO title/meta P1 packets` (`a7e883edd200`) continuam candidatos a reconciliação/arquivamento documental futuro.
6. **Delivery `origin` em watchdogs silent-OK**: vários watchdogs ativos ainda usam `origin` (`Hermes runtime + cron watchdog no_agent`, `Hermes compression failure self-heal watchdog`, watchdogs de gateways Mordomo/LK Growth/SPITI, `Hermes Brain Operating Layer structural watchdog`, `LK WhatsApp Hermes responder regression watchdog`). Não houve erro nesta execução, mas a documentação deve manter a pendência de revisão de ruído vs. exceção.

## Notas de reconciliação

- O erro anterior do `Hermes Brain Operating Layer structural watchdog` não aparece mais na evidência atual: último run registrado está `ok`.
- Não foram inferidos jobs ativos a partir de documentação; somente a listagem viva foi usada para contagem/status.
- Nenhum schedule, delivery, prompt, script, profile, Docker/gateway, VPS, Traefik, rede, container, Shopify, GMC, Notion, WhatsApp, email, campanha, sistema externo ou secret foi alterado.

## Verificação final

- `python3 scripts/brain_health_check.py --json reports/brain-health-check-2026-05-22-runtime-truth-reconciler.json` executado.
- Resultado do health check: `FAIL=2 / WARN=0`, ambos em arquivos pré-existentes fora do escopo desta reconciliação:
  - `reports/lk-os-daily-sales-brief-2026-05-10.json` — padrão `openai`.
  - `reports/lk-os-daily-sales-brief-2026-05-10.md` — padrão `openai`.
- Secret scan restrito aos arquivos desta execução: `possible_secrets 0`.
- `git diff --check` nos arquivos desta execução: sem problemas.

## Arquivos atualizados nesta execução

- `areas/operacoes/inventarios/crons-agentes-profiles.md`
- `reports/governance/runtime-truth-reconciler-2026-05-22.md`
- `reports/brain-health-check-2026-05-22-runtime-truth-reconciler.json`
