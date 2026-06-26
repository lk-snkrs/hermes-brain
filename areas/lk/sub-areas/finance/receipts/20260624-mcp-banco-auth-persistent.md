# Receipt — MCP Banco auth persistente para LK Finance

- Data/hora: 2026-06-24T09:56:57.783544+00:00
- Agente/profile/cron: lk-finance
- Empresa/área: LK / Finance
- Responsável humano: LK Finance
- Pedido original: Persistir autenticação do Banco MCP/Open Finance para evitar perda em reconnect/idle/restart.
- Classificação: infra-sensitive
- Fontes usadas:
- Aprovação explícita do Lucas em Telegram; Doppler lc-keys/prd; config local do perfil lk-finance; teste real via hermes mcp test com Doppler injection.
- O que foi feito:
- Secret MCP_BANCO_AUTH_TOKEN gravado no Doppler sem imprimir valor; config.yaml do lk-finance atualizado para header Authorization com placeholder; mapa esperado do helper Doppler atualizado; skill Banco MCP atualizada com pitfall de sanitização.
- Output/artefato:
- MCP Banco testado com header persistente: 56 tools descobertas, 18 openfinance_*, balance tool disponível, acting_as owner, connected_count=4, pending_count=0. values_printed=false.
- Aprovação: Aprovado pelo Lucas: salvar MCP_BANCO_AUTH_TOKEN no Doppler e configurar lk-finance para header permanente.
- Envio/publicação: Telegram: resumo executivo; sem token/preview/dados bancários completos.
- Writes externos: Doppler secret write: MCP_BANCO_AUTH_TOKEN em lc-keys/prd. Nenhum banco/gateway/contabilidade write.
- Riscos/bloqueios: Token foi colado em chat; tratar como sensível e considerar rotação se Lucas quiser reduzir exposição histórica. Runtime atual pode precisar restart para carregar config no processo de gateway, mas config e Doppler já estão verificados.
- Rollback/mitigação: Remover MCP_BANCO_AUTH_TOKEN do Doppler ou restaurar backup /opt/data/profiles/lk-finance/config.yaml.bak-mcp-banco-auth-20260624T095229+0000; remover header Authorization do bloco banco.
- Próximos passos: Em próximo restart do lk-finance, validar tools Banco MCP diretamente no runtime; não reiniciei o gateway durante a resposta para não interromper Telegram.
- Onde foi documentado no Brain: Receipt sanitized criado; skill lk-finance/reference Banco MCP atualizada; helper hermes_doppler PROFILE_SECRET_MAP inclui MCP_BANCO_AUTH_TOKEN.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
