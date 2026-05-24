# Auditoria — Memória, Cron, Inteligência e Proatividade — 2026-05-22

Data/hora: 2026-05-22 13:22 UTC  
Escopo: Hermes Agent produção, Hermes Brain/Cérebro Cimino, crons, loops de inteligência, watchdogs e superfícies proativas.  
Modo: read-only/runtime observability + uma correção documental A1 em `TOOLS.md`.  
Não alterado: Docker, VPS, Traefik, containers, gateway principal, secrets, Shopify, GMC, Tiny, Meta, Klaviyo, WhatsApp/e-mail externo, bancos, campanhas ou budgets.

## Veredito executivo

O sistema está **saudável no runtime**, mas ainda está **complexo demais na camada de governança**.

Não encontrei P0 crítico ativo: Brain Health passou, scheduler está rodando, jobs recentes estão `ok`, watchdogs principais estão silent-OK, 02h/23h existem e estão bem posicionados.

O principal risco agora não é “Hermes quebrado”; é **proatividade espalhada**: muitos crons/relatórios/watchdogs gerando decisões e artefatos em paralelo. Isso aumenta chance de ruído, duplicidade, memória saturada e decisões ficarem sem dono.

## Evidência coletada

### Runtime Hermes

- Versão local: `Hermes Agent v0.14.0 (2026.5.16)`.
- Config ativo: `/opt/data/config.yaml`.
- `hermes cron status`: gateway/scheduler rodando.
- Gateways reais observados por `HERMES_HOME`:
  - `/opt/data` — principal.
  - `/opt/data/profiles/mordomo`.
  - `/opt/data/profiles/lk-growth`.
  - `/opt/data/profiles/spiti`.
- Observação: o comando de status listou também o processo shell transitório da própria auditoria; a leitura por `/proc/*/environ` confirmou os quatro profiles esperados como runtime real.

### Brain / Memória

- `python3 scripts/brain_health_check.py`: `FAIL=0 / WARN=0`.
- `python3 /opt/data/scripts/brain_operating_layer_audit.py`: silent OK.
- Camadas observadas:
  - Memória quente: `memories/hot.md`.
  - Daily note: `memories/daily/2026-05-22.md`.
  - Decisões permanentes: `empresa/decisoes/decisoes-permanentes.md`.
  - Lições: `empresa/gestao/licoes.md`.
  - Inventário runtime: `areas/operacoes/inventarios/crons-agentes-profiles.md`.
  - Decision Inbox: `areas/operacoes/decision-inbox/decision-inbox-20260522.md`.
- Volume mapeado:
  - `memories/*.md`: 13 arquivos.
  - decisões/gestão/decision inbox: 38 arquivos `.md` relevantes.
  - agent docs: 26 arquivos.
  - rotinas: 312 arquivos.
  - skills locais Brain: 10 `SKILL.md`.
  - governance reports: 17 arquivos.

### Cron / Scheduler

Fonte: `cronjob list` e `/opt/data/cron/jobs.json`.

- Total atual: **27 jobs**.
- Ativos: **22**.
- Pausados: **5**.
- Delivery:
  - `local`: 17.
  - `origin`: 10.
- `last_status` não-ok na listagem viva: nenhum observado.
- `last_delivery_error`: nenhum observado.

Jobs estruturais saudáveis:

- `f5a23dd6a1bd` — Lucas Brain daily intelligence loop.
  - Schedule: `0 5 * * *` UTC = 02h BRT.
  - `deliver: local`.
  - `workdir: /opt/data/hermes_bruno_ingest/hermes-brain`.
  - `context_from`: `3fc45b0830c6`, `edd06fe19397`, `4bb4e2223fd3`.
  - Último run: `ok` em 2026-05-22.
- `3fc45b0830c6` — Fechamento Ágil 23h + Brain Sync.
  - `deliver: local`.
  - Último run: `ok` em 2026-05-22.
- `edd06fe19397` — runtime + cron watchdog.
  - `no_agent`, silent-OK, último run `ok`.
- `4bb4e2223fd3` — compression self-heal watchdog.
  - `no_agent`, silent-OK, último run `ok`.
- `d03fa04e1188` — Brain Operating Layer structural watchdog.
  - Ativo e último run `ok`; aplicou auto-heal documental local quando criou daily note.
- `2404c0766d33` — Runtime Truth Reconciler.
  - Ativo e último run `ok`.

Jobs pausados atuais:

- `c214051f7780` — LK weekly influencer sales email.
- `15777e3416dc` — LK SEO/CRO weekly Claude SEO improvement loop.
- `4ced266825f0` — Mordomo WhatsApp pessoal resumo 17h BRT.
- `051f05ce17c1` — Mordomo WhatsApp pessoal realtime scan.
- `a7e883edd200` — LK SEO/CRO impact review — SEO title/meta P1 packets.

## Auditoria por camada

## 1) Memória

### O que está bom

- O Brain já tem a arquitetura certa: `hot`, daily notes, decisões, lições, MAPA, AGENTS, rotinas, reports e health checks.
- A regra “Cérebro Cimino = Hermes Brain” já foi documentada e incorporada nos pontos principais.
- O 23h e o 02h já forçam a ideia correta: chat não é fonte de verdade; Brain é.
- O health check não encontrou falhas atuais.

### Problemas / riscos

1. **Memória persistente Hermes quase cheia.**  
   O perfil/memória injetados no runtime estão perto do limite. Isso aumenta risco de novas preferências importantes não entrarem ou de memórias ficarem longas e conflitantes.

2. **Brain tem material histórico misturado com regra operacional.**  
   O scan encontrou muitos termos históricos (`/root/*`, OpenClaw, `cerebro-cimino`). Parte é referência legítima, mas parte ainda aparece em docs de orientação. Corrigi um caso claro em `TOOLS.md`: a linha que sugeria SSH key `/root/.ssh/id_rsa` agora foi substituída por orientação de verificar credenciais atuais e usar o Brain canônico em `/opt/data/hermes_bruno_ingest/hermes-brain`.

3. **`empresa/gestao/licoes.md` e decisões antigas ainda carregam regras de abril que conflitam com o runtime atual.**  
   Exemplo: padrões antigos de `/root/.hermes/scripts/`, Mem0/write-through e `/tmp` como cópia ativa. Elas precisam virar seção “histórico/legado” ou serem migradas para uma página de lições superseded.

4. **Volume de rotinas alto demais para humano operar sem classificação.**  
   312 rotinas é bom para memória, ruim para priorização. Falta uma view viva por status: `active`, `paused`, `historical`, `needs_review`, `approval_needed`.

### Melhorias recomendadas

- **P0 local/documental:** criar um `memory-ledger` único com status: quente, permanente, superseded, histórico.
- **P0 local/documental:** separar `lições antigas` de `regras operacionais atuais`; tudo que fala `/root`, Mem0 legado, sshpass ou OpenClaw runtime deve ter banner `LEGACY / DO NOT EXECUTE` ou ser movido para histórico.
- **P1 com aprovação:** podar a memória persistente Hermes injetada no prompt. Recomendo reduzir 20–30% removendo fatos operacionais que mudam rápido e empurrando detalhes para Brain/skills.
- **P1 local:** adicionar um scanner ativo que ignore arquivos históricos, mas falhe se docs operacionais (`START*`, `TOOLS`, `AGENTS`, `skills`, `rotinas`) apresentarem `/root/*`, `sshpass`, Mem0 write-through ou comandos perigosos como instrução viva.

## 2) Cron

### O que está bom

- A estrutura central está correta:
  - 23h consolida e sincroniza.
  - 02h pensa, reconcilia e melhora.
  - watchdogs críticos são `no_agent` e silent-OK.
- O 02h está no formato certo: `deliver: local`, `workdir` Brain, `context_from` dos jobs certos.
- Jobs recentes principais estão `ok`.
- Não há erro de delivery vivo na lista atual.

### Problemas / riscos

1. **Ainda há crons pausados que viraram dívida operacional.**  
   Cinco pausados é aceitável, mas eles precisam de destino: reativar, remover, arquivar ou transformar em rotina manual.

2. **Há sobreposição entre inteligência diária e relatório executivo.**  
   Hoje existem pelo menos três superfícies de síntese:
   - 02h Daily Intelligence Loop (`local`).
   - 02h30 Relatório Hermes diário 23h + 02h (`origin`).
   - 08h30 Mesa COO diária Telegram (`origin`).
   Isso pode ser útil, mas hoje parece mais acúmulo do que design intencional.

3. **Cron output mantém histórico de jobs removidos/desconhecidos.**  
   Não é erro, mas confunde auditorias: diretórios de output de one-shots antigos aparecem como `unknown` porque os jobs já saíram da registry.

4. **Alguns scripts `no_agent` fazem auto-heal/restart local.**  
   Exemplo: watchdogs de gateway especialista e LK WhatsApp responder. Isso está dentro do padrão aprovado quando limitado a profiles/processos locais, mas precisa ficar explicitamente classificado como “auto-heal local”, não “read-only”.

### Melhorias recomendadas

- **P0:** criar uma página `cron-control-plane.md` com todos os 27 jobs, status, dono, risco, delivery, kill criteria e destino do output.
- **P0:** decidir o destino dos 5 pausados. Minha recomendação inicial:
  - remover/arquivar one-shot SEO impact se não será executado;
  - manter pausados Mordomo WhatsApp até política nova;
  - revisar se LK influencer e SEO/CRO weekly devem virar on-demand ou voltar com escopo novo.
- **P1:** consolidar os três resumos executivos. Recomendação: manter 02h local, manter Mesa COO Telegram se for útil para decisão diária, e transformar 02h30 em exceção/weekly ou eliminar se estiver redundante.
- **P1:** separar outputs históricos de jobs removidos em uma pasta/index `cron-output-archive`, sem apagar evidência.
- **P1:** rotular scripts de auto-heal local com `risk_class=A1/A2-local` e `side_effects=process_restart_local` no inventário.

## 3) Inteligência

### O que está bom

- O 02h já opera como meta-supervisor e não como robô produtivo solto.
- O 23h já funciona como fechamento/consolidação.
- O Runtime Truth Reconciler adicionou uma camada importante de runtime truth.
- O sistema já usa `context_from`, Brain reports, session_search e watchdogs como fontes.
- O runtime está em v0.14.0; release atual confirmada por busca pública e runtime local.

### Problemas / riscos

1. **Inteligência está distribuída em jobs demais.**  
   O 02h, 23h, Runtime Truth Reconciler, Operating Layer Watchdog, Mesa COO e relatório diário se sobrepõem parcialmente.

2. **Falta um “mapa de inteligência” único.**  
   Hoje existe inventário de cron e reports, mas falta uma visão que diga: “qual loop decide o quê”.

3. **A inteligência ainda depende muito de relatório em markdown.**  
   Markdown é bom para auditoria, mas ruim para acionar decisões. Falta um `decision queue` estruturado: item, dono, risco, prazo, opção recomendada, ação bloqueada, fonte.

4. **Adaptação de features Hermes v0.14 ainda não está totalmente convertida em hábito.**  
   O sistema já usa `no_agent`, `context_from` e profiles. Ainda pode usar melhor `/goal`, `/subgoal`/handoff, curator/skill hygiene e verifier como rotina explícita.

### Melhorias recomendadas

- **P0:** criar `intelligence-map.md`: loops, cadências, fontes, responsabilidades, outputs, guardrails e anti-duplicidade.
- **P0:** definir que o 02h é o supervisor principal; jobs 11h10/11h20 devem virar sub-checks/feed do 02h ou watchdogs estritamente silenciosos, não relatórios paralelos com recomendações próprias.
- **P1:** transformar Decision Inbox em JSONL/ledger estruturado além do markdown, para permitir dedupe, SLA e “waiting Lucas” limpo.
- **P1:** criar scoring de oportunidade: impacto, urgência, confiança, risco, actionability. O 02h deve rankear 3 itens, não listar tudo.
- **P2:** avaliar Hermes Curator/skills maintenance no perfil Lucas, mas só após backup e com regra para não deletar skills pinned/canônicas sem aprovação.

## 4) Proatividade

### O que está bom

- Watchdogs críticos estão silent-OK.
- O sistema já diferencia entrega obrigatória de watchdog de anomalia.
- Decision Inbox existe e está capturando sinais de Zipper/Mordomo.
- Gateways especialistas estão em profiles separados.
- Guardrails contra external send sem aprovação estão documentados e vivos.

### Problemas / riscos

1. **Proatividade ainda parece mais “muitos detectores” do que “um COO com fila de decisão”.**  
   Há sinais bons, mas eles precisam convergir para poucas decisões acionáveis.

2. **Decision Inbox tem falso positivo ou classificação fraca.**  
   Exemplo observado: item Itaú Private Bank aparece como `price_or_availability_or_conditions`, mas o conteúdo é gravação de live macro. Isso indica que o classificador precisa separar marketing/newsletter de pedido comercial real.

3. **Alguns jobs fazem entrega externa aprovada e imprimem recibo no output local.**  
   Isso é ok, mas precisa ser monitorado como external-delivery contract, não como watchdog comum.

4. **Frequência de 1 minuto em watchdogs locais é forte.**  
   Pode ser justificada para gateway/responder, mas merece métrica de restart count e falso positivo. Sem isso, um loop pode ficar “saudável” mas reiniciando demais.

### Melhorias recomendadas

- **P0:** consolidar proatividade em uma `COO Decision Queue` com no máximo 5 itens/dia para Lucas: decisão, recomendação, risco, fonte e botão mental: aprovar / bloquear / pedir dado.
- **P0:** melhorar classificador do Decision Inbox com categorias separadas: `commercial_reply`, `followup_due`, `newsletter_noise`, `price_availability_blocked`, `customer_complaint`, `supplier_or_internal`, `ignore`.
- **P1:** adicionar contadores de auto-heal/restart nos watchdogs de profiles e responder LK WhatsApp; alertar só se passar de threshold diário.
- **P1:** criar rota “draft-only by default” para Zipper/LK follow-ups, com external send sempre bloqueado até Lucas aprovar payload e destinatário.
- **P2:** criar painel local/Brain de “proatividade útil vs ruído”: quantos alertas viraram decisão, quantos foram falsos positivos, quantos foram auto-resolvidos.

## Correção aplicada nesta auditoria

Corrigi `TOOLS.md` em uma referência operacional desatualizada:

- Antes: sugeria SSH key `/root/.ssh/id_rsa` e repos ligados a `cerebro-cimino` como fonte operacional.
- Depois: orienta verificar credenciais atuais, usar o Brain canônico `/opt/data/hermes_bruno_ingest/hermes-brain` e tratar OpenClaw/cerebro-cimino como referência histórica.

Isso foi A1 local/documental, sem runtime/infra/secrets.

## Plano de melhoria recomendado

### P0 — Fazer agora, baixo risco local

1. Criar `intelligence-map.md` como mapa único dos loops 23h, 02h, 02h30, 08h30, 11h10, 11h20, watchdogs e relatórios obrigatórios.
2. Criar/atualizar `cron-control-plane.md` com os 27 jobs vivos, status, dono, risco, delivery, side effects, kill criteria e output.
3. Marcar lições antigas conflitantes como `LEGACY / SUPERSEDED`, especialmente `/root`, Mem0 write-through, sshpass e OpenClaw runtime.
4. Melhorar o Decision Inbox taxonomy para reduzir falso positivo de newsletter/marketing.
5. Criar um scanner “active docs legacy guard” que falha só em docs operacionais, não em arquivo histórico.

### P1 — Precisa decisão de desenho, mas é seguro se aprovado

1. Podar memória persistente Hermes: reduzir uso e mover detalhe operacional para Brain.
2. Decidir destino dos 5 crons pausados.
3. Consolidar 02h30 + Mesa COO + Decision Inbox para reduzir Telegram redundante.
4. Adicionar métricas de restart/auto-heal por watchdog de profile/responder.
5. Transformar Decision Inbox em ledger estruturado com dedupe/SLA.

### P2 — Mais impacto, mais cuidado

1. Ativar/avaliar Hermes Curator para skills com backup e exclusões de skills canônicas.
2. Painel local de proatividade e utilidade dos alertas.
3. Worker/Kanban para resolver itens read-only automaticamente, mantendo external sends e source-of-truth writes bloqueados.

## Minha recomendação de arquitetura

Não criar mais crons agora.

A melhor melhoria é **consolidar**:

- 23h = coleta/consolidação/Brain Sync.
- 02h = inteligência/meta-supervisor e ranking de prioridades.
- Mesa COO = única entrega executiva diária no Telegram, curta e acionável.
- Watchdogs = silent-OK, local, exceção apenas.
- Decision Queue = fila viva de decisões para Lucas, deduplicada e com SLA.

O sistema já tem capacidade. Agora precisa de menos superfícies e mais hierarquia.

## Próximos passos sugeridos

Se Lucas aprovar “P0 local”, executar:

1. Escrever `areas/operacoes/intelligence-map.md`.
2. Escrever `areas/operacoes/rotinas/cron-control-plane.md`.
3. Patch em `empresa/gestao/licoes.md` marcando blocos superseded.
4. Patch no Decision Inbox taxonomy/documentação.
5. Adicionar script local de legacy guard para docs operacionais.
6. Rodar `brain_health_check.py`, `brain_sync_safe.py --dry-run`, `git diff --check` e secret scan final.

Não inclui: cron update, remoção de job, gateway restart, Docker/VPS, external send, write em Shopify/GMC/Tiny/Klaviyo/Meta/WhatsApp/e-mail/banco.
