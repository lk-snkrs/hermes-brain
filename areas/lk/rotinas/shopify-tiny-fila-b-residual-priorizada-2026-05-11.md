# LK — Fila B residual priorizada para revisão manual

Data: 2026-05-11

## Veredito

Depois de classificar os 1.282 residuais, cruzei com a Fila B/estoque-venda já existente para decidir o que revisar primeiro antes de gerar nova Fila A. Esta etapa é read-only e não faz write em Shopify/Tiny.

## Resumo

- total_residual: **1282**
- ambiguous_total: **51**
- sem_sku_no_safe_total: **374**
- com_sku_no_safe_total: **857**
- matched_existing_stock_queue: **15**

## Sequência segura

1. **P0**: linhas residuais que já aparecem na fila de venda/ruptura existente — resolver antes de qualquer sourcing.
2. **P1**: todos os 51 casos ambíguos por título+tamanho — volume pequeno e exige decisão humana entre 2–3 candidatos.
3. **P2**: top 100 sem SKU Shopify e sem match Tiny seguro — cadastro precisa de SKU canônico.
4. **P3**: top 100 com SKU Shopify mas sem Tiny seguro — separar SKU temporário, produto fora do Tiny ou grafia diferente.

## P0 — aparece também na fila B/estoque-venda
- Camiseta Pace Cotton Code Branca — tamanho `G/L` — SKU `[sem SKU]` — pedidos sinal: 2, receita sinal: R$ 433.98 — no_safe_tiny_match_sem_sku
- Camiseta Aimé Leon Dore Musician Graphic Off White — tamanho `S/P` — SKU `[sem SKU]` — pedidos sinal: 1, receita sinal: R$ 1,299.99 — no_safe_tiny_match_sem_sku
- Rhode Pocket Blush — tamanho `Sleepy Girl - Soft Mauve` — SKU `[sem SKU]` — pedidos sinal: 1, receita sinal: R$ 399.99 — no_safe_tiny_match_sem_sku
- Camiseta Pace Cotton Code Preta — tamanho `G/L` — SKU `[sem SKU]` — pedidos sinal: 1, receita sinal: R$ 216.99 — no_safe_tiny_match_sem_sku
- Camiseta Pace Sketch Yourself Off White — tamanho `P/S` — SKU `[sem SKU]` — pedidos sinal: 1, receita sinal: R$ 209.99 — no_safe_tiny_match_sem_sku
- Tênis New Balance 204L Cortado Marrom — tamanho `39` — SKU `NB-0254942-39` — pedidos sinal: 2, receita sinal: R$ 5,599.98 — no_safe_tiny_match_com_sku
- Tênis Nike x Skims Rift Mesh Archaeo Brown Marrom — tamanho `36` — SKU `NKS-1065310-36` — pedidos sinal: 1, receita sinal: R$ 3,499.99 — no_safe_tiny_match_com_sku
- Tênis Nike Mind 002 Light Khaki Bege — tamanho `41` — SKU `NKE-9054174-41` — pedidos sinal: 1, receita sinal: R$ 3,199.99 — no_safe_tiny_match_com_sku
- Tênis Onitsuka Tiger Mexico 66 Fringe Mocha Brown/Dark Brown Marrom — tamanho `42.5` — SKU `ONI-0995678-425` — pedidos sinal: 1, receita sinal: R$ 2,999.99 — no_safe_tiny_match_com_sku
- Tênis New Balance 204L Cortado Marrom — tamanho `37` — SKU `NB-0254942-37` — pedidos sinal: 1, receita sinal: R$ 2,799.99 — no_safe_tiny_match_com_sku
- Tênis Onitsuka Tiger Mexico 66 Sabot Pure Silver Cream Cinza — tamanho `38` — SKU `ONI-6772830-38` — pedidos sinal: 1, receita sinal: R$ 2,199.99 — no_safe_tiny_match_com_sku
- Moletom Alo Yoga Cropped Serenity Coverup Black Preto — tamanho `S/P` — SKU `ALO-8506462-S` — pedidos sinal: 1, receita sinal: R$ 1,799.99 — no_safe_tiny_match_com_sku
- Calça Saint Studio Alfaiataria Leve Prega Dupla Cinza — tamanho `L/G` — SKU `SST-4542302-L` — pedidos sinal: 1, receita sinal: R$ 619.99 — no_safe_tiny_match_com_sku
- Camiseta Pace Buero Washed Black Preto — tamanho `S/P` — SKU `PAC-1197278-S` — pedidos sinal: 1, receita sinal: R$ 319.99 — no_safe_tiny_match_com_sku
- Camiseta Pace Patavision Off White — tamanho `P/S` — SKU `PAC-5857246-S` — pedidos sinal: 1, receita sinal: R$ 209.99 — no_safe_tiny_match_com_sku

## P1 — 51 ambíguos para decisão manual
- Calça Alo Yoga Airlift High-Waist 7/8 Line Up Legging Black Preto — tamanho `M/M` — SKU `[sem SKU]` — candidatos: 2
- Camiseta Aimé Leon Dore Unisphere Preto — tamanho `Jet Black / S/P` — SKU `[sem SKU]` — candidatos: 2
- Camiseta Aimé Leon Dore Unisphere Preto — tamanho `Jet Black / M` — SKU `[sem SKU]` — candidatos: 2
- Camiseta Aimé Leon Dore Unisphere Preto — tamanho `Jet Black / L/G` — SKU `[sem SKU]` — candidatos: 2
- Camiseta Aimé Leon Dore Unisphere Preto — tamanho `Jet Black / XL/GG` — SKU `[sem SKU]` — candidatos: 2
- Camiseta Aimé Leon Dore Unisphere Preto — tamanho `Botanical Green / S/P` — SKU `[sem SKU]` — candidatos: 2
- Camiseta Aimé Leon Dore Unisphere Preto — tamanho `Botanical Green / M` — SKU `[sem SKU]` — candidatos: 2
- Camiseta Aimé Leon Dore Unisphere Preto — tamanho `Botanical Green / L/G` — SKU `[sem SKU]` — candidatos: 2
- Camiseta Aimé Leon Dore Unisphere Preto — tamanho `Botanical Green / XL/GG` — SKU `[sem SKU]` — candidatos: 2
- Tênis Adidas Response CL x Bad Bunny Wonder Branco — tamanho `34` — SKU `[sem SKU]` — candidatos: 2
- Tênis Adidas Response CL x Bad Bunny Wonder Branco — tamanho `36` — SKU `[sem SKU]` — candidatos: 3
- Tênis Adidas Response CL x Bad Bunny Wonder Branco — tamanho `38` — SKU `[sem SKU]` — candidatos: 3
- Tênis Adidas Response CL x Bad Bunny Wonder Branco — tamanho `40` — SKU `[sem SKU]` — candidatos: 3
- Tênis Adidas Response CL x Bad Bunny Wonder Branco — tamanho `43` — SKU `[sem SKU]` — candidatos: 2
- Tênis Adidas Response CL x Bad Bunny Wonder Branco — tamanho `44` — SKU `[sem SKU]` — candidatos: 2
- Tênis Adidas Samba OG White Scarlet Branco — tamanho `34` — SKU `[sem SKU]` — candidatos: 2
- Tênis Adidas Samba OG White Scarlet Branco — tamanho `36` — SKU `[sem SKU]` — candidatos: 2
- Tênis New Balance 204L Arid Timberwolf Bege — tamanho `37.5` — SKU `[sem SKU]` — candidatos: 2
- Tênis New Balance 530 Brown Tan Marrom — tamanho `37` — SKU `[sem SKU]` — candidatos: 2
- Tênis New Balance 9060 Black Magnet Preto — tamanho `39.5` — SKU `[sem SKU]` — candidatos: 2
- Tênis Nike Air Jordan 1 Elevate Low SE Lucky Green Verde — tamanho `35.5` — SKU `[sem SKU]` — candidatos: 2
- Tênis Nike Air Jordan 1 Low "Eastside Golf" Azul Marinho — tamanho `41` — SKU `[sem SKU]` — candidatos: 3
- Tênis Nike Air Jordan 1 Low "Eastside Golf" Azul Marinho — tamanho `43` — SKU `[sem SKU]` — candidatos: 3
- Tênis Nike Air Jordan 1 Low "Multicolor Sashiko" Colorido — tamanho `35.5` — SKU `[sem SKU]` — candidatos: 2
- Tênis Nike Air Jordan 1 Low OG Obsidian UNC Azul — tamanho `42.5` — SKU `[sem SKU]` — candidatos: 2
- Tênis Nike Air Jordan 1 Low SE Diamond Preto — tamanho `46` — SKU `[sem SKU]` — candidatos: 2
- Tênis Nike Air Jordan 1 Mid SE Space Jam Preto ou — tamanho `36` — SKU `[sem SKU]` — candidatos: 3
- Tênis Nike Air Jordan 1 Mid Tropical Twist Igloo (GS) Verde — tamanho `36` — SKU `[sem SKU]` — candidatos: 2
- Tênis Nike Air Jordan 1 Mid Tropical Twist Igloo (GS) Verde — tamanho `37` — SKU `[sem SKU]` — candidatos: 2
- Tênis Nike Air Jordan 1 Mid Tropical Twist Igloo (GS) Verde — tamanho `38` — SKU `[sem SKU]` — candidatos: 2
- Tênis Nike Air Jordan 1 Retro High Rare Air Sail Cinnabar Bege — tamanho `35.5` — SKU `[sem SKU]` — candidatos: 2
- Tênis Nike Moon Shoe SP Jacquemus Alabaster Amarelo — tamanho `42.5` — SKU `[sem SKU]` — candidatos: 2
- Tênis Onitsuka Tiger Mexico 66 Kill Bill Amarelo — tamanho `36.5` — SKU `[sem SKU]` — candidatos: 2
- Tênis Onitsuka Tiger Mexico 66 Kill Bill Amarelo — tamanho `44` — SKU `[sem SKU]` — candidatos: 2
- Tênis Onitsuka Tiger Mexico 66 Sabot Cream Kale Bege — tamanho `36.5` — SKU `[sem SKU]` — candidatos: 2
- Tênis Onitsuka Tiger Mexico 66 SD Kill Bill Amarelo — tamanho `36.5` — SKU `[sem SKU]` — candidatos: 2
- Tênis Run The Jewels x Dunk Low SB '4/20' Azul — tamanho `38` — SKU `[sem SKU]` — candidatos: 2
- Tênis Run The Jewels x Dunk Low SB '4/20' Azul — tamanho `42.5` — SKU `[sem SKU]` — candidatos: 2
- Tênis Run The Jewels x Dunk Low SB '4/20' Azul — tamanho `43` — SKU `[sem SKU]` — candidatos: 2
- The Peptide Lip Tints Rhode Multicolor — tamanho `Short Cake` — SKU `[sem SKU]` — candidatos: 2
- Tênis Nike Air Jordan 1 Low Dark Grey Cinza — tamanho `34` — SKU `DC0774102` — candidatos: 2
- Tênis Nike Air Jordan 1 Low Dark Grey Cinza — tamanho `35` — SKU `DC0774102` — candidatos: 2
- Tênis Nike Air Jordan 1 Low Dark Grey Cinza — tamanho `36` — SKU `DC0774102` — candidatos: 2
- Tênis Nike Air Jordan 1 Low Dark Grey Cinza — tamanho `37` — SKU `DC0774102` — candidatos: 2
- Tênis Nike Air Jordan 1 Low Dark Grey Cinza — tamanho `39` — SKU `DC0774102` — candidatos: 2
- Tênis Nike Air Jordan 1 Low Dark Grey Cinza — tamanho `40` — SKU `DC0774102` — candidatos: 2
- Tênis Nike Air Jordan 1 Low Dark Grey Cinza — tamanho `41` — SKU `DC0774102` — candidatos: 2
- Tênis Nike Air Jordan 1 Low Dark Grey Cinza — tamanho `42` — SKU `DC0774102` — candidatos: 2
- Tênis Nike Air Jordan 1 Low Dark Grey Cinza — tamanho `42.5` — SKU `DC0774102` — candidatos: 2
- Tênis Nike Air Jordan 1 Low Dark Grey Cinza — tamanho `43` — SKU `DC0774102` — candidatos: 2
- Tênis Nike Air Jordan 1 Low Dark Grey Cinza — tamanho `44` — SKU `DC0774102` — candidatos: 2

## P2 — top sem SKU Shopify
- Camiseta Pace Cotton Code Branca — tamanho `G/L` — SKU `[sem SKU]`
- Camiseta Aimé Leon Dore Musician Graphic Off White — tamanho `S/P` — SKU `[sem SKU]`
- Rhode Pocket Blush — tamanho `Sleepy Girl - Soft Mauve` — SKU `[sem SKU]`
- Camiseta Pace Cotton Code Preta — tamanho `G/L` — SKU `[sem SKU]`
- Camiseta Pace Sketch Yourself Off White — tamanho `P/S` — SKU `[sem SKU]`
- Adidas Taekwondo Mei Ballet Preto e Branco — tamanho `34` — SKU `[sem SKU]`
- Adidas Taekwondo Mei Ballet Preto e Branco — tamanho `35` — SKU `[sem SKU]`
- Adidas Taekwondo Mei Ballet Preto e Branco — tamanho `36` — SKU `[sem SKU]`
- Adidas Taekwondo Mei Ballet Preto e Branco — tamanho `37` — SKU `[sem SKU]`
- Adidas Taekwondo Mei Ballet Preto e Branco — tamanho `38` — SKU `[sem SKU]`
- Adidas Taekwondo Mei Ballet Preto e Branco — tamanho `39` — SKU `[sem SKU]`
- Adidas Taekwondo Mei Ballet Preto e Branco — tamanho `40` — SKU `[sem SKU]`
- Adidas Taekwondo Mei Ballet Preto e Branco — tamanho `41` — SKU `[sem SKU]`
- Boné Aimé Leon Dore Micro Logo Lareul Oak Bege — tamanho `Default Title` — SKU `[sem SKU]`
- Boné Aimé Leon Dore Pigment Dyed Washed Cotton Bege — tamanho `Default Title` — SKU `[sem SKU]`
- Boné Aimé Leon Dore Pigment Dyed Washed Cotton Boné Plaza Taupe Bege — tamanho `Default Title` — SKU `[sem SKU]`
- Boné Aimé Leon Dore Saint George Logo Hat Bege/Marrom — tamanho `Default Title` — SKU `[sem SKU]`
- Boné Deus Ex Machina Classics Dad Hat Shield Standard Preto — tamanho `Default Title` — SKU `[sem SKU]`
- Boné Deus Ex Machina Records Dad Hat Strata Branco — tamanho `Default Title` — SKU `[sem SKU]`
- Boné Lululemon Classic Ball Tennis Crest Branco — tamanho `Default Title` — SKU `[sem SKU]`
- Boné Lululemon Structured Ball 1998 Branco — tamanho `Default Title` — SKU `[sem SKU]`
- Boné Lululemon Structured Ball Boné Collegiate Bege/Bordô — tamanho `Default Title` — SKU `[sem SKU]`
- Boné Lululemon Structured Classic Ball Script Green Verde — tamanho `Default Title` — SKU `[sem SKU]`
- Boné Nude Project Classique Preto — tamanho `Default Title` — SKU `[sem SKU]`
- Boné Nude Project New Varsity Cinza — tamanho `Default Title` — SKU `[sem SKU]`
- Boné Pace 6 Panel Vintage Stone Washed Preto — tamanho `Default Title` — SKU `[sem SKU]`
- Boné Pace 6 Panel Vintage Stone Washed Vermelho — tamanho `Default Title` — SKU `[sem SKU]`
- Boné Supreme x Weirdo Dave "Corduroy Camp Boné" Preto — tamanho `Default Title` — SKU `[sem SKU]`
- Boné Supreme x Weirdo Dave "Corduroy Camp Boné" Verde — tamanho `Default Title` — SKU `[sem SKU]`
- Calça Aphase Relaxed SweatPants - Stoned Black Preto — tamanho `G/L` — SKU `[sem SKU]`
- Calça Aphase Relaxed SweatPants - Stoned Black Preto — tamanho `GG/XL` — SKU `[sem SKU]`
- Calça Legging Alo Yoga 7/8 High-Waist Airlift Preto — tamanho `XS/PP` — SKU `[sem SKU]`
- Calça Legging Alo Yoga 7/8 High-Waist Airlift Preto — tamanho `S/P` — SKU `[sem SKU]`
- Calça Legging Alo Yoga 7/8 High-Waist Airlift Preto — tamanho `M/M` — SKU `[sem SKU]`
- Calça Legging Alo Yoga 7/8 High-Waist Airlift Preto — tamanho `L/G` — SKU `[sem SKU]`
- Calça Legging Alo Yoga 7/8 High-Waist Airlift Preto — tamanho `XL/GG` — SKU `[sem SKU]`
- Calça Nude Project Vinyl Chino Bege — tamanho `XS/PP` — SKU `[sem SKU]`
- Calça Nude Project Vinyl Chino Bege — tamanho `S/P` — SKU `[sem SKU]`
- Calça Nude Project Vinyl Chino Bege — tamanho `M/M` — SKU `[sem SKU]`
- Calça Nude Project Vinyl Chino Bege — tamanho `L/G` — SKU `[sem SKU]`

## P3 — top com SKU Shopify sem Tiny seguro
- Tênis New Balance 204L Cortado Marrom — tamanho `39` — SKU `NB-0254942-39`
- Tênis Nike x Skims Rift Mesh Archaeo Brown Marrom — tamanho `36` — SKU `NKS-1065310-36`
- Tênis Nike Mind 002 Light Khaki Bege — tamanho `41` — SKU `NKE-9054174-41`
- Tênis Onitsuka Tiger Mexico 66 Fringe Mocha Brown/Dark Brown Marrom — tamanho `42.5` — SKU `ONI-0995678-425`
- Tênis New Balance 204L Cortado Marrom — tamanho `37` — SKU `NB-0254942-37`
- Tênis Onitsuka Tiger Mexico 66 Sabot Pure Silver Cream Cinza — tamanho `38` — SKU `ONI-6772830-38`
- Moletom Alo Yoga Cropped Serenity Coverup Black Preto — tamanho `S/P` — SKU `ALO-8506462-S`
- Calça Saint Studio Alfaiataria Leve Prega Dupla Cinza — tamanho `L/G` — SKU `SST-4542302-L`
- Camiseta Pace Buero Washed Black Preto — tamanho `S/P` — SKU `PAC-1197278-S`
- Camiseta Pace Patavision Off White — tamanho `P/S` — SKU `PAC-5857246-S`
- Accolade Straight Leg Sweatpant - Charcoal Green verde — tamanho `S/P` — SKU `LK-5524446-S`
- Accolade Straight Leg Sweatpant - Charcoal Green verde — tamanho `XS/PP` — SKU `LK-5524446-XS`
- Accolade Straight Leg Sweatpant - Charcoal Green verde — tamanho `M/M` — SKU `LK-5524446-M`
- Accolade Straight Leg Sweatpant - Charcoal Green verde — tamanho `L/G` — SKU `LK-5524446-L`
- Accolade Straight Leg Sweatpant - Charcoal Green verde — tamanho `XL/GG` — SKU `LK-5524446-XL`
- Bolsa Pace Code Pro Leather Fold Bag Black — tamanho `Default Title` — SKU `PAC-3039582-OS`
- Boné Aimé Leon Dore Micro Logo Jet Black Preto — tamanho `Default Title` — SKU `ALD-8696798-OS`
- Boné Aime Leon Dore Washed Script Jet Black Preto — tamanho `Default Title` — SKU `ALD-3105758-OS`
- Boné Aime Leon Dore Washed Script Plaza Taupe Bege — tamanho `Default Title` — SKU `ALD-3072990-OS`
- Boné Alo Yoga Off-Duty Branco — tamanho `Default Title` — SKU `ALO-3137118-OS`
- Boné Alo Yoga Off-Duty Preto — tamanho `Default Title` — SKU `ALO-1465950-OS`
- Boné Aphase Connect - Stoned Black Preto — tamanho `Default Title` — SKU `APH-6956510-OS`
- Boné Aphase Twill Logo - Stoned Beige Bege — tamanho `Default Title` — SKU `APH-6989278-OS`
- Boné Kith Script Logo Classic Boné Nocturnal Branco/Azul — tamanho `Default Title` — SKU `KTH-4813662-OS`
- Boné Kith Script Logo Classic Boné Stadium Branco/Verde — tamanho `Default Title` — SKU `KTH-4846430-OS`
- Boné Lululemon Tennis Club Azul — tamanho `Default Title` — SKU `LLM-4879198-OS`
- Boné Lululemon Tennis Club Off White — tamanho `Default Title` — SKU `LLM-4911966-OS`
- Boné Nude Project New Varsity Bege — tamanho `Default Title` — SKU `NUD-9375070-OS`
- Calça Alo Yoga Accolade Straight Leg Gravel Bege — tamanho `XXS/PPP` — SKU `ALO-4485982-XXS`
- Calça Alo Yoga Accolade Straight Leg Gravel Bege — tamanho `XS/PP` — SKU `ALO-4485982-XS`
- Calça Alo Yoga Accolade Straight Leg Gravel Bege — tamanho `S/P` — SKU `ALO-4485982-S`
- Calça Alo Yoga Accolade Straight Leg Gravel Bege — tamanho `M/M` — SKU `ALO-4485982-M`
- Calça Alo Yoga Accolade Straight Leg Gravel Bege — tamanho `L/G` — SKU `ALO-4485982-L`
- Calça Alo Yoga Airbrush High-Waist Heart Throb Preto — tamanho `XS/PP` — SKU `ALO-9507806-XS`
- Calça Alo Yoga Airbrush High-Waist Heart Throb Preto — tamanho `S/P` — SKU `ALO-9507806-S`
- Calça Alo Yoga Airbrush High-Waist Heart Throb Preto — tamanho `M/M` — SKU `ALO-9507806-M`
- Calça Alo Yoga Airbrush High-Waist Heart Throb Preto — tamanho `L/G` — SKU `ALO-9507806-L`
- Calça Aphase Relaxed SweatPants - Stoned Beige Bege — tamanho `G/L` — SKU `APH-7284190-L`
- Calça Aphase Relaxed SweatPants - Stoned Beige Bege — tamanho `GG/XL` — SKU `APH-7284190-XL`
- Calça Pace Milli Cargo Azul Marinho — tamanho `38` — SKU `PAC-8544990-38`

## Próxima ação

Fazer lookup manual/read-only aprofundado primeiro nos P0/P1, preparando um preview de correção/mapeamento. Qualquer write SKU-only ou ajuste Tiny/Shopify continua exigindo preview + aprovação explícita do Lucas.
