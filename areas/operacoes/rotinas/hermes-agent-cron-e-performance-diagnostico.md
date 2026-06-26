# Rotina — Diagnóstico Hermes Agent: crons e performance

Atualizado em: 2026-05-25
Owner: Hermes Agent / Operações Hermes
Escopo: Hermes Agent central, runtime, crons, watchers e saúde de sessão
Risco: A0/A1 read-only por padrão; qualquer restart, criação/alteração de cron, Docker/VPS/gateway ou limpeza destrutiva exige aprovação explícita de Lucas.

## Objetivo

Transformar os aprendizados 1 e 2 do digest Pixel AI Hub / Brainzinho em rotina do **Hermes Agent central**, não do Mordomo operacional:

1. Auditoria de cron não pode enxergar só o próprio job.
2. Performance de agente deve ser diagnosticada por camadas antes de limpar, reiniciar ou mexer em runtime.

## 1. Auditoria de crons: fonte primária antes de conclusão

Quando um agente ou cron alegar que “está tudo certo”, “o job falhou” ou “não há cron ativo”, verificar mais de uma superfície antes de concluir.

### Fontes mínimas

1. Scheduler do perfil/runtime correto:
   - `HERMES_HOME=/opt/data /opt/hermes/.venv/bin/hermes cron list --all`
   - ferramenta `cronjob(action='list')` quando o guardrail permitir.
2. Registro persistido do scheduler:
   - `/opt/data/profiles/<profile>/cron/jobs.json`
3. Output real do job:
   - `/opt/data/profiles/<profile>/cron/output/<job>/`
4. Logs do agente/gateway quando houver falha de execução:
   - `/opt/data/profiles/<profile>/logs/agent.log`
   - logs de gateway somente em modo read-only.
5. Script ou prompt apontado pelo job, se existir.

### Regra de julgamento

- Se só uma fonte foi consultada, o resultado é **evidência parcial**, não conclusão.
- Se o job aparece em `jobs.json` mas não no CLI atual, investigar perfil/HERMES_HOME antes de declarar removido.
- Se stdout está vazio e `rc=0`, respeitar contrato silent-OK.
- Se stdout contém wrapper, job id ou metadado cru para Lucas, tratar como problema de UX/entrega, não necessariamente falha do conteúdo.

### Proibido sem aprovação

- Criar, remover, pausar, atualizar ou migrar cron real.
- Editar `jobs.json` manualmente como substituto do scheduler.
- Reiniciar gateway/Docker/VPS para “ver se resolve”.

## 2. Performance de agente: diagnóstico por camadas

Antes de recomendar “limpar tudo”, apagar memória, reiniciar runtime ou mexer em Docker, separar o problema por camada.

### Checklist read-only

1. **Canal**: Telegram/CLI/API/gateway? O atraso é só em um canal?
2. **Modelo/provedor**: latência, falha de stream, rate limit, erro de compressão ou provider específico?
3. **Sessão/contexto**: conversa longa, compressões frequentes, tool outputs grandes, skill demais carregada?
4. **Ferramentas**: loops de terminal, browser, web, session_search ou cron outputs gigantes?
5. **Runtime local**: disco, memória, processos, locks, logs, jobs concorrentes.
6. **Scheduler**: crons simultâneos, jobs no_agent com timeout, outputs ruidosos.
7. **Fonte de verdade**: confirmar se o runtime inspecionado é o mesmo que está atendendo Lucas.

### Ações seguras antes de qualquer mutação

- Testar uma sessão limpa ou pergunta simples para separar contexto vs runtime.
- Ler logs recentes sem expor segredo.
- Medir outputs e arquivos grandes antes de culpar o modelo.
- Produzir um packet com evidências, recomendação e rollback se a solução exigir restart/cron/config.

### Critérios para escalar

Escalar para approval packet quando a solução proposta envolver:

- restart de gateway;
- mudança de config/model/tools;
- criação/transferência/remoção de cron;
- limpeza de sessões/memória/arquivos;
- Docker/VPS/Traefik/volumes/rede;
- acesso ou movimentação de secrets.

## Aplicação ao digest Pixel AI Hub

Os itens 1 e 2 do digest de 2026-05-25 foram classificados como melhoria de **Hermes Agent / Operações**, não como tarefa do Mordomo. O destino durável é esta rotina e o cockpit/Brain do Hermes central.

## Verificação

Antes de declarar concluído após usar esta rotina:

```bash
python3 scripts/brain_health_check.py
python3 scripts/operational_docs_guard.py --json
python3 scripts/operational_docs_guard.py --strict-runtime --json
```

Critério: sem FAIL novo introduzido pela documentação.
