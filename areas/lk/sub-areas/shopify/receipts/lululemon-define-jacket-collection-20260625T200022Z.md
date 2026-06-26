# Receipt — LK Shopify — collection canônica Lululemon Define Jacket

- Data/hora: 2026-06-25T20:02:17.828926+00:00
- Agente/profile/cron: lk-shopify / kanban t_2443c1f6
- Empresa/área: LK Sneakers / Shopify
- Responsável humano: LK Shopify
- Pedido original: Validar/criar/ativar a collection canônica Lululemon Define Jacket em /collections/lululemon-define-jacket, usando apenas produtos Lululemon Define ACTIVE já existentes, sem consultar estoque/disponibilidade/grade e sem alterar preço, campanhas, GMC, Klaviyo, checkout, SEO title/meta ou descrição editorial.
- Classificação: external-write
- Fontes usadas:
- Handoff aprovado por Lucas: areas/lk/sub-areas/shopify/handoffs/lululemon-define-jacket-surface-handoff-20260625T195532Z.md
- Shopify Admin API via Doppler profile lk-shopify; values_printed=false; smoke shopify_lk HTTP 200.
- Readback público independente: https://lksneakers.com.br/collections/lululemon-define-jacket retornou HTTP 200.
- O que foi feito:
- Antes: collectionByHandle(lululemon-define-jacket) e collectionByHandle(lululemon-define) retornaram null no plano; a primeira tentativa criou a collection e vinculou produtos, depois falhou apenas na forma do campo GraphQL publishable{id}; a segunda execução idempotente concluiu publishablePublish e readback.
- Criada custom collection Shopify title=Lululemon Define Jacket, handle=lululemon-define-jacket, legacy id=1128948367582, gid=gid://shopify/Collection/1128948367582.
- Associados somente 6 produtos ACTIVE Lululemon Define identificados sem consultar variants/inventory: define-cropped-jacket-nulu; define-jacket-nulu-rose-gold; jaqueta-lululemon-define-luon-white-branco; jaqueta-lululemon-define-nulu; jaqueta-lululemon-define-nulu-black-gold-preto; jaqueta-lululemon-define-nulu-black-plum-gold-roxo.
- Collection publicada/ativada no canal Online Store publication gid://shopify/Publication/79413379294; publishablePublish retornou userErrors=[].
- Não foi feita consulta a inventory/variants/availability/Tiny/estoque; não houve alteração de preço, SEO title/meta, descrição editorial, tema, GMC, Klaviyo, campanhas ou checkout.
- Output/artefato:
- URL pública 200 OK: https://lksneakers.com.br/collections/lululemon-define-jacket; title tag público: Lululemon Define Jacket: 6 modelos | LK Sneakers; H1 público: Lululemon Define Jacket; HTML contém os 6 handles esperados.
- Readback/evidência JSON: /opt/data/kanban/boards/lk-growth-ops/workspaces/t_2443c1f6/lululemon-define-jacket-final-readback.json; plano inicial: /opt/data/kanban/boards/lk-growth-ops/workspaces/t_2443c1f6/lululemon-define-jacket-plan.json.
- Aprovação: Aprovação explícita de Lucas registrada no handoff: criar/validar/ativar collection canônica Lululemon Define Jacket, preferencialmente /collections/lululemon-define-jacket, usando apenas produtos Lululemon Define ativos já existentes, sem consultar/alterar estoque/preço/campanhas/GMC/Klaviyo/checkout, com preview/readback público.
- Envio/publicação: Sem envio externo/mensagem/campanha; apenas Shopify Admin write aprovado e receipt Brain.
- Writes externos: Shopify: criação de custom collection; associação de 6 collects; publicação no canal Online Store.
- Riscos/bloqueios: Cache/propagação pública pode variar, mas readback imediato confirmou HTTP 200 e presença dos 6 handles. A ordenação permaneceu padrão BEST_SELLING; não foi feita ordenação comercial manual.
- Rollback/mitigação: Rollback: remover os 6 collects da collection legacy id 1128948367582 e depois excluir ou despublicar a custom collection lululemon-define-jacket. Não há rollback de estoque, preço, SEO title/meta, descrição editorial, tema, GMC, Klaviyo, campanhas ou checkout porque essas superfícies não foram alteradas.
- Próximos passos: LK Growth pode preparar guia/FAQ/schema em dev/preview antes de qualquer produção, conforme handoff.
- Onde foi documentado no Brain: Receipt criado em areas/lk/sub-areas/shopify/receipts/lululemon-define-jacket-collection-20260625T200022Z.md; evidência técnica mantida no workspace kanban t_2443c1f6.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
