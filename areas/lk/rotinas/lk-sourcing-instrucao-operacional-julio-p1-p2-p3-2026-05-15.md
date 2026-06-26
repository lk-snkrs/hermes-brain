# LK Sourcing — Instrução operacional curta para Júlio (P1/P2/P3)

Status: `preview_operacional_interno`
Data: 2026-05-15
Contexto: LK Sneakers / Compras / Reposição / Encomendas

## Veredito

Esta é a regra curta para Júlio operar a fila de sourcing sem depender de interpretação solta do Hermes.

Hermes organiza evidência, ranking e cards. Júlio/humano confirma disponibilidade, preço final, logística e executa compra/log Notion quando fizer sentido.

## Como ler prioridade

### P1 — agir primeiro

Usar quando o card tem:

- venda/demanda real recente ou pedido/encomenda clara;
- Tiny zerado/baixo ou risco de ruptura no tamanho exato;
- preço atual LK suficiente para margem saudável;
- preço Droper ou StockX/GOAT validado por tamanho exato;
- rota recomendada clara.

Ação humana esperada:

1. confirmar se a oferta ainda está disponível;
2. confirmar preço final e frete/logística;
3. comprar somente se margem e prazo ainda fizerem sentido;
4. registrar no Notion/LK Compras conforme processo normal.

### P2 — acompanhar / validar antes de comprar

Usar quando há oportunidade, mas falta uma confirmação:

- preço mudou ou precisa segunda validação;
- margem boa, mas lead time/rota ainda incerta;
- estoque Tiny está baixo, mas não é ruptura crítica;
- demanda existe, mas não é tão forte quanto P1.

Ação humana esperada:

1. checar disponibilidade e prazo;
2. comparar alternativa nacional vs importada;
3. promover para P1 se o custo/prazo melhorar;
4. não comprar se a margem cair.

### P3 — backlog / monitorar

Usar quando:

- houve só 1 venda em 120 dias;
- margem está fraca;
- produto/tamanho é ambíguo;
- não existe preço exato confiável;
- rota de compra não está clara.

Ação humana esperada:

- não comprar agora;
- deixar em monitoramento;
- revisitar se houver nova venda, pedido de cliente ou queda relevante de custo.

## Campos que mandam na decisão

1. Preço Droper no tamanho exato, quando existir.
2. Menor StockX/GOAT no tamanho exato, após conversão BR → US quando aplicável.
3. Custo do produto / custo landed.
4. Preço atual no site LK por variante/SKU.
5. Margem estimada contra preço atual LK.
6. Lead time real por canal quando confirmado.

Preço médio vendido em 120 dias é contexto de demanda, não é o preço usado para decidir margem.

## O que Júlio não precisa preencher

- Júlio não preenche preço StockX/GOAT manualmente para o Hermes.
- Se falta preço exato por tamanho, o status correto é: `Hermes validar preço/tamanho`.
- Se o preço não está confiável, o card não deve virar P1 de compra.

## Guardrails

Hermes não executa:

- compra;
- reserva;
- pagamento;
- contato com vendedor/fornecedor;
- WhatsApp para grupo de compras;
- alteração Shopify;
- alteração Tiny;
- alteração Merchant/GMC;
- criação automática de card Notion sem aprovação/scope.

## Texto curto para Júlio

```text
Júlio, usar assim:
P1 = checar agora e comprar só se preço final/logística mantiverem a margem.
P2 = validar preço/prazo antes de decidir; pode virar P1 se melhorar.
P3 = não comprar agora; monitorar.

Decisão principal: preço Droper ou StockX/GOAT por tamanho exato + custo total + preço atual LK.
Preço médio antigo é só histórico, não define margem.
Se faltar preço exato, não preencher manualmente: deixar como Hermes validar preço/tamanho.
Hermes não compra, não reserva, não paga e não manda mensagem para fornecedor.
```

## Não executado

- Nenhuma compra.
- Nenhuma reserva.
- Nenhum contato externo.
- Nenhum WhatsApp/e-mail.
- Nenhum write em Shopify, Tiny, Merchant, Notion, Klaviyo ou banco de produção.
