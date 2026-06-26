# Approval packet — OG title da home LK

Data: 2026-05-31
Status: preview preparado; aguardando aprovação explícita para write Shopify/theme.

## Objetivo

Corrigir o `og:title` da home, que hoje aparece como `LK`, para melhorar previews em WhatsApp/social e consistência de marca.

## Campo proposto por Lucas

`LK Sneakers | Jardins SP, Originalidade Garantida, Curadoria Premium`

Comprimento: 68 caracteres.

## Evidência read-only

- HTML público atual da home: `og:title` = `LK`.
- Theme local `lk-new-theme/layout/theme.liquid` indica que, para `template.name == 'index'`, o OG title vem de:

```liquid
<meta property="og:title" content="{{ shop.name | escape }}">
```

- Isso explica o valor genérico atual, pois `shop.name` resolve como `LK`.

## Mudança técnica provável

Trocar apenas o branch da home/index para usar title fixo aprovado:

```liquid
<meta property="og:title" content="LK Sneakers | Jardins SP, Originalidade Garantida, Curadoria Premium">
```

Escopo limitado:

- apenas `layout/theme.liquid`;
- apenas `template.name == 'index'`;
- não altera produto, coleção, preço, estoque, checkout, apps, GMC, Klaviyo ou campanhas.

## Risco

Baixo, mas é write de theme Shopify. Deve passar por dev/unpublished theme primeiro ou por hotfix controlado com backup/readback, conforme aprovação de Lucas.

Riscos possíveis:

- duplicidade/override por outro snippet/app se o tema live divergir do local;
- cache social pode demorar a atualizar em alguns canais;
- alteração em `theme.liquid` afeta asset global, então deve ser extremamente localizada.

## Rollback

Restaurar a linha atual:

```liquid
<meta property="og:title" content="{{ shop.name | escape }}">
```

Guardar snapshot do asset antes de qualquer upload.

## Verificação pós-write

1. Ler asset remoto após upload e confirmar substring nova.
2. Buscar HTML público da home e confirmar:

```html
<meta property="og:title" content="LK Sneakers | Jardins SP, Originalidade Garantida, Curadoria Premium">
```

3. Confirmar que PDP/coleção seguem com seus OG titles próprios.

## Aprovação necessária

Lucas precisa aprovar explicitamente o write. Frase sugerida:

"Aprovado aplicar o OG title da home em dev theme primeiro: LK Sneakers | Jardins SP, Originalidade Garantida, Curadoria Premium"

ou, se quiser direto em produção:

"Aprovado aplicar em produção o OG title da home: LK Sneakers | Jardins SP, Originalidade Garantida, Curadoria Premium"
