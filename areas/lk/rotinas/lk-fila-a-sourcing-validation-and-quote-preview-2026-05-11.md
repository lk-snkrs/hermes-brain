# LK OS — Fila A validação interna + fila de cotação preview — 2026-05-11

## Escopo

Continuação aprovada por Lucas: (1) validar fornecedor/lead time/margem dos Top 15 e (2) montar fila de cotação. Este documento é **preview interno/read-only**.

## Guardrails

- Não houve contato com fornecedor.
- Não houve compra/PO.
- Não houve write Shopify/Tiny.
- Não houve alteração de preço, estoque, campanha ou envio externo.

## Método de validação

- **Margem**: como o custo real ainda não está no Brain, calculei tetos máximos de custo por item para margem bruta alvo de 45%, 50% e 55%, usando o preço médio vendido no sinal (`revenue/qty`).
- **Lead time**: P0 só deve avançar automaticamente se houver pronta-entrega ou lead time <= 7 dias. 8–15 dias exige decisão. >15 dias não recomendado sem pré-venda/decisão Lucas.
- **Fornecedor**: permanece campo obrigatório da cotação; nenhum fornecedor foi acionado.

## Resumo executivo

- Itens Top 15 validados: 15
- Grupos de cotação: 9
- P0: 11
- P1/opcional: 4
- Quantidade total de referência para cotar: 39

## Top 15 — validação interna de margem/lead time

### 1. Tênis Nike Moon Shoe SP Jacquemus Medium Brown — 38
- SKU: `HV8547-200-38`
- Família de cotação: Nike x Jacquemus Moon Shoe SP — Medium Brown
- Prioridade: P0 — ruptura com venda repetida
- Sinal: 5 pedidos / 5 un. / R$ 26.999,95
- Preço médio vendido no sinal: R$ 5.399,99
- Estoque Tiny LK | CONTROLE ESTOQUE: 0.0
- Qtd referência para cotar: 3
- Teto custo para margem bruta 45%: R$ 2.969,99
- Teto custo para margem bruta 50%: R$ 2.699,99
- Teto custo para margem bruta 55%: R$ 2.430,00
- Gate lead time: Aprovar só se pronta-entrega/lead time <=7 dias; 8–15 dias exige decisão; >15 dias não recomendado sem pré-venda.
- Status validação: pendente de preço/fornecedor real; margem validada como teto máximo de custo, não como margem real
- Ação preview: cotar agora em modo interno; não comprar sem preço final e fornecedor aprovado
- Riscos: ticket alto: evitar compra múltipla sem confirmação de demanda atual e margem; ruptura/estoque Tiny zerado ou negativo

### 2. Tênis Nike Air Jordan 4 Retro Metallic Gold Branco — 40
- SKU: `AQ9129-170-7`
- Família de cotação: Nike Air Jordan 4 Retro — Metallic Gold
- Prioridade: P0 — ruptura com venda repetida
- Sinal: 4 pedidos / 4 un. / R$ 13.399,96
- Preço médio vendido no sinal: R$ 3.349,99
- Estoque Tiny LK | CONTROLE ESTOQUE: 0.0
- Qtd referência para cotar: 3
- Teto custo para margem bruta 45%: R$ 1.842,49
- Teto custo para margem bruta 50%: R$ 1.674,99
- Teto custo para margem bruta 55%: R$ 1.507,50
- Gate lead time: Aprovar só se pronta-entrega/lead time <=7 dias; 8–15 dias exige decisão; >15 dias não recomendado sem pré-venda.
- Status validação: pendente de preço/fornecedor real; margem validada como teto máximo de custo, não como margem real
- Ação preview: cotar agora em modo interno; não comprar sem preço final e fornecedor aprovado
- Riscos: ruptura/estoque Tiny zerado ou negativo

### 3. Tênis Onitsuka Tiger Mexico 66 White Black Branco — 36
- SKU: `1183A201-126-3`
- Família de cotação: Onitsuka Tiger Mexico 66 — White/Black
- Prioridade: P0 — ruptura com venda repetida
- Sinal: 3 pedidos / 3 un. / R$ 7.199,97
- Preço médio vendido no sinal: R$ 2.399,99
- Estoque Tiny LK | CONTROLE ESTOQUE: 0.0
- Qtd referência para cotar: 3
- Teto custo para margem bruta 45%: R$ 1.319,99
- Teto custo para margem bruta 50%: R$ 1.200,00
- Teto custo para margem bruta 55%: R$ 1.080,00
- Gate lead time: Aprovar só se pronta-entrega/lead time <=7 dias; 8–15 dias exige decisão; >15 dias não recomendado sem pré-venda.
- Status validação: pendente de preço/fornecedor real; margem validada como teto máximo de custo, não como margem real
- Ação preview: cotar agora em modo interno; não comprar sem preço final e fornecedor aprovado
- Riscos: ruptura/estoque Tiny zerado ou negativo

### 4. Tênis Nike Moon Shoe SP Jacquemus Off Noir Preto — 41
- SKU: `HV8547-001-8`
- Família de cotação: Nike x Jacquemus Moon Shoe SP — Off Noir
- Prioridade: P0 — ruptura com venda repetida
- Sinal: 2 pedidos / 2 un. / R$ 11.999,98
- Preço médio vendido no sinal: R$ 5.999,99
- Estoque Tiny LK | CONTROLE ESTOQUE: 0.0
- Qtd referência para cotar: 2
- Teto custo para margem bruta 45%: R$ 3.299,99
- Teto custo para margem bruta 50%: R$ 2.999,99
- Teto custo para margem bruta 55%: R$ 2.700,00
- Gate lead time: Aprovar só se pronta-entrega/lead time <=7 dias; 8–15 dias exige decisão; >15 dias não recomendado sem pré-venda.
- Status validação: pendente de preço/fornecedor real; margem validada como teto máximo de custo, não como margem real
- Ação preview: cotar agora em modo interno; não comprar sem preço final e fornecedor aprovado
- Riscos: ticket alto: evitar compra múltipla sem confirmação de demanda atual e margem; ruptura/estoque Tiny zerado ou negativo

### 5. Tênis Nike Moon Shoe SP Jacquemus Off White — 39
- SKU: `HV8547-002-39`
- Família de cotação: Nike x Jacquemus Moon Shoe SP — Off White
- Prioridade: P0 — ruptura com venda repetida
- Sinal: 2 pedidos / 2 un. / R$ 9.999,98
- Preço médio vendido no sinal: R$ 4.999,99
- Estoque Tiny LK | CONTROLE ESTOQUE: 0.0
- Qtd referência para cotar: 2
- Teto custo para margem bruta 45%: R$ 2.749,99
- Teto custo para margem bruta 50%: R$ 2.499,99
- Teto custo para margem bruta 55%: R$ 2.250,00
- Gate lead time: Aprovar só se pronta-entrega/lead time <=7 dias; 8–15 dias exige decisão; >15 dias não recomendado sem pré-venda.
- Status validação: pendente de preço/fornecedor real; margem validada como teto máximo de custo, não como margem real
- Ação preview: cotar agora em modo interno; não comprar sem preço final e fornecedor aprovado
- Riscos: ticket alto: evitar compra múltipla sem confirmação de demanda atual e margem; ruptura/estoque Tiny zerado ou negativo

### 6. Tênis Nike Moon Shoe SP Jacquemus Off White — 38
- SKU: `HV8547-002-38`
- Família de cotação: Nike x Jacquemus Moon Shoe SP — Off White
- Prioridade: P0 — ruptura com venda repetida
- Sinal: 2 pedidos / 2 un. / R$ 9.999,98
- Preço médio vendido no sinal: R$ 4.999,99
- Estoque Tiny LK | CONTROLE ESTOQUE: 0.0
- Qtd referência para cotar: 2
- Teto custo para margem bruta 45%: R$ 2.749,99
- Teto custo para margem bruta 50%: R$ 2.499,99
- Teto custo para margem bruta 55%: R$ 2.250,00
- Gate lead time: Aprovar só se pronta-entrega/lead time <=7 dias; 8–15 dias exige decisão; >15 dias não recomendado sem pré-venda.
- Status validação: pendente de preço/fornecedor real; margem validada como teto máximo de custo, não como margem real
- Ação preview: cotar agora em modo interno; não comprar sem preço final e fornecedor aprovado
- Riscos: ticket alto: evitar compra múltipla sem confirmação de demanda atual e margem; ruptura/estoque Tiny zerado ou negativo

### 7. Tênis Onitsuka Tiger Mexico 66 Paraty Birch Cream Bege — 39
- SKU: `1183B601.200-6`
- Família de cotação: Onitsuka Tiger Mexico 66 Paraty — Birch Cream
- Prioridade: P0 — ruptura com venda repetida
- Sinal: 2 pedidos / 2 un. / R$ 4.599,98
- Preço médio vendido no sinal: R$ 2.299,99
- Estoque Tiny LK | CONTROLE ESTOQUE: 0.0
- Qtd referência para cotar: 2
- Teto custo para margem bruta 45%: R$ 1.264,99
- Teto custo para margem bruta 50%: R$ 1.149,99
- Teto custo para margem bruta 55%: R$ 1.035,00
- Gate lead time: Aprovar só se pronta-entrega/lead time <=7 dias; 8–15 dias exige decisão; >15 dias não recomendado sem pré-venda.
- Status validação: pendente de preço/fornecedor real; margem validada como teto máximo de custo, não como margem real
- Ação preview: cotar agora em modo interno; não comprar sem preço final e fornecedor aprovado
- Riscos: ruptura/estoque Tiny zerado ou negativo

### 8. Tênis Onitsuka Tiger Mexico 66 Sabot Beige Green Bege — 40
- SKU: `1183C123.252-7`
- Família de cotação: Onitsuka Tiger Mexico 66 Sabot — Beige Green
- Prioridade: P0 — ruptura com venda repetida
- Sinal: 2 pedidos / 2 un. / R$ 4.399,98
- Preço médio vendido no sinal: R$ 2.199,99
- Estoque Tiny LK | CONTROLE ESTOQUE: 0.0
- Qtd referência para cotar: 2
- Teto custo para margem bruta 45%: R$ 1.209,99
- Teto custo para margem bruta 50%: R$ 1.099,99
- Teto custo para margem bruta 55%: R$ 990,00
- Gate lead time: Aprovar só se pronta-entrega/lead time <=7 dias; 8–15 dias exige decisão; >15 dias não recomendado sem pré-venda.
- Status validação: pendente de preço/fornecedor real; margem validada como teto máximo de custo, não como margem real
- Ação preview: cotar agora em modo interno; não comprar sem preço final e fornecedor aprovado
- Riscos: ruptura/estoque Tiny zerado ou negativo

### 9. Tênis Onitsuka Tiger Mexico 66 Sabot Beige Green Bege — 38
- SKU: `1183C123.252-5`
- Família de cotação: Onitsuka Tiger Mexico 66 Sabot — Beige Green
- Prioridade: P0 — ruptura com venda repetida
- Sinal: 2 pedidos / 2 un. / R$ 4.399,98
- Preço médio vendido no sinal: R$ 2.199,99
- Estoque Tiny LK | CONTROLE ESTOQUE: 0.0
- Qtd referência para cotar: 2
- Teto custo para margem bruta 45%: R$ 1.209,99
- Teto custo para margem bruta 50%: R$ 1.099,99
- Teto custo para margem bruta 55%: R$ 990,00
- Gate lead time: Aprovar só se pronta-entrega/lead time <=7 dias; 8–15 dias exige decisão; >15 dias não recomendado sem pré-venda.
- Status validação: pendente de preço/fornecedor real; margem validada como teto máximo de custo, não como margem real
- Ação preview: cotar agora em modo interno; não comprar sem preço final e fornecedor aprovado
- Riscos: ruptura/estoque Tiny zerado ou negativo

### 10. Tênis Onitsuka Tiger Mexico 66 Sabot Beige Green Bege — 37
- SKU: `1183C123.252-4`
- Família de cotação: Onitsuka Tiger Mexico 66 Sabot — Beige Green
- Prioridade: P0 — ruptura com venda repetida
- Sinal: 2 pedidos / 2 un. / R$ 4.399,98
- Preço médio vendido no sinal: R$ 2.199,99
- Estoque Tiny LK | CONTROLE ESTOQUE: 0.0
- Qtd referência para cotar: 2
- Teto custo para margem bruta 45%: R$ 1.209,99
- Teto custo para margem bruta 50%: R$ 1.099,99
- Teto custo para margem bruta 55%: R$ 990,00
- Gate lead time: Aprovar só se pronta-entrega/lead time <=7 dias; 8–15 dias exige decisão; >15 dias não recomendado sem pré-venda.
- Status validação: pendente de preço/fornecedor real; margem validada como teto máximo de custo, não como margem real
- Ação preview: cotar agora em modo interno; não comprar sem preço final e fornecedor aprovado
- Riscos: ruptura/estoque Tiny zerado ou negativo

### 11. Jason Markk Essential Kit de Limpeza — [sem variant]
- SKU: `300110`
- Família de cotação: Jason Markk Essential Kit
- Prioridade: P0 — ruptura com venda repetida
- Sinal: 2 pedidos / 2 un. / R$ 399,98
- Preço médio vendido no sinal: R$ 199,99
- Estoque Tiny LK | CONTROLE ESTOQUE: -2.0
- Qtd referência para cotar: 12
- Teto custo para margem bruta 45%: R$ 109,99
- Teto custo para margem bruta 50%: R$ 100,00
- Teto custo para margem bruta 55%: R$ 90,00
- Gate lead time: Aprovar só se pronta-entrega/lead time <=7 dias; 8–15 dias exige decisão; >15 dias não recomendado sem pré-venda.
- Status validação: pendente de preço/fornecedor real; margem validada como teto máximo de custo, não como margem real
- Ação preview: cotar agora em modo interno; não comprar sem preço final e fornecedor aprovado
- Riscos: ruptura/estoque Tiny zerado ou negativo

### 12. Tênis Nike Moon Shoe SP Jacquemus Off Noir Preto — 38
- SKU: `HV8547-001-5`
- Família de cotação: Nike x Jacquemus Moon Shoe SP — Off Noir
- Prioridade: P1 — ruptura com venda unitária
- Sinal: 1 pedidos / 1 un. / R$ 5.999,99
- Preço médio vendido no sinal: R$ 5.999,99
- Estoque Tiny LK | CONTROLE ESTOQUE: 0.0
- Qtd referência para cotar: 1
- Teto custo para margem bruta 45%: R$ 3.299,99
- Teto custo para margem bruta 50%: R$ 2.999,99
- Teto custo para margem bruta 55%: R$ 2.700,00
- Gate lead time: Cotar como opcional; aprovar só se pronta-entrega ou aproveitando remessa de P0.
- Status validação: pendente de preço/fornecedor real; margem validada como teto máximo de custo, não como margem real
- Ação preview: cotar opcional/bundle; monitorar antes de reposição
- Riscos: ticket alto: evitar compra múltipla sem confirmação de demanda atual e margem; ruptura/estoque Tiny zerado ou negativo; P1: sinal unitário, menor convicção que P0

### 13. Tênis Nike Moon Shoe SP Jacquemus Off Noir Preto — 40
- SKU: `HV8547-001-7`
- Família de cotação: Nike x Jacquemus Moon Shoe SP — Off Noir
- Prioridade: P1 — ruptura com venda unitária
- Sinal: 1 pedidos / 1 un. / R$ 5.999,99
- Preço médio vendido no sinal: R$ 5.999,99
- Estoque Tiny LK | CONTROLE ESTOQUE: 0.0
- Qtd referência para cotar: 1
- Teto custo para margem bruta 45%: R$ 3.299,99
- Teto custo para margem bruta 50%: R$ 2.999,99
- Teto custo para margem bruta 55%: R$ 2.700,00
- Gate lead time: Cotar como opcional; aprovar só se pronta-entrega ou aproveitando remessa de P0.
- Status validação: pendente de preço/fornecedor real; margem validada como teto máximo de custo, não como margem real
- Ação preview: cotar opcional/bundle; monitorar antes de reposição
- Riscos: ticket alto: evitar compra múltipla sem confirmação de demanda atual e margem; ruptura/estoque Tiny zerado ou negativo; P1: sinal unitário, menor convicção que P0

### 14. Tênis Nike Moon Shoe SP Jacquemus Alabaster Amarelo — 40
- SKU: `HV8547-700-7`
- Família de cotação: Nike x Jacquemus Moon Shoe SP — Alabaster
- Prioridade: P1 — ruptura com venda unitária
- Sinal: 1 pedidos / 1 un. / R$ 5.999,99
- Preço médio vendido no sinal: R$ 5.999,99
- Estoque Tiny LK | CONTROLE ESTOQUE: 0.0
- Qtd referência para cotar: 1
- Teto custo para margem bruta 45%: R$ 3.299,99
- Teto custo para margem bruta 50%: R$ 2.999,99
- Teto custo para margem bruta 55%: R$ 2.700,00
- Gate lead time: Cotar como opcional; aprovar só se pronta-entrega ou aproveitando remessa de P0.
- Status validação: pendente de preço/fornecedor real; margem validada como teto máximo de custo, não como margem real
- Ação preview: cotar opcional/bundle; monitorar antes de reposição
- Riscos: ticket alto: evitar compra múltipla sem confirmação de demanda atual e margem; ruptura/estoque Tiny zerado ou negativo; P1: sinal unitário, menor convicção que P0

### 15. Tênis Nike Moon Shoe SP Jacquemus Off White — 36
- SKU: `HV8547-002-36`
- Família de cotação: Nike x Jacquemus Moon Shoe SP — Off White
- Prioridade: P1 — ruptura com venda unitária
- Sinal: 1 pedidos / 1 un. / R$ 4.999,99
- Preço médio vendido no sinal: R$ 4.999,99
- Estoque Tiny LK | CONTROLE ESTOQUE: 0.0
- Qtd referência para cotar: 1
- Teto custo para margem bruta 45%: R$ 2.749,99
- Teto custo para margem bruta 50%: R$ 2.499,99
- Teto custo para margem bruta 55%: R$ 2.250,00
- Gate lead time: Cotar como opcional; aprovar só se pronta-entrega ou aproveitando remessa de P0.
- Status validação: pendente de preço/fornecedor real; margem validada como teto máximo de custo, não como margem real
- Ação preview: cotar opcional/bundle; monitorar antes de reposição
- Riscos: ticket alto: evitar compra múltipla sem confirmação de demanda atual e margem; ruptura/estoque Tiny zerado ou negativo; P1: sinal unitário, menor convicção que P0

## Fila de cotação — agrupada por família/modelo

Use este bloco como **brief interno**. Não enviar sem aprovação explícita do Lucas.

### Grupo 1: Jason Markk Essential Kit
- Prioridade do grupo: P0
- Qtd total referência para cotar: 12
- Itens:
  - SKU `300110` — tamanho [sem variant] — qtd ref. 12 — preço médio sinal R$ 199,99 — teto custo 50% GM R$ 100,00
- Pergunta para fornecedor, em preview:
  > Consegue cotar Jason Markk Essential Kit nos tamanhos [sem variant] (SKU 300110, qtd ref. 12)? Informar custo unitário, pronta-entrega/lead time, frete/impostos e condição.

### Grupo 2: Onitsuka Tiger Mexico 66 Sabot — Beige Green
- Prioridade do grupo: P0
- Qtd total referência para cotar: 6
- Itens:
  - SKU `1183C123.252-7` — tamanho 40 — qtd ref. 2 — preço médio sinal R$ 2.199,99 — teto custo 50% GM R$ 1.099,99
  - SKU `1183C123.252-5` — tamanho 38 — qtd ref. 2 — preço médio sinal R$ 2.199,99 — teto custo 50% GM R$ 1.099,99
  - SKU `1183C123.252-4` — tamanho 37 — qtd ref. 2 — preço médio sinal R$ 2.199,99 — teto custo 50% GM R$ 1.099,99
- Pergunta para fornecedor, em preview:
  > Consegue cotar Onitsuka Tiger Mexico 66 Sabot — Beige Green nos tamanhos 40 (SKU 1183C123.252-7, qtd ref. 2), 38 (SKU 1183C123.252-5, qtd ref. 2), 37 (SKU 1183C123.252-4, qtd ref. 2)? Informar custo unitário, pronta-entrega/lead time, frete/impostos e condição.

### Grupo 3: Nike x Jacquemus Moon Shoe SP — Off White
- Prioridade do grupo: P0
- Qtd total referência para cotar: 5
- Itens:
  - SKU `HV8547-002-39` — tamanho 39 — qtd ref. 2 — preço médio sinal R$ 4.999,99 — teto custo 50% GM R$ 2.499,99
  - SKU `HV8547-002-38` — tamanho 38 — qtd ref. 2 — preço médio sinal R$ 4.999,99 — teto custo 50% GM R$ 2.499,99
  - SKU `HV8547-002-36` — tamanho 36 — qtd ref. 1 — preço médio sinal R$ 4.999,99 — teto custo 50% GM R$ 2.499,99
- Pergunta para fornecedor, em preview:
  > Consegue cotar Nike x Jacquemus Moon Shoe SP — Off White nos tamanhos 39 (SKU HV8547-002-39, qtd ref. 2), 38 (SKU HV8547-002-38, qtd ref. 2), 36 (SKU HV8547-002-36, qtd ref. 1)? Informar custo unitário, pronta-entrega/lead time, frete/impostos e condição.

### Grupo 4: Nike x Jacquemus Moon Shoe SP — Off Noir
- Prioridade do grupo: P0
- Qtd total referência para cotar: 4
- Itens:
  - SKU `HV8547-001-8` — tamanho 41 — qtd ref. 2 — preço médio sinal R$ 5.999,99 — teto custo 50% GM R$ 2.999,99
  - SKU `HV8547-001-5` — tamanho 38 — qtd ref. 1 — preço médio sinal R$ 5.999,99 — teto custo 50% GM R$ 2.999,99
  - SKU `HV8547-001-7` — tamanho 40 — qtd ref. 1 — preço médio sinal R$ 5.999,99 — teto custo 50% GM R$ 2.999,99
- Pergunta para fornecedor, em preview:
  > Consegue cotar Nike x Jacquemus Moon Shoe SP — Off Noir nos tamanhos 41 (SKU HV8547-001-8, qtd ref. 2), 38 (SKU HV8547-001-5, qtd ref. 1), 40 (SKU HV8547-001-7, qtd ref. 1)? Informar custo unitário, pronta-entrega/lead time, frete/impostos e condição.

### Grupo 5: Nike x Jacquemus Moon Shoe SP — Medium Brown
- Prioridade do grupo: P0
- Qtd total referência para cotar: 3
- Itens:
  - SKU `HV8547-200-38` — tamanho 38 — qtd ref. 3 — preço médio sinal R$ 5.399,99 — teto custo 50% GM R$ 2.699,99
- Pergunta para fornecedor, em preview:
  > Consegue cotar Nike x Jacquemus Moon Shoe SP — Medium Brown nos tamanhos 38 (SKU HV8547-200-38, qtd ref. 3)? Informar custo unitário, pronta-entrega/lead time, frete/impostos e condição.

### Grupo 6: Nike Air Jordan 4 Retro — Metallic Gold
- Prioridade do grupo: P0
- Qtd total referência para cotar: 3
- Itens:
  - SKU `AQ9129-170-7` — tamanho 40 — qtd ref. 3 — preço médio sinal R$ 3.349,99 — teto custo 50% GM R$ 1.674,99
- Pergunta para fornecedor, em preview:
  > Consegue cotar Nike Air Jordan 4 Retro — Metallic Gold nos tamanhos 40 (SKU AQ9129-170-7, qtd ref. 3)? Informar custo unitário, pronta-entrega/lead time, frete/impostos e condição.

### Grupo 7: Onitsuka Tiger Mexico 66 — White/Black
- Prioridade do grupo: P0
- Qtd total referência para cotar: 3
- Itens:
  - SKU `1183A201-126-3` — tamanho 36 — qtd ref. 3 — preço médio sinal R$ 2.399,99 — teto custo 50% GM R$ 1.200,00
- Pergunta para fornecedor, em preview:
  > Consegue cotar Onitsuka Tiger Mexico 66 — White/Black nos tamanhos 36 (SKU 1183A201-126-3, qtd ref. 3)? Informar custo unitário, pronta-entrega/lead time, frete/impostos e condição.

### Grupo 8: Onitsuka Tiger Mexico 66 Paraty — Birch Cream
- Prioridade do grupo: P0
- Qtd total referência para cotar: 2
- Itens:
  - SKU `1183B601.200-6` — tamanho 39 — qtd ref. 2 — preço médio sinal R$ 2.299,99 — teto custo 50% GM R$ 1.149,99
- Pergunta para fornecedor, em preview:
  > Consegue cotar Onitsuka Tiger Mexico 66 Paraty — Birch Cream nos tamanhos 39 (SKU 1183B601.200-6, qtd ref. 2)? Informar custo unitário, pronta-entrega/lead time, frete/impostos e condição.

### Grupo 9: Nike x Jacquemus Moon Shoe SP — Alabaster
- Prioridade do grupo: P1/opcional
- Qtd total referência para cotar: 1
- Itens:
  - SKU `HV8547-700-7` — tamanho 40 — qtd ref. 1 — preço médio sinal R$ 5.999,99 — teto custo 50% GM R$ 2.999,99
- Pergunta para fornecedor, em preview:
  > Consegue cotar Nike x Jacquemus Moon Shoe SP — Alabaster nos tamanhos 40 (SKU HV8547-700-7, qtd ref. 1)? Informar custo unitário, pronta-entrega/lead time, frete/impostos e condição.

## Checklist antes de aprovar envio de cotação

- Lucas/Júlio confirma quais fornecedores podem receber o brief.
- Definir se a cotação pode citar SKUs internos ou apenas nome/modelo/tamanho.
- Confirmar margem mínima aceitável por categoria: sneaker premium, Onitsuka fashion, acessório.
- Confirmar se P1 entra no mesmo pedido apenas como bundle/oportunidade.
- Após resposta do fornecedor: comparar custo real contra tetos de margem e gate de lead time antes de qualquer compra.

## Artefatos

- `reports/lk-fila-a-sourcing-validation-and-quote-preview-2026-05-11.json`
- `reports/lk-fila-a-sourcing-validation-and-quote-preview-2026-05-11.csv`
- Fonte: `reports/lk-os-next-stage-fila-a-sourcing-preview-2026-05-11.json`
