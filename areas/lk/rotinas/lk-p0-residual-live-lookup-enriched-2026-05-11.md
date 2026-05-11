# LK — P0 residual live lookup Shopify/Tiny enriquecido

Data: 2026-05-11T12:00:54

## Veredito
Aprofundei os 15 P0 residuais em modo read-only contra Shopify atual + busca/detalhe Tiny. Não há nenhuma linha segura para SKU-only automático agora, porque nenhuma retornou candidato Tiny único com `codigo` canônico preenchido.

## Resumo
- Total P0 verificado: 15
- Candidato Tiny único com código: 0
- Match de tamanho no Tiny, mas sem código ou ambíguo: 6
- Sem match de tamanho Tiny nos detalhes consultados: 9

## Resultado P0
- Camiseta Pace Cotton Code Branca — tamanho `G/L` — Shopify SKU `[sem SKU]` — match Tiny tamanho: 6 — [sem código] — Tamanho: G/L; [sem código] — Tamanho: GG/XL; [sem código] — Tamanho: G/L — status: `candidate_size_match_but_code_missing_or_ambiguous`
- Camiseta Aimé Leon Dore Musician Graphic Off White — tamanho `S/P` — Shopify SKU `[sem SKU]` — match Tiny tamanho: 0 — sem match de tamanho nos detalhes Tiny consultados — status: `no_tiny_size_match_found`
- Rhode Pocket Blush — tamanho `Sleepy Girl - Soft Mauve` — Shopify SKU `[sem SKU]` — match Tiny tamanho: 1 — [sem código] — Cor: Sleepy Girl - Soft Mauve — status: `candidate_size_match_but_code_missing_or_ambiguous`
- Camiseta Pace Cotton Code Preta — tamanho `G/L` — Shopify SKU `[sem SKU]` — match Tiny tamanho: 6 — [sem código] — Tamanho: G/L; [sem código] — Tamanho: GG/XL; [sem código] — Tamanho: G/L — status: `candidate_size_match_but_code_missing_or_ambiguous`
- Camiseta Pace Sketch Yourself Off White — tamanho `P/S` — Shopify SKU `[sem SKU]` — match Tiny tamanho: 6 — [sem código] — Tamanho: P/S; [sem código] — Tamanho: P/S; [sem código] — Camiseta Pace Sketch Yourself Off White - P-S — status: `candidate_size_match_but_code_missing_or_ambiguous`
- Tênis New Balance 204L Cortado Marrom — tamanho `39` — Shopify SKU `NB-0254942-39` — match Tiny tamanho: 1 — [sem código] — Tamanho do calçado: 39 — status: `candidate_size_match_but_code_missing_or_ambiguous`
- Tênis Nike x Skims Rift Mesh Archaeo Brown Marrom — tamanho `36` — Shopify SKU `NKS-1065310-36` — match Tiny tamanho: 2 — [sem código] — Tamanho do calçado: 36; [sem código] — Tênis Nike x Skims Rift Mesh Archaeo Brown Marrom - 36 — status: `candidate_size_match_but_code_missing_or_ambiguous`
- Tênis Nike Mind 002 Light Khaki Bege — tamanho `41` — Shopify SKU `NKE-9054174-41` — match Tiny tamanho: 0 — sem match de tamanho nos detalhes Tiny consultados — status: `no_tiny_size_match_found`
- Tênis Onitsuka Tiger Mexico 66 Fringe Mocha Brown/Dark Brown Marrom — tamanho `42.5` — Shopify SKU `ONI-0995678-425` — match Tiny tamanho: 0 — sem match de tamanho nos detalhes Tiny consultados — status: `no_tiny_size_match_found`
- Tênis New Balance 204L Cortado Marrom — tamanho `37` — Shopify SKU `NB-0254942-37` — match Tiny tamanho: 0 — sem match de tamanho nos detalhes Tiny consultados — status: `no_tiny_size_match_found`
- Tênis Onitsuka Tiger Mexico 66 Sabot Pure Silver Cream Cinza — tamanho `38` — Shopify SKU `ONI-6772830-38` — match Tiny tamanho: 0 — sem match de tamanho nos detalhes Tiny consultados — status: `no_tiny_size_match_found`
- Moletom Alo Yoga Cropped Serenity Coverup Black Preto — tamanho `S/P` — Shopify SKU `ALO-8506462-S` — match Tiny tamanho: 0 — sem match de tamanho nos detalhes Tiny consultados — status: `no_tiny_size_match_found`
- Calça Saint Studio Alfaiataria Leve Prega Dupla Cinza — tamanho `L/G` — Shopify SKU `SST-4542302-L` — match Tiny tamanho: 0 — sem match de tamanho nos detalhes Tiny consultados — status: `no_tiny_size_match_found`
- Camiseta Pace Buero Washed Black Preto — tamanho `S/P` — Shopify SKU `PAC-1197278-S` — match Tiny tamanho: 0 — sem match de tamanho nos detalhes Tiny consultados — status: `no_tiny_size_match_found`
- Camiseta Pace Patavision Off White — tamanho `P/S` — Shopify SKU `PAC-5857246-S` — match Tiny tamanho: 0 — sem match de tamanho nos detalhes Tiny consultados — status: `no_tiny_size_match_found`

## Próxima ação segura
- Não gerar Fila A/sourcing automático para estes 15 até resolver SKU canônico.
- Para os 6 com match Tiny sem código/ambíguo: precisam de decisão/correção no Tiny ou confirmação humana antes de qualquer preview de write Shopify.
- Para os 9 sem match: precisam busca manual por alias/cadastro ou criação/normalização no Tiny antes de decisão comercial.

## O que não fiz
- Não escrevi no Shopify.
- Não escrevi no Tiny.
- Não alterei preço, estoque, produto, campanha ou envio.
