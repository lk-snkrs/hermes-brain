# Cron Control Plane — Hermes Brain

Atualizado em: 2026-05-27 12:20 UTC

## Objetivo

Manter um controle executivo dos crons vivos do Hermes para reduzir ruído, duplicidade e jobs órfãos.

Este arquivo é um snapshot governamental do runtime local observado via registro Hermes. A fonte viva continua sendo `hermes cron list` / ferramenta `cronjob(action='list')`.

## Política

- Todo cron real deve ter owner, função, delivery e kill criteria.
- Watchdog técnico deve ser `silent-OK`.
- Telegram/origin é reservado para decisão, exceção, relatório aprovado ou falha relevante.
- Cron pausado por mais de 14 dias precisa decisão: remover, reativar, arquivar ou converter em rotina manual.
- Nenhum cron novo deve ser criado antes de checar duplicidade com 23h, 02h, 02h30 e Mesa COO.
- Loops de aprendizado Pixel AI Hub/Brainzinho/Openclawzinho pertencem ao Hermes Agent / Operações Hermes. Se o executor técnico ainda estiver no profile Mordomo para ler WhatsApp, o owner documental e o prompt devem apontar para Hermes Agent, não Mordomo.
- Rotina documentada não equivale a cron ativo: jobs ausentes do live list devem ficar como `histórico/não confirmado nesta rodada` até prova em outro scheduler/profile.

## Resumo do snapshot vivo

- Total observado no scheduler principal: 21 jobs.
- Ativos/scheduled: 21.
- Pausados: 0.
- Delivery `local`: 18.
- Delivery `origin`: 3.
- `last_status != ok`: 0.
- `last_delivery_error`: nenhum observado.
- Removidos em 2026-05-22 após aprovação de Lucas: 5 jobs pausados/orfãos.
- Criado em 2026-05-22 P2: `d9badcd83411` strict-runtime guard watchdog silent-OK.
- Reconciliação 2026-05-27: `98478b820720` está vivo como `origin`; a documentação anterior dizia `local`. Correção de preferência: Lucas quer este resumo no Telegram, então manter `origin` e não tratar como ruído por padrão.
- Reconciliação 2026-05-27: `c358f8f56a26`, `71b2636add5d`, `a5d7a392eed9` e `d4c26da4cd48` não apareceram no live list principal desta rodada; ficam históricos/não confirmados.

## Jobs ativos — controle

### Brain / governança central

- `f5a23dd6a1bd` — Lucas Brain daily intelligence loop
  - Schedule: `0 5 * * *` UTC / 02h BRT.
  - Delivery: `local`.
  - Owner: Operações / Hermes Brain / Chief of Staff.
  - Função: meta-supervisor diário.
  - Side effects: leitura e documentação local; sem write externo.
  - Kill criteria: duplicar Mesa COO sem gerar decisões novas por 7 dias; falhas recorrentes; output sem fonte.

- `3fc45b0830c6` — Hermes Brain Fechamento Ágil 23h + Brain Sync
  - Schedule: `0 2 * * *` UTC / 23h BRT.
  - Delivery: `local`.
  - Owner: Operações / Hermes Brain.
  - Função: consolidação diária + Brain Sync seguro.
  - Side effects: docs locais + sync allowlisted.
  - Kill criteria: dry-run/sync com FAIL; tentativa de tocar scripts/config/secrets; ruído no Telegram em sucesso normal.

- `98478b820720` — Relatório Hermes diário 23h + 02h para Lucas
  - Schedule: `30 5 * * *` UTC / 02h30 BRT.
  - Delivery vivo observado em 2026-05-27: `origin`.
  - Owner: Operações / Hermes Brain.
  - Função: resumo executivo curto sobre 23h + 02h que Lucas quer receber no Telegram.
  - Side effects: Telegram por `origin`.
  - Status documental: divergência real com snapshot anterior, que dizia `local`; preferência corrigida em 2026-05-27 para manter no Telegram.
  - Ação segura: manter `origin`; só mover para `local` se Lucas pedir explicitamente para parar este resumo no Telegram.
  - Kill criteria: duplicar Mesa COO; enviar sucesso técnico; mais de 5 itens sem decisão clara.

- `749ee30b51eb` — Mesa COO diária Telegram
  - Schedule vivo: `0 9 * * *` UTC.
  - Delivery: `origin`.
  - Owner: Operações / COO.
  - Função: fila executiva diária.
  - Side effects: Telegram.
  - Kill criteria: virar relatório longo; repetir 02h30; incluir item sem ação/fonte.

- `f4c499e85eac` — Lucas Brain weekly Learning Loop report
  - Schedule: `15 12 * * 1` UTC / segunda 09h15 BRT.
  - Delivery vivo: `local`.
  - Owner: Operações / melhoria contínua.
  - Função: revisão semanal de aprendizados.
  - Side effects: local; sem Telegram em sucesso normal.
  - Kill criteria: não gerar mudanças de skill/memória/rotina; repetir daily loop.

- `d03fa04e1188` — Hermes Brain Operating Layer structural watchdog
  - Schedule: `10 11 * * *` UTC.
  - Delivery: `local`.
  - Owner: Operações / Brain.
  - Função: checar estrutura do Brain Operating Layer.
  - Side effects: local/silent.
  - Kill criteria: output ruidoso sem anomalia; falso positivo recorrente.

- `d9badcd83411` — Hermes Brain strict-runtime guard watchdog
  - Schedule: `0 10 * * *` UTC / 07h BRT.
  - Delivery: `local`.
  - Owner: Operações / segurança runtime docs.
  - Função: rodar `scripts/operational_docs_guard.py --strict-runtime` diariamente.
  - Side effects: nenhum externo; stdout apenas em achados/erro de execução.
  - Kill criteria: falso positivo recorrente sem ajuste documentado; output em OK normal.

- `2404c0766d33` — Hermes Brain Runtime Truth Reconciler
  - Schedule: `20 11 * * *` UTC.
  - Delivery: `local`.
  - Owner: Operações / runtime truth.
  - Função: reconciliar docs vs runtime.
  - Side effects: local/silent.
  - Kill criteria: afirmar runtime sem evidência; duplicar inventário sem registrar diferença.

### Watchdogs técnicos

- `edd06fe19397` — Hermes runtime + cron watchdog no_agent
  - Schedule: `*/30 * * * *`.
  - Delivery: `local`.
  - Owner: Operações / runtime safety.
  - Kill criteria: prints em OK normal; restart sem receipt.

- `4bb4e2223fd3` — Hermes compression failure self-heal watchdog
  - Schedule: `*/10 * * * *`.
  - Delivery: `local`.
  - Owner: Operações / runtime safety.
  - Kill criteria: auto-heal fora do escopo seguro; spam.

- `ac0b440e2643` — Mordomo Telegram gateway watchdog
  - Schedule: `every 1m`.
  - Delivery: `local`.
  - Owner: Mordomo / Lucas pessoal.
  - Kill criteria: mexer no gateway sem aprovação fora de restart seguro documentado; spam.

- `876d54c62ccd` — LK Growth Telegram gateway watchdog
  - Schedule: `every 1m`.
  - Delivery: `local`.
  - Owner: LK Growth.
  - Kill criteria: spam; reinício em loop.

- `663e3e6a148c` — SPITI Telegram gateway watchdog
  - Schedule: `every 1m`.
  - Delivery: `local`.
  - Owner: SPITI OS.
  - Kill criteria: spam; reinício em loop.

- `c1ce34b4449a` — Hermes multi-profile latency watchdog
  - Schedule: `every 15m`.
  - Delivery: `origin`.
  - Owner: Operações / monitoramento de perfis.
  - Função: alerta de latência entre múltiplos profiles.
  - Side effects: Telegram quando houver anomalia relevante.
  - Kill criteria: alertar sucesso normal; alertar histórico já recuperado como se fosse falha atual.

### LK / negócio

Nota de ownership: nesta seção, diferenciar `LK Growth`, `LK Shopify` e `LK Comercial/Ops`. SEO, CRO, GEO, GMC, analytics, conteúdo e impact reviews pertencem ao especialista LK Growth. Produto/upload/coleções/superfície Shopify pertencem ao especialista LK Shopify. Vendas, pulso comercial, fechamento de loja e reports comerciais obrigatórios pertencem a LK Ops/Comercial. Não migrar automaticamente relatórios comerciais para LK Growth só por conterem “LK”.

- `7c688553e293` — LK Daily Sales Brief read-only mandatory delivery
  - Schedule: `0 11 * * *` UTC / 08h BRT.
  - Delivery vivo: `local`.
  - Owner: LK Ops / Comercial / Atendimento.
  - Função: briefing diário read-only.
  - Kill criteria: fonte indisponível sem sinalizar; dados sem verificação; misturar Tiny/Shopify indevidamente.

- `953b9055458e` — LK Weekly CEO Review read-only mandatory delivery
  - Schedule: `0 12 * * 1` UTC / segunda 09h BRT.
  - Delivery vivo: `local`.
  - Owner: LK Ops / Comercial / Atendimento.
  - Kill criteria: repetir daily sem insight semanal; enviar sem fonte.

- `c3bb587519d2` — LK Pulso Comercial 16h read-only delivery
  - Schedule: `0 19 * * *` UTC / 16h BRT.
  - Delivery: `local`.
  - Owner: LK Ops / Comercial / Atendimento.
  - Kill criteria: envio Telegram de sucesso; duplicar Daily Sales Brief.

- `e3279babbc4a` — LK 09h previous-day sales report external delivery
  - Schedule: `0 12 * * *` UTC / 09h BRT.
  - Delivery vivo: `local`.
  - Owner: LK Ops / Comercial / Atendimento.
  - Status: manter com cautela; nome sugere entrega externa, mas runtime está local.
  - Kill criteria: envio externo fora do script/escopo aprovado; fonte ausente.

- `a2ead305eab2` — LK 19h30 physical store close external delivery
  - Schedule: `30 22 * * *` UTC / 19h30 BRT.
  - Delivery vivo: `local`.
  - Owner: LK Ops / Comercial / Atendimento.
  - Status: manter com cautela; nome sugere entrega externa, mas runtime está local.
  - Kill criteria: envio externo fora do script/escopo aprovado; fonte ausente.

### Zipper / negócio

- `357d40a5863e` — Zipper OS vendas 09h WhatsApp/email
  - Schedule: `0 12 * * 1-5` UTC / dias úteis 09h BRT.
  - Delivery: `local`.
  - Owner: Zipper OS.
  - Kill criteria: contato externo fora dos destinatários aprovados; dados não vindos de `vendas_tango`; misturar SPITI.

- `71b147362ec1` — Zipper Gmail style learning refresh
  - Schedule: `20 6 * * *` UTC.
  - Delivery: `local`.
  - Owner: Zipper OS documental/read-only.
  - Kill criteria: criar draft/responder e-mail; usar e-mail enviado como autorização.

## Documentados mas não vistos no live list principal em 2026-05-27

Estes itens ficam históricos/não confirmados até prova em outro scheduler/profile. Não recriar automaticamente.

- `c358f8f56a26` — Pixel AI Hub / Brainzinho daily learning scan
  - Estado: não apareceu no `cronjob(action='list')` principal de 2026-05-27.
  - Owner documental esperado: Hermes Agent / Operações Hermes.
  - Ação segura: procurar read-only em profile Mordomo/registry antigo antes de declarar removido.

- `71b2636add5d` — LK WhatsApp Hermes responder watchdog
  - Estado: não apareceu no live list principal de 2026-05-27.
  - Owner esperado: LK Ops / WhatsApp, se existir.
  - Ação segura: não recriar; reconciliar origem e guardrails antes de qualquer ativação.

- `a5d7a392eed9` — LK WhatsApp Hermes responder regression watchdog
  - Estado: não apareceu no live list principal de 2026-05-27.
  - Owner esperado: LK Ops / QA WhatsApp, se existir.
  - Ação segura: não recriar; reconciliar origem e guardrails antes de qualquer ativação.

- `d4c26da4cd48` — LK GMC Review read-only mandatory delivery
  - Estado: não apareceu no live list principal de 2026-05-27.
  - Owner esperado: LK Growth/GMC.
  - Ação segura: não recriar; confirmar se foi removido, migrado ou está em registry diferente.

## Jobs pausados removidos — decisão executada em 2026-05-22

Após aprovação explícita de Lucas, os 5 jobs pausados/orfãos foram removidos do scheduler principal para reduzir ruído e risco de reativação acidental:

- `c214051f7780` — LK weekly influencer sales email
  - Motivo: escopo FHITS/Pareto/destinatários precisa novo approval packet antes de recriar.

- `15777e3416dc` — LK SEO/CRO weekly Claude SEO improvement loop
  - Motivo: trabalho operacional deve pertencer ao specialist/profile LK Growth; main Hermes fica em governança.

- `4ced266825f0` — Mordomo WhatsApp pessoal resumo 17h BRT
  - Motivo: Mordomo operacional pertence ao profile Mordomo, não ao main scheduler.

- `051f05ce17c1` — Mordomo WhatsApp pessoal realtime scan
  - Motivo: Mordomo operacional pertence ao profile Mordomo; recriação exige dry-run state safety verificado.

- `a7e883edd200` — LK SEO/CRO impact review — SEO title/meta P1 packets
  - Motivo: one-shot pausado/órfão; recriar apenas se ainda houver janela, fonte GSC/GA4 e pacote aprovado.

## Critérios antes de criar cron novo

1. Existe rotina `.md` correspondente?
2. Existe owner e empresa/área clara?
3. Output é local, origin ou externo? Por quê?
4. O job é silent-OK?
5. Qual erro vira alerta?
6. Qual critério de remoção?
7. Ele duplica 23h, 02h, 02h30, Mesa COO ou watchdog existente?
8. Usa secrets por Doppler/ambiente sem imprimir?
9. Tem rollback/disable path?

## Próxima revisão recomendada

- Confirmar semanalmente que o scheduler principal continua sem jobs pausados/orfãos.
- Consolidar 02h30 e Mesa COO se continuarem duplicando decisões.
- Recriar qualquer job removido ou ausente somente com rotina `.md`, owner, fonte, delivery, kill criteria e approval packet novo.
- Manter este arquivo atualizado sempre que `cronjob(action='create/update/pause/remove')` for usado.
