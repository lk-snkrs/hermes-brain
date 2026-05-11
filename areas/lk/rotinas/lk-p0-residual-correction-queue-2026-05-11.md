# LK — Fila acionável P0 residual para correção SKU/Tiny

Data: 2026-05-11

## Veredito
Transformei os 15 P0 residuais em uma fila acionável de decisão/correção. Nenhum item está pronto para write automático: todos exigem confirmação de SKU canônico no Tiny ou cadastro/alias antes de Fila A/sourcing.

## Resumo
- Total P0: 15
- Com match Tiny de tamanho, mas sem `codigo`/ambíguo: 6
- Sem match Tiny detalhado: 9

## Fila de decisão
### 1. Camiseta Pace Cotton Code Branca
- Shopify variant: `47512247599326`
- Tamanho: `G/L`
- SKU Shopify atual: `[sem SKU]`
- Sinal 30d: pedidos `2`, receita `R$ 433.98`
- Classificação: `A_match_tiny_sem_codigo_ou_ambiguo`
- Próximo passo: Definir codigo canônico no Tiny para a variação correta; depois preview SKU-only no Shopify se necessário.
- Matches Tiny tamanho consultados:
  - Tiny item `1065543106` — codigo `[sem código]` — Tamanho: G/L
  - Tiny item `1065543109` — codigo `[sem código]` — Tamanho: GG/XL
  - Tiny item `1069541599` — codigo `[sem código]` — Tamanho: G/L

### 2. Camiseta Aimé Leon Dore Musician Graphic Off White
- Shopify variant: `47579297939678`
- Tamanho: `S/P`
- SKU Shopify atual: `[sem SKU]`
- Sinal 30d: pedidos `1`, receita `R$ 1299.99`
- Classificação: `B_sem_match_tiny_detalhado`
- Próximo passo: Resolver cadastro/codigo canônico no Tiny manualmente antes de qualquer ação comercial.

### 3. Rhode Pocket Blush
- Shopify variant: `46838740648158`
- Tamanho: `Sleepy Girl - Soft Mauve`
- SKU Shopify atual: `[sem SKU]`
- Sinal 30d: pedidos `1`, receita `R$ 399.99`
- Classificação: `A_match_tiny_sem_codigo_ou_ambiguo`
- Próximo passo: Definir codigo canônico no Tiny para a variação correta; depois preview SKU-only no Shopify se necessário.
- Matches Tiny tamanho consultados:
  - Tiny item `1070288342` — codigo `[sem código]` — Cor: Sleepy Girl - Soft Mauve

### 4. Camiseta Pace Cotton Code Preta
- Shopify variant: `47512247730398`
- Tamanho: `G/L`
- SKU Shopify atual: `[sem SKU]`
- Sinal 30d: pedidos `1`, receita `R$ 216.99`
- Classificação: `A_match_tiny_sem_codigo_ou_ambiguo`
- Próximo passo: Definir codigo canônico no Tiny para a variação correta; depois preview SKU-only no Shopify se necessário.
- Matches Tiny tamanho consultados:
  - Tiny item `1065543087` — codigo `[sem código]` — Tamanho: G/L
  - Tiny item `1065543090` — codigo `[sem código]` — Tamanho: GG/XL
  - Tiny item `1069541614` — codigo `[sem código]` — Tamanho: G/L

### 5. Camiseta Pace Sketch Yourself Off White
- Shopify variant: `47019131568350`
- Tamanho: `P/S`
- SKU Shopify atual: `[sem SKU]`
- Sinal 30d: pedidos `1`, receita `R$ 209.99`
- Classificação: `A_match_tiny_sem_codigo_ou_ambiguo`
- Próximo passo: Definir codigo canônico no Tiny para a variação correta; depois preview SKU-only no Shopify se necessário.
- Matches Tiny tamanho consultados:
  - Tiny item `1063954611` — codigo `[sem código]` — Tamanho: P/S
  - Tiny item `1069539379` — codigo `[sem código]` — Tamanho: P/S
  - Tiny item `1069539379` — codigo `[sem código]` — Camiseta Pace Sketch Yourself Off White - P-S

### 6. Tênis New Balance 204L Cortado Marrom
- Shopify variant: `47856402596062`
- Tamanho: `39`
- SKU Shopify atual: `NB-0254942-39`
- Sinal 30d: pedidos `2`, receita `R$ 5599.98`
- Classificação: `A_match_tiny_sem_codigo_ou_ambiguo`
- Próximo passo: Validar se o SKU Shopify deve virar codigo Tiny; se aprovado, primeiro corrigir Tiny/codigo, depois revalidar Shopify.
- Matches Tiny tamanho consultados:
  - Tiny item `1069544054` — codigo `[sem código]` — Tamanho do calçado: 39

### 7. Tênis Nike x Skims Rift Mesh Archaeo Brown Marrom
- Shopify variant: `47868839035102`
- Tamanho: `36`
- SKU Shopify atual: `NKS-1065310-36`
- Sinal 30d: pedidos `1`, receita `R$ 3499.99`
- Classificação: `A_match_tiny_sem_codigo_ou_ambiguo`
- Próximo passo: Validar se o SKU Shopify deve virar codigo Tiny; se aprovado, primeiro corrigir Tiny/codigo, depois revalidar Shopify.
- Matches Tiny tamanho consultados:
  - Tiny item `1069544710` — codigo `[sem código]` — Tamanho do calçado: 36
  - Tiny item `1069544710` — codigo `[sem código]` — Tênis Nike x Skims Rift Mesh Archaeo Brown Marrom - 36

### 8. Tênis Nike Mind 002 Light Khaki Bege
- Shopify variant: `47893735932126`
- Tamanho: `41`
- SKU Shopify atual: `NKE-9054174-41`
- Sinal 30d: pedidos `1`, receita `R$ 3199.99`
- Classificação: `B_sem_match_tiny_detalhado`
- Próximo passo: Buscar alias/cadastro no Tiny usando SKU Shopify como pista; se não existir, decidir cadastro/codigo Tiny antes de sourcing.

### 9. Tênis Onitsuka Tiger Mexico 66 Fringe Mocha Brown/Dark Brown Marrom
- Shopify variant: `48066691465438`
- Tamanho: `42.5`
- SKU Shopify atual: `ONI-0995678-425`
- Sinal 30d: pedidos `1`, receita `R$ 2999.99`
- Classificação: `B_sem_match_tiny_detalhado`
- Próximo passo: Buscar alias/cadastro no Tiny usando SKU Shopify como pista; se não existir, decidir cadastro/codigo Tiny antes de sourcing.

### 10. Tênis New Balance 204L Cortado Marrom
- Shopify variant: `47856402530526`
- Tamanho: `37`
- SKU Shopify atual: `NB-0254942-37`
- Sinal 30d: pedidos `1`, receita `R$ 2799.99`
- Classificação: `B_sem_match_tiny_detalhado`
- Próximo passo: Buscar alias/cadastro no Tiny usando SKU Shopify como pista; se não existir, decidir cadastro/codigo Tiny antes de sourcing.

### 11. Tênis Onitsuka Tiger Mexico 66 Sabot Pure Silver Cream Cinza
- Shopify variant: `48054217933022`
- Tamanho: `38`
- SKU Shopify atual: `ONI-6772830-38`
- Sinal 30d: pedidos `1`, receita `R$ 2199.99`
- Classificação: `B_sem_match_tiny_detalhado`
- Próximo passo: Buscar alias/cadastro no Tiny usando SKU Shopify como pista; se não existir, decidir cadastro/codigo Tiny antes de sourcing.

### 12. Moletom Alo Yoga Cropped Serenity Coverup Black Preto
- Shopify variant: `47706484539614`
- Tamanho: `S/P`
- SKU Shopify atual: `ALO-8506462-S`
- Sinal 30d: pedidos `1`, receita `R$ 1799.99`
- Classificação: `B_sem_match_tiny_detalhado`
- Próximo passo: Buscar alias/cadastro no Tiny usando SKU Shopify como pista; se não existir, decidir cadastro/codigo Tiny antes de sourcing.

### 13. Calça Saint Studio Alfaiataria Leve Prega Dupla Cinza
- Shopify variant: `47860151976158`
- Tamanho: `L/G`
- SKU Shopify atual: `SST-4542302-L`
- Sinal 30d: pedidos `1`, receita `R$ 619.99`
- Classificação: `B_sem_match_tiny_detalhado`
- Próximo passo: Buscar alias/cadastro no Tiny usando SKU Shopify como pista; se não existir, decidir cadastro/codigo Tiny antes de sourcing.

### 14. Camiseta Pace Buero Washed Black Preto
- Shopify variant: `47967340331230`
- Tamanho: `S/P`
- SKU Shopify atual: `PAC-1197278-S`
- Sinal 30d: pedidos `1`, receita `R$ 319.99`
- Classificação: `B_sem_match_tiny_detalhado`
- Próximo passo: Buscar alias/cadastro no Tiny usando SKU Shopify como pista; se não existir, decidir cadastro/codigo Tiny antes de sourcing.

### 15. Camiseta Pace Patavision Off White
- Shopify variant: `47019093295326`
- Tamanho: `P/S`
- SKU Shopify atual: `PAC-5857246-S`
- Sinal 30d: pedidos `1`, receita `R$ 209.99`
- Classificação: `B_sem_match_tiny_detalhado`
- Próximo passo: Buscar alias/cadastro no Tiny usando SKU Shopify como pista; se não existir, decidir cadastro/codigo Tiny antes de sourcing.

## Regra de execução
- Antes de qualquer write, gerar preview linha a linha com: produto, variant ID, SKU atual, codigo Tiny alvo, fonte da decisão e rollback.
- Se a correção for em Tiny, aprovação precisa escopo explícito para Tiny.
- Se a correção for em Shopify, aprovação precisa escopo explícito SKU-only Shopify.

## O que não fiz
- Não escrevi Shopify/Tiny.
- Não fiz compra/sourcing/reposição.
- Não alterei preço, estoque, cadastro público, campanha ou cliente.
