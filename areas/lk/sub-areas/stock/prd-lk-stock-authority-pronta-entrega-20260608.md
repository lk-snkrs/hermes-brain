---
title: PRD — LK Stock como autoridade obrigatória de estoque/pronta entrega
date: 2026-06-08T18:03:43Z
status: proposed
owner: lk-stock
stakeholders:
  - lk-stock
  - lk-ops
  - lk-shopify
  - lk-growth
  - lk-content
  - lk-collection-optimizer
  - lk-trends
  - lk-analyst-readonly
external_writes: 0
secret_values_printed: false
---

# PRD — LK Stock como autoridade obrigatória de estoque/pronta entrega

## 1. Contexto

Lucas definiu que, na LK, qualquer necessidade de saber **estoque** ou **pronta entrega** deve ser respondida pelo agente `[LK] Estoque Loja Física` / `lk-stock`.

Antes, `lk-ops`/Atendimento tinha referências e rotinas que permitiam resolver disponibilidade, mapear SKU/produto/tamanho e corrigir divergências de estoque usando fluxos próprios. Isso cria risco operacional:

- prometer disponibilidade sem a evidência correta;
- misturar atendimento com controle de estoque;
- usar Shopify/local catalog como proxy indevido de estoque;
- duplicar lógica de resolver SKU/Tiny/Shopify em vários agentes;
- gerar respostas divergentes entre atendimento, growth, conteúdo, Shopify e estoque.

A melhoria proposta centraliza a autoridade de estoque no `lk-stock`, mantendo os demais agentes como consumidores/handoff requesters.

## 2. Objetivo

Transformar `lk-stock` na autoridade operacional obrigatória para:

- estoque físico;
- pronta entrega;
- disponibilidade por SKU/tamanho;
- ruptura/baixo estoque;
- best sellers disponíveis na loja;
- fila de reposição, transferência e compra;
- divergência SKU/Tiny/Shopify que afete disponibilidade;
- correção de mapeamento/resolve de estoque.

## 3. Não objetivos

Este PRD **não** autoriza:

- writes em Tiny;
- writes em Shopify inventory;
- reserva de produto;
- promessa ao cliente;
- compra/reposição automática;
- contato com fornecedor;
- envio WhatsApp/email/campanha;
- mudança em Docker/VPS/gateway sem aprovação escopada.

Este PRD define roteamento, contrato e melhoria de fluxo. Execução externa permanece dependente de approval packet.

## 4. Fonte de verdade

- Tiny / `LK | CONTROLE ESTOQUE`: fonte de verdade de estoque.
- Shopify: superfície, evento, catálogo/contexto e venda; não é estoque final.
- Catálogo/local DB/cache: pode ajudar a resolver candidato SKU/tamanho, mas não substitui a evidência do `lk-stock`.

## 5. Regra canônica de roteamento

Qualquer agente LK que detectar intenção de estoque deve rotear obrigatoriamente para `lk-stock`.

Intenções cobertas:

- “tem na loja?”;
- “pronta entrega?”;
- “qual estoque?”;
- “quantos pares?”;
- “tem tamanho 38?”;
- “está zerado?”;
- “baixo estoque?”;
- “o que repor?”;
- “qual grade disponível?”;
- “produto vendido ficou sem estoque?”;
- “SKU não bate Tiny/Shopify?”;
- “mapear/corrigir disponibilidade?”;
- “fila de compra/transferência/reposição?”.

## 6. Papéis por agente

### `lk-stock`

Dono obrigatório de:

- consulta e interpretação de estoque/pronta entrega;
- evidência por SKU/tamanho;
- validação Tiny / `LK | CONTROLE ESTOQUE`;
- análise de ruptura/baixo estoque;
- fila operacional de reposição/transferência/compra;
- correção ou decisão de mapeamento de estoque.

### `lk-ops` / Atendimento

Dono de:

- atendimento;
- WhatsApp/Chatwoot;
- triagem operacional;
- rascunho de resposta ao cliente;
- pós-venda;
- handoff para estoque quando houver disponibilidade/pronta entrega.

Removido do `lk-ops`:

- resolver estoque final por conta própria;
- manter mapeamento/correção de disponibilidade como função própria;
- prometer pronta entrega sem retorno do `lk-stock`;
- decidir reposição/transferência/compra sem `lk-stock`.

### `lk-shopify`

Pode fornecer:

- catálogo;
- variante;
- pedido/evento;
- contexto de SKU/handle/product ID.

Não pode decidir estoque final sem `lk-stock`.

### `lk-growth`, `lk-content`, `lk-trends`, `lk-collection-optimizer`, `lk-analyst-readonly`

Podem usar estoque como sinal para campanha, conteúdo, tendência, coleção ou análise, mas devem buscar evidência via `lk-stock` antes de recomendar ação dependente de disponibilidade.

## 7. Contrato de handoff para LK Stock

Todo handoff deve carregar, quando disponível:

- solicitante: agente/origem;
- pergunta original;
- produto/modelo;
- SKU Shopify/Tiny, se conhecido;
- tamanho/variante;
- link Shopify/handle/product ID/variant ID, se houver;
- canal: Telegram, WhatsApp, Chatwoot, Shopify, relatório, campanha;
- urgência: cliente aguardando, interno, rotina, campanha, reposição;
- evidência já coletada;
- ação desejada:
  - confirmar pronta entrega;
  - listar grade disponível;
  - investigar divergência;
  - avaliar ruptura;
  - sugerir reposição/transferência/compra;
  - preparar response payload para atendimento.

## 8. Resposta padrão enquanto aguarda LK Stock

Para atendimento/cliente interno:

```text
Vou confirmar com o LK Stock, que é o dono de estoque/pronta entrega da LK. Não vou afirmar disponibilidade até ele validar no Tiny / LK | CONTROLE ESTOQUE por SKU e tamanho.
```

Para relatório/gestão:

```text
Bloqueado por evidência de estoque: demanda roteada ao LK Stock para validação Tiny por SKU/tamanho antes de recomendação operacional.
```

## 9. Melhorias necessárias

### M1 — Canon de roteamento em todos os agentes LK

Adicionar regra obrigatória nos perfis LK:

- `lk-analyst-readonly`;
- `lk-collection-optimizer`;
- `lk-content`;
- `lk-content-reviewer`;
- `lk-growth`;
- `lk-ops`;
- `lk-shopify`;
- `lk-stock`;
- `lk-trends`.

Status inicial: aplicado em `SOUL.md`/`MEMORY.md`/`AGENTS.md`/`TOOLS.md` quando existentes.

### M2 — Remover ownership de mapeamento do `lk-ops`

Substituir instruções de `lk-ops` que tratavam estoque/availability como responsabilidade própria.

Novo comportamento:

- `lk-ops` identifica produto/SKU/tamanho;
- abre handoff para `lk-stock`;
- espera evidência;
- só então prepara resposta final ao cliente/equipe.

Status inicial: memória, SOUL e skills locais do `lk-ops` atualizadas.

### M3 — Transformar responder legado em consumer de `lk-stock`

O responder `lk_hermes_whatsapp_responder.py` e referências relacionadas devem migrar de “resolver estoque final” para “montar pergunta/contrato e consumir resposta `lk-stock`”.

Fases:

1. manter fallback seguro atual sem promessa;
2. adicionar detector de intenção de estoque que cria handoff `lk-stock`;
3. fazer resposta final usar payload validado pelo `lk-stock`;
4. aposentar caminho antigo como “legacy QA/local resolver”, não como autoridade.

### M4 — Payload estruturado de resposta do LK Stock

`lk-stock` deve responder em formato utilizável por outros agentes:

```json
{
  "status": "available|unavailable|needs_review|blocked",
  "product": "...",
  "sku": "...",
  "size": "...",
  "quantity": 0,
  "source": "Tiny / LK | CONTROLE ESTOQUE",
  "freshness": "...",
  "confidence": "high|medium|low",
  "evidence": ["..."],
  "safe_customer_copy": "...",
  "guardrails": ["no reservation", "no price/delivery promise", "no external write"]
}
```

### M5 — Handoff/receipt obrigatório para divergência

Se `lk-stock` encontrar divergência de mapeamento:

- SKU Shopify existe, Tiny sem código;
- Tiny duplicado;
- tamanho divergente;
- parent/child confuso;
- depósito errado;
- produto sem correspondência;

então deve gerar fila/receipt em `areas/lk/sub-areas/stock/` com classificação e próxima ação. Writes continuam bloqueados até aprovação.

### M6 — Verificação e testes

Adicionar/ajustar testes locais para garantir:

- prompts de estoque em `lk-ops` não tentam finalizar estoque sem `lk-stock`;
- `lk-shopify` não trata inventário Shopify como verdade final;
- todos os agentes LK possuem a regra de roteamento;
- handoff mínimo contém produto/SKU/tamanho/origem/ação desejada;
- resposta ao cliente só contém disponibilidade quando evidência do `lk-stock` existir.

## 10. Critérios de aceite

A melhoria será considerada aceita quando:

1. Todos os perfis LK tiverem instrução explícita de roteamento para `lk-stock`.
2. `lk-ops` não tiver mais instrução de ownership de estoque/availability/mapeamento como responsabilidade própria.
3. `lk-ops`/Atendimento usar `lk-stock` para corrigir divergência de estoque/SKU/Tiny/Shopify.
4. O Brain tiver referência canônica de roteamento e PRD linkado.
5. Houver receipt sanitizado com arquivos alterados e validações.
6. Secret scan focado retornar 0 hits reais.
7. Brain health passar sem erro.
8. Nenhum write externo tiver sido executado.

## 11. Riscos

- Legacy scripts ainda podem conter lógica local de resolver estoque. Mitigação: marcá-los como legado/consumer e migrar por fase.
- Agentes podem responder de memória antiga. Mitigação: atualizar `MEMORY.md`, `SOUL.md`, skills locais e watchdog de memória.
- Handoff pode ser lento para atendimento. Mitigação: resposta segura interim + contrato estruturado para acelerar `lk-stock`.
- Dependência de Tiny credencial/runtime. Mitigação: diferenciar secret presente, runtime não injetado e integração indisponível; nunca imprimir valores.

## 12. Rollout sugerido

### Fase 0 — Já aplicado nesta sessão

- canon Brain criado;
- perfis LK ensinados;
- `lk-ops` corrigido;
- watchdog de memória corrigido;
- PRD criado.

### Fase 1 — Implementação de handoff estruturado

- criar função/template único de handoff `stock_request`;
- garantir que `lk-ops`/responder gere esse payload.

### Fase 2 — Integração operacional LK Stock

- `lk-stock` responde com payload JSON + copy segura;
- `lk-ops` consome e monta mensagem final.

### Fase 3 — Retirada de legacy resolver como autoridade

- scripts legados viram apenas normalização/candidato;
- disponibilidade final sempre depende do `lk-stock`.

## 13. Decisão operacional

A partir desta regra, quando Lucas ou qualquer fluxo LK perguntar por estoque/pronta entrega, a resposta correta dos agentes deve ser:

> Isso precisa passar pelo LK Stock. Vou rotear produto/SKU/tamanho para ele e só responder disponibilidade depois da validação Tiny / LK | CONTROLE ESTOQUE.
