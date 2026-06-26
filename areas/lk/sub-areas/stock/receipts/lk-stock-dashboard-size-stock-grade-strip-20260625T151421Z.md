# Receipt — LK Stock dashboard grade strip size quantity fix

- Data/hora: 2026-06-25T15:21:54.393467+00:00
- Agente/profile/cron: lk-stock
- Empresa/área: LK / Stock OS / Dashboard
- Responsável humano: Hermes lk-stock
- Pedido original: Lucas corrigiu que no card/grade-strip não adianta mostrar só o tamanho; precisa mostrar tamanho/quantidade por pares, ex. 35/1 36/2.
- Classificação: infra-sensitive
- Fontes usadas:
- Pedido direto do Lucas com screenshot; código src/public/dashboard-utils.js e src/public/index.html; testes npm; detector Impeccable; validação interna do container lk-estoque-web; busca New Balance no endpoint de detalhe.
- O que foi feito:
- Adicionado available_size_stock no agrupador de cards, agregando estoque positivo por tamanho; renderizado grade-strip como tamanho/quantidade em renderizarGradePrincipal e renderStockCard; testes atualizados; deploy no container; commit/push c7d3cd191e5f84d7d71e0a47feb0e620baf1122d; skill lk-stock atualizada com regra durável.
- Output/artefato:
- Exemplo validado via endpoint interno: New Balance 9060 Black Cement Black Cat Preto => 40/2, 41/1, 42/2, 43/2; html 200, api 200; screenshot /tmp/lk_stock_size_stock_after/desktop1440.png; imagem Docker sha256:d1204af3e67d942d902d646bd1dcf1963db4bd2524ab360346ad25f014365c25.
- Aprovação: Aprovação escopada por pedido direto do Lucas para corrigir o dashboard informado. Nenhum write em Tiny, Shopify, Notion, WhatsApp, e-mail ou disponibilidade pública.
- Envio/publicação: Resposta Telegram com evidência.
- Writes externos: GitHub push no branch feat/stock-os-api-adapter e atualização do container web lk-estoque-web. Tiny write 0; Shopify write 0; Notion write 0; promessa disponibilidade pública 0.
- Riscos/bloqueios: Mudança de UI/agregação frontend; mitigada por backup, testes, detector Impeccable, validação em container e commit remoto.
- Rollback/mitigação: Backup source .hermes/backups/size-stock-strip-20260625T151421Z; backup container /opt/data/profiles/lk-stock/backups/lk-estoque-web-size-stock-strip-20260625T151421Z/src; rollback via docker cp do backup para /app/src ou retag imagem anterior.
- Próximos passos: Lucas revisar visual; se quiser, compactar ainda mais chips de grade para caber mais tamanhos sem quebrar card.
- Onde foi documentado no Brain: Receipt Memory OS; commit c7d3cd; skill lk-stock reference patch; npm test 39/39; impeccable []; container html/api 200.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
