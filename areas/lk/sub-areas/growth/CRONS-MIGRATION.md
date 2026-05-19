# LK Growth OS — Cron migration map

Última revisão: 2026-05-19.

## Princípio

O LK Growth OS deve receber apenas rotinas de Growth/Search/Analytics/CRO/GMC/GEO. Rotinas de operação financeira, loja física, WhatsApp, Mordomo, Zipper, runtime Hermes e Chief of Staff continuam fora deste agente.

Migração deve ser preview-first:

1. documentar candidato;
2. criar job equivalente no perfil `lk-growth`;
3. validar entrega no bot/canal correto;
4. pausar job antigo só depois de uma execução válida;
5. manter rollback: reativar job antigo se o novo falhar.

## Pré-requisito operacional

Antes de migrar entregas para o bot `@LKGrowth_HermesBot`, Lucas precisa abrir o bot e enviar `/start`; se for usar grupo, adicionar o bot ao grupo `[LK] Growth OS` e enviar `/sethome` pelo perfil `lk-growth`.

Status pós-migração inicial: o perfil `lk-growth` possui 2 jobs ativos próprios em `HERMES_HOME=/opt/data/profiles/lk-growth`.

## Candidatos a migrar para LK Growth OS

### 1. LK SEO/CRO weekly Claude SEO improvement loop

- Job antigo: `15777e3416dc`
- Schedule: `0 13 * * 1` — segunda 10h BRT.
- Status antigo: pausado no Hermes principal após migração.
- Destino antigo: `origin` no Hermes principal.
- Novo job `lk-growth`: `738d3deabaeb` — `LK Growth OS Weekly Growth Review`, deliver `telegram`.
- Motivo para migrar: é exatamente Growth/SEO/CRO decision-grade.
- Recomendação/status: migrado para `lk-growth` como Weekly Growth Review ampliado com checklist de 18 tópicos.
- Skills atuais relevantes: `lk-seo-weekly-improvement`, `lk-operational-intelligence`, `lk-shopify-readonly`, `seo-audit`, `seo-page`, `seo-content`, `seo-ecommerce`, `seo-google`.

### 2. LK GMC Review read-only mandatory delivery

- Job antigo: `d4c26da4cd48`
- Schedule: `0 12 * * 4` — quinta 09h BRT.
- Status antigo: pausado no Hermes principal após migração.
- Destino antigo: `origin` no Hermes principal.
- Novo job `lk-growth`: `1240644c5f3f` — `LK Growth OS GMC Review read-only`, deliver `telegram`.
- Motivo para migrar: rotina dedicada de Merchant Center pertence ao LK Growth OS.
- Recomendação/status: migrado para `lk-growth` mantendo read-only e approval packet para correções.

### 3. LK SEO/CRO impact review — SEO title/meta P1 packets

- Job antigo: `a7e883edd200`
- Schedule: once in 7d, next run original `2026-05-25T14:34:23Z`.
- Status antigo: pausado no Hermes principal após migração.
- Destino antigo: `origin` no Hermes principal.
- Novo job `lk-growth`: `c45cda5fe2df` — `LK Growth OS SEO/CRO impact review — SEO title/meta P1 packets`, deliver `telegram`.
- Prompt novo salvo em `/opt/data/profiles/lk-growth/cron-prompts/seo-impact-review-20260525.md`.
- Motivo para migrar: impact review de mudança SEO/CRO é parte do tópico 18 do escopo canônico.
- Recomendação/status: migrado; próximos impact reviews devem nascer diretamente no `lk-growth`.

### 4. LK weekly influencer sales email

- Job atual: `c214051f7780`
- Schedule: quarta 10h BRT.
- Status: pausado.
- Motivo parcial: influencer/social demand signal pertence ao escopo Growth, mas envio de email externo não deve rodar automático.
- Recomendação: não reativar como email. Se migrar, transformar em relatório read-only de sinal influencer + draft interno, sem envio externo.

## Não migrar para Growth OS

### Operação/financeiro/loja

- `7c688553e293` — LK Daily Sales Brief read-only mandatory delivery.
- `953b9055458e` — LK Weekly CEO Review read-only mandatory delivery.
- `c3bb587519d2` — LK 16h financial pulse external delivery.
- `e3279babbc4a` — LK 09h previous-day sales report external delivery.
- `a2ead305eab2` — LK 19h30 physical store close external delivery.

Motivo: são rotinas operacionais/gestão LK, não Growth especialista.

### WhatsApp / atendimento / Mordomo

- `71b2636add5d` — LK WhatsApp Hermes responder watchdog.
- `b2492892b18f`, `4ced266825f0`, `051f05ce17c1`, `527ee57b3a` — Mordomo/WhatsApp pessoal.

Motivo: canais pessoais/atendimento/WhatsApp não pertencem ao Growth OS.

### Zipper

- `71b147362ec1` — Zipper Gmail style learning refresh.
- `357d40a5863e` — Zipper OS vendas 09h WhatsApp/email.

Motivo: Zipper OS separado.

### Runtime/infra Hermes

- `edd06fe19397` — Hermes runtime + cron watchdog.
- `4bb4e2223fd3` — Hermes compression failure self-heal watchdog.
- `ac0b440e2643` — Mordomo Telegram gateway watchdog.
- `876d54c62ccd` — LK Growth Telegram gateway watchdog.
- `f5a23dd6a1bd` — Lucas Brain daily intelligence loop.

Motivo: infra/Chief of Staff, não Growth.

## Política de entrega após migração

- Rotinas Growth recorrentes devem entregar no bot/canal `LK Growth OS`, não no Hermes principal.
- Silent-OK para watchdogs; relatórios programados podem entregar quando são o produto esperado.
- Nenhum job Growth deve executar write externo sem aprovação explícita atual.
- Se o job cria recomendações, deve usar o checklist `ESCOPO-18-TOPICOS.md` ou declarar itens não aplicáveis.

## Backlog de migração segura

1. Canal/home definitivo do `lk-growth` confirmado por Lucas.
2. Rodar manualmente/validar a primeira entrega do `738d3deabaeb`.
3. Rodar manualmente/validar a primeira entrega do `1240644c5f3f`.
4. Impact review SEO title/meta migrado: novo `c45cda5fe2df`, antigo `a7e883edd200` pausado.
5. Se houver falha de entrega, rollback: reativar `15777e3416dc`, `d4c26da4cd48` ou `a7e883edd200` no Hermes principal, conforme o job afetado.
