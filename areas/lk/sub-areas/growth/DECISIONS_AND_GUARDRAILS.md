# Growth decisions and guardrails

## 2026-06-19 — PDP FAQ / JSON-LD guardrail

- Antes de propor ou aplicar FAQ em PDP Shopify da LK, verificar obrigatoriamente a cadeia completa: `product.metafields.custom.faq` → FAQ visual no HTML público → `FAQPage` JSON-LD público → paridade entre perguntas/respostas visíveis e schema.
- Nunca usar `body_html`/descrição como container de FAQ quando existir estrutura própria (`custom.faq`, bloco `pi-faq` ou equivalente).
- Para SEO/GEO/AI Visibility, o conteúdo só é considerado pronto quando as perguntas estão renderizadas no HTML público e no JSON-LD, não apenas gravadas no Admin.
- Se houver oscilação de cache/réplica no storefront, marcar como não finalizado para IA até validação pública estável.
- Esse check deve entrar antes de qualquer write em produto, tema ou conteúdo relacionado a FAQ.
