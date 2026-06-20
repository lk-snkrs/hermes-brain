# Nike Mind FAQ schema fix — final status

{
  "values_printed": false,
  "created_utc": "2026-06-19T20:36:47.196174+00:00",
  "status": "code_and_admin_correct_public_cache_not_stable",
  "what_changed": [
    "sections/lk-pdp.liquid: FAQ visual uses custom.faq; generic FAQ fallback only when custom.faq blank",
    "sections/lk-pdp.liquid: FAQPage JSON-LD uses same custom.faq with forloop.last comma safety",
    "2 Nike Mind PDPs touched with invisible body_html cache-bust marker"
  ],
  "public_validation_summary": {
    "slide-nike-mind-001-pearl-pink-rosa": {
      "samples": 19,
      "visible_7": 8,
      "schema_7": 8,
      "generic_schema_0": 0,
      "disclaimer": 8,
      "latest": {
        "visible": 0,
        "schema": 0,
        "generic_schema": 999,
        "title": "Nike Mind 001 Pearl Pink Original | LK Sneakers",
        "qs": [
          "Os produtos são originais?",
          "Qual o prazo de entrega?",
          "Como é a embalagem?",
          "Posso parcelar?"
        ]
      }
    },
    "slide-nike-mind-001-light-smoke-grey-cinza": {
      "samples": 19,
      "visible_7": 0,
      "schema_7": 0,
      "generic_schema_0": 0,
      "disclaimer": 0,
      "latest": {
        "visible": 2,
        "schema": 0,
        "generic_schema": 999,
        "title": "Nike Mind 001 Light Smoke Grey Original | LK Sneakers",
        "qs": [
          "Qual tamanho escolher no Slide Nike Mind 001 Light Smoke Grey?",
          "O Slide Nike Mind 001 Light Smoke Grey vendido na LK é original?",
          "Posso usar o Slide Nike Mind 001 Light Smoke Grey na chuva?",
          "Os produtos são originais?",
          "Qual o prazo de entrega?",
          "Como é a embalagem?",
          "Posso parcelar?"
        ]
      }
    }
  },
  "blocker": "public storefront still alternates old cached HTML/schema; cache-bust marker does not appear publicly yet",
  "recommendation": "wait/revalidate; if still stale, escalate to Shopify/theme cache/publish-level fix instead of more PDP content writes"
}