# Receipt — Inventory Hub product grid image and parent SKU fix

- Data/hora: 2026-06-27T16:54:10Z
- Agente/profile/cron: lk-stock
- Empresa/área: LK/Stock/Inventory Hub
- Responsável humano: Hermes lk-stock
- Pedido original: Lucas pediu corrigir duas coisas no grid de produtos do hub.lksnk.dev: foto sem crop na proporção original e exibir SKU do produto mãe, exemplos U204LMMC e U9060WHT.
- Classificação: external-write
- Fontes usadas:
- GitHub lk-snkrs/inventory-hub; Vercel production deploy; live hub.lksnk.dev HTML/API; npm test
- O que foi feito:
- Troquei thumbnails/cards para object-fit: contain sem crop e adicionei parent_sku derivado/normalizado no agrupamento de cards. O grid agora renderiza pill 'SKU mãe <codigo>' em cards e grade principal. Adicionei testes para CSS/label e derivação de parent_sku.
- Output/artefato:
- Commit 00474ff5bf857646ff36fc4ebbdc13a365a14838 enviado para dev e production. Deploy Vercel production Ready e alias hub.lksnk.dev atualizado. Live check: HTML contém object-fit: contain, não contém object-fit: cover, contém SKU mãe e parent-sku-pill; U204LMMC e U9060WHT retornam linhas no endpoint de estoque.
- Aprovação: Aprovação/escopo atual no Telegram: Lucas pediu explicitamente CORRIGIR DUAS COISAS NO GRID DE PRODUTOS do Hub Inventory. Escopo executado: UI/API client code do hub.lksnk.dev via GitHub + Vercel; sem Tiny/Shopify/customer writes.
- Envio/publicação: Telegram final report
- Writes externos: GitHub push dev/production; Vercel production deploy/alias. Sem Tiny write, sem Shopify write, sem contato externo, sem promessa pública.
- Riscos/bloqueios: parent_sku é derivado localmente a partir do SKU de variante quando não vem explícito da base; exemplos verificados U204LMMC e U9060WHT. Imagem preserva proporção no container, podendo deixar margem/fundo em vez de cortar.
- Rollback/mitigação: Reverter commit 00474ff e redeploy Vercel; deploy anterior inventory-ok9trerp8 permanece como referência.
- Próximos passos: Se Lucas quiser, validar visualmente em mobile após cache do navegador limpar; hard refresh pode ser necessário.
- Onde foi documentado no Brain: Receipt criado via Memory OS writer.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
