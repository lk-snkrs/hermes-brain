# Regra LKGOC — remover FAQ/descrição legado `coll-rich-content`

Atualizada em: 2026-06-05T17:42:57

## Correção de Lucas
Sempre que uma coleção for otimizada com LKGOC, o bloco legado da descrição/FAQ antigo **não pode permanecer visível**.

O bloco legado identificado é:
- `class="coll-rich-content"`
- especialmente quando contém o título **"Perguntas frequentes"**.

## Regra obrigatória
Ao aplicar LKGOC em qualquer coleção:

1. Remover, ocultar ou condicionar fora do render da coleção otimizada o bloco antigo `coll-rich-content`.
2. Não deixar duas áreas de FAQ na mesma landing: FAQ novo LKGOC + FAQ antigo da descrição/tema.
3. O FAQ visível deve ser o FAQ do padrão LKGOC, com layout, tom e schema controlados pelo LKGOC.
4. A descrição antiga da coleção pode continuar como dado de Shopify/SEO, mas não deve aparecer como bloco visual legado abaixo da coleção otimizada.
5. A verificação `coll-rich-content` ausente é QA obrigatório antes de preview, approval e merge para Production.

## QA obrigatório
Em toda coleção LKGOC, validar no DOM renderizado:

```js
!document.querySelector('.coll-rich-content')
```

ou, se a seção existir para outras coleções no template global, validar que ela está oculta/removida no escopo da coleção otimizada:

```js
getComputedStyle(document.querySelector('.coll-rich-content')).display === 'none'
```

Também validar que o texto "Perguntas frequentes" não aparece duplicado fora do bloco LKGOC aprovado.

## Motivo
O `coll-rich-content` antigo polui a experiência premium, duplica conteúdo e quebra o padrão visual LKGOC. A otimização LKGOC deve substituir a experiência editorial/FAQ antiga, não somar por cima dela.
