# Receipt — Memory OS v1.19 final silent auto-heal contract

- Data/hora: 2026-06-10T12:43:35.185420+00:00
- Agente/profile/cron: Hermes default / Memory OS
- Empresa/área: Operações / Brain Governance
- Responsável humano: Hermes Agent
- Pedido original: Após adicionar context_auto_heal, alinhar o wrapper para que auto-heal local recuperado também fique silent-OK e não gere Telegram.
- Classificação: local-write
- Fontes usadas:
- Pedido de Lucas; hermes_memory_os_daytime_alerting_watchdog.py; hermes_memory_os_daytime_checker.py; verificação local.
- O que foi feito:
- Wrapper alterado para silenciar quando status final é ok, gaps=0 e auto-heal corrigiu itens locais; evidência permanece nos JSONs/receipts. Referência v1.19 atualizada para context/adoption drift healed => Telegram silencioso.
- Output/artefato:
- py_compile ok; alert wrapper rc=0 stdout_bytes=0; adoption linter ok gap_count=0 drift_receipt_count=0.
- Aprovação: Aprovado por Lucas: auto-heal no Memory OS e corrigir automaticamente sempre que seguro/local.
- Envio/publicação: Sem envio externo; apenas resumo Telegram neste turno.
- Writes externos: nenhum
- Riscos/bloqueios: Se auto-heal falhar ou sobrar rota acionável, Telegram continuará alertando. Não houve runtime/gateway/Docker/VPS/provider/business writes.
- Rollback/mitigação: Reverter bloco do wrapper que silencia auto-heal recuperado para voltar a imprimir mensagem recuperada.
- Próximos passos: Próximo cron deve ficar silencioso se estado continuar verde.
- Onde foi documentado no Brain: hermes-brain-governance reference v1.19 patched.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
