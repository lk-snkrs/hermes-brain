# Receipt — LK Stock all-agents delegation policy

- Data/hora: 2026-06-11T20:27:14.873471+00:00
- Agente/profile/cron: Hermes Agent default
- Empresa/área: LK Sneakers / Stock OS / multi-agent routing
- Responsável humano: Lucas Cimino
- Pedido original: Ensinar todos os agentes que nunca devem consultar estoque diretamente; toda consulta de estoque deve ser solicitada ao agente LK Stock.
- Classificação: local-write
- Fontes usadas:
- Lucas Cimino Telegram 2026-06-11
- areas/lk/sub-areas/stock/references/lk-stock-routing-canon-all-agents-delegation-20260611.md
- profiles/*/AGENTS.md e Brain agentes/subáreas AGENTS.md
- O que foi feito:
- Aplicada política transversal: agentes não-lk-stock não consultam estoque diretamente em Tiny, Shopify, Stock OS DB local, caches, planilhas ou relatórios antigos.
- Atualizados AGENTS/SOUL/TOOLS/memories e skills centrais para handoff obrigatório ao [LK] Estoque Loja Física / lk-stock.
- Corrigido efeito colateral de node_modules revertendo 7 arquivos de dependências; preservados apenas perfis/Brain canônicos.
- Output/artefato:
- Regra forte documentada em profile-local AGENTS.md, Brain agentes/subáreas e referências/skills.
- Verificação: missing_marker_count=0, legacy_marker_count=0, Brain health all checks passed.
- Aprovação: Pedido explícito de Lucas para aplicar política transversal local/documental; sem writes externos.
- Envio/publicação: Sem envio/publicação externa; resposta apenas no Telegram de origem.
- Writes externos: 0
- Riscos/bloqueios: Risco principal: agentes consultarem estoque fora do lk-stock; mitigado por boot files, Brain refs, skills e memória.
- Rollback/mitigação: Backups locais em /opt/data/backups/lk-stock-all-agent-delegation-20260611T201840Z, /opt/data/backups/lk-stock-legacy-routing-block-upgrade-20260611T202057Z e /opt/data/backups/lk-stock-owner-block-fix-20260611T202134Z.
- Próximos passos: Manter regra em novos perfis/skills; qualquer consulta de estoque deve ser roteada para lk-stock.
- Onde foi documentado no Brain: areas/lk/sub-areas/stock/references/lk-stock-routing-canon-all-agents-delegation-20260611.md; areas/lk/sub-areas/stock/receipts/lk-stock-all-agents-delegation-policy-20260611T202500Z.md
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
