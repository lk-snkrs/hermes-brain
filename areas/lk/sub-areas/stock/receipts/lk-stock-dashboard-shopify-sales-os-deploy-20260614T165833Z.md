# Receipt — Deploy do Shopify Sales OS no estoque.lkskrs.online

- Data/hora: 2026-06-14T16:59:03.975457+00:00
- Agente/profile/cron: Hermes Agent default
- Empresa/área: LK / Stock OS / Estoque Web
- Responsável humano: Lucas Cimino
- Pedido original: Lucas aprovou: Pode fazer deploy da integração Shopify Sales OS no estoque.lkskrs.online.
- Classificação: external-write
- Fontes usadas:
- LK-Estoque-Web-inicial worktree; Docker lk-estoque-web; produção https://estoque.lkskrs.online; Shopify Sales OS summary JSON; cron wrapper lk_shopify_sales_os_nightly_reconcile.py
- O que foi feito:
- Deploy do commit 0d1a108 no container protegido; endpoint /api/vendas/shopify-sales-os e painel shopifySalesOsPanel ativados; imagem lk-estoque-web-web:shopify-sales-os-20260614T165341Z criada; rollback preservado como lk-estoque-web-rollback-shopify-sales-os-20260614T165341Z; nightly wrapper ajustado para copiar summary JSON ao container após reconcile OK.
- Output/artefato:
- Produção autenticada retorna API 200 status ok com orders 1959, units 3315, revenue 6443319.85; HTML contém shopifySalesOsPanel e /api/vendas/shopify-sales-os; sem auth retorna 401; guardrails Shopify/Tiny/external/public/auto_purchase zero.
- Aprovação: Aprovação explícita de Lucas no Telegram: Pode fazer deploy por favor.
- Envio/publicação: Dashboard interno protegido em https://estoque.lkskrs.online atualizado; nenhum contato externo/customer-facing.
- Writes externos: Docker/container deploy/restart; GitHub branch feat/stock-os-api-adapter verificado local=remote; local profile script update. Shopify write 0; Tiny write 0; cliente/fornecedor 0; public availability promise 0.
- Riscos/bloqueios: Migração para Vercel ainda não executada; app atual depende de runtime Docker/Stock OS/API/dados locais. O summary da Shopify Sales OS é copiado para o container e o reconcile noturno passa a atualizá-lo.
- Rollback/mitigação: Parar/remover lk-estoque-web atual e renomear/iniciar lk-estoque-web-rollback-shopify-sales-os-20260614T165341Z; imagem anterior era lk-estoque-web-web:sales-analytics-final-20260613T234308Z.
- Próximos passos: Decidir arquitetura futura: manter Hostinger/Docker enquanto APIs locais não estiverem externalizadas; avaliar Vercel somente com frontend stateless + API read-only protegida.
- Onde foi documentado no Brain: Receipt canônico; skill lk-stock referência Shopify Sales OS atualizada com pitfall de summary no container.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
