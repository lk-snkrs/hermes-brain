# Receipt — Onitsuka FAQ/schema consolidation

Data: 2026-05-28
Tema: Shopify production `155065417950`
Asset alterado: `sections/lk-collection.liquid`
URL: `https://lksneakers.com.br/collections/onitsuka-tiger-mexico-66`

## Objetivo
Consolidar a coleção Onitsuka Tiger Mexico 66 para usar apenas o FAQ canônico dentro do Guia LK e apenas um `FAQPage` JSON-LD na página.

## Patch aplicado
Foi adicionado um guardrail Liquid escopado para `collection.handle == 'onitsuka-tiger-mexico-66'` antes do bloco legado de enrichment, para suprimir o `.coll-faq` legado e o segundo `FAQPage` gerado por `lk_faq_override`.

```liquid
{%- comment -%} Onitsuka uses the canonical FAQ inside lk-guide-standard-panel; suppress legacy coll-faq + duplicate FAQPage JSON-LD. {%- endcomment -%}
{%- if collection.handle == 'onitsuka-tiger-mexico-66' -%}
  {%- assign lk_faq_override = false -%}
  {%- assign has_faq = false -%}
{%- endif -%}
{%- if lk_faq_override -%}{%- assign has_faq = true -%}{%- endif -%}
```

## Backups / rollback
Arquivos neste diretório:

- `sections__lk-collection.before.liquid` — backup antes do patch.
- `sections__lk-collection.after.liquid` — versão pretendida após patch.
- `sections__lk-collection.current-readback.liquid` — readback Admin final.
- `validation-final.json` — validação final.

Rollback: restaurar `sections__lk-collection.before.liquid` no asset `sections/lk-collection.liquid` do tema production `155065417950`.

## Validação Admin
- Patch presente no readback Admin: sim.
- SHA256 readback final: `58f4dda12e9145c303b634cdf3a9cb7517044637eb1c5cb57abaa0ce0ef6ba3a`.

## Validação storefront via Chromium
Resultado renderizado:

- `FAQPage` JSON-LD: `1`.
- `.coll-faq` no DOM renderizado: `0`.
- `.lk-guide-standard-faq` no DOM renderizado: `1`.
- Title: `Onitsuka Tiger Mexico 66 Original na LK Sneakers`.

FAQPage único contém as perguntas do Guia LK:

1. Quanto custa um Onitsuka Tiger no Brasil?
2. Qual a diferença entre ASICS e Onitsuka Tiger?
3. O Onitsuka Tiger Mexico 66 é da ASICS?
4. Como escolher entre Mexico 66, SD, Sabot e Slip-on?
5. O Mexico 66 tem a forma grande ou pequena?

## Observação de cache
Checks públicos por `urllib/curl` alternaram por alguns minutos entre variantes antigas do CDN Shopify, ainda mostrando 2 FAQPage. A validação renderizada em Chromium já refletiu o Liquid atualizado com 1 FAQPage e sem `.coll-faq`. Se necessário, revalidar novamente após cache assentar.
