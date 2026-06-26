# LK Compras — StockX/GOAT fallback/importação

Status: `approval_packet_ready_import_lookup_not_executed_to_purchase`

## Fórmula LK usada

`custo_final_estimado_brl = (preco_usd + custo_trazer_usd) × (dolar_atual × 1,05) × 2`

- Dólar usado: 4.911381 (open.er-api.com latest/USD, time_last_update_utc=Thu, 14 May 2026 00:02:31 +0000)
- Custo trazer padrão: US$ 100.00 configurável
- Fator por US$ de sticker depois de buffer/multiplicador: 10.3139 BRL

## Observação de lookup

- StockX/GOAT não entregaram preço público confiável nesta sessão sem login/bloqueio; portanto o pacote deixa os tetos de preço prontos para Júlio/Hermes preencher com fonte autenticada ou manual.
- Sem compra, reserva, contato, WhatsApp ou atualização de card após lookup.

## Fila por produto/tamanho

### P1 — Tênis New Balance 204L Arid Timberwolf Bege — Tam 37 — U204LMMC-4
- Demanda 120d: 8 un
- Preço médio vendido: R$ 2.799,99
- Benchmark nacional/Droper: R$ 1.999,90
- Rota nacional: Borderline: comparar fora/importação antes de comprar nacional.
- Prioridade do lookup StockX/GOAT: comparar antes de comprar nacional
- Teto sticker StockX/GOAT para 30% margem: US$ 90.03
- Teto sticker para 20% margem: US$ 117.18
- Breakeven sticker máximo: US$ 171.48
- Pré-veredito: buscar StockX/GOAT e comparar landed cost

### P1 — Tênis New Balance 204L Arid Timberwolf Bege — Tam 39 — U204LMMC-6
- Demanda 120d: 7 un
- Preço médio vendido: R$ 2.799,99
- Benchmark nacional/Droper: R$ 2.380,00
- Rota nacional: Nacional/Droper não recomendado pela margem; buscar fora/importação ou pular.
- Prioridade do lookup StockX/GOAT: obrigatório antes de qualquer compra nacional
- Teto sticker StockX/GOAT para 30% margem: US$ 90.03
- Teto sticker para 20% margem: US$ 117.18
- Breakeven sticker máximo: US$ 171.48
- Pré-veredito: buscar StockX/GOAT e comparar landed cost

### P1 — Tênis Onitsuka Tiger Mexico 66 White Black Branco — Tam 38 — 1183A201-126-5
- Demanda 120d: 6 un
- Preço médio vendido: R$ 2.399,99
- Benchmark nacional/Droper: R$ 1.890,00
- Rota nacional: Borderline: comparar fora/importação antes de comprar nacional.
- Prioridade do lookup StockX/GOAT: comparar antes de comprar nacional
- Teto sticker StockX/GOAT para 30% margem: US$ 62.89
- Teto sticker para 20% margem: US$ 86.16
- Breakeven sticker máximo: US$ 132.69
- Pré-veredito: só comprar fora se aparecer preço excepcionalmente baixo

### P1 — Tênis Onitsuka Tiger Mexico 66 White Black Branco — Tam 37 — 1183A201-126-4
- Demanda 120d: 5 un
- Preço médio vendido: R$ 2.399,99
- Benchmark nacional/Droper: R$ 1.890,00
- Rota nacional: Borderline: comparar fora/importação antes de comprar nacional.
- Prioridade do lookup StockX/GOAT: comparar antes de comprar nacional
- Teto sticker StockX/GOAT para 30% margem: US$ 62.89
- Teto sticker para 20% margem: US$ 86.16
- Breakeven sticker máximo: US$ 132.69
- Pré-veredito: só comprar fora se aparecer preço excepcionalmente baixo

### P2 — Tênis Nike Moon Shoe SP Jacquemus Alabaster Amarelo — Tam 38 — HV8547-700-5
- Demanda 120d: 4 un
- Preço médio vendido: R$ 5.999,99
- Benchmark nacional/Droper: R$ 6.500,00
- Rota nacional: Nacional/Droper não recomendado pela margem; buscar fora/importação ou pular.
- Prioridade do lookup StockX/GOAT: obrigatório antes de qualquer compra nacional
- Teto sticker StockX/GOAT para 30% margem: US$ 307.22
- Teto sticker para 20% margem: US$ 365.39
- Breakeven sticker máximo: US$ 481.74
- Pré-veredito: buscar StockX/GOAT e comparar landed cost

### P2 — Tênis Nike Moon Shoe SP Jacquemus Alabaster Amarelo — Tam 37 — HV8547-700-4
- Demanda 120d: 4 un
- Preço médio vendido: R$ 4.999,99
- Benchmark nacional/Droper: R$ 6.500,00
- Rota nacional: Nacional/Droper não recomendado pela margem; buscar fora/importação ou pular.
- Prioridade do lookup StockX/GOAT: obrigatório antes de qualquer compra nacional
- Teto sticker StockX/GOAT para 30% margem: US$ 239.35
- Teto sticker para 20% margem: US$ 287.83
- Breakeven sticker máximo: US$ 384.78
- Pré-veredito: buscar StockX/GOAT e comparar landed cost

### P2 — Tênis Onitsuka Tiger Mexico 66 Kill Bill Amarelo — Tam 41.5 — 1183C102.751
- Demanda 120d: 4 un
- Preço médio vendido: R$ 2.399,99
- Benchmark nacional/Droper: R$ 1.890,00
- Rota nacional: Borderline: comparar fora/importação antes de comprar nacional.
- Prioridade do lookup StockX/GOAT: comparar antes de comprar nacional
- Teto sticker StockX/GOAT para 30% margem: US$ 62.89
- Teto sticker para 20% margem: US$ 86.16
- Breakeven sticker máximo: US$ 132.69
- Pré-veredito: só comprar fora se aparecer preço excepcionalmente baixo

### P2 — Tênis Adidas Samba OG Crochet Pack Sand Strata Bege — Tam 35 — JR9446-2
- Demanda 120d: 4 un
- Preço médio vendido: R$ 2.199,99
- Benchmark nacional/Droper: R$ 1.299,99
- Rota nacional: Nacional pode fazer sentido, mas ainda comparar grupo/fora e logística.
- Prioridade do lookup StockX/GOAT: opcional/sanity check; nacional parece viável
- Teto sticker StockX/GOAT para 30% margem: US$ 49.31
- Teto sticker para 20% margem: US$ 70.64
- Breakeven sticker máximo: US$ 113.30
- Pré-veredito: só comprar fora se aparecer preço excepcionalmente baixo

### P2 — Tênis Nike Moon Shoe SP Jacquemus Alabaster Amarelo — Tam 36 — HV8547-700-3
- Demanda 120d: 3 un
- Preço médio vendido: R$ 5.333,32
- Benchmark nacional/Droper: sem match
- Rota nacional: Só investigar fora se virar prioridade ou exceção estratégica.
- Prioridade do lookup StockX/GOAT: obrigatório antes de qualquer compra nacional
- Teto sticker StockX/GOAT para 30% margem: US$ 261.97
- Teto sticker para 20% margem: US$ 313.68
- Breakeven sticker máximo: US$ 417.10
- Pré-veredito: buscar StockX/GOAT e comparar landed cost

### P2 — Tênis New Balance 204L Arid Timberwolf Bege — Tam 38 — U204LMMC-5
- Demanda 120d: 3 un
- Preço médio vendido: R$ 2.799,99
- Benchmark nacional/Droper: R$ 1.999,90
- Rota nacional: Borderline: comparar fora/importação antes de comprar nacional.
- Prioridade do lookup StockX/GOAT: comparar antes de comprar nacional
- Teto sticker StockX/GOAT para 30% margem: US$ 90.03
- Teto sticker para 20% margem: US$ 117.18
- Breakeven sticker máximo: US$ 171.48
- Pré-veredito: buscar StockX/GOAT e comparar landed cost

### P2 — Tênis New Balance 204L Arid Timberwolf Bege — Tam 40 — U204LMMC-7
- Demanda 120d: 3 un
- Preço médio vendido: R$ 2.799,99
- Benchmark nacional/Droper: R$ 2.380,00
- Rota nacional: Nacional/Droper não recomendado pela margem; buscar fora/importação ou pular.
- Prioridade do lookup StockX/GOAT: obrigatório antes de qualquer compra nacional
- Teto sticker StockX/GOAT para 30% margem: US$ 90.03
- Teto sticker para 20% margem: US$ 117.18
- Breakeven sticker máximo: US$ 171.48
- Pré-veredito: buscar StockX/GOAT e comparar landed cost

### P2 — Tênis Onitsuka Tiger Mexico 66 White Black Branco — Tam 36 — 1183A201-126-3
- Demanda 120d: 3 un
- Preço médio vendido: R$ 2.399,99
- Benchmark nacional/Droper: R$ 1.999,99
- Rota nacional: Nacional/Droper não recomendado pela margem; buscar fora/importação ou pular.
- Prioridade do lookup StockX/GOAT: obrigatório antes de qualquer compra nacional
- Teto sticker StockX/GOAT para 30% margem: US$ 62.89
- Teto sticker para 20% margem: US$ 86.16
- Breakeven sticker máximo: US$ 132.69
- Pré-veredito: só comprar fora se aparecer preço excepcionalmente baixo

### P2 — Tênis Onitsuka Tiger Mexico 66 White Black Branco — Tam 40 — 1183A201-126-7
- Demanda 120d: 3 un
- Preço médio vendido: R$ 2.399,99
- Benchmark nacional/Droper: R$ 2.389,70
- Rota nacional: Nacional/Droper não recomendado pela margem; buscar fora/importação ou pular.
- Prioridade do lookup StockX/GOAT: obrigatório antes de qualquer compra nacional
- Teto sticker StockX/GOAT para 30% margem: US$ 62.89
- Teto sticker para 20% margem: US$ 86.16
- Breakeven sticker máximo: US$ 132.69
- Pré-veredito: só comprar fora se aparecer preço excepcionalmente baixo

### P2 — Tênis Adidas Samba OG Crochet Pack Sand Strata Bege — Tam 36 — JR9446-3
- Demanda 120d: 3 un
- Preço médio vendido: R$ 2.199,99
- Benchmark nacional/Droper: R$ 899,00
- Rota nacional: Nacional pode fazer sentido, mas ainda comparar grupo/fora e logística.
- Prioridade do lookup StockX/GOAT: opcional/sanity check; nacional parece viável
- Teto sticker StockX/GOAT para 30% margem: US$ 49.31
- Teto sticker para 20% margem: US$ 70.64
- Breakeven sticker máximo: US$ 113.30
- Pré-veredito: só comprar fora se aparecer preço excepcionalmente baixo
