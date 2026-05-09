# Exemplo preenchido — Stock Intelligence Center LK

Status: exemplo fictício/read-only v0.1.
Período simulado: últimos 30 dias até 2026-05-08.
Uso: validar formato e lógica de decisão por variante/tamanho antes de dados reais.
Não faz: compra, contato com revendedor, mensagem no WhatsApp, criação Notion, alteração Shopify/Tiny/preço.

## Leitura CEO

O exemplo mostra três tipos de decisão que o Stock Intelligence Center precisa separar:

1. **Comprar antes de acabar**: produto ainda tem estoque, mas cobertura é menor que lead time.
2. **Checar fonte sem comprar automaticamente**: produto zerado ou quase zerado com venda recente.
3. **Não comprar / girar estoque**: produto parado, mesmo que pareça desejável.

## 1. Risco de ruptura

### New Balance 860 [cor a confirmar] — tamanho 37

```text
Produto/modelo/tamanho: New Balance 860 [cor] / 37
Status: risco ruptura
Estoque livre Tiny estimado: 1
Vendas 30d: 4 unidades
Velocidade venda: 0,13 un/dia
Cobertura estimada: ~7,5 dias
Lead time reposição: Brasil 3–7 dias; fora/US ~30 dias
Fonte recomendada para checar: Droper.app e grupo LK.Sneakers | Compras primeiro
Preço reposição estimado: [a confirmar]
Preço LK atual: [a preencher]
Preço LK sugerido: não sugerir sem preço reposição validado
Recomendação: checar fonte Brasil agora; se preço fizer sentido, pedir aprovação para compra/reposição
Confiança: média
Dados faltantes: reserva/encomenda no pedido, preço real Droper, disponibilidade por revendedor
Aprovação necessária: checar fonte externa e enviar rascunho ao grupo de compras
```

Leitura: se a reposição for Brasil, ainda dá tempo. Se depender de fora, já está tarde; o tamanho pode romper antes de chegar.

### Onitsuka [modelo/cor] — tamanho 36

```text
Produto/modelo/tamanho: Onitsuka [modelo/cor] / 36
Status: zerado relevante
Estoque livre Tiny estimado: 0
Vendas 30d: 3 unidades
Velocidade venda: 0,10 un/dia
Cobertura estimada: 0 dia
Lead time reposição: variável; Brasil se houver revendedor
Fonte recomendada para checar: Droper.app, pessoas/revendedores e histórico de compra
Preço reposição estimado: [a confirmar]
Preço LK atual: [a preencher]
Preço LK sugerido: manter indefinido até saber reposição
Recomendação: checar fonte, mas só comprar se preço e prazo preservarem caixa/giro
Confiança: baixa/média
Dados faltantes: se o produto existe no Brasil, preço de compra real, elasticidade de preço
Aprovação necessária: qualquer compra ou mensagem a fornecedor/grupo
```

Leitura: produto zerado com venda recente, mas a decisão depende muito de fonte humana. O sistema não deve classificar automaticamente como encomenda BR/US.

## 2. Compra antes de acabar

### Exemplo de lógica de timing

```text
Produto: New Balance 860 [cor]
Tamanho: 37
Estoque livre: 1
Vendas 30d: 4
Cobertura: ~7,5 dias
Lead time Brasil: 3–7 dias
Lead time fora/US: ~30 dias
Recomendação: iniciar checagem Brasil agora; se só existir fora, decidir se aceita ruptura temporária ou encomenda humana.
```

Decisão recomendada: aprovar **checagem**, não compra automática. Comprar só depois de preço/prazo/fonte.

## 3. Zeros importantes

- New Balance 860 tamanho 38: zerado e com venda recente.
- Onitsuka tamanho 36: zerado e com sinal de influencer no exemplo.
- Adidas `[modelo/cor]` tamanho 40: zerado, mas venda isolada; baixa prioridade.

Ação sugerida: priorizar New Balance 860 38 no rascunho para `LK.Sneakers | Compras`, porque combina venda recente + estoque zero + provável demanda por grade.

## 4. Estoque alto e venda lenta

### Nike [modelo/cor] — tamanho 44

```text
Produto/modelo/tamanho: Nike [modelo/cor] / 44
Status: estoque alto lento
Estoque livre Tiny estimado: 5
Vendas 30d: 0
Vendas 90d: 1
Cobertura estimada: não aplicável; velocidade muito baixa
Lead time reposição: não relevante agora
Fonte recomendada: nenhuma
Preço reposição estimado: não consultar
Preço LK atual: [a preencher]
Preço LK sugerido: avaliar campanha/conteúdo antes de desconto; não recomprar
Recomendação: não comprar; testar comunicação ou reposicionar em campanha se fizer sentido
Confiança: média
Dados faltantes: tráfego PDP, impressões, preço vs mercado, motivo de baixa conversão
Aprovação necessária: qualquer campanha/desconto/publicação
```

Leitura: não confundir “marca importante” com “precisa recomprar”. Aqui o melhor pode ser vender melhor o que já existe.

## 5. Restock externo acionado por demanda interna

Gatilho aprovado para busca externa:

```text
Sinal interno: vendeu 4 unidades em 30 dias e estoque livre está 0–1.
Ação permitida: checar Droper.app/StockX/KicksDev/lojas/fontes como pesquisa.
Ação bloqueada: comprar, reservar, mandar WhatsApp ou criar Notion sem aprovação.
```

Exemplo de output:

```text
Produto: New Balance 860 [cor] / 38
Sinal: venda recente + estoque zero
Fonte a checar: Droper.app primeiro; se indisponível, KicksDev/StockX
Mensagem sugerida para compras: “Pessoal, alguém com New Balance 860 [cor] tam. 38? Produto vendeu na LK e estamos zerados. Mandar preço/prazo.”
Status: rascunho, não enviado
```

## 6. Pricing Intelligence

Exemplo internacional fictício:

```text
Preço externo: US$ 120
Custo trazer: US$ 100
Dólar referência: R$ 5,00
Buffer: 5% → R$ 5,25
Custo BRL: (120 + 100) × 5,25 = R$ 1.155,00
Preço base LK: R$ 1.155,00 × 2 = R$ 2.310,00
Preço psicológico possível: R$ 2.299,99 ou R$ 2.349,99
```

Recomendação: não alterar preço publicado sem validar demanda, preço atual, estoque e risco de conversão. Se a reposição ficou mais cara e o produto continua vendendo, preparar proposta de aumento para aprovação.

## 7. Aprovações pendentes

```text
[ ] Aprovar checagem Droper.app para New Balance 860 37/38.
[ ] Aprovar rascunho de mensagem para LK.Sneakers | Compras sobre New Balance 860 38.
[ ] Aprovar investigação de status do pedido/tag encomenda para Onitsuka 36.
[ ] Aprovar análise CRO do PDP com estoque/tamanho pouco claro.
```

## 8. O que não foi feito

- Nenhum fornecedor/revendedor foi contatado.
- Nenhum grupo WhatsApp foi acionado.
- Nenhum item Notion foi criado.
- Nenhum preço foi alterado.
- Nenhum estoque Shopify/Tiny foi mexido.
