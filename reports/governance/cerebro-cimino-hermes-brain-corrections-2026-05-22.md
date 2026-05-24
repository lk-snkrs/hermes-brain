# Correções — Cérebro Cimino / Hermes Brain — 2026-05-22

Status: **executado e verificado localmente**
Escopo: documentação Brain, higiene de crons, segurança de scripts legados e triagem de logs.

## 0. Esclarecimento de nomenclatura

Decisão canônica: **Cérebro Cimino = Hermes Brain = Grande Mente / Hermes COO**.

Não são dois cérebros separados. A diferença é apenas de uso:

- `Hermes Brain`: nome técnico/documental do repositório e da camada versionada.
- `Cérebro Cimino`: nome executivo/humano para a mesma grande mente de Lucas.
- `Hermes Agent`: runtime/agente que conversa no Telegram e usa ferramentas; lê/escreve/executa usando o Brain.
- Perfis como Mordomo, LK Growth e SPITI: braços/agentes especialistas, não cérebros concorrentes.

Arquivos atualizados:

- `empresa/contexto/nomenclatura-cerebro-cimino-hermes-brain.md` criado como referência canônica.
- `START-HERE.md` atualizado para evitar duplicação de cérebro/profile/repo/rotina por diferença de nome.
- `MAPA.md` atualizado com link de navegação para a nomenclatura.

## 1. Backlog Git/Brain e allowlist segura

Correção aplicada:

- Reforçada a documentação de Brain Sync seguro em `areas/operacoes/rotinas/brain-sync.md`.
- Confirmado que o executor aprovado continua sendo `/opt/data/scripts/brain_sync_safe.py`.
- Explicitado que `scripts/brain_sync.sh` é legado/OpenClaw-era e deve sair com `DEPRECATED`, sem tocar SSH/VPS/arquivos.
- Dry-run do Brain Sync seguro mostrou allowlist documental e bloqueio de artefatos brutos/sensíveis:
  - `allowed_files`: 49
  - `skipped_files`: 291
  - bloqueios incluem `config/`, `scripts/`, HTML/CSV/TXT/JS/JSON brutos fora de allowlist, receipts e snapshots.

Decisão: não fazer push/commit manual nesta rodada; manter o sync seguro/allowlist como gate e evitar promover artefatos brutos por impulso.

## 2. Crons one-shot/pausados

Correção aplicada:

- Removido cron one-shot vencido, pausado e sem execução:
  - `527ee57b3a6b` — `Mordomo: confirmar entrega com Seda Embalagens`
  - schedule antigo: `once at 2026-05-19 12:00`

Preservado:

- `a7e883edd200` — `LK SEO/CRO impact review — SEO title/meta P1 packets`
  - motivo: one-shot futuro/pausado relacionado a avaliação operacional; não era a mesma categoria de vencido/obsoleto.

Nenhum delivery, schedule, script, Docker, gateway ou runtime foi alterado.

## 3. Scripts legados sensíveis

Correção aplicada:

- `scripts/brain_sync.sh` agora aborta imediatamente com status `2` e mensagem `DEPRECATED` antes de qualquer SSH/VPS/local write.
- `sync_hermes.sh`, `brain_sync.sh`, `scripts/memory-flush.sh` e `scripts/git-accountability.sh` também foram convertidos em stubs `DEPRECATED` sem side effects.
- `hermes_remediate.sh` agora aborta imediatamente com status `2` e mensagem `LEGACY_DISABLED` antes de qualquer mutação de host/processo/Docker/cache.

Motivo: ambos continham padrões legados ou mutações amplas demais para execução unattended no ambiente Lucas/Cimino.

Guardrail mantido:

- Remediação de runtime/Docker/VPS/gateway continua exigindo plano, rollback e aprovação explícita, salvo watchdog específico já aprovado e escopado.

## 4. Triagem de warnings recentes

Janela revisada: logs após 2026-05-22 13:09 UTC.

Achados:

- 6 matches recentes, todos gerados pela própria rodada de correção/verificação:
  - `.gitignore` inexistente consultado uma vez;
  - duas tentativas de patch que falharam por formato/hunk e foram corrigidas em seguida;
  - duplicação esperada em `agent.log` e `errors.log`.

Sem achados recentes de:

- `Port 8642/8644 already in use`;
- `Compression summary failed` / fallback marker;
- `Bad file descriptor`;
- `Firecrawl search error`;
- `Unauthorized: Failed`;
- traceback persistente pós-correção.

Correção aplicada: não houve restart/gateway/Docker. Os warnings eram de ferramenta nesta própria sessão e foram resolvidos por novo patch correto.

## Não-ações deliberadas

- Não toquei GMC/Shopify/Tiny/Ads/WhatsApp/e-mail externo.
- Não reiniciei gateway, Docker, VPS nem containers.
- Não fiz bulk cleanup de reports/receipts/snapshots.
- Não removi crons recorrentes pausados sem decisão operacional específica.
- Não expus secrets.

## Verificação final executada

Evidência local de 2026-05-22:

1. `python3 scripts/brain_health_check.py`
   - `secrets: FAIL=0 WARN=0`
   - `links: FAIL=0 WARN=0`
   - `required_files: FAIL=0 WARN=0`
   - `agent_files: FAIL=0 WARN=0`
   - `area_maps: FAIL=0 WARN=0`
   - `decisions_index: FAIL=0 WARN=0`
   - `routines_index: FAIL=0 WARN=0`
   - `skill_references: FAIL=0 WARN=0`
2. Execução controlada de scripts legados:
   - `scripts/brain_sync.sh`, `hermes_remediate.sh`, `sync_hermes.sh`, `brain_sync.sh`, `scripts/memory-flush.sh`, `scripts/git-accountability.sh` retornaram `rc=2` antes de qualquer ação.
3. Scan ativo de padrões legados perigosos em `.sh` e docs operacionais/skills:
   - `ACTIVE_LEGACY_FINDINGS=0` para os padrões testados.
4. `brain_sync_safe.py --dry-run --verbose`:
   - `exit=0`
   - `allowed_files=56`
   - denylist preservada para scripts/config/artefatos brutos.
5. `cronjob list` após remoção:
   - total reduziu para `27` jobs;
   - `527ee57b3a6b` ausente.
