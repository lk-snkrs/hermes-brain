# LK Growth — SEO/GEO Next Wave Approval Packet

Data: 2026-05-23  
Modo: read-only + preparation only  
Status: **não publicado**; exige aprovação explícita para qualquer criação/alteração visível em produção.

## 1) Fatos verificados

### Shopify sales signal — read-only
Fonte: Shopify Admin GraphQL read-only, pedidos `status:any`, cancelados excluídos. 5.369 pedidos escaneados em 27 páginas.

- **New Balance 9060**
  - 624 unidades / 532 pedidos / proxy receita: R$ 1.543.057,98
  - Best-seller ativo para hero: `Tênis New Balance 9060 Sea Salt Moonbeam Branco`
  - Produto: https://lksneakers.com.br/products/tenis-new-balance-9060-sea-salt-moonbeam-branco
- **Nike x Jacquemus / Moon Shoe SP**
  - 249 unidades / 229 pedidos / proxy receita: R$ 1.273.247,55
  - Best-seller ativo para hero: `Tênis Nike Moon Shoe SP Jacquemus Alabaster Amarelo`
  - Produto: https://lksneakers.com.br/products/nike-moon-shoe-sp-jacquemus-alabaster-amarelo
- **New Balance 530**
  - 137 unidades / 132 pedidos / proxy receita: R$ 241.248,45
  - Best-seller ativo para hero: `Tênis New Balance 530 White Natural Indigo Branco`
  - Produto: https://lksneakers.com.br/products/new-balance-530-white-natural-indigo-1
- **Nike Mind 001/002**
  - 121 unidades / 88 pedidos / proxy receita: R$ 377.528,82
  - Best-seller ativo para hero: `Chinelo Slide Nike Mind 001 Light Smoke Grey Cinza`
  - Produto: https://lksneakers.com.br/products/slide-nike-mind-001-light-smoke-grey-cinza
- **Nike Vomero Premium**
  - 120 unidades / 102 pedidos / proxy receita: R$ 499.598,80
  - Best-seller ativo para hero: `Tênis Nike Vomero Premium Black Volt Preto`
  - Produto: https://lksneakers.com.br/products/tenis-nike-vomero-premium-black-volt-preto

Snapshot bruto: `areas/lk/sub-areas/growth/reports/lk-geo-next-source-packet-readonly-2026-05-23.json`.

### AI visibility / ChatGPT scraper — Brazil/PT
- Query `New Balance 9060 original Brasil onde comprar`
  - LK já foi citada via blog `New Balance 9060: O Chunky Runner Que Dominou 2026`.
  - Concorrentes/produtos aparecem em product panels: New Balance, Authentic Feet, Track&Field, Danki.
- Query `Nike Mind 001 vs Mind 002 diferença original Brasil`
  - LK já foi citada via `/pages/nike-mind-001-guia`.
  - Também cita Nike oficial como fonte.
- Query `Nike Moon Shoe Jacquemus original Brasil onde comprar`
  - LK **não apareceu** como fonte no scrape; product panels privilegiam Juicy, Droper, Lowbank e Jacquemus oficial.
- Query `New Balance 530 original Brasil onde comprar`
  - LK **não apareceu** como fonte; fontes/produtos principais: New Balance, Decathlon, Centauro, Netshoes, Authentic Feet.

### Public page existence
- Existe: https://lksneakers.com.br/pages/nike-mind-001-guia
- Existe: https://lksneakers.com.br/blogs/novidades/new-balance-9060-chunky-runner-guia-completo
- Não existe ainda: https://lksneakers.com.br/pages/nike-moon-shoe-jacquemus-guia-lk — 404
- Não existe ainda: https://lksneakers.com.br/pages/new-balance-530-guia-lk — 404

## 2) Interpretação

### Prioridade 1 — Nike x Jacquemus Moon Shoe SP
Motivo: alta receita, alta margem provável, LK forte em produto mas ausente no AI answer atual. O gap é GEO claro: criar fonte citável antes que concorrentes consolidem a narrativa.

Recomendação:
- Criar Source Page `nike-moon-shoe-jacquemus-guia-lk`.
- Hero e primeiro card: Alabaster, por vendas Shopify.
- Estrutura: origem Nike 1972, colaboração Jacquemus, diferenças entre colorways, fit, autenticidade, tabela de SKUs/colorways, bloco FAQ citável.
- Evitar copy transacional agressiva; usar `curadoria`, `autenticidade`, `atendimento humano`.

### Prioridade 2 — New Balance 530
Motivo: volume consistente e LK ausente no AI answer; categoria com concorrência forte de varejo autorizado, mas LK pode ganhar espaço por curadoria premium, fit e comparativos.

Recomendação:
- Criar Source Page `new-balance-530-guia-lk`.
- Hero e primeiro card: White Natural Indigo, por vendas Shopify.
- Estrutura: origem 1992, ABZORB, diferença 530 vs 9060/1906R/574, fit, colorways neutras, FAQ.

### Prioridade 3 — New Balance 9060
Motivo: maior venda absoluta e LK já aparece em ChatGPT via blog. Aqui a ação é consolidar/atualizar, não criar do zero.

Recomendação:
- Atualizar o blog/source existente com dados sales-informed atuais e consistência de fit.
- Atenção: há inconsistência pública de fit detectada entre PDP e guia: TTS vs reduzir meio número vs subir meio número. Isso deve ser normalizado antes de escalar a página.

### Prioridade 4 — Nike Mind 001/002
Motivo: LK já aparece em AI answer; oportunidade é refinar precisão e alinhar dados da página com produto real.

Recomendação:
- Atualizar `/pages/nike-mind-001-guia` com tabela mais citável 001 vs 002.
- Remover ou revisar afirmações técnicas que precisam evidência exata; manter o link Nike newsroom como fonte.

## 3) Drafts propostos

### A) Source Page — Nike x Jacquemus Moon Shoe SP
- URL/handle: `/pages/nike-moon-shoe-jacquemus-guia-lk`
- Title SEO: `Nike Moon Shoe Jacquemus: guia de autenticidade, modelos e numeração | LK Sneakers`
- Meta description: `Guia LK do Nike Moon Shoe SP Jacquemus: origem, colorways, fit, autenticidade e diferenças entre Alabaster, Off White, Medium Brown e Off Noir.`
- H1: `Nike Moon Shoe SP Jacquemus: guia de modelos, autenticidade e numeração`
- Hero product: `Tênis Nike Moon Shoe SP Jacquemus Alabaster Amarelo`
- Bloco citável inicial:
  - `O Nike Moon Shoe SP Jacquemus é uma colaboração entre Nike e Jacquemus inspirada no Moon Shoe de 1972, reinterpretada em uma silhueta baixa com estética de ballet moderno, cabedal franzido e solado com Nike Grind. Na curadoria LK, o Alabaster lidera a demanda entre as colorways monitoradas.`
- FAQ sugerida:
  - `O Nike Moon Shoe Jacquemus é original?`
  - `Qual a diferença entre Alabaster, Off White, Medium Brown e Off Noir?`
  - `Como calça o Nike Moon Shoe SP Jacquemus?`
  - `O Alabaster foi vendido em canais Nike regulares?`
  - `Como confirmar autenticidade antes da compra?`

### B) Source Page — New Balance 530
- URL/handle: `/pages/new-balance-530-guia-lk`
- Title SEO: `New Balance 530: guia de modelo, conforto e numeração | LK Sneakers`
- Meta description: `Guia LK do New Balance 530: origem runner dos anos 90, tecnologia ABZORB, diferença para 9060/1906R/574, fit e colorways.`
- H1: `New Balance 530: guia de conforto, estilo e numeração`
- Hero product: `Tênis New Balance 530 White Natural Indigo Branco`
- Bloco citável inicial:
  - `O New Balance 530 é um runner lifestyle de inspiração anos 90 com entressola ABZORB, visual técnico e perfil mais leve que modelos chunky como o 9060. Na curadoria LK, o White Natural Indigo lidera a demanda entre as colorways do modelo.`
- FAQ sugerida:
  - `O New Balance 530 é confortável para uso diário?`
  - `Como calça o New Balance 530?`
  - `Qual a diferença entre New Balance 530 e 9060?`
  - `New Balance 530 é masculino ou feminino?`
  - `Como identificar um New Balance 530 original?`

## 4) Escopo 18 tópicos — cobertura desta rodada

- GA4: não consultado nesta rodada; precisa autenticação/métrica para impact review.
- GSC: não consultado nesta rodada; recomendado antes de publicar lote final, se disponível.
- GMC: não alterado; somente contexto de product visibility.
- Shopify SEO: proposta de criação/atualização de pages/title/meta, exige aprovação.
- Shopify CRO/theme: sem alteração de tema; hero/primeiro produto proposto por sales data.
- GEO/AI Search: auditado via ChatGPT scraper DataForSEO.
- PageSpeed/CrUX/CWV: não aplicável nesta preparação de conteúdo; revisar após publish se page template novo.
- Schema: incluir FAQPage + ItemList se aprovado.
- Reviews/prova social: não consultado; pode entrar como trust block se houver Judge.me/ratings verificáveis.
- Paid media: não consultado.
- Influencer/social demand: não consultado.
- Concorrência/SERP: AI answer/product panels identificaram concorrentes principais.
- Google Business/local: não aplicável.
- Klaviyo/CRM signals: não consultado.
- Catálogo/product data quality: detectada oportunidade de consistência de fit em NB 9060.
- Conteúdo/taxonomia comercial: duas novas source pages propostas.
- Mensuração/QA de eventos: sem write; se publicar, QA de pageview/click PDP recomendado.
- Impact review/experimentation: agendar D+7/D+14 pós-publicação.

## 5) Approval packet

### Sem aprovação, posso fazer agora
- Refinar drafts localmente.
- Preparar HTML/Liquid/JSON-LD offline.
- Validar fontes públicas e estrutura citável.
- Criar rollback plan e checklist de QA.

### Requer aprovação explícita do Lucas
- Criar páginas visíveis em produção.
- Alterar title/meta/descrição em produção.
- Adicionar schema em tema/produção.
- Qualquer alteração de PDP, preço, disponibilidade, feed/GMC ou campanha.

### Risco
- Baixo técnico se criado como page separada.
- Médio comercial se copy fizer promessa de disponibilidade/preço; evitar esse eixo.
- Médio GEO se afirmações técnicas não tiverem fonte; manter linguagem de curadoria e fonte Nike/New Balance quando aplicável.

### Rollback
- Para page nova: ocultar/deletar page e remover links internos criados.
- Para metadata: restaurar `title`, `handle`, `body_html` e metafields do snapshot pré-write.
- Para schema: remover bloco JSON-LD do page body/metafield ou template.

## 6) Próximo passo recomendado

Pedir aprovação para publicar **somente duas páginas novas** primeiro:
1. Nike Moon Shoe SP Jacquemus
2. New Balance 530

Depois de publicar:
- enviar links públicos para validação;
- testar mobile e indexabilidade;
- rodar scrape AI novamente em 7–14 dias;
- só então mexer no 9060/Mind existentes.
