# Receipt — Política CLI/MCP-first para integrações Hermes

- Data/hora: 2026-06-27T10:27:40.679142+00:00
- Agente/profile/cron: Hermes Geral / Brain Governance
- Empresa/área: Operações Hermes / Integrações
- Responsável humano: Hermes Geral; todos os agentes Hermes por herança de AGENTS/Brain
- Pedido original: Lucas definiu: ensinar os agentes Hermes a sempre usar MCP ou CLI, não API direta.
- Classificação: local-write
- Fontes usadas:
- Mensagem do Lucas em 2026-06-27; skill mcp-connections; Brain AGENTS.md; política Doppler-first/CLI wrappers existentes.
- O que foi feito:
- Criada rotina cli-mcp-first-integration-policy.md; AGENTS.md atualizado no Boot mínimo; MAPA de Operações indexado; skill mcp-connections reforçada; memória durável e Honcho atualizados.
- Output/artefato:
- areas/operacoes/rotinas/cli-mcp-first-integration-policy.md; AGENTS.md; areas/operacoes/MAPA.md; empresa/rotinas/_index.md; skill mcp-connections; memória user/Honcho
- Aprovação: Ação local/documental e memória decorrente de instrução explícita de Lucas; sem runtime/cron/gateway externo.
- Envio/publicação: Nenhum envio externo; resposta Telegram final somente resumo.
- Writes externos: 0
- Riscos/bloqueios: API direta/raw fica como exceção justificada quando MCP/CLI não existir; writes externos continuam exigindo aprovação escopada, rollback/readback e verificação.
- Rollback/mitigação: Reverter patches em AGENTS.md, MAPA.md, skill mcp-connections e remover rotina/receipt; memória pode ser substituída por nova preferência se Lucas corrigir.
- Próximos passos: Aplicar a regra em prompts de subagentes/crons materiais; quando integração recorrente só tiver API raw, criar backlog para wrapper MCP/CLI.
- Onde foi documentado no Brain: true
- Source confidence: fonte-primária

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
