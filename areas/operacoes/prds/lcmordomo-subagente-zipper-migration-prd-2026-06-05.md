# PRD — LC Mordomo OS: migração/ensino dos fluxos atuais para o Subagente Zipper

**Data:** 2026-06-05  
**Dono:** Lucas Cimino  
**Sistema:** LC Mordomo OS / Mordomo Hermes  
**Subagente:** Zipper  
**Status:** v0.1 para validação e execução incremental  
**Decisões de Lucas incorporadas:** Zipper primeiro; modo híbrido; subagente lógico por enquanto; Supabase Zipper como destino principal; MVP com 5 fluxos; A2 automático para fluxos seguros, A3/A4 approval-gated.

---

## 1. Contexto

Lucas pediu que o LC Mordomo deixe de ser um conjunto de capacidades soltas no agente central e passe a **ensinar/migrar tudo para seus respectivos subagentes**, começando pelo Zipper.

A inspiração operacional vem da aula do Bruno Okamoto sobre Hermes/OpenClaw/segundo cérebro:

- agente bom não é chatbot: é operador com função, ferramentas, rotinas, memória e governança;
- primeiro o agente lê/observa, depois revisa, depois automatiza;
- repetição vira skill, mas com curadoria para evitar skill inchada/redundante;
- memória curta guarda identidade/preferências; Brain/CRM guarda conhecimento durável;
- crons são heartbeat de rotina documentada, não mágica;
- Telegram deve ser interface única para Lucas, não vazamento de complexidade;
- OpenClaw/Dexter inspira uma camada auditora: falhas, crons, skills e decisões sem fonte devem ser revisados;
- não criar muitos agentes cedo: criar um agente útil, com base, canal, ferramentas e poucas skills canônicas.

Tradução para LC Mordomo OS: **LC Mordomo Central continua como interface única**, mas o conhecimento, estado, skills e rotinas específicas de Zipper passam a morar no **Subagente Zipper lógico**.

---

## 2. Objetivo

Criar o PRD de migração/ensino do **Subagente Zipper** para absorver os fluxos reais já existentes no LC Mordomo:

1. intake ZPR/site e envio de PDF;
2. drafts de e-mail Zipper;
3. WhatsApp pós-PDF e follow-ups;
4. CRM de interesse por artista, negative-fit e supressões;
5. Decision Inbox de casos sensíveis.

O resultado esperado é que o Subagente Zipper passe a ser o dono lógico desses fluxos, com memória/Brain/skills/estado próprios, enquanto o LC Mordomo Central continua coordenando, filtrando e falando com Lucas.

---

## 3. Decisões de produto já fechadas

### 3.1 Primeiro subagente

**Decisão:** Zipper primeiro.

Motivo:

- já existe fluxo vivo de clientes/leads;
- já existem scripts e estados operacionais;
- há dor real e repetição suficiente;
- há guardrails aprendidos por correções de Lucas;
- é o melhor laboratório para o padrão de subagentes.

### 3.2 Modo de ativação

**Decisão:** híbrido.

- Fluxos já seguros e estreitos podem executar.
- Fluxos novos entram em dry-run/preview.
- Ações sensíveis sobem para Lucas.

### 3.3 Forma do subagente no MVP

**Decisão:** subagente lógico por enquanto.

Não criar profile/runtime separado no MVP. O subagente nasce como separação de:

- Brain;
- skills;
- estado;
- rotinas;
- ownership;
- guardrails;
- relatórios;
- handoff para o LC Mordomo Central.

Promoção futura para profile/runtime separado só quando houver volume, risco, isolamento necessário ou maturidade operacional.

### 3.4 Estado principal

**Decisão:** Supabase Zipper como destino principal desde o início, com shadow/local para segurança e auditoria.

No MVP:

- Supabase Zipper/CRM é destino principal dos objetos estáveis;
- estado local continua como shadow log/dedupe/rollback/auditoria;
- Brain guarda decisões, rotinas, receipts, explicações e aprendizados, não PII bruta desnecessária.

### 3.5 Fluxos do MVP

**Decisão:** incluir 5 fluxos:

1. ZPR/PDF;
2. draft de e-mail;
3. WhatsApp pós-PDF;
4. CRM de interesse por artista/supressão;
5. Decision Inbox de casos sensíveis.

### 3.6 Regra de aprovação

**Decisão:** A2 automático para ZPR/PDF seguro + pós-PDF seguro; A3/A4 aprovação de Lucas.

---

## 4. Arquitetura desejada

```text
Lucas
  ⇄ LC Mordomo Central
      ⇄ Subagente Zipper lógico
          ⇄ Gmail lucas@zippergaleria.com.br
          ⇄ WhatsApp Lucas/pessoal via wacli, quando fluxo aprovado
          ⇄ Supabase Zipper/CRM
          ⇄ Brain Zipper
          ⇄ PDF registry
          ⇄ Decision Inbox
          ⇄ Follow-up engine
```

### Papel do LC Mordomo Central

- Interface única com Lucas.
- Decide roteamento entre subagentes.
- Protege atenção de Lucas.
- Recebe handoffs, exceções e receipts.
- Mantém política global A0-A4.
- Não deve carregar detalhes operacionais de Zipper além do necessário para decisão.

### Papel do Subagente Zipper

- Dono de contexto Zipper.
- Lê e classifica e-mails/leads/conversas Zipper.
- Mantém CRM de interesse por artista.
- Mantém fila de follow-up Zipper.
- Gera drafts e previews.
- Executa A2 seguro quando aprovado por política.
- Escala A3/A4 para Lucas via LC Mordomo Central.

---

## 5. Fontes e artefatos atuais a migrar/ensinar

### 5.1 PRDs e rotinas Zipper existentes

- `areas/zipper/prds/lucas-zipper-email-intake-drafts-prd-2026-05-18.md`
- `areas/zipper/projetos/prd-mordomo-zpr-enquiry-form-auto-pdf-send-2026-05-22.md`
- `areas/zipper/projetos/mordomo-proposta-pdf-flow-2026-05-18.md`
- `areas/zipper/base-conhecimento/whatsapp-followups-pos-pdf-2026-05-20.md`
- `areas/zipper/base-conhecimento/whatsapp-followups-pos-pdf-autoenvio-2026-05-20.md`
- `areas/zipper/base-conhecimento/auto-ack-recusa-cordial-pos-pdf-2026-05-20.md`
- `areas/zipper/base-conhecimento/artist-interest-crm-negative-fit-2026-06-05.md`
- `areas/zipper/operacoes/zipper-runtime-gatilhos-e-guardrails-2026-05-26.md`
- `areas/zipper/operacoes/incidentes/2026-05-25-whatsapp-ivan-grilo-routing-error.md`

### 5.2 Scripts atuais relevantes

- `/opt/data/profiles/mordomo/scripts/zipper_zpr_enquiry_watcher.py`
- `/opt/data/profiles/mordomo/scripts/zipper_gmail_intake_dryrun.py`
- `/opt/data/profiles/mordomo/scripts/zipper_whatsapp_response_watch.py`
- `/opt/data/profiles/mordomo/scripts/zipper_main_email_monitor.py`
- `/opt/data/profiles/mordomo/scripts/mordomo_decision_digest.py`
- `/opt/data/profiles/mordomo/scripts/mordomo_decision_dashboard.py`
- `/opt/data/profiles/mordomo/scripts/mordomo_crm_sync_local.py`
- `/opt/data/scripts/zipper_artist_interest_backfill.py`
- `/opt/data/scripts/zipper_artist_interest_thread_audit.py`
- `/opt/data/scripts/zipper_post_pdf_followup_watchdog.py`
- scripts `send_zpr_*` já criados para envios aprovados e casos específicos — devem virar referência de comportamento, não arquitetura permanente caso-a-caso.

### 5.3 Estados atuais relevantes

- `/opt/data/profiles/mordomo/state/zipper_zpr_enquiry_leads.jsonl`
- `/opt/data/profiles/mordomo/state/zipper_zpr_enquiry_pending.json`
- `/opt/data/profiles/mordomo/state/zipper_zpr_enquiry_watcher.json`
- `/opt/data/profiles/mordomo/state/zipper_gmail_intake_dryrun.json`
- `/opt/data/profiles/mordomo/state/zipper_main_email_monitor.json`
- `/opt/data/profiles/mordomo/state/zipper_whatsapp_response_watch.json`
- `/opt/data/profiles/mordomo/state/zipper_negative_fit_contacts.json`
- `/opt/data/profiles/mordomo/state/mordomo_followup_queue.json`
- `/opt/data/profiles/mordomo/state/mordomo_contact_profiles.json`
- `/opt/data/profiles/mordomo/state/mordomo_crm.sqlite`
- `/opt/data/profiles/mordomo/state/mordomo_decision_inbox_events.jsonl`

### 5.4 Supabase conhecido

Fonte documental atual:

- `areas/zipper/contexto/mordomo-zipper-spiti-supabase-map-2026-05-18.md`

Tabelas relevantes para Zipper/CRM:

- `contacts`
- `conversations`
- `secretary_log`
- `followups`
- `messages_log`
- `templates`
- `automation_logs`
- `sync_runs`
- `artist_pdfs` — hoje subutilizada/vazia; precisa de schema validado antes de write real
- `scheduled_sends` — subutilizada/vazia; precisa de schema validado antes de write real
- possível tabela nova: `site_enquiries` ou equivalente, se validada/criada depois

Regra: Supabase é destino principal desde o início, mas qualquer write em tabela nova ou alteração de schema exige PRD técnico + aprovação explícita.

---

## 6. Fluxo 1 — ZPR/Site → PDF → WhatsApp/e-mail → follow-up

### Estado atual aprendido

Quando Lucas manda “enviar” ou chega lead ZPR/Tidio/site, o Mordomo já sabe:

1. identificar nome, telefone, e-mail e artista;
2. localizar PDF comercial do artista;
3. usar WhatsApp pessoal de Lucas para leads Zipper, salvo instrução contrária;
4. enviar texto padrão antes do PDF;
5. enviar PDF sem legenda;
6. enviar e-mail por `lucas@zippergaleria.com.br` com PDF;
7. registrar recibos;
8. criar follow-up pós-PDF;
9. não falar preço, desconto, reserva ou disponibilidade específica sem fonte validada.

### Comportamento desejado no Subagente Zipper

- Monitorar e-mails ZPR/site.
- Parsear lead com dedupe.
- Confirmar artista.
- Confirmar PDF comercial validado.
- Consultar Supabase/Brain/local manifest.
- Classificar risco A0-A4.
- Se A2 seguro, executar conforme política aprovada.
- Registrar no Supabase e shadow local.
- Criar follow-up pós-PDF.
- Gerar receipt para LC Mordomo Central.

### Critérios A2 para execução automática

Todos precisam ser verdadeiros:

- origem clara: ZPR Enquiry Form/site Zipper;
- lead com nome e canal válido;
- artista identificado com alta confiança;
- PDF comercial validado existe;
- mensagem livre não contém preço, desconto, reserva, pagamento, reclamação ou negociação;
- não há conversa recente ativa que torne a resposta genérica inadequada;
- não há bloqueio por negative-fit/supressão aplicável;
- dedupe limpo;
- envio externo é o texto/PDF padrão já aprovado.

### Bloqueios A3/A4

Escalar para Lucas quando houver:

- preço;
- disponibilidade específica;
- reserva;
- desconto;
- condição de pagamento;
- promessa de prazo/logística;
- reclamação;
- artista ou PDF incerto;
- duplicidade com conversa recente;
- caso envolvendo Ivan Grilo/LK ou outro bloqueio específico registrado;
- qualquer ambiguidade de empresa/canal/destinatário.

---

## 7. Fluxo 2 — Drafts de e-mail Zipper

### Estado atual aprendido

PRD existente define que `lucas@zippergaleria.com.br` deve virar inbox operacional assistida para:

- ler e-mails;
- separar ruído;
- classificar casos;
- registrar clientes/assuntos;
- criar follow-ups;
- preparar drafts com linguagem de Lucas quando seguro.

Classificações atuais:

- `lead_comercial`
- `cliente_respondeu_pdf`
- `preco_disponibilidade`
- `logistica_producao`
- `financeiro_admin`
- `artista_relacao`
- `evento_institucional`
- `newsletter_ruido`
- `unknown`

### Comportamento desejado no Subagente Zipper

- Intake frequente de Gmail Zipper.
- Ruído silencioso.
- Classificação e extração estruturada.
- Registro em Supabase/Brain quando acionável.
- Draft automático apenas para classes seguras.
- Decision Packet para classes sensíveis.
- Dedupe por Gmail message/thread ID.

### Pode gerar draft automaticamente

- resposta cordial a lead genérico sem preço/disponibilidade;
- agradecimento simples;
- follow-up leve já aprovado;
- pedido de mais informação sem compromisso comercial;
- respostas com tom institucional/cultural da Zipper sem promessa.

### Não deve criar draft final sem revisão mais forte

- preço/disponibilidade/reserva/desconto;
- contrato, nota, pagamento, cobrança;
- logística sensível;
- conflito/reclamação;
- decisão curatorial/comercial de artista;
- empresa ou destinatário ambíguo.

---

## 8. Fluxo 3 — WhatsApp pós-PDF e follow-up

### Estado atual aprendido

Quando cliente responde após PDF:

- “vou ver com meu marido/esposa/sócio/cliente”;
- “estamos analisando”;
- “qualquer coisa entro em contato”;
- “vou pensar/avaliar”;
- “estou em dúvida”.

O sistema deve diferenciar:

1. **lead ainda em análise**;
2. **encerramento leve com reabertura futura**;
3. **negative-fit por orçamento**;
4. **caso sensível por preço/disponibilidade/negociação**.

### Regras aprovadas/registradas

- Lead ainda analisando: responder leve, sem pressão, e follow-up curto depois.
- “Vi/olhei, estou em dúvida, qualquer coisa entro em contato”, sem preço/disponibilidade/negociação/recusa: auto-resposta curta de encerramento e follow-up suave em 2 meses.
- Budget/money-based decline: marcar supressão `do_not_send_novidades` / `budget_decline`.
- Não insistir se houver negativa clara, pedido para parar, objeção de preço ou desinteresse.

### Comportamento desejado no Subagente Zipper

- Watcher lê respostas WhatsApp relacionadas a Zipper.
- Classifica resposta pós-PDF.
- Executa A2 seguro quando a classe estiver autorizada.
- Atualiza Supabase e shadow local.
- Cria/reagenda follow-up.
- Sobe para Decision Inbox quando houver sensibilidade.

---

## 9. Fluxo 4 — CRM de interesse por artista e supressões

### Estado atual aprendido

Toda pessoa que demonstrar interesse por um artista deve ser registrada por:

- artista;
- canal;
- evidência;
- PDF enviado;
- respostas;
- follow-ups;
- status de campanha futura.

Se a pessoa declinar por dinheiro/orçamento, não deve entrar automaticamente em novidades/campanhas futuras daquele contexto.

### Comportamento desejado no Subagente Zipper

- Escrever eventos de interesse no Supabase como fonte principal.
- Manter shadow/auditoria local até estabilizar writes.
- Dedupe por e-mail/WhatsApp/nome.
- Separar universo bruto e universo acionável.
- Antes de qualquer campanha por artista, excluir `do_not_send_novidades`.
- Campanhas externas continuam approval-gated por Lucas.

### Objetos mínimos de CRM

Se couber no schema atual:

- contato em `contacts`;
- evento/ação em `secretary_log` ou tabela equivalente;
- conversa/recibo em `conversations` / `messages_log`;
- follow-up em `followups`;
- supressão por tag/contexto em `contacts.tags` ou tabela específica futura.

Se o schema atual não suportar sem ambiguidade, criar proposta de schema antes de write real.

---

## 10. Fluxo 5 — Decision Inbox Zipper

### Objetivo

Lucas só deve ser interrompido por decisão, exceção, falha, aprovação ou resumo executivo útil.

### Casos que sobem

- A3/A4;
- preço/disponibilidade/reserva/desconto;
- logística sensível;
- reclamação;
- lead VIP ou artista importante;
- conflito de fonte;
- PDF não encontrado;
- Supabase write falhou;
- cron falhou;
- possível duplicidade;
- risco de mensagem para pessoa/canal errado.

### Formato do Decision Packet

```text
Zipper — decisão necessária
Caso: [lead/cliente/artista]
Fonte: [Gmail/WhatsApp/Supabase/Brain]
Confiança: [runtime-verificado/primária/secundária/inferido]
Risco: A3
Resumo: ...
Sugestão: ...
Bloqueio: ...
Ações possíveis:
1. Aprovar envio padrão
2. Pedir draft alternativo
3. Marcar como não fazer
4. Resolver manualmente
```

Sem JSON, sem logs técnicos e sem PII desnecessária no Telegram.

---

## 11. Modelo de autonomia A0-A4 do Subagente Zipper

### A0 — Leitura e preparação

Pode executar automaticamente:

- ler Gmail/WhatsApp/Supabase/Brain;
- parsing;
- dedupe;
- busca de PDF;
- classificação;
- relatório local;
- audit log.

### A1 — Registro e preview

Pode executar automaticamente:

- criar registro Supabase seguro em tabela existente e validada;
- atualizar shadow local;
- gerar draft/preview;
- criar Decision Packet;
- atualizar follow-up interno sem envio externo.

### A2 — Envio externo seguro e estreito

Pode executar automaticamente se todos os critérios do fluxo estiverem preenchidos:

- ZPR/PDF padrão seguro;
- pós-PDF seguro já classificado e autorizado;
- auto-ack curto sem preço/disponibilidade/negociação;
- follow-up suave em janela autorizada.

### A3 — Exige Lucas

- preço;
- disponibilidade;
- reserva;
- desconto;
- logística sensível;
- reclamação;
- artista/curadoria;
- cliente importante;
- fonte conflitante;
- risco reputacional.

### A4 — Proibido automático

- negociar;
- prometer disponibilidade;
- confirmar reserva;
- enviar preço sem fonte validada e aprovação;
- alterar venda/financeiro;
- apagar/mover e-mails sem política;
- mexer em schema/infra/credenciais;
- enviar para contatos bloqueados sem reaprovação explícita.

---

## 12. Persistência e ownership de dados

### Supabase — principal

Deve virar fonte principal para objetos estáveis do Subagente Zipper:

- contatos;
- conversas;
- mensagens enviadas;
- follow-ups;
- logs do secretário;
- interesse por artista;
- supressões;
- PDFs comerciais;
- leads ZPR/site.

### Local — shadow e recuperação

Manter local por segurança:

- dedupe;
- receipts de execução;
- rollback/auditoria;
- logs de migração;
- snapshots para comparação;
- sqlite local como espelho provisório até schema Supabase maduro.

### Brain — conhecimento e decisões

Guardar no Brain:

- PRDs;
- rotinas;
- guardrails;
- decisões de Lucas;
- aprendizados;
- receipts executivos;
- incidentes e correções.

Não usar Brain como depósito de PII bruta quando Supabase/CRM for o lugar correto.

---

## 13. Skills canônicas a criar/atualizar depois do PRD

O PRD recomenda consolidar os fluxos em poucas skills do Subagente Zipper:

1. `zipper-zpr-pdf-intake`
   - ZPR/site → PDF → canais → follow-up.
2. `zipper-email-drafts`
   - Gmail intake, classificação e draft-only.
3. `zipper-whatsapp-post-pdf-followup`
   - respostas pós-PDF, auto-ack seguro, reabertura, follow-up.
4. `zipper-artist-interest-crm`
   - interesse por artista, backfill, dedupe, negative-fit, campanhas futuras.
5. `zipper-decision-inbox`
   - escalonamento A3/A4, packets e receipts.

Não criar uma skill por cliente/caso. Scripts `send_zpr_*` existentes devem virar exemplos/regressões, não padrão permanente.

---

## 14. Crons/watchers recomendados

### MVP

- `zipper_zpr_enquiry_watcher`
  - lê Gmail/ZPR;
  - cria lead;
  - executa A2 quando seguro;
  - escala A3/A4.

- `zipper_gmail_intake_dryrun`
  - classifica e-mails;
  - gera drafts/previews;
  - começa dry-run para classes novas.

- `zipper_whatsapp_response_watch`
  - identifica respostas pós-PDF;
  - executa auto-ack seguro;
  - atualiza follow-up/CRM.

- `zipper_post_pdf_followup_watchdog`
  - cobra/reagenda follow-ups seguros;
  - sempre lê histórico antes de qualquer follow-up.

- `zipper_decision_digest`
  - consolida exceções para LC Mordomo Central.

### Contrato de cron

- silent OK quando nada acionável;
- stdout só para alerta/decisão/falha;
- erro técnico vira incidente claro;
- todo cron real deve ter rotina `.md` correspondente;
- falha de JSON/parser deve ser tratada com extração robusta e não quebrar por diagnóstico de CLI antes do JSON.

---

## 15. Migração incremental

### Fase 0 — Inventário e congelamento conceitual

- Confirmar PRD.
- Mapear scripts, estados e crons atuais.
- Marcar ownership: `Subagente Zipper`.
- Não mudar envio externo ainda.

### Fase 1 — Supabase shadow/write seguro

- Validar schema Supabase real por leitura.
- Definir mapeamento de campos.
- Ativar writes apenas em tabelas existentes e seguras.
- Manter shadow local.
- Comparar Supabase vs local.

### Fase 2 — Encapsular fluxos em módulos/skills

- Transformar scripts caso-a-caso em funções reutilizáveis.
- Criar skills canônicas.
- Criar testes/regressões a partir de casos reais.
- Manter scripts antigos como referência até substituição.

### Fase 3 — Ativação A2 híbrida

- ZPR/PDF seguro em A2 automático.
- Pós-PDF seguro em A2 automático.
- Novos tipos de e-mail em dry-run/draft-only.
- A3/A4 sempre sobem.

### Fase 4 — Auditoria e promoção

- Medir falsos positivos/negativos.
- Revisar incidentes.
- Confirmar se Zipper precisa virar profile/runtime separado.
- Só promover se isolamento/volume/risco justificar.

---

## 16. Métricas de sucesso

- Redução de alertas inúteis para Lucas.
- 0 envio para destinatário errado.
- 0 menção automática de preço/disponibilidade/reserva sem aprovação.
- 100% dos leads ZPR processados com dedupe.
- 100% dos envios A2 com receipt.
- 100% dos follow-ups com leitura de histórico antes de envio.
- CRM de interesse por artista consultável por artista e canal.
- Supressões `budget_decline` respeitadas antes de campanha.
- Falhas de cron geram alerta acionável e não stacktrace cru recorrente.

---

## 17. Riscos e mitigação

### Risco: envio errado no WhatsApp

Mitigação:

- preflight wacli;
- fallback de nono dígito com registro;
- dedupe por JID/telefone/e-mail;
- bloqueio para ambiguidades;
- regressão do incidente Ivan Grilo.

### Risco: Supabase schema inadequado

Mitigação:

- leitura antes de write;
- shadow local;
- PRD técnico para tabela nova;
- não alterar schema sem aprovação.

### Risco: excesso de skills

Mitigação:

- 5 skills canônicas no máximo para o MVP;
- curadoria mensal;
- scripts caso-a-caso viram testes, não skills.

### Risco: Lucas receber ruído

Mitigação:

- Decision Inbox com score;
- silent OK;
- apenas decisão/exceção/falha/resumo.

### Risco: subagente virar ilha

Mitigação:

- handoff obrigatório ao LC Mordomo Central;
- receipts no Brain;
- Approval Ledger;
- Source Confidence.

---

## 18. Perguntas ainda abertas para execução técnica

1. Quais tabelas Supabase existentes suportam melhor `artist_interest` e supressões sem criar schema novo?
2. `artist_pdfs` deve ser ativada como fonte canônica ou continuar com manifest local enquanto schema é validado?
3. Qual cron real está ativo hoje para cada watcher e qual deve ser pausado/renomeado na migração?
4. Qual formato mínimo de receipt Supabase + Brain para cada A2?
5. Quais casos reais devem virar suite de regressão obrigatória?

---

## 19. Próximo passo recomendado

Executar uma fase técnica read-only para produzir:

1. inventário de crons vivos Zipper;
2. mapa Supabase real com schema/permissions atuais;
3. matriz local-state → Supabase;
4. lista de scripts caso-a-caso que viram regressão;
5. plano de implementação Fase 1 sem envio externo novo.

Depois disso, implementar a migração em modo híbrido conforme aprovado.
