# Receipt — LK Stock OS demand score local enrichment

- Data/hora: 2026-06-10T19:11:02.277069+00:00
- Agente/profile/cron: lk-stock
- Empresa/área: LK / Estoque Loja Física
- Responsável humano: Hermes lk-stock
- Pedido original: Continuar o Stock OS após resolver identidade: popular vendas/demanda/score reais na nossa database.
- Classificação: local-write
- Fontes usadas:
- Stock OS DB pointer; reports locais LK Sales; snapshots locais LK Data Spine; sem chamadas Tiny/Shopify live.
- O que foi feito:
- Criada DB local enriquecida com demand_signals_stock_os, current_stock_scored e demand_score_summary; pointer atualizado.
- Output/artefato:
- DB: areas/lk/sub-areas/stock/data/lk_stock_os_current_demand_scored_20260610T190741Z.db; JSON/CSV/packet/guia gerados; 903 linhas; 352 SKUs com sinal; 18 linhas casadas; P0=4; P1=13.
- Aprovação: Não necessária para leitura/local write; qualquer compra/reposição/write externo exige aprovação separada.
- Envio/publicação: Nenhum envio externo.
- Writes externos: 0
- Riscos/bloqueios: Sinais vêm de reports locais/top products, não de export completo de pedidos; usar como score operacional inicial e confirmar pela DB Stock OS.
- Rollback/mitigação: Reapontar lk_stock_os_current_pointer.json para a DB anterior: areas/lk/sub-areas/stock/data/lk_stock_os_current_identity_resolved_20260610T172139Z.db.
- Próximos passos: Gerar fila P0/P1 de reposição/transferência local a partir de current_stock_scored, ainda sem write externo.
- Onde foi documentado no Brain: areas/lk/sub-areas/stock/PRD.md; areas/lk/sub-areas/stock/references/lk-stock-os-demand-score-guide-20260610.md; areas/lk/sub-areas/stock/approval-packets/lk-stock-os-demand-score-20260610T190741Z.md
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
