# Receipt — Hermes Central Auth Broker — Linear integration removal

- Data/hora: 2026-06-28T16:51:48.473085+00:00
- Agente/profile/cron: Hermes default / operações runtime
- Empresa/área: Operações Hermes / Governança de integrações
- Responsável humano: Hermes Agent
- Pedido original: Lucas decidiu não usar Linear e pediu deletar a integração.
- Classificação: local-write
- Fontes usadas:
- Pedido direto de Lucas em Telegram; scripts /opt/data/scripts/hermes_cli_integrations.py e hermes_cli_run.py; testes unitários e smoke real.
- O que foi feito:
- Removi Linear do inventory/smoke central e removi alias lin/LINEAR_API_KEY do broker hermes-cli-run. Arquivei o approval packet de rotação Linear como stale/no-action.
- Output/artefato:
- Inventory/smoke central agora não lista Linear; demais integrações seguem OK. Report atualizado: reports/governance/hermes-central-integration-auth-broker-login-repair-2026-06-28.md.
- Aprovação: Aprovação direta atual de Lucas: “não vamos usar o LINEAR, pode deletar essa integracao”.
- Envio/publicação: Telegram: resumo final nesta conversa.
- Writes externos: 0
- Riscos/bloqueios: Skill genérica Linear permanece disponível no catálogo Hermes, mas a integração operacional central foi removida; qualquer reativação exige pedido explícito. Não apaguei nem alterei secrets no Doppler.
- Rollback/mitigação: Restaurar /opt/data/scripts/hermes_cli_integrations.py e hermes_cli_run.py a partir de /opt/data/backups/remove-linear-integration-20260628T164835Z/ e rerodar py_compile/testes/smoke.
- Próximos passos: Nenhum. Não renovar LINEAR_API_KEY e não alertar sobre Linear enquanto não houver reativação explícita.
- Onde foi documentado no Brain: areas/operacoes/receipts/hermes-central-auth-broker-linear-removal-20260628.md; report governança atualizado.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
