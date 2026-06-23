# Receipt — Hermes v0.17 complete adoption started

- Data/hora: 2026-06-22T11:01:39.341991+00:00
- Agente/profile/cron: hermes-geral/default
- Empresa/área: operacoes
- Responsável humano: Hermes Geral
- Pedido original: Lucas pediu adotar todas as melhorias do Hermes 0.17
- Classificação: local-write
- Fontes usadas:
- Release notes oficiais v2026.6.19; runtime probes locais; Doppler candidate presence probe
- O que foi feito:
- Criada PRD/adoption matrix; criada referência de skill; executados probes read-only de comandos, curator, MCP catalog/list, dashboard strict status e config key presence
- Output/artefato:
- PRD em areas/operacoes/prds/hermes-v017-adocao-completa-20260622.md; skill reference hermes-v017-complete-adoption-20260622.md; Onda 1 local iniciada
- Aprovação: Pedido estratégico de Lucas para adoção total; ações executadas limitadas a documentação/local/read-only sem Docker/VPS/Traefik/secrets/writes externos
- Envio/publicação: Telegram final conciso
- Writes externos: nenhum
- Riscos/bloqueios: Ativações de dashboard público, WhatsApp Cloud, Photon/iMessage, Raft, SimpleX, model default e infra ficaram bloqueadas para approval packets separados
- Rollback/mitigação: Remover PRD e skill reference criadas; nenhuma mudança runtime/externa realizada nesta etapa
- Próximos passos: Executar Onda 1 segura; preparar approval packets para Desktop/Dashboard, WhatsApp Cloud, Photon/iMessage, xAI/Grok e MCP expansion conforme prioridade de Lucas
- Onde foi documentado no Brain: areas/operacoes/prds/hermes-v017-adocao-completa-20260622.md; skill lucas-runtime-operations reference
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
