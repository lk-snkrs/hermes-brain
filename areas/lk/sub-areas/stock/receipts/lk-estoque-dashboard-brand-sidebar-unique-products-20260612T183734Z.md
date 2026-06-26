# Receipt — LK Estoque dashboard — sidebar por produtos únicos disponíveis

- Data/hora: 2026-06-12T18:37:34.667607+00:00
- Agente/profile/cron: lk-stock
- Empresa/área: LK Sneakers / Stock OS
- Responsável humano: Hermes lk-stock
- Pedido original: Ajustar correção anterior: Lucas confirmou que quer NÚMERO de produtos, não linhas/variantes/tamanhos.
- Classificação: external-write
- Fontes usadas:
- Teste TDD dashboard-utils; produção https://estoque.lkskrs.online autenticada; Stock OS API read-only.
- O que foi feito:
- buildAvailableBrandCounts passou a deduplicar por marca + productGroupKey/handle; duas numerações positivas do mesmo produto contam como 1 no sidebar; deploy aplicado no container; commit 9f279f8 pushado e verificado.
- Output/artefato:
- Produção validada: JS 200 com uniqueProductsByBrand/productGroupKey; API 200; total API 5192; linhas variantes disponíveis 323; produtos únicos disponíveis sidebar 114; top marcas por produto único: Nike 60, New Balance 17, Adidas 16, Onitsuka 12, Outros 5; guardrails Tiny/Shopify/public availability = 0.
- Aprovação: Aprovação escopada nesta conversa para corrigir/publicar o dashboard de estoque e push GitHub; pedido direto incremental de Lucas: 'eu quero NUMERO de produtos ok?'. Escopo executado apenas frontend/dashboard + testes + deploy container + GitHub branch.
- Envio/publicação: Telegram: resumo final nesta conversa.
- Writes externos: Docker/container web: deploy/restart; GitHub push branch feat/stock-os-api-adapter. Tiny write 0; Shopify write 0; public availability 0.
- Riscos/bloqueios: Sem alteração de estoque real; risco limitado a apresentação do dashboard. Backup: /opt/data/lk-estoque-web-backups/20260612T183617Z-brand-sidebar-unique-products.
- Rollback/mitigação: Restaurar /app/src a partir do backup ou reverter commit 9f279f8; tag Docker brand-sidebar-unique-products-20260612T183617Z disponível.
- Próximos passos: Nenhum obrigatório.
- Onde foi documentado no Brain: Skill lk-stock atualizado: sidebar conta produto/modelo único disponível, não variante/tamanho.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
