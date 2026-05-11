# LK — Fila B residual após saneamento Shopify SKU→Tiny

Data: 2026-05-11
Fonte: `reports/lk-shopify-tiny-all-sku-normalization-execution-2026-05-11.json`

## Veredito

Os 505 SKUs divergentes seguros já foram corrigidos e verificados live. Esta rotina classifica os **1.282 variants pulados por segurança** para a próxima etapa da Fila B. Não houve write novo nesta etapa.

## Guardrails

- Shopify continua fonte de catálogo/venda; Tiny `LK | CONTROLE ESTOQUE` continua fonte de SKU/estoque.
- Não usar item residual para compra, reposição ou sourcing automático sem SKU Tiny confirmado.
- Esta etapa foi read-only sobre relatórios já gerados: sem Shopify write, sem Tiny write, sem preço/estoque/título/campanha/cliente.

## Números

- Total residual: **1282 variants**
- Sem SKU atual na Shopify: **414**
- Com SKU atual na Shopify, mas sem match Tiny seguro: **868**
- `no_safe_tiny_match`: **1231**
- `ambiguous_title_size`: **51**

## Buckets operacionais

- **no_safe_tiny_match_com_sku** — 857: SKU Shopify existe, mas não bateu com Tiny de forma segura
- **no_safe_tiny_match_sem_sku** — 374: Variant Shopify sem SKU e sem match Tiny seguro
- **ambiguous_title_size_sem_sku** — 40: Variant sem SKU com 2–3 candidatos Tiny por título+tamanho
- **ambiguous_title_size_com_sku** — 11: Variant com SKU e ambiguidade por título+tamanho

## Prioridade recomendada

1. Resolver primeiro as **51 linhas ambíguas**: volume pequeno, alta chance de destravar manualmente sem mexer em preço/estoque.
2. Em seguida, revisar as **374 variants sem SKU Shopify**: exigem SKU canônico antes de qualquer decisão comercial.
3. Depois, revisar as **857 variants com SKU Shopify sem match Tiny seguro**: separar SKU temporário LK, produto fora do Tiny, acessório/apparel e casos de grafia diferente no Tiny.
4. Só então gerar nova Fila A de sourcing/reposição com produto + SKU + tamanho + fonte + confiança.

## Top grupos por volume residual

- Tênis: 520
- Camiseta: 258
- Moletom: 151
- Calça: 72
- Tenis: 44
- Pop: 30
- Boné: 28
- Camisa: 25
- Top: 24
- Jaqueta: 19
- Shorts: 18
- Sapato: 13
- Regata: 11
- Onitsuka: 9
- Rhode: 9
- Sapatilha: 9
- Adidas: 8
- Accolade: 5
- Define: 5
- Polo: 5

## Top produtos com mais variants residuais

- Tênis Onitsuka Tiger x Versace TAI-CHI Sakura Metallic Têniss Silver Gold Prateado: 16
- Tênis Onitsuka Tiger x Versace TAI-CHI Sakura Nappa Têniss Black Brown Preto: 16
- Tênis Onitsuka Tiger x Versace TAI-CHI Sakura Nappa Têniss Brown Yellow Amarelo: 16
- Tênis Onitsuka Tiger x Versace TAI-CHI Sakura Suede Têniss Blue Azul: 16
- Tênis Onitsuka Tiger x Versace TAI-CHI Sakura Suede Têniss Green: 16
- Tênis Nike Air Jordan 4 Retro OG SP Brick By Brick Camurça Firewood Vermelho: 13
- Tênis Nike Mind 002 Light Khaki Bege: 13
- Tênis Onitsuka Tiger Mexico 66 Fringe Mocha Brown/Dark Brown Marrom: 13
- Tênis Onitsuka Tiger Mexico 66 Fringe Yellow/Black Amarelo: 13
- Camiseta Deus Ex Machina Shield Standard: 12
- Tênis Adidas Yeezy Boost 350 V2 Earth Marrom: 12
- Tênis Nike Air Jordan 1 Retro High OG SP Union LA Chicago Shadow: 12
- Tênis On Running Cloudtilt 'Black Ivory' Branco: 12
- Tênis Onitsuka Tiger Moage Co Oyster Grey/Feather Grey Cinza: 12
- Tênis Alo Yoga Alo Runner Pink Rosa: 11
- Tênis ASICS Gel-NYC Graphite Grey Black Preto: 11
- Tênis New Balance 204L Basketcase Beef & Broccoli Marrom: 11
- Tênis New Balance 204L Cortado Marrom: 11
- Tênis New Balance 204L Silver Metallic Double Bubble Prateado: 11
- Tênis New Balance 204L Silver Metallic Electric Indigo YKK Prateado: 11
- Tênis New Balance 204L Slate Grey Raincloud Cinza: 11
- Tênis New Balance 204L x Atmos Cow Girl Brown Marrom: 11
- Tênis New Balance 204L Year of the Horse Tan Verde: 11
- Tênis New Balance 204L Year of the Horse White Bege: 11
- Tênis New Balance 990v6 Made in USA 'Triple Black': 11

## Amostras por bucket

### no_safe_tiny_match_com_sku (857)
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

### no_safe_tiny_match_sem_sku (374)
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

### ambiguous_title_size_sem_sku (40)
- Calça Alo Yoga Airlift High-Waist 7/8 Line Up Legging Black Preto — tamanho `M/M` — SKU `[sem SKU]`; candidatos=2
- Camiseta Aimé Leon Dore Unisphere Preto — tamanho `Jet Black / S/P` — SKU `[sem SKU]`; candidatos=2
- Camiseta Aimé Leon Dore Unisphere Preto — tamanho `Jet Black / M` — SKU `[sem SKU]`; candidatos=2
- Camiseta Aimé Leon Dore Unisphere Preto — tamanho `Jet Black / L/G` — SKU `[sem SKU]`; candidatos=2
- Camiseta Aimé Leon Dore Unisphere Preto — tamanho `Jet Black / XL/GG` — SKU `[sem SKU]`; candidatos=2
- Camiseta Aimé Leon Dore Unisphere Preto — tamanho `Botanical Green / S/P` — SKU `[sem SKU]`; candidatos=2
- Camiseta Aimé Leon Dore Unisphere Preto — tamanho `Botanical Green / M` — SKU `[sem SKU]`; candidatos=2
- Camiseta Aimé Leon Dore Unisphere Preto — tamanho `Botanical Green / L/G` — SKU `[sem SKU]`; candidatos=2
- Camiseta Aimé Leon Dore Unisphere Preto — tamanho `Botanical Green / XL/GG` — SKU `[sem SKU]`; candidatos=2
- Tênis Adidas Response CL x Bad Bunny Wonder Branco — tamanho `34` — SKU `[sem SKU]`; candidatos=2

### ambiguous_title_size_com_sku (11)
- Tênis Nike Air Jordan 1 Low Dark Grey Cinza — tamanho `34` — SKU `DC0774102`; candidatos=2
- Tênis Nike Air Jordan 1 Low Dark Grey Cinza — tamanho `35` — SKU `DC0774102`; candidatos=2
- Tênis Nike Air Jordan 1 Low Dark Grey Cinza — tamanho `36` — SKU `DC0774102`; candidatos=2
- Tênis Nike Air Jordan 1 Low Dark Grey Cinza — tamanho `37` — SKU `DC0774102`; candidatos=2
- Tênis Nike Air Jordan 1 Low Dark Grey Cinza — tamanho `39` — SKU `DC0774102`; candidatos=2
- Tênis Nike Air Jordan 1 Low Dark Grey Cinza — tamanho `40` — SKU `DC0774102`; candidatos=2
- Tênis Nike Air Jordan 1 Low Dark Grey Cinza — tamanho `41` — SKU `DC0774102`; candidatos=2
- Tênis Nike Air Jordan 1 Low Dark Grey Cinza — tamanho `42` — SKU `DC0774102`; candidatos=2
- Tênis Nike Air Jordan 1 Low Dark Grey Cinza — tamanho `42.5` — SKU `DC0774102`; candidatos=2
- Tênis Nike Air Jordan 1 Low Dark Grey Cinza — tamanho `43` — SKU `DC0774102`; candidatos=2

## Próximo bloco seguro

Gerar uma fila curta de revisão manual dos 51 ambíguos e uma fila priorizada das 374 variants sem SKU, cruzando com venda/ruptura antes de qualquer nova sugestão comercial. Writes em Shopify/Tiny continuam dependendo de preview + aprovação explícita.
