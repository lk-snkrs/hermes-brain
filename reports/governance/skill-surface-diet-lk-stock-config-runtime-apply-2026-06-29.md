# Skill Surface Diet — lk-stock config/runtime apply

Data: 2026-06-29T15:19:23Z–2026-06-29T15:20:11Z UTC

## Escopo

Aplicação real da Skill Surface Diet no profile `lk-stock`, após escolha de Lucas para priorizar o P0 restante ligado ao incidente do webhook.

## Resultado

| Item | Resultado |
|---|---|
| Profile | `lk-stock` |
| Princípio | LK Stock = estoque/pronta entrega/Stock OS/Tiny/Inventory Hub first |
| Config migration | `_config_version: 27 → 30` |
| Skills totais lidas | 226 |
| Skills habilitadas no Telegram | 51 |
| Skills desabilitadas no Telegram | 175 |
| Skills protegidas desabilitadas | 0 |
| Runtime | gateway `lk-stock` reiniciado localmente |
| PID final verificado | `149655` |
| Telegram | `connected` |
| API server | disabled / não habilitado |
| Webhook | disabled / não habilitado |
| `DOPPLER_TOKEN` no processo | ausente (`values_printed=false`) |

## Core preservado

- `lk-stock`
- `lk-inventory-hub`
- `lk-operational-intelligence`
- `lk-shopify-readonly`
- `multiempresa-routing-lucas`
- `verification-before-completion`
- `superpowers`

## Proteções/lentes preservadas

- Honcho/Doppler/Auth Broker
- Supabase/MCP/read-only security ops
- Webhook troubleshooting/fast-ack
- Runtime/profile/gateway validation
- GitHub/Vercel/dashboard workflow
- Debug/TDD/review/worktree/QA visual
- Google Workspace/reporting quando ligado a estoque

## Fora do core no Telegram

ML training, gaming, creative/media ampla, ads/blog/SEO amplo, pesquisa acadêmica e skills genéricas ficam desabilitadas por `skills.platform_disabled.telegram`. Nenhuma skill foi deletada.

## Arquivos alterados

- `/opt/data/profiles/lk-stock/AGENTS.md`
- `/opt/data/profiles/lk-stock/skills/productivity/lk-stock/SKILL.md`
- `/opt/data/profiles/lk-stock/config.yaml`

## Backup

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/stock/backups/skill-surface-diet-apply-20260629T151923Z/`

Inclui versões anteriores de:

- `AGENTS.md`
- `lk-stock.SKILL.md`
- `config.yaml`
- `gateway_state.json`

## Verificações já realizadas

- `hermes config check` com `HERMES_HOME=/opt/data/profiles/lk-stock` → `Config version: 30 ✓`
- Gateway state → `running`, Telegram `connected`
- Processo vivo por `/proc` com `HERMES_HOME=/opt/data/profiles/lk-stock`
- API/webhook não habilitados no processo
- `skills.platform_disabled.telegram` com 175 entradas
- skills protegidas desabilitadas: 0
- QA independente: achou aplicação técnica OK, pediu receipt e relatório de apply para fechar; este relatório e o receipt atendem esse gap

## Não tocado

- Docker/VPS/Traefik/Main/default
- crons e rotas de webhook externas
- Tiny/Shopify/Supabase writes
- secrets ou valores de credenciais
- outros profiles

## Rollback

Restaurar os três arquivos do backup acima (`AGENTS.md.before`, `lk-stock.SKILL.md.before`, `config.yaml.before`) para seus caminhos originais e reiniciar somente o gateway `lk-stock` via `/opt/data/scripts/lk_stock_gateway_launcher.sh`. Para voltar ao estado runtime anterior, usar `gateway_state.json.before` apenas como evidência; não como fonte executável.
