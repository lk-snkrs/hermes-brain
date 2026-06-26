# Receipt — LK WhatsApp responder / vendas por SKU base

Data: 2026-05-26  
Área: LK Operações / WhatsApp responder  
Status: corrigido e verificado

## Pedido limpo
Lucas perguntou se o Hermes saberia responder variações como:

> quantos u204lmmc venderam nos últimos 3 meses

## Causa / lacuna

Antes da correção:

- `venderam` não estava entre os termos que classificavam a pergunta como vendas;
- `últimos 3 meses` caía no fallback de 30 dias;
- o responder de vendas mostrava resumo/top produtos, mas não agregava vendas por SKU base/variações;
- a consulta Shopify usava apenas a primeira página de pedidos, o que poderia subcontar janelas maiores.

## Correção aplicada

Arquivo alterado:

- `/opt/data/scripts/lk_hermes_whatsapp_responder.py`

Mudanças:

- `venderam`, `vendido`, `vendidos` adicionados aos termos de venda.
- Parser de janela agora entende `últimos N meses` e `últimos N dias`.
- Nova extração de SKU em perguntas de vendas.
- Perguntas por SKU base agregam line items cujo SKU é igual ao base ou começa com `BASE-` / `BASE `.
- Resultado por SKU mostra unidades, pedidos, receita bruta dos itens e quebra por tamanho/variante.
- Shopify orders agora pagina via header `Link`, evitando limite de 250 pedidos em janelas maiores.

Teste atualizado:

- `/opt/data/scripts/lk_hermes_whatsapp_responder_selftest.py`

## Resultado verificado

Consulta testada localmente com Shopify read-only:

```text
quantos u204lmmc venderam nos últimos 3 meses
```

Resposta atual:

```text
U204LMMC vendeu **37 un.** em **36 pedido(s)** (últimos 3 meses, geral, Shopify ao vivo).
Receita bruta dos itens: **R$ 103.599,63**.
Por tamanho/variante:
• 34 (`U204LMMC-1`): 2 un., R$ 5.599,98
• 35 (`U204LMMC-2`): 7 un., R$ 19.599,93
• 36 (`U204LMMC-3`): 7 un., R$ 19.599,93
• 37 (`U204LMMC-4`): 8 un., R$ 22.399,92
• 38 (`U204LMMC-5`): 5 un., R$ 13.999,95
• 39 (`U204LMMC-6`): 4 un., R$ 11.199,96
• 40 (`U204LMMC-7`): 2 un., R$ 5.599,98
• 41 (`U204LMMC-8`): 1 un., R$ 2.799,99
• 42 (`U204LMMC-9`): 1 un., R$ 2.799,99
Fonte: Shopify Admin API em tempo real; pedidos cancelados/pendentes fora do total.
```

## Verificações

- `python3 -m py_compile` no responder e selftest → OK.
- Selftest parser/offline → OK.
- Selftest live Tiny read-only → OK.
- Teste Shopify read-only da pergunta real → OK.
- Responder reiniciado localmente na porta `127.0.0.1:8787`.
- POST local `/wacli` retornou `200 ok`.

## Limites

- Sem write em Shopify/Tiny.
- Sem contato externo.
- Sem promessa para cliente.
- Fonte de vendas: Shopify Admin API read-only no momento do teste.
