## 2026-06-26 09:23Z — LK Shopify — New Balance 740 publicabilidade técnica bloqueada por Stock

- Pedido/evento: Kanban `t_1f079009`; Lucas/Mesa COO pediu seguir com validação read-only para destravar ou manter bloqueada a frente `New Balance 740`.
- Fonte viva consultada: Shopify Admin GraphQL read-only em 2026-06-26T09:20Z; public readback HTTP em `lksneakers.com.br`; Doppler `lc-keys/prd` injetou `SHOPIFY_STORE_URL` e `SHOPIFY_ACCESS_TOKEN` sem imprimir valores (`values_printed=false`).
- Item/SKU/tamanho/cliente/pedido/fornecedor:
  - Produto: `Tênis New Balance 740 x Concepts Saignée Verde`
  - Product GID: `gid://shopify/Product/8780230492382`
  - legacy ID: `8780230492382`
  - Handle: `tenis-new-balance-740-x-concepts-saignee-verde`
  - SKUs/tamanhos: `U740GP2-1`/37, `U740GP2-2`/38, `U740GP2-3`/39, `U740GP2-4`/40, `U740GP2-5`/41, `U740GP2-6`/42, `U740GP2-7`/43, `U740GP2-8`/44.
- Resultado verificado Shopify:
  - Produto segue `ARCHIVED`, `publishedAt=null`, `onlineStoreUrl=null`.
  - `resourcePublications` do produto retornou vazio.
  - Produto tem SEO, tags, imagem READY, variantes e coleções genéricas; superfície parece tecnicamente preparável, mas não publicável operacionalmente.
  - `collectionByHandle("new-balance-740")` retornou `null`; busca Admin por coleção `New Balance 740` retornou 0.
  - Public readback: PDP e `/collections/new-balance-740` redirecionam para `/collections/new-balance-todos-os-modelos`, canonical da coleção geral New Balance.
- Diagnóstico: Shopify não mostra coleção canônica pronta nem PDP pública; o estado `ARCHIVED` + sem publicações parece um bloqueio/publication gate. Tecnicamente destravável via status `ACTIVE` + publish Online Store + criação/associação de coleção, mas só após OK do `lk-stock` e aprovação explícita de Lucas.
- Output/rascunho: approval packet condicional em `areas/lk/sub-areas/shopify/approval-packets/2026-06-26-new-balance-740-publicability-write-preview-blocked-pending-stock.md`.
- Snapshot JSON sanitizado: `areas/lk/sub-areas/shopify/snapshots/2026-06-26-new-balance-740-shopify-readonly-snapshot.json`.
- Kanban criado para `lk-stock`: `t_55c1f648` — validar Tiny/Stock OS por SKU/tamanho.
- Writes externos: **0**.
- Aprovação: não há aprovação para write. Não foi reativado produto, publicado canal, criada coleção, alterado preço/estoque/SKU/SEO/tags/metafields/theme/menu/Tiny/GMC/Klaviyo/Meta/WhatsApp/campanha/checkout.
- Snapshot/readback/receipt: snapshot JSON local desta execução ficou no workspace do Kanban; evidência decisória resumida no packet acima.
- Risco/bloqueio: sem resposta do `lk-stock`, disponibilidade permanece **não confirmada** e a frente deve ficar bloqueada.
- Próximo passo: aguardar `lk-stock` classificar os SKUs como `publicável`, `não publicável`, `precisa correção SKU/Tiny` ou `indisponível/sem venda`; depois LK Shopify retoma o approval packet ou encerra bloqueado.
- Reminder OS loop needed: yes — bloqueio pendente de `lk-stock`/decisão Lucas.


## Atualização Stock final — 2026-06-26T09:18Z

LK Stock concluiu a validação (`t_55c1f648`): os 8 SKUs/tamanhos `U740GP2-1`…`U740GP2-8` têm match exato Shopify↔Tiny, mas saldo `0` no depósito Tiny `LK | CONTROLE ESTOQUE`. Classificação: `indisponível/sem venda` / `não publicável por estoque`. Portanto, este packet permanece **bloqueado/não executável**; não reativar, publicar ou criar coleção para New Balance 740 salvo nova entrada de estoque ou nova aprovação comercial separada.
