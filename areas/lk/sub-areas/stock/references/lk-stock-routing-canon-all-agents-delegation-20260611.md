---
title: LK Stock all-agent delegation canon
created_at: 2026-06-11T20:19:29.854853+00:00
status: active
owner: lk-stock
external_writes: 0
secret_values_printed: false
---

# LK Stock all-agent delegation canon

## Decisão de Lucas

Lucas corrigiu a arquitetura: **todos os agentes devem tratar o `[LK] Estoque Loja Física` / `lk-stock` como o único dono de consulta de estoque da LK**.

A regra não é apenas “usar DB local primeiro”. A regra transversal é:

- agentes que não são `lk-stock` **não consultam estoque diretamente** em Tiny, Shopify, Stock OS DB local, relatórios antigos, caches ou planilhas próprias;
- eles coletam produto/SKU/tamanho/contexto e solicitam a validação ao `lk-stock`;
- só usam disponibilidade, ruptura, grade/tamanho, pronta entrega ou divergência SKU/Tiny/Shopify depois que o `lk-stock` retornar evidência;
- se a evidência não vier suficiente, a resposta correta é `não confirmado` + reconciliação, não promessa.

## Exceção autorizada

O próprio `lk-stock` pode consultar a Stock OS DB local como caminho quente primário, porque esta é a base local operacional dele. Tiny/Olist alimenta/reconcilia essa base por webhooks diurnos e full sync noturno, e Tiny / `LK | CONTROLE ESTOQUE` segue como verdade operacional por trás da base.

## Agentes ensinados

A regra deve estar em:

- profile-local `AGENTS.md` de todos os perfis relevantes;
- Brain `agentes/*/AGENTS.md` e subáreas LK;
- routing skill central `multiempresa-routing-lucas`;
- skill operacional LK;
- receipts/handoffs futuros quando houver decisão material envolvendo estoque.

## Frase segura padrão

> Vou rotear para o LK Stock, que é o dono de estoque/pronta entrega. Só respondo disponibilidade depois da validação dele por SKU/tamanho.

## Guardrails

- Tiny write: 0 sem aprovação escopada.
- Shopify inventory/product write: 0 sem aprovação escopada.
- Reserva, compra, fornecedor ou promessa pública: 0 sem aprovação escopada.
- Atendimentos/campanhas podem preparar copy, mas o fato de estoque precisa vir do `lk-stock`.
