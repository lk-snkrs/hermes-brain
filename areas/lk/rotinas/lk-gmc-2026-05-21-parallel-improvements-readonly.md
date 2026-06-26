# LK GMC — melhorias paralelas read-only — 2026-05-21

Gerado em: `2026-05-21T20:55Z`
Modo: `read-only / local reports`, exceto arquivos locais no Brain.  
Writes externos executados: `0`.

## Escopo pedido

Lucas: "Fazer tudo acima paralelo" sobre próximos pontos de melhoria GMC após correções aprovadas.

Frentes executadas em paralelo:

1. Diagnóstico Packet A / Bad Bunny: fonte do preço `1799.99` vs variante `2199.99`.
2. Packet D: governança de `price_updated` / `strikethrough_price_updated`.
3. Fila dos `missing color` restantes e GTIN issues.
4. Reconciliar monitoramento recorrente GMC Review.

## 1) Packet A — diagnóstico Adidas Gazelle x Bad Bunny

### Veredito

A causa provável não é o preço das variantes Shopify dos SKUs alvo. A causa provável é a PDP expondo sinais mistos de preço.

### URLs verificadas

- `.js`: `https://lksneakers.com.br/products/tenis-adidas-gazelle-x-bad-bunny-core-white-bege.js`
- IF9737: `https://lksneakers.com.br/products/tenis-adidas-gazelle-x-bad-bunny-core-white-bege?currency=BRL&country=BR&variant=45906859589854&utm_source=google&utm_medium=cpc&utm_campaign=Google%20Shopping&stkn=789476af598e`
- IF9735-9: `https://lksneakers.com.br/products/tenis-adidas-gazelle-x-bad-bunny-core-white-bege?currency=BRL&country=BR&variant=45906859524318&utm_source=google&utm_medium=cpc&utm_campaign=Google%20Shopping&stkn=789476af598e`

### Evidência

- `.js` público confirma `2199.99 BRL` nos dois SKUs alvo:
  - `IF9735-9`, variant `45906859524318`, price `219999`, available `true`.
  - `IF9737`, variant `45906859589854`, price `219999`, available `true`.
- HTML das landings com `variant` correto ainda contém sinais fortes em `1799.99`:
  - `<title>`: `... por R$ 1.799,99 ...`
  - `var productPrice = 1799.99;`
  - preço principal visível: `<span class="pi-price">R$ 1.799,99</span>`
  - campos `Price: "R$ 1.799,99"` / `Value: "1.799,99"`
- O HTML também contém sinais corretos para a variante selecionada:
  - `active_sku_var`: `IF9737` ou `IF9735-9`
  - `hidden_variant_id`: correto
  - sticky price: `R$ 2.199,99`
  - eventos/variant JSON: `2199.99`
- JSON-LD Offer está correto para os SKUs alvo (`2199.99`), mas o Product multi-offer também contém outras variantes a `1799.99`.

### Próxima ação proposta

Corrigir storefront/theme/app para que, quando a URL tiver `?variant=...`, todos os sinais primários reflitam a variante selecionada ou parem de publicar preço global/min-price:

- `<title>` sem preço ou preço da variante correta.
- `.pi-price` = preço da variante selecionada.
- `var productPrice` = preço da variante selecionada.
- campos `Price`/`Value` = preço da variante selecionada.
- manter JSON-LD Offer por SKU correto.

Requer aprovação antes de qualquer Shopify/theme/app write.

## 2) Packet D — price governance preview

Arquivo gerado:

- `reports/lk-gmc-2026-05-21-packet-d-price-governance-preview.md`
- `reports/lk-gmc-2026-05-21-packet-d-price-governance-preview.csv`
- `reports/lk-gmc-2026-05-21-packet-d-price-governance-preview.json`

### Resumo

- Products lidos: `19652`
- Productstatuses lidos: `19633`
- Candidatos únicos Packet D: `512`
- `price_updated`: `1440` instâncias / `480` produtos
- `strikethrough_price_updated`: `863` instâncias / `289` produtos

### Classificação

- Preço final divergente: `19`
- SalePrice divergente: `31`
- Compare_at/strikethrough divergente: `1`
- False-positive/lag: `461`

### Micro-piloto top 10 proposto — somente se aprovado

1. `online:pt:BR:01424-002-2` — preço final divergente — feed `5999.90`, público `8999.99`.
2. `online:pt:BR:553558030-6` — salePrice divergente — feed price/sale `2399.99`/`2299.99`, público `2999.99`, compare_at `2399.99`.
3. `online:pt:BR:FD8776800-8` — compare_at/strikethrough — feed `3499.99`, público `4799.99`, compare_at `6999.99`.
4. `online:pt:BR:B75571-3` — preço final divergente — feed `3499.99`, público `6499.99`.
5. `online:pt:BR:B75571-5` — preço final divergente — feed `3499.99`, público `4799.99`.
6. `online:pt:BR:CJ5378700-36` — preço final divergente — feed `5499.99`, público `6099.99`.
7. `online:pt:BR:DC6991200-4` — preço final divergente — feed `2499.99`, público `2999.99`.
8. `online:pt:BR:DC6991200-44` — preço final divergente — feed `2499.99`, público `2999.99`.
9. `online:pt:BR:DD9335641-7` — preço final divergente — feed `2999.90`, público `2999.99`.
10. `online:pt:BR:DQ4040400-44` — preço final divergente — feed `2999.90`, público `2999.99`.

Observação: não recomendo bulk. Qualquer micro-piloto deve ter snapshot, rollback e readback.

## 3) Missing color restantes

Arquivos gerados:

- `reports/missing-color-review-queue-2026-05-21.md`
- `reports/missing-color-review-queue-2026-05-21.csv`

### Resumo

- Total original: `279`
- High-confidence já aplicado: `181`
- Fila pendente: `98`
  - `medium`: `50`
  - `needs_human_review`: `23`
  - `none/no_color_inferred`: `25`

### Próxima ação proposta

Revisão humana/semiautomática antes de qualquer ProductInput/supplemental feed:

- `medium`: revisar evidência de título/handle/imagem.
- `needs_human_review`: só aplicar com confirmação.
- `none`: não aplicar sem inspeção de PDP/imagem/título.

## 4) GTIN restricted/reserved

Arquivos gerados:

- `reports/gtin-review-queue-2026-05-21.md`
- `reports/gtin-review-queue-2026-05-21.csv`

### Resumo

- Produtos na fila: `12`
- `restricted_gtin`: `10` produtos
- `reserved_gtin`: `2` produtos
- Conferência bate com weekly review: `restricted_gtin` 15 instâncias / 10 produtos; `reserved_gtin` 3 instâncias / 2 produtos.

### Próxima ação proposta

Não inventar GTIN. Validar contra fonte oficial/fornecedor. Se não houver GTIN confiável, preparar approval packet para remover/ajustar identificador conforme política GMC, não para substituir por número sem fonte.

## 5) Cron / monitoramento GMC Review

Cron encontrado no runtime atual:

- Job: `d4c26da4cd48`
- Nome: `LK GMC Review read-only mandatory delivery`
- Schedule: quinta 09:00 BRT (`0 12 * * 4` UTC)
- Estado: `paused`
- Script: `lk_gmc_review_watchdog.py`

### Veredito

Monitoramento recorrente de GMC está documentado, mas pausado no perfil principal. Pela regra de Growth OS, a execução operacional deve idealmente ficar no perfil `lk-growth`, com Hermes principal apenas para Brain/governance/handoff.

### Próxima ação proposta

Não reativei nem migrei automaticamente para evitar duplicidade entre perfis. Próximo passo seguro:

1. Recriar/reativar o GMC Review no perfil `lk-growth`.
2. Manter o job `d4c26da4cd48` pausado no Hermes principal ou documentá-lo como legado.
3. Registrar de/para no Brain.
4. Entregar no canal aprovado do LK Growth; Hermes principal recebe só decisões/exceções.

## O que não foi feito

- Nenhum Shopify write.
- Nenhum theme/app write.
- Nenhum Content API write.
- Nenhum ProductInput PATCH.
- Nenhum supplemental feed upload/fetchNow.
- Nenhum preço/estoque/desconto alterado.
- Nenhum cron alterado/reativado/migrado.
- Nenhuma campanha/envio externo.

## Decisões pendentes para Lucas

1. Aprovar ou não correção Shopify/theme/app para Packet A.
2. Aprovar ou não micro-piloto Packet D top 10 com snapshot/rollback.
3. Indicar se a revisão dos 98 colors pendentes será feita por LK/time humano ou se devo preparar um pacote visual de revisão.
4. Aprovar ou não preparação de packet GTIN com fontes verificáveis.
5. Confirmar se o GMC Review deve ser reativado/migrado no `lk-growth` agora.
