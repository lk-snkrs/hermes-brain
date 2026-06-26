# Runtime Truth Reconciler — 2026-05-21

Timestamp UTC: 2026-05-21T11:20:49+00:00

## Escopo

Reconciliação read-only entre evidência viva de crons Hermes e documentação do Hermes Brain.

## Fonte viva consultada

1. `cronjob list` — indisponível neste shell (`command not found`).
2. Fallback canônico: `HERMES_HOME=/opt/data /opt/hermes/.venv/bin/hermes cron list --all` — executado com sucesso.

Não foram consultados Docker, VPS, Traefik, redes, containers, Shopify, GMC, Notion, WhatsApp, email, campanhas, bancos externos ou secrets.

## Resumo da evidência viva

- Total de jobs listados: 28.
- Ativos: 21.
- Pausados: 7.
- `last_status` não-ok: 1.
- Erros explícitos de delivery na listagem: 0.
- Jobs ativos sem `Last run`: 1.
- Jobs pausados sem `Last run`: 2.

## Anomalias / gaps acionáveis

1. `Hermes Brain Operating Layer structural watchdog` (`d03fa04e1188`) está ativo, mas o último run retornou erro: `Script exited with code 1`.
   - Saída reportada: falta a daily note de hoje `memories/daily/2026-05-21.md`.
   - Ação recomendada: criar/atualizar a nota diária pelo fluxo de memória/Fechamento, sem mexer em runtime.

2. `Lucas Brain weekly Learning Loop report` (`f4c499e85eac`) está ativo, mas ainda não tem `Last run` na listagem.
   - Interpretação: job semanal aguardando primeira execução registrada.
   - Ação recomendada: acompanhar após a próxima janela (`2026-05-25T12:15:00+00:00`).

3. Jobs pausados sem `Last run` que podem precisar de arquivamento/reconciliação documental futura:
   - `Mordomo: confirmar entrega com Seda Embalagens` (`527ee57b3a6b`) — one-shot antigo pausado.
   - `LK SEO/CRO impact review — SEO title/meta P1 packets` (`a7e883edd200`) — one-shot pausado sem execução registrada.

4. Drift de contagem em relação ao inventário anterior:
   - Snapshot anterior documentado: 26 jobs / 19 ativos / 7 pausados.
   - Snapshot vivo atual: 28 jobs / 21 ativos / 7 pausados.
   - Novos jobs observados na listagem atual que não apareciam no snapshot anterior do inventário: `LK WhatsApp Hermes responder regression watchdog` (`a5d7a392eed9`) e `Relatório Hermes diário 23h + 02h para Lucas` (`98478b820720`).

## O que não foi alterado

- Nenhum job foi executado manualmente.
- Nenhum schedule, delivery, prompt, script, profile ou config de cron foi alterado.
- Nenhum Docker/VPS/gateway/Traefik/rede/container foi alterado.
- Nenhum sistema externo, campanha, Shopify, GMC, Notion, WhatsApp, email, banco ou secret foi tocado.

## Arquivos de verificação

- Inventário atualizado: `areas/operacoes/inventarios/crons-agentes-profiles.md`.
- Health check JSON: `reports/brain-health-check-2026-05-21-runtime-truth-reconciler.json`.
