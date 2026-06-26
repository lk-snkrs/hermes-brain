# Receipt — Correção de prioridade Crocs no Stock OS

- Data/hora: 2026-06-11T00:12:53.499611+00:00
- Agente/profile/cron: lk-stock
- Empresa/área: LK / Estoque Loja Física
- Responsável humano: Hermes lk-stock
- Pedido original: Lucas corrigiu que Crocs nunca deveria ser prioridade automática e que 4 unidades foi excessivo.
- Classificação: local-write
- Fontes usadas:
- Mensagem Telegram de Lucas em 2026-06-11; skill lk-stock; referência p0-purchase-notion-julio-pattern
- O que foi feito:
- Atualizei a skill lk-stock e a referência de compra Notion/Júlio para aplicar exclusão/cap de Crocs antes de escolher P0; registrei que Crocs não deve ser P0 automático nem quantidade >1 sem validação humana explícita.
- Output/artefato:
- Regra operacional persistida localmente: Crocs rebaixado/excluído da seleção automática P0; item Notion anterior identificado como erro operacional a corrigir mediante aprovação escopada.
- Aprovação: Lucas aprovou/corrigiu a regra operacional por mensagem; nenhuma alteração externa no Notion foi feita nesta etapa.
- Envio/publicação: Telegram: resposta de reconhecimento pendente
- Writes externos: 0
- Riscos/bloqueios: A página Notion do Crocs criada anteriormente permanece até Lucas aprovar remover/ajustar; evitar novo write externo sem confirmação escopada.
- Rollback/mitigação: Reverter patches da skill/referência se Lucas mudar a regra; página Notion pode ser arquivada/ajustada com aprovação.
- Próximos passos: Pedir escolha de correção para o item Notion: arquivar/remover, manter mas reduzir/baixar prioridade, ou substituir por outro item não-Crocs.
- Onde foi documentado no Brain: productivity/lk-stock/SKILL.md; productivity/lk-stock/references/p0-purchase-notion-julio-pattern-20260610.md
- Source confidence: fonte-primária

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
