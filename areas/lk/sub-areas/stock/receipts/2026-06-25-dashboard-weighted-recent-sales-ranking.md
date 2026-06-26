# Receipt — Dashboard Stock OS ranking por vendas ponderadas 1m 3m 6m

- Data/hora: 2026-06-25T18:04:16.708938+00:00
- Agente/profile/cron: Hermes Agent default
- Empresa/área: LK / Stock OS / UI
- Responsável humano: lk-stock
- Pedido original: Lucas corrigiu que Yuto e High Seafoam não fazem sentido como prioridade e que prioridade deve ser por vendas dos últimos 6, 3 e 1 meses com pesos diferentes, considerando volume total.
- Classificação: external-write
- Fontes usadas:
- Mensagem de Lucas; Shopify Sales OS search index windows; Stock OS API; npm test; Impeccable; smoke container /api/estoque/detail quickFilter action-needed.
- O que foi feito:
- Enriquecido estoque com sales_units_30d/90d/180d, sales_velocity_score e sales_volume_relevant a partir do Shopify Sales OS. Ranking action-needed agora usa score 30d*5 + 90d*2 + 180d e mínimo sales_units_180d>=3; P0/P1 técnico e sell-through pequeno não bastam. Produtos P3/NO_ACTION podem entrar se volume real recente e estoque baixo/zero. Ajustado comparador para usar vendas ponderadas antes de bloqueio técnico.
- Output/artefato:
- Commit 7a5332c em feat/stock-os-api-adapter; container lk-estoque-web atualizado. Smoke: Kill Bill posições 1-12; U204LMMC 37-42; U204LMMA 43-45; U9060ERC 68+; U9060WHT 245+; Nike Mind 001 241+; Yuto/Seafoam/McQueen fora do top500 consultado.
- Aprovação: Pedido direto de Lucas para corrigir ranking no dashboard. Escopo UI/API read-only; sem Tiny/Shopify/Notion/customer write.
- Envio/publicação: Telegram final para Lucas
- Writes externos: GitHub push na branch feat/stock-os-api-adapter; atualização de arquivos no container lk-estoque-web e restart. Tiny write 0; Shopify write 0; Notion write 0; contato externo 0; compra automática 0.
- Riscos/bloqueios: Ranking ainda lista variantes/linhas; próxima melhoria possível é agrupar visualmente por produto/família para reduzir repetição de grade. U9060WHT e Nike Mind 001 aparecem mais abaixo porque têm menor D30/weighted score que Kill Bill/204L recentes.
- Rollback/mitigação: Backup local .hermes/backups/weighted-sales-ranking-20260625T174705Z; backup container /opt/data/profiles/lk-stock/backups/lk-estoque-web-weighted-sales-ranking-20260625T180240Z; rollback via git revert 7a5332c.
- Próximos passos: Se Lucas quiser, agrupar action-needed por família/produto e mostrar uma linha com grade/tamanhos, não múltiplas variantes repetidas.
- Onde foi documentado no Brain: Skill lk-stock atualizada com Weighted recent sales ranking rule.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
