# LC Mordomo OS — Plano de Controle Operacional

**Data:** 2026-06-05  
**Dono:** Lucas Cimino  
**Sistema:** LC Mordomo OS / Mordomo Central  
**Status:** v0.1 vivo — atualizado após correções de follow-up WhatsApp e parser de e-mail Zipper  
**Modo desta atualização:** local/documental/read-only sobre runtime; nenhuma mensagem externa, banco, infra ou cron foi alterado por este artefato.

---

## 1. Função deste plano

Este arquivo é o plano de controle do **LC Mordomo OS**. Ele conecta:

- PRD central do sistema;
- SOUL do Mordomo Central;
- registry de subagentes;
- rotinas de handoff, fonte e aprovação;
- módulos reais já rodando no profile `mordomo`;
- pendências de implementação e critérios de pronto.

O objetivo é evitar que o Mordomo vire um conjunto de scripts soltos. Todo módulo recorrente deve ter dono, fonte, risco, contrato de entrega e critério de verificação.

---

## 2. Arquitetura aprovada até agora

Tese operacional:

```text
Lucas
  ⇄ LC Mordomo Central
      ⇄ Subagente Pessoal/Calendário
      ⇄ Subagente Zipper
      ⇄ Subagente SPITI
      ⇄ Subagente LK
      ⇄ Subagente Hermes/Infra
      ⇄ Subagente CRM/Relacionamentos
      ⇄ Subagente Governança/Qualidade
```

Regra principal: Lucas fala com um ponto central. Subagentes são força interna, não múltiplos bots para Lucas gerenciar.

Artefatos canônicos atuais:

- `areas/operacoes/prds/lcmordomo-os-prd-2026-06-05.md`
- `areas/operacoes/mordomo/LC-MORDOMO-CENTRAL-SOUL-2026-06-05.md`
- `areas/operacoes/mordomo/subagent-registry-2026-06-05.md`
- `areas/operacoes/rotinas/lcmordomo-handoff-protocol.md`
- `areas/operacoes/rotinas/lcmordomo-source-confidence-and-approval-ledger.md`
- `areas/operacoes/prds/lcmordomo-subagente-zipper-migration-prd-2026-06-05.md`
- `areas/operacoes/prds/lcmordomo-whatsapp-pessoal-followup-autoack-prd-2026-06-05.md`

---

## 3. Estado runtime verificado em 2026-06-05

Fonte: `/opt/data/profiles/mordomo/cron/jobs.json` e estados locais em `/opt/data/profiles/mordomo/state/`.

### 3.1 Crons/Módulos ativos relevantes

- **Mordomo global WhatsApp watcher — Lucas pessoal**
  - ID: `6f4c913082db`
  - Status verificado: `enabled=true`, `state=scheduled`
  - Frequência: every 5m
  - Último status: `ok`
  - Script: `mordomo_whatsapp_global_watch.py`
  - Papel: intake/roteamento de WhatsApp pessoal, auto-ack seguro, follow-up e escalonamento.
  - Observação: foi reativado e corrigido em 2026-06-05 após falhas Lara/Henrique.

- **Mordomo CRM local sync**
  - ID: `daf97feec481`
  - Status verificado: ativo/scheduled
  - Frequência: every 10m
  - Script: `mordomo_crm_sync_local.py`
  - Papel: espelho local estruturado de CRM/follow-up e futura ponte para Supabase por domínio.

- **ZPR Enquiry Form watcher — approval-gated**
  - ID: `871b9bc5617a`
  - Status verificado: ativo/scheduled
  - Frequência: every 5m
  - Script: `zipper_zpr_enquiry_watcher.py`
  - Papel: intake ZPR/site → PDF/lead/follow-up; envio/ações externas continuam guardrailadas conforme classe.

- **Zipper direct main e-mail monitor — zipper@zippergaleria.com.br**
  - ID: `20972b3c7595`
  - Status verificado: ativo/scheduled
  - Frequência: every 60m
  - Script: `zipper_main_email_monitor.py`
  - Papel: monitor da caixa principal Zipper; registro Brain com corpo full/legível.
  - Correção 2026-06-05: parser passou a buscar RFC822 completo, decodificar MIME/quoted-printable e gravar corpo completo legível.

- **Zipper Gmail draft engine — safe draft-only**
  - ID: `5bbe5169fe62`
  - Status verificado: ativo/scheduled
  - Frequência: every 15m
  - Papel: draft/triagem safe draft-only, sem envio externo autônomo.

- **Zipper artist PDFs local-only known-answer ingest**
  - ID: `f537bb9c505b`
  - Status verificado: ativo/scheduled
  - Frequência: every 30m
  - Papel: registry local de PDFs/manifests e known-answer limitado.

### 3.2 Crons pausados relevantes

- **Mordomo global Calendar watcher**
  - ID: `fe5cf7f1b228`
  - Status: pausado
  - Último status: ok em 2026-06-02
  - Decisão: não reativar automaticamente neste plano; primeiro formalizar o contrato Pessoal/Calendário e verificar se há pendências reais.

- **Mordomo Decision Inbox digest**
  - ID: `e46ea230f0cf`
  - Status: pausado
  - Decisão: manter pausado. Lucas priorizou follow-up automático seguro sobre digest genérico. Só reativar se redesenhado como pacote action-ready.

- **Mordomo WhatsApp pessoal resumo 17h BRT**
  - ID: `3bcbf3be9b73`
  - Status: pausado
  - Decisão: manter pausado enquanto não houver contrato de digest limpo; alertas devem ser decisão/exceção/falha, não resumo ruidoso.

### 3.3 Estado local de follow-up

Fonte: `/opt/data/profiles/mordomo/state/mordomo_followup_queue.json`.

Snapshot observado:

- `signals`: 2666
- `sent_actions`: 94
- `updated_at`: `2026-06-05T20:19:10.864886+00:00`
- principais grupos de status:
  - Zipper `auto_sent/post_pdf_followup`: 15
  - Zipper `manual_sent` diversos: 29+
  - Zipper `responded_by_lucas`: múltiplas classes sensíveis e follow-up
  - Zipper `needs_lucas_decision/post_pdf_followup`: 5
  - Zipper `waiting_client/post_pdf_followup`: 3
  - LK e SPITI aparecem na fila, mas ainda sem subagente operacional próprio no LC Mordomo.

Leitura: o coração atual do LC Mordomo OS já é Zipper/follow-up. A próxima engenharia deve reduzir mistura de estados globais e promover objetos por domínio.

---

## 4. Módulos do LC Mordomo OS

### 4.1 Mordomo Central

**Status:** operacional/documentado.  
**Dono:** LC Mordomo Central.  
**Função:** roteamento, proteção de atenção, decisão, governança e learning loop.  
**Fonte:** Brain + runtime local + fontes vivas quando necessário.  
**Próximo critério de pronto:** todo alerta ao Lucas seguir contrato action-first, sem wrapper de cron/JSON/log.

### 4.2 Subagente Zipper

**Status:** prioridade 1; operacional parcial via scripts/crons existentes.  
**Dono lógico:** Subagente Zipper, mediado pelo Mordomo Central.  
**Já cobre:**

- ZPR/site watcher;
- envio/registro pós-PDF em classes já aprovadas;
- auto-ack A1/A2 no WhatsApp pessoal;
- CRM local de interesse por artista;
- supressão por budget/negative-fit;
- e-mail principal Zipper com registro full legível;
- draft-only Gmail;
- PDF/known-answer local.

**Gaps:**

- Supabase Zipper ainda não é destino primário de todos os objetos estáveis;
- scripts caso-a-caso ainda precisam virar executor genérico/fixtures;
- Decision Inbox Zipper ainda precisa ser pacote único, não fila solta;
- rotina de self-heal/watchdog para crons de follow-up ainda não está formalizada.

**Critério de pronto MVP:** leads Zipper entram em CRM/follow-up estruturado, follow-ups seguros rodam sem Lucas, e só sobem preço/disponibilidade/reserva/pagamento/negociação/reclamação.

### 4.3 WhatsApp pessoal / Follow-up / Auto-ack

**Status:** corrigido e ativo em 2026-06-05.  
**Dono:** Mordomo Central + Subagente Zipper para contexto Zipper.  
**Classes seguras:** agradecimento, recebido, vou olhar/analisar/verificar/avaliar/encaminhar e retorno se houver interesse.  
**Bloqueios:** preço, disponibilidade, reserva, pagamento, desconto, medida, frete, urgência, reclamação, pergunta material.

**Critério de pronto:**

- cron watcher scheduled/ok;
- execução silenciosa sem backlog duplicado;
- fixtures positivas e negativas mantidas;
- follow-up paralelo mesclado no canônico quando for ZPR/PDF;
- erro de cron pós-envio tratado por reconciliação antes de retry.

### 4.4 Zipper e-mail principal

**Status:** corrigido e ativo em 2026-06-05.  
**Dono:** Subagente Zipper / inbox monitor.  
**Regra nova:** artefato no Brain deve trazer corpo completo legível, não trecho parcial limpo nem MIME/quoted-printable cru.  
**Critério de pronto:** cada e-mail útil vira artifact com headers, corpo completo, classificação, risco e próximo passo; financeiro/admin rotineiro não interrompe Lucas por padrão.

### 4.5 Decision Inbox

**Status:** pausado/redesign necessário.  
**Dono futuro:** Mordomo Central com handoff dos subagentes.  
**Decisão atual:** não reativar digest genérico.  
**Critério de pronto:** cada alerta deve conter decisão/recomendação/draft/fonte/risco. Se for follow-up seguro, não deve virar decisão.

### 4.6 Pessoal/Calendário

**Status:** subagente lógico; cron de calendar watcher pausado.  
**Próximo passo seguro:** auditar contrato de calendário e pendências reais antes de reativar.  
**Critério de pronto:** compromisso com data/hora/contexto claro vira evento/reminder; visita não confirmada vira follow-up logístico; ambiguidade/sensível escala.

### 4.7 SPITI

**Status:** planejado.  
**Próximo passo:** criar SOUL/contrato operacional SPITI dentro do LC Mordomo OS e mapear fontes de verdade.  
**Critério:** nenhum dado de lance/leilão afirmado sem fonte primária; silêncio > dado errado.

### 4.8 LK

**Status:** planejado para fase posterior do LC Mordomo OS.  
**Próximo passo:** integrar como inteligência read-only, não como distração do núcleo Zipper/SPITI.  
**Critério:** LK entra por relatórios/drafts/read-only; customer/campaign/price/stock writes continuam aprovação-gated.

### 4.9 Hermes/Infra e Governança

**Status:** operacional parcial.  
**Responsabilidade:** crons, scripts, parser, QA, skill/Brain updates, watchdogs.  
**Gap crítico:** self-heal/watchdog de crons seguros de follow-up ainda precisa virar rotina/script formal.

---

## 5. Backlog priorizado

### P0 — Blindar follow-up seguro contra nova parada — concluído em 2026-06-05

**Implementado:** `/opt/data/profiles/mordomo/scripts/lcmordomo_critical_cron_watchdog.py`.

Escopo ativo:

- verifica `Mordomo global WhatsApp watcher — Lucas pessoal` enabled/scheduled;
- verifica `ZPR Enquiry Form watcher — approval-gated` enabled/scheduled;
- verifica `Zipper direct main e-mail monitor` enabled/scheduled;
- reativa localmente jobs críticos pausados quando a correção é segura/reversível;
- alerta Lucas só se houver falha real ou impossibilidade de self-heal seguro;
- não reinicia infra, não altera Docker/VPS, não envia mensagens externas.

**Cron registrado:** `LC Mordomo OS critical cron watchdog`, ID `lcmcw202606`, every 10m, `no_agent=true`, `deliver=local`.

**Critério de pronto atingido:** dry-run e run real retornaram `actions=[]`, `alerts=[]`, `changed=false`; crons críticos estavam enabled/scheduled/ok.

### P0 — Padronizar parser `wacli --json` — concluído em 2026-06-05

**Implementado:** `/opt/data/profiles/mordomo/scripts/mordomo_json_utils.py` com `parse_mixed_json()` / `wacli_data()`.

Aplicado nos watchers ativos:

- `mordomo_whatsapp_global_watch.py`;
- `zipper_whatsapp_response_watch.py`.

`zipper_zpr_enquiry_watcher.py` já usava parser tolerante equivalente em seu caminho de envio.

**Critério de pronto atingido:** fixtures cobrem JSON limpo, logs antes do JSON, objeto aninhado antes de `success:true` e payload lista; `py_compile` OK.

Relatório: `areas/operacoes/reports/lcmordomo-p0-watchdog-parser-2026-06-05.md`.

### P1 — Consolidar Zipper MVP runtime → objetos — concluído em 2026-06-05

**Implementado:** `/opt/data/profiles/mordomo/scripts/zipper_canonical_store_build.py`.

**Store local derivado:** `/opt/data/profiles/mordomo/state/zipper_canonical.sqlite`.

Objetos canônicos criados:

- `contact`;
- `lead_enquiry`;
- `artist_interest`;
- `followup`;
- `suppression`;
- `sent_action`;
- `decision_packet`.

**Snapshot do build:** `contact=130`, `lead_enquiry=9`, `artist_interest=32`, `followup=120`, `suppression=2`, `sent_action=171`, `decision_packet=15`.

**Critério de pronto atingido para P1.1:** runtime Zipper existente agora pode ser lido por objetos canônicos locais e rebuildable/idempotentes. O store é cache local, não Supabase e não fonte externa de verdade.

**Relatório:** `areas/operacoes/reports/lcmordomo-p1-zipper-canonical-store-2026-06-05.md`.

### P1 — Decision Inbox action-ready — P1.2 dry-run concluído em 2026-06-05

**Implementado:** `/opt/data/profiles/mordomo/scripts/zipper_canonical_queries.py`.

Consultas locais criadas:

- `summary` — resumo operacional do `zipper_canonical.sqlite`;
- `trace <termo>` — rastreio ponta-a-ponta por contato/artista/lead;
- `decision-dryrun --write` — classificação local de `decision_packet` em buckets action-ready.

**Resultado do dry-run:** 15 candidatos brutos viraram apenas 3 `action_ready_candidate` reais. O restante foi separado em `technical_error_local`, `suppress_followup_noise`, `review_before_alert`, `needs_enrichment` e `hard_recipient_blocklist`.

**Correção aplicada durante P1.2:** destinatários bloqueados por regra operacional, como Ivan Grilo e LK Sneakers, não podem virar candidato comum de envio/alerta; foram classificados como `hard_recipient_blocklist`.

**Relatório:** `areas/operacoes/reports/lcmordomo-p12-zipper-decision-inbox-dryrun-2026-06-05.md`.

**Critério de pronto P1.2 atingido:** Decision Inbox agora tem filtro local para não transformar follow-up seguro, erro técnico ou destinatário bloqueado em alerta solto para Lucas. Ainda não há envio Telegram/cron; é dry-run local.

### P1 — Zipper action packet renderer — P1.3 concluído em 2026-06-05

**Implementado:** `/opt/data/profiles/mordomo/scripts/zipper_action_packet_renderer.py`.

Saídas locais:

- `/opt/data/profiles/mordomo/state/zipper_action_packets_preview.json`;
- `areas/operacoes/reports/lcmordomo-p13-zipper-action-packet-renderer-2026-06-05.md`.

**Resultado:** os 3 candidatos action-ready viraram pacotes Lucas-facing com contexto, fonte mascarada, risco, recomendação, draft e decisão sugerida. Os demais 12 itens ficaram fora do alerta.

**Correção aplicada durante P1.3:** mascaramento de fonte foi ajustado para tratar WhatsApp JID como telefone mascarado, não como e-mail.

**Critério de pronto P1.3 atingido:** renderer recompõe a classificação a partir do SQLite local, gera somente pacotes action-first, passa regressão de termos proibidos de cron/log/classificador e não envia nada.

### P1 — Zipper packet QA + activation decision — P1.4 concluído em 2026-06-05

**Implementado:** `/opt/data/profiles/mordomo/scripts/test_zipper_action_packet_renderer.py` e função `activation_decision()` no renderer.

**Relatório:** `areas/operacoes/reports/lcmordomo-p14-zipper-packet-qa-activation-decision-2026-06-05.md`.

**Regressões cobertas:** 3 pacotes positivos, 12 itens negativos suprimidos, contrato Lucas-facing, termos proibidos, PII/JID masking e bloqueio de ativação sem aprovação explícita.

**Decisão de ativação:** bloqueada. O renderer está pronto para QA local, mas não pode criar cron nem enviar Telegram sem aprovação explícita do Lucas para formato, destino e cadência.

**Critério de pronto P1.4 atingido:** teste local `python3 -m unittest test_zipper_action_packet_renderer -v` passa e o gate `activation_decision(..., explicit_approval=False)` mantém entrega bloqueada.

### P1 — Zipper editorial packets + delivery proposal — P1.5 concluído em 2026-06-05

**Implementado:** pacote Lucas-facing v2 no renderer, regressões editoriais e função `delivery_contract_proposal()`.

**Relatório:** `areas/operacoes/reports/lcmordomo-p15-zipper-editorial-delivery-contract-2026-06-05.md`.

**Resultado:** os 3 pacotes ficaram mais curtos e orientados a decisão: decisão para Lucas, contexto curto, cuidado, recomendação, draft e opções. Removidos ruídos de timestamp/canais de outbound, códigos de risco no texto Lucas-facing e termos de classificador.

**Contrato proposto, não ativado:** `telegram:origin`, sob demanda ou 1 vez ao dia somente se houver pacote, máximo 3 pacotes, vazio silencioso, kill-switch para log/classificador/PII/pacote sem decisão/excesso de itens.

**Critério de pronto P1.5 atingido:** suíte local ampliada para 7 testes, renderer gera JSON preview com proposta de entrega e `activation_decision(..., explicit_approval=False)` segue bloqueando cron/Telegram.

### P1 — Correção Lucas: follow-ups não são Decision Inbox — P1.6 concluído em 2026-06-05

**Correção:** Lucas informou que os 3 exemplos eram follow-ups e, portanto, não deveriam virar aprovação. Mordomo deve fazer follow-ups sozinho; para follow-ups importantes, deve buscar o contexto das mensagens anteriores ligadas antes de executar.

**Implementado:** classificador ajustado para `important_followup_needs_context`, fila local `/opt/data/profiles/mordomo/state/zipper_important_followup_context_queue.json` e regressões locais.

**Relatório:** `areas/operacoes/reports/lcmordomo-p16-zipper-followup-correction-context-queue-2026-06-05.md`.

**Resultado atualizado:** `telegram_ready_count=0`, 0 pacotes Decision Inbox, 5 follow-ups importantes em fila de contexto antes de execução autônoma.

**Critério de pronto P1.6 atingido:** suíte local ampliada para 8 testes; nenhuma entrega externa, cron ou Supabase acionado.

### P1 — Zipper context enricher de follow-ups — P1.7 concluído em 2026-06-06

**Implementado:** `/opt/data/profiles/mordomo/scripts/zipper_followup_context_enricher.py` e regressão `/opt/data/profiles/mordomo/scripts/test_zipper_followup_context_enricher.py`.

**Saídas locais:**

- `/opt/data/profiles/mordomo/state/zipper_followup_context_enriched.json`;
- `areas/operacoes/reports/lcmordomo-p17-zipper-followup-context-enricher-2026-06-06.md`.

**Resultado:** 5 follow-ups importantes enriquecidos a partir do `zipper_canonical.sqlite`; 2 classificados como `blocked_sensitive_material`, 3 como `needs_lucas_context`, 0 liberados para envio por este passo.

**Critério de pronto P1.7 atingido:** contexto local mascarado, sem raw JID/telefone/e-mail, `py_compile` OK, regressões OK e Brain health OK. Nenhum Telegram, WhatsApp, e-mail, cron, Supabase, produção ou infra acionado.

**Próximo gate P1.8:** executor live/idempotente deve buscar histórico bruto do mesmo canal antes de qualquer follow-up, bloquear termos materiais, deduplicar por `sent_action` e só então enviar classes seguras já aprovadas.

### P2 — Pessoal/Calendário

**Ação:** formalizar contrato e avaliar reativação do calendar watcher.

**Critério de pronto:** evento/reminder/follow-up logístico claro; sem compromisso ambíguo automático.

### P2 — SPITI

**Ação:** criar subagente lógico SPITI dentro do LC Mordomo OS.

**Critério de pronto:** fontes primárias e blockers mapeados; nenhuma afirmação sem fonte.

### P3 — LK

**Ação:** integrar LK como read-only intelligence depois de Zipper/SPITI.

**Critério de pronto:** reports/drafts úteis sem writes externos.

---

## 6. Regras de entrega ao Lucas

Lucas só deve receber:

- decisão real;
- aprovação necessária;
- falha/exceção;
- risco;
- resumo executivo pedido;
- confirmação de entrega material quando útil.

Não enviar:

- logs crus;
- JSON;
- wrapper de cron;
- recibo de sucesso rotineiro;
- “tem coisas para ver” sem decisão;
- follow-up seguro como Decision Inbox.

---

## 7. Próxima execução recomendada

Próxima frente segura: **P1.7 context enricher + executor seguro de follow-up**.

Sequência:

1. Ler `/opt/data/profiles/mordomo/state/zipper_important_followup_context_queue.json`.
2. Para cada item, buscar mensagens anteriores ligadas ao lead/contato nas fontes locais disponíveis.
3. Reclassificar em `safe_to_autofollowup`, `needs_lucas_context` ou `blocked_sensitive_material`.
4. Executar autonomamente apenas `safe_to_autofollowup`, com idempotência e sem duplicar mensagens.
5. Alertar Lucas só para itens que precisam de contexto humano ou têm material sensível.

Parar antes de qualquer ação que envolva Docker/VPS/restart/deploy/secrets/banco de produção/Supabase write ou envio externo fora das classes A1/A2 já autorizadas.
