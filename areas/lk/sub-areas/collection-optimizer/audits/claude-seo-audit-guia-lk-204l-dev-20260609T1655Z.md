# Claude-SEO Audit — Guia LK New Balance 204L — DEV

Status: READ-ONLY / DEV PREVIEW  
Data: 2026-06-09  
URL: https://lksneakers.com.br/pages/new-balance-204l-original-brasil-guia-lk?preview_theme_id=155065450718

## Ferramenta

- Upstream `AgriciDaniel/claude-seo` clonado em `/tmp/claude-seo`.
- Skills aplicadas como playbook: `seo-page`, `seo-content`, `seo-schema`, `seo-geo`, `seo-ecommerce`.
- Script executado: `scripts/parse_html.py` sobre HTML de preview via curl.
- Script executado: `scripts/content_quality.py --json`.
- PageSpeed PSI mobile tentou rodar, mas retornou rate limit público.

## Evidência executada

### Claude SEO parse_html

- Title: `New Balance 204L Original | Guia LK`
- Meta description: `Guia LK do New Balance 204L original: estética low profile, colorways, autenticidade e como escolher seu par.`
- Canonical: `https://lksneakers.com.br/pages/new-balance-204l-original-brasil-guia-lk`
- H1 tags: 1
- H2 tags: 10
- Images: 10 no parser / 14 por regex raw HTML
- Internal links: 190
- External links: 7
- Schema blocks: 2
- Word count: 1282 no parser / 1828 por regex raw HTML

### Content quality

- Overall quality: 90/100
- Information density: 0.839
- Filler score: 0
- AI pattern score: 0
- Flag: repetitive

### Schema

- JSON-LD válido: 2 blocos carregaram sem erro.
- Organization/ShoeStore/ClothingStore: OK.
- FAQPage: OK tecnicamente, mas restrito em rich results Google para sites não gov/health; ainda útil como estrutura semântica/GEO quando verdadeiro.

### SERP/DataForSEO

Keyword `new balance 204l`, mobile Brasil:
- New Balance oficial ocupa topo orgânico e PDPs.
- Bloco de imagens alto na SERP.
- Vídeos curtos aparecem na primeira dobra.
- LK collection aparece no top 10 orgânico.
- Pessoas também pesquisam: feminino bege, feminino, marrom, 36, bege claro, Miu Miu, bege, Brasil, branco, sea salt, rosa, confortável, masculino, cinza, off white.

Search intent:
- `new balance 204l`: transactional 0.678
- `new balance 204l original`: transactional 0.753
- `new balance 204l brasil`: informational 0.454 + transactional 0.293
- `new balance 204l feminino`: transactional 0.785
- `new balance 204l bege`: informational 0.780
- `new balance 204l conforto`: transactional 0.823
- `new balance 204l comprar`: transactional 0.999
- `new balance 204l calça grande ou pequeno`: commercial 0.549
- `new balance 204l vs 530`: commercial 0.935
- `new balance 204l miu miu`: informational 0.451 + transactional 0.400

## Score Claude-SEO adaptado

- On-page SEO: 91/100
- Content quality: 90/100
- Technical/indexability: 86/100
- Schema: 84/100
- GEO/AI Search: 92/100
- Ecommerce/search intent fit: 88/100
- Images/SERP visual fit: 82/100
- Performance: inconclusivo por rate limit PSI; risco direcional moderado por Shopify/scripts.

Overall: 89/100 — A-

## Veredito

Está forte e apta para Lucas revisar. Não é 10/10 ainda por três pontos:

1. Title/meta ainda podem ficar mais agressivos para CTR antes de publicar.
2. OG image ainda aponta para logo LK, não para hero/editorial do 204L.
3. A camada visual/thumbnail/short video é uma lacuna contra a SERP, que mostra imagens e vídeos altos.

## Recomendações sem Production write

- Manter DEV como está para revisão visual.
- Preparar title/meta alternativos para approval.
- Preparar OG image editorial após aprovação e validação de asset.
- Registrar follow-up de Performance/CWV quando PSI sair do rate limit.

## Writes externos

- Nenhum.
