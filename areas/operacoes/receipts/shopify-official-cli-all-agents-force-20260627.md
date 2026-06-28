# Receipt — Shopify official CLI forced across agents

- Data/hora: 2026-06-27T15:33:27.145536+00:00
- Agente/profile/cron: Hermes Agent default
- Empresa/área: Operações Hermes / Shopify / agentes
- Responsável humano: Hermes default
- Pedido original: Forçar todos os agentes a usarem o Shopify CLI oficial após OAuth interativo.
- Classificação: local-write
- Fontes usadas:
- Shopify CLI OAuth oficial validado; profile AGENTS/SOUL; cron/jobs.json; scripts ativos LK Stock/Growth; skill Shopify; smoke read-only.
- O que foi feito:
- Propagada regra Shopify official CLI first para 59 instruction files, 28 cron jobs e skills relevantes; removido route hermes-cli-run shopify store execute -> shopify-admin-graphql; scripts ativos Shopify migrados para shopify store execute; enabled cron Shopify raw/wrapper gaps=0.
- Output/artefato:
- reports/governance/shopify-official-cli-all-agents-force-2026-06-27.md
- Aprovação: Pedido direto de Lucas: Agora force todos os agentes a usarem esse CLI.
- Envio/publicação: Resposta Telegram com resumo; crons permanecem silent-OK.
- Writes externos: 0
- Riscos/bloqueios: Sem restart de gateways; aplica a novas execuções por arquivos de contexto e prompts. OAuth oficial local pode expirar e deve ser renovado se quebrar.
- Rollback/mitigação: Restaurar /opt/data/backups/shopify-official-cli-force-20260627T151833Z; ou reverter arquivos modificados via git/backup. Nenhum estado externo Shopify foi alterado.
- Próximos passos: Opcional: restart controlado de gateways especialistas se Lucas quiser ativação imediata em processos já carregados.
- Onde foi documentado no Brain: reports/governance/shopify-official-cli-all-agents-force-2026-06-27.md
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
