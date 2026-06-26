# Receipt — Google Workspace 2FA OAuth blocked access_not_configured

- Data/hora: 2026-06-18T10:10:01.349829+00:00
- Agente/profile/cron: Hermes Geral / Mesa COO
- Empresa/área: Zipper / Google Workspace
- Responsável humano: Hermes
- Pedido original: Lucas tentou autorizar OAuth read-only para resolver alerta 2FA Zipper e recebeu erro access_not_configured.
- Classificação: read-only
- Fontes usadas:
- Relato direto de Lucas no Telegram; Google OAuth error 400 access_not_configured for app N8N.
- O que foi feito:
- Registrado bloqueio e próximo caminho seguro sem executar Admin Console write.
- Output/artefato:
- OAuth app precisa ser revisado/permitido por Super Admin ou usar revisão manual no Admin Console.
- Aprovação: Sem aprovação para alterar Admin Console; somente orientação/read-only.
- Envio/publicação: Nenhum envio externo.
- Writes externos: 0
- Riscos/bloqueios: Permitir app com escopos Admin Reports/Directory deve ser feito por Super Admin; enforcement de 2FA continua separado.
- Rollback/mitigação: Não aplicável: nenhuma mudança executada.
- Próximos passos: Super Admin Zipper revisar/permitir app N8N/OAuth client ou extrair lista manual de usuários sem 2FA no Admin Console.
- Onde foi documentado no Brain: areas/zipper/receipts/20260618T101001Z-google-workspace-2fa-oauth-access-not-configured.md
- Source confidence: fonte-primária

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
