---
title: LK Stock Routing Canon — Pronta Entrega e Estoque
date: 2026-06-08T17:58:21Z
status: active
owner: lk-stock
external_writes: 0
secret_values_printed: false
---

# LK Stock Routing Canon — Pronta Entrega e Estoque

## Decisão canônica

Sempre que qualquer agente da LK precisar saber **estoque**, **disponibilidade**, **pronta entrega**, **tem na loja?**, **ruptura**, **baixo estoque**, **grade/tamanho disponível**, **fila de reposição/transferência/compra** ou **corrigir divergência de estoque/SKU**, o dono obrigatório é o perfil:

- `[LK] Estoque Loja Física` / `lk-stock`

Nenhum outro agente LK deve responder estoque/pronta entrega por conta própria como fonte final.

## Regra de roteamento para todos os agentes LK

1. Detectou intenção de estoque/pronta entrega/disponibilidade por produto/SKU/tamanho?
2. Encaminhe para `lk-stock` ou crie handoff para `areas/lk/sub-areas/stock/`.
3. `lk-stock` resolve com Tiny / `LK | CONTROLE ESTOQUE` como fonte de verdade.
4. O agente solicitante só usa a resposta do `lk-stock` como evidência; não recalcula, não inventa e não promete disponibilidade.
5. Se a pergunta for atendimento/cliente, `lk-ops` pode preparar a resposta, mas o fato de estoque precisa vir do `lk-stock`.

## Remoção de responsabilidade do LK Ops/Atendimento

`lk-ops` / Atendimento não é mais o dono de mapeamento/correção de estoque. Quando houver divergência SKU Shopify ↔ Tiny, estoque pai/filho, variação/tamanho, pronta entrega ou erro de resolver, `lk-ops` deve abrir handoff obrigatório para `lk-stock`.

`lk-ops` pode continuar dono de:

- atendimento;
- copy/rascunho ao cliente;
- triagem de pedido;
- canal WhatsApp/Chatwoot;
- pós-venda;
- resposta final depois que `lk-stock` retornar a evidência.

Mas não deve manter como responsabilidade própria:

- mapear estoque final;
- corrigir resolver Tiny/Shopify de disponibilidade;
- prometer pronta entrega sem evidência `lk-stock`;
- decidir reposição/transferência/compra sem handoff `lk-stock`.

## Contrato mínimo do handoff para LK Stock

Todo handoff deve incluir, quando disponível:

- produto/modelo;
- SKU;
- tamanho/variante;
- canal/origem da pergunta;
- urgência: cliente aguardando, operação interna, relatório, campanha, reposição;
- evidência já conhecida: pedido Shopify, mensagem, link, print/arquivo, SKU Tiny/Shopify;
- ação desejada: confirmar pronta entrega, listar grade disponível, investigar divergência, avaliar ruptura, preparar fila.

## Resposta segura quando a fonte ainda não voltou

> Vou confirmar com o LK Stock, que é o dono de estoque/pronta entrega da LK. Não vou afirmar disponibilidade até ele validar no Tiny / LK | CONTROLE ESTOQUE por SKU e tamanho.

## Guardrails

- Tiny é fonte de verdade; Shopify é superfície/gatilho/contexto.
- Estoque/pronta entrega é variante/tamanho-level, não product-level.
- Sem reserva, promessa ao cliente, compra, fornecedor, Tiny write ou Shopify inventory write sem aprovação escopada.
- Secrets ficam em Doppler; nunca imprimir valores.
