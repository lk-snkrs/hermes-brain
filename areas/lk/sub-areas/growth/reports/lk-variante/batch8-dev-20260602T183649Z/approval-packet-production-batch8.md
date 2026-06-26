# Curadoria LK — Batch 8 Dev apply receipt / approval packet Production

## Aprovação Dev

Lucas aprovou via botão inline: `Pode aplicar no Dev o Batch 8`.

## Status

Batch 8 aplicado apenas no Dev theme.

- Dev theme ID: `155065450718`
- Production theme ID: `155065417950`
- Asset: `snippets/lk-variante-top30-visited.liquid`
- Dev readback: match
- Production unchanged: true
- SHA Dev readback final: `d6b35f73b048`

## Grupos no Batch 8 Dev

1. New Balance 204L regular
   - Marker: `top30-new-balance-204l-regular`
   - Produtos finais: 8
   - Handles públicos e disponíveis: 8/8

2. Onitsuka Mexico 66 Sabot regular
   - Marker: `top30-onitsuka-mexico-66-sabot-regular`
   - Produtos finais: 8
   - Handles públicos e disponíveis: 8/8

3. Adidas Taekwondo Mei Ballet regular
   - Marker: `top30-adidas-taekwondo-regular`
   - Produtos finais: 7
   - Handles públicos e disponíveis: 7/7

4. Nike Cortez regular
   - Marker: `top30-nike-cortez-regular`
   - Produtos finais: 8
   - Handles públicos e disponíveis: 8/8

5. Alo Airlift line
   - Marker: `top30-alo-airlift-line`
   - Produtos finais: 7
   - Handles públicos e disponíveis: 7/7
   - Correção: removido `short-alo-yoga-5-airlift-energy` porque `/products/{handle}.js` retornou `available=false`.

## QA Dev final

Arquivos:

- `dev-upload-readback-report.json`
- `dev-reupload-available-only-report.json`
- `dev-final-qa-batch8.json`
- `dev_before_batch8.liquid`
- `prod_before_batch8.liquid`
- `dev_readback_batch8_available_only.liquid`

Resultado: pass

- Markers no Dev: 5/5, exatamente 1 ocorrência cada
- Cada grupo tem `handles_count > 5`
- Simulação de cada PDP: 5 cards
- Produto atual excluído
- Todos os handles selecionados retornam `/products/{handle}.js` com HTTP 200
- Todos os handles selecionados estão `available=true`
- URLs de imagem: Shopify CDN válidas
- Malformed URL count: 0
- Literais `Liquid error` / `Liquid syntax error`: 0
- Production unchanged: true

## Risco

- Baixo/médio: mudança de tema em Dev; se promovida para Production, afeta visual/CRO de PDPs desses grupos.
- Alo Airlift é apparel e segue a exceção LK de linha/look coerente.
- Nike Cortez entrou por cobertura semântica, não por sinal recente de venda.

## Rollback Dev

Rollback do Dev: re-upar `dev_before_batch8.liquid` para `snippets/lk-variante-top30-visited.liquid` no Dev theme.

## Próxima decisão

Se aprovado, executar promoção Dev→Production do mesmo asset Dev final do Batch 8:

`Aprovado subir Batch 8 Curadoria LK para Production`

Escopo da aprovação: somente `snippets/lk-variante-top30-visited.liquid` no Production theme. Sem produto, preço, estoque, checkout, apps, GMC/feed, Klaviyo/Meta/Tiny ou campanha.
