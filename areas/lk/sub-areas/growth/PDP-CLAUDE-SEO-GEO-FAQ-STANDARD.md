# LK PDP Claude-SEO / GEO / FAQPage Standard

Status: canônico para Growth LK a partir de 2026-06-19.

## Objetivo

Todo PDP otimizado para SEO/GEO/AI Visibility deve ser validado como conteúdo público rastreável, não apenas como dado salvo no Shopify Admin.

## Gate obrigatório antes de chamar “pronto para IA”

1. `body_html` limpo: descrição editorial/comercial, sem FAQ embutida, sem `<dt>/<dd>` de perguntas e sem blocos `lk-growth-faq`.
2. FAQ de produto em estrutura própria: preferencialmente `product.metafields.custom.faq` JSON array `{q,a}`.
3. FAQ visual público: as perguntas/respostas do `custom.faq` aparecem no HTML público, no bloco próprio do tema.
4. JSON-LD público: existe `FAQPage` com as mesmas perguntas/respostas do bloco visual.
5. Paridade: se `custom.faq` existe, o `FAQPage` deve conter apenas a FAQ do produto; FAQ institucional entra somente como fallback quando não houver FAQ de produto.
6. GEO/AI readability: perguntas naturais de intenção real, respostas declarativas, entidade explícita, sem promessas médicas/estoque/prazo, com contexto suficiente para citação.
7. Validação pública estável: passar em múltiplas amostras públicas sem `preview_theme_id`; preview/Admin isoladamente não bastam.

## Claude-SEO lens

- `seo-content`: copy específica, útil, humana, sem filler genérico.
- `seo-ecommerce`: produto, marca, modelo, cor, uso e objeções de compra claros.
- `seo-schema`: Product/Breadcrumb/FAQPage válidos e sem duplicidade ruim.
- `seo-geo`: frases extraíveis, perguntas reais, respostas citáveis, entidades explícitas.

## Status possíveis

- `admin_ok`: Shopify Admin/metafields corretos, mas público não validado.
- `preview_ok`: tema/preview corretos, mas público ainda não confirmado.
- `public_ok`: HTML público + JSON-LD público passam no gate.
- `blocked_public_cache`: preview passa, público serve render antigo.

## Regra de operação

Não replicar em massa enquanto o status não for `public_ok` em pelo menos uma página piloto.
