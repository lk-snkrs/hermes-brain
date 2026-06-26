# Receipt — Cron diário saldo Itaú 10h BRT

- Data/hora: 2026-06-24T13:39:08.248545+00:00
- Agente/profile/cron: lk-finance
- Empresa/área: LK / Finance
- Responsável humano: LK Finance
- Pedido original: Enviar todo dia às 10h BRT o saldo do Itaú no Telegram.
- Classificação: infra-sensitive
- Fontes usadas:
- Pedido explícito do Lucas no Telegram; Banco MCP/Open Finance via Doppler/header persistente; Hermes cron do perfil lk-finance.
- O que foi feito:
- Criado script scripts/itau_daily_balance.py read-only e cron ativo Saldo Itaú diário 10h BRT com schedule 0 13 * * * UTC, equivalente a 10h BRT.
- Output/artefato:
- Script testado localmente com saldo verificado e sanitizado; cron list/status mostra 1 job ativo, próximo run 2026-06-25T13:00:00+00:00, deliver telegram, no-agent.
- Aprovação: Aprovado pelo Lucas por solicitação direta: precisa todo dia às 10h o saldo do Itaú.
- Envio/publicação: Telegram diário solicitado; somente saldo agregado e horários, sem conta/CNPJ/IDs/token.
- Writes externos: Nenhum write bancário/gateway/contabilidade. Write local de script/cron e receipt; leitura externa Open Finance apenas nos disparos.
- Riscos/bloqueios: Cron depende do gateway lk-finance ativo, MCP Banco conectado e Open Finance atualizado; falhas geram alerta sanitizado no Telegram.
- Rollback/mitigação: Pausar/remover job c18ab33ac8f0 via HERMES_HOME=/opt/data/profiles/lk-finance /opt/hermes/.venv/bin/hermes cron pause|remove c18ab33ac8f0; remover ou ajustar script se necessário.
- Próximos passos: Monitorar primeiro disparo em 2026-06-25 10h BRT; se houver falha, revisar MCP/Open Finance.
- Onde foi documentado no Brain: Receipt sanitizado criado no Brain; memória operacional do perfil atualizada.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
