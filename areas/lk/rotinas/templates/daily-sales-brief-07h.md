# Template — Daily Sales Brief LK 07h

Status: template read-only v0.1.
Uso: briefing diário interno para Lucas/equipe, antes de qualquer cron ou integração de escrita.
Não faz: envio WhatsApp, Klaviyo, Shopify, Notion, campanha, alteração de preço, alteração de estoque ou contato externo.

## Regras de execução

- Fonte oficial de vendas/clientes/source: Shopify.
- Fonte oficial de estoque: Tiny / `LK controle de stock`.
- Conversão online: Shopify Analytics como baseline principal; GA4 como apoio.
- Dados pessoais devem ser mascarados no Telegram por padrão.
- Toda recomendação precisa separar fato, leitura e ação sugerida.
- Se não houver sinal relevante, dizer isso; não inventar ação.
- Ação externa exige preview e aprovação explícita.

## Prompt operacional

```text
Gere o Daily Sales Brief da LK para o período [DATA_INÍCIO] até [DATA_FIM].
Use somente dados disponíveis/read-only.
Não altere Shopify, Tiny, Notion, Klaviyo, WhatsApp, Meta, Google, n8n ou qualquer sistema produtivo.

Objetivo:
- resumir vendas, conversão, produtos, tamanhos, estoque e sinais comerciais;
- detectar oportunidades de recompra, stock, preço, conteúdo e CRO;
- listar aprovações necessárias;
- não executar ações.
```

## Output esperado

### 1. Resumo executivo

```text
Ontem a LK vendeu [R$ X] em [N] pedidos.
Online: [R$ X / N pedidos]. Loja física: [R$ X / N pedidos].
Conversão online: [X%] vs baseline [0,13%] e meta [0,20%].
Leitura principal: [1 frase].
Ação recomendada nº 1: [ação].
```

### 2. Vendas Shopify

- Receita total:
- Pedidos:
- Ticket médio:
- Online:
- Loja física:
- Source/canal:
- Variação vs média 7 dias:
- Anomalias:

### 3. Conversão e CRO

- Conversão online Shopify Analytics:
- Sessões:
- Add to cart:
- Checkout iniciado:
- Compra:
- Páginas/produtos com tráfego e baixa conversão:
- Hipótese principal:
- Teste sugerido:
- Aprovação necessária:

### 4. Produtos/modelos/tamanhos vendidos

Para cada produto relevante:

```text
Produto/modelo:
Marca:
Tamanhos vendidos:
Canal/source:
Influencer/campanha/UTM, se houver:
Status estoque Tiny por tamanho:
Status comercial: pronta entrega aparente / encomenda BR / encomenda US / divergente / desconhecido
Leitura:
Ação sugerida:
Confiança: alta/média/baixa
```

### 5. Centro de Inteligência de Stock

- Produtos com risco de ruptura:
- Produtos com lead time maior que cobertura:
- Produtos que devem acionar busca de fonte/restock:
- Produtos para jogar no `LK.Sneakers | Compras` após aprovação:
- Produtos com estoque alto e venda lenta:
- Divergências Shopify × Tiny × pedido:

### 6. Recompra / CRM

- Vendas que geram oportunidade de segunda compra:
- Clientes elegíveis para recompra 90 dias:
- Segmentos por marca/tamanho:
- Sugestão Klaviyo:
- Sugestão WhatsApp loja física:
- Aprovação necessária antes de enviar:

### 7. Pricing signals

- Produto vendido com reposição mais cara que preço atual:
- Produto com StockX/KicksDev/Droper relevante:
- Sugestão de aumento:
- Sugestão de não mexer:
- Risco de conversão:
- Aprovação necessária:

### 8. Conteúdo/campanha

- Sinal que virou pauta:
- Formato recomendado: blog / PDP / newsletter / Instagram / WhatsApp / Klaviyo:
- Precisa seguir DesignMD LK:
- Link/produto relacionado:
- Aprovação necessária:

### 9. Aprovações pendentes

Liste em formato curto:

```text
[ ] Aprovar alerta para compras — motivo — risco — destino
[ ] Aprovar draft Klaviyo — motivo — segmento — risco
[ ] Aprovar ajuste preço — produto/tamanho — de/para — motivo
[ ] Aprovar blog/PDP — produto — motivo SEO/comercial
```

### 10. O que não vou fazer sozinho

- Não enviar WhatsApp/Klaviyo.
- Não publicar blog/produto/tema.
- Não alterar preço/estoque.
- Não comprar nem acionar fornecedor.
- Não criar item Notion de compra real sem aprovação.

## Checklist de qualidade

- [ ] Separou fatos de interpretação.
- [ ] Usou Tiny para estoque, não Shopify.
- [ ] Trabalhou por produto/modelo/tamanho quando necessário.
- [ ] Mascarou dados pessoais.
- [ ] Indicou confiança e dados faltantes.
- [ ] Terminou com aprovações, não com ações executadas.
