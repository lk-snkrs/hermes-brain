# Receipt — LK Shopify Sales OS token NameError autoheal

- Data/hora: 2026-06-28T06:02:44.536218+00:00
- Agente/profile/cron: cron: Relatório Hermes diário 03h / lk-stock support
- Empresa/área: LK / Stock / Shopify Sales OS
- Responsável humano: Hermes
- Pedido original: Reconciliar alerta do Nightly Ops 02h50 para cron lk-stock LK Shopify Sales OS nightly full reconcile read-only.
- Classificação: local-write
- Fontes usadas:
- reports/nightly-ops-audit/latest.json finding active_cron_non_ok; /opt/data/profiles/lk-stock/cron/jobs.json last_error sanitized; script /opt/data/profiles/lk-stock/scripts/lk_shopify_sales_os_supabase_direct.py.
- O que foi feito:
- Corrigido bug local NameError: removida chamada a token() inexistente no caminho migrado para Shopify CLI oficial; mantida checagem de presença de SHOPIFY_ACCESS_TOKEN sem imprimir valor; backup criado antes da edição.
- Output/artefato:
- /opt/data/profiles/lk-stock/scripts/lk_shopify_sales_os_supabase_direct.py; backup /opt/data/backups/lk-shopify-sales-os-token-nameerror-20260628T060159Z/; py_compile_ok.
- Aprovação: A1 local autoheal permitido; sem write externo manual, sem mutation Shopify/Tiny, sem restart, sem alteração de cron.
- Envio/publicação: nenhum
- Writes externos: nenhum
- Riscos/bloqueios: Não executei o reconcile completo porque ele escreve no read-model Supabase e o digest não tinha aprovação para Supabase write manual; validação completa fica para o próximo run do cron aprovado.
- Rollback/mitigação: Restaurar backup /opt/data/backups/lk-shopify-sales-os-token-nameerror-20260628T060159Z/lk_shopify_sales_os_supabase_direct.py para o script ativo.
- Próximos passos: Monitorar próximo run 2026-06-29 05:40 UTC do cron lk-stock; se falhar por outro motivo, abrir autoheal A1 ou approval packet conforme risco.
- Onde foi documentado no Brain: Receipt local criado e final 03h reportará atenção ainda aberta até próximo run.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
