# Receipt — Migração física dos canônicos LKGOC de growth para collection-optimizer

- Data/hora: 2026-06-27T17:02:02.166645+00:00
- Agente/profile/cron: lk-collection-optimizer
- Empresa/área: LK / Collection Optimizer / LKGOC
- Responsável humano: [LK] Otimização de Coleções
- Pedido original: Lucas pediu: MIGRAR fisicamente os growth/LKGOC-* para collection-optimizer/.
- Classificação: local-write
- Fontes usadas:
- Arquivos growth/LKGOC-* verificados; normalização LKGOC anterior; backups e hashes; smoke lkgoc_boot_smoke.py.
- O que foi feito:
- Migrados 12 arquivos LKGOC-* de areas/lk/sub-areas/growth/ para areas/lk/sub-areas/collection-optimizer/; deixados stubs de redirect no path growth/; atualizados canon/INDEX.md, MAPA, skill local e ponteiros ativos; corrigido wording do canon index; criados backups antes dos edits.
- Output/artefato:
- collection-optimizer agora é o local físico e lógico dos canônicos LKGOC-*; growth/LKGOC-* virou redirect legado. Verificação de hash contra backup PASS para 12/12; smoke PASS.
- Aprovação: Aprovação do Lucas recebida por Telegram: 'MIGRAR'. Escopo limitado a writes locais/Brain/profile; sem Shopify/prod/secrets.
- Envio/publicação: Resumo enviado no Telegram.
- Writes externos: nenhum
- Riscos/bloqueios: Baixo/médio: paths legados podem existir em reports/receipts/backups históricos; mitigado com stubs de redirect em growth/ e atualização de ponteiros ativos.
- Rollback/mitigação: Restaurar originais de collection-optimizer/backups/migracao-fisica-lkgoc-20260627T165939Z para growth/ e remover/copiar de volta os top-level collection-optimizer/LKGOC-*; ponteiros podem ser revertidos pelos backups ponteiros-pos-migracao-lkgoc-20260627T170018Z e active-pointer-cleanup-lkgoc-20260627T170111Z.
- Próximos passos: Opcional: curar índices gerados/projetos antigos que ainda mencionam growth/LKGOC-* como histórico; não necessário para runtime.
- Onde foi documentado no Brain: Receipt criado via hermes_memory_os_receipt_writer.py; canon/INDEX.md atualizado com regra de redirects legados.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
