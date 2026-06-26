# LK Fase 1 — Diagnóstico read-only do erro HTML global

Data: 2026-05-31
Escopo: investigação read-only do erro HTML global apontado por DataForSEO.

## Resultado curto

O erro HTML global não vem da home/PDP/collection em si. Ele aparece em múltiplas páginas porque está no footer global, especificamente no bloco de ícones de pagamento gerado pelo filtro nativo Shopify `payment_type_svg_tag`.

Origem local provável:

- `sections/lk-footer.liquid`
- linhas 276–278:
  - `<div class="ft__payments">`
  - loop em `shop.enabled_payment_types`
  - `{{ type | payment_type_svg_tag: class: 'ft__payment' }}`

## Evidência DataForSEO

Páginas testadas com JS habilitado:

- `https://lksneakers.com.br/`
  - score: 94.51
  - erro: line ~3175/3176, columns 2673 e 2984
  - mensagem: `The closing tag and the currently open tag do not match.`
- `https://lksneakers.com.br/collections/sneakers`
  - score: 96.34
  - erro equivalente em linha diferente, por causa do tamanho da página
- `https://lksneakers.com.br/cart`
  - score: 93.78
  - erro equivalente em linha diferente

Como a coluna é igual e a linha muda por template, o trecho é global/repetido, não específico de uma página.

## Evidência DOM renderizado

Via `custom_js` no DataForSEO, a linha apontada no DOM renderizado contém o SVG do método de pagamento Discover:

- `<svg ... aria-labelledby="pi-discover" ...>`
- `<title id="pi-discover">Discover</title>`
- vários `<linearGradient>` e `<stop ...></stop>` serializados pelo DOM.

Os pontos reportados ficam dentro do SVG Discover, em fechamentos `</stop>` / `</linearGradient>` / `</defs>`.

## Evidência local estática

HTML público baixado com `curl`/Python:

- `home.html`: ~1.13 MB, 5.764 linhas
- `sneakers.html`: ~1.32 MB, 6.903 linhas
- `cart.html`: ~1.09 MB, 5.210 linhas

Validação com `parse5` no HTML estático:

- `home.html`: 0 parse errors
- `sneakers.html`: 0 parse errors
- `cart.html`: 0 parse errors

Interpretação: o HTML original servido pela Shopify está parseável. O alerta surge na leitura/renderização do DOM com os SVGs de pagamento, especialmente o Discover.

## Interpretação

Este é um problema técnico de baixa criticidade para SEO real:

- Não quebra indexação.
- Não afeta H1, title, canonical, OG ou conteúdo principal.
- Está no footer, global, em SVG de pagamento.
- DataForSEO marca como `resource_errors.errors`, mas a pontuação continua alta: ~93–96.

Ainda assim, é útil limpar porque reduz ruído em auditorias e evita que checks técnicos fiquem sempre acusando erro global.

## Opções de correção

### Opção A — Não mexer agora

Manter como está. Classificar como falso positivo/baixo impacto vindo do `payment_type_svg_tag`.

Prós:

- Zero risco visual.
- Zero risco de remover sinal de pagamento aceito.

Contras:

- O alerta DataForSEO continua aparecendo.

### Opção B — Remover ou substituir apenas o ícone Discover do footer

Alterar `sections/lk-footer.liquid` para tratar `type == 'discover'`:

- pular Discover; ou
- renderizar texto/acessível simples em vez do SVG Shopify.

Prós:

- Provável remoção dos 2 erros globais.
- Mudança pequena e localizada.

Contras:

- Pequena alteração visual no footer: some ou muda o badge Discover.
- Se a LK aceita Discover e quiser exibir todos os meios, pode ser indesejado.

### Opção C — Substituir todos os SVGs de pagamento por badges estáticos controlados

Trocar o output nativo Shopify por HTML/CSS próprio.

Prós:

- Controle total do HTML.
- Remove dependência dos SVGs nativos.

Contras:

- Mais alteração visual.
- Maior superfície de manutenção.

## Recomendação

Para Fase 1, recomendo **Opção A** ou **Opção B**:

- Se o objetivo é só SEO real: A, documentar como baixo impacto.
- Se o objetivo é deixar auditoria técnica limpa: B, com preview em dev antes e aprovação para produção.

## Segurança / writes

Nenhuma alteração foi feita no Shopify nesta investigação.

## Próxima decisão

Aprovar ou não um micro-ajuste no footer:

- Dev preview: substituir/remover apenas o SVG Discover no footer.
- Validar DataForSEO.
- Se sumir o erro, aplicar em Production com backup/rollback.
