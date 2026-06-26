# LK WhatsApp AI Atendimento via Inbox Provider — Implementation Plan

> **For Hermes:** Use subagent-driven-development skill to implement this plan task-by-task after Lucas approves provider and rollout scope.

**Goal:** Implementar atendimento WhatsApp da LK via plataforma de inbox/mensageria com Hermes como cérebro de triagem, memória e rascunho, começando em observe-only/draft e evoluindo para auto-respostas seguras.

**Architecture:** Provider de inbox recebe WhatsApp e envia webhooks para Hermes. Hermes valida assinatura, normaliza evento, deduplica, atualiza memória, consulta fontes LK, aplica matriz A0-A4 e cria rascunho/nota/resposta conforme rollout. Auto-send fica desativado no início.

**Tech Stack:** Hermes webhook gateway, SQLite local, Brain LK, Tiny/Shopify read-only, provider escolhido entre Crisp/Twilio/Z-API/WATI, Doppler/secret store para tokens.

---

## Decisão registrada

Lucas escolheu a **Opção 3: plataforma intermediária / inbox humano + IA**.

Default recomendado para especificação: **Crisp ou ferramenta equivalente de inbox**. Se Lucas preferir WATI/Z-API/Twilio, adaptar o adapter mantendo a mesma arquitetura.

## Ajuste de escopo registrado em 2026-06-01

Lucas definiu que **neste momento Hermes não deve responder clientes**. O primeiro entregável deve ser observe-only/aprendizado:

- puxar histórico/conversas do Crisp;
- mapear mensagens que chegam;
- parear com respostas humanas já dadas pela Gisele/time;
- classificar intenção e autonomia A0-A4;
- aprender tom e padrões corretos;
- gerar relatório/lessons para Lucas corrigir;
- manter envio externo desligado.

Addendum PRD: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/atendimento/prds/lk-whatsapp-ai-atendimento-crisp-observe-learning-addendum-2026-06-01.md`.

## Task 0: Extrair histórico Crisp para aprendizado observe-only

**Objective:** Puxar conversas recentes do Crisp em modo read-only, montar pares cliente→Gisele/time e salvar lessons sanitizadas.

**Files:**
- Create: `/opt/data/scripts/lk_crisp_human_reply_learning.py`
- Create: `/opt/data/tests/test_lk_crisp_human_reply_learning.py`
- Output: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/atendimento/knowledge/lk-response-brain/daily-lessons/YYYY-MM-DD.md`

**Requirements:**
- Usar credenciais Crisp do secret store sem imprimir valores.
- Buscar conversas e mensagens em read-only.
- Separar `visitor/customer` de `operator`.
- Identificar Gisele por operator id/label/hash quando disponível.
- Para cada resposta humana, juntar as mensagens de cliente imediatamente anteriores.
- Redigir PII antes de salvar no Brain.
- Classificar cada par em `approved_pattern_candidate`, `source_required_pattern`, `human_only_pattern` ou `blocked_pattern`.
- Não enviar nenhuma mensagem ao cliente.

**Verification:**
- Testes com fixtures Crisp visitor/operator.
- Rodar dry-run sobre janela pequena.
- Conferir que output não contém telefones/e-mails brutos.
- Conferir que nenhum endpoint de envio Crisp foi chamado.

## Task 1: Fechar provider e canal piloto

**Objective:** Definir a ferramenta de inbox e o número/canal WhatsApp que será usado no piloto.

**Files:**
- Modify: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/atendimento/prds/lk-whatsapp-ai-atendimento-memory-bot-prd-2026-06-01.md`

**Steps:**
1. Confirmar provider: Crisp, WATI, Z-API, Twilio ou outro.
2. Confirmar número WhatsApp: atendimento LK, Hermes, outro número de teste.
3. Confirmar escopo inicial: clientes reais ou sandbox.
4. Registrar decisão no PRD.

**Verification:**
- PRD contém provider, número/canal e escopo.
- Nenhum token ou segredo aparece no PRD.

## Task 2: Criar schema local de memória e eventos

**Objective:** Criar SQLite local para memória de atendimento e eventos normalizados.

**Files:**
- Create: `/opt/data/scripts/lk_customer_service_memory_db.py`
- Create: `/opt/data/tests/test_lk_customer_service_memory_db.py`
- DB target: `/opt/data/hermes_bruno_ingest/local_sql/lk_whatsapp_ai_atendimento/lk_customer_service.sqlite`

**Tables:**
- `customer_memory`
- `conversation_events`
- `reply_decisions`
- `provider_deliveries`

**Verification:**
- Testes criam DB temporário.
- Testes validam idempotência por `provider_delivery_id`.
- Testes validam update de memória sem duplicar cliente.

## Task 3: Criar provider adapter observe-only

**Objective:** Receber webhook da plataforma escolhida e normalizar mensagem sem acionar resposta.

**Files:**
- Create: `/opt/data/scripts/lk_customer_service_provider_webhook.py`
- Create: `/opt/data/tests/test_lk_customer_service_provider_webhook.py`

**Requirements:**
- Validar assinatura/HMAC/token do provider.
- Preservar raw body para assinatura.
- Deduplicar evento.
- Ignorar mensagens originadas por operador/bot/plugin.
- Persistir evento normalizado.
- Retornar `202 accepted` rápido.

**Verification:**
- assinatura válida -> 202;
- assinatura inválida -> 401;
- duplicado -> 202 duplicate/no-op;
- origem operator/bot -> ignored;
- visitor/customer -> persisted.

## Task 4: Criar classificador A0-A4

**Objective:** Classificar intenção e autonomia antes de qualquer resposta.

**Files:**
- Create: `/opt/data/scripts/lk_customer_service_policy.py`
- Create: `/opt/data/tests/test_lk_customer_service_policy.py`

**Classes:**
- A0: resposta simples segura;
- A1: resposta com fonte viva;
- A2: rascunho humano;
- A3: escalar humano;
- A4: bloqueado.

**Verification:**
- desconto/reserva/prazo/reclamação nunca vira A0/A1;
- estoque sem fonte vira A2/A3;
- saudação simples vira A0;
- pedido de tamanho/modelo faltante vira A0.

## Task 5: Integrar fontes LK read-only

**Objective:** Permitir que o compositor consulte Tiny/SQLite/Shopify/Brain conforme intenção.

**Files:**
- Create: `/opt/data/scripts/lk_customer_service_sources.py`
- Test: `/opt/data/tests/test_lk_customer_service_sources.py`

**Sources:**
- SQLite estoque local;
- Tiny read-only quando necessário;
- Shopify read-only para pedido/produto;
- Brain para políticas aprovadas.

**Verification:**
- fonte indisponível gera bloqueio seguro;
- estoque usa depósito `LK | CONTROLE ESTOQUE`;
- nenhuma escrita externa ocorre.

## Task 6: Criar composer de rascunho

**Objective:** Gerar texto curto e seguro para humano aprovar/copiar.

**Files:**
- Create: `/opt/data/scripts/lk_customer_service_reply_composer.py`
- Test: `/opt/data/tests/test_lk_customer_service_reply_composer.py`

**Requirements:**
- Texto sem jargão técnico.
- Fonte e risco ficam em nota interna, não no texto ao cliente.
- Não prometer reserva/desconto/prazo.
- Quando baixa confiança, pedir dado faltante.

**Verification:**
- snapshots de resposta para saudação, estoque, reclamação, desconto, status de pedido.

## Task 7: Entregar draft para humano

**Objective:** Enviar rascunho para canal interno ou nota na inbox, sem resposta externa automática.

**Files:**
- Modify: provider adapter conforme provider escolhido.
- Create: `/opt/data/scripts/lk_customer_service_draft_delivery.py`

**Default:**
- `external_send_enabled = false`.
- Draft aparece como nota interna/inbox/Telegram, conforme escolha.

**Verification:**
- webhook real gera draft interno;
- cliente não recebe nada automaticamente;
- receipt contém decisão A0-A4 e fonte usada.

## Task 8: Canary 0 observe-only

**Objective:** Rodar piloto sem enviar mensagens.

**Run:**
- 50 mensagens ou 7 dias, o que vier primeiro.

**Metrics:**
- intenção;
- A0-A4;
- confiança;
- fonte necessária;
- resposta sugerida ou bloqueio.

**Verification:**
- relatório no Brain;
- zero envio externo;
- zero segredo em logs.

## Task 9: Canary 1 draft mode

**Objective:** Gerar rascunhos para o time usar.

**Gate:**
- Lucas aprova explicitamente depois do relatório do Canary 0.

**Verification:**
- >=80% rascunhos aproveitáveis;
- zero promessa indevida;
- todos os A3/A4 escalados.

## Task 10: Canary 2 auto A0

**Objective:** Permitir auto-resposta apenas para mensagens simples e seguras.

**Gate:**
- Aprovação explícita de Lucas com lista de templates A0.

**Verification:**
- flag rollback testada;
- templates aprovados versionados;
- logs de cada envio.

## Task 11: Canary 3 auto A1 estoque confiável

**Objective:** Permitir auto-resposta sobre estoque/produto quando fonte viva e match alto existirem.

**Gate:**
- Aprovação explícita de Lucas.

**Verification:**
- 100% respostas com `source_ref`;
- baixa confiança bloqueia;
- não promete reserva.

## Open decisions before implementation

1. Provider específico: Crisp, WATI, Z-API, Twilio ou outro.
2. Número/canal WhatsApp usado.
3. Onde o humano verá drafts: inbox, Telegram, WhatsApp interno ou painel.
4. Escopo do Canary 0: clientes reais ou sandbox.
5. Templates A0 aprovados.

## Safety gates

- Sem auto-send no início.
- Sem write em Shopify/Tiny/CRM no MVP.
- Segredos via Doppler/secret store.
- Logs redigidos.
- Rota com validação de assinatura.
- Rollback por flag `external_send_enabled=false`.
