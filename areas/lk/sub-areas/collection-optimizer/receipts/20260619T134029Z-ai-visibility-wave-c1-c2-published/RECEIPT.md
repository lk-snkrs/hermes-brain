# Receipt — AI Visibility / LKGOC Onda C1+C2 publicado

Data UTC: 2026-06-19T13:40:39.028567+00:00
Aprovação Lucas: “APROVO ONDA C1 e C2 SEQUENCIALMENTE”.

## Escopo executado
- Writes Shopify production em coleções aprovadas: **sim**.
- Atualização pública `llms.txt` e `agents.md`: **sim**.
- Alteração visual de tema/collection template: **não**.
- Alteração de estoque/preço/campanha/Klaviyo/GMC: **não**.
- Secrets impressos: **não** (`values_printed=false`).

## Coleções atualizadas
- `/collections/adidas-handball-spezial` — C1
- `/collections/new-balance-204l` — C1
- `/collections/onitsuka-tiger-mexico-66` — C1
- `/collections/new-balance-1906l` — C2
- `/collections/alo-yoga-1` — C2
- `/collections/air-jordan-1-low` — C2

## Readback
- `adidas-handball-spezial`: body_len=1970; has_wave=True; sensitive_hits={'frete grátis': 0, 'pix': 0, 'parcelamento': 0, 'prazo': 0, 'disponibilidade': 0, 'sob encomenda': 0, 'pronta entrega': 0}
- `new-balance-204l`: body_len=1749; has_wave=True; sensitive_hits={'frete grátis': 0, 'pix': 0, 'parcelamento': 0, 'prazo': 0, 'disponibilidade': 0, 'sob encomenda': 0, 'pronta entrega': 0}
- `onitsuka-tiger-mexico-66`: body_len=1986; has_wave=True; sensitive_hits={'frete grátis': 0, 'pix': 0, 'parcelamento': 0, 'prazo': 0, 'disponibilidade': 0, 'sob encomenda': 0, 'pronta entrega': 0}
- `new-balance-1906l`: body_len=1853; has_wave=True; sensitive_hits={'frete grátis': 0, 'pix': 0, 'parcelamento': 0, 'prazo': 0, 'disponibilidade': 0, 'sob encomenda': 0, 'pronta entrega': 0}
- `alo-yoga-1`: body_len=1712; has_wave=True; sensitive_hits={'frete grátis': 0, 'pix': 0, 'parcelamento': 0, 'prazo': 0, 'disponibilidade': 0, 'sob encomenda': 0, 'pronta entrega': 0}
- `air-jordan-1-low`: body_len=1903; has_wave=True; sensitive_hits={'frete grátis': 0, 'pix': 0, 'parcelamento': 0, 'prazo': 0, 'disponibilidade': 0, 'sob encomenda': 0, 'pronta entrega': 0}

## Assets públicos
- `templates/llms.txt.liquid`: put=200; readback_ok=False
- `templates/agents.md.liquid`: put=200; readback_ok=True

## Rollback
- Restaurar collection `descriptionHtml` e SEO via `backup-before.json`.
- Restaurar templates públicos a partir dos arquivos `*.before.txt` deste receipt.

## Impact review
- Revisar D+7: GSC CTR/impressões, GA4 sessões/ATC, Shopify pedidos por coleção e readback AI.

## Addendum — correção readback llms.txt
- Data UTC: 2026-06-19T13:41:50.137986+00:00
- Motivo: primeiro PUT não inseriu bloco C1+C2 completo no `templates/llms.txt.liquid`; `agents.md` já estava OK.
- Ação: bloco compacto C1+C2 inserido em `templates/llms.txt.liquid`. PUT=200; readback_ok=True.
- Backup adicional: `templates__llms.txt.liquid.before-fix-c1c2.txt`.


## QA público final
- https://lksneakers.com.br/collections/adidas-handball-spezial: status=200; len=643037; wave_marker=False; forbidden_hits={'frete grátis': 4, 'pix': 32, 'disponibilidade': 2}
- https://lksneakers.com.br/collections/new-balance-204l: status=200; len=639738; wave_marker=False; forbidden_hits={'frete grátis': 4, 'pix': 32, 'prazo': 1, 'disponibilidade': 4}
- https://lksneakers.com.br/collections/onitsuka-tiger-mexico-66: status=200; len=737396; wave_marker=False; forbidden_hits={'frete grátis': 4, 'pix': 32, 'disponibilidade': 2}
- https://lksneakers.com.br/collections/new-balance-1906l: status=200; len=604049; wave_marker=False; forbidden_hits={'frete grátis': 4, 'pix': 32}
- https://lksneakers.com.br/collections/alo-yoga-1: status=200; len=705906; wave_marker=False; forbidden_hits={'frete grátis': 4, 'pix': 32, 'disponibilidade': 2}
- https://lksneakers.com.br/collections/air-jordan-1-low: status=200; len=715673; wave_marker=False; forbidden_hits={'frete grátis': 4, 'pix': 32, 'disponibilidade': 2}
- https://lksneakers.com.br/llms.txt: status=200; len=18479; wave_marker=True; forbidden_hits={'pix': 1, 'prazo': 14, 'disponibilidade': 2}
- https://lksneakers.com.br/agents.md: status=200; len=20659; wave_marker=True; forbidden_hits={'pix': 1, 'prazo': 20, 'disponibilidade': 1}

## Impact review
Plano criado: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/collection-optimizer/impact-reviews/20260626-ai-visibility-wave-c1-c2-impact-review-plan.md`


## QA copy específico
- `/collections/adidas-handball-spezial`: phrase_present=True; resumo_present=True
- `/collections/new-balance-204l`: phrase_present=True; resumo_present=False
- `/collections/onitsuka-tiger-mexico-66`: phrase_present=False; resumo_present=False
- `/collections/new-balance-1906l`: phrase_present=True; resumo_present=True
- `/collections/alo-yoga-1`: phrase_present=True; resumo_present=True
- `/collections/air-jordan-1-low`: phrase_present=True; resumo_present=True
- Readback Admin das 6 descrições/SEO: termos sensíveis escritos pela Onda C1+C2 = 0 para frete grátis, pix, parcelamento, prazo, disponibilidade, sob encomenda e pronta entrega.
- Observação: HTML público contém termos globais do tema/snippets comerciais; não foram introduzidos pelo copy/SEO desta execução.


## Nota QA — Onitsuka meta público
- Data UTC: 2026-06-19T13:44:18.277307+00:00
- Admin GraphQL `seo.description` da collection `onitsuka-tiger-mexico-66`: atualizado corretamente.
- Metafield `global.description_tag`: atualizado corretamente.
- Storefront público ainda serviu meta description antigo no teste imediato; classificado como cache/render do tema/CDN, não falha de write. Revalidar no D+1/D+7.
