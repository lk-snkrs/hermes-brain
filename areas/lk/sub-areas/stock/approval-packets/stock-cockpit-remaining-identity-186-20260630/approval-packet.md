# Approval packet — LK Stock Cockpit remaining identity blockers 186 — 2026-06-30

- generated_at_utc: `2026-06-30T12:52:55Z`
- Pedido: Lucas pediu “Fazer corrigir todos os problemas possíveis”.
- Escopo executado antes deste packet: negativos zerados; SKU/tamanho ausente zerado; parent/base fora de anomalia; 63 técnicos resolvidos por Tiny exact readback.
- Estado residual verificado: **186 problemas técnicos**, todos bloqueados por identidade/cadastro.
- values_printed: false

## Resultado do diagnóstico residual

| Bucket | Count | Por que não dá para corrigir sem write/cadastro |
|---|---:|---|
| Tiny exact missing | 116 | SKU do read model/Shopify não encontra produto Tiny exato; precisa criar/corrigir SKU/código/cadastro ou mapear variante. |
| Tiny exact duplicate | 70 | Mais de um produto Tiny para o mesmo SKU; precisa deduplicar/desativar/eleger variante correta. |
| **Total** | **186** | Nenhum é correção determinística segura de read model sem risco de mentir disponibilidade. |

## Artefatos exatos

- JSON completo: `areas/lk/sub-areas/stock/approval-packets/stock-cockpit-remaining-identity-186-20260630/remaining_186_identity_blockers.json`
- CSV completo: `areas/lk/sub-areas/stock/approval-packets/stock-cockpit-remaining-identity-186-20260630/remaining_186_identity_blockers.csv`
- Missing-only: `blocked_tiny_exact_missing.json`
- Duplicate-only: `blocked_tiny_exact_duplicate.json`

## Amostra — Tiny exact missing

```json
[
  {
    "sku": "PAC-8676062-40",
    "handle": "shorts-pace-midmasa-tailored-charcoal",
    "product_name": "Shorts Pace Midmasa Tailored Charcoal",
    "size": "40",
    "demand_tier": "NONE",
    "prior_status": "BLOCKED_TINY_MISSING_LIVE_FULL",
    "resolution": "blocked_tiny_exact_missing",
    "tiny_exact_count": 0,
    "tiny_exact_sample_count": 0,
    "next_required_action": "tiny_or_shopify_identity_write_required"
  },
  {
    "sku": "CV1659001",
    "handle": "nike-sb-dunk-low-vx-1000-camcorder",
    "product_name": "Tênis Nike SB Dunk Low VX 1000 Camcorder Cinza",
    "size": "35",
    "demand_tier": "NONE",
    "prior_status": "BLOCKED_SHOPIFY_DUPLICATE_LIVE_FULL",
    "resolution": "blocked_tiny_exact_missing",
    "tiny_exact_count": 0,
    "tiny_exact_sample_count": 0,
    "next_required_action": "tiny_or_shopify_identity_write_required"
  },
  {
    "sku": "1203A655-100-7",
    "handle": "tenis-asics-gt-2160-x-above-the-clouds-white-pure-silver-branco",
    "product_name": "Tênis Asics GT-2160 x Above the Clouds White Pure Silver Branco",
    "size": "41",
    "demand_tier": null,
    "prior_status": "BLOCKED_TINY_MISSING_LIVE_FULL",
    "resolution": "blocked_tiny_exact_missing",
    "tiny_exact_count": 0,
    "tiny_exact_sample_count": 0,
    "next_required_action": "tiny_or_shopify_identity_write_required"
  },
  {
    "sku": "JH392-3",
    "handle": "tenis-adidas-sl72-og-solar-red-lavander-vermelho",
    "product_name": "Tênis adidas SL 72 Og Solar Red Lavander Vermelho",
    "size": "36",
    "demand_tier": null,
    "prior_status": "BLOCKED_TINY_DEPOSIT_MISSING_LIVE_FULL",
    "resolution": "blocked_tiny_exact_missing",
    "tiny_exact_count": 0,
    "tiny_exact_sample_count": 0,
    "next_required_action": "tiny_or_shopify_identity_write_required"
  },
  {
    "sku": "CD2563006-9",
    "handle": "nike-sb-dunk-low-pro-iso-black-gum",
    "product_name": "Tênis Nike SB Dunk Low Pro ISO Black Gum Preto",
    "size": "44",
    "demand_tier": "NONE",
    "prior_status": "BLOCKED_TINY_DUPLICATE_LIVE_FULL",
    "resolution": "blocked_tiny_exact_missing",
    "tiny_exact_count": 0,
    "tiny_exact_sample_count": 0,
    "next_required_action": "tiny_or_shopify_identity_write_required"
  }
]
```

## Amostra — Tiny exact duplicate

```json
[
  {
    "sku": "ST33",
    "handle": "camiseta-boxy-saint-studio-supima-preto",
    "product_name": "Camiseta Boxy Saint Studio Supima Preto",
    "size": "P/S",
    "demand_tier": "HIGH",
    "prior_status": "BLOCKED_SHOPIFY_DUPLICATE_LIVE_FULL",
    "resolution": "blocked_tiny_exact_duplicate",
    "tiny_exact_count": 5,
    "tiny_exact_sample_count": 3,
    "next_required_action": "deduplicate_tiny_or_map_exact_variant_required"
  },
  {
    "sku": "1183B566.201",
    "handle": "tenis-onitsuka-tiger-mexico-66-gold-white-dourado",
    "product_name": "Tênis Onitsuka Tiger Mexico 66 Gold White Dourado",
    "size": "39.5",
    "demand_tier": "MEDIUM",
    "prior_status": "BLOCKED_TINY_DUPLICATE_LIVE_FULL",
    "resolution": "blocked_tiny_exact_duplicate",
    "tiny_exact_count": 2,
    "tiny_exact_sample_count": 2,
    "next_required_action": "deduplicate_tiny_or_map_exact_variant_required"
  },
  {
    "sku": "PC9060GY-2",
    "handle": "tenis-new-balance-9060-kids-raincloud-cinza",
    "product_name": "Tênis New Balance 9060 Kids Raincloud Cinza (Infantil)",
    "size": "33",
    "demand_tier": "MEDIUM",
    "prior_status": "BLOCKED_TINY_DUPLICATE_LIVE_FULL",
    "resolution": "blocked_tiny_exact_duplicate",
    "tiny_exact_count": 2,
    "tiny_exact_sample_count": 2,
    "next_required_action": "deduplicate_tiny_or_map_exact_variant_required"
  },
  {
    "sku": "41499672090-4",
    "handle": "chinelo-havaianas-x-dolce-gabanna-carreto-ciciliano-vermelho",
    "product_name": "Chinelo Havaianas x Dolce & Gabbana Carreto Ciciliano Vermelho",
    "size": "41/42",
    "demand_tier": "MEDIUM",
    "prior_status": "BLOCKED_TINY_DUPLICATE_LIVE_FULL",
    "resolution": "blocked_tiny_exact_duplicate",
    "tiny_exact_count": 2,
    "tiny_exact_sample_count": 2,
    "next_required_action": "deduplicate_tiny_or_map_exact_variant_required"
  },
  {
    "sku": "ST34",
    "handle": "camisa-manga-curta-boxy-saint-studio-egipcio-listrada-marinho",
    "product_name": "Camisa Manga Curta Boxy Saint Studio Egípcio Listrada Marinho",
    "size": "P/S",
    "demand_tier": "NONE",
    "prior_status": "BLOCKED_SHOPIFY_DUPLICATE_LIVE_FULL",
    "resolution": "blocked_tiny_exact_duplicate",
    "tiny_exact_count": 5,
    "tiny_exact_sample_count": 3,
    "next_required_action": "deduplicate_tiny_or_map_exact_variant_required"
  }
]
```

## Correções possíveis por política

### Opção A — Missing SKUs/códigos Tiny, lote 116

Autoriza apenas preparar/executar correção de identidade para os 116 `blocked_tiny_exact_missing` após readback live por SKU/handle/variant.

- Possível write: Tiny cadastro/código ou Shopify SKU/variant, conforme fonte raiz confirmada.
- Não autoriza: estoque/quantidade, preço, publicação, compra, fornecedor, cliente.
- Requer antes: readback live Tiny + Shopify por item e snapshot rollback.
- Readback depois: SKU exato passa a resolver 1:1, health reduz bucket missing.

### Opção B — Duplicados Tiny, lote 70

Autoriza apenas preparar/executar deduplicação/mapeamento dos 70 `blocked_tiny_exact_duplicate`.

- Possível write: Tiny status/cadastro/código ou mapa de resolução, conforme política do `lk-stock`.
- Não autoriza: estoque/quantidade, Shopify publish, preço, compra, contato externo.
- Requer antes: escolher registro canônico por SKU/tamanho/produto com evidência.
- Readback depois: SKU exato resolve 1:1, duplicados somem do health.

### Opção C — Só packet/triagem humana

Sem writes. Usar CSV/JSON para revisão manual do LK Stock/Júlio antes de autorizar correção em lote.

## Recomendação

Começar por **Opção A em sublote de 20 missing SKUs**, porque missing tende a ser mais simples que duplicidade. Depois rodar novo health e só então atacar duplicados.

## Guardrails

- Tiny write: bloqueado até aprovação de opção/lote exato.
- Shopify write: bloqueado até aprovação separada de campo e item.
- Supabase/read model: só atualizar após fonte raiz/readback ou como cache de estado, com backup.
- Promessa de disponibilidade: proibida para estes 186 até identidade resolvida.
- values_printed: false
