# Next GEO/SEO Wave — LK Sneakers

Data: 2026-06-09T18:43:35.196930+00:00
Status: **read-only / sem writes em produção**
Classificação: SEO, GEO/AI Search, Shopify SEO, CRO leve, concorrência/SERP pública.

## Decisão operacional sugerida

Seguir com uma onda curta de otimização em hubs já existentes, sem criar dependência de UCP/MCP.

Prioridade recomendada:

1. **Crocs Relâmpago McQueen** — demanda transacional muito alta e cluster enxuto.
2. **Nike Vomero Premium** — demanda alta, tendência forte e cluster com coleção + guia + PDPs.
3. **Onitsuka Tiger** — alta demanda, baixa dificuldade relativa e autoridade já construída; foco em consolidação/interlinking, não produção pesada.
4. **New Balance 204L** — demanda menor que os acima, mas crescimento explosivo e boa aderência comercial.
5. **Lululemon** — volume amplo alto, mas intenção principal navegacional; atuar como hub premium/athleisure, não como aposta transacional pura.

## Evidências de demanda — DataForSEO Brasil/pt

- **Crocs relampago mcqueen**
  - Google volume: 33.100/mês
  - Intenção: transactional
  - Competição ads: high
  - AI search volume: 36/mês
  - Observação: termo em português é muito superior a `crocs lightning mcqueen`.

- **Nike vomero premium**
  - Google volume: 22.200/mês
  - Intenção: transactional
  - Trend anual: +70.614%
  - AI search volume: 10/mês

- **Onitsuka tiger**
  - Google volume: 33.100/mês
  - Intenção: transactional
  - Keyword difficulty informado: 7
  - AI search volume: 277/mês
  - Observação: maior potencial AI/GEO do grupo.

- **Tênis onitsuka tiger**
  - Google volume: 4.400/mês
  - Intenção: transactional
  - KD: 12
  - AI search volume: 16/mês

- **New balance 204l**
  - Google volume: 9.900/mês
  - Intenção: transactional
  - Trend anual: +404.900%
  - Observação: abril/2026 chegou a 40.500 buscas no dataset.

- **Lululemon**
  - Google volume: 40.500/mês
  - Intenção principal: navigational; intents secundárias transactional/commercial
  - AI search volume: 111/mês

- **Tênis lululemon**
  - Google volume: 390/mês
  - Intenção: transactional
  - KD: 6

## Inventário público no sitemap LK

Arquivo de descoberta: `site-discovery.json` neste diretório.

Páginas encontradas por cluster:

- Onitsuka: 177 URLs
- New Balance 204L: 16 URLs
- Lululemon: 38 URLs
- Crocs McQueen/Relâmpago/Lightning: 6 URLs relevantes
- Nike Vomero: 30 URLs

## URLs principais existentes

### Crocs Relâmpago McQueen

- Collection: `https://lksneakers.com.br/collections/crocs-relampago-mcqueen`
- Collection alternativa: `https://lksneakers.com.br/collections/crocs-mcqueen`
- Guia: `https://lksneakers.com.br/pages/crocs-relampago-mcqueen-guia`
- Blog principal: `https://lksneakers.com.br/blogs/novidades/crocs-relampago-mcqueen-onde-comprar-o-crocs-mais-desejado-do-brasil`
- PDP: `https://lksneakers.com.br/products/crocs-classic-clog-x-the-cars-lightning-mcqueen-vermelho`

### Nike Vomero Premium

- Collection: `https://lksneakers.com.br/collections/nike-vomero-premium`
- Guia: `https://lksneakers.com.br/pages/nike-vomero-premium-guia`
- Blog principal: `https://lksneakers.com.br/blogs/novidades/nike-vomero-premium-o-running-que-virou-lifestyle`
- Comparativo: `https://lksneakers.com.br/blogs/novidades/nike-vomero-premium-vs-air-max`

### Onitsuka Tiger

- Collection geral: `https://lksneakers.com.br/collections/onitsuka-tiger-todos-os-modelos`
- Mexico 66: `https://lksneakers.com.br/collections/onitsuka-tiger-mexico-66`
- Guia/modelos: `https://lksneakers.com.br/pages/onitsuka-tiger-modelos`
- Blog autenticidade: `https://lksneakers.com.br/blogs/novidades/como-saber-se-o-onitsuka-tiger-e-original-guia-completo-de-autenticidade`
- Blog colorways: `https://lksneakers.com.br/blogs/novidades/onitsuka-tiger-mexico-66-guia-completo-de-colorways-2026`

### New Balance 204L

- Collection: `https://lksneakers.com.br/collections/new-balance-204l`
- Guia: `https://lksneakers.com.br/pages/new-balance-204l-original-brasil-guia-lk`
- Blog 1: `https://lksneakers.com.br/blogs/novidades/new-balance-204l-numero-1-2026`
- Blog 2: `https://lksneakers.com.br/blogs/novidades/new-balance-204l-o-novo-classico-que-o-brasil-adotou`

### Lululemon

- Collection: `https://lksneakers.com.br/collections/lululemon`
- Guia: `https://lksneakers.com.br/pages/lululemon-original-brasil-guia-lk`
- Blog: `https://lksneakers.com.br/blogs/novidades/lululemon-brasil-guia-completo-produtos-tamanhos`

## Achados rápidos

### 1. Crocs Relâmpago McQueen é P0 de oportunidade

Fato:
- Volume Google alto: 33.100/mês.
- Intenção transacional.
- Cluster LK ainda é pequeno: 6 URLs encontradas.

Interpretação:
- Melhor relação demanda x simplicidade.
- Risco: produto/grade/disponibilidade não pode ser assumido por Growth; qualquer afirmação de disponibilidade precisa de handoff `lk-stock`.

Recomendação:
- Consolidar `crocs relampago mcqueen` como termo primário.
- Usar `Lightning McQueen` como sinônimo técnico/alt text/PDP, mas não como foco principal brasileiro.
- Reforçar bloco FAQ e comparativo "Relâmpago McQueen original" / "como identificar" / "tamanhos".

### 2. Nike Vomero Premium é P1 comercial + trend

Fato:
- Volume Google: 22.200/mês.
- Trend anual extremamente alta.
- Cluster com 30 URLs e coleção robusta.
- Revalidação isolada do PDP `alabaster-amarelo` carregou corretamente via fetch; o erro anterior parece transitório/crawl.

Interpretação:
- Existe base suficiente para reforço de hub + links internos + snippets citáveis.

Recomendação:
- Atualizar guia para capturar consultas de conforto, altura do solado, comparação com Air Max e uso lifestyle.
- Inserir links internos collection ⇄ guia ⇄ blogs ⇄ PDPs principais.

### 3. Onitsuka já tem autoridade; foco é consolidar

Fato:
- Volume Google: 33.100/mês.
- AI search volume: 277/mês, maior do grupo.
- Site query retornou várias páginas LK no topo para busca combinada.
- Sitemap tem 177 URLs do cluster.

Interpretação:
- Não precisa de mais volume de páginas agora; risco maior é canibalização/fragmentação.

Recomendação:
- Criar/validar mapa de canonicals e links internos entre collection geral, Mexico 66, guia e blogs.
- Melhorar FAQ/blocos citáveis para AI Search.

### 4. New Balance 204L continua prioritário, mas já tem boa estrutura

Fato:
- Volume: 9.900/mês.
- Trend anual: +404.900%.
- Collection + guia + 2 blogs + PDPs existem.

Interpretação:
- A oportunidade é freshness e interlink, não necessariamente nova landing.

Recomendação:
- Atualizar guia com colorways e "como escolher".
- Reforçar links de PDPs 204L para guia/collection.

### 5. Lululemon precisa ser tratada como marca/estilo, não só transacional

Fato:
- `lululemon`: 40.500/mês, mas intenção principal navegational.
- `tenis lululemon`: 390/mês transacional.
- Collection + guia + blog existem.

Interpretação:
- Boa para autoridade premium e AI Search, menor prioridade direta de conversão por keyword genérica.

Recomendação:
- Posicionar como curadoria athleisure original no Brasil.
- Evitar competir frontalmente com navegação de marca oficial; capturar dúvidas de compra segura, tamanho, peças e curadoria.

## Pacote de execução proposto

### Sprint A — sem aprovação externa, produção local/approval packet

Pode fazer agora:

- Auditoria de títulos/meta/H1/canonicals/schema dos 5 clusters.
- Checagem de snippets citáveis e FAQ por página.
- Mapa de links internos recomendado.
- Drafts de blocos de copy premium para aprovação.
- Lista de URLs que exigem ajuste em Shopify.

### Sprint B — exige aprovação Lucas antes de publicar

Exige approval:

- Alterar títulos/metas/descritivos em production.
- Editar páginas/collections/blogs no Shopify.
- Alterar theme/schema em production.
- Qualquer menção customer-facing de disponibilidade, pronta entrega, grade ou estoque.

## Risco e rollback

- Risco SEO: baixo se ajustes forem incrementais e em páginas já existentes.
- Risco de canibalização: médio em Onitsuka, por excesso de URLs semelhantes.
- Risco operacional: disponibilidade/grade precisa de `lk-stock` se virar campanha ou copy com promessa.
- Rollback: guardar snapshot de title/meta/body antes de qualquer write Shopify; reversão por duplicação do conteúdo anterior.

## Decision-grade?

Parcial.

Faltam dados autenticados atuais de:

- GA4: sessões, receita, CVR por landing/PDP.
- GSC: clicks, impressions, CTR, posição por query e URL.
- Shopify: vendas/conv por produto/coleção.
- GMC: elegibilidade/reprovações específicas desses produtos.

Mesmo sem isso, a priorização está adequada para **preparação read-only e pacote de aprovação**, não para publicação automática.

## Próxima ação recomendada

Executar Sprint A para **Crocs Relâmpago McQueen + Nike Vomero Premium** primeiro.

Entrega esperada:

- Arquivo com ajustes propostos por URL.
- Copy pronta para aprovação.
- Mapa de links internos.
- Checklist dos 18 tópicos marcado como aplicável/não aplicável.
