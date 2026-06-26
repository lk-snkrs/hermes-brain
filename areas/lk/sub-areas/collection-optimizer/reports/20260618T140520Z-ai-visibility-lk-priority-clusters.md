# AI Visibility LK — Auditoria v1 dos clusters prioritários

Data: 2026-06-18T14:05:20Z  
Escopo: GEO/AI Search para LK Sneakers com foco em New Balance 204L, Onitsuka Tiger, Jacquemus Nike, Nike Vomero Premium, Nike Mind 001 e Nike Mind 002.  
Status: read-only público + DataForSEO Google Keyword Overview. Não decision-grade para conversão porque ainda não inclui GA4/GSC/Shopify/GMC.

## Evidência pública verificada

- `/llms.txt`: existe, cita Mind e Vomero, mas ainda não cita Jacquemus/Nike x Jacquemus/Moon Shoe.
- `/agents.md`: existe, cita Mind e Vomero, mas ainda não cita Jacquemus/Nike x Jacquemus/Moon Shoe.
- `/sitemap_agentic_discovery.xml`: existe e aponta para `/agents.md`.
- `robots.txt`: permite GPTBot, ChatGPT-User, ClaudeBot, PerplexityBot, OAI-SearchBot e Google-Extended.
- DataForSEO LLM mentions: bloqueado por plano/acesso (40204). Sem métrica de menções LLM nesta rodada.

## Demanda Google — Brasil, pt

- `nike mind 001`: 27.100 buscas/mês; intent transacional + informacional; maio/2026 110.000.
- `nike vomero premium`: 27.100 buscas/mês; intent transacional; maio/2026 40.500.
- `new balance 204l`: 12.100 buscas/mês; intent transacional; maio/2026 40.500.
- `nike mind 002`: 3.600 buscas/mês; intent transacional.
- `nike jacquemus`: 1.300 buscas/mês; intent transacional.
- `jacquemus nike`: 390 buscas/mês; intent transacional + informacional.
- `nike x jacquemus`: 170 buscas/mês; intent transacional.
- `nike jacquemus moon shoe`: 110 buscas/mês; intent transacional.
- `nike moon shoe jacquemus`: 50 buscas/mês; intent transacional.
- `nike x jacquemus moon shoe`: 30 buscas/mês; intent informacional.

## Cluster: Nike x Jacquemus / Moon Shoe

URLs verificadas:
- Collection: `https://lksneakers.com.br/collections/nike-x-jacquemus-moon-shoe-sp`
- Guia: `https://lksneakers.com.br/pages/nike-moon-shoe-jacquemus-guia-lk`
- Collection geral Jacquemus: `https://lksneakers.com.br/collections/jacquemus`

Achados:
- Collection específica existe, indexável, com title/meta fortes, FAQPage schema, CollectionPage, ItemList e Organization/ShoeStore schema.
- Guia editorial existe, tem FAQ e bloco citável.
- `llms.txt` e `agents.md` não citam Jacquemus/Moon Shoe, apesar de o cluster estar publicado.
- Collection específica não foi detectada com “Bloco citável” textual, embora tenha FAQ e conteúdo editorial.

Prioridade: alta. Motivo: cluster premium, collab, bom fit de entidade fashion + sneaker, e lacuna clara no source map de IA.

Ação recomendada:
1. Adicionar Nike x Jacquemus/Moon Shoe ao `llms.txt` e `agents.md`.
2. Adicionar bloco citável curto na collection específica.
3. Garantir link explícito collection ↔ guia no topo/editorial.
4. Reforçar frases: original, curadoria LK, collab Nike x Jacquemus, Moon Shoe SP, atendimento humano para tamanho.

## Cluster: Nike Vomero Premium

URLs verificadas:
- Collection: `https://lksneakers.com.br/collections/nike-vomero-premium`
- Guia: `https://lksneakers.com.br/pages/nike-vomero-premium-guia`

Achados:
- Muito maduro para AI Visibility.
- Collection tem FAQ, bloco citável, CollectionPage, ItemList e FAQPage schema.
- Guia tem H1/H2 fortes, FAQ e bloco citável.
- Já aparece em `llms.txt` e `agents.md`.
- Meta description da collection ainda fala “15 modelos”; página pública indicou “20 itens” em conteúdo renderizado. Verificar divergência para evitar ruído.

Prioridade: muito alta. Motivo: 27.100 buscas/mês e conteúdo já quase pronto para ser source page.

Ação recomendada:
1. Corrigir/confirmar contagem na meta description da collection, se necessário.
2. Fortalecer link acima da dobra para Guia Vomero Premium.
3. Manter bloco citável com definição curta de “super trainer / ZoomX / Air Zoom / plataforma alta”.
4. Usar como padrão para outros clusters.

## Cluster: Nike Mind 001 e Nike Mind 002

URLs verificadas:
- Collection/hub: `https://lksneakers.com.br/collections/nike-mind-001`
- Guia 001/002: `https://lksneakers.com.br/pages/guia-nike-mind-001-002`
- Guia antigo/específico 001: `https://lksneakers.com.br/pages/nike-mind-001-guia`

Achados:
- Não existe collection `/collections/nike-mind-002`; a arquitetura atual concentra 001 e 002 em `/collections/nike-mind-001`.
- Collection/hub tem bom title/meta, FAQ e schema, mas não foi detectada com bloco citável explícito.
- Guia 001/002 está forte: FAQ, bloco citável, H2s comparativos e schema FAQPage.
- Guia específico 001 parece menos alinhado ao padrão atual: não detectou FAQ textual/schema FAQPage nem bloco citável; linguagem de H1 mais “hype” (“mais desejado de 2026”).
- Demanda é muito forte: Mind 001 27.100/mês e Mind 002 3.600/mês.

Prioridade: muito alta. Motivo: demanda alta e potencial de resposta AI para “diferença entre Nike Mind 001 e 002”.

Ação recomendada:
1. Manter `/collections/nike-mind-001` como hub 001/002 ou criar decisão explícita sobre URL canônica para Mind 002.
2. Adicionar bloco citável na collection/hub.
3. Revisar guia `nike-mind-001-guia`: atualizar tom para premium/curatorial, inserir FAQPage, bloco citável e linkar para o guia 001/002.
4. Em AI source map, tratar como “Nike Mind 001/002” e não só Mind 001.

## Clusters já incluídos no escopo anterior

### New Balance 204L
- Forte demanda: 12.100/mês, com pico recente de 40.500/mês.
- Guia já tem blocos citáveis e conteúdo comparativo robusto.
- Manter como gold source visual/editorial para LKGOC.

### Onitsuka Tiger
- Já aparece no source map com collection e guia.
- `onitsuka tiger original`: 90/mês no termo exato, mas a demanda real tende a estar distribuída em Mexico 66, SD, Sabot, Slip-on e termos de cor/modelo.
- Recomendação: auditar subclusters por modelo, não apenas marca.

## Score AI Visibility inicial

- Nike Vomero Premium: 9/10 — pronto para reforço fino.
- Nike Mind 001/002: 8/10 — forte, mas precisa resolver hub/002 e guia antigo.
- Nike x Jacquemus Moon Shoe: 7/10 — páginas boas, mas ausente do source map de IA.
- New Balance 204L: 9/10 — usar como padrão canônico.
- Onitsuka Tiger: 8/10 — bom, precisa granularidade por submodelo.

## Quick wins sem write externo

- Preparar diff textual para `llms.txt` e `agents.md` com Jacquemus/Moon Shoe.
- Preparar bloco citável para collection Nike x Jacquemus Moon Shoe.
- Preparar bloco citável para collection Nike Mind 001/002.
- Preparar revisão editorial do guia antigo Nike Mind 001.
- Criar checklist de QA LKGOC: FAQ visível, FAQPage schema, bloco citável, link coleção↔guia, title/meta, ausência de promessa pública de disponibilidade.

## Writes que exigem aprovação Lucas

- Qualquer alteração visível em collection/guia production.
- Alteração em theme production ou template LKGOC.
- Alteração em `llms.txt`, `llms-full.txt`, `agents.md` se publicada no storefront/repo ligado à produção.

## Approval packet sugerido — lote 1

Impacto esperado:
- Melhorar chance de citação por ChatGPT/Perplexity/Gemini/AI Overviews nos clusters de alta demanda.
- Reduzir ambiguidade de entidade e fonte para Nike Mind 001/002 e Nike x Jacquemus.
- Reforçar LK como fonte premium, original e assistida, sem promessa de estoque.

Esforço:
- Baixo a médio. Conteúdo e estrutura já existem; maior parte é ajuste de source map, bloco citável e links internos.

Risco:
- Baixo, desde que sem mexer em preço/estoque/disponibilidade e sem production write sem QA.

Rollback:
- Reverter snippets/blocos para versão anterior; manter receipt de diff; revisar impacto em ~7 dias via GSC/GA4 quando disponível.

Aprovação necessária:
- Aprovação explícita de Lucas antes de publicar qualquer mudança em produção.

## Camada Claude SEO aplicada — 2026-06-18

Correção de processo aplicada após pergunta do Lucas: esta auditoria agora incorpora explicitamente a família Claude SEO/AgriciDaniel como lente diagnóstica secundária, depois da demanda comercial e das fontes vivas. Skills/lentes usadas: `seo-page`, `seo-content`, `seo-ecommerce` e critérios GEO/AEO de citabilidade.

Critérios usados: title/meta/H1/canonical/alt/schema; estrutura editorial, FAQ, E-E-A-T e entidade LK; schema CollectionPage/ItemList/FAQPage/Organization; risco de promessa pública de disponibilidade; presença de bloco citável.

### Scorecard Claude SEO

- Nike x Jacquemus Moon Shoe collection: **95/100** — page 40/40, content 30/35, ecommerce/GEO 25/25. Issues: explicit citable block missing. URL: https://lksneakers.com.br/collections/nike-x-jacquemus-moon-shoe-sp

- Nike x Jacquemus Moon Shoe guia: **96/100** — page 36/40, content 35/35, ecommerce/GEO 25/25. Issues: meta length 53. URL: https://lksneakers.com.br/pages/nike-moon-shoe-jacquemus-guia-lk

- Nike Vomero Premium collection: **100/100** — page 40/40, content 35/35, ecommerce/GEO 25/25. Issues: sem issues materiais detectadas. URL: https://lksneakers.com.br/collections/nike-vomero-premium

- Nike Vomero Premium guia: **100/100** — page 40/40, content 35/35, ecommerce/GEO 25/25. Issues: sem issues materiais detectadas. URL: https://lksneakers.com.br/pages/nike-vomero-premium-guia

- Nike Mind 001/002 collection: **95/100** — page 40/40, content 30/35, ecommerce/GEO 25/25. Issues: explicit citable block missing. URL: https://lksneakers.com.br/collections/nike-mind-001

- Nike Mind 001/002 guia: **100/100** — page 40/40, content 35/35, ecommerce/GEO 25/25. Issues: sem issues materiais detectadas. URL: https://lksneakers.com.br/pages/guia-nike-mind-001-002

- Nike Mind 001 guia antigo: **82/100** — page 36/40, content 25/35, ecommerce/GEO 21/25. Issues: title length 23; FAQ missing; explicit citable block missing. URL: https://lksneakers.com.br/pages/nike-mind-001-guia

- New Balance 204L guia: **100/100** — page 40/40, content 35/35, ecommerce/GEO 25/25. Issues: sem issues materiais detectadas. URL: https://lksneakers.com.br/pages/new-balance-204l-original-brasil-guia-lk

- Autenticidade LK: **89/100** — page 34/40, content 30/35, ecommerce/GEO 25/25. Issues: H1 count 2; explicit citable block missing. URL: https://lksneakers.com.br/pages/autenticidade


### Mudanças no diagnóstico após Claude SEO

- Nike Vomero Premium e Guia Mind 001/002 sobem para status quase pronto/pronto como source pages: score 100/100 na lente pública.

- Nike x Jacquemus collection continua prioridade alta: tecnicamente forte (95/100), mas precisa de bloco citável e entrada no `llms.txt`/`agents.md`.

- Nike Mind collection/hub também é forte (95/100), mas precisa de bloco citável explícito e decisão canônica para Mind 002.

- Guia antigo Nike Mind 001 vira principal débito editorial: 82/100 por falta de FAQ detectável e bloco citável; recomenda-se atualizar ou consolidar com o guia 001/002.

- Autenticidade LK é forte como entidade, mas pode ganhar bloco citável explícito e revisar duplicidade de H1 detectada pela lente pública.


### Implicação operacional

A partir desta correção, qualquer auditoria LKGOC/AI Visibility deste profile deve declarar a camada Claude SEO aplicada ou justificar indisponibilidade. A camada não substitui GSC/GA4/Shopify/GMC, mas é gate obrigatório para scorecard de collection/guia/source page.
