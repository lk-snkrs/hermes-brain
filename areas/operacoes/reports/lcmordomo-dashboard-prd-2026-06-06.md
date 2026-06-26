# PRD — LC Mordomo OS Dashboard

Data: 2026-06-06
Status: Draft v0.1 para execução
Owner: Lucas Cimino / Mordomo OS
Fonte analisada: https://lc-whatsapp-prd.up.railway.app/dashboard

## 1. Resumo executivo

Vamos usar o dashboard atual `LC WhatsApp - Dashboard` como referência de lógica, UX e módulos operacionais, mas o **correto para o LC Mordomo OS** é que a fonte de verdade seja o **database do Mordomo**.

Decisão principal:

- O dashboard deve virar uma interface operacional do LC Mordomo OS.
- A lógica visual e funcional atual é aproveitável: métricas, contatos, conversas, busca por PDF, histórico, campanha, agendamento, templates, artistas, automações e agentes IA.
- A persistência canônica deve ser a database do Mordomo, hoje materializada localmente em:
  - `/opt/data/profiles/mordomo/state/zipper_canonical.sqlite`
  - `/opt/data/profiles/mordomo/state/zipper_canonical_summary.json`
- O dashboard legado pode ser usado como inspiração/adaptador, mas **não deve ser a fonte de verdade** para follow-up, contato, interesse por artista ou decision packets.

## 2. Problema

Hoje existem duas camadas separadas:

1. Dashboard WhatsApp/LK existente:
   - bom painel visual;
   - boa navegação;
   - funções úteis de envio, scan, contatos, artistas e IA;
   - fala em Supabase e foi originalmente feito com lógica LK/WhatsApp Agent.

2. LC Mordomo OS / Zipper OS:
   - tem fila real de follow-ups;
   - tem watcher local/no-agent;
   - tem regras de segurança e bloqueio material;
   - tem CRM canônico local derivado com contato, interesse por artista, lead enquiry, follow-up, sent actions, suppressions e decision packets;
   - ainda precisa evoluir para auto-follow-up seguro A1.

O risco é usar o dashboard como “sistema principal” e quebrar a segurança/idempotência do Mordomo. O correto é o contrário: **dashboard como cockpit; Mordomo database como cérebro e fonte de verdade**.

## 3. Objetivo do produto

Criar/adaptar um dashboard oficial do LC Mordomo OS para Lucas operar Zipper/LC com clareza sobre:

- quem são os contatos/clientes enviados;
- qual artista cada cliente demonstrou interesse;
- quais PDFs/catálogos foram enviados;
- quais follow-ups estão pendentes, vencidos, seguros ou bloqueados;
- quais mensagens foram enviadas pelo Mordomo;
- quais casos exigem decisão humana;
- quando o auto-follow-up seguro está ativo, bloqueado ou aguardando aprovação.

## 4. Não-objetivos nesta fase

Fase inicial não deve:

- ativar envio externo automático amplo;
- disparar campanha em massa sem aprovação explícita;
- usar Supabase legado como fonte de verdade;
- misturar LK Sneakers e Zipper/LC sem namespace claro;
- expor telefone/JID bruto em logs, relatórios ou telas não-operacionais;
- permitir alteração sensível de preço, disponibilidade, reserva, pagamento, desconto, frete/logística, dimensões ou reclamações via automação.

## 5. Usuários

### 5.1 Lucas

Precisa ver rapidamente:

- quem está sem resposta;
- quem precisa de follow-up;
- quem está bloqueado por tema material;
- interesse por artista;
- histórico por contato;
- saúde do sistema.

### 5.2 Mordomo Hermes

Precisa de interface/API para:

- consultar estado;
- registrar ações;
- deduplicar envios;
- gerar decision packets;
- validar guardrails antes de qualquer envio.

### 5.3 Futuro operador comercial/assistente

Pode usar dashboard para triagem, mas não deve conseguir burlar guardrails.

## 6. Princípios de produto

1. Database do Mordomo é fonte de verdade.
2. Dashboard é cockpit, não motor decisório final.
3. Todo envio precisa ser idempotente.
4. Todo auto-follow-up precisa de classificação de risco.
5. Material sensível sempre escala para Lucas.
6. Separar claramente LK, LC/Zipper e outros domínios.
7. Silent-OK para rotinas: ausência de problema não deve gerar ruído.
8. Telefone/JID devem ser mascarados em relatórios; exibição operacional só quando necessário.

## 7. Dashboard atual analisado

O dashboard atual tem navegação lateral com módulos:

- Métricas
- Contatos
- Conversas
- Busca
- Histórico
- Enviar
- Campanha
- Agendamento
- Templates
- Artistas
- Automações
- Agentes IA

Endpoints extraídos do app atual incluem:

- Saúde/status:
  - `/health`
  - `/api/version`
  - `/api/db/test`
  - `/api/stats`
- Métricas:
  - `/api/metrics?days=`
  - `/api/funnel`
  - `/api/insights`
- Contatos/artistas/tags:
  - `/api/contacts?`
  - `/api/contacts/by-artist?artist=`
  - `/api/contacts/by-tag?tag=`
  - `/api/contacts/import`
  - `/api/artists`
  - `/api/artists/known`
  - `/api/artists/custom`
  - `/api/tags`
- Conversas/mensagens:
  - `/api/messages?`
  - `/api/conversations?`
  - `/api/conversations/{phone}/thread`
- Busca por PDF/documentos:
  - `/api/scan`
  - `/api/scan/full`
  - `/api/scan/status`
  - `/api/scan/debug`
- Templates/campanha/agendamento:
  - `/api/templates`
  - `/api/campaign`
  - `/api/campaign/preview`
  - `/api/campaign/test`
  - `/api/campaign/status`
  - `/api/campaign/cancel`
  - `/api/scheduled`
- Agentes IA:
  - `/api/agents/lead-score`
  - `/api/agents/lead-score/bulk`
  - `/api/agents/lead-score/status`
  - `/api/agents/followup`
  - `/api/agents/followup/bulk`
  - `/api/agents/followup/send`
  - `/api/agents/campaign-report`
- Quick send:
  - `/api/quicksend/parse`
  - `/api/quicksend/send`
  - `/api/quicksend/email-status`
- Automações:
  - `/api/automations`
  - `/api/automations/google/status`
  - `/api/automations/transcription/status`
  - `/api/automations/transcription/toggle`

## 8. Fonte de verdade proposta

### 8.1 Database atual do Mordomo

Estado atual verificado:

- DB: `/opt/data/profiles/mordomo/state/zipper_canonical.sqlite`
- Integrity: `ok`
- Summary: `/opt/data/profiles/mordomo/state/zipper_canonical_summary.json`

Contagens atuais:

- Contatos: 123
- Interesses por artista: 36
- Lead enquiries: 126
- Follow-ups: 126
- Sent actions: 150
- Decision packets: 18
- Suppressions: 10

### 8.2 Tabelas canônicas atuais

- `contact`
- `lead_enquiry`
- `artist_interest`
- `followup`
- `sent_action`
- `suppression`
- `decision_packet`

### 8.3 Camada recomendada

Criar uma API `lcmordomo-dashboard-api` que lê/escreve contra o database do Mordomo.

O dashboard não deve falar direto com arquivos JSON de fila, nem com Supabase legado, nem com WhatsApp sender. Ele deve chamar a API do Mordomo, que aplica guardrails.

## 9. Modelo de domínio correto

### 9.1 Contact

Representa cliente/lead.

Campos mínimos:

- `contact_id`
- `display_name`
- `phone_hash`
- `phone_masked`
- `channel`
- `source`
- `created_at`
- `updated_at`
- `last_interaction_at`
- `tags`
- `notes`
- `risk_flags`

### 9.2 Artist Interest

Representa interesse de um cliente por artista.

Campos mínimos:

- `interest_id`
- `contact_id`
- `artist_name`
- `source_event`
- `confidence`
- `first_seen_at`
- `last_seen_at`
- `pdf_count`
- `status`

### 9.3 Lead Enquiry

Representa pedido/lead gerado por PDF, conversa ou indicação.

Campos mínimos:

- `lead_id`
- `contact_id`
- `artist_name`
- `enquiry_type`
- `source_message_id`
- `source_file`
- `created_at`
- `status`

### 9.4 Follow-up

Representa uma obrigação de retorno.

Campos mínimos:

- `followup_id`
- `contact_id`
- `artist_name`
- `context_type`
- `status`
- `due_at`
- `risk_class`
- `safe_to_auto_send`
- `suggested_message`
- `block_reason`
- `last_checked_at`
- `completed_at`

Estados recomendados:

- `waiting_client`
- `due`
- `ready_safe_auto_send`
- `blocked_material`
- `needs_lucas_decision`
- `sent`
- `cancelled`
- `snoozed`

### 9.5 Sent Action

Registro idempotente de tudo que foi enviado ou tentado.

Campos mínimos:

- `action_id`
- `contact_id`
- `followup_id`
- `channel`
- `message_hash`
- `message_preview`
- `sent_at`
- `sender`
- `delivery_status`
- `idempotency_key`

### 9.6 Decision Packet

Casos que exigem Lucas.

Campos mínimos:

- `packet_id`
- `contact_id`
- `artist_name`
- `reason`
- `risk_class`
- `summary`
- `suggested_options`
- `created_at`
- `status`

## 10. Módulos do dashboard adaptado

### 10.1 Métricas

Objetivo: visão executiva.

Cards:

- Contatos totais
- Follow-ups pendentes
- Follow-ups vencidos
- Auto-follow-ups seguros hoje
- Bloqueados por material
- Decision packets abertos
- Última execução do cron
- Saúde do runner

Gráficos:

- mensagens/follow-ups por dia;
- artistas mais requisitados;
- funil: captado → PDF enviado → respondeu → follow-up due → convertido/decisão.

### 10.2 Contatos

Lista de contatos com:

- nome;
- telefone mascarado;
- artista(s) de interesse;
- quantidade de PDFs;
- último contato;
- próximo follow-up;
- status de risco;
- tags/notas.

Ações permitidas:

- editar nome/tag/nota/artista;
- abrir histórico;
- criar decision packet manual;
- snooze follow-up;
- marcar como não contatar.

Ações bloqueadas por padrão:

- envio direto sem preview/aprovação;
- alteração material de preço/disponibilidade/reserva.

### 10.3 Conversas

Thread por contato:

- mensagens inbound/outbound;
- PDFs/documentos enviados;
- detecção de interesse por artista;
- status de leitura/ack quando disponível;
- resumo do último contexto.

Requisito crítico:

- antes de qualquer auto-follow-up, o backend deve reler a thread mais recente.

### 10.4 Busca / Scan

Adaptar “Buscar Contatos por PDF Enviado” para LC/Zipper.

Funções:

- buscar por artista;
- buscar por nome de PDF/catálogo;
- buscar por período;
- debug de contato específico;
- gerar/atualizar `artist_interest` e `lead_enquiry`.

Mudança de arquitetura:

- resultado deve salvar no database do Mordomo, não no Supabase legado.

### 10.5 Histórico

Histórico de ações:

- mensagens enviadas pelo Mordomo;
- follow-ups automáticos;
- envios bloqueados;
- tentativas idempotentes;
- decision packets criados.

Filtros:

- contato;
- artista;
- período;
- status;
- tipo de ação.

### 10.6 Enviar / Quick Send

Usar com muito cuidado.

Modo permitido na primeira fase:

- análise/parse de dados do contato;
- preview de WhatsApp/e-mail;
- salvar contato/interesse;
- criar follow-up.

Modo bloqueado por padrão:

- “Enviar WhatsApp + Email” direto sem aprovação explícita.

### 10.7 Campanha

Para LC/Zipper, campanha não é foco inicial do Mordomo OS.

Prioridade baixa até estabilizar follow-up A1.

Se mantida:

- deve ter namespace separado de follow-up individual;
- requer aprovação explícita do Lucas;
- deve excluir clientes com bloqueio, opt-out, negociação ativa ou risco material.

### 10.8 Agendamento

Útil para follow-ups futuros, mas deve escrever em `followup`, não em uma tabela solta.

Ações:

- criar follow-up agendado;
- alterar `due_at`;
- snooze;
- cancelar.

### 10.9 Templates

Templates devem representar fluxos seguros.

Templates iniciais:

1. Pós-PDF A1 leve:
   - “Oi, {nome}! Passando só para saber se conseguiu olhar o material de {artista}. Fico à disposição se alguma obra chamar sua atenção.”
2. Pós-agradecimento/análise:
   - esperar 4 dias antes de follow-up.
3. Reenvio de PDF seguro:
   - permitido se for pedido de reenvio, sem pergunta material.

Cada template precisa de:

- `risk_class`;
- canal permitido;
- bloqueios;
- delay mínimo;
- idempotency key.

### 10.10 Artistas

Aba crítica para Zipper/LC.

Deve mostrar:

- artistas cadastrados/conhecidos;
- número de interessados;
- PDFs enviados;
- follow-ups pendentes por artista;
- leads bloqueados/decision packets por artista.

### 10.11 Automações

Mostrar saúde do Mordomo OS:

- cron `LC Mordomo OS real local no-agent watcher`;
- última execução;
- runner status;
- silent-OK;
- falhas recentes;
- auto-send ligado/desligado;
- política ativa.

### 10.12 Agentes IA

Adaptar agentes para trabalhar como copiloto, não executor livre.

Funções:

- lead scoring;
- sugestão de follow-up;
- análise de campanha/respostas;
- classificação de risco;
- detecção de perguntas materiais.

Regra:

- agente gera sugestão; backend de policy decide se pode auto-send.

## 11. Regras de auto-follow-up A1

Auto-send permitido somente quando todos os critérios passarem:

- contexto: Zipper/LC;
- canal: WhatsApp pessoal individual;
- tipo: pós-PDF leve;
- classe: A1;
- due_at vencido;
- histórico relido antes do envio;
- cliente não respondeu depois do evento-base;
- sem pergunta material;
- sem termo de preço, disponibilidade, reserva, pagamento, negociação/desconto, frete/logística, dimensão/medida/tamanho, reclamação;
- dedupe por idempotency key;
- registro obrigatório em `sent_action`;
- se falhar qualquer regra, criar `decision_packet` ou manter bloqueado.

## 12. Policy engine

Criar camada `MordomoPolicyEngine` antes de qualquer envio.

Entrada:

- followup;
- contato;
- artista;
- thread recente;
- sent_actions;
- suppressions;
- template pretendido.

Saída:

- `ALLOW_AUTO_SEND`
- `BLOCK_MATERIAL`
- `NEEDS_LUCAS_DECISION`
- `SNOOZE`
- `NOOP_ALREADY_SENT`
- `NOOP_NOT_DUE`

## 13. APIs novas recomendadas

Manter compatibilidade com o dashboard atual, mas apontar para Mordomo DB.

### 13.1 Read APIs

- `GET /api/mordomo/stats`
- `GET /api/mordomo/contacts?search=&artist=&tag=&status=&limit=&offset=`
- `GET /api/mordomo/contacts/{id}`
- `GET /api/mordomo/contacts/{id}/thread`
- `GET /api/mordomo/artists`
- `GET /api/mordomo/followups?status=&risk=&due_before=`
- `GET /api/mordomo/decision-packets?status=open`
- `GET /api/mordomo/actions?contact_id=&period=`
- `GET /api/mordomo/automation/status`

### 13.2 Write APIs

Todas com policy/idempotência:

- `PUT /api/mordomo/contacts/{id}`
- `PUT /api/mordomo/contacts/{id}/tags`
- `PUT /api/mordomo/contacts/{id}/notes`
- `POST /api/mordomo/followups`
- `POST /api/mordomo/followups/{id}/snooze`
- `POST /api/mordomo/followups/{id}/preview`
- `POST /api/mordomo/followups/{id}/approve-send`
- `POST /api/mordomo/followups/{id}/auto-send-if-safe`
- `POST /api/mordomo/decision-packets/{id}/resolve`

### 13.3 Compatibility layer

Para reaproveitar o dashboard atual mais rápido, podemos mapear endpoints existentes:

- `/api/stats` → `/api/mordomo/stats`
- `/api/contacts` → `/api/mordomo/contacts`
- `/api/artists` → `/api/mordomo/artists`
- `/api/messages` → `/api/mordomo/actions/messages`
- `/api/conversations` → `/api/mordomo/contacts/thread`
- `/api/agents/followup` → `/api/mordomo/followups/preview`

## 14. UX prioritária para LC Mordomo

### Tela inicial ideal

Seções:

1. Hoje
   - follow-ups vencidos;
   - seguros para auto-send;
   - bloqueados;
   - precisam Lucas.

2. Artistas quentes
   - top artistas por interesse recente.

3. Leads recentes
   - contato + artista + PDF + próximo follow-up.

4. Saúde
   - cron ok;
   - database ok;
   - runner ok;
   - auto-send status.

### CTA principal

- “Ver follow-ups de hoje”
- “Ver bloqueados para decisão”
- “Ver artistas”

Não destacar campanha em massa como ação principal do Mordomo OS.

## 15. Segurança e guardrails

### Sempre bloquear auto-send se houver

- preço;
- disponibilidade;
- reserva;
- pagamento;
- desconto;
- negociação;
- frete/logística;
- dimensão/medida/tamanho;
- reclamação;
- pedido ambíguo;
- conversa de grupo;
- contato suprimido;
- opt-out;
- ação enviada recentemente;
- histórico não lido.

### UI deve mostrar motivo do bloqueio

Exemplos:

- “Bloqueado: perguntou disponibilidade”
- “Bloqueado: possível negociação”
- “Bloqueado: já enviado em X”
- “Aguardando: due_at ainda não venceu”

## 16. Requisitos funcionais MVP

P0 — obrigatório:

- Dashboard lê `zipper_canonical.sqlite` via API.
- Métricas principais carregam.
- Contatos e artistas aparecem corretamente.
- Follow-ups aparecem com status e due_at.
- Decision packets aparecem separados.
- Histórico por contato mostra ações e contexto.
- Botão “preview follow-up” gera mensagem, mas não envia.
- Botão “aprovar envio” exige confirmação explícita.
- Auto-send continua bloqueado até v1.1 ser implementado e aprovado.

P1 — próximo:

- Endpoint `auto-send-if-safe` com policy A1.
- Registro `sent_action` idempotente.
- Releitura de histórico antes do envio.
- Página de automações com cron status.
- Alertas de falha.

P2 — depois:

- Scan completo integrado ao DB canônico.
- Templates editáveis com risk_class.
- Agentes IA de scoring/follow-up conectados ao policy engine.
- Export CSV/Excel.

## 17. Requisitos não funcionais

- API deve responder consultas simples em < 500ms localmente.
- Operações de scan podem ser assíncronas com polling.
- Writes devem ser transacionais.
- Idempotência obrigatória em envio.
- Logs sem PII bruta quando possível.
- Secrets nunca exibidos.
- Erros devem ser explícitos na UI, sem stack trace sensível.

## 18. Migração proposta

### Fase 1 — Cockpit read-only

- Subir API read-only em cima do `zipper_canonical.sqlite`.
- Adaptar dashboard atual para exibir dados Mordomo.
- Desabilitar botões de envio/campanha/agendamento externo.

### Fase 2 — CRM operacional

- Permitir editar tags/notas/artista.
- Criar/snoozar/cancelar follow-ups.
- Criar decision packets.

### Fase 3 — Preview e aprovação

- Gerar preview de follow-up seguro.
- Aprovação explícita para envio individual.
- Registrar `sent_action` mesmo em envio manual/aprovado.

### Fase 4 — Auto-follow-up A1

- Habilitar `auto-send-if-safe` somente para A1 pós-PDF.
- Runner usa policy engine.
- UI mostra liga/desliga e auditoria.

### Fase 5 — Unificação futura

- Decidir se Supabase entra como réplica/cache remoto.
- Separar namespace LK e LC/Zipper.
- Criar visão multiempresa se necessário.

## 19. Critérios de aceite

MVP aceito quando:

- dashboard mostra contatos reais do Mordomo DB;
- artistas/interesses batem com `artist_interest`;
- follow-ups vencidos e pendentes aparecem corretamente;
- decision packets aparecem em fila própria;
- nenhuma ação de envio externo acontece sem aprovação;
- testes comprovam que material sensível bloqueia;
- `sent_action` impede duplicidade;
- cron/runner aparecem como saudáveis ou falhos;
- Lucas consegue responder: “quem eu preciso acompanhar hoje?” em menos de 30 segundos.

## 20. Decisão final

Sim: vamos usar a lógica e UX desse dashboard como base.

Mas a arquitetura correta do LC Mordomo é:

- Dashboard = cockpit/interface.
- Mordomo database = fonte de verdade.
- Policy engine = juiz de segurança.
- Runner/cron = executor.
- WhatsApp/e-mail = canais, nunca fonte canônica.

O dashboard legado pode acelerar muito a entrega, desde que seja reorientado para ler/escrever pelo Mordomo OS e não por Supabase/WhatsApp direto.
