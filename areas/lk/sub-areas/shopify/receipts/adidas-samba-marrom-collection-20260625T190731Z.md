# Receipt — LK Shopify — collection canônica Adidas Samba Marrom

- Data/hora: 2026-06-25T19:09:17.051026+00:00
- Agente/profile/cron: lk-shopify / kanban t_ae530570
- Empresa/área: LK Sneakers / Shopify
- Responsável humano: LK Shopify
- Pedido original: Validar/criar/ativar a collection canônica Adidas Samba Marrom em /collections/adidas-samba-marrom, usando apenas produtos Adidas Samba marrom ACTIVE já existentes, sem consultar estoque/disponibilidade/grade e sem alterar preço, campanhas, GMC, Klaviyo, checkout, SEO title/meta ou descrição editorial.
- Classificação: external-write
- Fontes usadas:
- Handoff aprovado por Lucas: areas/lk/sub-areas/shopify/handoffs/adidas-samba-marrom-surface-handoff-20260625T184438Z.md
- Shopify Admin API via Doppler profile lk-shopify; values_printed=false.
- Readback público: https://lksneakers.com.br/collections/adidas-samba-marrom retornou HTTP 200.
- O que foi feito:
- Antes: collectionByHandle(adidas-samba-marrom) retornou null; equivalentes por título/handle não confirmados.
- Criada custom collection Shopify title=Adidas Samba Marrom, handle=adidas-samba-marrom, legacy id=1128947417310, gid=gid://shopify/Collection/1128947417310.
- Collection publicada/ativada no canal Online Store publication gid://shopify/Publication/79413379294; publishablePublish retornou userErrors=[].
- Associados somente 3 produtos ACTIVE: tenis-adidas-samba-og-shadow-brown-powder-yellow-marrom; tenis-adidas-samba-lt-cow-print-brown-white-marrom; tenis-adidas-samba-62-wild-brown-marrom.
- Não foi feita consulta a inventory/variants/availability/Tiny/estoque; não houve alteração de preço, SEO title/meta, descrição editorial, tema, GMC, Klaviyo, campanhas ou checkout.
- Output/artefato:
- URL pública 200 OK: https://lksneakers.com.br/collections/adidas-samba-marrom; title tag público: Adidas Samba Marrom: 3 modelos | LK Sneakers; H1 público: Adidas Samba Marrom; HTML contém os 3 handles esperados.
- Readback e evidência JSON: /opt/data/kanban/boards/lk-growth-ops/workspaces/t_ae530570/adidas-samba-marrom-final-readback.json e /opt/data/kanban/boards/lk-growth-ops/workspaces/t_ae530570/adidas-samba-marrom-publish-result.json.
- Aprovação: Aprovação explícita de Lucas registrada no handoff: criar/ativar collection canônica Adidas Samba Marrom, preferencialmente /collections/adidas-samba-marrom, usando apenas produtos Adidas Samba marrom ativos já existentes, sem consultar/alterar estoque/preço/campanhas/GMC/Klaviyo/checkout, com preview/readback público.
- Envio/publicação: Sem envio externo/mensagem/campanha; apenas Shopify Admin write aprovado e receipt Brain.
- Writes externos: Shopify: criação de custom collection; associação de 3 collects; publicação no canal Online Store.
- Riscos/bloqueios: Cache/propagação pública pode variar, mas readback imediato confirmou HTTP 200 e presença dos 3 handles. A ordenação permaneceu padrão BEST_SELLING; não foi feita ordenação comercial manual.
- Rollback/mitigação: Rollback: remover os 3 collects da collection legacy id 1128947417310 e depois excluir ou despublicar a custom collection adidas-samba-marrom. Não há rollback de estoque, preço, SEO title/meta, descrição editorial, tema, GMC, Klaviyo, campanhas ou checkout porque essas superfícies não foram alteradas.
- Próximos passos: LK Growth pode preparar guia/FAQ/schema em dev theme 155065450718 antes de qualquer produção, conforme handoff.
- Onde foi documentado no Brain: Receipt criado em areas/lk/sub-areas/shopify/receipts/adidas-samba-marrom-collection-20260625T190731Z.md; evidência técnica mantida no workspace kanban t_ae530570.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
