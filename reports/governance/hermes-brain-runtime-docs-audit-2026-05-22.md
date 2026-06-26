# Hermes Brain + Runtime Docs Audit — 2026-05-22

> **HISTÓRICO / AUDITORIA — NÃO EXECUTAR COMO RUNBOOK.** Este relatório cita strings legadas perigosas apenas como evidência de saneamento.

**Solicitante:** Lucas Cimino  
**Execução:** 2026-05-22 10:05 BRT / 13:05 UTC  
**Escopo:** runtime/config/processos/logs, Brain/documentação/MAPAs/arquivos estruturais, crons/watchdogs/canais e ruído.  
**Modo:** read-only para produção/externos; correções feitas apenas em documentação local do Brain.

## Veredito executivo

O Hermes está **operacional e saudável** para continuar o trabalho, inclusive GMC em modo governado/read-only quando necessário.

Não encontrei falha estrutural bloqueante no Brain: o `brain_health_check.py` terminou com **0 FAIL / 0 WARN** depois das correções. A API local do Hermes respondeu `200 {"status":"ok","platform":"hermes-agent"}` e os gateways principais/secundários seguem ativos.

O que não estava 100% certo era **documentação legada**: alguns arquivos ainda traziam caminhos e procedimentos antigos de OpenClaw/`/root/*`/Mem0/`sshpass`, que poderiam induzir agente futuro a executar fluxo errado. Corrigi os pontos críticos.

## Evidências executadas

- `python3 scripts/brain_health_check.py`
  - secrets: FAIL=0 WARN=0
  - links: FAIL=0 WARN=0
  - required_files: FAIL=0 WARN=0
  - agent_files: FAIL=0 WARN=0
  - area_maps: FAIL=0 WARN=0
  - decisions_index: FAIL=0 WARN=0
  - routines_index: FAIL=0 WARN=0
  - skill_references: FAIL=0 WARN=0
  - Resultado: `All checks passed.`
- Health local Hermes: `http://127.0.0.1:8642/health` → `200`.
- Processos gateway encontrados: 1 gateway principal no container + 3 gateways especialistas isolados.
- Web tools validadas no turno: `web_search` e `web_extract` funcionando via Tavily/docs.
- Secret scan documental por padrões sensíveis: não apareceu token real; apenas variáveis/código que lê config (`TELEGRAM_BOT_TOKEN` em `hermes_remediate.sh`).
- Referências estruturais raiz (`README.md`, `START-HERE.md`, `AGENTS.md`, `MAPA.md`) sem backtick links quebrados.

## Correções aplicadas agora

### 1. Desativação segura do skill legado `brain-sync`

Arquivos corrigidos:

- `skills/brain-sync/SKILL.md`
- `areas/operacoes/skills/brain-sync/SKILL.md`

Antes: instruía `sshpass -p 'password'`, `/root/.hermes`, `/root/hermes-brain`, Mem0 e sync manual bidirecional.  
Depois: marcado como **legado / não executar**, apontando para:

- Brain atual: `/opt/data/hermes_bruno_ingest/hermes-brain`
- Runtime: `/opt/data` e `/opt/data/profiles/*`
- Sync atual: fechamento/sync allowlist do cron `3fc45b0830c6`
- Regra: nada de senha/token em comando, arquivo ou log.

### 2. Atualização do skill documental `hermes-brain`

Arquivo corrigido:

- `skills/hermes-brain/SKILL.md`

Antes: dizia que a memória central era consolidada do `cerebro-cimino` e mostrava `/root/hermes-brain`. Também tinha números de empresa que poderiam envelhecer.  
Depois: aponta para a estrutura atual do Brain e reforça que métricas/status vivos vêm de banco/API/fonte operacional.

### 3. Atualização de `TOOLS.md`

Arquivo corrigido:

- `TOOLS.md`

Antes: comandos de status em `/root/hermes-brain` e seção Brain com paths legados.  
Depois: status em `/opt/data/hermes_bruno_ingest/hermes-brain`, sync atual via `cronjob list`/cron `3fc45b0830c6`, scripts em `scripts/` e `/opt/data/scripts/` quando aplicável.

### 4. Atualização de protocolo de início de sessão

Arquivos corrigidos:

- `STARTUP.md`
- `skills/session-start-protocol/SKILL.md`

Antes: protocolo rígido com `cat /root/.hermes/*`, `brain_sync.sh`, Mem0 e commit/push antigo.  
Depois: protocolo Hermes-native com:

- `START-HERE.md`, `MAPA.md`, `AGENTS.md`
- `session_search` para histórico
- `cronjob list` para verdade de crons
- Brain atual em `/opt/data/hermes_bruno_ingest/hermes-brain`
- proibição de usar sync legado `/root/.hermes/scripts/brain_sync.sh`.

## Validação pós-correção

Busca por padrões críticos legados em Markdown:

- `sshpass -p 'password'`: 0
- `cd /root/hermes-brain && git status`: 0
- `bash /root/.hermes/scripts/brain_sync.sh`: 0
- `/root/hermes-brain/sync_hermes.sh`: 0
- `mem0_conclude`: 2 ocorrências históricas em `memories/lessons.md` e `empresa/gestao/licoes.md` — mantidas como memória/registro histórico, não instrução operacional.

Health check do Brain após as correções: **All checks passed**.

## Pontos de atenção encontrados

### A. Backlog Git grande / muitos arquivos não versionados

`git status --short` mostra muitas alterações e arquivos novos acumulados, principalmente relatórios, receipts e outputs de rotinas. Isso não quebra o runtime, mas é risco de governança:

- dificulta review;
- aumenta chance de commitar artefato grande/ruidoso;
- pode misturar documentação, evidência e output operacional.

Recomendação: fazer um PR/commit de higiene separado, com allowlist e revisão de tamanho/secrets antes.

### B. Crons: configuração geral saudável, mas há itens pausados/stale e um lembrete GMC one-shot antigo

`cronjob list` mostra 29 jobs. A maioria relevante está `ok` e os watchdogs ruidosos foram movidos para `local`, como decidido.

Pontos a revisar sem urgência:

- alguns jobs antigos pausados ainda aparecem no backlog;
- o lembrete `Lembrete GMC Data Sources 10h` aparece como one-shot com `next_run_at` já no horário do pedido e sem `last_run_at`; não mexi/removi porque alteração de cron é estado operacional, não apenas documentação.

Recomendação: em uma passada própria, limpar/arquivar one-shots vencidos e confirmar quais pausados continuam necessários.

### C. `hermes_remediate.sh` é perigoso se executado sem governança

O script existe no Brain e contém ações como matar processos, limpar cache, reiniciar serviços e enviar Telegram lendo token de config. Não encontrei token real versionado, mas o comportamento é sensível.

Recomendação: manter esse script documentado como legado/sensível ou envolver com guardrail explícito antes de qualquer uso. Não executei.

### D. Logs recentes têm warnings operacionais, mas não indicam falha sistêmica atual

Após 12:49 UTC apareceram warnings como:

- uma falha minha de comando de auditoria (`/usr/bin/command`/módulo yaml) — não afetou runtime;
- HTTP 500 transitório do provider com retry;
- warnings em perfis especialistas de tarefas paralelas/patches;
- navegação browser com HTTP error em Mordomo.

Não apareceram novos erros de Firecrawl/Tavily após a troca no contexto principal; web search/extract estão funcionando.

## O que está certo

- Brain estrutural passa no health check.
- Root docs principais estão coerentes: `README.md`, `START-HERE.md`, `AGENTS.md`, `MAPA.md`.
- Modelo mental da “Grande Mente / Hermes Brain / Hermes COO” está preservado.
- Guardrails de produção/externos estão claros.
- Web backend atual é `tavily` nos perfis auditados.
- Compressão está configurada para `google/gemini-3-flash-preview` via OpenRouter, como remediação anterior.
- API health local responde OK.
- Watchdogs barulhentos principais estão em `deliver=local`.

## Próximos passos recomendados

1. **Seguir no GMC**: ambiente está suficientemente estável para continuar diagnóstico de Data Sources em modo read-only.
2. **Higiene Git/Brain**: fazer uma rodada separada para classificar e versionar/ignorar outputs acumulados.
3. **Cron backlog**: revisar one-shots vencidos e pausados antigos; remover/pausar só com critério claro.
4. **Remediation script**: marcar `hermes_remediate.sh` como sensível/legado ou refatorar para dry-run + aprovação antes de qualquer ação destrutiva.

## Status final

**Stable / OK com ressalvas de higiene.**  
Não há bloqueio técnico para continuar GMC. As correções documentais críticas foram aplicadas e validadas.
