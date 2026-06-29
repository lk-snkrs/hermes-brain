# Receipt — Hermes Central Integration Auth Broker PRD e plano

- Data/hora: 2026-06-28T14:48:13.784752+00:00
- Agente/profile/cron: Hermes Agent default
- Empresa/área: Operações Hermes / Integrações
- Responsável humano: Hermes default
- Pedido original: Criar PRD para corrigir autenticação individual de agentes em Shopify CLI/MCP/CLI e centralizar logins/execução autenticada.
- Classificação: local-write
- Fontes usadas:
- Docs oficiais Hermes: profiles, configuration, MCP, credential pools, secrets, managed scope; Brain policy cli-mcp-first; receipts Shopify CLI OAuth/bridge; wrapper hermes-cli-run.
- O que foi feito:
- Criado PRD v1 e plano de implementação para Hermes Central Integration Auth Broker; nenhum runtime/gateway/secret/integração externa alterado; validado secret scan dos artefatos.
- Output/artefato:
- reports/governance/hermes-central-integration-auth-broker-prd-2026-06-28.md; areas/operacoes/implementation-plans/hermes-central-integration-auth-broker-2026-06-28.md
- Aprovação: Lucas aprovou seguir após pesquisa da solução nativa Hermes; implementação runtime/code continua exigindo aprovação escopada separada.
- Envio/publicação: Telegram final com resumo; silent-OK para artefatos locais.
- Writes externos: 0
- Riscos/bloqueios: PRD define mudanças futuras em broker/runtime; execução não realizada nesta etapa para evitar alteração sensível sem novo approval.
- Rollback/mitigação: Remover/reverter apenas os dois artefatos locais e este receipt se Lucas solicitar; nenhum estado externo ou auth foi modificado.
- Próximos passos: Se Lucas aprovar implementação runtime, executar Fase 1: backup, inventory/smoke read-only e drift report antes de alterar hermes_cli_run.py.
- Onde foi documentado no Brain: reports/governance/hermes-central-integration-auth-broker-prd-2026-06-28.md
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
