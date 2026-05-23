# Hermes runtime audit — 2026-05-22

Status: **read-only audit + Brain receipt**. Nenhum Docker, gateway, cron, config, segredo, GMC, Shopify ou integração externa foi alterado.

## Escopo verificado

- Runtime principal Hermes em `/opt/data`.
- Perfis Telegram secundários: Mordomo, LK Growth e SPITI.
- Processos `hermes gateway run` por `HERMES_HOME` real via `/proc`.
- API local `/health`.
- Logs recentes dos perfis, sem preservar segredos.
- Crons/registries em `/opt/data/**/cron/jobs.json`.
- Watchdogs principais: runtime cron watchdog, Brain operating layer audit e LK WhatsApp responder selftest.
- Brain health, git diff check e safe sync dry-run.

## Evidência de saúde

- Hermes: `v0.14.0 (2026.5.16)`; config path principal `/opt/data/config.yaml`.
- Ambiente: Docker/container detectado; `/opt/hermes/.git` ausente, coerente com imagem/runtime instalado.
- Gateway principal: rodando.
- Gateways por perfil, contagem exata por `HERMES_HOME`:
  - `/opt/data`: 1 processo.
  - `/opt/data/profiles/mordomo`: 1 processo.
  - `/opt/data/profiles/lk-growth`: 1 processo.
  - `/opt/data/profiles/spiti`: 1 processo.
  - Duplicates: nenhum.
  - Missing: nenhum.
  - Unexpected: nenhum.
- API local: `GET http://127.0.0.1:8642/health` retornou 200 `{"status":"ok","platform":"hermes-agent"}`.
- Disco: `/opt/data` com ~17% usado.
- Memória: ~31 GiB total, ~23 GiB disponível.
- Brain health: `FAIL=0`, `WARN=0`, `All checks passed`.
- Operating layer audit: exit 0, stdout vazio.
- `git diff --check`: OK.
- `brain_sync_safe.py --dry-run`: OK; branch `consolidation/brain-filesystem-git-hygiene-20260516`.

## Achados

### P0 — nenhum achado crítico imediato

Não encontrei gateway morto, duplicidade real de gateway, falta de disco/memória, Brain quebrado, secret leak no relatório ou API health local fora.

### P1 — Web search / web extract quebrados por Firecrawl unauthorized

Evidência:

- `web_search("Hermes Agent NousResearch")` falhou com `Firecrawl search failed: Unauthorized: Invalid token`.
- `web_extract("https://example.com")` falhou com `Unauthorized: Failed to scrape. Unauthorized: Invalid token`.
- Logs dos perfis também repetem `Firecrawl search error: Unauthorized`.

Impacto:

- Pesquisa web e extração web do Hermes ficam indisponíveis ou intermitentes quando o backend escolhido é Firecrawl.
- Isso afeta auditorias, SEO, Growth, SPITI e tarefas que dependem de web live.

Provável causa:

- `FIRECRAWL_API_KEY` está presente, mas inválida/expirada/rejeitada pelo provedor; não foi impressa nem preservada.

Correção segura proposta:

1. Validar/fazer rotação da chave Firecrawl em Doppler/runtime sem imprimir segredo.
2. Alternativamente configurar backend secundário de busca/extract, se disponível.
3. Verificar com `web_search` e `web_extract` simples.
4. Reiniciar somente o runtime necessário se a variável for lida no startup.

### P1 — perfis secundários estão herdando `API_SERVER_*` e `WEBHOOK_*` do ambiente principal

Evidência live por `/proc/<pid>/environ`:

- Mordomo, LK Growth e SPITI estão com:
  - `WEBHOOK_ENABLED=true`
  - `WEBHOOK_PORT=8644`
  - `API_SERVER_ENABLED=true`
  - `API_SERVER_PORT=8642`
  - `API_SERVER_HOST=0.0.0.0`
- Os logs dos três perfis registram conflito de webhook: `Port 8644 already in use`, seguido de pausa do webhook após falhas.
- Os arquivos `.env` dos perfis indicam intenção diferente para API server (`API_SERVER_ENABLED=false` e portas vazias), mas o processo vivo herdou o ambiente do supervisor/gateway principal.

Impacto:

- Não parece derrubar o Telegram dos perfis, porque os gateways estão vivos.
- Porém gera erro recorrente, ruído em logs e risco de superfície indevida caso algum perfil consiga abrir API/webhook em ambiente futuro.

Provável causa:

- Watchdogs de gateway dos perfis exportam `HERMES_HOME`, mas não limpam variáveis herdadas `API_SERVER_*`/`WEBHOOK_*`; o processo pai já tem essas vars setadas.

Correção segura proposta:

1. Patch nos launchers/watchdogs dos perfis para iniciar com ambiente limpo ou explicitamente:
   - `API_SERVER_ENABLED=false`
   - unset/empty `API_SERVER_KEY`, `API_SERVER_PORT`, `API_SERVER_HOST`
   - `WEBHOOK_ENABLED=false`
   - unset/empty `WEBHOOK_PORT`, `WEBHOOK_SECRET`
2. Não reiniciar imediatamente no meio de sessões ativas.
3. Em janela segura, restart drenado apenas dos perfis secundários.
4. Verificar `/proc/<pid>/environ` pós-restart e ausência de `Port 8644 already in use` novo.

### P2 — `python` não existe no PATH; só `python3`

Evidência:

- `command -v python` não retornou caminho.
- `command -v python3` retornou `/usr/bin/python3`.
- Logs mostram múltiplas falhas `/usr/bin/bash: line N: python: command not found`, especialmente Mordomo e LK Growth.

Impacto:

- Agentes/crons que geram comandos com `python` falham até se autocorrigirem para `python3`.
- Um cron recorrente do Mordomo (`Zipper Gmail draft engine — safe draft-only`) teve falhas desse tipo nos logs, embora `last_status=ok` no registry.

Correção segura proposta:

- Preferir corrigir prompts/scripts recorrentes para `python3` ou `/opt/hermes/.venv/bin/python`.
- Não criar symlink global `/usr/bin/python` sem avaliar impacto da imagem/container.

### P2 — eventos de compressão/context summary ainda aparecem, mas com fallback

Evidência:

- Logs recentes têm `Bad file descriptor`, `record layer failure`, `PEM lib` e timeout de auxiliary compression.
- Também há fallback para OpenRouter/Gemini após falha do Codex auxiliary.

Impacto:

- Pode degradar/pausar resumo de contexto por janelas curtas.
- Não observei falha fatal do gateway nessa auditoria.

Correção/monitoramento:

- Manter watchdog de self-heal de compressão ativo.
- Se repetir em alta frequência, aplicar o playbook `context-compression-transient-retry` e testes direcionados.

### P2 — memória de alguns perfis está cheia/limite apertado

Evidência:

- Logs mostram várias falhas `Memory at ... would exceed the limit` / `Replacement would put memory at ...`.

Impacto:

- Fatos duráveis podem deixar de ser salvos e gerar loops de ferramenta.

Correção segura proposta:

- Curadoria/compactação de memória por perfil, sem aumentar limite cegamente.

### P3 — Telegram fallback recorrente

Evidência:

- Logs mostram `api.telegram.org connection failed`, com fallback IP sticky.

Impacto:

- Degradação de rede/Telegram, mas o fallback está funcionando.

Ação:

- Monitorar; não requer correção Hermes imediata.

## Crons e watchdogs pós-mudança

- Watchdog runtime manual verbose: OK; 4 gateways esperados; sem duplicados.
- Brain operating layer audit: silent OK.
- LK WhatsApp responder selftest: silent OK.
- Mudança anterior de ruído preservada:
  - `d03fa04e1188`: `deliver=local`.
  - `a5d7a392eed9`: `deliver=local`.

Observações:

- Há jobs one-shot futuros com `last_status=None`; isso é esperado antes da primeira execução.
- O perfil SPITI não possui `cron/jobs.json`; isso não é erro se o perfil não usa scheduler próprio.

## Recomendações por prioridade

1. **Corrigir Firecrawl**: web tools estão objetivamente quebradas agora.
2. **Corrigir launch env dos perfis secundários**: evitar herança de API/webhook do Hermes principal.
3. **Reduzir falhas `python` vs `python3`** em crons/prompts recorrentes.
4. **Curar memória dos perfis** para reduzir loops de `memory` failed.
5. **Monitorar compressão**; agir se o self-heal voltar a alertar.

## Limite desta rodada

Nenhuma alteração operacional foi feita nesta auditoria. As correções propostas que envolvem secrets, env de gateway ou restart devem ser aplicadas com escopo e rollback explícitos.
