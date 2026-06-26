# Receipt — Brain Sync reactivated on main

- Data/hora: 2026-06-26T10:26:31.672932+00:00
- Agente/profile/cron: Hermes Brain Governance
- Empresa/área: Operações / Hermes Brain
- Responsável humano: Hermes Geral
- Pedido original: Lucas aprovou aceitar PR estrutural e seguir passos 3, 4 e 5: trocar checkout operacional para main, rodar dry-run e reativar Brain Sync canônico.
- Classificação: external-write
- Fontes usadas:
- PR #149 mergeado; checkout /opt/data/hermes_bruno_ingest/hermes-brain; backup /opt/data/hermes_bruno_ingest/hermes-brain.backup-pre-main-switch-20260626T102451Z; brain_sync_safe.py.
- O que foi feito:
- PR #149 mergeado em main; checkout operacional antigo preservado como backup; clone main criado no caminho canônico; 64 arquivos allowlisted pós-cron restaurados; dry-run em main OK; Brain Sync --push executado em main.
- Output/artefato:
- GitHub main atualizado para b21a4edff7763e22b5a8e402fe0fcf0617f21625; working tree canônico limpo após sync; branch atual main.
- Aprovação: Aprovação escopada por Lucas no Telegram: 'Seguir, fazer o 2 depois 3 4 e 5' — aceitar PR estrutural, trocar checkout operacional para main, rodar dry-run e reativar sync canônico; sem Docker/VPS/Shopify/Tiny/runtime.
- Envio/publicação: Sem envio/publicação externa; evidência local no Brain.
- Writes externos: GitHub: merge PR #149 em main; push Brain Sync no main com 60 arquivos allowlisted. Nenhum runtime/Docker/VPS/Shopify/Tiny.
- Riscos/bloqueios: Backup do checkout antigo preserva arquivos skipped/não allowlisted; remover backup só após janela de validação. Gates históricos amplos ainda têm whitespace/health legados, mas sync canônico allowlist/secret scan passou.
- Rollback/mitigação: Resetar main para f89bcc0e864ee2c5cc45aa6a405c2306a86ddf47 ou reverter commit b21a4ed se necessário; restaurar diretório backup se precisar recuperar artefatos locais não allowlisted.
- Próximos passos: Monitorar próximo cron 04:00 UTC; depois de validar, remover backup antigo ou criar rotina de limpeza; abrir higiene separada para whitespace/JSON/health histórico.
- Onde foi documentado no Brain: areas/operacoes/receipts/brain-sync-main-reactivation-20260626.md; PR #149; reports/governance/brain-sync-correction-2026-06-26.md
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
