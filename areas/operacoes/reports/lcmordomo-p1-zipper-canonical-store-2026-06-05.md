# LC Mordomo OS — P1 Zipper canonical store

**Data:** 2026-06-05  
**Escopo:** consolidar runtime Zipper MVP em objetos canônicos locais.  
**Modo:** local/read-only derivado; nenhuma mensagem externa, Supabase, produção, infraestrutura ou credencial alterada.

---

## Resultado

Foi criado um store canônico local para o Subagente Zipper:

- Script: `/opt/data/profiles/mordomo/scripts/zipper_canonical_store_build.py`
- SQLite derivado: `/opt/data/profiles/mordomo/state/zipper_canonical.sqlite`
- Resumo JSON local: `/opt/data/profiles/mordomo/state/zipper_canonical_summary.json`

O store é rebuildable/idempotente: ele apaga e recria as tabelas derivadas a partir dos estados locais existentes. O objetivo é dar ao Zipper MVP um eixo comum de leitura antes de qualquer futura ponte para Supabase ou runtime mais forte.

---

## Fontes locais usadas

- `/opt/data/profiles/mordomo/state/mordomo_followup_queue.json`
- `/opt/data/profiles/mordomo/state/zipper_zpr_enquiry_pending.json`
- `/opt/data/profiles/mordomo/state/zipper_zpr_enquiry_leads.jsonl`
- `/opt/data/profiles/mordomo/state/zipper_negative_fit_contacts.json`
- `/opt/data/profiles/mordomo/state/zipper_main_email_monitor.json`
- `/opt/data/profiles/mordomo/state/zipper_whatsapp_response_watch.json`

Inventário inicial verificado:

- Follow-ups totais na fila global: 141
- Follow-ups Zipper: 120
- `sent_actions` na fila global: 94
- `signals` na fila global: 2666
- ZPR pending records: 8
- ZPR leads JSONL: 14 linhas
- Supressões Zipper por negative/budget fit: 2
- CRM local genérico existente: `/opt/data/profiles/mordomo/state/mordomo_crm.sqlite`

---

## Schema canônico MVP

Tabelas criadas:

- `contact`
- `lead_enquiry`
- `artist_interest`
- `followup`
- `suppression`
- `sent_action`
- `decision_packet`
- `meta`

Contrato: este SQLite é cache local derivado, não fonte externa de verdade e não substitui Supabase. Ele serve como base de normalização para reduzir fragmentação entre scripts, fila de follow-up, ZPR, supressões e recibos.

---

## Contagem após build

Build verificado em `/opt/data/profiles/mordomo/state/zipper_canonical_summary.json`:

- `contact`: 130
- `lead_enquiry`: 9
- `artist_interest`: 32
- `followup`: 120
- `suppression`: 2
- `sent_action`: 171
- `decision_packet`: 15

Status de follow-up Zipper consolidados:

- `auto_sent`: 17
- `manual_sent`: 38
- `responded_by_lucas`: 29
- `needs_lucas_decision`: 8
- `manual_send_failed`: 5
- `waiting_client`: 4
- `llm_suppressed`: 5
- `silenced_by_lucas`: 3
- `due_alerted`: 2
- `ignored_by_lucas`: 2
- `resolved_by_client_budget_decline`: 2
- `resolved_by_lucas_closure`: 2
- demais estados unitários: `long_term_nurture`, `merged_into_canonical_followup`, `responded_by_client`

Supressões:

- `budget_decline`: 2

---

## Verificação executada

Comandos/checagens executadas:

- `python3 -m py_compile /opt/data/profiles/mordomo/scripts/zipper_canonical_store_build.py`
- execução do builder com `--json`
- `pragma integrity_check` no SQLite: `ok`
- contagens por tabela após build
- reexecução do builder para validar idempotência por contagem estável
- `sha256sum` dos artefatos locais gerados

Evidência principal:

- SQLite integrity: `ok`
- Rebuild manteve contagens: `contact=130`, `lead_enquiry=9`, `artist_interest=32`, `followup=120`, `suppression=2`, `sent_action=171`, `decision_packet=15`

---

## Limitações conhecidas

- O store ainda é derivado local; não grava em Supabase.
- `decision_packet` é extraído de estados operacionais existentes, não é ainda uma Decision Inbox redesenhada action-ready.
- `lead_enquiry` consolida os registros identificáveis a partir de ZPR pending/JSONL; a camada ainda pode ser enriquecida com artefatos Brain de e-mail e PDF em etapas seguintes.
- Dados sensíveis permanecem no profile local; este relatório não expõe PII bruto.

---

## Próximo passo recomendado

P1.2 — transformar este store em rotina operacional:

1. Registrar cron local/silent-OK de rebuild do `zipper_canonical.sqlite`, se Lucas quiser manter o cache sempre fresco.
2. Criar consultas operacionais seguras para:
   - lead ponta-a-ponta por contato/artista;
   - supressões por artista;
   - follow-ups vencidos por classe de risco;
   - recibos de envio por `followup_id`;
   - candidatos reais para Decision Inbox.
3. Só depois redesenhar o Decision Inbox Zipper em cima dessas consultas, para não voltar ao modelo de “fila solta”.

Parar antes de qualquer Supabase write, envio externo, alteração de campanha, contato com cliente/fornecedor ou mudança de infraestrutura.
