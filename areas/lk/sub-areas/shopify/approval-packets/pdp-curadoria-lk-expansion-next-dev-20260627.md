# Approval packet — PDP Curadoria LK expansion — próxima rodada DEV

- Data/hora: 2026-06-27
- Agente/profile: lk-shopify
- Superfície: PDP `.lk-variante` / Curadoria LK
- Status: preparado; sem write em Shopify/tema executado
- Pedido: Lucas perguntou se vamos continuar as melhorias e citou o aumento da Curadoria LK.
- Writes externos: 0
- Consulta direta de estoque: 0
- values_printed=false

## Histórico verificado

- `areas/lk/sub-areas/shopify/reports/curadoria-ald-hats-saint-george-dev-20260626.md`
- `areas/lk/sub-areas/shopify/reports/pdp-product-suggestions-v3-ald-hats-family-source-20260627.md`
- `areas/lk/sub-areas/shopify/prd/curadoria-lk-pdp-maintenance-system-20260607.md`
- Product Suggestions v3 Production já publicado via PR #111; isso é camada separada do aumento da Curadoria LK.

## Interpretação

Temos duas frentes diferentes:

1. **Product Suggestions v3** — bloco inferior `Você também pode gostar`, já em Production.
2. **Curadoria LK** — bloco editorial `.lk-variante` / `Curadoria LK`, que deve ser aumentado e mantido como camada premium de família/variação.

O aumento da Curadoria LK não deve ser feito no escuro e não deve puxar estoque direto. Deve seguir:

```text
read-only audit → candidate packet → DEV aprovado → QA → Production aprovado → readback/receipt
```

## Estado atual — ALD hats / Saint George

Bloco atual documentado:

- snippet: `snippets/lk-variante-ald-hats-saint-george-20260626.liquid`
- render: `data-lk-variante="ald-hats-saint-george-20260626"`
- atual: 6 handles no grupo; renderiza 5 cards porque exclui o produto atual.

Curadoria atual do PDP Saint George:

1. `bone-aime-leon-dore-saint-george-logo-hat-bege-verde`
2. `bone-aime-leon-dore-micro-logo-hat-bege-verde`
3. `bone-aime-leon-dore-porsche-nylon-logo-jet-black-preto`
4. `bone-aime-leon-dore-unisphere-verde`
5. `bone-aime-leon-dore-washed-script-plaza-taupe-bege`

Fonte read-only adicional já encontrada para ALD hats:

| handle | status |
|---|---|
| `bone-aime-leon-dore-unisphere-preto` | público HTTP 200 |
| `bone-6-panel-aime-leon-dore-cycling-logo-azul` | público HTTP 200 |
| `bone-5-panel-aime-leon-dore-unisphere-azul` | público HTTP 200 |
| `bone-5-panel-aime-leon-dore-unisphere-branco` | público HTTP 200 |
| `bone-aime-leon-dore-washed-script-jet-black-preto` | público HTTP 200 |
| `bone-aime-leon-micro-logo-hat-jet-black-preto` | público HTTP 200 |
| `bone-aime-leon-dore-x-porsche-colorblock-logo-pristine-off-white` | público HTTP 200 |

## Proposta DEV — rodada 1

Escopo DEV proposto:

1. Manter a Curadoria LK com limite de render de até 5 cards.
2. Usar os candidatos adicionais acima apenas como pool de substituição/backup editorial, não para aumentar o número visível de cards.
3. Manter exclusão do produto atual.
4. Manter labels curtos.
5. Manter imagens válidas.
6. Não consultar/prometer estoque.
7. Não mexer no Product Suggestions v3, Trust Bar, Google Reviews, preço, produto, checkout ou metafields.

## QA DEV obrigatório

PDP alvo:

- `https://lksneakers.com.br/products/bone-aime-leon-dore-saint-george-logo-hat-bege-marrom?preview_theme_id=155065450718`

Gates:

- HTTP `200`.
- Liquid errors `0`.
- `.lk-variante` presente.
- `Curadoria LK` presente.
- produto atual não aparece no próprio bloco.
- mínimo 4 e máximo 5 cards visíveis no bloco, conforme qualidade do pool editorial.
- todos os links `/products/...` retornam HTTP `200`.
- mobile não quebra o rail.
- Production não alterado.

## Risco

| Risco | Nível | Mitigação |
|---|---:|---|
| Bloco ficar longo demais no mobile | Médio | limitar a 8 cards e QA mobile |
| Duplicar produto atual | Baixo | exclusão por `product.handle` |
| Misturar apparel/sneaker | Baixo | somente handles `bone-...` ALD |
| Prometer disponibilidade | Alto | sem estoque/disponibilidade; eligibility fica fora do texto |

## Rollback DEV

Restaurar snippet/section anteriores a partir dos backups do workdir da execução DEV.

## Fora de escopo

- Sem Production merge.
- Sem Shopify product/metafield/preço/estoque.
- Sem Tiny.
- Sem GMC/Klaviyo/ads/WhatsApp/email.
- Sem mudança no Product Suggestions v3.

## Aprovação necessária para aplicar em DEV

> Aprovo DEV manutenção da Curadoria LK ALD hats no PDP Saint George com até 5 cards visíveis, usando candidatos extras apenas como pool editorial/backup, sem Production merge.

## Próxima frente depois da rodada 1

Após validar ALD hats, rodar o audit batch de Curadoria LK para mais famílias/PDPs:

- classificar gaps verdadeiros;
- separar source/public divergence;
- excluir itens de superfície errada;
- gerar batch DEV pequeno e aprovado, não “100 produtos às cegas”.

## Reminder OS

- loop needed: yes
- owner: lk-shopify
- next action: aguardar aprovação DEV ou ajustar pool/ordem dos 5 cards
- review trigger: resposta de Lucas aprovando DEV ou pedindo outra família primeiro
- evidence: este approval packet + reports citados acima
