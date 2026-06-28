# LK Growth — Ranking OS v2 — QA + Impact Review — 2026-06-27

- Execução: `2026-06-27T11:31Z–11:45Z`.
- Modo: read-only / preview-only.
- Writes externos: `0`.
- values_printed=false.
- Rotina: sábado — QA + Impact Review.

## Veredito executivo

Há achado material. O QA público básico está saudável para Home/PDP/arquivos AI (`HTTP 200`, canonical, H1 e schema sem noindex), mas surgiram **3 pontos acionáveis**:

1. `/collections/new-balance-740` ainda não é superfície canônica: retorna `200`, mas redireciona/finaliza em `/collections/new-balance-todos-os-modelos`, com title/canonical da coleção geral e `FAQPage=0`.
2. O bug público da Adidas Sambae citado no packet de 2026-06-26 parece **corrigido**: hoje `/collections/adidas-sambae` retorna `HTTP 200`, `Liquid error=false`, title novo, canonical correto e `FAQPage=1`.
3. Há divergência pós-receipt em Tokyo/Speedcat: receipts de 2026-06-26 registravam `FAQPage=1`, mas QA público de hoje encontrou `FAQPage=0` em `/collections/adidas-tokyo` e `/collections/puma-speedcat`. Precisa readback técnico antes de qualquer novo schema-only packet.

Status: **decision-grade para QA técnico e fila de investigação**, não decision-grade para impacto comercial dos writes de 2026-06-25/26 porque a janela GSC/GA4/Shopify ainda é curta e parte dos conectores Shopify/Google Workspace via wrapper falhou no smoke.

## Fontes e evidência

### GSC

Script read-only executado:

```bash
python3 scripts/lk_search_console_readonly_router_20260511.py
```

Resultado:

- Property: `sc-domain:lksneakers.com.br`.
- Janela final: `2026-05-28` a `2026-06-24`.
- Linhas query/page: `25000`.
- Páginas agregadas: `11294`.
- Oportunidades: `40`, todas `P1`.
- Writes: `0`.

Top sinais atuais:

- `nike mind 001` → PDP Black Chrome: `4 / 31.462` clicks/impressões, CTR `0,01%`, posição `8,9`.
- `onitsuka tiger` → collection todos modelos: `133 / 31.337`, CTR `0,42%`, posição `7,4`.
- `nike mind 001` → PDP Pearl Pink: `11 / 30.810`, CTR `0,04%`, posição `9,0`.
- `lululemon` → collection: `146 / 21.105`, CTR `0,69%`, posição `4,8`.
- `crocs mcqueen` → PDP Crocs McQueen: `36 / 17.378`, CTR `0,21%`, posição `8,3`.

Artefatos atualizados:

- `reports/lk-search-console-readonly-router-2026-05-11.json`
- `reports/lk-search-console-readonly-router-2026-05-11.md`

### QA leve obrigatório

| Superfície | URL | Resultado |
|---|---|---|
| Home | `https://lksneakers.com.br/` | `HTTP 200`; title head `LK Sneakers Jardins | Curadoria de Sneakers Originais`; H1 único; canonical correto; noindex=false; schema org/site presente. |
| PDP prioritária | `/products/slide-nike-mind-001-light-smoke-grey-cinza` | `HTTP 200`; title head `Nike Mind Slide 001 Light Smoke Grey Original | LK`; H1 único; canonical correto; Product/Breadcrumb/FAQPage; `FAQPage=1`; noindex=false. |
| Collection prioritária | `/collections/new-balance-740` | `HTTP 200`, mas final URL/canonical/title são `/collections/new-balance-todos-os-modelos`; `FAQPage=0`; confirma lacuna de collection NB740 canônica. |
| `robots.txt` | `/robots.txt` | `HTTP 200`; sitemap presente. |
| `sitemap.xml` | `/sitemap.xml` | `HTTP 200`; sitemapindex Shopify OK. |
| `llms.txt` | `/llms.txt` | `HTTP 200`; `Last updated: 2026-06-26 15:26:17 UTC`. |
| `llms-full.txt` | `/llms-full.txt` | `HTTP 200`; `Last updated: 2026-06-26 15:26:20 UTC`. |
| `agents.md` | `/agents.md` | `HTTP 200`. |
| `agents.txt` | `/agents.txt` | `404`; não tratado como quebra porque `agents.md` e `llms` estão ativos. |

Observação de parsing: o HTML contém `<title>` de ícones SVG/pagamento; o QA final usou o primeiro `<title>` dentro de `<head>` para evitar falso positivo de title contaminado.

### QA de mudanças recentes / receipts

Receipts revisados:

- `areas/lk/sub-areas/growth/receipts/theme-production/nb530-hub-serp-faq-production-20260625T100110Z/RECEIPT.md`
- `areas/lk/sub-areas/growth/receipts/theme-production/adidas-sl72-guide-faq-production-20260625T143142Z/RECEIPT.md`
- `areas/lk/sub-areas/growth/receipts/theme-production/asics-gel-nyc-guide-faq-production-20260626T0118Z/RECEIPT.md`
- `areas/lk/sub-areas/growth/receipts/three-collections-seo-schema-dev-20260626T0027Z/RECEIPT.md`
- `areas/lk/sub-areas/growth/approval-packets/semrush-continue-after-three-collections-20260626/APPROVAL-PACKET.md`

QA público de coleções recentes:

| Collection | HTTP | Title/canonical | FAQPage | Liquid error | Termos operacionais proibidos |
|---|---:|---|---:|---:|---|
| `adidas-sambae` | 200 | title novo / canonical correto | 1 | false | nenhum dos termos testados |
| `adidas-handball-spezial` | 200 | title/canonical OK | 0 | false | nenhum dos termos testados |
| `new-balance-530` | 200 | title/canonical OK | 1 | false | nenhum dos termos testados |
| `adidas-sl-72` | 200 | title/canonical OK | 1 | false | nenhum dos termos testados |
| `asics-gel-nyc` | 200 | title `ASICS Gel NYC: 1 modelos | LK Sneakers`; canonical correto | 1 | false | `envio imediato` aparece na meta description/OG global da página |
| `adidas-taekwondo` | 200 | title novo / canonical correto | 0 | false | nenhum dos termos testados |
| `adidas-tokyo` | 200 | title/canonical OK | 0 | false | nenhum dos termos testados |
| `puma-speedcat` | 200 | title/canonical OK | 0 | false | nenhum dos termos testados |

Achados:

- **Sambae:** o `Liquid error` apontado no approval packet de 2026-06-26 não aparece mais. Tratar como corrigido/QA OK, não como pendente bruto.
- **Tokyo/Speedcat:** divergência material; receipt dizia `FAQPage=1`, QA público atual mostra `FAQPage=0`. Próximo passo seguro é readback técnico do snippet/render e não novo write automático.
- **ASICS Gel NYC:** a página está `HTTP 200`, com guia/schema e `FAQPage=1`, mas a meta description pública ainda contém `Envio imediato e troca grátis`, termo operacional fora do guardrail LK. Isso deve virar cleanup packet de SEO/meta/OG se confirmado em Admin/readback, sem execução automática.
- **NB740:** segue lacuna prioritária de superfície canônica; confirmar/criar collection é dono LK Shopify, com Growth entregando escopo/SEO/GEO.

### PageSpeed / CrUX

Execução read-only via PageSpeed Insights API, com secrets injetados pelo helper Doppler e sem imprimir valores:

- URL: `https://lksneakers.com.br/`
- Strategy: mobile
- Performance score lab: `0.55`
- LCP lab: `16.6 s`
- TBT lab: `140 ms`
- CLS lab: `0`
- CrUX/loadingExperience: `FAST`
- Origin loadingExperience: `FAST`

Leitura: field data/origin aparece bom, mas o lab mobile ainda sugere gargalo de LCP acima da dobra. Não é prioridade de write neste sábado; entra como monitoramento/performance packet se repetir em páginas de coleção/PDP.

### Conectores / disponibilidade

- GSC read-only: OK via script local Doppler-first.
- PageSpeed API key: `PAGESPEED_API_KEY` e `GOOGLE_API_KEY` presentes; `CRUX_API_KEY` ausente; valores não impressos.
- `hermes-cli-integrations smoke google_workspace shopify_lk`: retornou `failed` para ambos nesta execução (`values_printed=false`). Como GSC funcionou via script e Shopify não foi necessário para writes, isso é limitação operacional, não bloqueio de QA público.
- GA4/Shopify commercial impact: parcial/não atualizado nesta rotina; usar D+7/D+14 quando houver janela suficiente e connector OK.
- GMC: último snapshot material é 2026-06-25; `landing_page_error` permanece packet prioritário até nova leitura GMC.
- DataForSEO AI/LLM: não executado; histórico recente registrou bloqueio de AI mentions/subscription e ausência de MCP ativo.

## Impact review / experiment ledger

| Experimento/mudança | Data live | Evidência atual | Classificação | Próxima ação segura |
|---|---:|---|---|---|
| Pacote B / Nike Mind PDP FAQ + nomenclatura | 2026-06-19 | PDP Light Smoke Grey HTTP 200, H1 único, Product/Breadcrumb/FAQPage, GSC ainda mostra CTR muito baixo para Mind 001 nas PDPs Black/Pearl | `qa_ok_impact_inconclusive` | D+14 com GSC/GA4/Shopify; não novo write imediato. |
| LKGOC C1+C2 AI Visibility | 2026-06-19 | D+7 oficial 2026-06-26: sinais mistos positivos; `llms.txt` cobre 2/6 handles; `agents.md` 6/6 | `early_mixed_positive` | D+14 em 2026-07-03; possível packet read-only de `llms.txt` se gap confirmar. |
| NB530 hub SERP FAQ | 2026-06-25 | QA público hoje: HTTP 200, FAQPage=1, sem Liquid error | `qa_ok_no_impact_window` | Medir GSC D+7/D+14 (`new balance 530`, `530 feminino`, page). |
| Adidas SL72 guide/FAQ/schema | 2026-06-25 | QA público hoje: HTTP 200, FAQPage=1, sem Liquid error | `qa_ok_no_impact_window` | Medir D+7/D+14. |
| ASICS Gel NYC guide/FAQ/schema | 2026-06-26 | HTTP 200, FAQPage=1, sem Liquid error; porém meta/OG contém `Envio imediato e troca grátis` | `qa_partial_cleanup_needed` | Confirmar Admin/readback SEO/meta; preparar cleanup packet sem write. |
| Adidas Taekwondo SEO/meta + DEV guide | 2026-06-26 | HTTP 200, title novo, FAQPage=0 conforme production escopo; sem Liquid error | `qa_ok_no_impact_window` | D+7/D+14; production guide/schema só com aprovação separada. |
| Adidas Tokyo schema-only | 2026-06-26 | HTTP 200, mas `FAQPage=0` embora receipt anterior dissesse 1 | `qa_regression_or_render_gap` | Readback técnico snippet/render; packet de correção se confirmado. |
| Puma Speedcat schema-only | 2026-06-26 | HTTP 200, mas `FAQPage=0` embora receipt anterior dissesse 1 | `qa_regression_or_render_gap` | Readback técnico snippet/render; packet de correção se confirmado. |
| Adidas Sambae bug público | Packet 2026-06-26 | Hoje `Liquid error=false`, title novo, FAQPage=1, forbidden terms zerados | `qa_fixed_monitor` | Não sugerir como bug pendente; apenas monitorar e medir. |
| NB740 GEO/source-page | Packet 2026-06-26 | `/collections/new-balance-740` cai na coleção geral; `llms` sem NB740 específico no relatório de sexta | `surface_gap_confirmed` | Handoff para LK Shopify validar/criar collection canônica; depois Growth DEV/preview para FAQ/schema/bloco citável. |

## Cobertura dos 18 tópicos

- GA4: parcial/não atualizado hoje; impact comercial ainda não decision-grade.
- GSC: coberto, script executado.
- GMC: parcial via snapshot 2026-06-25; sem novo write.
- Shopify SEO: QA público e receipts revisados; Admin/readback Shopify não executado por smoke wrapper falho.
- Shopify CRO: não aplicável nesta rotina salvo QA público leve.
- GEO/AI Search: `llms.txt`, `llms-full.txt`, `agents.md`, FAQPage e NB740/llms gap revisados.
- PageSpeed/CrUX/CWV: PageSpeed mobile home executado; field/origin FAST; lab LCP ruim.
- Schema: coberto em PDP/collections, achados Tokyo/Speedcat/ASICS/NB740.
- Reviews: parcial via schema AggregateRating público, sem Judge.me deep-dive.
- Paid media: não consultado; não necessário para QA técnico.
- Influencer/social demand: não consultado nesta rotina.
- Concorrência/SERP: usado via relatórios anteriores; sem nova SERP live ampla hoje.
- Google Business/local: parcial via Organization/local schema home.
- Klaviyo/CRM: não consultado.
- Catálogo/product data quality: parcial via GMC 2026-06-25 e QA collection/PDP; sem estoque.
- Conteúdo/taxonomia comercial: coberto nos guardrails de copy e NB740 canônico.
- Mensuração/QA de eventos: parcial; GA4/Shopify impact não atualizado.
- Impact review/experimentation: atualizado neste relatório.

## Decisão recomendada

Prioridade de segunda/terça: **readback técnico/packet de correção para schema-only Tokyo/Speedcat + cleanup meta ASICS Gel NYC + handoff NB740 canônico**. Não executar writes automaticamente.

## Non-actions

- Não consultei Tiny/estoque/disponibilidade.
- Não executei Shopify/theme/GMC/feed/GA4/GSC config/Ads/Klaviyo/WhatsApp/e-mail/preço/estoque/desconto write.
- Não imprimi secrets/tokens/service-account JSON.
- Não tratei `agents.txt` 404 como quebra porque `agents.md` e `llms` estão ativos.
