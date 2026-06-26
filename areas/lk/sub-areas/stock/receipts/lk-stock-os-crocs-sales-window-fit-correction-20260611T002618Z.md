# Receipt — Refino Crocs por janelas de venda

- Data/hora: 2026-06-11T00:26:31.094431+00:00
- Agente/profile/cron: lk-stock
- Empresa/área: LK / Estoque Loja Física
- Responsável humano: Hermes lk-stock
- Pedido original: Lucas refinou: Crocs pode entrar na fila, mas a prioridade/quantidade precisa fazer sentido pelas vendas D30/D90/D180, não por score genérico.
- Classificação: local-write
- Fontes usadas:
- Mensagem Telegram de Lucas em 2026-06-11; skill lk-stock; referência p0-purchase-notion-julio-pattern
- O que foi feito:
- Atualizei a regra local: Crocs pode entrar quando o sales-window-fit sustentar; D30/D90/D180 devem justificar prioridade e quantidade; caso contrário não promover para P0 nem sugerir quantidade alta.
- Output/artefato:
- Skill lk-stock, referência de compra Notion/Júlio e PRD ajustados para regra de janelas de venda em Crocs.
- Aprovação: Correção operacional fornecida diretamente por Lucas; nenhum write externo executado nesta etapa.
- Envio/publicação: Telegram: resposta de confirmação
- Writes externos: 0
- Riscos/bloqueios: Se houver grafia D390 na fala, interpretar como janela maior disponível somente se existir nos dados; regra mínima aplicada a D30/D90/D180.
- Rollback/mitigação: Reverter patches se Lucas mudar a regra; página Notion Crocs já arquivada por aprovação anterior e pode ser restaurada separadamente.
- Próximos passos: Em futuras filas P0, aplicar sales-window-fit antes de escolher Crocs/quantidade.
- Onde foi documentado no Brain: productivity/lk-stock/SKILL.md; productivity/lk-stock/references/p0-purchase-notion-julio-pattern-20260610.md; areas/lk/sub-areas/stock/PRD.md
- Source confidence: fonte-primária

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
