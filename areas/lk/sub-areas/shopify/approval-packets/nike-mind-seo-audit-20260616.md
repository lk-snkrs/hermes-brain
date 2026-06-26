# Approval Packet — Auditoria SEO Nike Mind 001/002 — 2026-06-16

## Escopo

Auditoria read-only da família Nike Mind no Shopify:

- Mind 002: 7 PDPs
- Mind 001: 11 PDPs
- Total: 18 PDPs

Nenhum write foi executado nesta auditoria.

## Fontes

- Shopify Admin GraphQL read-only: produto, SEO title, SEO description, metafields SEO globais
- HTML público live: `<title>`, meta description, H1 e Liquid errors

Artefatos:

- `reports/assets/nike-mind-seo-audit-20260616/nike-mind-seo-audit-readonly-seo-only.json`
- `reports/assets/nike-mind-seo-audit-20260616/nike-mind-seo-recommendations.json`

## Resultado executivo

Resumo por prioridade:

- P1: 6 PDPs — corrigir primeiro
- P2: 4 PDPs — padronização importante
- P3: 8 PDPs — já aceitáveis ou polish editorial

Principais problemas encontrados:

- 5 PDPs com SEO title vazio no Admin
- 5 PDPs com SEO description vazia no Admin
- 7 PDPs com title live longo
- 6 PDPs com meta live longa
- 6 PDPs com preço/parcelamento aparecendo no title live
- 3 PDPs com preço aparecendo na meta description

## P1 — Aplicar primeiro

Estes PDPs têm campos vazios, title/meta longos ou preço no title.

### Tênis Nike Mind 002 Grey Football Grey Cinza

Handle: `tenis-nike-mind-002-grey-football-grey-cinza`  
URL: `https://lksneakers.com.br/products/tenis-nike-mind-002-grey-football-grey-cinza`  
Problemas: SEO title vazio no Admin, SEO description vazia no Admin, title live longo, meta live longa, preço/parcelamento no title

Atual:

- SEO title Admin: `None`
- SEO description Admin: `None`
- HTML title length: `85`
- HTML meta length: `320`

Proposto:

- SEO title: `Tênis Nike Mind 002 Grey Football Grey | LK Sneakers` (`52` chars)
- SEO description: `Nike Mind 002 Grey Football Grey original. Design escultural Nike, curadoria LK, atendimento humano e compra segura em até 10x sem juros.` (`137` chars)

### Tênis Nike Mind 002 Sail Bege

Handle: `tenis-nike-mind-002-sail-bege`  
URL: `https://lksneakers.com.br/products/tenis-nike-mind-002-sail-bege`  
Problemas: title live longo, meta live longa, preço/parcelamento no title

Atual:

- SEO title Admin: `Tênis Nike Mind 002 Sail Bege | LK Sneakers`
- SEO description Admin: `Nike Mind 002 Sail Bege original. Design escultural Nike, curadoria LK, atendimento humano e compra segura em até 10x sem juros.`
- HTML title length: `70`
- HTML meta length: `320`

Proposto:

- SEO title: `Tênis Nike Mind 002 Sail | LK Sneakers` (`38` chars)
- SEO description: `Nike Mind 002 Sail original. Design escultural Nike, curadoria LK, atendimento humano e compra segura em até 10x sem juros.` (`123` chars)

### Chinelo Slide Nike Mind 001 Blackened Blue Azul

Handle: `slide-nike-mind-001-blackened-blue-azul`  
URL: `https://lksneakers.com.br/products/slide-nike-mind-001-blackened-blue-azul`  
Problemas: SEO title vazio no Admin, SEO description vazia no Admin, title live longo, meta live longa, preço/parcelamento no title

Atual:

- SEO title Admin: `None`
- SEO description Admin: `None`
- HTML title length: `88`
- HTML meta length: `319`

Proposto:

- SEO title: `Slide Nike Mind 001 Blackened Blue | LK Sneakers` (`48` chars)
- SEO description: `Nike Mind 001 Blackened Blue original. Slide escultural Nike com curadoria LK, atendimento humano para tamanho e compra em até 10x sem juros.` (`141` chars)

### Chinelo Slide Nike Mind 001 Mineral Slate Verde

Handle: `slide-nike-mind-001-mineral-slate-verde`  
URL: `https://lksneakers.com.br/products/slide-nike-mind-001-mineral-slate-verde`  
Problemas: SEO title vazio no Admin, SEO description vazia no Admin, title live longo, meta live longa, preço/parcelamento no title

Atual:

- SEO title Admin: `None`
- SEO description Admin: `None`
- HTML title length: `88`
- HTML meta length: `320`

Proposto:

- SEO title: `Slide Nike Mind 001 Mineral Slate | LK Sneakers` (`47` chars)
- SEO description: `Nike Mind 001 Mineral Slate original. Slide escultural Nike com curadoria LK, atendimento humano para tamanho e compra em até 10x sem juros.` (`140` chars)

### Chinelo Slide Nike Mind 001 'Team Red' Vermelho

Handle: `slide-nike-mind-001-team-red-vermelho`  
URL: `https://lksneakers.com.br/products/slide-nike-mind-001-team-red-vermelho`  
Problemas: SEO title vazio no Admin, SEO description vazia no Admin, title live longo, meta live longa, preço/parcelamento no title

Atual:

- SEO title Admin: `None`
- SEO description Admin: `None`
- HTML title length: `88`
- HTML meta length: `320`

Proposto:

- SEO title: `Slide Nike Mind 001 Team Red | LK Sneakers` (`42` chars)
- SEO description: `Nike Mind 001 Team Red original. Slide escultural Nike com curadoria LK, atendimento humano para tamanho e compra em até 10x sem juros.` (`135` chars)

### Chinelo Slide Nike Mind 001 White Speed Red Branco

Handle: `slide-nike-mind-001-white-speed-red-branco`  
URL: `https://lksneakers.com.br/products/slide-nike-mind-001-white-speed-red-branco`  
Problemas: SEO title vazio no Admin, SEO description vazia no Admin, title live longo, meta live longa, preço/parcelamento no title

Atual:

- SEO title Admin: `None`
- SEO description Admin: `None`
- HTML title length: `91`
- HTML meta length: `320`

Proposto:

- SEO title: `Slide Nike Mind 001 White Speed Red | LK Sneakers` (`49` chars)
- SEO description: `Nike Mind 001 White Speed Red original. Slide escultural Nike com curadoria LK, atendimento humano para tamanho e compra em até 10x sem juros.` (`142` chars)


## P2 — Padronização importante

Estes PDPs já têm SEO, mas ainda carregam preço na meta ou title acima do ideal.

### Tênis Nike Mind 002 Black Hyper Crimson Preto

Handle: `tenis-nike-mind-002-black-hyper-crimson-preto`  
URL: `https://lksneakers.com.br/products/tenis-nike-mind-002-black-hyper-crimson-preto`  
Problemas: preço/parcelamento na meta

Atual:

- SEO title Admin: `Tênis Nike Mind 002 Black Hyper Crimson Preto | LK Sneakers`
- SEO description Admin: `Tênis Nike Mind 002 Black Hyper Crimson Preto original. a partir de R$ 3200 em 10x sem juros. Curadoria LK · Frete grátis +R$500 · LK Sneakers`
- HTML title length: `59`
- HTML meta length: `142`

Proposto:

- SEO title: `Tênis Nike Mind 002 Black Hyper Crimson | LK Sneakers` (`53` chars)
- SEO description: `Nike Mind 002 Black Hyper Crimson original. Design escultural Nike, curadoria LK, atendimento humano e compra segura em até 10x sem juros.` (`138` chars)

### Tênis Nike Mind 002 Light Smoke Grey Cinza

Handle: `tenis-nike-mind-002-light-smoke-grey-cinza`  
URL: `https://lksneakers.com.br/products/tenis-nike-mind-002-light-smoke-grey-cinza`  
Problemas: preço/parcelamento na meta

Atual:

- SEO title Admin: `Tênis Nike Mind 002 Light Smoke Grey Cinza | LK Sneakers`
- SEO description Admin: `Tênis Nike Mind 002 Light Smoke Grey Cinza original. a partir de R$ 3200 em 10x sem juros. Curadoria LK · Frete grátis +R$500 · LK Sneakers`
- HTML title length: `56`
- HTML meta length: `139`

Proposto:

- SEO title: `Tênis Nike Mind 002 Light Smoke Grey | LK Sneakers` (`50` chars)
- SEO description: `Nike Mind 002 Light Smoke Grey original. Design escultural Nike, curadoria LK, atendimento humano e compra segura em até 10x sem juros.` (`135` chars)

### Chinelo Slide Nike Mind 001 Light Smoke Grey Cinza

Handle: `slide-nike-mind-001-light-smoke-grey-cinza`  
URL: `https://lksneakers.com.br/products/slide-nike-mind-001-light-smoke-grey-cinza`  
Problemas: preço/parcelamento na meta

Atual:

- SEO title Admin: `Slide Nike Mind 001 Light Smoke Grey Cinza | LK Sneakers`
- SEO description Admin: `Slide Nike Mind 001 Light Smoke Grey Cinza original. a partir de R$ 3200 em 10x sem juros. Curadoria LK · Frete grátis +R$500 · LK Sneakers`
- HTML title length: `56`
- HTML meta length: `139`

Proposto:

- SEO title: `Slide Nike Mind 001 Light Smoke Grey | LK Sneakers` (`50` chars)
- SEO description: `Nike Mind 001 Light Smoke Grey original. Slide escultural Nike com curadoria LK, atendimento humano para tamanho e compra em até 10x sem juros.` (`143` chars)

### Chinelo Slide Nike Mind 001 Solar Red Vermelho

Handle: `slide-nike-mind-001-solar-red-vermelho`  
URL: `https://lksneakers.com.br/products/slide-nike-mind-001-solar-red-vermelho`  
Problemas: title live longo

Atual:

- SEO title Admin: `Nike Mind 001 Slide Solar Red Original — Slide Premium | LK Sneakers`
- SEO description Admin: `Slide Nike Mind 001 Solar Red vermelho original. Design premium exclusivo. 10x sem juros. ✓ 100% autêntico ✓ Frete grátis ✓ Edição limitada`
- HTML title length: `68`
- HTML meta length: `139`

Proposto:

- SEO title: `Slide Nike Mind 001 Solar Red | LK Sneakers` (`43` chars)
- SEO description: `Nike Mind 001 Solar Red original. Slide escultural Nike com curadoria LK, atendimento humano para tamanho e compra em até 10x sem juros.` (`136` chars)


## P3 — Polish editorial / já aceitáveis

Estes PDPs estão aceitáveis no SEO técnico, mas podem receber padronização de família.

### Tênis Nike Mind 002 Light Khaki Bege

Handle: `tenis-nike-mind-002-light-khaki-bege`  
URL: `https://lksneakers.com.br/products/tenis-nike-mind-002-light-khaki-bege`  
Problemas: sem problema crítico

Atual:

- SEO title Admin: `Tênis Nike Mind 002 Light Khaki Bege | LK Sneakers`
- SEO description Admin: `Nike Mind 002 Light Khaki Bege original. Design escultural Nike, curadoria LK, atendimento humano e compra segura em até 10x sem juros.`
- HTML title length: `50`
- HTML meta length: `135`

Proposto:

- SEO title: `Tênis Nike Mind 002 Light Khaki | LK Sneakers` (`45` chars)
- SEO description: `Nike Mind 002 Light Khaki original. Design escultural Nike, curadoria LK, atendimento humano e compra segura em até 10x sem juros.` (`130` chars)

### Tênis Nike Mind 002 Light Violet Ore Roxo

Handle: `tenis-nike-mind-002-light-violet-ore-roxo`  
URL: `https://lksneakers.com.br/products/tenis-nike-mind-002-light-violet-ore-roxo`  
Problemas: sem problema crítico

Atual:

- SEO title Admin: `Tênis Nike Mind 002 Light Violet Ore | LK Sneakers`
- SEO description Admin: `Nike Mind 002 Light Violet Ore original. Design escultural Nike, curadoria LK, atendimento humano e compra segura em até 10x sem juros.`
- HTML title length: `50`
- HTML meta length: `135`

Proposto:

- SEO title: `Tênis Nike Mind 002 Light Violet Ore | LK Sneakers` (`50` chars)
- SEO description: `Nike Mind 002 Light Violet Ore original. Design escultural Nike, curadoria LK, atendimento humano e compra segura em até 10x sem juros.` (`135` chars)

### Tênis Nike Mind 002 Thunder Blue Azul

Handle: `tenis-nike-mind-002-thunder-blue-azul`  
URL: `https://lksneakers.com.br/products/tenis-nike-mind-002-thunder-blue-azul`  
Problemas: sem problema crítico

Atual:

- SEO title Admin: `Tênis Nike Mind 002 Thunder Blue | LK Sneakers`
- SEO description Admin: `Nike Mind 002 Thunder Blue original. Modelo lifestyle Nike com design escultural, curadoria LK, compra segura e até 10x sem juros.`
- HTML title length: `46`
- HTML meta length: `130`

Proposto:

- SEO title: `Tênis Nike Mind 002 Thunder Blue | LK Sneakers` (`46` chars)
- SEO description: `Nike Mind 002 Thunder Blue original. Design escultural Nike, curadoria LK, atendimento humano e compra segura em até 10x sem juros.` (`131` chars)

### Nike Mind 001 Black Chrome original

Handle: `slide-nike-mind-001-black-chrome-preto`  
URL: `https://lksneakers.com.br/products/slide-nike-mind-001-black-chrome-preto`  
Problemas: sem problema crítico

Atual:

- SEO title Admin: `Nike Mind 001 Black Chrome Original no Brasil | LK`
- SEO description Admin: `Nike Mind 001 Black Chrome original no Brasil: slide escultural da linha Nike Mind com curadoria exclusiva LK, autenticidade e atendimento humano.`
- HTML title length: `50`
- HTML meta length: `146`

Proposto:

- SEO title: `Slide Nike Mind 001 Black Chrome | LK Sneakers` (`46` chars)
- SEO description: `Nike Mind 001 Black Chrome original. Slide escultural Nike com curadoria LK, atendimento humano para tamanho e compra em até 10x sem juros.` (`139` chars)

### Chinelo Slide Nike Mind 001 Geode Teal Verde

Handle: `slide-nike-mind-001-geode-teal-verde`  
URL: `https://lksneakers.com.br/products/slide-nike-mind-001-geode-teal-verde`  
Problemas: sem problema crítico

Atual:

- SEO title Admin: `Slide Nike Mind 001 Geode Teal | LK Sneakers`
- SEO description Admin: `Nike Mind 001 Geode Teal original. Slide escultural Nike com curadoria LK, atendimento humano para tamanho e compra em até 10x sem juros.`
- HTML title length: `44`
- HTML meta length: `137`

Proposto:

- SEO title: `Slide Nike Mind 001 Geode Teal | LK Sneakers` (`44` chars)
- SEO description: `Nike Mind 001 Geode Teal original. Slide escultural Nike com curadoria LK, atendimento humano para tamanho e compra em até 10x sem juros.` (`137` chars)

### Chinelo Slide Nike Mind 001 Light Bone Bege

Handle: `slide-nike-mind-001-light-bone-bege`  
URL: `https://lksneakers.com.br/products/slide-nike-mind-001-light-bone-bege`  
Problemas: sem problema crítico

Atual:

- SEO title Admin: `Slide Nike Mind 001 Light Bone | LK Sneakers`
- SEO description Admin: `Nike Mind 001 Light Bone original. Slide escultural Nike, curadoria LK, atendimento humano para tamanho e compra segura em até 10x.`
- HTML title length: `44`
- HTML meta length: `131`

Proposto:

- SEO title: `Slide Nike Mind 001 Light Bone | LK Sneakers` (`44` chars)
- SEO description: `Nike Mind 001 Light Bone original. Slide escultural Nike com curadoria LK, atendimento humano para tamanho e compra em até 10x sem juros.` (`137` chars)

### Chinelo Slide Nike Mind 001 Pearl Pink Rosa

Handle: `slide-nike-mind-001-pearl-pink-rosa`  
URL: `https://lksneakers.com.br/products/slide-nike-mind-001-pearl-pink-rosa`  
Problemas: sem problema crítico

Atual:

- SEO title Admin: `Slide Nike Mind 001 Pearl Pink | LK Sneakers`
- SEO description Admin: `Nike Mind 001 Pearl Pink original. Slide de design sensorial Nike com curadoria LK, atendimento humano e compra segura em até 10x.`
- HTML title length: `44`
- HTML meta length: `130`

Proposto:

- SEO title: `Slide Nike Mind 001 Pearl Pink | LK Sneakers` (`44` chars)
- SEO description: `Nike Mind 001 Pearl Pink original. Slide escultural Nike com curadoria LK, atendimento humano para tamanho e compra em até 10x sem juros.` (`137` chars)

### Chinelo Slide Nike Mind 001 Sail Bege

Handle: `slide-nike-mind-001-sail-bege`  
URL: `https://lksneakers.com.br/products/slide-nike-mind-001-sail-bege`  
Problemas: sem problema crítico

Atual:

- SEO title Admin: `Slide Nike Mind 001 Sail Bege | LK Sneakers`
- SEO description Admin: `Nike Mind 001 Sail Bege original. Slide escultural Nike com curadoria LK, atendimento humano para tamanho e compra em até 10x sem juros.`
- HTML title length: `43`
- HTML meta length: `136`

Proposto:

- SEO title: `Slide Nike Mind 001 Sail | LK Sneakers` (`38` chars)
- SEO description: `Nike Mind 001 Sail original. Slide escultural Nike com curadoria LK, atendimento humano para tamanho e compra em até 10x sem juros.` (`131` chars)


## Recomendação

Minha recomendação operacional:

1. Aplicar **P1 + P2** agora.
2. Deixar P3 sem write por enquanto, porque já está aceitável e parte foi ajustada no pacote anterior.
3. Fazer readback Admin em 100% dos produtos alterados.
4. Fazer HTML live QA em amostra: 2 Mind 002 + 2 Mind 001 + qualquer produto que tenha apresentado cache.

Se Lucas quiser consistência máxima, também é possível aplicar P1 + P2 + P3, mas isso altera PDPs que já não têm problema crítico.

## Risco

Baixo-médio.

- Não envolve preço, estoque, disponibilidade, imagens, variantes, coleção, tag ou tema.
- Envolve apenas campos Shopify Product SEO.
- Google pode demorar a refletir snippets após crawl.
- Storefront público pode servir HTML antigo temporariamente por cache após update.

## Rollback

Antes de qualquer aplicação, salvar snapshot com:

- product id
- handle
- SEO title atual
- SEO description atual
- metafields globais SEO atuais quando existirem

Rollback:

- restaurar `seo.title` e `seo.description` a partir do snapshot;
- readback Admin;
- HTML live QA em amostra.

## Aprovação necessária

Qualquer aplicação exige aprovação explícita porque é write em Shopify Product SEO fields.

Decisão sugerida:

- **Aprovar P1 + P2 Nike Mind**.
