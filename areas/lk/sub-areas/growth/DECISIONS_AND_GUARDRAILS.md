# Growth decisions and guardrails

## 2026-06-19 — PDP FAQ / JSON-LD guardrail

- Antes de propor ou aplicar FAQ em PDP Shopify da LK, verificar obrigatoriamente a cadeia completa: `product.metafields.custom.faq` → FAQ visual no HTML público → `FAQPage` JSON-LD público → paridade entre perguntas/respostas visíveis e schema.
- Nunca usar `body_html`/descrição como container de FAQ quando existir estrutura própria (`custom.faq`, bloco `pi-faq` ou equivalente).
- Para SEO/GEO/AI Visibility, o conteúdo só é considerado pronto quando as perguntas estão renderizadas no HTML público e no JSON-LD, não apenas gravadas no Admin.
- Se houver oscilação de cache/réplica no storefront, marcar como não finalizado para IA até validação pública estável.
- Esse check deve entrar antes de qualquer write em produto, tema ou conteúdo relacionado a FAQ.

## Guardrail AI/GEO endpoints — 2026-06-21

- `/llms.txt` da LK deve permanecer curto, curated e estável, com `LK_GEO_SOURCE_MAP_START`; não regenerar de catálogo/páginas/blogs brutos.
- `/llms-full.txt` pode ser completo, mas deve ser sanitizado, com `LK_GEO_SOURCE_MAP_START` e sem termos operacionais públicos como `pronta entrega`, `encomenda`, `sob encomenda`, `prazo de entrega`, `confirme disponibilidade` ou uso promocional de `estoque`.
- Qualquer rotina de SEMrush/Ahrefs/SEO/GEO que tocar assets AI deve preservar baseline aprovada ou abrir approval packet específico com rollback/readback.
- `/agents.md` pode conter `estoque` apenas em guardrails negativos, por exemplo “não afirmar estoque”; isso não deve ser contado como oferta/disponibilidade.
- Se monitor acusar drift em `/llms.txt` ou `/llms-full.txt`, prioridade é restaurar baseline limpa antes de atualizar baseline.

