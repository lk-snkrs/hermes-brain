# Pacote — próximos 19 negativos com Tiny produto exato encontrado

Data: 2026-06-29
values_printed=false

## Resumo

- Negativos restantes no Cockpit/read model: `19`
- Tiny product search encontrou produto com `codigo` exato para: `19`
- A correção proposta é zerar via `lk-tiny estoque balanco` somente estes 19 `tiny_id`, com readback antes/depois.
- Não alterar Shopify, preço, cadastro, compra, cliente, outros depósitos ou outros SKUs.

## Candidatos

| SKU | Tamanho | Produto | Tiny id | Tiny código | Ação proposta |
|---|---:|---|---:|---|---|
| `JQ6445-4` | `37` | Tênis Adidas Samba Jane 'Black White Gum' Preto | `1064244214` | `JQ6445-4` | zerar LK Controle Estoque para `0` |
| `JQ6446-3` | `36` | Tênis Adidas Samba Jane 'Scarlet Gum' Vermelho | `1064244129` | `JQ6446-3` | zerar LK Controle Estoque para `0` |
| `UNISPHERE` | `ÚNICO` | Boné 5 Panel Aimé Leon Dore Unisphere Branco | `1060299626` | `UNISPHERE` | zerar LK Controle Estoque para `0` |
| `JI2734-7` | `40` | Tênis adidas Samba Og Preloved Red Leopard Pack Marrom | `1061459718` | `JI2734-7` | zerar LK Controle Estoque para `0` |
| `41499672090-2` | `37/38` | Chinelo Havaianas x Dolce & Gabbana Carreto Ciciliano Vermelho | `1060924098` | `41499672090-2` | zerar LK Controle Estoque para `0` |
| `U9060EEB-7` | `41` | Tênis New Balance 9060 Moonrock Linen Dark Artic Grey Cinza | `1062072249` | `U9060EEB-7` | zerar LK Controle Estoque para `0` |
| `PAC-1604574-L` | `G/L` | Camiseta Pace Fold Preta | `1069541509` | `PAC-1604574-L` | zerar LK Controle Estoque para `0` |
| `HQ4310-002-40` | `40` | Tênis Nike Mind 002 Grey Football Grey Cinza | `1070659310` | `HQ4310-002-40` | zerar LK Controle Estoque para `0` |
| `ALD-3072990-OS` | `OS` | Boné Aime Leon Dore Washed Script Plaza Taupe Bege | `1066011620` | `ALD-3072990-OS` | zerar LK Controle Estoque para `0` |
| `ST67` | `44` | Calça Saint Studio Jeans Baggy Risca de Giz Azul | `1069931372` | `ST67` | zerar LK Controle Estoque para `0` |
| `U9060ERA-2` | `35` | Tênis New Balance 9060 Black Castlerock Preto | `1064786634` | `U9060ERA-2` | zerar LK Controle Estoque para `0` |
| `002010765` | `40` | Tênis Autry Medalist Low LL15 Branco | `1065806450` | `002010765` | zerar LK Controle Estoque para `0` |
| `ST52-5` | `XL/GG` | Jaqueta Saint Studio Puffer Sarja Pied Bege | `1063685956` | `ST52-5` | zerar LK Controle Estoque para `0` |
| `1183A201254-2` | `35` | Tênis Onitsuka Tiger Mexico 66 Oatmeal Ginger Peach Rosa | `1061436118` | `1183A201254-2` | zerar LK Controle Estoque para `0` |
| `JM6` | `ÚNICO` | Jason Markk Durables Cleaning Brush | `1061206321` | `JM6` | zerar LK Controle Estoque para `0` |
| `30095-1` | `S/P` | Camiseta Aphase Quadrile - Dirty Black Preto | `1063886187` | `30095-1` | zerar LK Controle Estoque para `0` |
| `FD9711-602-42` | `42` | Tênis Nike Air Zoom Vomero 5 Doernbecher 2023 Laranja | `1069546386` | `FD9711-602-42` | zerar LK Controle Estoque para `0` |
| `DL4081684-3` | `36` | Tênis Onitsuka Tiger Mexico 66 Birch Green Branco | `1058893918` | `DL4081684-3` | zerar LK Controle Estoque para `0` |
| `ST45-5` | `44` | Calça Saint Studio Wide Alfaiataria Risca de Giz Preta | `1063679812` | `ST45-5` | zerar LK Controle Estoque para `0` |

## Procedimento aprovado recomendado

Para cada SKU:

1. Readback Tiny por produto/código antes do write.
2. Executar:

```bash
/opt/data/scripts/hermes_doppler.py run --profile lk-stock -- \
/opt/data/home/.local/bin/lk-tiny estoque balanco \
  --id-produto <tiny_id> \
  --quantidade 0 \
  --deposito 'LK | CONTROLE ESTOQUE' \
  --approval '<aprovação escopada>' \
  --allow-write --json
```

3. Readback Tiny depois; sucesso somente se controle do depósito LK ficar `0`.
4. Atualizar Supabase/read model apenas para os SKUs que confirmarem `controle=0`.
5. Validar Cockpit health/queue.

## Rollback

- Restaurar quantidade anterior por SKU a partir do readback antes no arquivo de execução.
- Restaurar Supabase a partir de backup pontual dos 19 SKUs.

## Aprovação sugerida

```text
APROVO Tiny estoque: zerar no Tiny somente os 19 SKUs exatos do pacote negative_19_tiny_identity_classification_20260629.json, usando lk-tiny estoque balanco com readback antes/depois, sem Shopify write e sem outros SKUs.
```
