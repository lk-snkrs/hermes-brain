# Receipt — Propagação CLI/MCP-first para agentes, crons e scripts

- Data/hora: 2026-06-27T10:55:06.941960+00:00
- Agente/profile/cron: Hermes Geral / Brain Governance
- Empresa/área: Operações Hermes / Runtime profiles / Crons / Scripts
- Responsável humano: Hermes Geral; todos os perfis e crons locais cobertos por arquivos/prompt locais
- Pedido original: Lucas pediu: auditar todos os agentes e ensinar; crons, scripts e agentes devem seguir CLI primeiro, MCP segundo, API direta só exceção.
- Classificação: local-write
- Fontes usadas:
- Instrução direta de Lucas; auditoria local de /opt/data/profiles, /opt/data/home/.hermes/profiles, /opt/data/cron, /opt/data/profiles/*/cron, /opt/data/scripts e Brain.
- O que foi feito:
- Adicionada regra CLI/MCP-first em AGENTS/SOUL de perfis; criadas instruções em /opt/data/scripts/AGENTS.md; adicionados headers de política em scripts com uso de rede/API; prompts de crons com prompt receberam regra explícita; corrigidas ocorrências antigas MCP-first; criado report de auditoria.
- Output/artefato:
- Report: reports/governance/cli-mcp-first-all-agents-audit-2026-06-27.md; backup: /opt/data/backups/cli-mcp-all-agents-policy-20260627T105044Z; crons prompts atualizados=50; scripts headers=42; profile AGENTS/SOUL tocados=34.
- Aprovação: Aprovado por instrução explícita de Lucas nesta conversa; sem restart/runtime externo.
- Envio/publicação: Nenhum envio externo; apenas resposta final no Telegram.
- Writes externos: 0
- Riscos/bloqueios: Mudanças locais em prompts de cron alteram instrução de futuras execuções, mas preservam schedule/delivery/enabled/model; rollback via backup informado. API raw permanece exceção, não ban absoluto.
- Rollback/mitigação: Restaurar arquivos pelo backup /opt/data/backups/cli-mcp-all-agents-policy-20260627T105044Z; para crons, restaurar jobs.json backups preservados; nenhum runtime restart foi feito.
- Próximos passos: Monitorar futuras skills/crons novos para incluir a regra; se algum agente tiver integração sem CLI/MCP, criar backlog para wrapper.
- Onde foi documentado no Brain: true
- Source confidence: fonte-primária

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
