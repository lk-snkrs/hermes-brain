# PRD — LK WhatsApp Hermes: Base local Tiny por webhook + full sync diário

**Data:** 2026-06-01T12:17:24+00:00  
**Área:** LK Sneakers / Atendimento / WhatsApp Hermes / Estoque  
**Status:** PRD v1 — aguardando aprovação de execução  
**Owner operacional:** LK Ops / Atendimento  
**Fonte de verdade:** Tiny, depósito `LK | CONTROLE ESTOQUE`  

---

## 1. Contexto

As pesquisas live no Tiny podem levar cerca de 2 minutos em casos de família/modelo amplo, por exemplo perguntas como:

- `@Hermes você tem Onitsuka 38?`
- `@Hermes quais pares 9060 temos?`
- `@Hermes quais modelos e tamanhos de Slide Nike Mind temos?`

Para atendimento, esse tempo é ruim: o vendedor precisa de resposta rápida no WhatsApp. Ao mesmo tempo, não podemos inventar estoque nem calcular saldo por delta local.

Já existe um caminho inicial de snapshot local SQLite para respostas rápidas. A evolução correta é transformar isso em um espelho operacional do Tiny:

1. **Webhook/event-driven** para atualizar SKUs afetados quando houver venda/cancelamento/evento Shopify.
2. **Full sync diário read-only Tiny → SQLite** para corrigir drift, perdas de webhook, erros transitórios e SKUs que não tiveram evento.
3. **Responder WhatsApp lendo primeiro a base local fresca**, e só caindo para Tiny live/manual quando a base local estiver ausente, velha ou ambígua.

---

## 2. Problema

Hoje, existem três riscos:

1. **Lentidão operacional:** consulta live ampla no Tiny pode demorar ~2 minutos.
2. **Baixa cobertura local:** snapshot local ainda é parcial; quando não existe registro fresco, o bot cai em resposta segura, mas não resolve o atendimento.
3. **Risco de drift:** uma base local parcial ou não reconciliada pode envelhecer se depender só de leituras ocasionais.

---

## 3. Objetivo

Construir uma base local de estoque Tiny para o WhatsApp Hermes que responda a perguntas de produto/modelo/tamanho em menos de 2 segundos na maioria dos casos, mantendo Tiny como fonte de verdade.

A resposta deve informar:

- total de pares validados;
- modelo;
- tamanho;
- SKU;
- quantidade por SKU/tamanho;
- timestamp da última leitura oficial Tiny;
- confiança/freshness;
- aviso interno de que não houve reserva/promessa/alteração de estoque.

---

## 4. Não objetivos

Este PRD **não** autoriza:

- escrever no Tiny;
- alterar estoque Shopify;
- criar webhook real em Shopify;
- ativar cron/produção;
- enviar mensagem externa para cliente;
- prometer disponibilidade, preço, prazo, reserva ou desconto;
- comprar/contatar fornecedor.

Tudo isso exige approval packet separado e aprovação explícita.

---

## 5. Princípios operacionais

1. **Tiny é a verdade.** SQLite local é cache/snapshot operacional, não inventário independente.
2. **Nunca usar delta local.** Evento Shopify nunca faz `saldo = saldo - quantidade` ou `+ quantidade`.
3. **Evento serve para decidir o que reler no Tiny.** Após venda/cancelamento, resolver variante/SKU/tamanho e consultar Tiny; salvar o saldo absoluto retornado.
4. **Full sync diário corrige drift.** Mesmo com webhook, rodar varredura diária para reconciliar tudo.
5. **Responder rápido primeiro.** Se a base local está fresca, responder localmente. Se não está, resposta segura + enfileirar refresh.
6. **Freshness visível.** Toda resposta baseada em SQLite deve mostrar `Última leitura oficial Tiny`.
7. **Fail closed.** Se dado está ambíguo/velho/ausente, não dizer “tem” nem “não tem” como verdade final.

---

## 6. Usuários e casos de uso

### 6.1 Vendedor no WhatsApp

Quer saber rapidamente:

- quantos pares de um modelo existem;
- quais tamanhos;
- qual SKU;
- se existe um tamanho específico.

### 6.2 Atendimento interno

Quer responder cliente sem travar 2 minutos e sem prometer algo errado.

### 6.3 Operação LK

Quer reduzir divergência entre Tiny, Shopify e atendimento, preservando Tiny como fonte de verdade.

---

## 7. Requisitos funcionais

### RF1 — Base local SQLite de estoque Tiny

A base local deve manter, no mínimo:

- SKU canônico;
- Tiny product/variation id quando disponível;
- título/modelo limpo;
- tamanho;
- depósito;
- saldo oficial Tiny no depósito `LK | CONTROLE ESTOQUE`;
- timestamp da leitura oficial Tiny;
- fonte da leitura: `webhook_refresh`, `daily_fullsync`, `manual_refresh`, `read_through`;
- confiança/status: `fresh`, `stale`, `ambiguous`, `missing`, `error`.

### RF2 — Webhook/event-driven refresh

Quando chegar evento Shopify relevante:

- `orders/paid`;
- `orders/cancelled`;
- futuro: refund/restock se aplicável;

O sistema deve:

1. validar assinatura/identidade do evento;
2. resolver order + line item + variant id + SKU + tamanho;
3. consultar Tiny para o SKU/tamanho exato;
4. salvar saldo absoluto Tiny na SQLite;
5. registrar ledger idempotente;
6. opcionalmente preparar preview de espelhamento Shopify, sem executar write sem aprovação.

### RF3 — Full sync diário Tiny → SQLite

Uma vez por dia, rodar reconciliação read-only:

1. listar/consultar SKUs relevantes da LK;
2. consultar Tiny por lotes com throttle seguro;
3. salvar saldo absoluto no SQLite;
4. marcar itens não encontrados/ambíguos;
5. gerar relatório local com:
   - total consultado;
   - total atualizado;
   - erros;
   - stale restantes;
   - famílias mais perguntadas sem cobertura.

### RF4 — Refresh sob demanda em background

Quando o WhatsApp receber pergunta e a base local estiver ausente/stale:

1. responder rápido com fallback seguro;
2. enfileirar refresh Tiny para a família/SKU/tamanho;
3. atualizar SQLite quando terminar;
4. opcionalmente permitir uma segunda resposta interna se o grupo aprovar comportamento futuro.

### RF5 — Responder por família/modelo/tamanho

Para pergunta ampla, exemplo `quais pares 9060 temos?`, responder com agrupamento:

```text
Total validado: X par(es) em Y tamanho(s) (...).

• Modelo: ... — Tamanho: ... (`SKU`): saldo N par(es).
```

Deve limitar saída para não poluir WhatsApp e informar se há mais resultados.

### RF6 — Freshness e fallback

Se leitura local tiver TTL expirado ou fonte incerta:

- não prometer disponibilidade;
- informar que precisa validação live/manual;
- enfileirar refresh;
- nunca retornar falso negativo absoluto.

---

## 8. Requisitos não funcionais

### Performance

- Resposta com SQLite fresco: alvo p95 < 2s.
- Resposta fallback quando ausente/stale: alvo p95 < 5s.
- Live Tiny não deve bloquear o handler WhatsApp por 2 minutos.

### Confiabilidade

- Ledger idempotente para eventos.
- Retentativas com backoff para Tiny.
- Full sync diário para corrigir drift.
- Relatório de erros e stale.

### Segurança

- Segredos apenas via Doppler/arquivos já aprovados; nunca imprimir valores.
- Não expor PII desnecessária no Brain/Telegram.
- Não executar writes externos sem aprovação.

### Observabilidade

Registrar localmente:

- tempo de resposta do responder;
- hit/miss/stale da base local;
- duração das chamadas Tiny;
- erros por tipo;
- número de SKUs atualizados por fonte;
- últimas famílias perguntadas sem cobertura.

---

## 9. Arquitetura proposta

### Componentes

1. **Responder WhatsApp Hermes**
   - Arquivo atual: `/opt/data/scripts/lk_hermes_whatsapp_responder.py`
   - Lê SQLite primeiro.
   - Nunca bloqueia por busca ampla live.

2. **Módulo SQLite Tiny local**
   - Arquivo atual: `/opt/data/scripts/lk_tiny_stock_local_db.py`
   - DB atual: `/opt/data/hermes_bruno_ingest/local_sql/lk_whatsapp_hermes/lk_tiny_stock_local.sqlite`

3. **Processador event-driven dry-run**
   - Arquivo atual/referência: `/opt/data/scripts/lk_shopify_tiny_stock_sync_dryrun.py`
   - Evoluir para refresh absoluto Tiny por evento, inicialmente dry-run/local-only.

4. **Fila local de refresh**
   - Nova tabela ou arquivo SQLite: `refresh_queue`.
   - Estados: `queued`, `running`, `done`, `error`, `skipped_ambiguous`.

5. **Full sync diário**
   - Novo script proposto: `/opt/data/scripts/lk_tiny_stock_fullsync.py`
   - Inicialmente execução manual/read-only; cron só depois de aprovação.

---

## 10. Modelo de dados sugerido

### `stock_by_sku`

Campos mínimos:

- `sku` primary key;
- `canonical_sku`;
- `product_title`;
- `variant_title`;
- `size`;
- `tiny_product_id`;
- `tiny_variation_id`;
- `warehouse_name`;
- `official_available_qty`;
- `last_tiny_read_at`;
- `source`;
- `confidence`;
- `raw_hash`;
- `updated_at`.

### `stock_event_ledger`

- `event_id` / delivery id;
- `topic`;
- `order_id`;
- `line_item_id`;
- `variant_id`;
- `sku`;
- `size`;
- `status`;
- `tiny_read_at`;
- `tiny_qty`;
- `write_executed` default false;
- `error_reason`;
- `created_at`.

### `refresh_queue`

- `id`;
- `query_type`: `sku`, `family`, `product_title`, `size_family`;
- `query_value`;
- `size` nullable;
- `priority`;
- `status`;
- `attempts`;
- `last_error`;
- `created_at`;
- `updated_at`.

### `fullsync_runs`

- `run_id`;
- `started_at`;
- `finished_at`;
- `status`;
- `skus_seen`;
- `skus_updated`;
- `errors`;
- `stale_after_run`;
- `report_path`.

---

## 11. Fluxos principais

### Fluxo A — pergunta com dado fresco

1. WhatsApp: `@Hermes você tem Onitsuka 38?`
2. Resolver termos: família `Onitsuka`, tamanho `38`.
3. Consultar SQLite.
4. Se há leitura Tiny fresca:
   - responder total/modelo/tamanho/SKU/pares;
   - informar última leitura oficial Tiny;
   - não prometer reserva/preço/entrega.

### Fluxo B — pergunta sem dado fresco

1. WhatsApp: `@Hermes quais pares 9060 temos?`
2. SQLite sem saldo fresco ou todos zerados/ambíguos.
3. Responder fallback seguro em poucos segundos.
4. Enfileirar refresh família `9060`.
5. Worker lê Tiny em background e atualiza SQLite.

### Fluxo C — venda Shopify

1. Shopify dispara `orders/paid`.
2. Handler valida evento.
3. Resolve line item SKU/tamanho.
4. Consulta Tiny para o SKU/tamanho.
5. Upsert no SQLite com saldo absoluto Tiny.
6. Registra ledger.
7. Não escreve Shopify sem aprovação/escopo separado.

### Fluxo D — full sync diário

1. Script diário pega catálogo/SKUs relevantes.
2. Consulta Tiny com throttle.
3. Atualiza SQLite com saldos absolutos.
4. Gera relatório local.
5. Falhas viram alerta/receipt, não spam de sucesso.

---

## 12. Critérios de aceite

### CA1 — velocidade

- Perguntas com dado fresco respondem em <2s p95.
- Perguntas sem dado fresco não ficam bloqueadas por chamada Tiny ampla.

### CA2 — exatidão

- Toda disponibilidade positiva vem de leitura Tiny `LK | CONTROLE ESTOQUE`.
- Não há cálculo local de delta.
- Resposta inclui timestamp/fonte.

### CA3 — cobertura

- Famílias prioritárias têm cobertura após full sync:
  - Onitsuka;
  - New Balance 9060;
  - New Balance 204L;
  - Slide Nike Mind;
  - outras famílias mais perguntadas no WhatsApp.

### CA4 — segurança

- Sem writes em Tiny/Shopify.
- Sem criação/alteração de webhooks/crons sem aprovação.
- Sem envio externo ao cliente.

### CA5 — operação

- Existe relatório diário local com updated/stale/errors.
- Existe ledger idempotente de eventos.
- Existe rollback simples: desativar leitura local e voltar ao fallback seguro/live manual.

---

## 13. Plano de implementação em fases

### Fase 0 — PRD e desenho

- Este documento.
- Aprovação do escopo.

### Fase 1 — Local DB hardening read-only

- Consolidar schema SQLite.
- Adicionar freshness/confidence/source.
- Testes unitários para upsert absoluto.
- Responder sempre mostra timestamp Tiny quando usar DB.

### Fase 2 — Full sync manual read-only

- Criar `/opt/data/scripts/lk_tiny_stock_fullsync.py`.
- Rodar manualmente sem cron.
- Gerar relatório local.
- Validar cobertura das famílias prioritárias.

### Fase 3 — Refresh queue background

- Criar fila local.
- Perguntas com miss/stale enfileiram refresh.
- Worker manual/read-only processa fila.
- Responder não bloqueia.

### Fase 4 — Webhook dry-run/local-only

- Conectar eventos Shopify apenas em dry-run/local ledger.
- Validar assinatura, idempotência, blockers.
- Atualizar SQLite só com leitura absoluta Tiny.
- Sem Shopify write.

### Fase 5 — Cron diário full sync

- Só após aprovação explícita.
- Ativar execução diária local/silent-OK.
- Alertar apenas exceções/falhas.

### Fase 6 — Opcional: espelho Shopify inventory

- Fora deste PRD operacional inicial.
- Requer approval packet separado, rollback e verificação live.

---

## 14. Testes mínimos

1. Unitário: upsert absoluto substitui saldo anterior pelo saldo Tiny, sem delta.
2. Unitário: evento duplicado não gera processamento duplicado.
3. Unitário: pergunta por família agrupa por modelo/tamanho/SKU.
4. Unitário: dado stale gera fallback seguro + refresh queue.
5. Smoke CLI:
   - `@Hermes você tem Onitsuka 38?`
   - `@Hermes quais modelos e tamanhos de Slide Nike Mind temos?`
   - `@Hermes quais pares 9060 temos?`
6. Fullsync dry-run/manual:
   - gera relatório;
   - atualiza contadores;
   - não escreve externos.

---

## 15. Métricas

- `stock_answer_local_hit_rate`;
- `stock_answer_stale_rate`;
- `stock_answer_avg_latency_ms`;
- `tiny_refresh_success_rate`;
- `tiny_refresh_avg_duration_ms`;
- `fullsync_skus_updated`;
- `fullsync_errors`;
- `families_without_fresh_stock`.

---

## 16. Riscos

### R1 — Tiny API lenta/instável

Mitigação: timeouts curtos no responder, fila background, full sync com throttle/backoff.

### R2 — SKU/tamanho ambíguo

Mitigação: resolver via catálogo local + Tiny; se ambíguo, fallback/manual, nunca promessa.

### R3 — Webhook perdido

Mitigação: full sync diário.

### R4 — Base local virar verdade paralela

Mitigação: linguagem e schema deixam claro `last_tiny_read_at`; nunca delta; full sync; TTL/stale.

### R5 — Spam no Telegram/WhatsApp

Mitigação: sucesso silencioso; alertas só para erro/exceção; receipts no Brain.

---

## 17. Approval packet proposto

Para executar Fase 1 e Fase 2, aprovação sugerida:

> Aprovo Fase 1 e Fase 2 do PRD `lk-whatsapp-tiny-local-stock-webhook-fullsync-prd-2026-06-01`: hardening da base SQLite local e full sync manual/read-only Tiny → SQLite, sem criar cron, sem criar webhook real, sem escrever Shopify/Tiny, sem envio externo.

Para fases seguintes, pedir aprovações separadas:

- Fase 3: refresh queue background local.
- Fase 4: webhook dry-run/local-only.
- Fase 5: cron diário.
- Fase 6: qualquer Shopify inventory write.

---

## 18. Recomendação

Sim: a arquitetura correta é **database local atualizada por eventos + full sync diário**.

Mas a ordem segura é:

1. endurecer SQLite e freshness;
2. fazer full sync manual/read-only;
3. só depois ligar fila/background;
4. só depois webhook dry-run;
5. só depois cron diário;
6. Shopify write fica fora, separado e opcional.
