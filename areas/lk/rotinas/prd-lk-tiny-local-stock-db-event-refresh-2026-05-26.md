# PRD — LK Tiny Local Stock DB + Event-Driven Refresh

Status: PRD aprovado para revisão antes de implementação.
Data: 2026-05-26.
Owner operacional: LK Ops / Atendimento.
Executor técnico: Hermes, escopo local/dry-run.

## 1. Contexto

Lucas identificou um problema operacional real: consultas amplas de estoque no Telegram/WhatsApp podem levar tempo demais quando dependem de busca ampla no Tiny. Exemplo reportado: pergunta sobre `New Balance 9060 tamanho 38` levou ~180 segundos.

Foi criada uma primeira camada de cache local com TTL curto para reduzir repetição de consultas. Isso melhorou a latência, mas não resolve a pergunta principal: como garantir que o cache esteja atualizado após uma movimentação de estoque?

A resposta de produto correta é evoluir de “cache TTL” para uma base local de estoque derivada do Tiny, com atualização por evento e validação de frescor.

## 2. Problema

O Tiny é a fonte oficial de estoque, mas pode ser lento para consultas amplas ou em alto volume. O atendimento precisa responder rápido no Telegram e em grupos de WhatsApp, sem prometer disponibilidade incorreta.

Problemas atuais:

- Busca ampla no Tiny pode ser lenta ou rate-limited.
- Cache TTL melhora velocidade, mas pode ficar incorreto se houver venda/cancelamento/movimentação antes do vencimento.
- Shopify não pode ser usado como saldo oficial.
- Não podemos calcular estoque local por delta, porque isso recria o erro de usar outro sistema como fonte de verdade.

## 3. Objetivo

Criar uma base local de estoque por SKU/tamanho, derivada exclusivamente de leituras Tiny, para responder consultas de estoque com baixa latência e com contrato claro de frescor.

Objetivos específicos:

1. Responder consultas frequentes de estoque em segundos.
2. Manter Tiny / `LK | CONTROLE ESTOQUE` como fonte de verdade.
3. Atualizar a base local quando houver eventos relevantes.
4. Evitar cálculo por delta local.
5. Registrar timestamp, fonte, confiança e status de frescor de cada SKU.
6. Bloquear/promover fallback live Tiny quando a base estiver stale, ausente ou ambígua.

## 4. Não objetivo

Esta Fase A não autoriza:

- criar webhooks novos em Shopify ou Tiny;
- criar cron recorrente;
- escrever em Shopify;
- escrever em Tiny;
- enviar mensagens externas a cliente/fornecedor;
- prometer reserva, preço, prazo ou entrega;
- substituir o Tiny como fonte de verdade.

## 5. Princípios de produto

### 5.1 Tiny é verdade; base local é espelho operacional

A base local nunca é “dona” do estoque. Ela é um snapshot local de leituras Tiny, com timestamp e status de confiança.

### 5.2 Evento não altera saldo; evento dispara reconsulta

Venda/cancelamento/movimentação não deve fazer:

- `saldo_local = saldo_local - quantidade`
- `saldo_local = saldo_local + quantidade`

O correto é:

1. evento identifica SKU/tamanho afetado;
2. Hermes consulta Tiny por SKU exato;
3. base local salva o saldo absoluto retornado pelo Tiny.

### 5.3 Resposta rápida precisa mostrar frescor operacional

Toda resposta baseada na base local deve ser capaz de carregar, internamente ou na resposta, metadados de frescor:

- fonte: Tiny local snapshot / Tiny live;
- timestamp da última leitura Tiny;
- confiança: alta/média/baixa;
- stale/fresco.

### 5.4 Falha de atualização não vira disponibilidade

Se Tiny falhar, rate-limit, SKU ambíguo ou dado stale crítico:

- não afirmar disponibilidade como final;
- responder que está validando ou que precisa checagem manual;
- registrar bloqueio.

## 6. Escopo da Fase A local

A aprovação do Lucas para esta fase é:

> criar base local Tiny stock por SKU/tamanho e ligar ao responder + processor dry-run, sem webhooks novos, sem cron, sem Shopify/Tiny writes e sem mensagens externas.

Entregáveis Fase A:

1. Criar módulo local de stock DB.
2. Criar SQLite local para estoque Tiny por SKU/tamanho.
3. Integrar o responder Telegram/WhatsApp para ler essa base antes de cair em Tiny amplo.
4. Integrar o processor dry-run existente para atualizar a base local quando ele já consulta Tiny.
5. Adicionar testes de schema, upsert, frescor, stale fallback e resposta rápida.
6. Documentar operação e rollback.

## 7. Arquitetura proposta

### 7.1 Componentes

- `lk_tiny_stock_local_db.py`
  - módulo único para schema, upsert, lookup, stale checks e fila local.

- `lk_tiny_stock_local.sqlite`
  - banco local SQLite.

- `lk_hermes_whatsapp_responder.py`
  - lê a base local para responder rápido.
  - usa Tiny live apenas quando base local está ausente/stale/ambígua.

- `lk_shopify_tiny_stock_sync_dryrun.py`
  - quando processa evento Shopify em dry-run e consulta Tiny, atualiza a base local com o resultado Tiny.
  - não escreve em Shopify/Tiny.

### 7.2 Caminho de leitura para atendimento

1. Usuário pergunta: “tem New Balance 9060 38?”
2. Resolver termos locais para SKU/tamanho candidatos.
3. Consultar `stock_by_sku`.
4. Se registro fresco e confiança alta:
   - responder em segundos usando base local.
5. Se registro ausente/stale:
   - consultar Tiny live por SKU exato, com timeout curto;
   - upsert na base local;
   - responder.
6. Se ainda incerto:
   - responder “validando / precisa checagem manual”, sem promessa.

### 7.3 Caminho de atualização por evento

Fase A usa somente eventos processados em dry-run local já existentes.

1. Processor recebe payload/sample/evento já disponível.
2. Canonicaliza line items: SKU, variant_id, tamanho.
3. Consulta Tiny por SKU exato.
4. Salva o saldo oficial `LK | CONTROLE ESTOQUE` na base local.
5. Grava ledger do evento e do upsert local.
6. Não escreve em Shopify/Tiny.

### 7.4 Futuro: movimentação direta no Tiny

Se o Tiny oferecer webhook/event log confiável de movimentação de estoque:

- adicionar rota aprovada para receber evento Tiny;
- extrair SKU/produto afetado;
- reconsultar Tiny para saldo absoluto;
- atualizar base local.

Se Tiny não oferecer webhook confiável:

- usar Shopify events para venda/cancelamento;
- usar refresh on-demand em consultas;
- usar micro-batches de reconciliação somente em fase futura e aprovada, respeitando rate-limit.

A Fase A não cria webhook Tiny nem cron.

## 8. Modelo de dados

Banco sugerido:

`/opt/data/hermes_bruno_ingest/local_sql/lk_whatsapp_hermes/lk_tiny_stock_local.sqlite`

### 8.1 Tabela `stock_by_sku`

Campos:

- `sku` TEXT PRIMARY KEY
- `tiny_id` TEXT
- `product` TEXT
- `size` TEXT
- `official_available` REAL
- `saldo_total` REAL
- `deposit` TEXT DEFAULT `LK | CONTROLE ESTOQUE`
- `source` TEXT
- `confidence` TEXT
- `last_tiny_read_at` TEXT ISO UTC
- `last_event_at` TEXT ISO UTC nullable
- `last_event_type` TEXT nullable
- `stale_reason` TEXT nullable
- `raw_hash` TEXT nullable
- `updated_at` TEXT ISO UTC

### 8.2 Tabela `stock_events`

Campos:

- `id` TEXT PRIMARY KEY
- `event_source` TEXT, ex. `shopify`, `tiny`, `manual_cli`
- `event_type` TEXT, ex. `orders/paid`, `orders/cancelled`, `manual_refresh`
- `delivery_id` TEXT
- `order_id` TEXT
- `line_item_id` TEXT
- `variant_id` TEXT
- `sku` TEXT
- `size` TEXT
- `status` TEXT, ex. `updated_local`, `blocked`, `duplicate`
- `block_reason` TEXT nullable
- `tiny_read_at` TEXT nullable
- `created_at` TEXT ISO UTC

### 8.3 Tabela `refresh_queue`

Campos:

- `sku` TEXT PRIMARY KEY
- `reason` TEXT
- `priority` INTEGER
- `created_at` TEXT ISO UTC
- `attempt_count` INTEGER
- `last_attempt_at` TEXT nullable
- `status` TEXT, ex. `pending`, `done`, `blocked`

Na Fase A, a fila pode existir sem worker recorrente. Ela serve para testes, CLI manual e preparação das fases futuras.

## 9. Regras de frescor

Valores iniciais propostos:

- `fresh_seconds_default`: 10 minutos.
- `fresh_seconds_after_event`: 30 minutos, porque o evento acabou de forçar leitura Tiny.
- `stale_immediate`: quando SKU tem evento recebido mas Tiny falhou.

Critérios:

- `fresh`: leitura Tiny recente e confiança alta/média aceitável.
- `stale`: leitura antiga, evento pendente ou falha posterior.
- `unknown`: nunca lido do Tiny.
- `blocked`: SKU ausente, ambíguo, Tiny rate-limit, sem depósito oficial.

Para promessa comercial/reserva: mesmo com `fresh`, manter guardrail de não prometer reserva/preço/prazo sem aprovação/humano.

## 10. Requisitos funcionais

### RF1 — Upsert de estoque Tiny

Dado um resultado Tiny por SKU, o sistema deve salvar/atualizar `stock_by_sku` com saldo oficial, produto, tamanho, fonte e timestamp.

### RF2 — Lookup rápido por SKU/tamanho

Dado um SKU ou candidato local, o sistema deve retornar o registro local com status de frescor.

### RF3 — Integração com resposta de atendimento

Responder deve consultar a base local antes de iniciar busca ampla Tiny.

### RF4 — Fallback live Tiny

Se base local estiver ausente/stale, responder deve tentar Tiny live por SKU exato, não busca ampla, e atualizar a base local.

### RF5 — Integração com processor dry-run

Quando o processor dry-run lê Tiny para `orders/paid` ou `orders/cancelled`, ele deve atualizar a base local com o saldo Tiny retornado.

### RF6 — Ledger de eventos locais

Cada atualização vinda de evento deve registrar `stock_events` com idempotência.

### RF7 — Sem side effects externos

Fase A não pode escrever Shopify/Tiny, enviar WhatsApp, criar Notion, webhook, cron ou campanha.

## 11. Requisitos não funcionais

- Resposta via base local: alvo < 1s após resolução de candidatos.
- Primeira confirmação live por SKU exato: alvo < 30s, com timeout seguro.
- SQLite com permissões restritas (`0600`).
- Diretório local com permissões restritas (`0700`).
- Erros Tiny não podem virar saldo zero.
- Testes automatizados obrigatórios antes de runtime.

## 12. Critérios de aceite

A Fase A só estará pronta quando:

1. Testes unitários cobrirem schema, upsert, stale, lookup e idempotência.
2. Teste de resposta `New Balance 9060 38` usar base local quando existe registro fresco.
3. Teste provar que registro stale chama fallback live por SKU exato.
4. Teste provar que evento dry-run atualiza a base local sem writes externos.
5. Comando CLI manual retorna resposta rápida baseada na base local.
6. Nenhum teste chama `send_text`, Shopify write, Tiny write, Notion ou webhook externo.
7. Receipt Brain registra arquivos alterados, evidências e rollback.

## 13. Métricas de sucesso

- Latência p95 para consulta com base fresca: < 1s.
- Latência p95 para fallback SKU exato: < 30s.
- Zero writes externos na Fase A.
- Zero respostas com disponibilidade sem fonte/timestamp.
- Zero uso de delta local para saldo.

## 14. Riscos e mitigação

### Risco: base local desatualizada

Mitigação: status de frescor, fallback Tiny live, timestamp e stale guardrail.

### Risco: Tiny rate-limit

Mitigação: consulta por SKU exato, timeouts, sem snapshot amplo em loop, micro-batch futuro só com aprovação.

### Risco: SKU ambíguo

Mitigação: bloquear update local como confiança alta; responder validação pendente.

### Risco: movimentação direta no Tiny sem evento Shopify

Mitigação Fase A: on-demand refresh quando consulta detectar stale; fase futura avaliar webhook Tiny ou reconciliação micro-batch aprovada.

### Risco: usuário interpretar base local como promessa

Mitigação: manter texto “uso interno / não reservei / não prometi entrega/preço”.

## 15. Plano de rollout

### Fase A — Local/dry-run, aprovada por Lucas neste pedido

- Criar DB local.
- Integrar responder e processor dry-run.
- Testar localmente.
- Sem webhooks novos, sem cron, sem writes externos.

### Fase B — Webhook/eventos reais em dry-run

Requer nova aprovação.

- Conectar eventos Shopify reais em dry-run.
- Atualizar base local com leituras Tiny acionadas por eventos reais.
- Monitorar bloqueios.

### Fase C — Write Shopify inventory

Requer nova aprovação explícita.

- Após validação, usar Tiny como fonte para setar estoque Shopify.
- Idempotência e readback obrigatório.

### Fase D — Tiny movement direct integration

Requer descoberta e aprovação.

- Verificar se Tiny oferece webhook/event log adequado.
- Se sim, integrar movimentações Tiny.
- Se não, desenhar reconciliação micro-batch controlada.

## 16. Rollback

Rollback da Fase A:

1. Desligar leitura da base local no responder por flag/código.
2. Voltar ao fluxo anterior: cache TTL curto + Tiny live.
3. Manter SQLite local apenas como artefato ignorado.
4. Nenhuma reversão em Shopify/Tiny é necessária, porque Fase A não escreve externamente.

## 17. Decisão para começar implementação

Este PRD atende ao pedido “crie o PRD antes de começar”.

Próximo passo, se Lucas aprovar, é gerar o implementation plan Superpowers com tarefas TDD bite-sized e então executar Fase A local.

Frase de avanço sugerida:

> Pode seguir com o implementation plan e executar a Fase A local conforme este PRD.
