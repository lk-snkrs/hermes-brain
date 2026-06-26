# Backlog audit LKGOC — próximas candidatas

Data: 2026-06-25  
Agente: `[LK] Otimização de Coleções` / LKGOC  
Escopo: auditoria read-only de backlog de coleções para priorizar próximas otimizações LKGOC.  
Writes externos: 0.  
Fontes: Brain/receipts recentes, sitemap público, Shopify Admin read-only de collections, QA público e DataForSEO keyword overview/search intent Brasil.  
Claude SEO/AEO: aplicado como checklist diagnóstico LKGOC; dados de Growth amplo/GA4/GSC/GMC não consultados.

## Histórico verificado

- Alo Yoga + Crocs McQueen já corrigidas em production/main e impact review pós-cache = PASS.
- Gold Source 204L preservado como benchmark.
- Production atual tem LKGOC/theme handles existentes para 204L, 530, 9060, 2002R, Onitsuka Mexico 66, Moon Shoe, Alo Yoga, Crocs McQueen etc.
- Não sugeri novamente superfícies recém-feitas como trabalho novo.

## Top 3 recomendadas

| Prioridade | Coleção | Keyword BR | Volume BR | Estado público | Motivo LKGOC |
|---:|---|---|---:|---|---|
| 1 | `asics-gel-nyc` | asics gel nyc | 60.500 | HTTP 200, H1 1, sem Guia, sem FAQPage, sem bloco citável | Maior demanda; intenção transacional; coleção pública muito curta/sem arquitetura LKGOC. Mesmo com 1 item, cabe Lite pós-grid no padrão Crocs. |
| 2 | `puma-speedcat` | puma speedcat | 18.100 | HTTP 200, H1 1, sem Guia, sem FAQPage, sem bloco citável | Tendência forte, storytelling fashion/motorsport e intenção informacional alta — bom para Guia LK + bloco citável. |
| 3 | `adidas-tokyo` | adidas tokyo | 9.900 | HTTP 200, H1 1, sem Guia, sem FAQPage, sem bloco citável | Crescimento anual forte, precisa capturar intenção informacional com guia pós-grid sem mexer em produto/ordem. |

## Candidatas secundárias

| Coleção | Volume BR | Sinal | Recomendação |
|---|---:|---|---|
| `asics-gel-1130` | 12.100 | já tem FAQPage bruto, mas sem Guia LK/bloco citável | Boa 4ª candidata; precisa cuidado para não duplicar FAQ/schema. |
| `adidas-taekwondo` | 6.600 | tendência mensal alta; sem Guia/FAQPage | Boa candidata de onda fashion/sneakerina, depois de Tokyo/Speedcat. |
| `lululemon-define-jacket` | 140 | volume baixo no Brasil; já tem FAQPage bruto | Não priorizar agora, salvo campanha/editorial específica. |

## QA público resumido

| Handle | HTTP | H1 | FAQPage | Guia LK | Bloco citável | Liquid error |
|---|---:|---:|---:|---:|---:|---:|
| `asics-gel-nyc` | 200 | 1 | 0 | 0 | 0 | não |
| `puma-speedcat` | 200 | 1 | 0 | 0 | 0 | não |
| `adidas-tokyo` | 200 | 1 | 0 | 0 | 0 | não |
| `asics-gel-1130` | 200 | 1 | 1 | 0 | 0 | não |
| `adidas-taekwondo` | 200 | 1 | 0 | 0 | 0 | não |
| `lululemon-define-jacket` | 200 | 1 | 1 | 0 | 0 | não |

## Recomendação operacional

Abrir **DEV preview LKGOC Lite** para `asics-gel-nyc` primeiro:

- não mexer em preço, estoque, produtos ou ordenação;
- não usar `descriptionHtml` como mecanismo final se o tema jogar conteúdo antes do grid;
- aplicar no padrão aprendido em Alo/Crocs: `sections/lk-collection.liquid` + `snippets/lk-goc-collection.liquid`, DEV/unpublished primeiro;
- QA mobile/desktop + readback público preview;
- approval packet antes de production/main.

## Próximo pacote se Lucas aprovar

`asics-gel-nyc` — LKGOC Lite pós-grid com:

1. copy curta de banner/override se necessário;
2. Guia LK pós-grid;
3. 3–4 cards de escolha;
4. FAQPage único;
5. bloco citável LK;
6. QA contra Gold Source 204L e contra caso Crocs de 1 item.

## Artefatos

- `sitemap-collections.json`
- `shopify-collections-readonly.json`
- `candidate-public-qa.json`
- `backlog-prioritized.json`
