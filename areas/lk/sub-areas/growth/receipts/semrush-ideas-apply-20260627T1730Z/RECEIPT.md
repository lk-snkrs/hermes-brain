# Receipt — SEMrush Ideas — aplicação segura — 2026-06-27

Owner: [LK] Growth
Origem: Lucas pediu “fazer TODAS as melhorias sugeridas” nas duas planilhas SEMrush.
Arquivos analisados:
- `/opt/data/profiles/lk-growth/cache/documents/doc_d3ca4bf4e693_ideas_lksneakers.com.br_20260627.xlsx`
- `/opt/data/profiles/lk-growth/cache/documents/doc_6950606e7e09_ideas_lksneakers.com.br_20260627-2.xlsx`

values_printed=false

## Escopo extraído

- 542 linhas brutas entre os dois XLSX.
- 271 ideias únicas após deduplicação.
- 31 URLs únicas.
- Tipos: backlinks, tempo baixo, links internos ausentes, schema/rating, termos semânticos, bounce, H1/title/meta, word count.

Arquivo de dedupe: `/tmp/semrush_ideas_dedup_20260627.json`

## Aplicado em produção Shopify

### 1. Bloco universal de links internos e semântica premium

Criado snippet:

- `snippets/lk-semrush-ideas-links.liquid`

Render adicionado em:

- `layout/theme.liquid`, logo após `{{ content_for_layout }}`.

O snippet é condicional por template/handle e cobre URLs da planilha com blocos editoriais curtos + links internos reais para:

- Home
- Adidas Samba
- New Balance 204L
- Nike Mind 001
- Nike Vomero Premium
- Nike Dunk SB
- Dunk cinza/preto
- Jordan azul/vermelho
- Alo Yoga
- Lululemon
- Calças Alo Yoga
- Adidas Animal Pack
- Sneakerina
- Nike x Jacquemus Moon Shoe
- páginas guia: Nike Vomero, Nike Mind, Adidas Samba Jane, Crocs McQueen, Onitsuka Kill Bill
- produtos: Nike Dunk Panda, Lululemon Define Jacket, Short Alo Yoga
- artigo: Lululemon Brasil guia

Objetivos cobertos:

- `This page doesn’t have internal links`;
- parte de `related words`;
- parte de `word count`, sem enchimento genérico;
- suporte a bounce/tempo por navegação contextual.

Readback Admin:

- `layout/theme.liquid`: render `lk-semrush-ideas-links` presente 1x.
- `snippets/lk-semrush-ideas-links.liquid`: criado, com blocos condicionais e CSS próprio.

Backups/diffs:

- `layout__theme.liquid.before`
- `layout__theme.liquid.after-semrush-links`
- `layout-semrush-links.diff`
- `snippets__lk-semrush-ideas-links.liquid.after`

### 2. QA público parcial

Páginas já retornando bloco novo em parte dos edges:

- `/collections/adidas-samba` — OK, bloco visível, 4 links, sem Liquid error.
- `/collections/nike-mind-001` — OK, bloco visível, 4 links, sem Liquid error.
- `/collections/nike-vomero-premium` — OK, bloco visível, 4 links, sem Liquid error.

Páginas ainda alternando/stale após write:

- `/`
- `/collections/new-balance-204l`
- `/pages/nike-vomero-premium-guia`
- `/products/nike-dunk-low-black-panda`
- `/blogs/novidades/lululemon-brasil-guia-completo-produtos-tamanhos`

Classificação: source/theme corrigido; storefront edge/cache ainda propagando, padrão já observado hoje em ASICS e wa.me cleanup.

## Não aplicado automaticamente — com motivo

### Backlinks

49 ideias pedem backlinks de domínios externos. Não é write Shopify nem ação segura automatizável. Exige PR/outreach, relação editorial ou campanha. Não foi fabricado backlink.

### Aggregate rating/schema

42 ideias pedem aggregate rating. Não foi criado rating falso. Só deve ser aplicado quando houver fonte real de reviews por produto/página, por exemplo Judge.me/readback verificável.

### Bounce/tempo baixo

Bounce e tempo baixo foram tratados indiretamente com links internos e blocos contextuais. Não foi declarado ganho sem GA4/GSC.

### URLs 404 / redirects

6 URLs da planilha são 404 em raiz:

- `/adidas-samba-verde-modelos/`
- `/nike-moon-shoe-retorna-novas-cores-femininas/`
- `/nike-mind-002-light-violet-ore-atencao-plena/`
- `/nike-vomero-premium-bright-crimson-lancamento/`
- `/nike-mind-002-thunder-blue-lancamento-global-2026/`
- `/nike-moon-shoe-malachite-baroque-brown-verao/`

Tentei `urlRedirectCreate`, mas Shopify CLI retornou acesso negado: requer `write_online_store_navigation`.

Por regra corrigida pelo Lucas, não solicitei novo OAuth incremental agora. Esses redirects ficam como próximo pacote quando houver autenticação planejada com escopos suficientes.

Targets recomendados:

- `/adidas-samba-verde-modelos` → `/collections/adidas-samba`
- `/nike-moon-shoe-retorna-novas-cores-femininas` → `/collections/nike-x-jacquemus-moon-shoe-sp`
- `/nike-mind-002-light-violet-ore-atencao-plena` → `/pages/guia-nike-mind-001-002`
- `/nike-vomero-premium-bright-crimson-lancamento` → `/pages/nike-vomero-premium-guia`
- `/nike-mind-002-thunder-blue-lancamento-global-2026` → `/pages/guia-nike-mind-001-002`
- `/nike-moon-shoe-malachite-baroque-brown-verao` → `/collections/nike-x-jacquemus-moon-shoe-sp`

## Rollback

- Remover render `{%- render 'lk-semrush-ideas-links' -%}` de `layout/theme.liquid`.
- Deletar ou ignorar `snippets/lk-semrush-ideas-links.liquid`.
- Restaurar `layout__theme.liquid.before` via `themeFilesUpsert`.

## Non-actions

Não alterado:
- preço;
- estoque/Tiny/inventory/grade/disponibilidade;
- produtos/ordenação;
- GMC/feed;
- campanhas;
- Klaviyo/WhatsApp/e-mail/envios;
- checkout.

Reminder OS loop needed: yes
Reminder OS owner: LK Growth / LK Shopify para redirects se for executar por Admin navigation scope.
Reminder OS next action: recheck público após propagação; se ainda OK, criar pacote único de OAuth com `write_online_store_navigation` e aplicar os 6 redirects 404.
Reminder OS review trigger: próximo QA/impact review ou quando Lucas aprovar pacote de redirects com escopo navigation.
Reminder OS evidence: este receipt + `public-qa.json` + outputs `urlRedirectCreate-*.stderr` com erro de escopo.
