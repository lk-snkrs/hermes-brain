# Receipt — CLI/MCP active cron fix

- Data/hora: 2026-06-27T13:29:07.158912+00:00
- Agente/profile/cron: Hermes Agent default
- Empresa/área: Operações Hermes / LK Stock / Mordomo
- Responsável humano: Hermes default
- Pedido original: Corrigir crons ativos que ainda usavam API raw após auditoria CLI-first/MCP-second.
- Classificação: local-write
- Fontes usadas:
- cron registries 11/11; scripts LK Stock Supabase, Shopify Sales OS, analytics; wrapper Hermes/Doppler; Supabase CLI readback; Shopify wrapper smoke; Brain health.
- O que foi feito:
- LK Stock Supabase cron convertido para gate readback via hermes-cli-run supabase db query --linked; Shopify Sales OS e analytics convertidos para wrapper CLI shopify-admin-graphql; skill/AGENTS LK Stock corrigidos para CLI-first/MCP-second; enabled external raw API gaps=0; values_printed=false.
- Output/artefato:
- reports/governance/cli-mcp-active-cron-fix-2026-06-27.md; /opt/data/scripts/shopify_admin_graphql_cli.py; cron/jobs.json e scripts atualizados.
- Aprovação: Pedido direto de Lucas: Corrigir. Nenhum write externo/prod executado; mudanças locais/documentais/scripts; cron Supabase agora não escreve Supabase.
- Envio/publicação: Telegram final somente com resumo; silent-OK preservado nos crons.
- Writes externos: 0
- Riscos/bloqueios: Shopify CLI oficial store execute ainda sem stored auth neste runtime; wrapper Hermes é fallback CLI governado. Full nightly Shopify reconcile não foi forçado para evitar backfill pesado.
- Rollback/mitigação: Restaurar arquivos de /opt/data/backups/cli-mcp-active-cron-fix-20260627T132053Z e remover symlink /opt/data/home/.local/bin/shopify-admin-graphql se necessário.
- Próximos passos: Opcional: configurar auth do Shopify CLI oficial store execute e migrar wrapper para delegar nele quando disponível.
- Onde foi documentado no Brain: reports/governance/cli-mcp-active-cron-fix-2026-06-27.md
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
