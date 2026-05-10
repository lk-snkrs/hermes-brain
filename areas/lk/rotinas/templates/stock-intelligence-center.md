# Template — Stock Intelligence Center LK

Status: template read-only v0.1.
Uso: diagnóstico interno para prever ruptura, reposição, compra, encomenda, pricing e sourcing.
Não faz: compra, contato com fornecedor, mensagem em grupo, criação Notion, alteração Shopify/Tiny.

## Objetivo

Transformar vendas Shopify + estoque Tiny + disponibilidade externa + lead time em recomendações por produto/modelo/tamanho.

O centro deve responder:

- o que está vendendo;
- o que vai acabar;
- quanto tempo o estoque cobre;
- quanto tempo demora para repor;
- se vale comprar agora;
- qual fonte checar;
- se o preço precisa mudar;
- se a recomendação é comprar, esperar, não mexer ou desovar.

## Regras

- Granularidade obrigatória: marca → modelo → produto/cor → tamanho/variante.
- Estoque oficial: Tiny / depósito `LK | CONTROLE ESTOQUE`.
- Shopify informa venda/pedido/source, mas não manda no estoque.
- Encomenda BR/US é classificação humana marcada no contexto do pedido Shopify; o sistema sugere, não decide sozinho.
- Droper.app, StockX, KicksDev, GOAT, Flight Club, retailers e revendedores são fontes de sourcing, não concorrentes a monitorar continuamente.
- Buscar fontes externas só quando houver sinal interno ou oportunidade de tendência. Exemplo: produto/tamanho vendeu bem, Tiny está zerado/baixo, e uma fonte relevante parece ter restock.
- Para Brasil, incluir Droper e Monbam/grupos de revendedores quando fizer sentido; preparar mensagem, mas não postar sem aprovação.

## Fórmulas v0.1

```text
velocidade_venda_diaria = unidades_vendidas_periodo / dias_periodo

dias_de_cobertura = estoque_livre / velocidade_venda_diaria

risco_ruptura = dias_de_cobertura <= lead_time_reposicao
```

Lead times padrão, até discovery refinado:

- Brasil: 3–7 dias.
- Fora/US: ~30 dias.
- StockX/KicksDev internacional: ~30 dias.
- Revendedor/pessoa: variável; confirmar manualmente.

## Input mínimo

```text
Produto/modelo:
Marca:
Cor:
Tamanho/variante:
Vendas 7d:
Vendas 30d:
Vendas 90d:
Estoque Tiny físico:
Estoque livre estimado:
Status pedido/tag: sem encomenda / encomenda BR / encomenda US / desconhecido, sempre como sinal humano do pedido
Preço LK atual:
Preço externo, se consultado:
Fonte externa:
Lead time esperado:
```

## Output por item

```text
Produto/modelo/tamanho:
Status: saudável / atenção / risco ruptura / zerado / estoque alto lento / divergente
Estoque livre:
Velocidade venda:
Cobertura estimada:
Lead time reposição:
Fonte recomendada para checar:
Preço reposição estimado:
Preço LK atual:
Preço LK sugerido, se aplicável:
Recomendação: comprar para repor estoque / checar fonte / não comprar / subir preço / manter / preparar conteúdo / investigar divergência
Confiança: alta/média/baixa
Dados faltantes:
Aprovação necessária:
```

## Blocos do relatório

### 1. Risco de ruptura

Produtos/tamanhos onde cobertura estimada é menor ou igual ao lead time.

```text
Produto:
Tamanho:
Estoque livre:
Vendas 30d:
Cobertura:
Lead time:
Recomendação:
```

### 2. Zeros importantes

Produtos vendidos recentemente e zerados no Tiny.

- Checar Droper.app se for Brasil.
- Checar StockX/KicksDev se for fora.
- Sugerir mensagem para `LK.Sneakers | Compras`, mas não enviar sem aprovação.

### 3. Compra antes de acabar

Produtos com estoque ainda positivo, mas cobertura apertada.

Exemplo de leitura:

```text
Temos 2 unidades livres, vendemos ~2/mês e reposição fora leva ~30 dias.
Se quisermos evitar ruptura, a compra precisa ser decidida agora.
```

### 4. Estoque alto e venda lenta

Separar:

- produto bom com comunicação fraca;
- preço travando conversão;
- tamanho difícil;
- compra errada;
- falta de tráfego;
- precisa conteúdo/campanha;
- não mexer.

### 5. Restock externo acionado por demanda interna

Usar apenas quando:

- produto vendeu bem;
- estoque LK está baixo/zerado;
- há sinal de restock externo;
- preço e prazo podem fazer sentido.

### 6. Pricing Intelligence

Fórmula internacional v0.1:

```text
preco_base = (preco_usd + custo_trazer_usd) × (dolar_atual × 1,05) × 2
preco_lk = arredondamento LK para final 49,99 ou 99,99
```

Sugerir aumento quando:

- produto vendeu recentemente;
- estoque baixo;
- reposição está cara;
- demanda/conversão não parecem ruins.

Não sugerir aumento quando:

- produto está parado;
- conversão já está ruim;
- estoque alto e velho;
- objetivo é girar capital.

### 7. Aprovações

```text
[ ] Aprovar checagem/fonte manual
[ ] Aprovar mensagem para LK.Sneakers | Compras
[ ] Aprovar criação de item em LK Compras
[ ] Aprovar criação de item em LK Encomendas
[ ] Aprovar alteração de preço
[ ] Aprovar conteúdo/campanha derivada
```

## Checklist de qualidade

- [ ] A recomendação está por tamanho/variante.
- [ ] Tiny foi usado como estoque oficial.
- [ ] Status de encomenda foi tratado como humano/curatorial.
- [ ] Lead time foi explicitado.
- [ ] A sugestão pode ser “não comprar”.
- [ ] Toda ação externa ficou pendente de aprovação.
