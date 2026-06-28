# Receipt — Correção da política CLI/MCP-first para integrações Hermes

- Data/hora: 2026-06-27T10:41:12.535463+00:00
- Agente/profile/cron: Hermes Geral / Brain Governance
- Empresa/área: Operações Hermes / Integrações
- Responsável humano: Hermes Geral; especialistas por Brain/AGENTS e futura onda de profile hardening quando aprovada
- Pedido original: Lucas corrigiu: CLI primeiro, depois MCP; perguntou se todos os agentes foram ensinados.
- Classificação: local-write
- Fontes usadas:
- Correção direta do Lucas em 2026-06-27; auditoria local de Brain e profiles por busca textual.
- O que foi feito:
- Renomeada e corrigida a rotina para cli-mcp-first-integration-policy.md; AGENTS.md, MAPA, índice de rotinas e skill mcp-connections atualizados para CLI primeiro, MCP segundo; memória durável e Honcho corrigidos; auditado que ainda existe exceção/conflito específico em lk-stock/Supabase MCP-first fora do pacote central.
- Output/artefato:
- areas/operacoes/rotinas/cli-mcp-first-integration-policy.md; AGENTS.md; areas/operacoes/MAPA.md; empresa/rotinas/_index.md; skill mcp-connections; memória user/Honcho; este receipt de correção.
- Aprovação: Ação local/documental e memória por correção explícita de Lucas; sem runtime/cron/gateway externo.
- Envio/publicação: Nenhum envio externo; resposta Telegram final somente resumo.
- Writes externos: 0
- Riscos/bloqueios: A política central foi corrigida, mas ensinar literalmente todos os agentes vivos exige onda separada por perfis isolados/skills/crons; não reiniciar runtime nem editar profile isolado sem escopo claro.
- Rollback/mitigação: Reverter rename/patches em AGENTS.md, MAPA.md, índice, skill mcp-connections e rotina; memória pode ser substituída se Lucas mudar a regra.
- Próximos passos: Se Lucas quiser cobertura 100%, executar auditoria/patch local por profile: AGENTS/MEMORY/skills/crons prompts, com backup, sem restart, e reportar exceções como lk-stock Supabase MCP-first.
- Onde foi documentado no Brain: true
- Source confidence: fonte-primária

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
