# Gate B2 — Decision packet pós-investigação live read-only P0 (20260610T113047Z)

## Escopo executado
- Gatilho: Lucas respondeu `Seguir` após preview do lote P0.
- Execução: consulta read-only Shopify Admin + Tiny API para os 9 handles P0, com artefatos locais.
- Não houve write Tiny/Shopify, compra, transferência, contato externo, cron, webhook, gateway ou bot novo.

## Resultado consolidado
- Handles investigados: 9
- Linhas live avaliadas: 74
- shopify_variant_tiny_missing: 6
- shopify_duplicate_sku_blocked: 58
- matched_exact_sku_stock_resolved: 6
- tiny_duplicate_exact_code_blocked: 4
- Linhas exatas resolvidas com depósito oficial Tiny: 6
- Observação: todas as linhas resolvidas no lote retornaram saldo `0.0` no depósito `LK | CONTROLE ESTOQUE`; isso é evidência interna, não promessa pública.

## Leitura operacional por handle
1. `slipper-alo-yoga-recovery-saddle-ivory-bege`
   - Produto: Slipper Alo Yoga Recovery Saddle/Ivory Bege
   - Status live: {'shopify_variant_tiny_missing': 1, 'shopify_duplicate_sku_blocked': 11}
   - Bloqueio dominante: duplicidade de SKU em variantes Shopify; precisa diff/rollback específico antes de qualquer correção.
   - Bloqueio missing: SKU Shopify sem código Tiny exato confirmado.
   - Disponibilidade pública/pronta entrega: bloqueada até saneamento e aprovação do fluxo de atendimento.
2. `tenis-asics-gel-1130-black-pure-silver-prata`
   - Produto: Tênis ASICS Gel-1130 Black Pure Silver Prata
   - Status live: {'shopify_variant_tiny_missing': 1, 'shopify_duplicate_sku_blocked': 11}
   - Bloqueio dominante: duplicidade de SKU em variantes Shopify; precisa diff/rollback específico antes de qualquer correção.
   - Bloqueio missing: SKU Shopify sem código Tiny exato confirmado.
   - Disponibilidade pública/pronta entrega: bloqueada até saneamento e aprovação do fluxo de atendimento.
3. `tenis-asics-gel-1130-white-black-silver-prata`
   - Produto: Tênis ASICS Gel-1130 White Black Silver Prata
   - Status live: {'shopify_variant_tiny_missing': 1, 'shopify_duplicate_sku_blocked': 11}
   - Bloqueio dominante: duplicidade de SKU em variantes Shopify; precisa diff/rollback específico antes de qualquer correção.
   - Bloqueio missing: SKU Shopify sem código Tiny exato confirmado.
   - Disponibilidade pública/pronta entrega: bloqueada até saneamento e aprovação do fluxo de atendimento.
4. `tenis-jordan-4-retro-toro-bravo-2026-vermelho`
   - Produto: Tênis Jordan 4 Retro Toro Bravo 2026 Vermelho
   - Status live: {'shopify_variant_tiny_missing': 1, 'shopify_duplicate_sku_blocked': 11, 'matched_exact_sku_stock_resolved': 2}
   - Resolvidos exatos: FQ8138-600-45 tamanho 45 saldo 0.0, FQ8138-600-46 tamanho 46 saldo 0.0
   - Bloqueio dominante: duplicidade de SKU em variantes Shopify; precisa diff/rollback específico antes de qualquer correção.
   - Bloqueio missing: SKU Shopify sem código Tiny exato confirmado.
   - Disponibilidade pública/pronta entrega: bloqueada até saneamento e aprovação do fluxo de atendimento.
5. `tenis-new-balance-204l-grey-matter-shipyard-cinza`
   - Produto: Tênis New Balance 204L Grey Matter Shipyard Cinza
   - Status live: {'shopify_variant_tiny_missing': 1, 'shopify_duplicate_sku_blocked': 11}
   - Bloqueio dominante: duplicidade de SKU em variantes Shopify; precisa diff/rollback específico antes de qualquer correção.
   - Bloqueio missing: SKU Shopify sem código Tiny exato confirmado.
   - Disponibilidade pública/pronta entrega: bloqueada até saneamento e aprovação do fluxo de atendimento.
6. `tenis-air-jordan-1-low-og-year-of-snake-2025-cinza`
   - Produto: Tênis Nike Air Jordan 1 Low Og Year of Snake 2025 Cinza
   - Status live: {'shopify_duplicate_sku_blocked': 3}
   - Bloqueio dominante: duplicidade de SKU em variantes Shopify; precisa diff/rollback específico antes de qualquer correção.
   - Disponibilidade pública/pronta entrega: bloqueada até saneamento e aprovação do fluxo de atendimento.
7. `air-jordan-1-low-true-blue`
   - Produto: Tênis Nike Air Jordan 1 Low True Blue Azul
   - Status live: {'tiny_duplicate_exact_code_blocked': 1}
   - Bloqueio Tiny: código exato duplicado no Tiny; precisa escolher item canônico antes de liberar.
   - Disponibilidade pública/pronta entrega: bloqueada até saneamento e aprovação do fluxo de atendimento.
8. `nike-dunk-low-pink-red-white`
   - Produto: Tênis Nike Dunk Low Pink Red White Rosa
   - Status live: {'matched_exact_sku_stock_resolved': 1}
   - Resolvidos exatos: CW1588601-4 tamanho 37 saldo 0.0
   - Disponibilidade pública/pronta entrega: bloqueada até saneamento e aprovação do fluxo de atendimento.
9. `tenis-adidas-handball-spezial-sporty-rich-brown-marrom`
   - Produto: Tênis adidas Handball Spezial Sporty & Rich Brown Marrom
   - Status live: {'shopify_variant_tiny_missing': 1, 'matched_exact_sku_stock_resolved': 3, 'tiny_duplicate_exact_code_blocked': 3}
   - Resolvidos exatos: IH2612-12 tamanho 34 saldo 0.0, IH2612-1 tamanho 35 saldo 0.0, IH2612-13 tamanho 38 saldo 0.0
   - Bloqueio Tiny: código exato duplicado no Tiny; precisa escolher item canônico antes de liberar.
   - Bloqueio missing: SKU Shopify sem código Tiny exato confirmado.
   - Disponibilidade pública/pronta entrega: bloqueada até saneamento e aprovação do fluxo de atendimento.

## Próximo gate recomendado
A. Preparar pacote de correção Shopify/Tiny por handle, começando pelos 5 handles com duplicidade Shopify dominante, com diff proposto e rollback — ainda sem executar write.
B. Preparar pacote Tiny-only para os códigos com `tiny_duplicate_exact_code_blocked`, escolhendo item canônico provável por saldo/depósito/nome — ainda sem executar write.
C. Registrar somente os 6 matches exatos resolvidos na base local Gate B como cache read-only e manter todo o resto bloqueado — sem write Tiny/Shopify.
D. Escolher 1 handle piloto para montar packet detalhado com candidatos de correção por tamanho.

## Fora de escopo sem nova aprovação
- Corrigir Tiny/Shopify.
- Deduplicar SKU automaticamente.
- Compra/transferência/reserva/cliente/fornecedor.
- Prometer disponibilidade pública.
- Criar cron/webhook/runtime novo.

## Artefatos
- JSON agregado: `areas/lk/sub-areas/stock/reports/gate-b2-p0-live-readonly-investigation-20260610T113047Z.json`
- CSV agregado: `areas/lk/sub-areas/stock/reports/gate-b2-p0-live-readonly-investigation-20260610T113047Z.csv`
- a0827u: `areas/lk/sub-areas/stock/reports/gate-b2-p0-live-readonly-a0827u-20260610T113047Z.json` / `areas/lk/sub-areas/stock/reports/gate-b2-p0-live-readonly-a0827u-20260610T113047Z.csv`
- 1201A906-001: `areas/lk/sub-areas/stock/reports/gate-b2-p0-live-readonly-1201A906-001-20260610T113047Z.json` / `areas/lk/sub-areas/stock/reports/gate-b2-p0-live-readonly-1201A906-001-20260610T113047Z.csv`
- 1201A933-100: `areas/lk/sub-areas/stock/reports/gate-b2-p0-live-readonly-1201A933-100-20260610T113047Z.json` / `areas/lk/sub-areas/stock/reports/gate-b2-p0-live-readonly-1201A933-100-20260610T113047Z.csv`
- FQ8138-600: `areas/lk/sub-areas/stock/reports/gate-b2-p0-live-readonly-FQ8138-600-20260610T113047Z.json` / `areas/lk/sub-areas/stock/reports/gate-b2-p0-live-readonly-FQ8138-600-20260610T113047Z.csv`
- U204L86W: `areas/lk/sub-areas/stock/reports/gate-b2-p0-live-readonly-U204L86W-20260610T113047Z.json` / `areas/lk/sub-areas/stock/reports/gate-b2-p0-live-readonly-U204L86W-20260610T113047Z.csv`
- HF3144 100-1: `areas/lk/sub-areas/stock/reports/gate-b2-p0-live-readonly-HF3144 100-1-20260610T113047Z.json` / `areas/lk/sub-areas/stock/reports/gate-b2-p0-live-readonly-HF3144 100-1-20260610T113047Z.csv`
- 553560412-2: `areas/lk/sub-areas/stock/reports/gate-b2-p0-live-readonly-553560412-2-20260610T113047Z.json` / `areas/lk/sub-areas/stock/reports/gate-b2-p0-live-readonly-553560412-2-20260610T113047Z.csv`
- CW1588601-4: `areas/lk/sub-areas/stock/reports/gate-b2-p0-live-readonly-CW1588601-4-20260610T113047Z.json` / `areas/lk/sub-areas/stock/reports/gate-b2-p0-live-readonly-CW1588601-4-20260610T113047Z.csv`
- IH2612: `areas/lk/sub-areas/stock/reports/gate-b2-p0-live-readonly-IH2612-20260610T113047Z.json` / `areas/lk/sub-areas/stock/reports/gate-b2-p0-live-readonly-IH2612-20260610T113047Z.csv`
