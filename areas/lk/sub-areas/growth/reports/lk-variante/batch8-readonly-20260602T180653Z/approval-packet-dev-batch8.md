# Curadoria LK — Batch 8 read-only candidate packet / aprovação para Dev

## Status

Pacote montado em modo read-only. Nenhum upload de tema foi executado.

## Fontes lidas

- Shopify Theme Asset API GET — Production `snippets/lk-variante-top30-visited.liquid`.
- Shopify Products API GET — catálogo ativo/publicado.
- Shopify Orders API GET — janela de 180 dias, pedidos paid-like e não cancelados, sem PII no relatório.
- Storefront público `/products/{handle}.js` — disponibilidade pública dos handles selecionados.

## Batch 8 recomendado para Dev

1. New Balance 204L regular
   - Marker proposto: `top30-new-balance-204l-regular`
   - Produtos: 8
   - Sinal 180d nos selecionados: 231 unidades / 219 pedidos
   - Observação: grupo distinto de 1906L/530/9060 já publicados.

2. Onitsuka Mexico 66 Sabot regular
   - Marker proposto: `top30-onitsuka-mexico-66-sabot-regular`
   - Produtos: 8
   - Sinal 180d nos selecionados: 111 unidades / 105 pedidos
   - Observação: separado do Mexico 66 regular por tipo/silhueta Sabot.

3. Adidas Taekwondo Mei Ballet regular
   - Marker proposto: `top30-adidas-taekwondo-regular`
   - Produtos: 7
   - Sinal 180d nos selecionados: 10 unidades / 10 pedidos
   - Limpeza: item com handle/título inconsistente envolvendo Onitsuka foi removido.

4. Nike Cortez regular
   - Marker proposto: `top30-nike-cortez-regular`
   - Produtos: 8
   - Sinal 180d nos selecionados: 0 unidades / 0 pedidos nos 180d lidos
   - Motivo: grupo semântico limpo e público, expansão de cobertura.

5. Alo Airlift line
   - Marker proposto: `top30-alo-airlift-line`
   - Produtos: 8
   - Sinal 180d nos selecionados: 0 unidades / 0 pedidos nos 180d lidos
   - Observação: apparel segue regra LK de linha/look coerente; não usa restrição sneaker de mesma silhueta.

## Bloqueados / removidos na limpeza

- Adidas Spezial regular: removido porque duplicava Handball Spezial já publicado e trazia ruído não-sneaker/collab.
- Nike Zoom Vomero 5 regular: removido porque, após excluir Doernbecher/Premium, restaram só 3 produtos públicos limpos — insuficiente para 5 cards.
- Item Taekwondo cross-brand/handle inconsistente: removido do grupo.
- Yeezy Slide continua bloqueado pela regra de 5 alternativas, salvo se o catálogo ganhar mais produtos públicos seguros.

## QA read-only/local

Arquivos:

- `batch8-candidates-readonly.json`
- `batch8-expanded-discovery.json`
- `batch8-apparel-and-other-discovery.json`
- `batch8-refined-replacement-discovery.json`
- `batch8-selected-final.json`
- `batch8-proposed-append.liquid`
- `batch8-proposed-static-qa.json`

Resultado:

- Cada grupo selecionado tem `handles_count > 5`.
- Simulação: cada current renderiza 5 cards.
- Produto atual nunca aparece nos próprios cards.
- Imagens: URLs Shopify CDN válidas.
- Malformed URL count: 0.
- Aspas/backslash problemáticas: 0.
- Balanceamento básico Liquid:
  - `for/endfor`: 10/10
  - `if/endif`: 15/15
- Sem upload Dev/Production nesta etapa.

## Risco

- Baixo/médio se aprovado para Dev: alteração de tema no Dev, sem afetar Production.
- Nike Cortez e Alo Airlift entraram por cobertura semântica/linha, não por sinal recente de vendas nos 180d lidos.
- Apparel Alo Airlift mistura peças da mesma linha/look, seguindo a exceção aprovada para apparel.

## Rollback planejado para Dev

Antes de qualquer upload no Dev, snapshot do asset Dev atual e do Production atual. Rollback do Dev = re-upar o snapshot `dev_before_batch8.liquid`.

## Não-ações

Não foi alterado:

- Dev theme
- Production theme
- Produtos
- Preço
- Estoque
- Checkout
- Apps
- GMC/feed
- Klaviyo
- Meta
- Tiny
- Campanhas/envios

## Próxima decisão

Para aplicar esse pacote no Dev theme, Lucas precisa aprovar explicitamente:

`Pode aplicar no dev o Batch 8 da Curadoria LK com New Balance 204L, Onitsuka Mexico 66 Sabot, Adidas Taekwondo, Nike Cortez e Alo Airlift, sem mexer em Production/produtos/preço/estoque/apps.`
