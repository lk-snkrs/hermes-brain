# LK Growth — Ranking OS v2 — QA + Impact Review — 2026-06-20

- Execução: `2026-06-20T11:31Z`.
- Modo: read-only / preview; nenhum write externo executado.
- values_printed=false; Shopify Admin usado apenas com GraphQL `query` para confirmar readback de SEO fields.

## Veredito executivo

Há achado material para Lucas: o QA público pós-propagação resolveu o bloqueio dos PDPs Nike Mind 001 — os 2 PDPs agora retornam HTTP 200, H1 único, FAQ visual com 7 perguntas e FAQPage JSON-LD com as mesmas 7 perguntas, sem FAQ genérico legado. A oportunidade/riscos restantes são: `collection /collections/nike-mind-001` ainda renderiza **2 FAQPage JSON-LD** com perguntas parcialmente duplicadas, e o impact review comercial do Pacote B ainda é `no_signal_yet` por janela curta.

## Escopo QA leve

URLs e assets testados:

| Superfície | URL | Status | Title/meta | H1 | Schema | Observação |
|---|---:|---:|---|---:|---|---|
| Home | `https://lksneakers.com/` → `.com.br/` | 200 | OK | 1 | Organization/ShoeStore/ClothingStore/WebSite | Sem noindex; canonical `.com.br` |
| PDP prioritária | `/products/slide-nike-mind-001-light-smoke-grey-cinza` | 200 | OK após nomenclatura `Nike Mind Slide 001` | 1 | Product/BreadcrumbList/FAQPage | 7 FAQ visíveis + 7 no schema; sem FAQ genérico |
| Collection prioritária | `/collections/nike-mind-001` | 200 | OK | 1 | BreadcrumbList/CollectionPage/FAQPage/FAQPage | Risco: 2 FAQPage JSON-LD; perguntas repetidas/parciais |
| `robots.txt` | `/robots.txt` | 200 | n/a | n/a | n/a | Sitemap presente; GPTBot/OAI-SearchBot/ChatGPT-User/ClaudeBot/PerplexityBot mencionados |
| `sitemap.xml` | `/sitemap.xml` | 200 | n/a | n/a | n/a | Inclui `sitemap_agentic_discovery.xml` e sitemaps Shopify |
| `llms.txt` | `/llms.txt` | 200 | n/a | n/a | n/a | `Last updated: 2026-06-19`; 251 linhas |
| `llms-full.txt` | `/llms-full.txt` | 200 | n/a | n/a | n/a | `Last updated: 2026-06-19`; 526 linhas |
| `agents.txt` | `/agents.txt` | 404 | n/a | n/a | n/a | Não tratado como quebra porque é “quando aplicável”; `llms` está OK |

## Readback específico — Pacote B / Nike Mind

### Receipts revisados

- `reports/growth-commercial-ctr-package-b-20260619/PACKAGE_B_EXECUTION_SUMMARY.md`
- `receipts/shopify-production-nike-mind-slide-nomenclature-fix-20260619T195122Z.md`
- `receipts/shopify-production-nike-mind-001-faq7-20260619T201857Z.md`
- `reports/nike-mind-001-faq-schema-fix-20260619/FINAL_STATUS.md`
- `reports/impact-reviews/product-description-operational-copy-cleanup-d14-20260619T191244Z/impact-review.md`

### O que mudou desde o status final anterior

O relatório `FINAL_STATUS.md` de 2026-06-19 marcava `code_and_admin_correct_public_cache_not_stable`. O QA de hoje confirmou estabilização pública nos 2 PDPs Nike Mind:

- `slide-nike-mind-001-light-smoke-grey-cinza`: 7/7 perguntas visíveis; 7/7 em FAQPage; FAQ genérico legado ausente.
- `slide-nike-mind-001-pearl-pink-rosa`: 7/7 perguntas visíveis; 7/7 em FAQPage; FAQ genérico legado ausente.
- Admin readback atual confirma os SEO fields finais pós-nomenclatura:
  - `Nike Mind Slide 001 Light Smoke Grey Original | LK`
  - `Nike Mind Slide 001 Pearl Pink Original | LK`
- Isso não é reversão indesejada: está alinhado ao receipt de nomenclatura que corrigiu `Nike Mind 001` para `Nike Mind Slide 001`.

## Impact review / experiment ledger

| Experimento/mudança | Data live | Status hoje | Classificação | Próxima leitura |
|---|---:|---|---|---|
| Pacote B CTR Produtos — 4 PDPs | 2026-06-19 | QA técnico OK; janela curta para impacto | `no_signal_yet` | D+7 em ~2026-06-26 com GSC/GA4/Shopify |
| Nike Mind 001 FAQ7 + schema parity | 2026-06-19 | Regra de FAQ real intent e parity agora OK nos 2 PDPs | `learning_only` positivo | Revalidar junto com D+7 do Pacote B |
| Limpeza de termos operacionais D+14 | review 2026-06-19 | Regressão em `seo_description` com `envio imediato` já detectada em 172 produtos; GA4 403 | `material_anomaly` já documentado | Precisa approval packet específico; não executar automático |
| Collection Nike Mind 001/002 | anterior | 2 FAQPage JSON-LD detectados publicamente | `material_anomaly` leve | Preparar packet/dev fix para schema único se Lucas aprovar |

## Limitações de decisão

- GA4 segue parcial no impact review D+14 por `403` na propriedade canônica `253411115`; não declarar review 100% decision-grade até normalizar permissão ou confirmar propriedade funcional.
- Pacote B ainda não tem janela suficiente para variação GSC/GA4/Shopify; Search Analytics também tem lag de 2–3 dias.
- PageSpeed/CrUX não foi reexecutado nesta passada porque o review anterior registrou timeout e a decisão material de hoje veio de QA público/schema/readback; recomendável rodar novamente no D+7 se a rotina não expirar.
- Não consultei estoque/Tiny/availability; fora do escopo Growth e pertence ao `lk-stock`.

## Decisão/packet recomendado

### Packet pequeno — schema único na collection Nike Mind 001

- Problema: `/collections/nike-mind-001` publica 2 blocos `FAQPage` com sobreposição:
  - bloco A: `Qual a diferença entre Nike Mind 001 e Nike Mind 002?`, `Nike Mind é tênis de corrida?`, `Qual Nike Mind é mais fácil de usar na rua?`, `O Nike Mind da LK Sneakers é original?`
  - bloco B: `O que o Nike Mind 001 faz?`, `Qual a diferença entre Nike Mind 001 e Nike Mind 002?`, `Nike Mind 001 é tênis de corrida?`, `Nike Mind 001 é confortável para usar na rua?`, `O Nike Mind 001 da LK é original?`
- Impacto esperado: melhora de higiene schema/GEO, reduz ambiguidade para Google/LLMs e mantém padrão de FAQ único aprovado pela LK.
- Esforço: baixo/médio, provavelmente ajuste theme/section ou fonte de FAQ da collection.
- Risco: baixo se feito primeiro em dev theme; produção exige aprovação explícita e rollback.
- Próximo passo sem aprovação: preparar approval packet com diff proposto e QA esperado.
- Precisa aprovação antes de executar: qualquer Shopify/theme production write.

## Non-actions

Nenhum write em Shopify, theme, GMC/feed, GA4/GSC config, Ads, Klaviyo/WhatsApp/email, preço, estoque, desconto ou campanha foi executado.
