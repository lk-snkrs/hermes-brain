# Receipt — fix Sambae guide branch routing DEV

Data UTC: 2026-06-02T22:13:09Z
Tema DEV: 155065450718
Produção: não alterada.

Correção: Sambae removido do branch Nike Mind e inserido no branch padrão `lk-guide-standard-panel` usado pela 204L.

QA:
```json
{
  "theme_id": "155065450718",
  "production_changed": false,
  "section_bytes": 260169,
  "under_256kb": true,
  "nike_mind_if_clean": true,
  "sambae_in_standard_guide_elsif": true,
  "sambae_not_in_nike_mind_if": true,
  "sambae_phase_anchor_count": 1,
  "sambae_guide_h2_count": 1,
  "sambae_card_count": 1,
  "readmore_js_has_copy_toggle": true,
  "readmore_js_has_ler_menos": true,
  "old_wrong_snippet_refs": 0,
  "routing_excerpt": " frete, prazo e parcelamento aparecem no checkout conforme endereço e forma de pagamento.\"}}\n    ]\n  }\n  </script>\n{%- endif -%}\n\n{%- if collection.handle == 'nike-mind-001' -%}\n  {% render 'lk-nike-mind-guide-panel' %}\n{%- elsif collection.handle == 'new-balance-204l' or collection.handle == 'adidas-sambae' or collection.handle == 'nike-x-jacquemus-moon-shoe-sp' or collection.handle == 'adidas-samba-jane' or collection.handle == 'onitsuka-tiger' or collection.handle == 'onitsuka-tiger-todos-os-modelos' or collection.handle == 'onitsuka-tiger-mexico-66-sabot' or collection.handle == 'onitsuka-"
}
```
