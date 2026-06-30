# Receipt — Hermes Power-User Gap Audit Reddit benchmark 2026-06-29

- Data/hora: 2026-06-29T09:32:03Z
- Agente/profile/cron: Hermes Geral / Operações
- Empresa/área: Operações Hermes
- Responsável humano: Hermes Geral
- Pedido original: Fazer a auditoria do 1 ao 5 comparando o uso Lucas/Cimino do Hermes com o benchmark do post Reddit.
- Classificação: read-only
- Fontes usadas:
- Reddit post via web_extract/search; hermes status --all; /opt/data/profiles configs; /proc live gateway evidence; cronjob list; Brain governance docs.
- O que foi feito:
- Auditados os 5 eixos: software factory, bridge operacional, Task OS, skills/runtime cleanup e daily usage UX; produzido relatório executivo com notas e recomendações.
- Output/artefato:
- /opt/data/hermes_bruno_ingest/hermes-brain/reports/governance/hermes-power-user-gap-audit-reddit-2026-06-29.md
- Aprovação: Não exigida: auditoria read-only/local sem mudança de runtime, cron, gateway, Docker/VPS ou integração externa.
- Envio/publicação: Resumo enviado no Telegram; relatório salvo no Brain.
- Writes externos: nenhum
- Riscos/bloqueios: Relatório usa evidência atual read-only; post Reddit foi parcialmente acessado por extração/search, com fetch direto bloqueado por robots.txt.
- Rollback/mitigação: Não aplicável a runtime; para desfazer, arquivar/remover o relatório e este receipt local no Brain.
- Próximos passos: Decidir se segue com Workcell v1, Ops Bridge v1 read-only, Skill Surface Diet, Task OS minimalista e Telegram Executive UX v2.
- Onde foi documentado no Brain: /opt/data/hermes_bruno_ingest/hermes-brain/reports/governance/hermes-power-user-gap-audit-reddit-2026-06-29.md
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
