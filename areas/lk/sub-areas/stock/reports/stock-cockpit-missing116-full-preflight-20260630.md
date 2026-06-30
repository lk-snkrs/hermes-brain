# Missing116 full preflight consolidated — 2026-06-30

- generated_at_utc: `2026-06-30T14:11:45.940141+00:00`
- Pedido/aprovação: Lucas aprovou A20/seguir para corrigir problemas possíveis.
- Escopo: Shopify Admin read-only via CLI oficial + Tiny read-only via `lk-tiny` broker.
- values_printed: false
- writes_executed: 0

## Resultado executivo

Nenhum dos 116 `Tiny exact missing` tem correção automática determinística segura neste momento.

## Gate Shopify

| Resultado | Qtde |
|---|---:|
| Shopify SKU único encontrado | 98 |
| Shopify SKU duplicado | 18 |

## Preflight Tiny nos 98 com Shopify SKU único

| Resultado | Qtde |
|---|---:|
| Ambíguo / sem candidato seguro | 91 |
| Sem match Tiny por tamanho | 7 |
| Candidato seguro para write de `codigo` | 0 |

## Conclusão

- **Correções executáveis agora:** 0.
- **Tiny write:** 0.
- **Shopify write:** 0.
- **Supabase write:** 0.
- **Motivo:** falta match 1:1 confiável entre Shopify variant SKU/tamanho e Tiny product/variation sem `codigo`; ou há duplicidade de SKU no Shopify/Tiny.

## Próximo passo seguro

1. Criar triagem humana/`lk-stock` dos 116 missing com foco em mapeamento variante → Tiny.
2. Resolver primeiro os 18 Shopify SKU duplicados, porque duplicidade no próprio Shopify invalida o target de correção Tiny.
3. Só depois autorizar qualquer `produto.alterar`/cadastro, idealmente via wrapper governado novo para Tiny cadastro, não script raw.
