# LK Stock → LK Content — Apparel best sellers com estoque confirmado para newsletter

Criado: 2026-06-21 20:42 BRT / 2026-06-21T23:42:35Z  
Origem do pedido: `areas/lk/sub-areas/stock/handoffs/lk-content-request-apparel-bestsellers-in-stock-newsletter-20260621.md`  
Dono da validação: `[LK] Estoque Loja Física` / `lk-stock`  
Writes externos: 0 — Tiny/Shopify/Klaviyo somente leitura/cache local  
values_printed=false

## Fontes consultadas

- Vendas/demanda agregada: `shopify_sales_os.db`, view `shopify_sales_paid_line_items_enriched`; janela calculada contra último pedido observado `2026-06-21T20:09:32-03:00`; sem dados de cliente/pedido individual.
- Estoque/disponibilidade interna: Stock OS DB local atual `lk_stock_os_current_tiny_full_sync_20260621T162032Z.db`, tabela `current_local_stock`; fonte de estoque `tiny_full_sync`, depósito operacional `LK | CONTROLE ESTOQUE`; observações Tiny majoritariamente `2026-06-21T06:20:29Z` para camisetas e `2026-06-21T07:20:30Z` para moletons.
- Guardrail: `public_availability_safe=0` e `availability_claim_allowed=0` no Stock OS. Portanto, este relatório confirma disponibilidade apenas para decisão interna de curadoria; não deve prometer grade/pronta entrega publicamente sem reconfirmação final pré-envio.

## Leitura executiva

Há candidatos bons e seguros para newsletter, principalmente camisetas com grade interna positiva. Para inverno/styling masculino, incluir **apenas 1 moletom** com disponibilidade confirmada; alguns moletons best sellers recentes aparecem com demanda, mas estoque atual zerado ou não confirmado.

Recomendação: usar **7 produtos** abaixo. Evitar citar tamanhos na copy pública; tamanhos ficam como apoio interno.

## Ranking por marca — demanda + estoque

### Nude Project

| rank | produto | link | demanda agregada | estoque/disponibilidade interna | confiança | leitura |
|---:|---|---|---|---|---|---|
| 1 | Camiseta Nude Project Global Soon | https://lksneakers.com.br/products/camiseta-nude-project-global-soon | 30d: 1 un.; 60d: 1; 90d: 3; histórico total na base: 5 | **confirmado**: 5 un. internas em 3 variantes; tamanhos seguros: White S/P 2, L/G 2, XL/GG 1 | confirmado | melhor equilíbrio Nude: venda recente + grade mais ampla |
| 2 | Camiseta Nude Project Xoxo Cinza | https://lksneakers.com.br/products/camiseta-nude-projet-xoxo-cinza | 30d: 0; 60d: 0; 90d: 2; histórico: 2 | **confirmado**: 2 un. internas; tamanho seguro: GG/XL 2 | confirmado | gráfico/cinza, bom apoio editorial; grade estreita |
| 3 | Camiseta Nude Project Berry Tee White Branco | https://lksneakers.com.br/products/camiseta-nude-project-berry-tee-white-branco | 30d: 1; 60d: 1; 90d: 1 | **confirmado**: 1 un.; tamanho seguro: M/M 1 | confirmado, baixo estoque | camiseta branca de styling; usar com cautela por estoque baixo |
| 4 | Camiseta Nude Project Kora Black Preto | https://lksneakers.com.br/products/camiseta-nude-project-kora-black-preto | 30d: 0; 60d: 1; 90d: 1 | **confirmado**: 1 un.; tamanho seguro: L/G 1 | confirmado, baixo estoque | opção preta, mas não priorizar acima dos 3 primeiros |
| 5 | Camiseta Nude Project Global Soon Black Preto | https://lksneakers.com.br/products/camiseta-nude-project-global-soon-black-preto | 30d: 2; 60d: 2; 90d: 2 | **não confirmado no handle**; Stock OS encontrou SKUs parecidos em `Global Soon Ash Cinza` com identidade bloqueada | parcial/não confirmado para este link | demanda boa, mas precisa reconciliação SKU/handle antes de entrar |
| 6 | Moletom Nude Project Nude Tour Preto | https://lksneakers.com.br/products/moletom-nude-project-nude-tour-preto | 30d: 1; 60d: 1; 90d: 1 | **sem disponibilidade**: variantes resolvidas com qty 0 | não confirmado para campanha | bloquear; era preview, mas estoque atual não sustenta |

Backups Nude com estoque confirmado, porém sem sinal 90d no ranking de vendas: Calça Nude Project Jeans Old Baggy Blue Azul (2 un.; M/M 1, L/G 1), Camiseta Nude Project Honor Tee Black Preto (2 un.; L/G 1, XL/GG 1), Moletom Nude Project Kill Bill Zip-Up Ash Cinza (1 un.; XL/GG 1). Usar só se Content quiser variedade editorial e aceitar sinal comercial menor.

### Aimé / Aimé Leon Dore

| rank | produto | link | demanda agregada | estoque/disponibilidade interna | confiança | leitura |
|---:|---|---|---|---|---|---|
| 1 | Camiseta Aimé Leon Dore Unisphere Verde | https://lksneakers.com.br/products/camiseta-aime-leon-dore-unisphere-verde | 30d: 1; 60d: 1; 90d: 2 | **confirmado**: 3 un.; S/P 1, M 1, L/G 1 | confirmado | melhor Aimé por venda + grade; verde funciona no inverno |
| 2 | Camiseta Aimé Leon Dore Postcard Cream Bege | https://lksneakers.com.br/products/camiseta-aime-leon-dore-postcard-cream-bege | 30d: 1; 60d: 2; 90d: 2 | **confirmado parcial**: 2 un. seguras M/M 1, L/G 1; variante S/P está bloqueada por duplicidade Tiny | confirmado parcial | boa para bloco neutro/cream; não citar S/P |
| 3 | Camiseta Aimé Leon Dore Unisphere Black White Preto | https://lksneakers.com.br/products/camiseta-aime-leon-dore-unisphere-black-white-preto | 30d: 1; 60d: 1; 90d: 1; histórico: 3 | **confirmado**: 4 un.; S/P 1, M 2, L/G 1 | confirmado | preto gráfico, forte para styling masculino |
| 4 | Camiseta Aimé Leon Dore Saint George Asphalt Preto | https://lksneakers.com.br/products/camiseta-aime-leon-dore-saint-george-asphalt-preto | 30d: 1; 60d: 1; 90d: 1 | **confirmado**: 3 un.; M/M 1, L/G 1, XL/GG 1 | confirmado | já estava no preview e está seguro internamente |
| 5 | Camiseta Aimé Leon Dore Unisphere Pristine Off White | https://lksneakers.com.br/products/camiseta-aime-leon-dore-unisphere-pristine-off-white | 30d: 0; 60d: 0; 90d: 1; histórico: 5 | **confirmado**: 7 un.; S/P 3, M/M 1, L/G 3 | confirmado | maior colchão de estoque Aimé; usar se quiser peça clara/neutra |
| 6 | Camiseta Aimé Leon Dore Saint George Coconut Milk Bege | https://lksneakers.com.br/products/camiseta-aime-leon-dore-saint-george-coconut-milk-bege | 30d: 0; 60d: 0; 90d: 1 | **confirmado**: 5 un.; S/P 1, M/M 2, L/G 1, XL/GG 1 | confirmado | boa alternativa neutra com grade melhor |
| 7 | Camiseta Aimé Leon Dore Pappoús Logo Navy Blazer Azul | https://lksneakers.com.br/products/camiseta-aime-leon-dore-pappous-logo-navy-blazer-azul | 30d: 0; 60d: 0; 90d: 1 | **confirmado**: 5 un.; P 2, M 2, G 1 | confirmado | marinho editorial; boa variação de cor |
| 8 | Moletom Aimé Leon Dore Market Hoodie Pine Groove Verde | https://lksneakers.com.br/products/moletom-aime-leon-dore-market-hoodie-pine-groove-verde | sem venda 90d no ranking principal desta consulta; estava no preview | **confirmado**: 1 un.; M/M 1 | confirmado, baixo estoque | único hoodie Aimé confirmado; usar como peça de inverno, sem prometer grade |
| 9 | Moletom Aimé Leon Dore Unisphere Botanical Green Verde | https://lksneakers.com.br/products/moletom-aime-leon-dore-unisphere-botanical-green-verde | 30d: 1; 60d: 2; 90d: 2 | **sem disponibilidade**: variantes resolvidas com qty 0 | não confirmado para campanha | bloquear apesar de vender bem |
| 10 | Jaqueta Aimé Leon Dore Micro Logo Lightweight Jacket Preto | https://lksneakers.com.br/products/jaqueta-aime-leon-dore-micro-logo-lightweight-jacket-preto | 30d: 1; 60d: 1; 90d: 1 | **não confirmado**: tamanho vendido/consultado com identidade bloqueada; demais variantes qty 0 | não confirmado | bloquear até reconciliação |

## Recomendação final para newsletter — 7 produtos

1. **Camiseta Nude Project Global Soon** — principal Nude; venda 90d mais alta da marca e 5 un. confirmadas em 3 tamanhos.
2. **Camiseta Nude Project Xoxo Cinza** — segundo Nude com venda 90d e estoque confirmado; usar como peça gráfica/cinza.
3. **Camiseta Aimé Leon Dore Unisphere Verde** — principal Aimé por combinação de venda recente e grade confirmada.
4. **Camiseta Aimé Leon Dore Unisphere Black White Preto** — preto gráfico com 4 un. confirmadas; forte para styling masculino.
5. **Camiseta Aimé Leon Dore Saint George Asphalt Preto** — já validada no preview; 3 un. confirmadas e leitura inverno/preto.
6. **Camiseta Aimé Leon Dore Unisphere Pristine Off White** — menor venda recente, mas melhor estoque (7 un.) e peça neutra para compor looks.
7. **Moletom Aimé Leon Dore Market Hoodie Pine Groove Verde** — incluir se a newsletter precisar de inverno/hoodie; estoque interno confirmado, mas baixo (1 un. M/M), então não destacar grade nem disponibilidade pública.

Alternativa se Content quiser 8º produto: **Camiseta Aimé Leon Dore Saint George Coconut Milk Bege** — 5 un. confirmadas e leitura neutra, embora demanda recente menor. Para equilibrar marcas, alternativa Nude seria **Berry Tee White**, mas com apenas 1 un.; eu deixaria como backup, não como hero.

## Itens bloqueados / não confirmados

- **Moletom Nude Project Cult Kid Blue/Grey Cinza** — link do preview não retornou linha confirmada no Stock OS local por handle; **NÃO CONFIRMADO**.
- **Moletom Nude Project Nude Tour Preto** — demanda 90d existe, mas estoque Tiny/Stock OS atual qty 0 em todas as variantes; **bloquear**.
- **Camiseta Nude Project Play With Logo Black Preto** — link do preview não retornou linha confirmada no Stock OS local por handle; **NÃO CONFIRMADO**.
- **Camiseta Nude Project Global Soon Black Preto** — demanda forte, mas estoque local seguro não reconciliou o handle; há SKUs parecidos em `Global Soon Ash Cinza` com identidade bloqueada; **pedir reconciliação SKU/handle antes de usar**.
- **Moletom Aimé Leon Dore Unisphere Botanical Green Verde** — venda boa, mas estoque atual qty 0; **bloquear**.
- **Jaqueta Aimé Leon Dore Micro Logo Lightweight Jacket Preto** — venda recente, mas variante principal bloqueada por duplicidade Tiny e demais zeradas; **bloquear**.
- **Camiseta Aimé Leon Dore Sound Branco** — estoque confirmado (2 un.), mas não apareceu com demanda 90d nesta consulta; pode ser backup editorial, não best seller.

## Próxima ação sugerida

LK Content pode montar a curadoria com os 7 recomendados, sem mencionar grade/quantidade/pronta entrega na copy. Se o HTML for finalizar amanhã, recomendo uma reconfirmação Stock OS/Tiny rápida imediatamente antes do envio para os itens com estoque baixo: `Berry Tee White` se entrar, `Market Hoodie Pine Groove`, e quaisquer peças de 1 unidade.

Reminder OS loop needed: no  
Owner: lk-content após recebimento deste relatório  
Próxima ação: Content selecionar produtos/copy usando apenas itens `confirmado`/`confirmado parcial` acima  
Gatilho de revisão: se qualquer item de baixo estoque for hero ou se houver atraso até o envio amanhã  
Evidência: este relatório + DBs locais citados  
Writes externos executados: 0
