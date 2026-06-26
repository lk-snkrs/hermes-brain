# Receipt — Regra UI Stock OS endereçável por link

- Data/hora: 2026-06-25T16:40:53.268607+00:00
- Agente/profile/cron: Hermes Agent default
- Empresa/área: LK / Stock OS / UI
- Responsável humano: lk-stock
- Pedido original: Lucas corrigiu por voz que toda página/tela alterada precisa ter HTML/rota/link direto para busca automática e validação por link.
- Classificação: local-write
- Fontes usadas:
- Mensagem de voz de Lucas em 2026-06-25; skill lk-stock; AGENTS.md do Stock OS.
- O que foi feito:
- Aplicada regra durável em duas superfícies: skill lk-stock/reference do dashboard e areas/lk/sub-areas/stock/AGENTS.md. Regra exige rota canônica, HTML/IDs estáveis, smoke/DOM/screenshot via URL final e bloqueia reportar UI como pronta sem link direto.
- Output/artefato:
- Skill contém Link-addressable page rule; AGENTS contém Regra obrigatória — UI Stock OS precisa ser endereçável por link.
- Aprovação: Pedido direto de Lucas: Aplicar.
- Envio/publicação: Telegram final para Lucas
- Writes externos: 0
- Riscos/bloqueios: Baixo; mudança de procedimento. Backup criado antes de editar AGENTS.
- Rollback/mitigação: Backup /opt/data/hermes_bruno_ingest/hermes-brain/.hermes/backups/stock-agents-link-addressable-20260625T163946Z.md; skill pode ser revertida por patch removendo a seção.
- Próximos passos: Nas próximas mudanças UI, começar pelo link/rota canônica e validar diretamente por URL.
- Onde foi documentado no Brain: areas/lk/sub-areas/stock/AGENTS.md e skill lk-stock reference stock-dashboard-impeccable-topology-rebuild-pattern-20260622.md.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
