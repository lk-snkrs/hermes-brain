# Approval packet — Cart drawer upsell position + `/cart` add button fix

- **Data:** 2026-06-25
- **Perfil:** lk-shopify
- **Superfície:** Shopify theme — cart drawer + full cart page
- **Pedido do Lucas:** corrigir 2 bugs:
  1. No cart drawer, `MAIS VENDIDOS LK` deve ficar abaixo da lista de produtos; hoje comprime/sobrepõe visualmente a lista.
  2. Na página `/cart`, clicar em `Adicionar` em produto recomendado trava/dá problema.
- **Status:** patch local preparado e validado estaticamente; **nenhum write Shopify/GitHub/tema executado neste packet**.

## Histórico/fonte verificados

- Skill aplicada: `lk-shopify-cart-drawer`.
- Referência canônica já dizia que, se upsell espreme a lista, o bloco deve entrar na mesma região scrollável da lista, não ficar entre lista e footer.
- Brain histórico encontrado:
  - `prd-cart-drawer-smart-product-match-20260617.md` registra problema de relevância/`MAIS VENDIDOS LK` no drawer.
  - receipts/packets anteriores de cart drawer e scroll confirmam padrão DEV primeiro, Production via GitHub PR/merge.
- Shopify Production readback dos assets atuais via Admin/Asset API:
  - `snippets/lk-cart-drawer.liquid` SHA atual: `1960968c3e5f41a6606d0bafb3016f4d9390f40d1b0ab8a09abc44fea01147c3`
  - `sections/lk-cart.liquid` SHA atual: `c27b971f09db3da63dc277e14b3c7bc32f4c64d8654fc115ce9962b0af8d0084`

## Diagnóstico

### 1) Cart drawer — upsell comprimindo lista

O drawer já tem `#cart-drawer-body` com flex/min-height correto, mas o bloco `cart-drawer__upsell` fica como irmão da lista e do footer:

```text
shipping
items(scroll)
upsell(fixo dentro body)
footer
```

Com carrinho cheio/mobile, o upsell ocupa altura fixa entre items e footer, deixando a lista de produtos com área visual pequena. Isso explica a imagem: aparece topo do item, mas a lista fica praticamente escondida pelo bloco `MAIS VENDIDOS LK`.

### 2) `/cart` — botão Adicionar instável

Na seção `sections/lk-cart.liquid`, o handler de add é anexado dentro de `renderCards()`, usa `data-vid`, faz `window.location.reload()` diretamente após `r.ok`, e não trata de forma robusta produto sem variante adicionável. Isso pode deixar o botão em estado ruim/travado quando a recomendação vem sem variant válida ou quando o add retorna erro.

## Patch local preparado

Workdir:

`/opt/data/profiles/lk-shopify/workdirs/cart-drawer-fix-20260625/`

Arquivos alvo locais:

- `target_snippets__lk-cart-drawer.liquid`
- `target_sections__lk-cart.liquid`

Diffs:

- `snippet.patch` — 34 linhas.
- `cart-section.patch` — 106 linhas.

### Mudanças em `snippets/lk-cart-drawer.liquid`

- Move `#cart-drawer-upsell` para **dentro** de `.cart-drawer__items`, depois dos itens.
- Faz o mesmo no render JS (`renderCart`).
- Mantém footer fora da região scrollável.
- Resultado esperado:

```text
shipping
items scrollável:
  - produtos
  - MAIS VENDIDOS LK
footer fixo abaixo
```

Isso mantém o upsell abaixo da lista sem esconder a lista de produtos.

### Mudanças em `sections/lk-cart.liquid`

- Troca listener por delegação única no container, fora de `renderCards()`.
- Botão passa a `type="button"`.
- Usa `data-variant-id` em vez de `data-vid`.
- Se não houver variante adicionável, renderiza `Indisponível` disabled.
- Remove `window.location.reload()` direto; após add OK, busca `/cart.js` e navega para `/cart`.
- Usa `credentials: 'same-origin'` e `Accept: application/json`.
- Em erro, mostra `Tentar novamente` e reabilita o botão.
- Fallback filtra produto indisponível (`p.available !== false`).

## Static QA local

Relatório:

`/opt/data/profiles/lk-shopify/workdirs/cart-drawer-fix-20260625/static_qa_patch.json`

Resultado:

- `node --check` nos scripts extraídos: **OK**.
- Drawer:
  - upsell dentro de `.cart-drawer__items` no HTML server-rendered: **OK**.
  - upsell dentro de `.cart-drawer__items` no JS render: **OK**.
  - `#cart-drawer-body` flex/min-height preservado: **OK**.
- Cart page:
  - handler único: **OK**.
  - `window.location.reload()` removido: **OK**.
  - `type="button"` + `data-variant-id`: **OK**.
  - estado `Indisponível` para sem variante: **OK**.
  - `credentials: 'same-origin'`: **OK**.

## QA necessário após DEV

1. Abrir Dev/unpublished com preview cookie.
2. Montar carrinho com 3+ itens para reproduzir overflow mobile.
3. Abrir drawer pelo ícone real do carrinho.
4. Validar:
   - lista de produtos visível;
   - `MAIS VENDIDOS LK` abaixo da lista;
   - lista scrollável;
   - footer/CTA ainda acessível;
   - sem sobreposição visual.
5. Em `/cart`, clicar `Adicionar` em recomendação e verificar:
   - não trava;
   - produto entra no carrinho ou erro reabilita botão;
   - página/cart state atualiza.

## Risco

- Theme write em 2 assets (`snippets/lk-cart-drawer.liquid`, `sections/lk-cart.liquid`).
- Impacta cart drawer e full cart page, superfícies sensíveis perto do checkout.
- Não altera checkout, preço, estoque, produto, app, campanha ou metafields.

## Rollback

- DEV: restaurar backups pré-write dos 2 assets.
- Production: reverter PR/commit do fix, aguardar Shopify sync, readback e QA.

## Addendum 2026-06-25 — Trust Grid Google reviews no `/cart`

Lucas adicionou o item 3: o Trust Grid de `https://lksneakers.com.br/cart` deve puxar a quantidade correta de avaliações do Google usando a mesma lógica do checkout.

### Evidência read-only

- `/cart` theme section tem blocks configurados; nesse caminho, o Google badge usa `block.settings.label_line2`, que está estático (`4.9 · 376 avaliações`) e ignora o metafield.
- O fallback sem blocks já tenta ler `shop.metafields.lk_google.reviews.value`, mas usa `count` e fallback `376`.
- O cron de checkout usa estado local:
  - `/opt/data/profiles/lk-shopify/cron/state/lk_google_reviews_state.json`
  - estado atual: rating `4.9`, `userRatingCount = 418`, atualizado em 2026-06-22.
- O metafield Shopify `shop.metafields.lk_google.reviews` existe, mas está stale (`count = 384`, updated `2026-04-08`), então só trocar o Liquid para metafield sem atualizar a fonte ainda não garante o número correto.

### Patch local adicionado ao target

Arquivo local:

`/opt/data/profiles/lk-shopify/workdirs/cart-drawer-fix-20260625/target_sections__lk-cart.liquid`

Mudanças preparadas:

- Define uma única fonte Liquid para o Trust Grid:
  - `shop.metafields.lk_google.reviews.value.rating`
  - `shop.metafields.lk_google.reviews.value.userRatingCount`
  - fallback `count`
  - fallback final `418`, alinhado ao cron/checkout state atual.
- Faz o caminho com `section.blocks.size > 0` ignorar `block.settings.label_line2` no Google badge e renderizar:
  - `Google<br>{{ lk_google_rating }} · {{ lk_google_review_count }} avaliações`
- Faz o fallback sem blocks usar a mesma variável.
- Atualiza o schema default de `376` para `418` para novos instanciamentos.

Static QA:

`/opt/data/profiles/lk-shopify/workdirs/cart-drawer-fix-20260625/cart_trust_grid_static_qa.json`

Resultado: `ok=true`; `node --check` OK; `376` removido do target; `userRatingCount` + metafield usados; Google block dinâmico em ambos os caminhos.

### Observação importante

Para o cart ficar **sempre correto automaticamente**, existem dois escopos possíveis:

1. **Tema somente:** `/cart` passa a puxar do metafield/fallback correto. Requer que o metafield seja mantido atualizado.
2. **Tema + fonte:** além do tema, atualizar o metafield `lk_google.reviews` para o estado atual `418` e/ou aprovar uma rotina que atualize esse metafield quando o cron detectar mudança. Isso é Shopify/metafield write recorrente e precisa aprovação explícita própria.

## Aprovação necessária

Para aplicar primeiro em DEV/unpublished somente o tema/cart:

`Aprovo DEV cart drawer + cart add + Trust Grid Google reviews`

Para já autorizar também o merge Production **após DEV readback/QA OK**:

`Aprovo DEV e merge Production cart drawer + cart add + Trust Grid Google reviews`

Escopo: assets de tema do cart (`snippets/lk-cart-drawer.liquid` e `sections/lk-cart.liquid`). Sem produto, preço, estoque, Tiny, checkout config, apps, campanhas ou GMC.

Se quiser também manter a fonte 100% automática via Shopify metafield/cron, aprovação separada necessária:

`Aprovo atualizar e manter metafield lk_google.reviews pelo cron Google Reviews`
