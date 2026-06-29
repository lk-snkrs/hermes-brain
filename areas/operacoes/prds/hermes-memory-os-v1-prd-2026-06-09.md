# PRD — Hermes Memory OS v1

Data: 2026-06-09  
Status: Memory OS v1.1–v1.18 executado em escopo local/read-only/silent-OK conforme fases registradas; Mission Control/card visual permanece pendente por decisão de Lucas; provider externo e runtime sensível permanecem bloqueados.  
Owner lógico: LC Hermes / Hermes Agent central.  
Escopo: memória Hermes/Brain, dailies, `hot.md`, boot memories, receipts, skills e rotinas locais.

## 1. Problema

Lucas apontou que a memória está “praticamente abandonada” quando depende só do ciclo noturno. A evidência atual confirma a crítica:

- `reports/memory-hygiene/latest.json` está com `status=action_required`.
- `profiles/lk-stock/memories/MEMORY.md` está over-limit: 2493/2200 chars (113.3%).
- `profiles/lk-content/memories/USER.md` está near saturation: 1321/1375 chars (96.1%).
- Faltam templates de auto-compactação para arquivos existentes de `lk-content` e `lk-stock`.
- `memories/hot.md` ainda dizia “Atualizado: 2026-06-07” e continha estado operacional agora incorreto.
- `memories/daily/2026-06-09.md` existia como skeleton, não como daily curada.

Conclusão: a arquitetura de camadas está correta, mas a operação ainda não é Bruno-grade porque não fecha o loop durante o dia.

## 2. Tese de produto

Hermes Memory OS v1 transforma memória em um loop operacional contínuo:

`evento → classificação → camada correta → compactação preventiva → daily/hot atualizado → receipt → verificação → Telegram só se acionável`

O objetivo não é aumentar memória injetada. O objetivo é manter `MEMORY.md`/`USER.md` como boot mínimo e fazer Brain/daily/hot/reports/skills/session_search funcionarem como memória rica viva.

## 3. Não-objetivos

- Não ativar Mem0, Honcho ou qualquer provider externo.
- Não alterar Docker, VPS, Traefik, gateway, containers ou runtime produtivo nesta fase.
- Não criar ou mudar cron produtivo sem aprovação escopada.
- Não gravar secrets, tokens, paths sensíveis ou payloads de credencial no Brain.
- Não transformar `hot.md` em histórico longo nem daily em dump bruto de conversa.

## 4. Personas / owners

- **Lucas:** recebe apenas decisão, exceção, falha ou resumo explicitamente desejado.
- **LC Hermes central:** owner sistêmico de memória, compactação, políticas e scorecards.
- **Especialistas:** mantêm boot memory mínimo e handoffs/receipts para o Brain central.
- **Watchdogs/rotinas:** executam higiene local/silent-OK e deixam evidência sanitizada.

## 5. Arquitetura v1

### 5.1 Memory Event Router

Classifica todo evento relevante em uma destas saídas objetivas:

- preferência durável do usuário/Lucas → `USER.md` curto;
- guardrail global, regra de segurança ou política de boot → `MEMORY.md` curto;
- prioridade/bloqueio/estado current → `memories/hot.md`;
- decisão/entrega/pendência do dia → `memories/daily/YYYY-MM-DD.md`;
- evidência, relatório, auditoria, receipt ou output material → Brain em `reports/`, `receipts/` ou área dona;
- procedimento reutilizável ou rotina repetível → skill, referência de skill ou rotina canônica;
- contexto de domínio → `areas/<domínio>/` ou `agentes/<especialista>/`;
- dado vivo → fonte real no momento; Brain guarda ponteiro/receipt/report com timestamp/incerteza;
- conversa antiga → `session_search`, promovendo só se virar preferência estável, decisão durável, guardrail ou procedimento.

`USER.md`/`MEMORY.md` não viram memória rica; Brain/receipts/reports/daily/hot/skills carregam o detalhe certo por camada.

### 5.2 Daytime Hygiene Watcher

Executa localmente durante o dia, antes do ciclo noturno, com gatilhos:

- boot memory > 80%: pré-alerta local;
- boot memory > 85% e template seguro existe: compactar com backup;
- over-limit: ação obrigatória antes de alertar;
- template ausente para profile com memória: gerar gap/packet e, quando seguro, criar template mínimo;
- `hot.md` stale: refresh local;
- daily skeleton depois de evento relevante: curar daily;
- receipt operacional novo criado: usar preferencialmente o wrapper `hermes_memory_os_receipt_writer.py` para validar campos, salvar no Brain e chamar hook em uma única operação local.
- handoff, approval packet ou artefato legado/excepcional criado: chamar o hook `hermes_memory_os_event_hook.py <path>` como fallback para classificar evento e atualizar scorecard sem criar cron/runtime novo.

### 5.3 Daily Curator

Mantém a daily como memória corrente do dia, não só fechamento noturno:

- decisões;
- entregas;
- aprendizados;
- handoffs/receipts;
- não-ações;
- pendências current.

### 5.4 Hot Refresher

Mantém `hot.md` pequeno e atual:

- prioridades atuais;
- bloqueios atuais;
- guardrails em vigor;
- links quentes;
- remove claims datados ou já falsos.

### 5.5 Profile Coverage Manager

Todo profile com `memories/MEMORY.md` ou `memories/USER.md` precisa de cobertura automática:

- descoberta por filesystem, não lista manual incompleta;
- template mínimo por profile;
- score de cobertura;
- alertar só quando impossível compactar com segurança.

### 5.6 Memory Scorecard

Score diário e sob demanda:

- over-limit count = 0;
- near saturation count ideal = 0;
- template coverage missing = 0;
- `hot.md` atualizado hoje ou justificado;
- daily do dia curada se houve evento material;
- provider externo off;
- secret scan 0;
- receipts presentes para correções.

## 6. UX Telegram

Contrato:

- sucesso rotineiro = silencioso/local;
- alerta só se existir decisão, falha, risco ou ação humana;
- mensagem deve explicar gatilho, impacto, ação já tomada e próximo passo;
- nunca enviar JSON bruto, wrapper, job id, path interno desnecessário ou logs longos.

## 7. Fases

### Fase 0 — R&D/documental local

- PRD, rotina, plano e receipt.
- Refresh de daily/hot se local e seguro.
- Nenhuma alteração de runtime/cron/provider.

### Fase 1 — Correções locais imediatas

- Criar templates seguros para `lk-stock` e `lk-content`.
- Compactar `lk-stock/MEMORY.md` com backup.
- Compactar `lk-content/USER.md` se ainda near saturation.
- Atualizar `hermes-profile-memory-coverage.md`.
- Rodar py_compile/watchdog/secret scan/Brain checks.

### Fase 2 — Router/checker diurno — executada

- Criado `/opt/data/scripts/hermes_memory_os_daytime_checker.py`.
- Implementado `--dry-run` read-only, modo auto-heal local e JSON report.
- Verificado manualmente: dry-run `ok`, run `ok`, stdout vazio quando verde.

### Fase 3 — Agendamento ou hook — executada com aprovação desta conversa

- Criado cron local/no_agent `Hermes Memory OS daytime checker/router`, `every 2h`, `deliver=local`, script `hermes_memory_os_daytime_checker.py`.
- Sem Telegram em sucesso; stdout só em alerta acionável.
- Sem Docker/VPS/gateway/restart/provider externo.

### Fase 4 — Mission Control futuro — executada como dashboard local documental

- Criado `areas/operacoes/runtime/hermes-memory-os-dashboard.md` como painel local de estado.
- UI Mission Control continua futuro/não implantada; Brain permanece fonte canônica.

### Fase 4.5 / v1.1 — Event-aware scorecard local — executada

- `hermes_memory_os_daytime_checker.py` agora classifica artefatos locais recentes de `receipts`, `handoffs` e `approval-packets` sem ler/despejar conteúdo sensível.
- Gera `reports/memory-hygiene/events-latest.json` com caminhos/tipos sanitizados e camadas sugeridas.
- Gera `reports/memory-hygiene/scorecard-latest.json` com checks objetivos: watchdog, boot memory, coverage, provider externo, secret locator, hot/daily e captura de contexto de evento.
- Mantém contrato silent-OK: presença de eventos recentes não gera Telegram se hot/daily/memória estiverem saudáveis.

### Fase 4.6 / v1.2 — Hook local explícito — executada

- Criado `/opt/data/scripts/hermes_memory_os_event_hook.py`.
- O hook recebe um caminho de artefato Brain, infere tipo (`receipt`, `handoff`, `approval_packet`, `routine`, `prd`, `daily`, `hot`) e sugere camadas de memória.
- Em seguida chama o checker diurno com janela curta (`--since-minutes`) para atualizar scorecard/eventos imediatamente, não só no ciclo de 2h.
- Gera `reports/memory-hygiene/hook-latest.json` e acrescenta linha sanitizada em `reports/memory-hygiene/hook-events.jsonl`.
- Preserva silent-OK: sem `--json`, stdout fica vazio quando verde.

### Fase 4.7 / v1.3 — Integração padrão em protocolos — executada

- Atualizado `areas/operacoes/templates/receipt-operacional.md` para tornar o hook pós-receipt material obrigatório.
- Atualizado `areas/operacoes/rotinas/protocolo-receipts-handoff-v016-operating-layer.md` com regra Memory OS v1.3 pós-receipt/handoff/approval packet.
- Atualizado `areas/operacoes/rotinas/checklist-handoff-receipt-obrigatorio-2026-05-26.md` com checklist de hook.
- Isso padroniza a chamada do hook nos procedimentos canônicos, sem daemon, sem cron novo, sem gateway e sem Telegram em sucesso.

### Fase 4.8 / v1.4 — Wrapper local de receipt — executada

- Criado `/opt/data/scripts/hermes_memory_os_receipt_writer.py`.
- O wrapper recebe campos explícitos do template operacional, valida presença/consistência mínima, salva o receipt dentro do Brain e chama o hook v1.2 automaticamente.
- Gera `reports/memory-hygiene/receipt-writer-latest.json` e `reports/memory-hygiene/receipt-writer-events.jsonl` com evidência sanitizada.
- Preserva silent-OK: sem `--json`, stdout fica vazio quando receipt/hook/checker estão verdes.
- Bloqueia inconsistências locais óbvias: path fora do Brain, arquivo não-`.md`, classificação inválida, classificação sensível sem texto de aprovação/escopo, e writes externos declarados em receipt `read-only`/`local-write`.

### Fase 4.9 / v1.5 — Integração em rotinas frequentes — executada

- Atualizado `protocolo-receipts-handoff-v016-operating-layer.md` para tornar o wrapper o caminho preferencial de receipt novo.
- Atualizado `checklist-handoff-receipt-obrigatorio-2026-05-26.md` para exigir wrapper ou hook antes de fechar tarefa material.
- Atualizado `template-receipt-executivo-telegram-safe-v016.md` para lembrar que resultado no Telegram não substitui receipt completo via wrapper/hook.
- Atualizado `lcmordomo-handoff-protocol.md` para impedir que handoffs/receipts de subagentes virem ilhas sem Memory OS.
- Isso integra o wrapper onde os agentes realmente decidem criar receipts/handoffs, sem automatizar runtime, cron, gateway ou sistemas externos.

### Fase 4.10 / v1.6 — Linter local de adoção — executada

- Criado `/opt/data/scripts/hermes_memory_os_adoption_linter.py`.
- O linter compara artefatos recentes (`receipts`, `handoffs`, `approval-packets`) com evidências sanitizadas de `hook-events.jsonl` e `receipt-writer-events.jsonl`.
- Gera `reports/memory-hygiene/adoption-latest.json`, `adoption-events.jsonl` e baseline `adoption-baseline.json`.
- Preserva silent-OK: sem `--json`, stdout fica vazio quando não há gap; stdout aparece apenas para gap local acionável.
- Usa janela de graça padrão de 5 minutos para não competir com agentes ainda escrevendo/hookando artefatos ativos.
- Primeiro run detectou receipts recentes sem hook e os gaps seguros foram fechados localmente chamando o hook, sem ler/despejar conteúdo do artefato.

### Fase 4.11 / v1.7 — Linter integrado ao checker diurno — executada

- `hermes_memory_os_daytime_checker.py` agora chama o adoption linter em modo baseline v1.6.
- O relatório `daytime-latest.json` inclui bloco `adoption_linter` com `status`, `gap_count`, `covered_count`, `scanned_artifacts` e `grace_minutes`.
- O scorecard inclui `adoption_linter_ok`.
- Gaps pós-baseline viram rota local `memory_os_adoption_linter`; OK permanece silent-OK.
- O linter considera hook `ok` ou `attention` como evidência de adoção quando o evento foi logado, evitando deadlock onde o hook executa mas o checker ainda reportava gap anterior.

### Fase 4.12 / v1.8 — Auto-heal local limitado para gaps vencidos — executada

- O checker diurno agora tenta fechar até `--adoption-auto-heal-limit` gaps pós-graça, default `5`, rodando o hook local no artefato sem ler/despejar conteúdo.
- Auto-heal é desativado em `--dry-run`, quando o limite é `0`, e quando `HERMES_MEMORY_OS_SUPPRESS_ADOPTION_AUTOHEAL=1` está presente.
- O hook é chamado com a variável de supressão para impedir recursão hook → checker → auto-heal.
- Após tentativas, o checker reroda o linter e só fica verde se `gap_count=0`; gaps restantes continuam como rota local acionável.
- Teste sintético local comprovou `attempted=1`, `healed=1`, `gap_count=0`, `routes=[]` e stdout final vazio.

### Fase 4.13 / v1.9 — Observabilidade semanal/local — executada

- Criado `/opt/data/scripts/hermes_memory_os_weekly_observability.py`.
- Lê apenas logs sanitizados locais (`hook-events`, `receipt-writer-events`, `adoption-events`, `daytime-latest`, `scorecard-latest`).
- Gera `reports/memory-hygiene/weekly-observability-latest.json`, `.md` e `weekly-observability-events.jsonl`.
- Resume janela de 7 dias: saúde atual, gaps históricos vs latest, hooks, wrapper, áreas top por path sanitizado e recomendações.
- Mantém silent-OK: stdout vazio quando verde; `--json`/`--markdown` imprimem sob demanda.
- Não cria cron novo, não entrega Telegram, não lê conteúdo de artefatos e não vira fonte paralela ao Brain.

## 8. Acceptance criteria

- `latest.json` com `status=ok` ou alertas justificados e não corrigíveis localmente.
- `auto_template_coverage.coverage_missing_for_existing_memory=[]`.
- Nenhum boot memory acima do limite.
- Nenhum boot memory acima de 85% sem template seguro.
- `hot.md` current.
- daily do dia curada quando houver evento material.
- Provider externo off.
- Secret scan dos arquivos alterados com 0 achados.
- Receipts registram escopo, backups, verificação e não-ações.
- Quando possível, receipts operacionais são criados pelo wrapper v1.4+ e `receipt-writer-latest.json.status=ok`.
- Handoffs/approval-packets/artefatos legados usam hook como fallback, não como substituto padrão do `receipt_writer` para receipt novo.
- `adoption-latest.json.status=ok` para artefatos após o baseline v1.6.
- `daytime-latest.json.adoption_linter.status=ok` e scorecard `adoption_linter_ok=true` após v1.7.
- `daytime-latest.json.adoption_auto_heal` registra tentativas/heals v1.8 sem quebrar silent-OK.
- `weekly-observability-latest.json` e `.md` existem, status `ok`, findings vazios e stdout vazio quando verde.

## 9. Decisões abertas

1. Resolvido v1: rotina diurna como cron local/no_agent a cada 2h, `deliver=local`, mantendo ciclo 02h/02h15 como supervisor noturno.
2. Resolvido v1: templates seguem explícitos por profile enquanto não houver schema seguro testado para auto-geração.
3. Resolvido v1: frequência inicial a cada 2h; eventos materiais continuam exigindo curadoria/handoff no momento do evento.

## 10. Safe next step recomendado

Pendente: Mission Control/card visual read-only usando `weekly-observability-latest.json` fica fora do escopo atual por decisão de Lucas. Próxima melhoria segura: operar a v1.9 local por ciclos reais; só retomar Mission Control em rodada dedicada.

## v1.13 — ativação local 30min + alertas acionáveis + todos agentes/workers (2026-06-09)

Decisão Lucas:
- Memory OS daytime checker ativo a cada 30 minutos.
- OK permanece silencioso.
- Quando houver problema, o watcher tenta auto-heal local primeiro.
- Se corrigir, avisa Lucas com resumo curto: problema detectado, corrigido, nenhuma ação necessária.
- Se não corrigir e precisar de decisão humana, pergunta a Lucas o que fazer.
- Todos os `AGENTS.md` do Brain receberam contrato v1.13: receipts novos via `hermes_memory_os_receipt_writer.py`; workers legados devem usar `hermes_memory_os_worker_receipt_guard.py`/`--register-existing`; handoffs/approval packets seguem via hook.
- Mission Control não será usado como superfície operacional do Memory OS.

Estado de ativação:
- cron `bc96bb03d2b0`: `every 30m`, `deliver=origin`, `no_agent=true`, script `hermes_memory_os_daytime_alerting_watchdog.py`; stdout vazio = sem Telegram; stdout não vazio = alerta acionável.
- cron `e4c6b7c9b6dc`: observabilidade semanal local/silent mantida.
- helper worker: `/opt/data/scripts/hermes_memory_os_worker_receipt_guard.py`.



### v1.18 — Readiness pós-rollout profile-local — executada

- Rodada read-only/sanitizada após v1.17 para validar profiles, gateways vivos por `/proc`, config check, cron summaries e probes Memory OS.
- Corrigido drift local de data: `hot.md` e daily `2026-06-10` atualizados antes de alertar Lucas.
- `lc-claude-cli` era originalmente CLI/local-only, mas foi reativado como gateway Telegram em 2026-06-27 após aprovação escopada explícita de Lucas para `@hermesclaude_lcbot`; watchdogs devem tratar esse profile como gerenciado/esperado enquanto o receipt `areas/operacoes/receipts/lc-claude-cli-telegram-reactivation-20260627.md` estiver vigente.
- Nenhum restart, kill, cron mutation, Docker/VPS/Traefik, sistema externo ou valor de secret.
