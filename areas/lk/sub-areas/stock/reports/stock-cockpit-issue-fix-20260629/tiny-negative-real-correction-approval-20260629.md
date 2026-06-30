# Tiny negativos — pacote de correção real

Data: 2026-06-29
Fonte: Tiny read-only exact SKU + Stock OS DB/Supabase latest snapshot
values_printed=false

## Resumo

- Negativos atuais no Cockpit/Supabase: `28`
- Candidatos com SKU exato no Tiny e controle ainda negativo: `9`
- Bloqueados sem match Tiny exato / match divergente: `19`

## Ação proposta para candidatos

Ajustar no Tiny o depósito `LK | CONTROLE ESTOQUE` para `0`, preservando readback antes/depois por SKU. Não alterar Shopify, preço, descrição, produto, cliente ou compra.

| SKU | Tamanho | Produto | Controle Tiny atual | Saldo total | Tiny id | Ação |
|---|---:|---|---:|---:|---:|---|
| `1183A872254-5` | `38` | Tênis Onitsuka Tiger Mexico 66 SD Beige Green Bege | `-1.0` | `0.0` | `1061569141` | set controle `0` |
| `300110` | `ÚNICO` | Jason Markk Essential Kit de Limpeza | `-5.0` | `32.0` | `1060840285` | set controle `0` |
| `APH-7120350-XL` | `GG/XL` | Camisa Aphase Check - Dark Blue Azul | `-1.0` | `0.0` | `1064645630` | set controle `0` |
| `1183C015101-6` | `39` | Tênis Onitsuka Tiger Mexico 66 SD Cream Birch Bege | `-1.0` | `1.0` | `1061569709` | set controle `0` |
| `L49205900-39` | `39` | Tênis Salomon XT-6 Vanilla Ice Oxford Tan Bege Bege | `-1.0` | `-1.0` | `1071546207` | set controle `0` |
| `DZ2795-200-4` | `37` | Tênis Nike Cortez Baroque Brown Marrom | `-1.0` | `-1.0` | `1063779796` | set controle `0` |
| `f99717` | `41` | Tênis Adidas Yeezy Boost 350 V2 Sesame Cinza | `-1.0` | `-1.0` | `1069539548` | set controle `0` |
| `ALO-8506462-S` | `S/P` | Moletom Alo Yoga Cropped Serenity Coverup Black Preto | `-1.0` | `-1.0` | `1069542767` | set controle `0` |
| `1183C015200-4` | `37` | Tênis Onitsuka Tiger Mexico 66 SD Birch Metropolis Bege | `-2.0` | `0.0` | `1061570172` | set controle `0` |

## Bloqueados

Estes não devem ser alterados automaticamente porque não há match Tiny exato pelo SKU atual, ou o Tiny retornou outro código. Precisam correção de SKU/cadastro antes.

| SKU | Tamanho | Produto | Motivo | Tiny código readback | Controle readback |
|---|---:|---|---|---|---:|
| `JQ6445-4` | `37` | Tênis Adidas Samba Jane 'Black White Gum' Preto | sem match Tiny exato | `—` | `None` |
| `JQ6446-3` | `36` | Tênis Adidas Samba Jane 'Scarlet Gum' Vermelho | sem match Tiny exato | `—` | `None` |
| `UNISPHERE` | `ÚNICO` | Boné 5 Panel Aimé Leon Dore Unisphere Branco | Tiny retornou código divergente | `ALD-4108254-M` | `2.0` |
| `JI2734-7` | `40` | Tênis adidas Samba Og Preloved Red Leopard Pack Marrom | sem match Tiny exato | `—` | `None` |
| `41499672090-2` | `37/38` | Chinelo Havaianas x Dolce & Gabbana Carreto Ciciliano Vermelho | sem match Tiny exato | `—` | `None` |
| `U9060EEB-7` | `41` | Tênis New Balance 9060 Moonrock Linen Dark Artic Grey Cinza | sem match Tiny exato | `—` | `None` |
| `PAC-1604574-L` | `G/L` | Camiseta Pace Fold Preta | sem match Tiny exato | `—` | `None` |
| `HQ4310-002-40` | `40` | Tênis Nike Mind 002 Grey Football Grey Cinza | sem match Tiny exato | `—` | `None` |
| `ALD-3072990-OS` | `OS` | Boné Aime Leon Dore Washed Script Plaza Taupe Bege | sem match Tiny exato | `—` | `None` |
| `ST67` | `44` | Calça Saint Studio Jeans Baggy Risca de Giz Azul | sem match Tiny exato | `—` | `None` |
| `U9060ERA-2` | `35` | Tênis New Balance 9060 Black Castlerock Preto | sem match Tiny exato | `—` | `None` |
| `002010765` | `40` | Tênis Autry Medalist Low LL15 Branco | sem match Tiny exato | `—` | `None` |
| `ST52-5` | `XL/GG` | Jaqueta Saint Studio Puffer Sarja Pied Bege | sem match Tiny exato | `—` | `None` |
| `1183A201254-2` | `35` | Tênis Onitsuka Tiger Mexico 66 Oatmeal Ginger Peach Rosa | sem match Tiny exato | `—` | `None` |
| `JM6` | `ÚNICO` | Jason Markk Durables Cleaning Brush | sem match Tiny exato | `—` | `None` |
| `30095-1` | `S/P` | Camiseta Aphase Quadrile - Dirty Black Preto | sem match Tiny exato | `—` | `None` |
| `FD9711-602-42` | `42` | Tênis Nike Air Zoom Vomero 5 Doernbecher 2023 Laranja | sem match Tiny exato | `—` | `None` |
| `DL4081684-3` | `36` | Tênis Onitsuka Tiger Mexico 66 Birch Green Branco | sem match Tiny exato | `—` | `None` |
| `ST45-5` | `44` | Calça Saint Studio Wide Alfaiataria Risca de Giz Preta | sem match Tiny exato | `—` | `None` |

## Guardrails

- Usar broker/Doppler; nunca imprimir `TINY_API_TOKEN`.
- Write Tiny somente para os 9 SKUs exatos listados.
- Antes de cada write: readback Tiny do SKU e controle negativo.
- Depois de cada write: readback Tiny deve retornar controle `0`.
- Se qualquer readback divergir, bloquear o SKU e continuar/abortar conforme segurança.
- Não escrever Shopify/Supabase na mesma etapa; Supabase/Hub sincroniza depois.

## Rollback

Para cada SKU alterado, restaurar o controle Tiny anterior registrado no pacote/readback se Lucas solicitar rollback.
