# PRD — Mordomo Hermes v2: Inteligência, Autonomia e CRM Global

Data: 2026-05-21
Status: aprovado por Lucas para seguir
Contexto: evolução do Mordomo de automações isoladas para sistema operacional pessoal/empresarial com CRM, Decision Inbox, autonomia por risco e aprendizado durável.

## 1. Decisão de produto aprovada

Lucas aprovou evoluir o Mordomo Hermes para uma camada operacional única, com prioridade prática em CRM comercial multiempresa começando por Zipper, mantendo a experiência de um único contato/interface para Lucas.

A tese aprovada:

> O Mordomo não deve ser apenas um chatbot inteligente. Deve ser um sistema operacional pessoal/empresarial com memória, CRM, fila de ação, decisão, aprovação, logs e aprendizado.

Ordem recomendada e aprovada:

1. CRM/follow-up estruturado da Zipper.
2. Decision Inbox para o que realmente precisa de Lucas.
3. Motor de regras de autonomia.
4. Painel Mission Control do Mordomo.
5. Aprendizado automático das correções e respostas reais de Lucas.

## 2. Objetivo

Construir o Mordomo v2 como uma camada que:

- lê sinais de WhatsApp, Gmail, calendário, Telegram, webhooks e documentos autorizados;
- classifica cada sinal por empresa/contexto antes de agir;
- transforma conversas em objetos operacionais estruturados;
- mantém estado vivo de pessoas, oportunidades, follow-ups, decisões e riscos;
- executa ações internas e follow-ups seguros dentro de classes aprovadas;
- bloqueia e escala tudo que envolve decisão humana, preço, disponibilidade, negociação, dinheiro, fornecedor sensível, cliente sensível, produção, dados não verificados ou infraestrutura;
- aprende quando Lucas corrige, aprova, rejeita ou edita uma resposta.

## 3. Modelo conceitual

```text
Lucas / Telegram
  ↓
Mordomo Hermes
  ↓
Camada de Intake Global
  - WhatsApp
  - Gmail
  - Agenda
  - Telegram
  - Webhooks
  - PDFs/documentos
  ↓
Classificador
  - pessoal
  - LK
  - Zipper
  - SPITI
  - Hermes/infra
  ↓
Objetos estruturados
  - pessoa
  - empresa
  - contato
  - conversa
  - lead
  - oportunidade
  - obra/produto/lote
  - tarefa
  - follow-up
  - decisão
  - risco
  - draft
  ↓
Motor de Autonomia
  - pode agir
  - pode preparar
  - precisa aprovar
  - bloqueado
  ↓
Mission Control
  - painel
  - filas
  - relatórios
  - aprovações
  - histórico
  ↓
Learning Loop
  - memória
  - Hermes Brain
  - skills
  - regras
  - CRM/fonte de verdade
```

## 4. Princípios de design

### 4.1 Uma interface, múltiplos domínios

Lucas interage com um Mordomo só. Internamente, o Mordomo roteia para:

- Lucas pessoal;
- Zipper OS;
- SPITI OS;
- LK OS;
- Hermes/Infra;
- Operações globais.

Nenhuma regra, cliente, credencial, banco, oportunidade ou contexto deve ser misturado entre empresas.

### 4.2 Inteligência = LLM + estrutura

O LLM interpreta. O sistema operacionaliza.

O ganho não vem apenas de “mais IA”, mas de combinar:

- banco de estado;
- fila;
- regras;
- logs;
- aprovações;
- rotinas;
- Mission Control;
- memória durável;
- skills;
- validação antes de agir.

### 4.3 Autonomia por risco, não por canal

O canal não define segurança. O tipo de ação define.

- Ler/classificar é seguro.
- Criar rascunho é geralmente seguro.
- Enviar mensagem externa é bloqueado, salvo subfluxos estreitos já aprovados.
- Preço, disponibilidade, reserva, negociação, infraestrutura e produção exigem aprovação atual.

### 4.4 Silêncio inteligente

O Mordomo não deve avisar tudo.

Deve separar:

- silencioso: registrado, classificado, draft criado, follow-up atualizado;
- digest: precisa de atenção, mas pode esperar;
- interrupção: risco, decisão, prazo curto, cliente quente, oportunidade relevante ou bloqueio real.

### 4.5 Aprendizado obrigatório

Correções de Lucas não podem morrer no chat.

Cada correção deve ser classificada e persistida na camada certa:

- fato/preferência compacta → memória;
- regra durável de negócio → Hermes Brain;
- procedimento repetível → skill;
- estado operacional → CRM/fila/banco;
- trabalho futuro → backlog/Mission Control.

## 5. Objetos mínimos do Mordomo v2

### 5.1 Contact Profile

Perfil operacional por contato relevante:

- `contact_id`;
- `display_name`;
- `business_context`;
- `relationship_type`;
- `tone_profile`;
- `allowed_autonomy_classes`;
- `blocked_autonomy_classes`;
- `open_pendencies`;
- `last_lucas_reply_examples`;
- `last_seen_at`;
- `last_decision_at`.

### 5.2 Entity Map

Mapa vivo de entidades:

- pessoas;
- empresas;
- artistas;
- obras;
- produtos;
- pedidos;
- lotes;
- oportunidades;
- fornecedores;
- compromissos;
- documentos;
- conversas.

### 5.3 Signal

Unidade de entrada:

- `source_channel`;
- `source_account`;
- `raw_pointer`;
- `contact_id`;
- `business_context`;
- `intent`;
- `risk_level`;
- `summary`;
- `detected_entities`;
- `detected_at`;
- `proposed_action`;
- `status`.

### 5.4 Opportunity

Oportunidade comercial/operacional:

- `opportunity_id`;
- `business_context`;
- `contact_id`;
- `source`;
- `object_of_interest`;
- `stage`;
- `next_action`;
- `due_at`;
- `owner`;
- `risk_flags`;
- `last_touch_at`;
- `status`.

### 5.5 Follow-up

Fila de acompanhamento:

- `followup_id`;
- `business_context`;
- `contact_id`;
- `channel`;
- `reason`;
- `template_class`;
- `due_at`;
- `allowed_autonomy_class`;
- `blocked_reasons`;
- `last_thread_check_at`;
- `status`;
- `sent_actions`.

### 5.6 Decision Packet

Quando exigir Lucas:

- contato;
- contexto;
- o que aconteceu;
- por que importa;
- risco;
- recomendação;
- resposta sugerida;
- ações possíveis;
- deadline, se houver;
- bloqueador/fonte faltante;
- evidência/pointer.

## 6. Zipper como primeiro caso de uso

Zipper é a prioridade inicial porque já existe valor comercial imediato e fluxo vivo de:

- leads de artista;
- PDFs enviados;
- obras esgotadas;
- alternativas disponíveis;
- clientes analisando;
- follow-ups;
- rascunhos Gmail;
- WhatsApp pessoal como canal de Lucas;
- Supabase/Brain como fontes estruturadas.

### 6.1 Regra comercial aprovada: obra esgotada

Se o cliente se interessou por obra específica esgotada, o lead não está resolvido.

Estado correto:

- `opportunity_active`;
- `reason`: interesse real em artista/obra, mas item específico indisponível;
- `next_action`: oferecer alternativas disponíveis do PDF/seleção;
- `due_at`: 2 dias após o último contato de Lucas, se o cliente ficar em silêncio;
- `risk`: não prometer disponibilidade, preço, reserva ou condição sem fonte verificada.

Template-base:

> Oi, tudo bem? Só passando para saber se alguma outra obra da seleção chamou atenção. Mesmo aquela obra não estando disponível, temos outras opções e posso te ajudar a pensar em uma alternativa.

Adaptar artista, projeto e tom do contato. Envio externo continua sujeito às regras de autonomia vigentes.

### 6.2 Classes Zipper iniciais

- `zipper_pdf_sent_waiting_client`;
- `zipper_client_reviewing_pdf`;
- `zipper_unavailable_artwork_offer_alternatives`;
- `zipper_price_availability_request`;
- `zipper_logistics_supplier_update`;
- `zipper_artist_or_institutional_contact`;
- `zipper_new_site_lead`;
- `zipper_post_pdf_refusal_nurture`.

## 7. Decision Inbox

A Decision Inbox é a fila única do que precisa de Lucas.

Não deve incluir ruído nem candidatos crus.

Critérios de entrada:

- decisão comercial;
- risco de venda esfriar;
- cliente quente sem resposta;
- pedido de preço/disponibilidade/condição/reserva;
- compromisso com data/hora;
- fornecedor ou produção precisando decisão;
- conflito operacional;
- automação bloqueada por falta de dado;
- caso novo não coberto por regra.

Formato obrigatório:

```text
Contato:
Contexto:
O que aconteceu:
Por que importa:
Risco:
Recomendação:
Ação sugerida:
Bloqueador:
Prazo:
```

## 8. Autonomy Engine

O Autonomy Engine deve consultar, nesta ordem:

1. regra global de segurança;
2. contexto da empresa;
3. classe do caso;
4. perfil do contato;
5. estado da conversa real mais recente;
6. bloqueadores materiais;
7. duplicidade de envio;
8. disponibilidade de template aprovado;
9. log/estado anterior.

Resultado possível:

- `silent_record`;
- `create_followup`;
- `create_calendar_event`;
- `create_draft`;
- `send_safe_autonomous_message`;
- `decision_packet`;
- `blocked`.

Nenhum envio pode ocorrer sem checar duplicidade no canal real antes da execução.

## 9. Mission Control do Mordomo

Superfícies mínimas:

### Hoje

- decisões pendentes;
- follow-ups vencendo;
- clientes quentes;
- riscos;
- agenda relevante;
- automações bloqueadas.

### Zipper

- leads ativos;
- PDFs enviados;
- oportunidades por artista;
- follow-ups;
- rascunhos;
- pedidos de decisão;
- obras/seleções relacionadas.

### SPITI

- interessados;
- lotes/consignações;
- follow-ups;
- perguntas bloqueadas por fonte;
- decisão de Lucas.

### LK

- alertas comerciais;
- recompra/CRM;
- estoque crítico;
- campanhas/relatórios;
- pendências operacionais.

### Aprendizado

- novas regras aprendidas;
- correções recentes;
- classes de autonomia promovidas/rebaixadas;
- skills/Brain atualizados.

## 10. Requisitos de implementação

### 10.1 Segurança

- Não expor tokens ou segredos.
- Não enviar WhatsApp/e-mail externo sem regra aprovada ou aprovação atual.
- Não fazer mutações em Supabase/Shopify/Tiny/Merchant/VPS/Docker sem aprovação explícita.
- Não misturar dados entre LK, Zipper e SPITI.
- Rodar checagens de duplicidade antes de envio.
- Registrar audit log minimizado.

### 10.2 Observabilidade

Cada ação automatizada deve registrar:

- `decision_id`;
- `source_pointer`;
- `strategy_decision`;
- `executor_action`;
- `risk_level`;
- `autonomy_class`;
- `blocked_reasons`;
- `result`;
- `timestamp`.

### 10.3 Verificação

Antes de declarar fase pronta:

- teste de classificação;
- teste de bloqueio A3/A4;
- teste de duplicidade;
- teste de follow-up Zipper pós-PDF;
- teste de obra esgotada → alternativas;
- teste de contato com perfil sem autonomia;
- teste de Decision Inbox;
- teste de secret/PII scan em artefatos.

## 11. Fases aprovadas

### Fase 1 — Zipper CRM/follow-up estruturado

Objetivo: transformar leads Zipper em objetos estruturados e fortalecer fila de follow-up.

Critério de pronto:

- todo lead pós-PDF tem contato, artista, canal, origem, status, próxima ação e due date;
- obra esgotada abre oportunidade de alternativas em 2 dias;
- follow-ups consultam thread real antes de qualquer envio/draft;
- bloqueios por preço/disponibilidade viram Decision Packet.

### Fase 2 — Decision Inbox

Objetivo: unificar o que precisa de Lucas.

Critério de pronto:

- digest/alertas seguem formato de decisão;
- ruídos ficam silenciosos;
- cada item tem recomendação e bloqueador claro.

### Fase 3 — Autonomy Engine v1

Objetivo: formalizar regras por classe, contato e risco.

Critério de pronto:

- registry cobre classes iniciais Zipper + secretaria pura;
- executor não reinterpreta strategy;
- regressões impedem envio indevido.

### Fase 4 — Mission Control Mordomo

Objetivo: superfície visual/operacional.

Critério de pronto:

- painel mostra Hoje, Zipper, SPITI, LK e Aprendizado;
- dados vêm de estado local/CRM, não de texto solto;
- ações externas aparecem como preview/aprovação, não execução cega.

### Fase 5 — Learning Loop

Objetivo: aprender das respostas/correções de Lucas.

Critério de pronto:

- correções viram regra/Brain/skill/fila conforme tipo;
- respostas manuais de Lucas alimentam tom por contato;
- classes podem subir/descer confiança com evidência.

## 12. Fora de escopo imediato

- envio massivo;
- automação de campanhas;
- writes em bancos oficiais sem PRD específico;
- integração full Supabase de produção sem auditoria de schema e aprovação;
- dashboard público sem autenticação;
- alteração de infraestrutura Hermes/VPS;
- promessas comerciais autônomas.

## 13. Próximo passo operacional

Gerar e executar plano de implementação da Fase 1, começando por Zipper:

1. auditar estado atual dos scripts/fila/registry;
2. normalizar schema local de `opportunity` e `followup`;
3. adicionar classe `zipper_unavailable_artwork_offer_alternatives` ao registry;
4. criar regressões para Camila/obra esgotada;
5. garantir Decision Packet para pedidos de preço/disponibilidade;
6. preparar relatório de readiness antes de qualquer ampliação de envio automático.
