# Gate B2 — Preview de lote P0 para saneamento SKU/Tiny/Shopify (20260610T112421Z)

## Escopo
- Pedido: Lucas respondeu `Seguir` após a fila P0/P1 de saneamento Gate B2.
- Interpretação segura: preparar o lote P0 com evidência e opções de aprovação; não corrigir Tiny/Shopify e não ativar runtime.
- Fonte: artefatos locais/read-only do Gate B2. A base local é índice operacional, não fonte final de disponibilidade.

## Resultado do lote
- Handles P0: 9
- Linhas SKU/tamanho bloqueadas no lote: 84
- shopify_variant_tiny_missing: 7
- tiny_duplicate_exact_code_blocked: 11
- shopify_duplicate_sku_blocked: 66
- Tiny write: 0
- Shopify write: 0
- Contato externo/fornecedor/cliente: 0
- Cron/webhook/runtime novo: 0

## Handles P0 e ação segura proposta
1. `slipper-alo-yoga-recovery-saddle-ivory-bege`
   - Produto: Slipper Alo Yoga Recovery Saddle/Ivory Bege
   - Bloqueios: 12 linhas / 12 SKUs
   - Tipos: {'shopify_duplicate_sku_blocked': 11, 'shopify_variant_tiny_missing': 1}
   - SKUs: a0827u, a0827u-1, a0827u-10, a0827u-11, a0827u-2, a0827u-3, a0827u-4, a0827u-5, a0827u-6, a0827u-7, a0827u-8, a0827u-9
   - Dono sugerido: lk-shopify + lk-stock
   - Próxima ação segura: Revisar grade/variants Shopify e definir SKU único por tamanho; checar se o SKU base sem sufixo é variante real ou duplicidade herdada; depois reconfirmar Tiny por código exato.
   - Disponibilidade: bloqueada até saneamento + readback Tiny oficial.
2. `tenis-asics-gel-1130-black-pure-silver-prata`
   - Produto: Tênis ASICS Gel-1130 Black Pure Silver Prata
   - Bloqueios: 12 linhas / 12 SKUs
   - Tipos: {'shopify_duplicate_sku_blocked': 11, 'shopify_variant_tiny_missing': 1}
   - SKUs: 1201A906-001, 1201A906-001-34, 1201A906-001-35, 1201A906-001-36, 1201A906-001-37, 1201A906-001-38, 1201A906-001-39, 1201A906-001-40, 1201A906-001-41, 1201A906-001-42, 1201A906-001-43, 1201A906-001-44
   - Dono sugerido: lk-shopify + lk-stock
   - Próxima ação segura: Revisar grade/variants Shopify e definir SKU único por tamanho; checar se o SKU base sem sufixo é variante real ou duplicidade herdada; depois reconfirmar Tiny por código exato.
   - Disponibilidade: bloqueada até saneamento + readback Tiny oficial.
3. `tenis-asics-gel-1130-white-black-silver-prata`
   - Produto: Tênis ASICS Gel-1130 White Black Silver Prata
   - Bloqueios: 12 linhas / 12 SKUs
   - Tipos: {'shopify_duplicate_sku_blocked': 11, 'shopify_variant_tiny_missing': 1}
   - SKUs: 1201A933-100, 1201A933-100-34, 1201A933-100-35, 1201A933-100-36, 1201A933-100-37, 1201A933-100-38, 1201A933-100-39, 1201A933-100-40, 1201A933-100-41, 1201A933-100-42, 1201A933-100-43, 1201A933-100-44
   - Dono sugerido: lk-shopify + lk-stock
   - Próxima ação segura: Revisar grade/variants Shopify e definir SKU único por tamanho; checar se o SKU base sem sufixo é variante real ou duplicidade herdada; depois reconfirmar Tiny por código exato.
   - Disponibilidade: bloqueada até saneamento + readback Tiny oficial.
4. `tenis-jordan-4-retro-toro-bravo-2026-vermelho`
   - Produto: Tênis Jordan 4 Retro Toro Bravo 2026 Vermelho
   - Bloqueios: 12 linhas / 12 SKUs
   - Tipos: {'shopify_duplicate_sku_blocked': 11, 'shopify_variant_tiny_missing': 1}
   - SKUs: FQ8138-600, FQ8138-600-34, FQ8138-600-35, FQ8138-600-36, FQ8138-600-37, FQ8138-600-38, FQ8138-600-39, FQ8138-600-40, FQ8138-600-41, FQ8138-600-42, FQ8138-600-43, FQ8138-600-44
   - Dono sugerido: lk-shopify + lk-stock
   - Próxima ação segura: Revisar grade/variants Shopify e definir SKU único por tamanho; checar se o SKU base sem sufixo é variante real ou duplicidade herdada; depois reconfirmar Tiny por código exato.
   - Disponibilidade: bloqueada até saneamento + readback Tiny oficial.
5. `tenis-new-balance-204l-grey-matter-shipyard-cinza`
   - Produto: Tênis New Balance 204L Grey Matter Shipyard Cinza
   - Bloqueios: 12 linhas / 12 SKUs
   - Tipos: {'shopify_duplicate_sku_blocked': 11, 'shopify_variant_tiny_missing': 1}
   - SKUs: U204L86W, U204L86W-1, U204L86W-10, U204L86W-11, U204L86W-2, U204L86W-3, U204L86W-4, U204L86W-5, U204L86W-6, U204L86W-7, U204L86W-8, U204L86W-9
   - Dono sugerido: lk-shopify + lk-stock
   - Próxima ação segura: Revisar grade/variants Shopify e definir SKU único por tamanho; checar se o SKU base sem sufixo é variante real ou duplicidade herdada; depois reconfirmar Tiny por código exato.
   - Disponibilidade: bloqueada até saneamento + readback Tiny oficial.
6. `tenis-air-jordan-1-low-og-year-of-snake-2025-cinza`
   - Produto: Tênis Nike Air Jordan 1 Low Og Year of Snake 2025 Cinza
   - Bloqueios: 11 linhas / 11 SKUs
   - Tipos: {'shopify_duplicate_sku_blocked': 11}
   - SKUs: HF3144 100-1, HF3144 100-10, HF3144 100-11, HF3144 100-2, HF3144 100-3, HF3144 100-4, HF3144 100-5, HF3144 100-6, HF3144 100-7, HF3144 100-8, HF3144 100-9
   - Dono sugerido: lk-shopify + lk-stock
   - Próxima ação segura: Revisar grade/variants Shopify e definir SKU único por tamanho; checar se o SKU base sem sufixo é variante real ou duplicidade herdada; depois reconfirmar Tiny por código exato.
   - Disponibilidade: bloqueada até saneamento + readback Tiny oficial.
7. `air-jordan-1-low-true-blue`
   - Produto: Tênis Nike Air Jordan 1 Low True Blue Azul
   - Bloqueios: 5 linhas / 5 SKUs
   - Tipos: {'tiny_duplicate_exact_code_blocked': 5}
   - SKUs: 553560412-2, 553560412-3, 553560412-4, 553560412-5, 553560412-6
   - Dono sugerido: lk-stock/Tiny ops
   - Próxima ação segura: Resolver duplicidade de código exato no Tiny antes de liberar disponibilidade; escolher item canônico e manter os duplicados bloqueados até saneamento.
   - Disponibilidade: bloqueada até saneamento + readback Tiny oficial.
8. `nike-dunk-low-pink-red-white`
   - Produto: Tênis Nike Dunk Low Pink Red White Rosa
   - Bloqueios: 4 linhas / 4 SKUs
   - Tipos: {'shopify_variant_tiny_missing': 1, 'tiny_duplicate_exact_code_blocked': 3}
   - SKUs: CW1588601-4, CW1590-601-1, CW1590-601-3, CW1590-601-5
   - Dono sugerido: lk-stock/Tiny ops
   - Próxima ação segura: Resolver duplicidade de código exato no Tiny antes de liberar disponibilidade; escolher item canônico e manter os duplicados bloqueados até saneamento.
   - Disponibilidade: bloqueada até saneamento + readback Tiny oficial.
9. `tenis-adidas-handball-spezial-sporty-rich-brown-marrom`
   - Produto: Tênis adidas Handball Spezial Sporty & Rich Brown Marrom
   - Bloqueios: 4 linhas / 4 SKUs
   - Tipos: {'shopify_variant_tiny_missing': 1, 'tiny_duplicate_exact_code_blocked': 3}
   - SKUs: IH2612, IH2612-10, IH2612-2, IH2612-8
   - Dono sugerido: lk-stock/Tiny ops
   - Próxima ação segura: Resolver duplicidade de código exato no Tiny antes de liberar disponibilidade; escolher item canônico e manter os duplicados bloqueados até saneamento.
   - Disponibilidade: bloqueada até saneamento + readback Tiny oficial.

## Opções de aprovação
A. Autorizar investigação read-only ao vivo Shopify/Tiny dos 9 handles P0 para montar candidatos canônicos por SKU/tamanho.
B. Não investigar ao vivo; gerar checklist manual para equipe operar no admin/Tiny.
C. Escolher só 1 handle P0 para piloto antes dos demais.

## Fora de escopo sem nova aprovação
- Corrigir Tiny ou Shopify.
- Deduplicar SKU automaticamente.
- Prometer disponibilidade/pronta entrega.
- Compra, transferência, reserva, campanha, cliente, fornecedor.
- Cron/webhook/gateway/bot novo.

## Kill criteria
- Divergência entre Shopify/Tiny que não permita candidato único por tamanho.
- Duplicidade Tiny exata sem item canônico claro.
- Falha ou rate limit de fonte viva durante investigação read-only.
- Qualquer necessidade de write externo.

## Rollback
- Nenhum write externo foi feito. Para rollback local, descartar estes artefatos e voltar à fila P0/P1 de 20260610T105900Z.

## Artefatos
- JSON: `areas/lk/sub-areas/stock/reports/gate-b2-sku-saneamento-p0-batch-packet-20260610T112421Z.json`
- CSV: `areas/lk/sub-areas/stock/reports/gate-b2-sku-saneamento-p0-batch-issues-20260610T112421Z.csv`
