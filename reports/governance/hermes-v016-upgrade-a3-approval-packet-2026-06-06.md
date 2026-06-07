# Approval Packet A3 — Avaliação de upgrade Hermes v0.16 — 2026-06-06

Status: preparado após Lucas escolher `Fazer` na Mesa COO 2026-06-06 Decisão 1/4.

## Escopo aprovado nesta etapa

Preparar pacote read-only/documental para avaliar o upgrade Hermes v0.15.2 → v0.16.0.

## Escopo explicitamente NÃO aprovado

- Sem Docker/container/compose/image swap.
- Sem gateway restart/reload.
- Sem alteração de cron.
- Sem troca de runtime vivo.
- Sem alteração de secrets/credenciais.
- Sem exposição pública de dashboard/API/desktop backend.
- Sem writes em Shopify, Tiny, GMC, Klaviyo, Meta, Supabase, WhatsApp, e-mail ou qualquer sistema externo.

## Evidência verificada

- Data/hora da preparação: 2026-06-06T09:39Z UTC.
- Runtime local vivo: `Hermes Agent v0.15.2 (2026.5.29.2)`.
- Release upstream: `v2026.6.5` / Hermes Agent v0.16.0, publicada em `2026-06-06T00:55:58Z`.
- Fonte release: GitHub Releases API `https://api.github.com/repos/NousResearch/hermes-agent/releases?per_page=5`.
- Report 02h: `reports/hermes-continuous-improvement/2026-06-06.md`.
- Matriz inicial: `reports/governance/hermes-v016-adoption-matrix-2026-06-06.md`.
- Cron vivo inspecionado via `cronjob list`: 31 jobs listados; Mesa COO e daily intelligence loop com `last_status=ok`.

## Por que v0.16 importa

Release grande: 874 commits, 542 PRs, 1.962 arquivos alterados, com foco em superfície/admin/desktop e correções de segurança.

Pontos relevantes para Lucas/Hermes:

1. **Hermes Desktop**: app nativo macOS/Linux/Windows, drag-and-drop, sessões, model picker, multi-profile e conexão remota.
2. **Remote Hermes / auth**: desktop pode conectar a Hermes remoto via OAuth ou username/password.
3. **Web dashboard/admin panel**: MCP catalog, messaging channels, credentials, webhooks, memory e login pluggable.
4. **Setup/model picker/skills**: setup via Nous Portal, fuzzy model picker, default skills trimmed, skills hub taps.
5. **UX de sessão**: `/undo` para remover últimos N turns.
6. **Segurança**: Starlette/CVE-2026-48710, SSRF off-loop hardening e stripping de credenciais em subprocessos.

## Classificação de risco

A3 — oportunidade de upgrade planejado. A preparação é local/read-only; a execução real envolve runtime/Docker/gateway e exige aprovação explícita separada.

Motivo: produção atual é Docker-first, com Telegram gateway, crons, profiles especialistas, patches locais e watchdogs sensíveis. v0.16 muda superfície/admin/autenticação e pode alterar comportamento de dashboard/API/skills/setup.

## Impacto esperado por área

### Telegram/gateway

Avaliar se alterações de gateway/dashboard/auth interferem em:

- entrega limpa da Mesa COO;
- botões inline / callbacks;
- mensagens `MEDIA:`;
- voice/STT/TTS quando aplicável;
- health checks e logs pós-restart.

### Cron/scheduler

Avaliar:

- `cronjob list/status`;
- `no_agent` silent-OK;
- `context_from` nos jobs 01h/02h/02h15/02h30;
- Mesa COO com decisão sequencial e botões nativos;
- watchdogs de gateway, runtime, compressão, memória e latency.

### Skills/memory/profiles

Avaliar:

- skills locais e profile-specific skills;
- default skill set trimmed na v0.16;
- memória boot mínima vs Brain;
- profiles default, mordomo, lk-growth, lk-shopify, lk-collection-optimizer, spiti e outros esperados.

### Dashboard/Desktop/Mission Control

Separação recomendada:

- Dashboard/Desktop v0.16 = superfície admin/runtime/observabilidade.
- Mission Control = decisão executiva, receipts, approval packets e cockpit de negócio.

Não conectar desktop/dashboard direto ao backend produtivo sem plano de autenticação, rede, rollback e permissões mínimas.

## Patches locais críticos a preservar/testar

Inventário mínimo antes de qualquer swap:

- Telegram clean delivery / remoção de wrappers técnicos.
- Mesa COO inline buttons / callback handling.
- Context compression transient retry/self-heal.
- Model timeout/fallback/latency watchdogs.
- Specialist profile runtime verification.
- Memory hygiene watchdog e compaction safe scope.
- Runtime/cron watchdog expectations.
- Host Docker observability helper.
- Brain Health / Brain Improvement Score / artifact validator.

## Plano de preparação antes do upgrade real

1. Criar inventário exato do runtime atual:
   - versão Hermes;
   - config path;
   - env keys presentes sem valores;
   - profile homes;
   - cron registry;
   - scripts locais;
   - patches locais relevantes.
2. Fazer backup local/sanitizado:
   - `config.yaml`;
   - `.env` somente como arquivo protegido, sem imprimir valores;
   - skills;
   - sessions quando necessário;
   - cron registry;
   - scripts em `/opt/data/scripts/`;
   - Brain artifacts de governança.
3. Preparar instalação paralela ou imagem paralela, sem trocar runtime vivo.
4. Rodar checks em paralelo/staging:
   - `hermes --version`;
   - `hermes config check`;
   - `hermes config migrate --dry-run` quando suportado, ou plano manual se não suportado;
   - `hermes skills list`;
   - `hermes tools list`;
   - `hermes cron list/status` em ambiente apropriado;
   - smoke CLI simples;
   - smoke profile-local para perfis críticos.
5. Rodar testes/validações dirigidas:
   - parser de botões Mesa COO;
   - extração/limpeza de wrappers Telegram;
   - watchdogs silent-OK;
   - memory hygiene receipt;
   - Brain Health;
   - targeted secret scan.
6. Preparar janela de ativação com plano de rollback antes de qualquer restart/swap.

## Smoke tests mínimos se Lucas aprovar o upgrade real

Antes do swap:

- Backup concluído e rollback legível.
- Runtime paralelo responde `hermes --version` v0.16.
- `hermes config check` sem erro crítico.
- Skills essenciais visíveis.
- Toolsets críticos visíveis.
- Brain Health local sem FAIL/WARN novos.
- Secret scan targeted limpo.

Depois do swap/restart, se aprovado:

- Gateway main vivo por `HERMES_HOME` correto.
- Telegram conectado e responde.
- API `/health` ok quando habilitada.
- `cronjob list` preservado.
- Mesa COO entrega card limpo sem wrapper/JSON/marcador.
- `no_agent` watchdogs silent-OK.
- Perfis especialistas esperados classificados como required vs dormant.
- Logs sem crash loop e sem secrets.

## Rollback proposto

Rollback deve ser preparado antes da ativação real:

1. Manter runtime v0.15.2 atual intacto até v0.16 passar smoke tests.
2. Preservar launcher/config anterior.
3. Se gateway falhar após swap, restaurar launcher/runtime anterior e reiniciar somente o gateway afetado dentro da janela aprovada.
4. Se cron/scheduler falhar, restaurar cron registry backup e voltar runtime anterior.
5. Se dashboard/API apresentar risco de auth/exposição, desligar superfície nova e manter Telegram/CLI como canais principais.
6. Registrar receipt pós-rollback com versão ativa, processo vivo e logs sanitizados.

## Decisão necessária para executar upgrade real

Ainda não aprovado.

Para avançar além deste pacote, Lucas precisa aprovar explicitamente uma janela e escopo contendo:

- alvo: Hermes default production runtime v0.15.2 → v0.16.0;
- método: instalação/imagem paralela primeiro;
- ação permitida: backup + staging + smoke + restart/swap controlado;
- rollback: restaurar v0.15.2/launcher/config anterior;
- exclusões: sem exposição pública nova, sem writes externos, sem secrets, sem Shopify/Tiny/GMC/Klaviyo/Meta/Supabase/WhatsApp/e-mail.

## Recomendação

Preparar staging/paralelo é recomendado. Executar upgrade real hoje só deve acontecer se houver janela curta, rollback testável e prioridade para segurança/surface v0.16 maior que o risco de mexer em gateway/crons durante o dia.
