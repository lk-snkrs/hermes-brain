# Relatório read-only — Subagente Zipper: inventário técnico inicial

**Data:** 2026-06-05  
**Escopo:** LC Mordomo OS / Subagente Zipper lógico  
**Modo:** read-only/local; nenhuma mensagem externa, e-mail, WhatsApp, banco ou infra alterados.

---

## 1. Motivo

Após o PRD de migração do Subagente Zipper, a próxima etapa segura é inventariar o runtime atual antes de qualquer implementação.

Este relatório registra o que já existe e o que precisa ser promovido do LC Mordomo Central para ownership do Subagente Zipper.

---

## 2. Resultado executivo

### Achado principal

O ecossistema Zipper já tem vários blocos prontos, mas ainda está espalhado entre:

- scripts específicos de caso (`send_zpr_*`);
- watchers genéricos do Mordomo;
- estado local JSON/SQLite;
- Brain Zipper;
- crons ativos/pausados;
- Supabase ainda não usado como destino principal para todos os objetos estáveis.

Isso confirma a necessidade do Subagente Zipper lógico como dono de contexto, estado, rotinas e skills.

### Status dos crons Zipper/Mordomo relevantes

Fonte verificada: `/opt/data/profiles/mordomo/cron/jobs.json`.

- `Zipper Gmail draft engine — safe draft-only`
  - id: `5bbe5169fe62`
  - status: **ativo/scheduled**
  - frequência: 15 min
  - entrega: local
  - papel no Subagente Zipper: **draft de e-mail / Decision Inbox local**

- `Mordomo CRM local sync`
  - id: `daf97feec481`
  - status: **ativo/scheduled**
  - frequência: 10 min
  - entrega: local
  - papel no Subagente Zipper: **espelho/local CRM e futura ponte para Supabase**

- `Zipper artist PDFs local-only known-answer ingest`
  - id: `f537bb9c505b`
  - status: **ativo/scheduled**
  - frequência: 30 min
  - entrega: local
  - papel no Subagente Zipper: **PDF registry / known answers**

- `ZPR Enquiry Form watcher — approval-gated`
  - id: `871b9bc5617a`
  - status: **pausado** desde 2026-06-02
  - frequência configurada: 5 min
  - papel no Subagente Zipper: **ZPR/site intake → PDF → follow-up**
  - observação: precisa ser reavaliado antes de reativação, principalmente com a decisão nova de Supabase como destino principal e A2 seguro automático.

- `Mordomo global WhatsApp watcher — Lucas pessoal`
  - id: `6f4c913082db`
  - status: **pausado** desde 2026-06-02
  - papel: watcher global; não deve virar dono de Zipper, mas pode fornecer sinais roteados.

- `Mordomo Decision Inbox digest`
  - id: `e46ea230f0cf`
  - status: **pausado**
  - papel: deve ser redesenhado como interface consolidada do LC Mordomo Central, recebendo handoff do Subagente Zipper.

- `Zipper direct main e-mail monitor — zipper@zippergaleria.com.br`
  - id: `20972b3c7595`
  - status: **pausado**
  - papel: fonte secundária/operacional da caixa principal Zipper.

Observação técnica: os comandos `hermes cron list` e `cronjob list` não estão disponíveis neste shell, mas o arquivo runtime `jobs.json` está presente e atualizado até `2026-06-05T18:23:37Z`, com outputs recentes em `/opt/data/profiles/mordomo/cron/output/`.

---

## 3. Scripts que devem ser absorvidos pelo Subagente Zipper

### Núcleo recorrente

- `zipper_zpr_enquiry_watcher.py`
  - papel: ZPR/site intake;
  - status cron: pausado;
  - destino futuro: skill `zipper-zpr-pdf-intake`.

- `zipper_gmail_intake_dryrun.py`
  - papel: triagem de Gmail Zipper / drafts;
  - destino futuro: skill `zipper-email-drafts`.

- `zipper_whatsapp_response_watch.py`
  - papel: resposta WhatsApp pós-PDF;
  - destino futuro: skill `zipper-whatsapp-post-pdf-followup`.

- `mordomo_crm_sync_local.py`
  - papel: CRM local estruturado;
  - destino futuro: ponte local → Supabase / skill `zipper-artist-interest-crm`.

- `mordomo_decision_digest.py` e `mordomo_decision_dashboard.py`
  - papel: Decision Inbox;
  - destino futuro: skill `zipper-decision-inbox` + handoff para LC Mordomo Central.

- `zpr_artist_pdf_local_ingest.py`
  - papel: ingest local de PDFs comerciais;
  - destino futuro: PDF registry / known answers.

### Scripts caso-a-caso

Existem muitos scripts `send_zpr_*` e similares. Eles não devem virar arquitetura permanente.

Uso correto na migração:

- extrair padrões reutilizáveis;
- transformar casos reais em fixtures/regressões;
- substituir gradualmente por um executor genérico parametrizado;
- manter recibos e dedupe por lead/canal/thread.

---

## 4. Estado local atual

Fonte: `/opt/data/profiles/mordomo/state/`.

- `zipper_zpr_enquiry_leads.jsonl`
  - 14 linhas;
  - papel: histórico de leads ZPR processados.

- `zipper_zpr_enquiry_pending.json`
  - contém `pending` e `updated_at`;
  - papel: fila de leads ZPR pendentes/bloqueados.

- `zipper_zpr_enquiry_watcher.json`
  - contém `seen_hashes`, `seen_message_ids`, `updated_at`;
  - papel: dedupe de watcher.

- `zipper_gmail_intake_dryrun.json`
  - contém `seen`, `updated_at`;
  - papel: dedupe de triagem de Gmail.

- `zipper_whatsapp_response_watch.json`
  - contém `seen`, `last_run_at`, `active_chats`;
  - papel: watcher pós-PDF.

- `zipper_negative_fit_contacts.json`
  - contém `contacts`, `updated_at`;
  - papel: supressão/negative-fit inicial.

- `mordomo_followup_queue.json`
  - ~2.67 MB;
  - papel: fila global de follow-ups, hoje misturando contextos.

- `mordomo_contact_profiles.json`
  - perfis/allowances de contatos;
  - papel: aprendizado por contato.

- `mordomo_decision_inbox_events.jsonl`
  - 4 linhas;
  - papel: histórico inicial de Decision Inbox.

- `mordomo_crm.sqlite`
  - tabelas relevantes:
    - `followups`: 190 linhas;
    - `zipper_artist_interest`: 52 linhas;
    - `zipper_artist_interest_events`: 68 linhas;
    - `zipper_campaign_suppression`: 1 linha.

---

## 5. Mapeamento local → Supabase desejado

### Leads ZPR/site

Origem local:

- `zipper_zpr_enquiry_leads.jsonl`
- `zipper_zpr_enquiry_pending.json`

Destino Supabase provável:

- `contacts` para contato;
- `secretary_log` para ação/triagem;
- `messages_log` para envio;
- `followups` para pós-PDF;
- tabela nova ou equivalente para `site_enquiries`, se o schema atual não acomodar.

### Follow-ups

Origem local:

- `mordomo_followup_queue.json`
- `mordomo_crm.sqlite.followups`

Destino Supabase provável:

- `followups`.

Regra: antes de write real, mapear status/intent/risk_level para campos existentes sem perder semântica.

### Interesse por artista

Origem local:

- `mordomo_crm.sqlite.zipper_artist_interest`
- `mordomo_crm.sqlite.zipper_artist_interest_events`

Destino Supabase provável:

- `contacts.artist_interest`, se suficiente;
- `secretary_log`, para eventos;
- tabela nova específica se precisar de `contact_key + artist + suppression` como objeto forte.

### Supressões / negative-fit

Origem local:

- `zipper_negative_fit_contacts.json`
- `mordomo_crm.sqlite.zipper_campaign_suppression`

Destino Supabase provável:

- `contacts.tags` ou `contacts.notes`, se for provisório;
- tabela específica futura se for necessário query robusta para campanhas.

Requisito: campanha futura por artista precisa excluir `do_not_send_novidades` / `budget_decline` antes de qualquer lista de envio.

### PDF registry

Origem local:

- `/opt/data/zipper_artist_pdfs/manifest.json`
- `/opt/data/zipper_artist_pdfs/`
- `zpr_artist_pdf_local_ingest.py`

Destino Supabase provável:

- `artist_pdfs`.

Observação: documentação anterior indicava `artist_pdfs` como vazia/subutilizada no sample. Precisa de validação de schema/permissões antes de write.

---

## 6. Gaps encontrados

1. **ZPR watcher está pausado.**
   - O fluxo ZPR/site não está no estado final desejado de A2 híbrido.

2. **Decision Inbox global está pausado.**
   - O LC Mordomo Central ainda não está recebendo um digest estruturado vivo de Zipper por esse canal.

3. **Supabase ainda não é destino principal para todos os objetos.**
   - Existe CRM local forte, mas falta ponte validada local → Supabase.

4. **Scripts caso-a-caso ainda concentram lógica operacional.**
   - Bom para aprendizado/regressão; ruim como arquitetura permanente.

5. **Follow-up queue é global e grande.**
   - Precisa de separação por business/contexto e ownership do Subagente Zipper.

6. **Alguns watchers globais estão pausados.**
   - Isso pode ser correto por redução de ruído, mas o Subagente Zipper precisa de ingest próprio claro.

---

## 7. Próximo plano seguro

### Etapa 1 — Supabase schema read-only

- Verificar tabelas reais e permissões atuais.
- Confirmar campos de `contacts`, `secretary_log`, `followups`, `messages_log`, `artist_pdfs`.
- Não escrever nada.

### Etapa 2 — matriz de migração

Criar matriz formal:

- objeto local;
- campos;
- destino Supabase;
- transformação;
- dedupe;
- risco;
- rollback.

### Etapa 3 — skill canônica v0

Criar/atualizar 5 skills do Subagente Zipper:

1. `zipper-zpr-pdf-intake`
2. `zipper-email-drafts`
3. `zipper-whatsapp-post-pdf-followup`
4. `zipper-artist-interest-crm`
5. `zipper-decision-inbox`

### Etapa 4 — executor genérico

Substituir gradualmente scripts `send_zpr_*` por executor parametrizado, com fixtures/regressões baseadas nos casos antigos.

### Etapa 5 — ativação híbrida

- Reativar/ajustar ZPR watcher somente depois da validação Supabase e testes.
- A2 seguro pode executar.
- A3/A4 sobe para Lucas.

---

## 8. Verificação

- Inventário feito por leitura local de scripts/state/jobs.
- Nenhum secret impresso.
- Nenhum e-mail/WhatsApp enviado.
- Nenhum Supabase write executado.
- Nenhum cron alterado.
- Nenhuma infra alterada.
