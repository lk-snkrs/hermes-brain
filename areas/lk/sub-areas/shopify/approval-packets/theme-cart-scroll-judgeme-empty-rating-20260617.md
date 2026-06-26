# Approval packet — Cart drawer scroll + Judge.me empty rating gap

Data: 2026-06-17
values_printed=false

## Pedido Lucas
1. Corrigir drawer do carrinho: quando abre, o scroll não funciona e fica preso no fundo.
2. Corrigir PDP: quando produto não tem rating no Judge.me, remover o espaço vazio do badge.

## Status
Patch local preparado em worktree limpo baseado em `origin/production` local.

Worktree:
`/opt/data/worktrees/lk-new-theme-cart-scroll-judgeme-rating-20260617`

Branch local:
`fix/cart-scroll-judgeme-empty-rating-20260617`

## Arquivos alterados
- `snippets/lk-cart-drawer.liquid`
- `sections/lk-pdp.liquid`
- `snippets/judgeme_widgets.liquid`

## Diagnóstico
### 1) Cart drawer scroll
O drawer é `display:flex`, mas o wrapper dinâmico `#cart-drawer-body` não participava como coluna flex com `min-height:0`. Resultado: o bloco `.cart-drawer__items` tinha `overflow-y:auto`, mas sem limite de altura confiável; em carrinho cheio/mobile, o conteúdo empurrava footer/CTA e o scroll ficava preso no fundo/página.

### 2) Espaço vazio Judge.me na PDP
A PDP sempre renderizava o `<a class="pi-rating-link">` com margem `8px 0 4px`, mesmo quando o snippet Judge.me não tinha conteúdo útil. Em produto sem avaliação, o conteúdo ficava vazio, mas o container continuava ocupando espaço.

## Mudança proposta
### Cart drawer
Adicionar ao CSS:
- `#cart-drawer-body { flex: 1 1 auto; min-height: 0; display:flex; flex-direction:column; overflow:hidden; }`
- `.cart-drawer__items { flex:1 1 auto; min-height:0; overflow-y:auto; overscroll-behavior:contain; }`

Efeito esperado:
- Header, shipping bar, upsell e footer ficam preservados.
- A lista de itens vira a área rolável real.
- Mobile não deve mais ficar preso no fundo.

### Judge.me PDP
- Criar guard Liquid baseado em:
  - `product.metafields.judgeme.review_widget_data.value.number_of_reviews > 0`
  - badge não vazio
  - badge diferente de `<div></div>`
- Só renderizar o `<a class="pi-rating-link">` quando houver avaliação real.
- Ajustar o snippet `judgeme_widgets` para o preview badge não emitir wrapper vazio.

Efeito esperado:
- Produto com rating: badge continua aparecendo e clicável.
- Produto sem rating: nenhum espaço vazio entre título e colorway/preço.

## Verificação local executada
- `git diff --check`: OK.
- Contagem de tags Liquid nos 3 arquivos alterados: pares `{% %}` e `{{ }}` balanceados.
- Substrings esperadas confirmadas:
  - `#cart-drawer-body`
  - `overscroll-behavior: contain`
  - `lk_show_jdgm_preview_badge`
  - `jdgm_preview_count > 0`

## Risco
Baixo/médio.

- Cart drawer: CSS estrutural do drawer; precisa QA mobile com carrinho cheio para garantir footer/checkout visíveis.
- Judge.me: guard depende do metafield `judgeme.review_widget_data`; se produto tiver badge mas metadado de contagem ausente, o badge não aparecerá. Isso é aceitável para o pedido atual porque o objetivo é evitar espaço vazio quando não há avaliação.

## QA necessário em Dev preview
1. PDP com avaliação:
   - badge aparece;
   - click abre modal/scroll reviews;
   - layout não muda indevidamente.
2. PDP sem avaliação:
   - badge não aparece;
   - não há espaço vazio entre título e próximo bloco.
3. Cart drawer desktop/mobile:
   - abrir drawer com 1 item;
   - abrir drawer com vários itens;
   - scroll interno funciona;
   - footer/CTA checkout permanece acessível;
   - qty +/- e remover continuam funcionando;
   - fechar por X, overlay e ESC.

## Rollback
Reverter os 3 arquivos para `origin/production` ou restaurar backup antes do upload no Dev theme.

## Aprovação necessária
Para eu subir em **Dev/unpublished theme preview**, preciso aprovação explícita atual de Lucas para esse escopo:

- Upload Dev theme somente dos 3 arquivos listados.
- Sem produção.
- Sem produto/preço/estoque/checkout/app writes.

Production continua bloqueado até aprovação separada depois do QA.
