# Impact review D+7 — AI Visibility / LKGOC Onda C1+C2

Gerado em UTC: 2026-06-26T09:31:49Z
Status: `completed_read_only`
Writes externos: `0`
Secrets impressos: `0` (`values_printed=false`)

## Escopo e janelas

Coleções publicadas em 2026-06-19: `adidas-handball-spezial`, `new-balance-204l`, `onitsuka-tiger-mexico-66`, `new-balance-1906l`, `alo-yoga-1`, `air-jordan-1-low`.

- GSC pré comparável: 2026-06-15 a 2026-06-18
- GSC pós final disponível: 2026-06-20 a 2026-06-23
- GA4/Shopify pós consultado: 2026-06-20 a 2026-06-25

Observação: D+7 ainda é janela curta; GSC tem lag e a comparação usa janela exata por URL de coleção, não atribuição ampla multi-touch.

## Veredito executivo

- **Resultado geral:** sinais iniciais **mistos com viés positivo**, não fortes o bastante para write/rollback imediato.
- **Melhores sinais:** `new-balance-204l`, `onitsuka-tiger-mexico-66` e `air-jordan-1-low` cresceram em busca/sessões e têm sinal comercial/readback.
- **Atenção:** `alo-yoga-1` caiu em GSC/GA4 na landing exata apesar de ter vendas de produtos da coleção; `adidas-handball-spezial` ainda quase não apareceu em GSC; `new-balance-1906l` teve sinal inicial de busca mas sem venda atribuída.
- **AI readback:** `agents.md` menciona 6/6 handles; `llms.txt` menciona 2/6 handles por handle/URL exato. Isso é gap de cobertura AI-citable para investigar antes de mexer.
- **Decisão recomendada:** registrar D+14 e não abrir Shopify/theme/content write agora. Se Lucas quiser uma ação intermediária, preparar apenas um packet read-only para corrigir cobertura exata do `llms.txt`.

## Resultado por coleção

### Adidas Handball Spezial — `adidas-handball-spezial`

- Veredito: `early_positive_search_weak_commerce`
- GSC clicks/impressões/CTR/posição: 0/0/0.00%/0.0 → 0/7/0.00%/10.7
- GA4 landing exata sessões/ATC/purchases/receita: 2/0/0/R$ 0.00 → 3/0/0/R$ 0.00
- Shopify produtos da coleção na janela 2026-06-15..25: 1 pedidos / 1 unidades / R$ 1499.99
- Readback público: status 200=True; canonical `https://lksneakers.com.br/collections/adidas-handball-spezial`
- AI surfaces: agents.md=True; llms.txt=False

### New Balance 204L — `new-balance-204l`

- Veredito: `early_positive_mixed`
- GSC clicks/impressões/CTR/posição: 6/1108/0.54%/7.0 → 7/2400/0.29%/9.2
- GA4 landing exata sessões/ATC/purchases/receita: 24/1/0/R$ 0.00 → 36/3/1/R$ 3599.98
- Shopify produtos da coleção na janela 2026-06-15..25: 8 pedidos / 8 unidades / R$ 22399.92
- Readback público: status 200=True; canonical `https://lksneakers.com.br/collections/new-balance-204l`
- AI surfaces: agents.md=True; llms.txt=True

### Onitsuka Tiger Mexico 66 — `onitsuka-tiger-mexico-66`

- Veredito: `early_positive`
- GSC clicks/impressões/CTR/posição: 39/2032/1.92%/3.8 → 49/2152/2.28%/3.2
- GA4 landing exata sessões/ATC/purchases/receita: 74/2/0/R$ 0.00 → 93/2/0/R$ 0.00
- Shopify produtos da coleção na janela 2026-06-15..25: 13 pedidos / 15 unidades / R$ 37799.85
- Readback público: status 200=True; canonical `https://lksneakers.com.br/collections/onitsuka-tiger-mexico-66`
- AI surfaces: agents.md=True; llms.txt=True

### New Balance 1906L — `new-balance-1906l`

- Veredito: `early_positive_search_weak_commerce`
- GSC clicks/impressões/CTR/posição: 0/75/0.00%/6.4 → 2/82/2.44%/4.8
- GA4 landing exata sessões/ATC/purchases/receita: 0/0/0/R$ 0.00 → 3/0/0/R$ 0.00
- Shopify produtos da coleção na janela 2026-06-15..25: 0 pedidos / 0 unidades / R$ 0.00
- Readback público: status 200=True; canonical `https://lksneakers.com.br/collections/new-balance-1906l`
- AI surfaces: agents.md=True; llms.txt=False

### Alo Yoga — `alo-yoga-1`

- Veredito: `commercial_positive_search_mixed`
- GSC clicks/impressões/CTR/posição: 6/1021/0.59%/9.8 → 1/576/0.17%/11.2
- GA4 landing exata sessões/ATC/purchases/receita: 18/0/0/R$ 0.00 → 11/0/0/R$ 0.00
- Shopify produtos da coleção na janela 2026-06-15..25: 13 pedidos / 15 unidades / R$ 26849.85
- Readback público: status 200=True; canonical `https://lksneakers.com.br/collections/alo-yoga-1`
- AI surfaces: agents.md=True; llms.txt=False

### Air Jordan 1 Low — `air-jordan-1-low`

- Veredito: `early_positive`
- GSC clicks/impressões/CTR/posição: 0/1697/0.00%/8.5 → 4/2345/0.17%/8.4
- GA4 landing exata sessões/ATC/purchases/receita: 2/0/0/R$ 0.00 → 11/0/0/R$ 0.00
- Shopify produtos da coleção na janela 2026-06-15..25: 2 pedidos / 3 unidades / R$ 6599.97
- Readback público: status 200=True; canonical `https://lksneakers.com.br/collections/air-jordan-1-low`
- AI surfaces: agents.md=True; llms.txt=False

## Guardrails / non-actions

- Não fiz Shopify/theme/content write.
- Não fiz GSC/GA4/Google write, Indexing API, GMC, campanha, Klaviyo, Meta, WhatsApp ou e-mail.
- Não usei estoque/preço/disponibilidade como promessa pública.
- Não imprimi secrets, service account JSON, tokens ou `.env`.

## Próximo gate

- Registrar D+14 para 2026-07-03 com a mesma bateria read-only.
- Se D+14 confirmar queda de `alo-yoga-1` ou gap de `llms.txt`, preparar approval packet específico. Não executar patch automaticamente.
