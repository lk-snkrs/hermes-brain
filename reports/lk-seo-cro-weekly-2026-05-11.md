# LK SEO/CRO Weekly Improvement — 2026-05-11

## Veredito

A base pública da LK está tecnicamente forte, indexável e com schema/estrutura muito acima do básico. O principal gargalo acionável desta semana não é bloqueio técnico: é **truncamento de títulos SEO em homepage/PDPs importantes** e a falta de dados autenticados de **Search Console/Merchant** nesta execução para priorizar por CTR/feed real.

- **Nota SEO/CRO operacional:** 86/100
- **Nota do snapshot público HTML/sitemap/robots:** 97/100
- **Meta próxima semana:** 90/100 operacional
- **Semana anterior:** sem relatório `lk-seo-cro-weekly-*.md` anterior encontrado em `reports/`; este run vira baseline.
- **Modo:** read-only. Nenhum write em Shopify, tema, Merchant, Search Console, banco, campanhas, Klaviyo ou WhatsApp.

## Escopo auditado

- Site: `https://lksneakers.com` → redireciona/canoniza para `https://lksneakers.com.br/`.
- Sitemap público lido: 2.111 URLs encontradas.
- Páginas/PDPs checados nesta rodada: 12.
- `robots.txt`: 200.
- `llms.txt`: 200.
- Skills usadas/referenciadas: `lk-seo-weekly-improvement`, `seo-audit`, `seo-page`, `seo-content`, `seo-ecommerce`.

## Scorecard

| Categoria | Nota | Evidência |
|---|---:|---|
| Técnico/indexabilidade | 100 | Páginas retornaram 200, canonical presente, robots sem `noindex`, sitemap acessível. |
| On-page title/meta/H1 | 88 | Boa estrutura geral, mas homepage e PDPs prioritários têm title acima do ideal de SERP. |
| Conteúdo/E-E-A-T/helpfulness | 100 | Conteúdo público rico, com sinais de autenticidade, loja física, troca/devolução/atendimento e textos por coleção/PDP. |
| E-commerce/Product SEO/schema | 95 | Product/Organization/WebSite schema detectados, offer/preço/disponibilidade/regras comerciais presentes; oportunidade de refinamento em rich snippets/reviews por PDP. |
| AI/GEO readiness | 100 | Estrutura com headings, conteúdo extraível, `llms.txt` ativo e schema forte. |
| Imagens/performance riscos HTML | 98 | Alt text presente; poucos casos de imagens sem dimensão explícita. CWV real não medido sem API/lab nesta execução. |
| Search Console | Pendente | Scripts/credenciais Google não estavam disponíveis no runtime do Brain; sem inventar CTR/impressões. |
| Merchant/feed | Pendente | Workflow/credenciais Merchant não disponíveis no runtime; sem inventar feed/disapprovals. |

**Como li a nota:** a camada pública está em 97/100. A nota operacional entregue ao módulo semanal fica em 86/100 porque Search Console e Merchant/feed ainda não entraram no loop desta execução; sem esses dados, a priorização por CTR/feed fica incompleta.

## Páginas prioritárias avaliadas

1. `https://lksneakers.com` → final `https://lksneakers.com.br/`
2. `https://lksneakers.com/collections/tenis` → final `https://lksneakers.com.br/collections/sneakers`
3. `https://lksneakers.com.br/collections/nike-air-force-1`
4. `https://lksneakers.com.br/collections/nike-dunk`
5. `https://lksneakers.com.br/collections/air-jordan-1`
6. `https://lksneakers.com.br/collections/yeezy`
7. `https://lksneakers.com.br/products/nike-dunk-low-rose-whisper`
8. `https://lksneakers.com.br/products/nike-dunk-low-ocean-bliss`
9. `https://lksneakers.com.br/products/nike-dunk-low-teddy-bear-pink`
10. `https://lksneakers.com.br/products/air-jordan-1-mid-wolf-grey`
11. `https://lksneakers.com.br/products/air-jordan-1-low-sunset-haze`
12. `https://lksneakers.com.br/products/supreme-x-nike-air-force-1-low-box-logo-white`

## Top 5 ações da semana

| # | Página/PDP | Problema atual | Recomendação | Impacto | Esforço | Risco | Status |
|---:|---|---|---|---|---|---|---|
| 1 | Homepage `https://lksneakers.com.br/` | Title com 78 chars e meta description com 187 chars: alto risco de truncamento em SERP. | Preparar preview de title com 55–65 chars e description com 150–160 chars, mantendo “tênis originais”, Jardins/SP e autenticidade. | Alto | Baixo | Baixo | `needs_approval` para publicar |
| 2 | PDPs Nike Dunk/Jordan/Supreme auditados | Titles de 77–90 chars por incluir nome + preço + “em até 10x” + marca; SERP tende a cortar justamente a proposta comercial. | Criar lote-preview de títulos por template curto: `Nike Dunk Low Rose Whisper Rosa | LK Sneakers` e deixar preço/10x na meta/structured data. | Alto | Médio | Baixo | `needs_approval` para alterar Shopify SEO fields |
| 3 | Coleção `Nike Dunk` | Title com 67 chars; meta boa mas curta/sem CTA forte. | Ajustar title para ~60 chars e meta para reforçar autenticidade, pronta entrega, loja SP e 10x sem passar de 155 chars. | Médio | Baixo | Baixo | `needs_approval` |
| 4 | Coleção `Sneakers` | H1 atual `Sneakers for You` é genérico e menos orientado a busca/compra. | Preparar preview de H1/intro: `Tênis e Sneakers Originais` + subtítulo curto com marcas-chave. | Médio | Baixo | Médio, pois altera texto visível | `needs_approval` |
| 5 | Operação semanal | Sem GSC/Merchant nesta execução; fila de PDPs foi por sitemap/páginas públicas, não por CTR/feed real. | Conectar check read-only GSC + Merchant no cron para priorizar PDPs com impressões, CTR baixo, posição 4–20 e problemas de feed. | Alto | Médio | Baixo se read-only | Sem write externo; requer só setup seguro/credencial via Doppler |

## Previews que posso preparar sem aprovação pública

- Tabela de novos titles/metas para homepage, coleções e PDPs prioritários.
- Preview de H1/intro para a coleção `Sneakers`.
- Checklist de schema Product por PDP, comparando campos presentes vs rich result ideal.
- Lista de URLs candidatas para próxima rodada, assim que GSC/Merchant read-only estiverem disponíveis.

## O que exige aprovação antes de escrever/publicar

- Alterar title/meta/H1/descrição em Shopify.
- Alterar conteúdo visível de coleção/PDP.
- Alterar alt text, imagens ou dimensões em Shopify/theme.
- Editar tema/Liquid/app/schema global.
- Mudar Merchant Center/feed ou Search Console.
- Qualquer bulk update.

## O que não foi feito

- Não usei Search Console/GA4/CrUX autenticado: scripts/credenciais Google não encontrados neste runtime.
- Não usei Merchant Center/feed: workflow/credenciais Merchant não disponíveis nesta execução.
- Não medi Lighthouse/PageSpeed lab completo; a performance aqui é risco por HTML, imagens e metatags, não CWV real.
- Não alterei Shopify, Tiny, tema, Merchant, Search Console, banco, campanha, Klaviyo, WhatsApp ou conteúdo público.

## Evidências brutas

- JSON do snapshot: `/opt/data/hermes_bruno_ingest/hermes-brain-follow-20260510/reports/lk-seo-cro-weekly-2026-05-11.json`
- Relatório markdown: `/opt/data/hermes_bruno_ingest/hermes-brain-follow-20260510/reports/lk-seo-cro-weekly-2026-05-11.md`
