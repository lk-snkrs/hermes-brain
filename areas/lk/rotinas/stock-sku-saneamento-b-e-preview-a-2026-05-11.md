# LK Stock — Fila B saneada + Fila A preview — 2026-05-11

Status: análise read-only. Não altera Shopify, Tiny, campanhas, fornecedores, clientes, banco ou estoque.

## Fontes e método
- Fonte de venda/estoque operacional anterior: `reports/lk-influencer-sku-stock-matrix-readonly-2026-05-10.json`.
- Shopify Admin GraphQL usado apenas em `query` para procurar SKU atual de produto/variante quando o pedido veio sem SKU.
- Tiny API usada apenas para pesquisa read-only de candidatos quando havia SKU candidato ou `mapear SKU no Tiny`.
- SKU Shopify continua sendo chave canônica; Tiny continua verdade de estoque.

## Resultado da Fila B — sanear antes de comprar
- Total Fila B analisado: 33 linhas.
- needs_manual_shopify_sku: 11
- sku_candidate_found: 14
- tiny_candidate_found: 8

### B1 — Candidatos com SKU atual encontrado na Shopify
- **Tênis Nike Moon Shoe SP Jacquemus Off White / SKU candidato HV8547-002-36 / tam. 36**
  - influencer: Silvia Heinz; vendido: 2 un.; receita: R$ 9.999,98
  - Shopify atual: variante `36`; handle `tenis-nike-moon-shoe-sp-jacquemus-off-white`
  - Tiny candidato: `HV8547-002-36` — Tênis Nike Moon Shoe SP Jacquemus Off White - 36; status A
  - ação segura: validar cadastro/mapeamento; só depois mover para Fila A se estoque Tiny confirmar ruptura/baixo estoque.
- **Tênis New Balance 204L Cortado Marrom / SKU candidato NB-0254942-39 / tam. 39**
  - influencer: Silvia Heinz; vendido: 2 un.; receita: R$ 5.599,98
  - Shopify atual: variante `39`; handle `tenis-new-balance-204l-cortado-marrom`
  - Tiny candidato: `` — Tênis New Balance 204L Cortado Marrom - 39; status A
  - ação segura: validar cadastro/mapeamento; só depois mover para Fila A se estoque Tiny confirmar ruptura/baixo estoque.
- **Tênis Nike Moon Shoe SP Jacquemus Off White / SKU candidato HV8547-002-44 / tam. 44**
  - influencer: Silvia Heinz; vendido: 1 un.; receita: R$ 4.999,99
  - Shopify atual: variante `44`; handle `tenis-nike-moon-shoe-sp-jacquemus-off-white`
  - Tiny candidato: `HV8547-002-44` — Tênis Nike Moon Shoe SP Jacquemus Off White - 44; status A
  - ação segura: validar cadastro/mapeamento; só depois mover para Fila A se estoque Tiny confirmar ruptura/baixo estoque.
- **Tênis Nike x Skims Rift Mesh Archaeo Brown Marrom / SKU candidato NKS-1065310-36 / tam. 36**
  - influencer: Silvia Heinz; vendido: 1 un.; receita: R$ 3.499,99
  - Shopify atual: variante `36`; handle `tenis-nike-x-skims-rift-mesh-archaeo-brown-marrom`
  - Tiny candidato: `` — Tênis Nike x Skims Rift Mesh Archaeo Brown Marrom - 36; status A
  - ação segura: validar cadastro/mapeamento; só depois mover para Fila A se estoque Tiny confirmar ruptura/baixo estoque.
- **Tênis Nike Mind 002 Light Khaki Bege / SKU candidato NKE-9054174-41 / tam. 41**
  - influencer: Silvia Heinz; vendido: 1 un.; receita: R$ 3.199,99
  - Shopify atual: variante `41`; handle `tenis-nike-mind-002-light-khaki-bege`
  - Tiny candidato: `` — Tênis Nike Mind 002 Light Khaki Bege - 41; status A
  - ação segura: validar cadastro/mapeamento; só depois mover para Fila A se estoque Tiny confirmar ruptura/baixo estoque.
- **Tênis Nike Mind 002 Light Smoke Grey Cinza / SKU candidato HQ4308-003-1 / tam. 41**
  - influencer: Silvia Heinz; vendido: 1 un.; receita: R$ 3.199,99
  - Shopify atual: variante `41`; handle `tenis-nike-mind-002-light-smoke-grey-cinza`
  - Tiny candidato: `HQ4308-003-1` — Tênis Nike Mind 002 Light Smoke Grey Cinza - 41; status A
  - ação segura: validar cadastro/mapeamento; só depois mover para Fila A se estoque Tiny confirmar ruptura/baixo estoque.
- **Tênis Onitsuka Tiger Mexico 66 Fringe Mocha Brown/Dark Brown Marrom / SKU candidato ONI-0995678-425 / tam. 42.5**
  - influencer: Silvia Heinz; vendido: 1 un.; receita: R$ 2.999,99
  - Shopify atual: variante `42.5`; handle `tenis-onitsuka-tiger-mexico-66-fringe-mocha-brown-dark-brown-marrom`
  - Tiny candidato: `` — Tênis Onitsuka Tiger Mexico 66 Fringe Mocha Brown/Dark Brown Marrom - 42.5; status A
  - ação segura: validar cadastro/mapeamento; só depois mover para Fila A se estoque Tiny confirmar ruptura/baixo estoque.
- **Tênis New Balance 204L Cortado Marrom / SKU candidato NB-0254942-37 / tam. 37**
  - influencer: Silvia Heinz; vendido: 1 un.; receita: R$ 2.799,99
  - Shopify atual: variante `37`; handle `tenis-new-balance-204l-cortado-marrom`
  - Tiny candidato: `` — Tênis New Balance 204L Cortado Marrom - 37; status A
  - ação segura: validar cadastro/mapeamento; só depois mover para Fila A se estoque Tiny confirmar ruptura/baixo estoque.
- **Tênis Onitsuka Tiger Mexico 66 Sabot Pure Silver Cream Cinza / SKU candidato ONI-6772830-38 / tam. 38**
  - influencer: Silvia Heinz; vendido: 1 un.; receita: R$ 2.199,99
  - Shopify atual: variante `38`; handle `tenis-onitsuka-tiger-mexico-66-sabot-pure-silver-cream-cinza`
  - Tiny candidato: `` — Tênis Onitsuka Tiger Mexico 66 Sabot Pure Silver Cream Cinza - 38; status A
  - ação segura: validar cadastro/mapeamento; só depois mover para Fila A se estoque Tiny confirmar ruptura/baixo estoque.
- **Moletom Alo Yoga Cropped Serenity Coverup Black Preto / SKU candidato ALO-8506462-XS / tam. S/P**
  - influencer: Silvia Heinz; vendido: 1 un.; receita: R$ 1.799,99
  - Shopify atual: variante `XS/PP`; handle `moletom-alo-yoga-cropped-serenity-coverup-black-preto`
  - Tiny candidato: `` — Moletom Alo Yoga Cropped Serenity Coverup Black Preto; status A
  - ação segura: validar cadastro/mapeamento; só depois mover para Fila A se estoque Tiny confirmar ruptura/baixo estoque.
- **Calça Saint Studio Alfaiataria Leve Prega Dupla Cinza / SKU candidato SST-4542302-L / tam. L/G**
  - influencer: Silvia Heinz; vendido: 1 un.; receita: R$ 619,99
  - Shopify atual: variante `L/G`; handle `calca-saint-studio-alfaiataria-leve-prega-dupla-cinza`
  - Tiny candidato: `` — Calça Saint Studio Alfaiataria Leve Prega Dupla Cinza; status A
  - ação segura: validar cadastro/mapeamento; só depois mover para Fila A se estoque Tiny confirmar ruptura/baixo estoque.
- **Camiseta Pace Buero Washed Black Preto / SKU candidato PAC-1197278-S / tam. S/P**
  - influencer: Silvia Heinz; vendido: 1 un.; receita: R$ 319,99
  - Shopify atual: variante `S/P`; handle `camiseta-pace-buero-washed-black-preto`
  - Tiny candidato: `` — Camiseta Pace Buero Washed Black Preto; status A
  - ação segura: validar cadastro/mapeamento; só depois mover para Fila A se estoque Tiny confirmar ruptura/baixo estoque.
- **Camiseta Pace Patavision Off White / SKU candidato PAC-5857246-S / tam. P/S**
  - influencer: Silvia Heinz; vendido: 1 un.; receita: R$ 209,99
  - Shopify atual: variante `P/S`; handle `camiseta-pace-patavision-off-white`
  - Tiny candidato: `` — Camiseta Pace Patavision Off White - P/S; status A
  - ação segura: validar cadastro/mapeamento; só depois mover para Fila A se estoque Tiny confirmar ruptura/baixo estoque.
- **Tênis Nike Moon Shoe SP Jacquemus Off White / SKU candidato HV8547-002-38 / tam. 38**
  - influencer: Helena Lunardelli; vendido: 1 un.; receita: R$ 4.999,99
  - Shopify atual: variante `38`; handle `tenis-nike-moon-shoe-sp-jacquemus-off-white`
  - Tiny candidato: `HV8547-002-38` — Tênis Nike Moon Shoe SP Jacquemus Off White - 38; status A
  - ação segura: validar cadastro/mapeamento; só depois mover para Fila A se estoque Tiny confirmar ruptura/baixo estoque.

### B2 — Candidatos Tiny encontrados para itens `mapear SKU no Tiny`
- **Tênis Onitsuka Tiger Mexico 66 Kill Bill Amarelo / SKU Shopify 1183C102751-4 / tam. 37**
  - influencer: Silvia Heinz; vendido: 2 un.; receita: R$ 4.799,98
  - Tiny candidato: `1183C102 751-4` — Tênis Onitsuka Tiger Mexico 66 Kill Bill Amarelo - 37; matches exatos: 1
  - ação segura: aprovar alias/normalização de mapeamento Tiny somente após revisão humana; não alterar Shopify.
- **Tênis Onitsuka Tiger Mexico 66 Kill Bill Amarelo / SKU Shopify 1183C102751-8 / tam. 42.5**
  - influencer: Silvia Heinz; vendido: 1 un.; receita: R$ 2.399,99
  - Tiny candidato: `1183C102 751-8` — Tênis Onitsuka Tiger Mexico 66 Kill Bill Amarelo - 42.5; matches exatos: 1
  - ação segura: aprovar alias/normalização de mapeamento Tiny somente após revisão humana; não alterar Shopify.
- **Tênis Onitsuka Tiger Mexico 66 Kill Bill Amarelo / SKU Shopify 1183C102751-9 / tam. 40**
  - influencer: Silvia Heinz; vendido: 1 un.; receita: R$ 2.399,99
  - Tiny candidato: `1183C102 751-9` — Tênis Onitsuka Tiger Mexico 66 Kill Bill Amarelo - 40; matches exatos: 1
  - ação segura: aprovar alias/normalização de mapeamento Tiny somente após revisão humana; não alterar Shopify.
- **Tênis Onitsuka Tiger Mexico 66 Chrome Silver Prata / SKU Shopify 1183B566021-4 / tam. 37**
  - influencer: Silvia Heinz; vendido: 1 un.; receita: R$ 2.399,99
  - Tiny candidato: `1183B566 021-4` — Tênis Onitsuka Tiger Mexico 66 Chrome Silver Prata - 37; matches exatos: 1
  - ação segura: aprovar alias/normalização de mapeamento Tiny somente após revisão humana; não alterar Shopify.
- **Tênis Onitsuka Tiger Mexico 66 Kill Bill Amarelo / SKU Shopify 1183C102751-6 / tam. 39**
  - influencer: Silvia Heinz; vendido: 1 un.; receita: R$ 2.399,99
  - Tiny candidato: `1183C102 751-6` — Tênis Onitsuka Tiger Mexico 66 Kill Bill Amarelo - 39; matches exatos: 1
  - ação segura: aprovar alias/normalização de mapeamento Tiny somente após revisão humana; não alterar Shopify.
- **Tênis Onitsuka Tiger Mexico 66 Sabot Birch Peacoat Bege / SKU Shopify ONI-3740254-39 / tam. 39**
  - influencer: Silvia Heinz; vendido: 1 un.; receita: R$ 2.199,99
  - Tiny candidato: `` — Tênis Onitsuka Tiger Mexico 66 Sabot Birch Peacoat Bege - 39; matches exatos: 0
  - ação segura: aprovar alias/normalização de mapeamento Tiny somente após revisão humana; não alterar Shopify.
- **Tênis Onitsuka Tiger Mexico 66 Kill Bill Amarelo / SKU Shopify 1183C102751-2 / tam. 35**
  - influencer: Helena Lunardelli; vendido: 1 un.; receita: R$ 2.399,99
  - Tiny candidato: `1183C102 751-2` — Tênis Onitsuka Tiger Mexico 66 Kill Bill Amarelo - 35; matches exatos: 1
  - ação segura: aprovar alias/normalização de mapeamento Tiny somente após revisão humana; não alterar Shopify.
- **Tênis Onitsuka Tiger Mexico 66 Kill Bill Amarelo / SKU Shopify 1183C102751-3 / tam. 36**
  - influencer: Helena Lunardelli; vendido: 1 un.; receita: R$ 2.399,99
  - Tiny candidato: `1183C102 751-3` — Tênis Onitsuka Tiger Mexico 66 Kill Bill Amarelo - 36; matches exatos: 1
  - ação segura: aprovar alias/normalização de mapeamento Tiny somente após revisão humana; não alterar Shopify.

### B3 — Ainda precisam revisão manual
- **Tênis Nike Moon Shoe SP Jacquemus Medium Brown / SKU [sem SKU no Shopify] / tam. 37** — Sem SKU atual encontrado via busca Shopify read-only; revisar cadastro Shopify manualmente antes de decisão.
- **Tênis Nike Moon Shoe SP Jacquemus Medium Brown / SKU [sem SKU no Shopify] / tam. 36** — Sem SKU atual encontrado via busca Shopify read-only; revisar cadastro Shopify manualmente antes de decisão.
- **Tênis Nike Moon Shoe SP Jacquemus Medium Brown / SKU [sem SKU no Shopify] / tam. 38** — Sem SKU atual encontrado via busca Shopify read-only; revisar cadastro Shopify manualmente antes de decisão.
- **Tênis Onitsuka Tiger Mexico 66 Chrome Silver Prata / SKU [sem SKU no Shopify] / tam. 35.5** — Sem SKU atual encontrado via busca Shopify read-only; revisar cadastro Shopify manualmente antes de decisão.
- **Tênis Nike Air Jordan 1 Low White University Red Branco / SKU [sem SKU no Shopify] / tam. 36** — Sem SKU atual encontrado via busca Shopify read-only; revisar cadastro Shopify manualmente antes de decisão.
- **Camiseta Aimé Leon Dore Musician Graphic Off White / SKU [sem SKU no Shopify] / tam. S/P** — Sem SKU atual encontrado via busca Shopify read-only; revisar cadastro Shopify manualmente antes de decisão.
- **Rhode Pocket Blush / SKU [sem SKU no Shopify] / tam. Sleepy Girl - Soft Mauve** — Sem SKU atual encontrado via busca Shopify read-only; revisar cadastro Shopify manualmente antes de decisão.
- **Camiseta Pace Cotton Code Preta / SKU [sem SKU no Shopify] / tam. G/L** — Sem SKU atual encontrado via busca Shopify read-only; revisar cadastro Shopify manualmente antes de decisão.
- **Camiseta Pace Cotton Code Branca / SKU [sem SKU no Shopify] / tam. G/L** — Sem SKU atual encontrado via busca Shopify read-only; revisar cadastro Shopify manualmente antes de decisão.
- **Camiseta Pace Sketch Yourself Off White / SKU [sem SKU no Shopify] / tam. P/S** — Sem SKU atual encontrado via busca Shopify read-only; revisar cadastro Shopify manualmente antes de decisão.
- **Camiseta Pace Cotton Code Branca / SKU [sem SKU no Shopify] / tam. G/L** — Sem SKU atual encontrado via busca Shopify read-only; revisar cadastro Shopify manualmente antes de decisão.

## Fila A — preview de sourcing/reposição após B
Regra: aprovação aqui libera apenas checagem/sourcing interno; compra/contato externo continua exigindo novo preview.

### Top P0/P1 por venda e ruptura
- **Tênis Nike Air Jordan 4 Retro Metallic Gold Branco / SKU AQ9129-170-7 / tam. 40**
  - prioridade: P0 — ruptura com venda repetida; influencer: Silvia Heinz; vendido: 4 un.; receita: R$ 13.399,96
  - Tiny LK Controle Estoque: 0.0; leitura: ruptura agora; velocidade estimada: 1.32 un./30d
  - ação preview: checar sourcing/reposição; sem compra/fornecedor sem aprovação explícita.
- **Tênis Nike Moon Shoe SP Jacquemus Medium Brown / SKU HV8547-200-38 / tam. 38**
  - prioridade: P0 — ruptura com venda repetida; influencer: Silvia Heinz; vendido: 3 un.; receita: R$ 14.999,97
  - Tiny LK Controle Estoque: 0.0; leitura: ruptura agora; velocidade estimada: 0.99 un./30d
  - ação preview: checar sourcing/reposição; sem compra/fornecedor sem aprovação explícita.
- **Tênis Onitsuka Tiger Mexico 66 White Black Branco / SKU 1183A201-126-3 / tam. 36**
  - prioridade: P0 — ruptura com venda repetida; influencer: Silvia Heinz; vendido: 3 un.; receita: R$ 7.199,97
  - Tiny LK Controle Estoque: 0.0; leitura: ruptura agora; velocidade estimada: 0.99 un./30d
  - ação preview: checar sourcing/reposição; sem compra/fornecedor sem aprovação explícita.
- **Tênis Nike Moon Shoe SP Jacquemus Medium Brown Marrom / SKU HV8547-200-38 / tam. 38**
  - prioridade: P0 — ruptura com venda repetida; influencer: Silvia Heinz; vendido: 2 un.; receita: R$ 11.999,98
  - Tiny LK Controle Estoque: 0.0; leitura: ruptura agora; velocidade estimada: 0.66 un./30d
  - ação preview: checar sourcing/reposição; sem compra/fornecedor sem aprovação explícita.
- **Tênis Nike Moon Shoe SP Jacquemus Off Noir Preto / SKU HV8547-001-8 / tam. 41**
  - prioridade: P0 — ruptura com venda repetida; influencer: Silvia Heinz; vendido: 2 un.; receita: R$ 11.999,98
  - Tiny LK Controle Estoque: 0.0; leitura: ruptura agora; velocidade estimada: 0.66 un./30d
  - ação preview: checar sourcing/reposição; sem compra/fornecedor sem aprovação explícita.
- **Tênis Nike Moon Shoe SP Jacquemus Off White / SKU HV8547-002-39 / tam. 39**
  - prioridade: P0 — ruptura com venda repetida; influencer: Silvia Heinz; vendido: 2 un.; receita: R$ 9.999,98
  - Tiny LK Controle Estoque: 0.0; leitura: ruptura agora; velocidade estimada: 0.66 un./30d
  - ação preview: checar sourcing/reposição; sem compra/fornecedor sem aprovação explícita.
- **Tênis Nike Moon Shoe SP Jacquemus Off White / SKU HV8547-002-38 / tam. 38**
  - prioridade: P0 — ruptura com venda repetida; influencer: Silvia Heinz; vendido: 2 un.; receita: R$ 9.999,98
  - Tiny LK Controle Estoque: 0.0; leitura: ruptura agora; velocidade estimada: 0.66 un./30d
  - ação preview: checar sourcing/reposição; sem compra/fornecedor sem aprovação explícita.
- **Tênis New Balance 204L Arid Timberwolf Bege / SKU U204LMMC-3 / tam. 36**
  - prioridade: P2 — monitorar / validar lead time; influencer: Silvia Heinz; vendido: 2 un.; receita: R$ 5.599,98
  - Tiny LK Controle Estoque: 2.0; leitura: baixo estoque; velocidade estimada: 0.66 un./30d
  - ação preview: checar sourcing/reposição; sem compra/fornecedor sem aprovação explícita.
- **Tênis New Balance 9060 Cortado Marrom / SKU U9060496 / tam. 37**
  - prioridade: P2 — monitorar / validar lead time; influencer: Silvia Heinz; vendido: 2 un.; receita: R$ 4.799,98
  - Tiny LK Controle Estoque: 1.0; leitura: baixo estoque; velocidade estimada: 0.66 un./30d
  - ação preview: checar sourcing/reposição; sem compra/fornecedor sem aprovação explícita.
- **Tênis Onitsuka Tiger Mexico 66 Paraty Birch Cream Bege / SKU 1183B601.200-6 / tam. 39**
  - prioridade: P0 — ruptura com venda repetida; influencer: Silvia Heinz; vendido: 2 un.; receita: R$ 4.599,98
  - Tiny LK Controle Estoque: 0.0; leitura: ruptura agora; velocidade estimada: 0.66 un./30d
  - ação preview: checar sourcing/reposição; sem compra/fornecedor sem aprovação explícita.
- **Tênis Onitsuka Tiger Mexico 66 Sabot Beige Green Bege / SKU 1183C123.252-7 / tam. 40**
  - prioridade: P0 — ruptura com venda repetida; influencer: Silvia Heinz; vendido: 2 un.; receita: R$ 4.399,98
  - Tiny LK Controle Estoque: 0.0; leitura: ruptura agora; velocidade estimada: 0.66 un./30d
  - ação preview: checar sourcing/reposição; sem compra/fornecedor sem aprovação explícita.
- **Tênis Onitsuka Tiger Mexico 66 Sabot Beige Green Bege / SKU 1183C123.252-5 / tam. 38**
  - prioridade: P0 — ruptura com venda repetida; influencer: Silvia Heinz; vendido: 2 un.; receita: R$ 4.399,98
  - Tiny LK Controle Estoque: 0.0; leitura: ruptura agora; velocidade estimada: 0.66 un./30d
  - ação preview: checar sourcing/reposição; sem compra/fornecedor sem aprovação explícita.
- **Tênis Onitsuka Tiger Mexico 66 Sabot Beige Green Bege / SKU 1183C123.252-4 / tam. 37**
  - prioridade: P0 — ruptura com venda repetida; influencer: Silvia Heinz; vendido: 2 un.; receita: R$ 4.399,98
  - Tiny LK Controle Estoque: 0.0; leitura: ruptura agora; velocidade estimada: 0.66 un./30d
  - ação preview: checar sourcing/reposição; sem compra/fornecedor sem aprovação explícita.
- **Jason Markk Essential Kit de Limpeza / SKU 300110 / tam. [sem variant]**
  - prioridade: P0 — ruptura com venda repetida; influencer: Silvia Heinz; vendido: 2 un.; receita: R$ 399,98
  - Tiny LK Controle Estoque: -2.0; leitura: ruptura agora; velocidade estimada: 0.66 un./30d
  - ação preview: checar sourcing/reposição; sem compra/fornecedor sem aprovação explícita.
- **Tênis Onitsuka Tiger x Versace TAI-CHI Sakura Suede Sneakers Brown Bege / SKU 1025116-1A17741_2NM5J-3 / tam. 36**
  - prioridade: P2 — monitorar / validar lead time; influencer: Silvia Heinz; vendido: 1 un.; receita: R$ 8.499,99
  - Tiny LK Controle Estoque: 1.0; leitura: baixo estoque; velocidade estimada: 0.33 un./30d
  - ação preview: checar sourcing/reposição; sem compra/fornecedor sem aprovação explícita.
- **Tênis Nike Moon Shoe SP Jacquemus Off Noir Preto / SKU HV8547-001-5 / tam. 38**
  - prioridade: P1 — ruptura com venda unitária; influencer: Silvia Heinz; vendido: 1 un.; receita: R$ 5.999,99
  - Tiny LK Controle Estoque: 0.0; leitura: ruptura agora; velocidade estimada: 0.33 un./30d
  - ação preview: checar sourcing/reposição; sem compra/fornecedor sem aprovação explícita.
- **Tênis Nike Moon Shoe SP Jacquemus Off Noir Preto / SKU HV8547-001-7 / tam. 40**
  - prioridade: P1 — ruptura com venda unitária; influencer: Silvia Heinz; vendido: 1 un.; receita: R$ 5.999,99
  - Tiny LK Controle Estoque: 0.0; leitura: ruptura agora; velocidade estimada: 0.33 un./30d
  - ação preview: checar sourcing/reposição; sem compra/fornecedor sem aprovação explícita.
- **Tênis Nike Moon Shoe SP Jacquemus Alabaster Amarelo / SKU HV8547-700-7 / tam. 40**
  - prioridade: P1 — ruptura com venda unitária; influencer: Silvia Heinz; vendido: 1 un.; receita: R$ 5.999,99
  - Tiny LK Controle Estoque: 0.0; leitura: ruptura agora; velocidade estimada: 0.33 un./30d
  - ação preview: checar sourcing/reposição; sem compra/fornecedor sem aprovação explícita.
- **Tênis Nike Moon Shoe SP Jacquemus Off White / SKU HV8547-002-36 / tam. 36**
  - prioridade: P1 — ruptura com venda unitária; influencer: Silvia Heinz; vendido: 1 un.; receita: R$ 4.999,99
  - Tiny LK Controle Estoque: 0.0; leitura: ruptura agora; velocidade estimada: 0.33 un./30d
  - ação preview: checar sourcing/reposição; sem compra/fornecedor sem aprovação explícita.
- **Tênis Nike Moon Shoe SP Jacquemus Medium Brown / SKU HV8547-200-39 / tam. 39**
  - prioridade: P1 — ruptura com venda unitária; influencer: Silvia Heinz; vendido: 1 un.; receita: R$ 4.999,99
  - Tiny LK Controle Estoque: -1.0; leitura: ruptura agora; velocidade estimada: 0.33 un./30d
  - ação preview: checar sourcing/reposição; sem compra/fornecedor sem aprovação explícita.
- **Tênis Nike Moon Shoe SP Jacquemus Off White / SKU HV8547-002-34 / tam. 34**
  - prioridade: P1 — ruptura com venda unitária; influencer: Silvia Heinz; vendido: 1 un.; receita: R$ 4.999,99
  - Tiny LK Controle Estoque: 0.0; leitura: ruptura agora; velocidade estimada: 0.33 un./30d
  - ação preview: checar sourcing/reposição; sem compra/fornecedor sem aprovação explícita.
- **Tênis Nike Moon Shoe SP Jacquemus Medium Brown / SKU HV8547-200-37 / tam. 37**
  - prioridade: P1 — ruptura com venda unitária; influencer: Silvia Heinz; vendido: 1 un.; receita: R$ 4.999,99
  - Tiny LK Controle Estoque: 0.0; leitura: ruptura agora; velocidade estimada: 0.33 un./30d
  - ação preview: checar sourcing/reposição; sem compra/fornecedor sem aprovação explícita.
- **Tênis Nike Moon Shoe SP Jacquemus Pale Pink Rosa / SKU HV8547-601-34 / tam. 34**
  - prioridade: P1 — ruptura com venda unitária; influencer: Silvia Heinz; vendido: 1 un.; receita: R$ 4.999,99
  - Tiny LK Controle Estoque: 0.0; leitura: ruptura agora; velocidade estimada: 0.33 un./30d
  - ação preview: checar sourcing/reposição; sem compra/fornecedor sem aprovação explícita.
- **Tênis Nike Moon Shoe SP Jacquemus Off White / SKU HV8547-002-37 / tam. 37**
  - prioridade: P1 — ruptura com venda unitária; influencer: Silvia Heinz; vendido: 1 un.; receita: R$ 4.999,99
  - Tiny LK Controle Estoque: 0.0; leitura: ruptura agora; velocidade estimada: 0.33 un./30d
  - ação preview: checar sourcing/reposição; sem compra/fornecedor sem aprovação explícita.
- **Tênis Nike Moon Shoe SP Jacquemus Medium Brown / SKU HV8547-200-36 / tam. 36**
  - prioridade: P1 — ruptura com venda unitária; influencer: Silvia Heinz; vendido: 1 un.; receita: R$ 4.999,99
  - Tiny LK Controle Estoque: 0.0; leitura: ruptura agora; velocidade estimada: 0.33 un./30d
  - ação preview: checar sourcing/reposição; sem compra/fornecedor sem aprovação explícita.

## Mission Control — cards unassigned
- `LK-STOCK-B-SKU-SANEAR` — ready_for_review — owner: unassigned — validar candidatos SKU Shopify/Tiny e aprovar ajustes de mapeamento/alias; sem write automático
- `LK-STOCK-A-SOURCING-PREVIEW` — needs_lucas_approval — owner: unassigned — aprovar checagem de sourcing/reposição dos P0/P1; sem compra/contato externo
- `LK-STOCK-VELOCITY-LEADTIME` — draft_ready — owner: unassigned — substituir lead time padrão por lead time real Monbam/Droper/interno quando disponível
- `LK-DATA-SPINE-V0` — next — owner: unassigned — inventário de fontes e matriz de credenciais sem valores

## Frase de aprovação sugerida
```text
Aprovo usar a Fila B saneada para validar mapeamento SKU Shopify↔Tiny e aprovo checar sourcing/reposição dos P0/P1 da Fila A, sem compra, sem contato externo e sem alteração em Shopify/Tiny sem novo preview.
```
