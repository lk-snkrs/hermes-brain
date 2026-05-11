# LK Stock/Sourcing — sinais de reposição (read-only)

Gerado em BRT: 2026-05-10T22:07:12.970051-03:00
Escopo: Tiny depósito oficial `LK | CONTROLE ESTOQUE` + Shopify SKU/vendas; sem PII, sem writes externos, sem PO/compra.

## Status das fontes
- Shopify: OK; janela 30 dias; pedidos válidos sem PII: 357; SKUs vendidos: 316; produtos lidos: 2271.
- Tiny: consultado por SKU vendido; SKUs checados: 316; produtos encontrados: 267; erros por SKU: 49.
- Depósito `LK | CONTROLE ESTOQUE`: encontrado explicitamente em 265/316 SKUs vendidos. Quando não encontrado, o relatório mantém lacuna e não inventa estoque por depósito.
- Lead time: não disponível por SKU/tamanho nas fontes consultadas; tratado como lacuna bloqueante para decisão final de reposição.

## Contagem de sinais
- crítico: 201
- alto: 0
- médio: 49
- lacuna: 51
- monitorar: 15

## Ranking produto + SKU + tamanho
| Sinal | Produto | SKU | Tam. | Vend. 30d | Estoque Tiny LK Controle | Estoque Tiny total | Estoque Shopify | Cobertura est. | Recomendação analítica | Decisão de estoque |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| crítico | Camiseta MASP x Leonilson "Sem Titulo" Bege | MASP1-1 | P/S | 6 | 0.0 | 6.0 | -6 | 0.0 | cotação/sourcing recomendado | não decidir automaticamente; validar Tiny depósito LK \| CONTROLE ESTOQUE + lead time + margem antes de PO/compra |
| crítico | Tênis Nike Moon Shoe SP Jacquemus Off White | HV8547-002-38 | 38 | 5 | 0.0 | 13.0 | 0 | 0.0 | cotação/sourcing recomendado | não decidir automaticamente; validar Tiny depósito LK \| CONTROLE ESTOQUE + lead time + margem antes de PO/compra |
| crítico | Tênis New Balance 204L Mushroom Arid Stone Marrom | U204LMMA-5 | 38 | 4 | 0.0 | 14.0 | -1 | 0.0 | cotação/sourcing recomendado | não decidir automaticamente; validar Tiny depósito LK \| CONTROLE ESTOQUE + lead time + margem antes de PO/compra |
| crítico | Tênis New Balance 9060 Sea Salt Moonbeam Branco | U9060WHT-4 | 37 | 4 | -1.0 | 6.0 | -2 | -7.5 | cotação/sourcing recomendado | não decidir automaticamente; validar Tiny depósito LK \| CONTROLE ESTOQUE + lead time + margem antes de PO/compra |
| crítico | Tênis Nike Moon Shoe SP Jacquemus Medium Brown Marrom | HV8547-200-38 | 38 | 4 | 0.0 | 8.0 | -2 | 0.0 | cotação/sourcing recomendado | não decidir automaticamente; validar Tiny depósito LK \| CONTROLE ESTOQUE + lead time + margem antes de PO/compra |
| crítico | Pullover Alo Yoga Accolade 1/4 Zip Preto | u3040rg_00-4 | M/M | 3 | 0.0 | 3.0 | -2 | 0.0 | cotação/sourcing recomendado | não decidir automaticamente; validar Tiny depósito LK \| CONTROLE ESTOQUE + lead time + margem antes de PO/compra |
| crítico | Tênis New Balance 204L Mushroom Arid Stone Marrom | U204LMMA-2 | 35 | 3 | 0.0 | 14.0 | 0 | 0.0 | cotação/sourcing recomendado | não decidir automaticamente; validar Tiny depósito LK \| CONTROLE ESTOQUE + lead time + margem antes de PO/compra |
| crítico | Tênis New Balance 9060 Bisque Sea Salt Bege | U9060CCB-6 | 39 | 3 | 0.0 | 0.0 | 0 | 0.0 | cotação/sourcing recomendado | não decidir automaticamente; validar Tiny depósito LK \| CONTROLE ESTOQUE + lead time + margem antes de PO/compra |
| crítico | Tênis Nike Moon Shoe SP Jacquemus Medium Brown Marrom | HV8547-200-41 | 41 | 3 | 0.0 | 5.0 | 0 | 0.0 | cotação/sourcing recomendado | não decidir automaticamente; validar Tiny depósito LK \| CONTROLE ESTOQUE + lead time + margem antes de PO/compra |
| crítico | Tênis Nike Moon Shoe SP Jacquemus Medium Brown Marrom | HV8547-200-39 | 39 | 3 | -1.0 | 0.0 | 0 | -10.0 | cotação/sourcing recomendado | não decidir automaticamente; validar Tiny depósito LK \| CONTROLE ESTOQUE + lead time + margem antes de PO/compra |
| crítico | Tênis Nike Moon Shoe SP Jacquemus Off White | HV8547-002-36 | 36 | 3 | 0.0 | 8.0 | -3 | 0.0 | cotação/sourcing recomendado | não decidir automaticamente; validar Tiny depósito LK \| CONTROLE ESTOQUE + lead time + margem antes de PO/compra |
| crítico | Tênis Nike Moon Shoe SP Jacquemus Off White | HV8547-002-39 | 39 | 3 | 0.0 | 9.0 | 0 | 0.0 | cotação/sourcing recomendado | não decidir automaticamente; validar Tiny depósito LK \| CONTROLE ESTOQUE + lead time + margem antes de PO/compra |
| crítico | Tênis Nike Vomero Premium Flat Stout Marrom | IQ0028-209 | 43 | 3 | 0.0 | 1.0 | -1 | 0.0 | cotação/sourcing recomendado | não decidir automaticamente; validar Tiny depósito LK \| CONTROLE ESTOQUE + lead time + margem antes de PO/compra |
| crítico | Jason Markk Essential Kit de Limpeza | 300110 | lacuna | 2 | -2.0 | 70.0 | 0 | -30.0 | cotação/sourcing recomendado | não decidir automaticamente; validar Tiny depósito LK \| CONTROLE ESTOQUE + lead time + margem antes de PO/compra |
| crítico | The Peptide Lip Tints Rhode Multicolor | LIP | Espresso Rich Brown | 2 | 0.0 | 0.0 | -1 | 0.0 | cotação/sourcing recomendado | não decidir automaticamente; validar Tiny depósito LK \| CONTROLE ESTOQUE + lead time + margem antes de PO/compra |
| crítico | Tênis New Balance 9060 Black Castlerock Grey Preto | U9060BLK | 39 | 2 | 0.0 | 3.0 | 5 | 0.0 | cotação/sourcing recomendado | não decidir automaticamente; validar Tiny depósito LK \| CONTROLE ESTOQUE + lead time + margem antes de PO/compra |
| crítico | Tênis New Balance 9060 Mushroom Arid Stone Bege | 43774078389050 | 34 | 2 | 0.0 | 0.0 | 0 | 0.0 | cotação/sourcing recomendado | não decidir automaticamente; validar Tiny depósito LK \| CONTROLE ESTOQUE + lead time + margem antes de PO/compra |
| crítico | Tênis New Balance 9060 Mushroom Arid Stone Bege | U9060ERC-4 | 37 | 2 | 0.0 | 7.0 | -2 | 0.0 | cotação/sourcing recomendado | não decidir automaticamente; validar Tiny depósito LK \| CONTROLE ESTOQUE + lead time + margem antes de PO/compra |
| crítico | Tênis New Balance 9060 Rich Oak Marrom | U9060CCC-4 | 37 | 2 | 0.0 | 2.0 | -2 | 0.0 | cotação/sourcing recomendado | não decidir automaticamente; validar Tiny depósito LK \| CONTROLE ESTOQUE + lead time + margem antes de PO/compra |
| crítico | Tênis New Balance 9060 Sea Salt Concrete Branco | U9060ECA-10 | 40 | 2 | 0.0 | 2.0 | -3 | 0.0 | cotação/sourcing recomendado | não decidir automaticamente; validar Tiny depósito LK \| CONTROLE ESTOQUE + lead time + margem antes de PO/compra |

## Interpretação
- “Recomendação analítica” indica prioridade de cotação/sourcing/monitoramento interno; não é autorização para compra, PO ou alteração de estoque.
- “Decisão de estoque” permanece pendente quando falta lead time, margem, grade ideal por tamanho ou confirmação do depósito Tiny oficial.
- Não houve inferência de produto por campaign_id/adset_id; os produtos vieram de line_items/SKUs Shopify e busca Tiny por SKU.

## Lacunas/checklist antes de repor
- Lead time por SKU/tamanho não apareceu nas fontes locais/API consultadas; precisa campo/tabela canônica antes de decisão de reposição.
- Tiny foi consultado por SKUs vendidos no Shopify; não houve monitoramento amplo de retailers externos.
- Decisão de repor estoque ficou separada da recomendação analítica; nenhuma PO/compra/write externo executado.
- Criar/validar campo canônico de lead time por produto+SKU+tamanho e política de cobertura desejada por categoria/curva.
- Confirmar por que o endpoint Tiny não retorna explicitamente o depósito oficial para todos os SKUs antes de tratar estoque total como estoque disponível LK Controle.
