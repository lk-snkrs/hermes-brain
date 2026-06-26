# Reconciliação final — Main/Mordomo, live scheduler e docs

Data/hora: 2026-05-27 12:07 UTC  
Base: `cronjob(action='list')` executado nesta rodada + docs de governança.  
Escopo: local/documental/read-only. Nenhum runtime, cron, gateway, Docker/VPS, produção, Shopify, Tiny, WhatsApp, e-mail, banco ou secret foi alterado.

## Veredito executivo

O runtime está saudável, mas o Brain ainda tem **drift documental** em torno de alguns crons antigos.

- Live scheduler atual: **21 jobs**.
- Todos ativos/scheduled.
- `last_status`: **ok** em todos os jobs listados.
- `last_delivery_error`: nenhum na listagem.
- Delivery vivo: **18 local / 3 origin**.
- Problema principal: **documentação antiga/control-plane cita jobs ou delivery que não batem 100% com o live list atual**.

## Ações recomendadas por prioridade

### P1 — reconciliar documentação, sem mexer no runtime

1. Atualizar o `cron-control-plane.md` para refletir o live list atual:
   - total 21, não 23;
   - `98478b820720` está `origin`, não `local`;
   - jobs não vistos no live list devem virar `histórico/não confirmado nesta rodada`.
2. Não alterar delivery agora sem uma decisão explícita, porque isso já vira mutação de cron.
3. Preservar a regra: Telegram/origin só para decisão, exceção, relatório aprovado ou alerta relevante.

### P2 — manter como está

- Mesa COO.
- Watchdogs centrais.
- Watchdogs de gateways.
- LK reports em delivery local.
- Zipper style learning local.
- SPITI gateway watchdog local.

### P3 — deixar em backlog de limpeza documental

- Rotas Zipper/Mordomo históricas.
- LK WhatsApp jobs citados em docs, mas não vistos no live list atual.
- LK GMC Review citado em docs, mas não visto no live list atual.
- Pixel AI Hub / Brainzinho citado em docs, mas não visto no live list atual.

## Reconciliação final por rotina viva

### `f5a23dd6a1bd` — Lucas Brain daily intelligence loop
- Presente no live scheduler: sim.
- Owner lógico: Operações / Hermes Brain / Chief of Staff.
- Runtime atual: `/opt/data/hermes_bruno_ingest/hermes-brain`.
- Delivery vivo: `local`.
- Status final: **manter**.
- Ação segura recomendada: manter local; usar como insumo, não como interrupção Telegram.

### `edd06fe19397` — Hermes runtime + cron watchdog no_agent
- Presente no live scheduler: sim.
- Owner lógico: Operações / runtime safety.
- Runtime atual: scheduler principal.
- Delivery vivo: `local`.
- Status final: **manter**.
- Ação segura recomendada: manter silent-OK.

### `7c688553e293` — LK Daily Sales Brief read-only mandatory delivery
- Presente no live scheduler: sim.
- Owner lógico: LK Ops / Comercial / Atendimento.
- Runtime atual: scheduler principal, script `lk_daily_sales_brief_watchdog.py`.
- Delivery vivo: `local`.
- Status final: **manter**.
- Ação segura recomendada: manter como local/read-only; não confundir com Growth.

### `953b9055458e` — LK Weekly CEO Review read-only mandatory delivery
- Presente no live scheduler: sim.
- Owner lógico: LK Ops / Comercial / Atendimento.
- Runtime atual: scheduler principal, script `lk_weekly_ceo_review_watchdog.py`.
- Delivery vivo: `local`.
- Status final: **manter**.
- Ação segura recomendada: manter local e semanal.

### `71b147362ec1` — Zipper Gmail style learning refresh
- Presente no live scheduler: sim.
- Owner lógico: Zipper OS documental/read-only.
- Runtime atual: `/opt/data`.
- Delivery vivo: `local`.
- Status final: **manter**.
- Ação segura recomendada: manter como aprendizado local; não transformar em draft/envio automático.

### `4bb4e2223fd3` — Hermes compression failure self-heal watchdog
- Presente no live scheduler: sim.
- Owner lógico: Operações / runtime safety.
- Runtime atual: scheduler principal.
- Delivery vivo: `local`.
- Status final: **manter**.
- Ação segura recomendada: manter silent-OK.

### `c3bb587519d2` — LK Pulso Comercial 16h read-only delivery
- Presente no live scheduler: sim.
- Owner lógico: LK Ops / Comercial / Atendimento.
- Runtime atual: scheduler principal, script `lk_financial_pulse_16h_watchdog.py`.
- Delivery vivo: `local`.
- Status final: **manter**.
- Ação segura recomendada: manter local; evitar duplicar Daily Sales Brief.

### `e3279babbc4a` — LK 09h previous-day sales report external delivery
- Presente no live scheduler: sim.
- Owner lógico: LK Ops / Comercial / Atendimento.
- Runtime atual: scheduler principal, script `lk_previous_day_09h_sales_report_watchdog.py`.
- Delivery vivo: `local`.
- Status final: **manter com cautela**.
- Ação segura recomendada: reconciliar nome “external delivery” vs delivery vivo `local`; não mudar canal sem packet.

### `a2ead305eab2` — LK 19h30 physical store close external delivery
- Presente no live scheduler: sim.
- Owner lógico: LK Ops / Comercial / Atendimento.
- Runtime atual: scheduler principal, script `lk_store_close_1930_watchdog.py`.
- Delivery vivo: `local`.
- Status final: **manter com cautela**.
- Ação segura recomendada: reconciliar nome “external delivery” vs delivery vivo `local`; não mudar canal sem packet.

### `ac0b440e2643` — Mordomo Telegram gateway watchdog
- Presente no live scheduler: sim.
- Owner lógico: Mordomo / Lucas pessoal.
- Runtime atual: profile Mordomo.
- Delivery vivo: `local`.
- Status final: **manter**.
- Ação segura recomendada: manter como watchdog de canal, não como owner de LK/Zipper.

### `357d40a5863e` — Zipper OS vendas 09h WhatsApp/email
- Presente no live scheduler: sim.
- Owner lógico: Zipper OS.
- Runtime atual: scheduler principal, script `zipper_weekday_sales_report_watchdog.py`.
- Delivery vivo: `local`.
- Status final: **manter com cautela**.
- Ação segura recomendada: documentar como fluxo Zipper guardrailed; não criar runtime Zipper por simetria e não expandir contato externo sem aprovação.

### `876d54c62ccd` — LK Growth Telegram gateway watchdog
- Presente no live scheduler: sim.
- Owner lógico: LK Growth.
- Runtime atual: profile LK Growth.
- Delivery vivo: `local`.
- Status final: **manter**.
- Ação segura recomendada: manter watchdog do gateway; não misturar com LK Ops.

### `749ee30b51eb` — Mesa COO diária Telegram
- Presente no live scheduler: sim.
- Owner lógico: Operações / COO.
- Runtime atual: `/opt/data/hermes_bruno_ingest/hermes-brain`.
- Delivery vivo: `origin`.
- Status final: **manter**.
- Ação segura recomendada: manter como superfície executiva principal no Telegram.

### `663e3e6a148c` — SPITI Telegram gateway watchdog
- Presente no live scheduler: sim.
- Owner lógico: SPITI OS.
- Runtime atual: profile SPITI.
- Delivery vivo: `local`.
- Status final: **manter**.
- Ação segura recomendada: manter watchdog local.

### `3fc45b0830c6` — Hermes Brain Fechamento Ágil 23h + Brain Sync
- Presente no live scheduler: sim.
- Owner lógico: Operações / Hermes Brain.
- Runtime atual: `/opt/data/hermes_bruno_ingest/hermes-brain`.
- Delivery vivo: `local`.
- Status final: **manter**.
- Ação segura recomendada: manter local/silent-OK; não transformar em recibo Telegram.

### `f4c499e85eac` — Lucas Brain weekly Learning Loop report
- Presente no live scheduler: sim.
- Owner lógico: Operações / melhoria contínua.
- Runtime atual: `/opt/data/hermes_bruno_ingest/hermes-brain`.
- Delivery vivo: `local`.
- Status final: **manter**.
- Ação segura recomendada: manter local; revisar se um dia voltar a gerar decisão semanal para Telegram.

### `d03fa04e1188` — Hermes Brain Operating Layer structural watchdog
- Presente no live scheduler: sim.
- Owner lógico: Operações / Brain.
- Runtime atual: scheduler principal.
- Delivery vivo: `local`.
- Status final: **manter**.
- Ação segura recomendada: manter silent-OK.

### `2404c0766d33` — Hermes Brain Runtime Truth Reconciler
- Presente no live scheduler: sim.
- Owner lógico: Operações / runtime truth.
- Runtime atual: `/opt/data/hermes_bruno_ingest/hermes-brain`.
- Delivery vivo: `local`.
- Status final: **manter**.
- Ação segura recomendada: manter; este job deve capturar justamente drifts como esta reconciliação.

### `98478b820720` — Relatório Hermes diário 23h + 02h para Lucas
- Presente no live scheduler: sim.
- Owner lógico: Operações / Hermes Brain.
- Runtime atual: `/opt/data/hermes_bruno_ingest/hermes-brain`.
- Delivery vivo: `origin`.
- Status final: **precisa decisão antes de alterar**.
- Ação segura recomendada: preparar packet curto se Lucas quiser reduzir ruído; não mudar para `local` sem aprovação explícita, porque é mutação de cron.
- Divergência documental: control-plane anterior dizia `local`; live list atual confirma `origin`.

### `d9badcd83411` — Hermes Brain strict-runtime guard watchdog
- Presente no live scheduler: sim.
- Owner lógico: Operações / segurança runtime docs.
- Runtime atual: scheduler principal.
- Delivery vivo: `local`.
- Status final: **manter**.
- Ação segura recomendada: manter silent-OK.

### `c1ce34b4449a` — Hermes multi-profile latency watchdog
- Presente no live scheduler: sim.
- Owner lógico: Operações / monitoramento de perfis.
- Runtime atual: scheduler principal.
- Delivery vivo: `origin`.
- Status final: **manter com regra de alerta**.
- Ação segura recomendada: manter se só avisa anomalia; se estiver enviando sucesso normal, ajustar depois com packet.

## Itens documentados mas não vistos no live list desta rodada

### `c358f8f56a26` — Pixel AI Hub / Brainzinho daily learning scan
- Presente no live scheduler: não.
- Owner lógico esperado: Hermes Agent / Operações Hermes.
- Status final: **histórico/não confirmado**.
- Ação segura recomendada: marcar no control-plane como não confirmado no scheduler principal; procurar em profile Mordomo só read-only antes de concluir removido.

### `71b2636add5d` — LK WhatsApp Hermes responder watchdog
- Presente no live scheduler: não.
- Owner lógico esperado: LK Ops / canal WhatsApp conforme risco.
- Status final: **histórico/não confirmado**.
- Ação segura recomendada: não recriar; primeiro reconciliar se existe em outro profile/registry.

### `a5d7a392eed9` — LK WhatsApp Hermes responder regression watchdog
- Presente no live scheduler: não.
- Owner lógico esperado: LK Ops / QA de WhatsApp.
- Status final: **histórico/não confirmado**.
- Ação segura recomendada: não recriar; primeiro reconciliar se existe em outro profile/registry.

### `d4c26da4cd48` — LK GMC Review read-only mandatory delivery
- Presente no live scheduler: não.
- Owner lógico esperado: LK Growth/GMC.
- Status final: **histórico/não confirmado**.
- Ação segura recomendada: não recriar; primeiro confirmar se foi removido, migrado ou está em registry diferente.

## Conclusão

A malha atual está funcional. A limpeza necessária agora é **documental**, não operacional:

1. Atualizar o control-plane com o live list atual.
2. Marcar jobs não vistos como `histórico/não confirmado nesta rodada`.
3. Criar packet separado se Lucas quiser mudar `98478b820720` de `origin` para `local` para reduzir ruído.
4. Preservar autonomia dos especialistas: LK Ops, LK Growth, Zipper e SPITI continuam donos lógicos dos seus assuntos, mesmo quando o scheduler técnico fica no Main.

## O que não foi feito

- Nenhum cron foi alterado.
- Nenhum delivery foi alterado.
- Nenhum gateway/profile foi reiniciado.
- Nenhum Docker/VPS/Traefik/container foi tocado.
- Nenhum write externo foi executado.
- Nenhum Shopify/Tiny/WhatsApp/e-mail/banco foi tocado.
