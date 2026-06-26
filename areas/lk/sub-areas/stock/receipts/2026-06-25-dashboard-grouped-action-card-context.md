# Receipt — Dashboard Stock OS card usa contexto agregado da família

- Data/hora: 2026-06-25T18:36:24.900001+00:00
- Agente/profile/cron: Hermes Agent default
- Empresa/área: LK / Stock OS / UI
- Responsável humano: lk-stock
- Pedido original: Lucas apontou que Nike Moon Shoe Jacquemus Medium Brown não podia aparecer sem ação imediata apesar de vender bem, e que New Balance 204L Arid Timberwolf mostrava 1 un./Corrigir cadastro apesar de ter diversas unidades em estoque.
- Classificação: external-write
- Fontes usadas:
- Mensagem de Lucas; Stock OS API container; Shopify Sales OS windows já enriquecidas; npm test; Impeccable; smoke container /api/estoque/detail quickFilter action-needed.
- O que foi feito:
- Corrigido rótulo visual para vendas ponderadas relevantes: produtos core com sales_volume_relevant/sales_velocity_score agora aparecem como Comprar/repor mesmo se action_lane técnico vier NO_ACTION. Backend expõe product_group_stock_units/product_group_positive_variant_count/product_group_available_size_stock. Cards agrupados usam resumo da família para estoque/grade e evitam double-count, em vez de herdar estoque/status de uma variante filtrada.
- Output/artefato:
- Commit f723e7d em feat/stock-os-api-adapter; container lk-estoque-web atualizado. Smoke: Moon Shoe HV8547-200 aparece action-needed pos 14+ com u30=12/u90=47/u180=60/vel=214 e group=7; U204LMMC aparece com group=20 e grade 35/4 36/4 37/7 38/2 39/2 41/1.
- Aprovação: Pedido direto de Lucas para corrigir informações erradas no dashboard. Escopo UI/API read-only do dashboard.
- Envio/publicação: Telegram final para Lucas
- Writes externos: GitHub push na branch feat/stock-os-api-adapter; atualização de src/index.js, src/public/dashboard-utils.js e src/public/index.html no container lk-estoque-web e restart. Tiny write 0; Shopify write 0; Notion write 0; contato externo 0.
- Riscos/bloqueios: Não altera estoque real nem cadastro Tiny/Shopify; corrige apenas leitura/agregação/rótulo. Se houver divergência real em uma variante específica, continuará visível em Base/Cadastro, mas não contamina o card agregado de reposição.
- Rollback/mitigação: Backup local .hermes/backups/grouped-action-card-fix-20260625T183205Z; backup container /opt/data/profiles/lk-stock/backups/lk-estoque-web-grouped-action-cards-20260625T183504Z; rollback via git revert f723e7d.
- Próximos passos: Se Lucas quiser, agrupar visualmente action-needed por família em uma única linha, reduzindo repetição de variantes.
- Onde foi documentado no Brain: Skill lk-stock atualizada com regra de card usar contexto agregado de família.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
