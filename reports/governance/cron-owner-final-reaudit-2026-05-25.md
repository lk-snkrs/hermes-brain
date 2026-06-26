# Reauditoria final — matriz crons x organograma Hermes

Data: 2026-05-25 11:35 UTC
Escopo: leitura dos registros locais de cron por profile + conferência documental do organograma/Task Router. Sem writes externos.

## Resultado executivo
- A migração anterior ficou consistente: não há duplicidade de IDs entre Main, LK Growth e Mordomo.
- Nenhum job adicional é inequívoco o bastante para migração automática sem decisão de governança.
- Main ainda concentra alguns watchdogs de profiles especialistas; isso é aceitável como supervisão central do COO, desde que sejam silent-OK/local.
- LK Growth está bem separado para SEO/CRO/GEO/GMC; ainda há alto volume de entregas `origin` de reviews D+7, que é a principal fonte potencial de ruído.
- Mordomo concentra pessoal/WhatsApp/Zipper documental; Zipper ainda é candidato natural a profile próprio, mas não obrigatório agora.
- SPITI segue sem `cron/jobs.json`; status correto por enquanto: profile vivo/observado, sem crons locais registrados.
- Alterações nesta rodada: apenas relatório local + handoff; nenhum cron/runtime alterado.

## Matriz por profile

### main
- Total: 20
- Ativos: 20
- Pausados: 0
- Com script: 13
- Entrega: local=19, origin=1
- Lista:
  - Hermes Brain Fechamento Ágil 23h + Brain Sync — status=active; deliver=local
  - Hermes Brain Operating Layer structural watchdog — status=active; deliver=local
  - Hermes Brain Runtime Truth Reconciler — status=active; deliver=local
  - Hermes Brain strict-runtime guard watchdog — status=active; deliver=local
  - Hermes compression failure self-heal watchdog — status=active; deliver=local
  - Hermes runtime + cron watchdog no_agent — status=active; deliver=local
  - LK 09h previous-day sales report external delivery — status=active; deliver=local
  - LK 19h30 physical store close external delivery — status=active; deliver=local
  - LK Daily Sales Brief read-only mandatory delivery — status=active; deliver=local
  - LK Growth Telegram gateway watchdog — status=active; deliver=local
  - LK Pulso Comercial 16h read-only delivery — status=active; deliver=local
  - LK Weekly CEO Review read-only mandatory delivery — status=active; deliver=local
  - Lucas Brain daily intelligence loop — status=active; deliver=local
  - Lucas Brain weekly Learning Loop report — status=active; deliver=local
  - Mesa COO diária Telegram — status=active; deliver=origin
  - Mordomo Telegram gateway watchdog — status=active; deliver=local
  - Relatório Hermes diário 23h + 02h para Lucas — status=active; deliver=local
  - SPITI Telegram gateway watchdog — status=active; deliver=local
  - Zipper Gmail style learning refresh — status=active; deliver=local
  - Zipper OS vendas 09h WhatsApp/email — status=active; deliver=local

### lk-growth
- Total: 23
- Ativos: 23
- Pausados: 0
- Com script: 1
- Entrega: local=1, origin=19, telegram=3
- Lista:
  - LK Auth Hub D+7 impact review — status=active; deliver=origin
  - LK blog boutique premium D+7 impact review — status=active; deliver=origin
  - LK cart intent Crisp REST identity review D+7 — status=active; deliver=origin
  - LK collection GEO FAQ production D+7 impact review — status=active; deliver=origin
  - LK CRO dev preview impact review — Onitsuka/NB/Kill Bill — status=active; deliver=origin
  - LK D+7 impact review — Adidas SL 72 OG vs RS GEO page table — status=active; deliver=origin
  - LK D+7 impact review — Packet D GEO Source Pages — status=active; deliver=origin
  - LK D+7 review — botão Compre Já branco PDP — status=active; deliver=origin
  - LK D+7 review — PDP CRO production promotion 2026-05-19 — status=active; deliver=origin
  - LK GEO llms.txt root D+7 impact review — status=active; deliver=origin
  - LK GEO Source Pages D+7 Impact Review — status=active; deliver=origin
  - LK GMC Review read-only mandatory delivery — status=active; deliver=local
  - LK Growth OS GMC Review read-only — status=active; deliver=telegram
  - LK Growth OS SEO/CRO impact review — SEO title/meta P1 packets — status=active; deliver=telegram
  - LK Growth OS Weekly Growth Review — status=active; deliver=telegram
  - LK Menu Drawer Production D+7 Review — status=active; deliver=origin
  - LK n8n checkout abandonado hardening impact review — status=active; deliver=origin
  - LK NB blog rewrite D+7 impact review — status=active; deliver=origin
  - LK PDP CRO hotfix D+7 review — trustbar/reviews/tryon — status=active; deliver=origin
  - LK PDP preorder compact hotfix D+7 review — status=active; deliver=origin
  - LK Recovery OS checkout_started webhook D+7 impact review — status=active; deliver=origin
  - LK Recovery OS T1 go-live D+7 impact review — status=active; deliver=origin
  - LK SEO/GEO Experiment Ledger — weekly impact review — status=active; deliver=origin

### mordomo
- Total: 13
- Ativos: 13
- Pausados: 0
- Com script: 10
- Entrega: local=5, origin=8
- Lista:
  - Follow-up Leticia Albuquerque — importação/Portugal — status=active; deliver=origin
  - LK WhatsApp Hermes responder regression watchdog — status=active; deliver=local
  - LK WhatsApp Hermes responder watchdog — status=active; deliver=local
  - Mordomo CRM local sync — status=active; deliver=local
  - Mordomo Decision Inbox digest — status=active; deliver=origin
  - Mordomo global Calendar watcher — status=active; deliver=origin
  - Mordomo global WhatsApp watcher — Lucas pessoal — status=active; deliver=origin
  - Mordomo WhatsApp pessoal resumo 17h BRT — status=active; deliver=origin
  - Pixel AI Hub / Brainzinho daily learning scan — status=active; deliver=origin
  - Zipper artist PDFs local-only known-answer ingest — status=active; deliver=local
  - Zipper direct main e-mail monitor — zipper@zippergaleria.com.br — status=active; deliver=origin
  - Zipper Gmail draft engine — safe draft-only — status=active; deliver=local
  - ZPR Enquiry Form watcher — approval-gated — status=active; deliver=origin

### spiti
- Registro: ausente

## Duplicidades
- Nenhuma duplicidade de ID encontrada entre Main, LK Growth e Mordomo.

## Classificação por domínio operacional

### Central runtime / COO — manter no Main
- Mesa COO, Brain, runtime, compression self-heal e strict-runtime guard.
- Watchdogs de gateways especialistas no Main são aceitáveis quando funcionam como supervisão central, `deliver=local` e silent-OK.

### LK Growth — já separado
- SEO/CRO/GEO/GMC e reviews D+7 estão majoritariamente no profile `lk-growth`.
- Ponto de atenção: 19 reviews D+7 ainda usam `origin`; isso é mais problema de ruído/consolidação do que de ownership.

### LK Comercial/Ops — decisão futura
- Daily Sales Brief, Weekly CEO Review, Pulso 16h, relatório 09h e fechamento 19h30 continuam no Main.
- Isso é aceitável enquanto Hermes Geral/COO centraliza operação comercial; só migrar se for criado um profile operacional LK separado.

### Mordomo / WhatsApp / pessoal
- Watchdogs WhatsApp migrados estão no `mordomo`, como esperado.
- Fluxos pessoais, calendário, digest e follow-up permanecem no `mordomo`.

### Zipper
- Hoje fica dividido entre Main e Mordomo, com comportamento documental/read-only e approval-gated.
- Não é erro crítico; é candidato a profile próprio se volume/risco/autonomia aumentarem.

### SPITI
- Possui watchdog central no Main, mas não possui registry local de crons.
- Status correto: sem crons locais até decisão explícita de criar registry/profile scheduler.

## Lacunas reais / decisões pendentes
1. **LK Growth com muitos `origin`**: 19 reviews D+7 ainda entregam no Telegram/origin. Recomendo consolidar em digest/ledger antes de criar ou mover mais crons.
2. **Zipper**: continua aceitável dentro do Mordomo como documental/read-only. Criar profile próprio só quando houver volume/risco/autonomia suficiente.
3. **SPITI**: ausência de registry deve virar decisão explícita: manter “sem crons locais” documentado ou criar skeleton vazio para auditoria.
4. **Main como COO**: manter watchdogs de gateways especialistas no Main é coerente enquanto eles supervisionam saúde geral e ficam `local`/silent-OK.
5. **LK Comercial/Ops no Main**: relatórios de vendas/fechamento são operação comercial, não necessariamente Growth; antes de migrar, decidir se LK terá profile operacional separado ou se continuam sob COO.

## Próximo bloco seguro recomendado
- Criar uma rotina documental semanal de reauditoria crons x donos em `areas/operacoes/rotinas/`, sem criar cron automático.
- Atualizar índice de rotinas para que futuros agentes saibam quando reexecutar a auditoria.
- Preparar, se Lucas aprovar depois, um pacote de decisão 1/N para: consolidar reviews LK Growth, criar profile Zipper, ou criar skeleton registry SPITI.

## Não realizado
- Não criei, removi, pausei ou editei cron.
- Não reiniciei gateway, Docker, VPS, containers, Traefik ou integrações externas.
- Não enviei mensagem externa nem acionei produção.
