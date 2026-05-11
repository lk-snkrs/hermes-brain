# LK P0 — fila dos 6 bloqueados restantes pós-correção Tiny — 2026-05-11

## Contexto

Após os 2 primeiros writes Tiny e os 7 writes aprovados seguintes, restaram 6 P0 bloqueados. Rodei recheck live read-only contra Shopify e Tiny para transformar o bloqueio em fila de decisão/cadastro.

## Resultado

- Total rechecado: 6
- needs_canonical_code_decision_shopify_and_tiny_blank: 5
- ambiguous_tiny_duplicate_with_shopify_sku: 1
- Candidatos seguros para write automático agora: 0
- Shopify writes: 0
- Tiny writes: 0
- Sourcing/contato fornecedor/campanha: 0

## Fila acionável

### Camiseta Pace Cotton Code Branca — G/L
- Shopify variant: `47512247599326`
- Shopify SKU live: `[sem SKU]`
- Classificação: `needs_canonical_code_decision_shopify_and_tiny_blank`
- Tiny matches: `1065543106 | 1069541599`
- Tiny parents: `1065543095 | 1065543095`
- Tiny códigos atuais: `[sem codigo] | [sem codigo]`
- Próximo passo: Definir código canônico/SKU do item e escolher Tiny ID correto; depois criar preview de preenchimento Tiny codigo e Shopify SKU.
- Limite de aprovação: Sem write automático: falta SKU Shopify e/ou Tiny codigo canônico.

### Camiseta Aimé Leon Dore Musician Graphic Off White — S/P
- Shopify variant: `47579297939678`
- Shopify SKU live: `[sem SKU]`
- Classificação: `needs_canonical_code_decision_shopify_and_tiny_blank`
- Tiny matches: `1066011682 | 1069541741 | 1066011725 | 1069541726`
- Tiny parents: `1066011677 | 1066011677 | 1066011720 | 1066011720`
- Tiny códigos atuais: `[sem codigo] | [sem codigo] | [sem codigo] | [sem codigo]`
- Próximo passo: Definir código canônico/SKU do item e escolher Tiny ID correto; depois criar preview de preenchimento Tiny codigo e Shopify SKU.
- Limite de aprovação: Sem write automático: falta SKU Shopify e/ou Tiny codigo canônico.

### Rhode Pocket Blush — Sleepy Girl - Soft Mauve
- Shopify variant: `46838740648158`
- Shopify SKU live: `[sem SKU]`
- Classificação: `needs_canonical_code_decision_shopify_and_tiny_blank`
- Tiny matches: `1070288342`
- Tiny parents: `1070288304`
- Tiny códigos atuais: `[sem codigo]`
- Próximo passo: Definir código canônico/SKU do item e escolher Tiny ID correto; depois criar preview de preenchimento Tiny codigo e Shopify SKU.
- Limite de aprovação: Sem write automático: falta SKU Shopify e/ou Tiny codigo canônico.

### Camiseta Pace Cotton Code Preta — G/L
- Shopify variant: `47512247730398`
- Shopify SKU live: `[sem SKU]`
- Classificação: `needs_canonical_code_decision_shopify_and_tiny_blank`
- Tiny matches: `1065543087 | 1069541614`
- Tiny parents: `1065543076 | 1065543076`
- Tiny códigos atuais: `[sem codigo] | [sem codigo]`
- Próximo passo: Definir código canônico/SKU do item e escolher Tiny ID correto; depois criar preview de preenchimento Tiny codigo e Shopify SKU.
- Limite de aprovação: Sem write automático: falta SKU Shopify e/ou Tiny codigo canônico.

### Camiseta Pace Sketch Yourself Off White — P/S
- Shopify variant: `47019131568350`
- Shopify SKU live: `[sem SKU]`
- Classificação: `needs_canonical_code_decision_shopify_and_tiny_blank`
- Tiny matches: `1063954611 | 1069539379`
- Tiny parents: `1063954607 | 1063954607`
- Tiny códigos atuais: `[sem codigo] | [sem codigo]`
- Próximo passo: Definir código canônico/SKU do item e escolher Tiny ID correto; depois criar preview de preenchimento Tiny codigo e Shopify SKU.
- Limite de aprovação: Sem write automático: falta SKU Shopify e/ou Tiny codigo canônico.

### Camiseta Pace Patavision Off White — P/S
- Shopify variant: `47019093295326`
- Shopify SKU live: `PAC-5857246-S`
- Classificação: `ambiguous_tiny_duplicate_with_shopify_sku`
- Tiny matches: `1063951385 | 1069539349`
- Tiny parents: `1063951381 | 1063951381`
- Tiny códigos atuais: `[sem codigo] | [sem codigo]`
- Próximo passo: Lucas/Júlio escolher qual Tiny ID duplicado é o item real; depois aprovar preencher Tiny codigo com SKU Shopify live e revalidar Shopify.
- Limite de aprovação: Tiny codigo write só após escolha do Tiny ID; Shopify write separado se necessário.

## Próxima decisão necessária

Para os 5 sem SKU Shopify/Tiny codigo, Lucas/Júlio precisa definir o código canônico e qual Tiny ID fica como registro real quando houver duplicidade. Para Patavision, já existe SKU Shopify (`PAC-5857246-S`), mas há dois matches Tiny P/S sem código; precisa escolher o Tiny ID correto antes de preencher.

## Artefatos

- `reports/lk-p0-blocked-six-live-recheck-2026-05-11.json`
- `reports/lk-p0-blocked-six-correction-queue-2026-05-11.json`
- `reports/lk-p0-blocked-six-correction-queue-2026-05-11.csv`
- `scripts/lk_p0_blocked_six_live_recheck_20260511.py`
