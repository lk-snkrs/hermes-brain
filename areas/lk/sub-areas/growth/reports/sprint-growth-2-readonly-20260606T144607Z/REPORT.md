# LK Growth Sprint 2 — read-only SEO/CRO/Performance audit

Status: read-only. Nenhum write externo executado nesta etapa.

## Evidências coletadas
- Public head recheck: `public-head-recheck.json`
- Playwright mobile CRO: `playwright-mobile-cro.json`
- Screenshots mobile: `screenshots/`
- GSC priority rows: `gsc-priority-opportunities.json`

## Recheck pós-deploy
- https://lksneakers.com.br/: status=200, title_len=78, meta_len=187, liquid_error=False, scripts=63, imgs=35, html_len=522172
- https://lksneakers.com.br/products/slide-nike-mind-001-black-chrome-preto: status=200, title_len=49, meta_len=144, liquid_error=False, scripts=68, imgs=33, html_len=636002
- https://lksneakers.com.br/products/slide-nike-mind-001-pearl-pink-rosa: status=200, title_len=47, meta_len=137, liquid_error=False, scripts=68, imgs=23, html_len=602131
- https://lksneakers.com.br/collections/new-balance-204l: status=200, title_len=49, meta_len=143, liquid_error=False, scripts=66, imgs=34, html_len=628000
- https://lksneakers.com.br/collections/adidas-samba-jane: status=200, title_len=41, meta_len=127, liquid_error=False, scripts=65, imgs=23, html_len=601251
- https://lksneakers.com.br/collections/onitsuka-tiger-todos-os-modelos: status=200, title_len=38, meta_len=124, liquid_error=False, scripts=66, imgs=58, html_len=725417
- https://lksneakers.com.br/collections/lululemon: status=200, title_len=44, meta_len=138, liquid_error=False, scripts=66, imgs=54, html_len=770130

Leitura: hotfix Samba Jane está OK; Nike Mind e NB 204L já servem title/meta novos. Homepage ainda mostrou head antigo via urllib, mas Playwright no browser humano já leu title/meta novos — cache/stale storefront provável.

## Mobile CRO / performance
- https://lksneakers.com.br/: status=200, h1='LK Sneakers — Curadoria de Sneakers e Lifestyle Premium | São Paulo', requests=268, scripts=87, images=29, domContentLoaded=1373ms, load=2248ms, trust=['Autenticidade', '10×', 'Jardins'], has_size=True, has_add=True
- https://lksneakers.com.br/products/slide-nike-mind-001-black-chrome-preto: status=200, h1='Chinelo Slide Nike Mind 001 Black Chrome Preto', requests=295, scripts=90, images=27, domContentLoaded=1802ms, load=2861ms, trust=['Autenticidade', '10×', '10x', 'Jardins'], has_size=True, has_add=True
- https://lksneakers.com.br/products/slide-nike-mind-001-pearl-pink-rosa: status=200, h1='Chinelo Slide Nike Mind 001 Pearl Pink Rosa', requests=292, scripts=91, images=22, domContentLoaded=2119ms, load=4714ms, trust=['Autenticidade', '10×', '10x', 'Jardins'], has_size=True, has_add=True
- https://lksneakers.com.br/collections/new-balance-204l: status=200, h1='New Balance 204L', requests=266, scripts=86, images=29, domContentLoaded=1520ms, load=2866ms, trust=['Autenticidade', '10×', 'Jardins'], has_size=True, has_add=True
- https://lksneakers.com.br/collections/adidas-samba-jane: status=200, h1='Adidas Samba Jane', requests=263, scripts=86, images=27, domContentLoaded=1216ms, load=2168ms, trust=['Autenticidade', '10×', 'Jardins'], has_size=True, has_add=True
- https://lksneakers.com.br/collections/onitsuka-tiger-todos-os-modelos: status=200, h1='Onitsuka Tiger', requests=270, scripts=87, images=29, domContentLoaded=2018ms, load=3927ms, trust=['Autenticidade', '10×', 'Jardins'], has_size=True, has_add=True
- https://lksneakers.com.br/collections/lululemon: status=429, h1='Your connection needs to be verified before you can proceed', requests=15, scripts=6, images=2, domContentLoaded=139ms, load=301ms, trust=[], has_size=False, has_add=False

Principais anomalias técnicas:
- 263–295 requests por página mobile nos checks principais.
- 86–91 scripts por página mobile.
- Console/failures recorrentes: CORS em `recovery.lucascimino.com/links/whatsapp/mint`, CORS em `n8n.lucascimino.com/webhook/lk-cart-intent-v1`, `[ET] tracker not configured`, Judge.me sem key em alguns contextos, fetch aborts de Google/Shopify/Attentive.
- Lululemon retornou 429 em Playwright depois de sequência de auditoria; direct HTTP retornou 200. Provável proteção/rate-limit por sessão/IP, não queda real da página.

## GSC / demanda
- nike mind 001 → https://lksneakers.com.br/products/slide-nike-mind-001-black-chrome-preto: clicks=5, impressions=30305, CTR=0.02%, pos=9.0
- onitsuka tiger → https://lksneakers.com.br/collections/onitsuka-tiger-todos-os-modelos: clicks=66, impressions=25976, CTR=0.25%, pos=8.3
- nike mind 001 → https://lksneakers.com.br/products/slide-nike-mind-001-pearl-pink-rosa: clicks=9, impressions=25038, CTR=0.04%, pos=8.9
- lululemon → https://lksneakers.com.br/collections/lululemon: clicks=124, impressions=17661, CTR=0.7%, pos=5.5
- nike mind 001 → https://lksneakers.com.br/products/slide-nike-mind-001-black-chrome-preto?currency=BRL&country=BR&variant=47839129239774&utm_source=google&utm_medium=cpc&utm_campaign=Google%20Shopping&stkn=789476af598e: clicks=12, impressions=12483, CTR=0.1%, pos=12.5
- new balance 204l → https://lksneakers.com.br/collections/new-balance-204l: clicks=28, impressions=10615, CTR=0.26%, pos=9.7
- chinelo nike mind 001 → https://lksneakers.com.br/products/slide-nike-mind-001-black-chrome-preto: clicks=2, impressions=7873, CTR=0.03%, pos=6.1
- chinelo nike mind 001 → https://lksneakers.com.br/products/slide-nike-mind-001-light-smoke-grey-cinza: clicks=1, impressions=7430, CTR=0.01%, pos=6.1

DataForSEO confirmou demanda forte/atual: Nike Mind 001 ~18.1k/mês; NB 204L ~9.9k/mês com picos recentes; Onitsuka ~33.1k/mês; Lululemon ~40.5k/mês; Adidas Samba Jane ~2.4k/mês com pico 8.1k.

## O que está ruim
1. Scripts e integrações pesados/dando erro: volume alto de JS e erros CORS/tracker podem afetar INP, confiabilidade de tracking e conversão mobile.
2. Alguns templates/heads ainda têm cache/stale, especialmente home; precisa recheck antes de nova alteração em head.
3. Onitsuka public head direto ainda mostrou title/meta antigo em uma leitura, apesar de GraphQL SEO aplicado; precisa confirmar se o template/fallback está sobrescrevendo ou se é cache.
4. Lululemon gerou 429 no Playwright durante auditoria, sinal de sensibilidade de proteção/rate-limit para navegação automatizada.
5. Páginas com demanda alta ainda dependem de copy/CRO acima da dobra; title/meta ajuda CTR, mas o clique precisa converter em PDP/collection.

## Próximas melhorias propostas
### P1 — QA técnico de head/cache
- Recheck amanhã: home, Onitsuka, Lululemon, Nike Mind, NB 204L e Samba Jane.
- Se Onitsuka seguir com head antigo, ajustar template/SEO source especificamente.

### P1 — Auditoria de tags/scripts
- Mapear origem de GA4/Ads/Meta/Attentive/Judge.me/recovery/n8n.
- Corrigir CORS de recovery/n8n ou desativar chamadas client-side que falham.
- Validar Judge.me key/widget.
- Separar tags essenciais de tags que podem carregar após interação/consentimento.

### P1 — CRO mobile nas páginas quentes
- Nike Mind PDPs: reforçar bloco curto above-the-fold com “o que é / para quem é / autenticidade / atendimento humano”, sem linguagem operacional proibida.
- NB 204L collection: inserir/otimizar bloco de escolha por cor/estilo e links para variações mais buscadas: bege, feminino, branco, cinza, 36/35.
- Adidas Samba Jane: trocar shim por editorial snippet completo se desejado; o guia existe no HTML público e está bom, mas precisa QA visual.
- Onitsuka/Lululemon: ajustar bloco de trust + orientação de escolha e confirmação por atendimento humano.

## Approval packet sugerido
Sem aprovação ainda para writes. Sugestão de próximo pacote com aprovação separada:
- Dev-theme/preview de CRO above-the-fold para Nike Mind + NB 204L.
- Hotfix técnico CORS/tracker/Judge.me apenas após mapeamento da origem.
- Recheck head/cache antes de novo write SEO.

## Checklist 18 tópicos
- GA4: não cruzado nesta etapa; pendente para decision-grade comercial.
- GSC: usado e salvo.
- GMC: não aplicável nesta etapa.
- Shopify SEO: recheck público + SEO aplicado previamente.
- Shopify CRO/theme: auditado read-only via Playwright; mudanças pendem aprovação.
- GEO/AI Search: oportunidades de blocos citáveis em Nike Mind/NB/Loja/FAQ.
- PageSpeed/CWV: Playwright indica risco por requests/scripts; CrUX não consultado aqui.
- Schema: contagem JSON-LD registrada; validação profunda pendente.
- Reviews: Judge.me apontou possível key/widget issue em console; investigar.
- Paid media: tags/Google/Meta aparecem no ruído; auditar duplicação.
- Influencer/social demand: SERP mostra vídeos/Instagram fortes para Nike Mind/NB; oportunidade de conteúdo visual/social proof.
- Concorrência/SERP: Nike/NB oficiais, Instagram, marketplaces e Shopping dominam; LK aparece em Shopping/orgânico para Nike Mind/NB.
- Google Business/local: não reavaliado nesta rodada.
- Klaviyo/CRM signals: não avaliado.
- Catálogo/product data quality: não avaliado; Shopping mostra LK em alguns produtos.
- Conteúdo/taxonomia comercial: oportunidades por variações e guias de escolha.
- Mensuração/QA eventos: P1 por erros CORS/tracker.
- Impact review/experimentation: D+7 já agendado para pacote SEO; este sprint recomenda novo pacote controlado.
