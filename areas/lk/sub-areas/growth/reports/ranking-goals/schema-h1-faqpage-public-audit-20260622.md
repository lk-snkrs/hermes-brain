# Auditoria pública read-only — Schema / H1 / FAQPage — 2026-06-22

**Escopo:** top páginas comerciais iniciais solicitadas. Auditoria por HTTP público/HTML raw via `requests`, sem writes externos.  
**Excluídas como próxima ação:** `/collections/nike-mind-001` e `/collections/nike-vomero-premium`; usadas apenas como referência/impact review, pois há evidência local de cleanup aplicado em 2026-06-22.  
**Timestamp da coleta:** 2026-06-22T17:06:54Z.  
**Host auditado:** `https://lksneakers.com.br` (requests iniciou em `www` e seguiu 301 canônico).

## Achados P0/P1

### P0

Nenhum P0 técnico confirmado nas páginas auditadas: não encontrei H1 duplicado, JSON-LD inválido, ausência de Product schema em PDP auditado, ausência de CollectionPage/Breadcrumb nas collections ativas, nem `Liquid error`/`translation missing` público.

### P1

1. **`/collections/alo-yoga` redireciona para home**  
   - Evidência pública: histórico HTTP `301 https://lksneakers.com.br/collections/alo-yoga` → `301 https://lksneakers.com.br/`; final `200` na home.  
   - Impacto: página comercial citada em relatórios recentes deixa de expor H1/schema/FAQ/canonical próprios; o HTML final tem H1 da home, canonical da home, sem CollectionPage/Breadcrumb/FAQPage.  
   - Prioridade: P1 por perda de landing/canonização para cluster comercial.

2. **Collections comerciais com `FAQPage=0`** — não é erro fatal, mas é gap de schema/citabilidade em páginas com demanda/comercialidade.  
   - `/collections/crocs-relampago-mcqueen`: H1=1, CollectionPage=1, Breadcrumb=1, FAQPage=0.  
   - `/collections/adidas-handball-spezial`: H1=1, CollectionPage=1, Breadcrumb=1, FAQPage=0.  
   - `/collections/new-balance-1906l`: H1=1, CollectionPage=1, Breadcrumb=1, FAQPage=0.  
   - `/collections/air-jordan-1-low`: H1=1, CollectionPage=1, Breadcrumb=1, FAQPage=0.  
   - Impacto: menor elegibilidade/clareza de FAQ real-intent vs. benchmarks que já têm FAQPage único.

3. **`/collections/onitsuka-tiger-todos-os-modelos` ainda mostra title/meta público anterior ao receipt do Package A**  
   - Evidência local: `growth-commercial-ctr-package-a-20260619/PACKAGE_A_FINAL_RECEIPT.md` diz que Admin API foi atualizado, mas polling público final ainda servia title/meta/body anterior/cache.  
   - Evidência pública atual: title `Onitsuka Tiger Original no Brasil | Mexico 66 e LK`; meta `... para escolher.`; H1/schema OK.  
   - Impacto: não é schema P0; é P1 de propagação/consistência de SEO copy em página top.

## Matriz pública coletada

| Página | Status/final | H1 | FAQPage | Product | CollectionPage | Breadcrumb | JSON-LD parse | Liquid público | Nota |
|---|---:|---|---:|---:|---:|---:|---:|---|---|
| `/products/crocs-classic-clog-x-the-cars-lightning-mcqueen-vermelho` | 200 final canonical PDP | 1 — `Crocs Classic Clog x The Cars Lightning McQueen Vermelho` | 1 | 1 | 0 | 1 | 0 erros | 0 | OK; trabalhada 2026-06-19 Package A. |
| `/collections/onitsuka-tiger-todos-os-modelos` | 200 | 1 — `Onitsuka Tiger` | 1 | 0 | 1 | 1 | 0 | 0 | OK schema; checar propagação title/meta do Package A. |
| `/collections/onitsuka-tiger-mexico-66` | 200 | 1 — `Onitsuka Tiger Mexico 66` | 1 | 0 | 1 | 1 | 0 | 0 | OK; redirects antigos corrigidos 2026-06-18. |
| `/collections/lululemon` | 200 | 1 — `Lululemon` | 1 | 0 | 1 | 1 | 0 | 0 | OK; trabalhada em Ahrefs 1–4 em 2026-06-19. |
| `/collections/yeezy` | 200 | 1 — `Yeezy` | 1 | 0 | 1 | 1 | 0 | 0 | OK; teve redirect/page fixes 2026-06-18. |
| `/collections/air-jordan-travis-scott` | 200 | 1 — `Nike x Travis Scott` | 1 | 0 | 1 | 1 | 0 | 0 | OK schema; refresh packet recente 2026-06-17; redirect antigo para `/collections/air-jordan` corrigido. |
| `/collections/crocs-relampago-mcqueen` | 200 | 1 — `Crocs Relâmpago McQueen` | 0 | 0 | 1 | 1 | 0 | 0 | P1 gap FAQPage em collection. |
| `/collections/adidas-handball-spezial` | 200 | 1 — `Adidas Handball Spezial` | 0 | 0 | 1 | 1 | 0 | 0 | P1 gap FAQPage em collection. |
| `/collections/new-balance-204l` | 200 | 1 — `New Balance 204L` | 1 | 0 | 1 | 1 | 0 | 0 | OK; benchmark, trabalhada/revisada recentemente. |
| `/collections/new-balance-1906l` | 200 | 1 — `New Balance 1906L` | 0 | 0 | 1 | 1 | 0 | 0 | P1 gap FAQPage em collection; PDPs 1906L trabalhados 2026-06-18. |
| `/collections/alo-yoga` | 200 final home após 301+301 | 1 da home | 0 | 0 | 0 | 0 | 0 | 0 | P1: handle redireciona para home; sem landing/schema próprios. |
| `/collections/air-jordan-1-low` | 200 | 1 — `Air Jordan 1 Low` | 0 | 0 | 1 | 1 | 0 | 0 | P1 gap FAQPage em collection. |

## Referência/impact review — páginas corrigidas hoje, não usar como próxima ação

| Página | Status/final | H1 | FAQPage | CollectionPage | Breadcrumb | Nota |
|---|---:|---|---:|---:|---:|---|
| `/collections/nike-mind-001` | 200 | 1 — `Nike Mind 001/002` | 1 | 1 | 1 | Corrigida hoje; antes havia 2 FAQPage segundo command center. Agora público mostra FAQPage único. |
| `/collections/nike-vomero-premium` | 200 | 1 — `Nike Vomero Premium` | 1 | 1 | 1 | Corrigida hoje; antes havia 2 FAQPage segundo command center. Agora público mostra FAQPage único. |

## Evidência local de “já trabalhada recentemente”

- Hoje / excluídas: `impact-reviews/nike-mind-vomero-collection-cleanup-20260622/2026-06-29-D+7-review.md` registra cleanup aplicado em `/collections/nike-mind-001` e `/collections/nike-vomero-premium` em 2026-06-22.
- PDP Crocs McQueen + Onitsuka todos modelos: `growth-commercial-ctr-package-a-20260619/PACKAGE_A_FINAL_RECEIPT.md` registra SEO/microcopy/FAQ/intro aplicados; Crocs validou publicamente, Onitsuka tinha cache/propagação no polling final.
- Lululemon: `ahrefs-execute-1to4-20260619/AHREFS_1TO4_EXECUTION_RECEIPT.md` registra write/verify público em `/collections/lululemon`.
- Onitsuka Mexico 66 / Yeezy / New Balance 204L / Air Jordan Travis Scott: `ahrefs-p0-fix-packet/20260618T205642Z/P0_B1_B2_B4_EXECUTION_RECEIPT.md` registra redirects de pages antigas para collections.
- Air Jordan Travis Scott: `ranking-goals/factory-3-4-5-20260617/EXECUCAO-3-4-5-20260617.md` registra diagnóstico/packet recente; público atual já tem FAQPage=1.
- New Balance 1906L e PDPs Onitsuka/Vomero: `pdp-leakage/pdp-leakage-20260618T181804Z/batch-1-5-execution-20260618T183732Z/RECEIPT.md` registra execução recente em PDPs, não necessariamente na collection 1906L.

## Notas de metodologia

- `nil` em HTML foi ignorado como falso positivo: aparece em handles/textos como `leonilson` ou dados de produto, não como erro Liquid. Contagens confirmadas: `Liquid error=0`, `Liquid syntax error=0`, `translation missing=0` nas amostras.
- JSON-LD parse errors: 0 em todas as páginas auditadas.
- 301 de `www` para apex é normal/canônico; único redirect problemático encontrado foi `/collections/alo-yoga` para home.
