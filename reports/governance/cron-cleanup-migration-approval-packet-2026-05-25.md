# Approval packet — Cron ownership cleanup/migration pós-organograma

Data: 2026-05-25
Status: packet preparado; nenhuma alteração executada ainda.

## Escopo aprovado a confirmar

Lucas aprovou seguir. Para evitar alteração ampla demais, este packet divide a execução em blocos pequenos com rollback. A execução só deve mexer nos jobs listados em cada bloco aprovado.

## Bloco 1 — Reduzir ruído de Telegram

Objetivo: mover para `local` apenas entregas operacionais que não são decisões reais para Lucas. Manter Mesa COO em Telegram por ser decisão 1/N.

Candidatos encontrados:
- `main` `7c688553e293` — LK Daily Sales Brief read-only mandatory delivery — entrega `origin` — `0 11 * * *` — recomendação: move_to_local_if_no_decision_card
- `main` `953b9055458e` — LK Weekly CEO Review read-only mandatory delivery — entrega `origin` — `0 12 * * 1` — recomendação: move_to_local_if_no_decision_card
- `main` `d4c26da4cd48` — LK GMC Review read-only mandatory delivery — entrega `origin` — `0 12 * * 4` — recomendação: move_to_local_if_no_decision_card
- `main` `f4c499e85eac` — Lucas Brain weekly Learning Loop report — entrega `origin` — `15 12 * * 1` — recomendação: move_to_local_if_no_decision_card
- `main` `98478b820720` — Relatório Hermes diário 23h + 02h para Lucas — entrega `origin` — `30 5 * * *` — recomendação: move_to_local_if_no_decision_card
- `lk-growth` `738d3deabaeb` — LK Growth OS Weekly Growth Review — entrega `telegram` — `0 13 * * 1` — recomendação: keep_if_specialist_channel_expected_else_local
- `lk-growth` `1240644c5f3f` — LK Growth OS GMC Review read-only — entrega `telegram` — `0 12 * * 4` — recomendação: keep_if_specialist_channel_expected_else_local
- `lk-growth` `c45cda5fe2df` — LK Growth OS SEO/CRO impact review — SEO title/meta P1 packets — entrega `telegram` — `once at 2026-05-25 14:34` — recomendação: keep_if_specialist_channel_expected_else_local
- `lk-growth` `3526b59ca052` — LK CRO dev preview impact review — Onitsuka/NB/Kill Bill — entrega `origin` — `once at 2026-05-26 12:00` — recomendação: keep_if_specialist_channel_expected_else_local
- `lk-growth` `61717aaf7c61` — LK D+7 review — botão Compre Já branco PDP — entrega `origin` — `once at 2026-05-26 15:30` — recomendação: keep_if_specialist_channel_expected_else_local
- `lk-growth` `9834f69e3541` — LK D+7 review — PDP CRO production promotion 2026-05-19 — entrega `origin` — `once at 2026-05-26 15:30` — recomendação: keep_if_specialist_channel_expected_else_local
- `lk-growth` `d34a61f3bcd9` — LK PDP CRO hotfix D+7 review — trustbar/reviews/tryon — entrega `origin` — `once at 2026-05-26 15:45` — recomendação: keep_if_specialist_channel_expected_else_local
- `lk-growth` `3c6547609c35` — LK PDP preorder compact hotfix D+7 review — entrega `origin` — `once at 2026-05-26 16:05` — recomendação: keep_if_specialist_channel_expected_else_local
- `lk-growth` `20affa4dcba6` — LK n8n checkout abandonado hardening impact review — entrega `origin` — `once at 2026-05-27 17:50` — recomendação: keep_if_specialist_channel_expected_else_local
- `lk-growth` `350be0e438c7` — LK cart intent phase 2 — monitor 90min — entrega `origin` — `once in 30m` — recomendação: keep_if_specialist_channel_expected_else_local
- `lk-growth` `015cb75e8e91` — LK cart intent v2.2 cache/event monitor — entrega `origin` — `once in 15m` — recomendação: keep_if_specialist_channel_expected_else_local
- `lk-growth` `2fd730af8433` — LK cart intent Crisp REST identity review D+7 — entrega `origin` — `once at 2026-05-27 12:00` — recomendação: keep_if_specialist_channel_expected_else_local
- `lk-growth` `a215814309a2` — LK Recovery OS T1 go-live D+7 impact review — entrega `origin` — `once at 2026-05-28 12:00` — recomendação: keep_if_specialist_channel_expected_else_local
- `lk-growth` `36694eae598e` — LK Recovery OS production tracker propagation monitor — entrega `origin` — `once in 15m` — recomendação: keep_if_specialist_channel_expected_else_local
- `lk-growth` `fdc9ad165daa` — LK Recovery OS cart intent controlled LIVE runner — entrega `origin` — `every 30m` — recomendação: keep_if_specialist_channel_expected_else_local
- `lk-growth` `644f8a37e250` — LK Recovery OS checkout_started webhook D+7 impact review — entrega `origin` — `once in 7d` — recomendação: keep_if_specialist_channel_expected_else_local
- `lk-growth` `e87932cda969` — LK GEO llms.txt root D+7 impact review — entrega `origin` — `once at 2026-05-29 13:45` — recomendação: keep_if_specialist_channel_expected_else_local
- `lk-growth` `de3a45d36040` — LK SEO/GEO Experiment Ledger — weekly impact review — entrega `origin` — `30 13 * * 5` — recomendação: keep_if_specialist_channel_expected_else_local
- `lk-growth` `cd5f548bfe49` — LK collection GEO FAQ production D+7 impact review — entrega `origin` — `once at 2026-05-29 18:45` — recomendação: keep_if_specialist_channel_expected_else_local
- `lk-growth` `b58683155a65` — LK Auth Hub D+7 impact review — entrega `origin` — `once at 2026-05-29 19:11` — recomendação: keep_if_specialist_channel_expected_else_local
- `lk-growth` `e0f45429a4f7` — LK blog boutique premium D+7 impact review — entrega `origin` — `once in 7d` — recomendação: keep_if_specialist_channel_expected_else_local
- `lk-growth` `c90e2186b0a0` — LK NB blog rewrite D+7 impact review — entrega `origin` — `once in 7d` — recomendação: keep_if_specialist_channel_expected_else_local
- `lk-growth` `e0088791bb3b` — LK GEO Source Pages D+7 Impact Review — entrega `origin` — `once at 2026-05-30 10:00` — recomendação: keep_if_specialist_channel_expected_else_local
- `lk-growth` `0ab9cd485d15` — LK D+7 impact review — Adidas SL 72 OG vs RS GEO page table — entrega `origin` — `once in 7d` — recomendação: keep_if_specialist_channel_expected_else_local
- `lk-growth` `31b40105c4e5` — LK D+7 impact review — Packet D GEO Source Pages — entrega `origin` — `once at 2026-05-30 10:30` — recomendação: keep_if_specialist_channel_expected_else_local
- `lk-growth` `f81883cce339` — LK Menu Drawer Production D+7 Review — entrega `origin` — `once at 2026-05-30 13:00` — recomendação: keep_if_specialist_channel_expected_else_local
- `mordomo` `6f4c913082db` — Mordomo global WhatsApp watcher — Lucas pessoal — entrega `origin` — `every 5m` — recomendação: keep_if_specialist_channel_expected_else_local
- `mordomo` `fe5cf7f1b228` — Mordomo global Calendar watcher — entrega `origin` — `every 15m` — recomendação: keep_if_specialist_channel_expected_else_local
- `mordomo` `e46ea230f0cf` — Mordomo Decision Inbox digest — entrega `origin` — `0 9 * * *` — recomendação: keep_if_specialist_channel_expected_else_local
- `mordomo` `058df00bf941` — Mordomo A2 executor scaffold — entrega `origin` — `every 30m` — recomendação: keep_if_specialist_channel_expected_else_local
- `mordomo` `c358f8f56a26` — Pixel AI Hub / Brainzinho daily learning scan — entrega `origin` — `30 23 * * *` — recomendação: keep_if_specialist_channel_expected_else_local
- `mordomo` `20972b3c7595` — Zipper direct main e-mail monitor — zipper@zippergaleria.com.br — entrega `origin` — `every 60m` — recomendação: keep_if_specialist_channel_expected_else_local
- `mordomo` `3bcbf3be9b73` — Mordomo WhatsApp pessoal resumo 17h BRT — entrega `origin` — `0 20 * * *` — recomendação: keep_if_specialist_channel_expected_else_local
- `mordomo` `871b9bc5617a` — ZPR Enquiry Form watcher — approval-gated — entrega `origin` — `every 5m` — recomendação: keep_if_specialist_channel_expected_else_local
- `mordomo` `1f734765abc4` — Follow-up Leticia Albuquerque — importação/Portugal — entrega `origin` — `once at 2026-05-28 12:00` — recomendação: keep_if_specialist_channel_expected_else_local

Proposta de execução segura: começar só pelos candidatos `main` com recomendação `move_to_local_if_no_decision_card`; não tocar canais especialistas `telegram` sem validação de destino.
Rollback: restaurar `deliver` anterior a partir do backup do registry.

## Bloco 2 — Limpar one-shots expirados/pausados

Objetivo: reduzir sujeira operacional. Executar somente depois de backup dos registries e confirmar que não são rotinas recorrentes úteis.

Candidatos encontrados: 5
- `lk-growth` `350be0e438c7` — LK cart intent phase 2 — monitor 90min — paused — `once in 30m` — motivo: past_once
- `lk-growth` `015cb75e8e91` — LK cart intent v2.2 cache/event monitor — paused — `once in 15m` — motivo: past_once
- `lk-growth` `36694eae598e` — LK Recovery OS production tracker propagation monitor — paused — `once in 15m` — motivo: past_once
- `lk-growth` `fdc9ad165daa` — LK Recovery OS cart intent controlled LIVE runner — paused — `every 30m` — motivo: paused
- `mordomo` `058df00bf941` — Mordomo A2 executor scaffold — paused — `every 30m` — motivo: paused

Proposta de execução segura: remover apenas jobs `once` no passado e jobs pausados com receipt/histórico no Brain; se houver dúvida, manter e marcar `review`.
Rollback: backup JSON completo antes da remoção; restauração copiando o registry anterior.

## Bloco 3 — Migrar donos inequívocos

Objetivo: alinhar runtime ao organograma sem mudar comportamento funcional.
- migrar `main` → `lk-growth` `d4c26da4cd48` — LK GMC Review read-only mandatory delivery — Growth/GMC pertence ao LK Growth
- migrar `main` → `mordomo` `71b2636add5d` — LK WhatsApp Hermes responder watchdog — watcher de atendimento/WhatsApp deve ficar no Mordomo/LK atendimento
- migrar `main` → `mordomo` `a5d7a392eed9` — LK WhatsApp Hermes responder regression watchdog — watcher de atendimento/WhatsApp deve ficar no Mordomo/LK atendimento

Proposta de execução segura: copiar job para registry destino preservando id/name/schedule/script/deliver; pausar/remover origem somente depois de validar que destino aparece no registry. Preferir pausa temporária na origem antes de remoção definitiva.
Rollback: remover cópia no destino e restaurar/reativar origem a partir do backup.

## Ordem recomendada

1. Fazer backup dos registries atuais em `reports/governance/cron-registry-backups/`.
2. Executar Bloco 1 apenas para main/noise óbvio.
3. Verificar registry e registrar diff.
4. Só então executar Bloco 2 ou 3 em rodadas separadas.

## Bloqueios

- Não reiniciar gateway/Docker/VPS.
- Não alterar schedule/prompt/script nesta rodada, exceto `deliver` no Bloco 1 ou registry move explícito no Bloco 3.
- Não tocar produção externa, Shopify, GMC, WhatsApp, e-mail, Supabase.
- Não imprimir credenciais.

## Decisão sugerida

Executar primeiro somente o Bloco 1 restrito aos jobs main de ruído óbvio. Depois voltar com receipt e pedir próxima decisão.