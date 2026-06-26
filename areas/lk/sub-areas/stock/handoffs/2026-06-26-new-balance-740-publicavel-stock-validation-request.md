## 2026-06-26 09:05Z — LK Stock — New Balance 740 publicável?

- Pedido/evento: Mesa COO retornou **Fazer** para destravar ou manter bloqueada a frente `New Balance 740` na LK.
- Fonte viva consultada: Shopify Admin read-only pelo originador; produto candidato existe, mas está `ARCHIVED`, `publishedAt=null`, `onlineStoreUrl=null`; coleção `new-balance-740` retornou `null` por Admin GraphQL.
- Item/SKU/tamanho/cliente/pedido/fornecedor:
  - Produto: `Tênis New Balance 740 x Concepts Saignée Verde`
  - Handle: `tenis-new-balance-740-x-concepts-saignee-verde`
  - Product GID: `gid://shopify/Product/8780230492382`
  - SKUs/variantes Shopify vistas: `U740GP2-1` tamanho 37, `U740GP2-2` tamanho 38, `U740GP2-3` tamanho 39, `U740GP2-4` tamanho 40, `U740GP2-5` tamanho 41, `U740GP2-6` tamanho 42, `U740GP2-7` tamanho 43, `U740GP2-8` tamanho 44.
- Resultado verificado: Shopify inventory exibiu quantidade, mas **não usar como verdade de estoque**. O desbloqueio depende de LK Stock validar Tiny/Stock OS por SKU/tamanho e dizer se o produto é publicável/vendável.
- Output/rascunho: approval/handoff packet completo em `areas/lk/sub-areas/collection-optimizer/approval-packets/20260626T0905Z-new-balance-740-unblock-readonly-packet.md`.
- Writes externos: não.
- Aprovação: Lucas aprovou **preparar handoff/packet read-only**; não aprovou Tiny/Shopify write, publicação, reativação ou coleção.
- Snapshot/readback/receipt: Shopify read-only consultado em 2026-06-26T09:05Z; `values_printed=false`.
- Risco/bloqueio: coleção vazia seria ruim para SEO/Growth; produto único está arquivado e não publicado; sem validação Tiny não prometer disponibilidade.
- Próximo passo: LK Stock validar em Tiny/Stock OS os SKUs/tamanhos e responder uma das classes: `publicável`, `não publicável`, `precisa correção SKU/Tiny`, `indisponível/sem venda`.
- Atualização 2026-06-26T09:23Z: LK Shopify criou Kanban `t_55c1f648` para essa validação e registrou snapshot Shopify read-only adicional em `areas/lk/sub-areas/shopify/approval-packets/2026-06-26-new-balance-740-publicability-write-preview-blocked-pending-stock.md`.
- Onde ficou documentado: este handoff + packet LKGOC acima.
- Reminder OS loop needed: yes — depende de retorno do `lk-stock` para destravar ou manter bloqueio.
