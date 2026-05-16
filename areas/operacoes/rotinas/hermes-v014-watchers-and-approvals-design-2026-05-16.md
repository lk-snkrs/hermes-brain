# Hermes v0.14 — Watchers padronizados e aprovações estruturadas

Data: 2026-05-16 08:56 BRT  
Atualizado: 2026-05-16 09:08 BRT  
Contexto: Lucas aprovou executar itens 2 e 3 do relatório `Lucas Brain Daily Intelligence Loop` de 2026-05-16 e depois aprovou implementar o pacote todo.  
Modo: design/Brain/skill + crons `no_agent` locais; nenhum envio externo, endpoint exposto, Docker/gateway/host, banco produtivo ou secret alterado.

## Item 2 — Watchers v0.14 padronizados

Objetivo: transformar monitoramento em sinais úteis, silenciosos quando OK, sem cron sprawl.

### Inventário atual de watchers / no_agent

Watchdogs em `/opt/data/scripts/`:

- `hermes_runtime_cron_watchdog.py` — runtime Hermes + cron health; roda a cada 30 min; OK = stdout vazio.
- `hermes_artifacts_freshness_watchdog.py` — frescor dos artefatos operacionais Hermes; roda diariamente 09h BRT; OK = stdout vazio.
- `lk_daily_sales_brief_watchdog.py` — entrega obrigatória do daily sales brief LK; roda 08h BRT.
- `lk_weekly_ceo_review_watchdog.py` — entrega semanal CEO Review LK; roda segunda 09h BRT.
- `lk_gmc_review_watchdog.py` — revisão GMC LK; roda quinta 09h BRT.
- `mordomo_whatsapp_scan.sh` — scan realtime Mordomo pessoal; roda a cada 15 min.
- `mordomo_whatsapp_summary_09.sh` e `mordomo_whatsapp_summary_17.sh` — resumos diários Mordomo.

Crons agent-driven relevantes:

- `Lucas Brain daily intelligence loop` — cérebro diário 02h BRT.
- `Zipper Gmail auto-draft reply-all` — draft-only, local, a cada 15 min.
- `Zipper Gmail style learning refresh` — aprendizado de estilo diário.

### Contrato padrão

- `rc=0` + stdout vazio = saudável e silencioso.
- `rc=0` + stdout não vazio = alerta acionável para Lucas.
- `rc!=0` = falha do watchdog, alertar com erro sanitizado.
- Watcher nunca imprime secrets, tokens, headers OAuth, connection strings ou payload bruto sensível.
- Watcher nunca faz mutação externa/produtiva; só observa e/ou escreve artefato local sanitizado.
- Alerta deve indicar: contexto, impacto provável, ação segura recomendada, e se precisa de aprovação.

### Matriz de padronização

1. **Hermes runtime/release**
   - Atual: runtime watchdog + Lucas Brain daily loop.
   - Melhorar: separar `release drift` de `runtime health` para evitar falso positivo quando update já foi aprovado.

2. **Zipper OS**
   - Atual: Gmail draft-only + style learning + cockpit diário `no_agent`.
   - Implementado após aprovação Lucas: `/opt/data/scripts/zipper_os_cockpit.py`, wrappers `zipper_os_cockpit_daily.sh` e `zipper_os_cockpit_watchdog.sh`.
   - Crons: `f00c68f5967a` (`Zipper OS daily executive cockpit`, 08:15 BRT, entrega resumo e grava `.md/.json`) e `af07bbc077b8` (`Zipper OS inbox/followups watchdog silent`, a cada 30 min, Silent OK).
   - Watchdog alerta sem PII se IMAP de rascunhos cair, backlog Gmail superar limite, houver follow-up vencido ou urgência de secretaria exceder limiar.
   - Regra: nunca envia e-mail/WhatsApp nem grava Supabase; só lê Gmail/Supabase e escreve artefato local sanitizado.

3. **LK mandatory reports**
   - Atual: daily sales, weekly CEO, GMC.
   - Melhorar: padrão único de mensagem e dedupe de alertas.

4. **Mordomo**
   - Atual: realtime scan + resumos.
   - Implementado na varredura realtime: `mordomo_whatsapp_scan.sh` agora declara o contrato v0.14, força `WACLI_READONLY=1` e usa timeout de 120s; validação manual e via cron `051f05ce17c1` retornou `last_status=ok` e stdout vazio quando saudável.
   - Melhorar: distinguir “informativo” vs “precisa Lucas” para reduzir ruído.

5. **GitHub/Hermes releases**
   - Atual: dentro do daily loop.
   - Próximo watcher possível: release watcher silencioso que alerta apenas quando existir release posterior à produção.
   - Não deve fazer update automático.

### Próxima implementação recomendada

Zipper OS agora está em produção local/read-only com cockpit diário e watchdog silencioso. Próxima melhoria recomendada: reduzir ruído do Mordomo distinguindo “informativo” vs “precisa Lucas” e, depois, consolidar um `watcher_contract.md` para padronizar mensagens/dedupe nos watchers LK/Mordomo/Hermes.

## Item 3 — Clarify buttons / aprovações estruturadas

Objetivo: aprovações A2/A3/A4 mais rápidas e menos ambíguas no Telegram.

### Padrão de decisão

Quando houver decisão de risco médio/alto, Hermes deve perguntar com opções curtas, mas a mensagem precisa conter antes:

- contexto;
- ação exata;
- payload/escopo;
- risco;
- rollback ou reversibilidade;
- o que NÃO será feito.

### Botões recomendados

Até 4 opções:

1. **Aprovar escopo** — executa exatamente o payload descrito.
2. **Ajustar** — Lucas pede alteração antes de executar.
3. **Somente preview** — gera artefato/rascunho, sem ação produtiva.
4. **Bloquear** — não executa.

Para casos técnicos:

1. **Aprovar com rollback**
2. **Aprovar só read-only**
3. **Pedir plano maior**
4. **Bloquear**

### Regra crítica

Botão/“aprovar” só vale para o escopo mostrado inline. Não autoriza expansão silenciosa para Docker, host, secrets, envio externo, dinheiro, banco, Shopify, Meta/Google/Klaviyo ou ação destrutiva.

### Aplicação imediata

A partir desta data, decisões de Hermes runtime, Zipper drafts/follow-ups, Mordomo externo, LK writes e novos crons produtivos devem usar esse padrão quando o canal suportar `clarify`/botões. Se botões não aparecerem, usar o mesmo formato em texto.
