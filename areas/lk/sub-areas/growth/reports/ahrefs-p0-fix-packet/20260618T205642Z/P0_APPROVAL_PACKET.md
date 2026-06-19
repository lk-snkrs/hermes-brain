# P0 Approval Packet — Ahrefs technical fixes

- Status: **pronto para aprovação**, nenhum write executado.
- Evidência: Ahrefs API + Shopify Admin read-only + home HTML público.
- values_printed=false.

## Correção 1 — Mega menu Adidas Samba quebrado

- Problema: home/mega menu aponta `Adidas > Adidas Samba` para `/collections/samba-duplicata-backup-20260616`.
- Essa collection existe no Shopify como smart collection **não publicada**.
- Collection pública equivalente encontrada: `/collections/adidas-samba` publicada.
- Redirect existente para o path backup: **0**.
- Menu confirmado via GraphQL:
  - menu: `mega-menu-c-pia-1`
  - item: `gid://shopify/MenuItem/618084499678`
  - URL atual: `/collections/samba-duplicata-backup-20260616`
  - recurso atual: `gid://shopify/Collection/424590213342`

### Ação proposta
- Atualizar o item de menu para apontar para `/collections/adidas-samba` / collection `gid://shopify/Collection/468244332766`.
- Opcional: criar redirect `/collections/samba-duplicata-backup-20260616` → `/collections/adidas-samba`.

### Risco
- Baixo. É correção de link quebrado em navegação principal.

### Rollback
- Reverter menu item para URL/resource anterior; remover redirect opcional se criado.

## Correção 2 — Links de blog/conteúdo para produtos em draft

- Produtos 404 existem no Shopify, mas estão `draft`:
  - `bone-nude-project-new-varsity-cinza`
  - `camiseta-essentials-fear-of-god-plum-vinho`
  - `camiseta-essentials-fear-of-god-sycamore-verde`
  - `bone-nude-project-classique-preto`
- Redirect existente para esses paths: **0**.

### Ação proposta
- Não publicar produto e não decidir por estoque aqui.
- Não criar redirect automático se houver chance de publicar o mesmo handle no futuro.
- Corrigir links internos nos blogs/origens para collection ativa mais próxima ou remover o link.
- Arquivo de revisão: `p0-broken-url-action-review.csv`.

### Risco
- Médio se redirect for criado para handle de produto que pode voltar a ser publicado.
- Baixo se apenas corrigirmos/removermos links internos nos blogs.

### Rollback
- Snapshot do artigo antes/depois; reverter link manualmente.

## Correção 3 — Judge.me imagens quebradas

- Problema: snippet renderiza `review.pictures_urls` direto como `src`.
- Ahrefs detectou URLs como `/products/{"original"=>"https://judgeme.imgix.net/...`.
- Isso acontece quando `picture_url` é objeto/hash e não string.

### Ação proposta
- Aplicar primeiro em dev theme: se `picture_url.original` existir, usar esse valor; fallback para `huge`, `compact`, `small`, senão string original.
- Patch local gerado: `p0-judgeme_widgets.proposed.patch` — status `created`.

### Risco
- Médio/baixo; afeta bloco de fotos de reviews. Precisa testar em PDP com reviews/fotos.

### Rollback
- Reverter snippet `snippets/judgeme_widgets.liquid` para versão anterior.

## Correção 4 — Broken images externas

- 4 linhas de imagens externas/limitadas detectadas.
- Ação: substituir por asset próprio no Shopify CDN ou remover referência externa.
- Deve ser feito após localizar origem exata em conteúdo/template.

## Aprovação necessária para executar

Para seguir com writes, preciso aprovação explícita para uma destas opções:

### Opção A — segura recomendada
1. Atualizar menu Adidas Samba em produção.
2. Preparar/aplicar patch Judge.me em dev theme apenas.
3. Preparar lista de edições de blog sem publicar ainda.

### Opção B — P0 completo
1. Atualizar menu em produção.
2. Criar redirect backup → adidas-samba.
3. Aplicar patch Judge.me em dev theme e, após validação, production.
4. Editar links de blogs para produtos draft.

## Arquivos
- Pasta: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/ahrefs-p0-fix-packet/20260618T205642Z`
- `P0_APPROVAL_PACKET.md`
- `p0-broken-url-action-review.csv`
- `p0-judgeme_widgets.proposed.patch`
- `shopify-readonly/graphql-menu-samba-hits.json`
- `shopify-readonly/products-by-handle.json`
- `shopify-readonly/collections-by-handle.json`
