# Curadoria LK fixes — thumbs, position, color pi-section

{
  "timestamp_utc": "2026-06-02T13:50:46.156537+00:00",
  "theme_id": "155065450718",
  "changed_assets": [
    "snippets/lk-variante-top30-visited.liquid",
    "sections/lk-pdp.liquid"
  ],
  "requested_fixes": [
    "thumbs functional",
    "Curadoria LK after price",
    "remove duplicated color pi-section legacy selector"
  ],
  "qa": {
    "url": "https://www.lksneakers.com.br/products/jaqueta-lululemon-define-nulu?preview_theme_id=155065450718&fixqa=1",
    "status_len": 1367181,
    "readback_snippet_match": true,
    "readback_pdp_sha16": "c4f1847d83cc6ce5",
    "block": true,
    "items": 5,
    "imgs": 5,
    "first_imgs": [
      "<img src=\"https://cdn.shopify.com/s/files/1/0621/8969/9294/files/jaqueta-lululemon-define-luon-white-branco-lk-3637785.png?v=1779804672\" alt=\"Luon White\" width=\"72\" height=\"72\" loading=\"lazy\" decoding=\"async\">",
      "<img src=\"https://cdn.shopify.com/s/files/1/0621/8969/9294/files/jaqueta-lululemon-define-nulu-blackgold-preto-lk-8103980.png?v=1779804673\" alt=\"Black Gold\" width=\"72\" height=\"72\" loading=\"lazy\" decoding=\"async\">"
    ],
    "position_after_price": true,
    "color_pi_section_present": false,
    "size_label_present": true,
    "errors": 0,
    "prod_control_blocks": 0,
    "section_labels_after_price": [
      "Tamanho: XXS/PPP Guia de tamanhos"
    ],
    "note": "Second HTML inspection: no COR/Color pi-section after price; only Tamanho pi-section remains intentionally, because size selector is required for ATC."
  },
  "backup_dir": "/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/lk-variante/fix-thumbs-price-position-remove-color-pisection-20260602T134844Z",
  "non_actions": [
    "production theme",
    "publish",
    "products",
    "prices",
    "stock",
    "campaigns",
    "apps disabled"
  ]
}