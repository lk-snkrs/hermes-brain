# LC Mordomo OS Runtime Consolidation PRD

**Data:** 2026-06-07
**Owner:** Lucas Cimino / Mordomo Hermes
**Status:** Draft operacional, sem cutover executado

## Problema

O LC Mordomo hoje funciona, mas a lógica está espalhada entre crons Hermes, scripts `no_agent`, processos WACLI contínuos, watchers Zipper, watchers LK/Hermes e rotinas de e-mail/CRM. Isso cria três riscos:

1. O usuário vê "Mordomo OS", mas a decisão real pode estar em um script isolado.
2. Follow-ups, alertas e rascunhos podem divergir de uma política única de contexto, aprovação e idempotência.
3. A manutenção fica difícil: para saber o que está rodando, é preciso cruzar cron, processos, estado local, WACLI e dashboard.

## Decisão de produto

Migrar a operação para um **LC Mordomo OS Runtime** único: um núcleo orquestrador que registra, classifica, executa e audita todos os fluxos do Mordomo, com módulos internos para WhatsApp, Zipper, CRM, e-mail, calendário, watchdogs e aprendizados.

A migração não significa desligar tudo de uma vez. Significa:

- Centralizar ownership, estado, política e logs dentro do LC Mordomo OS.
- Manter conectores técnicos externos apenas quando necessário, como WACLI e Hermes cron scheduler.
- Substituir scripts soltos por módulos registrados no runtime.
- Expor tudo no dashboard como sistema operacional legível: jobs, decisões, fontes, últimos runs, bloqueios, filas e auditoria.

## Escopo inicial

### Entram no LC Mordomo OS

1. `mordomo_whatsapp_global_watch.py`
   - Núcleo de WhatsApp pessoal, auto-ack e follow-ups.
   - Deve virar módulo `whatsapp_context_engine`.

2. `zipper_zpr_enquiry_watcher.py`
   - Entrada ZPR/site e Zipper follow-up.
   - Deve virar módulo `zipper_lead_intake`.

3. `mordomo_crm_sync_local.py`
   - Sincronização CRM local/read-only.
   - Deve virar módulo `crm_sync`.

4. `zipper_main_email_monitor.py`
   - Monitor do e-mail principal Zipper.
   - Deve virar módulo `email_monitor`.

5. `zpr_artist_pdf_local_ingest.py`
   - Ingest local de PDFs/artistas.
   - Deve virar módulo `knowledge_ingest`.

6. `lcmordomo_critical_cron_watchdog.py`
   - Watchdog crítico.
   - Deve virar módulo `runtime_health`.

7. `Zipper Gmail draft engine — safe draft-only`
   - Deve virar módulo `email_draft_engine`.

8. Decision Inbox e resumos pausados
   - Devem ser substituídos por `decision_queue` com regra de interrupção: só Telegram se houver urgência real.

### Ficam como conectores técnicos, mas visíveis no OS

1. WACLI `pessoal`
   - Fonte de WhatsApp pessoal do Lucas.
   - Não é "lógica", é conector.

2. WACLI `hermes`
   - Fonte técnica do responder Hermes/LK.

3. Hermes cron scheduler
   - Pode continuar disparando o runtime inicialmente.
   - O ownership conceitual passa para LC Mordomo OS.

### Fora do núcleo Mordomo, mas precisam ser roteados

1. `lk_hermes_whatsapp_watchdog.sh`
2. `lk_hermes_whatsapp_responder_selftest.sh`
3. `lk_hermes_whatsapp_responder.py`

Esses são LK/Hermes. Devem ser exibidos no LC Mordomo OS como integrações vizinhas ou migrados para um módulo separado `external_integrations.lk_hermes`, não misturados com Zipper/Mordomo pessoal.

## Política central obrigatória

Todo módulo que sugere ou envia uma mensagem precisa passar pelo mesmo gate:

1. Ler contexto real recente.
2. Classificar estágio da conversa.
3. Aplicar matriz de autonomia.
4. Checar bloqueios sensíveis.
5. Checar idempotência e reconciliação.
6. Só então sugerir, rascunhar, auto-ack ou enviar.

### Bloqueios sensíveis

Sempre escalar ou exigir aprovação atual para:

- preço;
- disponibilidade;
- reserva;
- pagamento;
- negociação;
- reclamação;
- logística sensível;
- fornecedor;
- campanha/bulk;
- compromisso externo sem fonte atual.

### Regra Zipper crítica

Se o cliente já demonstrou interesse por obra específica, o LC Mordomo OS não pode sugerir follow-up genérico. Deve recomendar resposta contextual/pessoal do Lucas, muitas vezes por áudio.

## Arquitetura alvo

```text
LC Mordomo OS Runtime
├── registry/jobs.yaml
├── runtime/orchestrator.py
├── runtime/policy.py
├── runtime/idempotency.py
├── runtime/audit_log.py
├── modules/
│   ├── whatsapp_context_engine.py
│   ├── zipper_lead_intake.py
│   ├── crm_sync.py
│   ├── email_monitor.py
│   ├── email_draft_engine.py
│   ├── knowledge_ingest.py
│   ├── decision_queue.py
│   └── runtime_health.py
├── connectors/
│   ├── wacli_personal.py
│   ├── wacli_hermes.py
│   ├── gmail.py
│   ├── calendar.py
│   └── crm_store.py
└── dashboard/
    ├── runtime overview
    ├── job detail
    ├── decision queue
    ├── conversation intelligence
    └── audit timeline
```

## Modelo de job unificado

Cada job deve declarar:

- `id`
- `owner`: `mordomo`, `zipper`, `lk`, `hermes`, `pixel`
- `module`
- `schedule`
- `mode`: `read_only`, `draft_only`, `approval_gated`, `auto_safe`, `external_send`
- `sources`
- `writes`
- `approval_required`
- `silent_ok`
- `last_run_at`
- `last_status`
- `last_decision`
- `last_blockers`
- `rollback`

## Plano de migração

### Fase 0: Auditoria e congelamento

- Inventariar todos os crons, scripts, processos vivos, state files e outputs.
- Classificar ownership e risco.
- Criar snapshot/backup dos scripts e `cron/jobs.json`.
- Não mudar produção.

### Fase 1: Runtime read-only

- Criar registry de jobs e endpoint/dashboard read-only.
- O runtime apenas lê estados atuais e exibe.
- Nenhum cron antigo é pausado.

### Fase 2: Policy gate único

- Extrair política de contexto, autonomia, bloqueios e idempotência para módulo central.
- Testar com os casos existentes: follow-up seguro, José Luzada/obra específica, preço/disponibilidade, ZPR.
- Ainda sem cutover.

### Fase 3: Adaptadores por módulo

- Envolver cada script atual com um adapter interno ao runtime.
- Manter comportamento idêntico, mas logs e decisões passam pelo runtime.
- Rodar em dry-run paralelo contra os scripts atuais.

### Fase 4: Cutover progressivo

Ordem recomendada:

1. CRM sync read-only.
2. PDF ingest local-only.
3. Critical watchdog.
4. ZPR watcher approval-gated.
5. WhatsApp global watcher.
6. Email monitor/draft engine.

Cada cutover exige:

- teste unitário;
- dry-run;
- uma execução manual sem envio externo;
- comparação com estado antigo;
- aprovação explícita;
- plano de rollback.

### Fase 5: Dashboard operacional

Adicionar ao dashboard:

- jobs ativos/pausados;
- últimos runs;
- fila de decisões;
- conversation intelligence;
- bloqueios sensíveis;
- auditoria por contato/conversa;
- saúde dos conectores WACLI/Gmail/CRM.

## Critérios de aceite

- Lucas consegue responder: "o que está rodando?", "por que ele sugeriu isso?", "qual contexto ele leu?", "o que foi bloqueado?" diretamente no dashboard.
- Nenhum follow-up é sugerido/enviado sem `conversation_intelligence` registrada quando houver conversa relevante.
- Scripts antigos só ficam como wrappers ou conectores, não como donos da decisão.
- Crons críticos têm silent OK.
- Nenhum segredo ou PII bruto aparece em Telegram, dashboard público ou logs resumidos.
- Todos os módulos têm teste de regressão para bloqueios sensíveis.
- Cutover pode ser revertido por job individual.

## Não fazer sem aprovação explícita

- Pausar crons existentes.
- Reiniciar gateways.
- Alterar WACLI em produção.
- Enviar WhatsApp/e-mail.
- Fazer deploy/cutover.
- Expor novos endpoints públicos.

## Próximo artefato

Criar plano de implementação detalhado em `.hermes/plans/lc-mordomo-os-runtime-consolidation-2026-06-07.md` ou no Brain, com tarefas TDD pequenas e gates de rollback.
