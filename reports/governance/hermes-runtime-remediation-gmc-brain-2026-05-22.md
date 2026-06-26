# Hermes runtime remediation — GMC/Brain continuation (2026-05-22)

## Context

Lucas pediu para continuar no GMC e corrigir o que estava errado no Brain/runtime para evitar problemas.

## Correções aplicadas

- Web tools: `web.backend` alterado de `firecrawl` para `tavily` no perfil principal e nos perfis Mordomo, LK Growth e SPITI.
- Credencial web: `TAVILY_API_KEY` materializada a partir do Doppler `lc-keys/prd` nos `.env` dos quatro perfis, sem imprimir segredo.
- Tavily provider: adicionado fallback seguro para ler apenas `TAVILY_API_KEY` de `HERMES_HOME/.env` quando o processo já está vivo e não herdou a env no startup.
- Perfis secundários: watchdogs agora neutralizam env herdada de API/webhook (`API_SERVER_*`, `WEBHOOK_*`) antes de subir Mordomo/LK Growth/SPITI.
- Perfis secundários: reinício drenado executado; API/webhook continuam somente no perfil principal.
- Bare `python`: prompt ativo do cron `f5a23dd6a1bd` corrigido para `python3`; não restaram jobs ativos com bare `python` detectável.
- Compressão: `auxiliary.compression` fixado para `openrouter` + `google/gemini-3-flash-preview` + timeout 180s nos quatro perfis para evitar timeouts/false positives do provedor auto.
- Skill Hermes runtime audit atualizado com o novo procedimento Tavily/Firecrawl e compressão.

## Verificações executadas

- Backups criados antes das alterações em `/opt/data/backups/hermes-audit-fix-20260522T122829Z`.
- `hermes config check`: OK para `/opt/data`, Mordomo, LK Growth e SPITI.
- Brain health check: `FAIL=0`, `WARN=0` em todos os buckets.
- Brain operating layer audit: branch `consolidation/brain-filesystem-git-hygiene-20260516`, allowlist funcionando.
- `brain_sync_safe.py --dry-run`: somente arquivos permitidos no conjunto allowed; bloqueios de scripts/config/json/csv/txt preservados.
- Tavily provider test via `/opt/hermes/.venv/bin/python`: search OK com 1 resultado; extract OK em `example.com` com conteúdo.

## Observações

- O gateway principal foi reiniciado após autorização explícita de Lucas para limpar cache/import state das ferramentas web.
- Logs antigos ainda contêm ocorrências históricas de Firecrawl Unauthorized, port conflict e `python: command not found`; a correção deve ser validada por ausência de novas ocorrências após o horário desta remediação.

## Verificação final pós-reinício — 2026-05-22T12:49:19Z

- `web_search`: sucesso no contexto da conversa após reinício do gateway principal (`success=true`).
- `web_extract`: sucesso no contexto da conversa após reinício do gateway principal, extraindo docs públicas do Hermes.
- Brain health: `All checks passed`, `FAIL=0`, `WARN=0`.
- Gateway principal e perfis secundários ativos: PID 7 principal + 3 gateways de perfil (`mordomo`, `lk-growth`, `spiti`).
- Compatibilidade `python`: `/opt/data/.local/bin/python --version` retornou Python 3.13.5.
- Watchdogs de ruído migrados para `deliver=local`: runtime/cron watchdog, compression self-heal, Mordomo gateway, LK Growth gateway, SPITI gateway.
- Varredura rápida de padrões sensíveis em áreas Brain encontrou apenas ocorrências benignas de documentação/regex/exemplos `sk-*`, não valores reais de chaves.
