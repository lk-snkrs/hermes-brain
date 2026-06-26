# Preview/Aprovação LK Shopify — New Balance 740 publicabilidade — BLOQUEADO até LK Stock

Criado em: 2026-06-26T09:23Z  
Origem: Kanban `t_1f079009` — LK Shopify read-only após decisão Mesa COO “Fazer” / Lucas “seguir”  
Escopo executado: **READ-ONLY Shopify + readback público**.  
Writes externos executados: **0**.  
Secrets: Doppler `lc-keys/prd` via helper; `SHOPIFY_STORE_URL` e `SHOPIFY_ACCESS_TOKEN` presentes; `values_printed=false`.

## 1. Veredito curto

- **Tipo de ação:** approval packet/preview **condicional**, sem execução.
- **Alvo exato:** produto `gid://shopify/Product/8780230492382` / `tenis-new-balance-740-x-concepts-saignee-verde` e futura coleção `new-balance-740`.
- **Risco:** A1 read-only agora; A3 Shopify write se Lucas aprovar reativar/publicar/criar coleção; estoque/Tiny continua dono do `lk-stock`.
- **Status recomendado:** **manter bloqueado por enquanto**. Shopify está tecnicamente preparável, mas não publicável operacionalmente sem OK do `lk-stock`.
- **Diagnóstico:** o produto parece ter cadastro de superfície suficientemente completo (SEO, imagem, variantes, tags e coleções genéricas), mas está `ARCHIVED`, sem publicação e com URL pública redirecionando para a coleção geral New Balance. Isso parece um bloqueio operacional/publication gate, não uma coleção pronta.

## 2. Fonte viva e evidências

- Shopify Admin GraphQL read-only consultado em 2026-06-26T09:20Z, API `2025-04`.
- Snapshot JSON sanitizado salvo em `areas/lk/sub-areas/shopify/snapshots/2026-06-26-new-balance-740-shopify-readonly-snapshot.json` (`values_printed=false`).
- Publicações da loja consultadas read-only: `Online Store`, `Facebook & Instagram`, `Google & YouTube`, `Point of Sale`, `Linktree`, `Pinterest`, `TikTok`, `Attentive`.
- Public readback via HTTP em `lksneakers.com.br`:
  - `/products/tenis-new-balance-740-x-concepts-saignee-verde` → HTTP 200 final em `/collections/new-balance-todos-os-modelos`, canonical da coleção geral New Balance, 2 redirects.
  - `/collections/new-balance-740` → HTTP 200 final em `/collections/new-balance-todos-os-modelos`, canonical da coleção geral New Balance, 1 redirect.
- `collectionByHandle(handle: "new-balance-740")` retornou `null`.
- Busca Admin por coleção `New Balance 740` retornou 0 coleções.
- **Tiny/Stock OS não consultado por este perfil.** Shopify inventory apareceu no snapshot, mas não é fonte final de estoque/disponibilidade.

## 3. Snapshot antes — produto

- Produto: `Tênis New Balance 740 x Concepts Saignée Verde`
- Product GID: `gid://shopify/Product/8780230492382`
- legacy ID: `8780230492382`
- handle: `tenis-new-balance-740-x-concepts-saignee-verde`
- status: `ARCHIVED`
- `publishedAt`: `null`
- `onlineStoreUrl`: `null`
- vendor: `New Balance`
- product type: `Tênis`
- `tracksInventory`: `true`
- `totalInventory` Shopify: `24` (**não usar como prova de disponibilidade**)
- templateSuffix: `null`
- SEO title: `New Balance 740 x Concepts Saignée Original | LK`
- SEO description: `New Balance 740 x Concepts Saignée original na LK: collab Concepts em verde, running retrô premium, curadoria e atendimento humano para escolher.`
- Tags: `Conforto`, `encomenda`, `Estilo`, `Exclusivo`, `New Balance`, `sneakers`, `Tênis`.
- Opção: `Tamanho` com valores `37`, `38`, `39`, `40`, `41`, `42`, `43`, `44`.
- Mídia: 1 imagem `READY`, 1600×1066, alt/preview presente.
- Publicações do produto: `resourcePublications` vazio; nenhuma publicação ativa retornada.
- Coleções anexadas ao produto mesmo arquivado:
  - `ultimos-lancamentos-2` — Todos os Produtos
  - `lancamentos` — Lançamentos
  - `sneakers` — Tênis e Sneakers Originais
  - `best-sellers-1` — Sneakers | Best Sellers
  - `geral-best-sellers` — Geral | Best Sellers
  - `new-balance-todos-os-modelos` — New Balance
  - `todos-special-collections` — Special Collections
  - `novidades-da-lk` — Novidades da LK

### Variantes Shopify vistas

| Tamanho | SKU | Variant legacy ID | preço | compareAt | inventoryPolicy | availableForSale no Admin |
|---|---|---:|---:|---:|---|---|
| 37 | `U740GP2-1` | 47608727912670 | 3199.99 | 3199.99 | `CONTINUE` | true |
| 38 | `U740GP2-2` | 47608727945438 | 3199.99 | 3199.99 | `CONTINUE` | true |
| 39 | `U740GP2-3` | 47608727978206 | 3199.99 | 3199.99 | `CONTINUE` | true |
| 40 | `U740GP2-4` | 47608728010974 | 3199.99 | 3199.99 | `CONTINUE` | true |
| 41 | `U740GP2-5` | 47608728043742 | 3199.99 | 3199.99 | `CONTINUE` | true |
| 42 | `U740GP2-6` | 47608728076510 | 3199.99 | 3199.99 | `CONTINUE` | true |
| 43 | `U740GP2-7` | 47608728109278 | 3199.99 | 3199.99 | `CONTINUE` | true |
| 44 | `U740GP2-8` | 47608728142046 | 3199.99 | 3199.99 | `CONTINUE` | true |

Nota: `availableForSale=true` no Admin não substitui validação Tiny/Stock OS, especialmente porque o produto está arquivado/não publicado e as variantes usam `CONTINUE`.

## 4. Alteração proposta — NÃO executar ainda

A execução abaixo só faz sentido se `lk-stock` retornar OK explícito por SKU/tamanho e Lucas aprovar o texto de aprovação no fim deste packet.

| Objeto | Campo/ação | Valor atual | Valor proposto | Motivo | Status |
|---|---|---|---|---|---|
| Produto | `status` | `ARCHIVED` | `ACTIVE` | tornar produto elegível à publicação | pendente LK Stock + aprovação Lucas |
| Produto | publicação Online Store | sem `resourcePublications` | publicar no `Online Store` (`gid://shopify/Publication/79413379294`) | permitir PDP pública | pendente LK Stock + aprovação Lucas |
| Coleção | criar coleção | `collectionByHandle("new-balance-740") = null` | coleção manual/smart com handle `new-balance-740` | superfície canônica da frente New Balance 740 | pendente produto publicável + aprovação Lucas |
| Coleção | associar produto | não existe | incluir `gid://shopify/Product/8780230492382` | evitar coleção vazia | pendente produto ativo/publicado |
| Coleção | publicar Online Store | não existe | publicar no Online Store | expor `/collections/new-balance-740` | pendente coleção criada/aprovada |

Não proponho alterar preço, estoque, SKU, tag, SEO, metafield, tema, menu, GMC, Klaviyo, Meta, WhatsApp, Tiny ou campanha neste packet.

## 5. Padrão canônico aplicado

- `lk-shopify-readonly` para evidência Shopify sem write.
- Template `areas/lk/sub-areas/shopify/templates/preview-aprovacao-shopify.md`.
- Regra LK Stock: Tiny/Stock OS é fonte final para estoque/disponibilidade; este perfil não validou nem promete disponibilidade.
- Fronteira LKGOC/Collection Optimizer: não criar coleção vazia; frente só destrava com produto ativo/publicado ou plano de correção aprovado.

## 6. Readback e verificação esperados se houver aprovação futura

1. Antes do write: salvar JSON Admin completo do produto, variantes, coleções associadas e publicações.
2. Após `productUpdate(status: ACTIVE)`: readback Admin deve retornar `status=ACTIVE` mantendo handle/SEO/tags/variantes.
3. Após publicação Online Store: readback Admin deve retornar `publishedAt` preenchido e `onlineStoreUrl` não nulo.
4. Após criação/associação de coleção: `collectionByHandle("new-balance-740")` deve retornar ID/handle/produto associado.
5. Public readback:
   - `/products/tenis-new-balance-740-x-concepts-saignee-verde` deve resolver para PDP/canonical do produto, não redirecionar para coleção geral.
   - `/collections/new-balance-740` deve resolver para a coleção canônica, não redirecionar para `new-balance-todos-os-modelos`.
6. Provar que nada fora do escopo mudou comparando snapshot antes/depois dos campos listados.

## 7. Rollback

- Produto: restaurar `status=ARCHIVED` e remover publicação do Online Store se ela tiver sido adicionada.
- Coleção nova: remover/arquivar a coleção `new-balance-740` e remover associação do produto.
- Campos não alterados: preço, estoque, SKUs, SEO, tags, metafields e tema devem permanecer iguais; se qualquer diff aparecer, restaurar via snapshot.
- Tiny/Stock: não há rollback deste perfil porque nenhum Tiny write é proposto.

## 8. O que NÃO está aprovado

- Reativar produto agora.
- Publicar produto agora.
- Criar/editar/publicar coleção agora.
- Alterar preço, estoque, SKU, Tiny, SEO, tags, metafields, tema, menu, GMC, Klaviyo, Meta, WhatsApp, campanha ou checkout.
- Usar Shopify inventory como prova de disponibilidade.
- Prometer pronta entrega ou venda sem evidência do `lk-stock`.

## 9. Texto de aprovação futuro para Telegram

Usar somente se `lk-stock` responder `publicável`/OK por SKU/tamanho e Lucas quiser executar:

> Aprovo LK Shopify executar exatamente este preview para New Balance 740: reativar o produto `gid://shopify/Product/8780230492382` (`tenis-new-balance-740-x-concepts-saignee-verde`) de `ARCHIVED` para `ACTIVE`, publicar no canal `Online Store`, criar/publicar a coleção `new-balance-740` e associar somente esse produto, com snapshot antes, readback Admin+público, receipt e rollback. Não aprovo preço, estoque, SKU, Tiny, SEO, tags, metafields, tema, menu, GMC, Klaviyo, Meta, WhatsApp, campanha ou checkout fora do que está listado.

## 10. Continuidade / bloqueio

- Kanban LK Stock criado: `t_55c1f648` — validar Tiny/Stock OS para publicabilidade New Balance 740.
- Status atual recomendado: **bloqueado aguardando `lk-stock`**.
- Próxima ação concreta: `lk-stock` classificar SKUs/tamanhos como `publicável`, `não publicável`, `precisa correção SKU/Tiny` ou `indisponível/sem venda`.
- Gatilho de retomada: resposta do `lk-stock` ou nova decisão explícita de Lucas mantendo arquivado.
- Reminder OS loop needed: yes.


## Atualização Stock final — 2026-06-26T09:18Z

LK Stock concluiu a validação (`t_55c1f648`): os 8 SKUs/tamanhos `U740GP2-1`…`U740GP2-8` têm match exato Shopify↔Tiny, mas saldo `0` no depósito Tiny `LK | CONTROLE ESTOQUE`. Classificação: `indisponível/sem venda` / `não publicável por estoque`. Portanto, este packet permanece **bloqueado/não executável**; não reativar, publicar ou criar coleção para New Balance 740 salvo nova entrada de estoque ou nova aprovação comercial separada.
