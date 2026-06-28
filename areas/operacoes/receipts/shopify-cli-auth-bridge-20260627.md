# Receipt — Shopify CLI auth bridge

- Data/hora: 2026-06-27T14:10:45.312431+00:00
- Agente/profile/cron: Hermes Agent default
- Empresa/área: Operações Hermes / Shopify / LK Stock
- Responsável humano: Hermes default
- Pedido original: Adicionar auth da Shopify para uso CLI-first sem raw API em crons/agentes.
- Classificação: local-write
- Fontes usadas:
- Doppler lc-keys/prd via hermes_doppler.py; hermes-cli-run; shopify-admin-graphql wrapper; smoke read-only Shopify shop query.
- O que foi feito:
- Adicionado mapeamento de auth Shopify no hermes_cli_run.py; shopify store execute agora roteia para wrapper CLI Doppler-first em runtime não-interativo; redaction Shopify reforçado; mutações bloqueadas por padrão; cache manual removido/redigido.
- Output/artefato:
- reports/governance/shopify-cli-auth-bridge-2026-06-27.md; /opt/data/scripts/hermes_cli_run.py
- Aprovação: Pedido direto de Lucas: adicionar auth da Shopify. Sem write externo; sem mutação Shopify; sem alteração runtime/gateway.
- Envio/publicação: Telegram final com resumo; crons continuam silent-OK.
- Writes externos: 0
- Riscos/bloqueios: Shopify store auth OAuth oficial continua exigindo browser/callback interativo; ponte atual usa Doppler-first process scoped auth.
- Rollback/mitigação: Reverter /opt/data/scripts/hermes_cli_run.py para versão anterior ou remover aliases/route Shopify; nenhum estado externo a reverter.
- Próximos passos: Opcional: fazer OAuth interativo oficial do Shopify CLI se Lucas quiser store auth nativo persistido.
- Onde foi documentado no Brain: reports/governance/shopify-cli-auth-bridge-2026-06-27.md
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
