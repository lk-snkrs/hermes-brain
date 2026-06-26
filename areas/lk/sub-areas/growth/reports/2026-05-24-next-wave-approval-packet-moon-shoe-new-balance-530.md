# LK Growth — Approval packet next wave: Nike Moon Shoe Jacquemus + New Balance 530

Data: 2026-05-24  
Status: **approval packet local/read-only; nenhum publish ou write executado**.  
Escopo: preparar próximo passo de LK Growth/GEO com pacote visual+técnico para revisão do Lucas.

## Veredito

Avançar faz sentido, mas **não publicar direto**. O caminho seguro é aprovar apenas um preview em dev/local para duas páginas-fonte/experiências editoriais:

1. Nike x Jacquemus Moon Shoe — consolidar a coleção existente + source page editorial.
2. New Balance 530 — criar a source page `new-balance-530-original-brasil` e conectar à coleção existente.

## Evidência consultada

### Nike x Jacquemus Moon Shoe

- Collection atual: `https://lksneakers.com.br/collections/nike-x-jacquemus-moon-shoe-sp`
- Status público: 200.
- Title público atual: `Nike x Jacquemus Moon Shoe SP | Collab 2026 | LK Sneakers`
- Meta pública atual: `Nike Jacquemus Moon Shoe SP: 6 colorways originais da collab 2026 a partir de R$ 5.000 em 10x. Estoque limitado · Entrega SP · Autenticidade.`
- Problema: a meta ainda usa linguagem operacional (`Estoque limitado`), fora do padrão atual de copy LK.
- Dossiê interno existente: `areas/lk/sub-areas/growth/reports/2026-05-23-moon-shoe-jacquemus-fashion-research.md`
- Packet anterior existente: `areas/lk/sub-areas/growth/reports/2026-05-23-moon-shoe-post-collection-custom-packet.md`
- Draft HTML local existente: `areas/lk/sub-areas/growth/drafts/2026-05-23-nike-moon-shoe-jacquemus-source-page-draft.html`
- Sinal comercial consolidado nos relatórios: 249–266 unidades e acima de R$ 1,27M–1,30M em proxy/receita combinada.
- Sinal GSC consolidado no packet anterior: 166 cliques, 5.872 impressões, CTR 2,83%, posição média 3,0.
- Fontes editoriais já consolidadas: Nike Newsroom, Vogue, WWD/Footwear News, GQ, Highsnobiety, Hypebeast/Hypebae, Sneaker Freaker, Complex, PAUSE, nss.

### New Balance 530

- Collection atual: `https://lksneakers.com.br/collections/new-balance-530`
- Status público: 200.
- Title público atual: `New Balance 530 | Clássico Raro | LK Sneakers`
- Meta pública atual: `Confira os New Balance 530 na LK Sneakers. 100% originais · Parcele em 10x · Frete grátis · Loja Jardins SP.`
- Source page sugerida: `https://lksneakers.com.br/pages/new-balance-530-original-brasil`
- Status atual da source page sugerida: 404; página ainda não existe/publicada.
- PDP orgânico citado nos relatórios: `https://lksneakers.com.br/products/tenis-new-balance-530-silver-black-cinza`
- PDP público atual status: 200.
- PDP title público atual: `Tênis New Balance 530 Silver Black Cinza por R$ 1.449,99 em até 10x | LK Sneakers`
- PDP meta pública atual: `Tênis New Balance 530 Silver Black Cinza oferece estilo e conforto incomparáveis. Conheça a nova sensação em sneakers e eleve seu visual com exclusividade!`
- Sinal GSC interno anterior: query `tenis new balance 530` apontando para esse PDP em `reports/lk-search-console-readonly-router-2026-05-11.md`.
- Sinal comercial interno anterior: New Balance 530 aparece em filas de sourcing/CRM/receita, com `revenue_signal_fact_shopify=5999.97` em `reports/lk-os-current-next-decision-queue-2026-05-13.md`.
- Fontes editoriais externas usadas para brief: New Balance/retailer references sobre 530 como retro runner com ABZORB/mesh; Vogue 2025 cita o 530 como twist contemporâneo do MR530 dos anos 2000, chunky runner com mesh exterior.

## Proposta A — Nike x Jacquemus Moon Shoe

### Objetivo

Transformar a coleção existente em uma experiência de curadoria e usar a source page como fonte citável para GEO/AI Search, sem depender só de vitrine de produto.

### URL / arquitetura

- Collection existente: `/collections/nike-x-jacquemus-moon-shoe-sp`
- Source page proposta: `/pages/nike-moon-shoe-jacquemus-guia-lk`
- Relação: collection converte; source page explica e cita.

### Campos propostos

- SEO title source page: `Nike Moon Shoe Jacquemus: história, modelos e curadoria | LK Sneakers`
- Meta source page: `Guia LK do Nike x Jacquemus Moon Shoe: origem do modelo, solado waffle, colorways, estética balletcore e por que a collab virou peça de curadoria.`
- H1 source page: `Nike x Jacquemus Moon Shoe: história, design e por que virou peça de curadoria`
- Hero sales-informed: `Tênis Nike Moon Shoe SP Jacquemus Alabaster Amarelo`
- Produto hero: `/products/nike-moon-shoe-sp-jacquemus-alabaster-amarelo`

### Estrutura da source page

1. O que é o Nike Moon Shoe?
2. Por que ele é importante para a Nike?
3. Como Jacquemus reinterpretou o modelo?
4. O que muda entre Alabaster, Off Noir, University Red, Sail, Brown e Pink?
5. Por que a moda adotou esse tênis?
6. Como a LK enxerga o Moon Shoe na curadoria?
7. FAQ citável.
8. Seleção LK relacionada.

### Blocos citáveis GEO

- Origem: Bowerman, solado waffle, década de 1970, apelido Moon Shoe.
- Collab: arquivo técnico da Nike + minimalismo Jacquemus + sneakerina/balletcore.
- Curadoria LK: produto culturalmente relevante, não volume de catálogo.

### Schema recomendado

- Source page: `Article`, `WebPage`, `BreadcrumbList`, `Organization`.
- Collection: `CollectionPage`, `ItemList`, `BreadcrumbList`.
- FAQ visível pode existir como conteúdo; não depender de rich result de FAQ para Google, já que FAQ rich result é restrito.

## Proposta B — New Balance 530

### Objetivo

Criar uma página-fonte para capturar demanda informacional/comercial de `new balance 530 original`, `tenis new balance 530`, `new balance 530 feminino/masculino`, `new balance 530 como calça`, conectando PDPs e coleção com uma narrativa de curadoria.

### URL / arquitetura

- Collection existente: `/collections/new-balance-530`
- Source page proposta: `/pages/new-balance-530-original-brasil`
- Relação: source page responde dúvidas; collection/PDPs convertem.

### Campos propostos

- SEO title: `New Balance 530 original no Brasil | Guia LK Sneakers`
- Meta description: `Guia LK do New Balance 530: história runner, design retrô, numeração, conforto ABZORB e curadoria de modelos originais.`
- H1: `New Balance 530: história, conforto e por que virou clássico de curadoria`
- Hero recomendado: PDP/coleção de maior sinal orgânico atual — começar pelo `Tênis New Balance 530 Silver Black Cinza`, com validação visual antes do preview final.

### Estrutura da source page

1. O que é o New Balance 530?
2. Por que o 530 voltou como sneaker de moda?
3. New Balance 530 é confortável? O que é ABZORB?
4. New Balance 530 combina com quais estilos?
5. Como escolher cor e numeração?
6. Como a LK seleciona New Balance 530 originais?
7. FAQ citável.
8. Seleção LK relacionada.

### Blocos citáveis GEO

- Definição: o New Balance 530 é um retro runner com leitura dos anos 1990/2000, mesh/sintético e amortecimento ABZORB.
- Tendência: o modelo voltou por unir conforto, estética dad shoe/chunky runner e versatilidade de styling.
- Curadoria LK: foco em pares originais, seleção de colorways e atendimento humano para confirmar tamanho e prazo.

### Schema recomendado

- Source page: `Article`, `WebPage`, `BreadcrumbList`, `Organization`.
- Collection: `CollectionPage`, `ItemList`, `BreadcrumbList`.
- Não usar schema de FAQ como promessa de rich result; manter FAQ como conteúdo visível e citável.

## Guardrails de copy pública

Permitido:

- `curadoria exclusiva`
- `seleção LK`
- `produto original`
- `atendimento humano`
- `confirme tamanho e prazo pelo chat`
- `história`, `design`, `colorways`, `proporção`, `conforto`, `estilo`

Evitar/remover:

- `Estoque limitado`
- `pronta entrega`
- `sob encomenda` / `encomenda`
- `consultar estoque`
- promessas de disponibilidade por tamanho/modelo
- qualquer tom de catálogo completo ou hype vazio sem fonte

## Plano técnico seguro

### Fase 1 — autorizável agora com este packet

Se Lucas aprovar, Hermes pode preparar **apenas preview/dev/local**:

1. Finalizar HTML/Markdown da source page Moon Shoe.
2. Criar HTML/Markdown da source page New Balance 530.
3. Montar blueprint Liquid/section de collection/source sem produção.
4. Validar forbidden terms.
5. Validar schema JSON-LD local.
6. Gerar rollback plan.
7. Se necessário, subir em **dev theme/unpublished** somente, com receipt e readback SHA.

### Fase 2 — exige nova aprovação separada

Não está autorizado agora:

- publicar page Shopify em produção;
- alterar collection/product SEO fields em produção;
- alterar description/body/tema em produção;
- mexer em preço, estoque, PDP, checkout, campanha, Klaviyo, WhatsApp, GMC/feed;
- linkar menu ou navegar público;
- apagar/substituir conteúdo existente.

## Rollback proposto

Para qualquer preview em dev theme:

1. Verificar theme id/name/role antes do upload.
2. Fazer backup de cada asset remoto alterado.
3. Upload somente dos assets do preview.
4. Readback por SHA e markers.
5. Rollback = reupload dos backups ou remoção dos assets novos, se não existiam.

Para eventual publicação futura de pages/SEO fields:

1. Snapshot prévio de page/collection/product SEO/body/template.
2. Mutação mínima por objeto aprovado.
3. Readback Admin + verificação pública.
4. D+7 read-only review com GSC/GA4/Shopify quando disponível.

## Pedido de aprovação recomendado ao Lucas

Aprovação segura para próximo passo:

`Aprovo preparar o preview em dev/local das source pages Nike Moon Shoe Jacquemus e New Balance 530, sem publicar em produção e sem mexer em preço, estoque, campanha, WhatsApp/Klaviyo ou GMC.`

Aprovação que **não** deve ser inferida:

- “publica”;
- “manda para cliente”;
- “altera produção”;
- “mexe no tema live”.

Essas ações precisam de outro pacote com links/prints/receipts finais.

## Próximo passo se aprovado

Preparar dois artefatos locais/dev:

1. `nike-moon-shoe-jacquemus-guia-lk` — já tem pesquisa/draft base; finalizar e validar.
2. `new-balance-530-original-brasil` — criar draft completo com hero, FAQ, schema e links para collection/PDPs.

Entrega esperada: preview visual + checklist técnico + rollback + proposta de publicação separada.
