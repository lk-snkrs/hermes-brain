# Cron Control Plane — Hermes Brain

Atualizado em: 2026-05-22 14:22 UTC

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

## Resumo do snapshot

- Total: 23 jobs.
- Ativos/scheduled: 23.
- Pausados: 0.
- Removidos em 2026-05-22 após aprovação de Lucas: 5 jobs pausados/orfãos.
- Criado em 2026-05-22 P2: `d9badcd83411` strict-runtime guard watchdog silent-OK.
- Redução de ruído P2: `98478b820720` movido de `origin` para `local`; Mesa COO fica como fila executiva principal no Telegram.
- Sem `last_delivery_error` observado.
- Sem `last_status` não-ok observado entre jobs já executados.

## Jobs ativos — controle

### Brain / governança central

- `f5a23dd6a1bd` — Lucas Brain daily intelligence loop
  - Schedule: `0 5 * * *` UTC / 02h BRT.
  - Delivery: `local`.
  - Owner: Operações / Hermes Brain.
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
  - Delivery: `local` desde P2 2026-05-22.
  - Owner: Operações / Hermes Brain.
  - Função: resumo executivo local do 23h + 02h; insumo para Mesa COO, não interrupção no Telegram.
  - Side effects: documentação/local scheduler output; sem Telegram em sucesso normal.
  - Kill criteria: duplicar Mesa COO; enviar sucesso técnico; mais de 5 itens sem decisão clara.
  - Rollback se Lucas quiser voltar o Telegram 02h30: `cronjob update 98478b820720 deliver=origin`.

- `749ee30b51eb` — Mesa COO diária Telegram
  - Schedule: `30 11 * * *` UTC / 08h30 BRT.
  - Delivery: `origin`.
  - Owner: Operações / COO.
  - Função: fila executiva diária.
  - Side effects: Telegram.
  - Kill criteria: virar relatório longo; repetir 02h30; incluir item sem ação/fonte.

- `f4c499e85eac` — Lucas Brain weekly Learning Loop report
  - Schedule: `15 12 * * 1` UTC / segunda 09h15 BRT.
  - Delivery: `origin`.
  - Owner: Operações / melhoria contínua.
  - Função: revisão semanal de aprendizados.
  - Side effects: Telegram.
  - Kill criteria: não gerar mudanças de skill/memória/rotina; repetir daily loop.

- `d03fa04e1188` — Hermes Brain Operating Layer structural watchdog
  - Schedule: `10 11 * * *` UTC.
  - Delivery: `local`.
  - Owner: Operações.
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
  - Owner: Operações.
  - Função: reconciliar docs vs runtime.
  - Side effects: local/silent.
  - Kill criteria: afirmar runtime sem evidência; duplicar inventário sem registrar diferença.

- `c358f8f56a26` — Pixel AI Hub / Brainzinho daily learning scan
  - Schedule: `30 23 * * *` UTC / fim do dia.
  - Delivery: `origin` apenas quando houver aprendizado relevante; no-op deve ser silent-OK quando tecnicamente possível.
  - Owner corrigido em 2026-05-25: Hermes Agent / Operações Hermes, não Mordomo.
  - Estado observado: ainda localizado no scheduler/profile Mordomo como executor técnico histórico; migração real para Hermes Agent exige alteração controlada de cron, backup antes/depois e prompt sem identidade Mordomo.
  - Rotina/PRD: `areas/operacoes/prds/pixel-ai-hub-learning-loop-hermes-agent-2026-05-25.md`.
  - Kill criteria: virar spam diário, copiar material bruto, tratar comunidade como lead/CRM, ou rodar com prompt/owner Mordomo depois da migração aprovada.

### Watchdogs técnicos

- `edd06fe19397` — Hermes runtime + cron watchdog no_agent
  - Schedule: `*/30 * * * *`.
  - Delivery: `local`.
  - Kill criteria: prints em OK normal; restart sem receipt.

- `4bb4e2223fd3` — Hermes compression failure self-heal watchdog
  - Schedule: `*/10 * * * *`.
  - Delivery: `local`.
  - Kill criteria: auto-heal fora do escopo seguro; spam.

- `71b2636add5d` — LK WhatsApp Hermes responder watchdog
  - Schedule: `every 1m`.
  - Delivery: `local`.
  - Kill criteria: qualquer envio fora dos guardrails LK; prints em OK.

- `a5d7a392eed9` — LK WhatsApp Hermes responder regression watchdog
  - Schedule: `*/30 * * * *`.
  - Delivery: `local`.
  - Kill criteria: teste não cobre gramática real; falso positivo/negativo recorrente.

- `ac0b440e2643` — Mordomo Telegram gateway watchdog
  - Schedule: `every 1m`.
  - Delivery: `local`.
  - Kill criteria: mexer no gateway sem aprovação fora de restart seguro documentado; spam.

- `876d54c62ccd` — LK Growth Telegram gateway watchdog
  - Schedule: `every 1m`.
  - Delivery: `local`.
  - Kill criteria: spam; reinício em loop.

- `663e3e6a148c` — SPITI Telegram gateway watchdog
  - Schedule: `every 1m`.
  - Delivery: `local`.
  - Kill criteria: spam; reinício em loop.

### LK / negócio

Nota de ownership: nesta seção, diferenciar `LK Growth` de `LK Comercial/Ops`. SEO, CRO, GEO, GMC, analytics, conteúdo e impact reviews pertencem ao especialista LK Growth. Vendas, pulso comercial, fechamento de loja e reports comerciais obrigatórios permanecem no Main/COO enquanto não existir um profile operacional LK próprio. Não migrar automaticamente relatórios comerciais para LK Growth só por conterem “LK”.

- `7c688553e293` — LK Daily Sales Brief read-only mandatory delivery
  - Schedule: `0 11 * * *` UTC / 08h BRT.
  - Delivery: `origin`.
  - Função: briefing diário aprovado.
  - Kill criteria: fonte indisponível sem sinalizar; dados sem verificação; misturar Tiny/Shopify indevidamente.

- `953b9055458e` — LK Weekly CEO Review read-only mandatory delivery
  - Schedule: `0 12 * * 1` UTC / segunda 09h BRT.
  - Delivery: `origin`.
  - Kill criteria: repetir daily sem insight semanal; enviar sem fonte.

- `d4c26da4cd48` — LK GMC Review read-only mandatory delivery
  - Schedule: `0 12 * * 4` UTC / quinta 09h BRT.
  - Delivery: `origin`.
  - Kill criteria: sugerir write GMC sem approval packet; não diferenciar read-only vs ação externa.

- `c3bb587519d2` — LK Pulso Comercial 16h read-only delivery
  - Schedule: `0 19 * * *` UTC / 16h BRT.
  - Delivery: `local`.
  - Kill criteria: envio Telegram de sucesso; duplicar Daily Sales Brief.

- `e3279babbc4a` — LK 09h previous-day sales report external delivery
  - Schedule: `0 12 * * *` UTC / 09h BRT.
  - Delivery: `local`.
  - Kill criteria: envio externo fora do script/escopo aprovado; fonte ausente.

- `a2ead305eab2` — LK 19h30 physical store close external delivery
  - Schedule: `30 22 * * *` UTC / 19h30 BRT.
  - Delivery: `local`.
  - Kill criteria: envio externo fora do script/escopo aprovado; fonte ausente.

### Zipper / negócio

- `357d40a5863e` — Zipper OS vendas 09h WhatsApp/email
  - Schedule: `0 12 * * 1-5` UTC / dias úteis 09h BRT.
  - Delivery: `local`.
  - Kill criteria: contato externo fora dos destinatários aprovados; dados não vindos de `vendas_tango`; misturar SPITI.

- `71b147362ec1` — Zipper Gmail style learning refresh
  - Schedule: `20 6 * * *` UTC.
  - Delivery: `local`.
  - Kill criteria: criar draft/responder e-mail; usar e-mail enviado como autorização.

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
- Recriar qualquer job removido somente com rotina `.md`, owner, fonte, delivery, kill criteria e approval packet novo.
- Manter este arquivo atualizado sempre que `cronjob(action='create/update/pause/remove')` for usado.
