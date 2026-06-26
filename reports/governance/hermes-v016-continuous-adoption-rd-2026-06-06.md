# RD/PRD — Adoção contínua Hermes v0.16 para Lucas/Cimino

Data: 2026-06-06
Fonte oficial: GitHub Releases API — `NousResearch/hermes-agent`, tag `v2026.6.5`
Release: **Hermes Agent v0.16.0 (2026.6.5) — The Surface Release**
Runtime remoto atual: **Hermes Agent v0.16.0**, config version **27 ✓**
Interface escolhida por Lucas: **Dashboard remoto** em `https://hermes.lucascimino.com`

## 1. Objetivo

Transformar a v0.16 em melhoria real do ecossistema Lucas/Cimino, sem criar ruído técnico nem riscos desnecessários.

O foco não é “ter a versão nova instalada”. Isso já foi feito. O foco agora é **adotar os recursos certos como hábito operacional**:

- Dashboard como cockpit administrativo remoto.
- Telegram para decisões/alertas acionáveis, não ruído.
- Brain como fonte rica/canônica de documentação, receipts e governança.
- Desktop Mac somente como evolução futura se trouxer ganho claro sobre o Dashboard.
- Novas superfícies/admin/credentials/webhooks/MCP sempre com guardrails, backup e rollback.

## 2. Status atual verificado

Já concluído:

- Runtime remoto atualizado para `v0.16.0`.
- Config version `27 ✓`.
- Dashboard público configurado em `https://hermes.lucascimino.com`.
- Auth pública validada:
  - `/` sem login redireciona para `/login`.
  - `/api/config` sem auth retorna `401`.
- Container dashboard persistente `hermes-dashboard-public`, usuário não-root `10000:10000`.
- TRACK1 executado:
  - backup;
  - snapshot de dependências/config/tools/skills;
  - API/model catalog readback;
  - `/undo` validado por smoke descartável.
- TRACK2 executado:
  - Dashboard remoto como superfície principal;
  - Desktop remoto classificado como opcional/futuro;
  - API bruta não exposta publicamente.

Receipts principais:

- `receipts/hermes-dashboard-bridge-hermes-lucascimino-com-receipt-2026-06-06.md`
- `receipts/hermes-v016-track1-track2-receipt-2026-06-06.md`
- `reports/governance/hermes-v016-stage2-cutover-final-report-2026-06-06.md`

## 3. O que há de novo na v0.16 — visão completa por categoria

### 3.1 Desktop App nativo

Novidades:

- App Electron nativo para macOS/Linux/Windows.
- Instalação desktop e self-update in-app.
- Drag-and-drop de arquivos no chat.
- Paste de imagem do clipboard.
- Command palette `Cmd+K`.
- Picker de modelo no status bar.
- Sessões concorrentes multi-profile.
- Remote Hermes/gateway via OAuth ou username/password.
- Multi-profile remoto com links `@session` entre perfis.
- Interface traduzida para chinês simplificado.

Valor para Lucas:

- Pode virar um app confortável no Mac.
- Mas, para o objetivo atual, **Dashboard remoto é mais seguro e suficiente**.

Decisão de adoção:

- **P2 opcional**: testar só se Lucas sentir falta de uma experiência nativa.
- Não instalar/configurar como padrão agora.
- Não expor API bruta na internet para isso.

### 3.2 Dashboard Web virou admin panel completo

Novidades:

- Painel administrativo completo no browser.
- MCP catalog com enable/disable.
- Channels page para configurar plataformas de mensagem.
- Credentials management.
- Webhooks/hook creation.
- Memory configuration.
- Gateway controls.
- System page com check-before-update e Debug Share.
- Temas, bulk sessions, schedule picker, perfis enriquecidos.
- Auth username/password, OIDC/self-hosted, refresh-token rotation.
- Chat tab funciona em gated/OAuth mode.
- WebSocket/upload/plugin auth melhorados.

Valor para Lucas:

- Este é o maior ganho prático: o Dashboard deixa de ser só visualizador e vira cockpit administrativo.

Decisão de adoção:

- **P0/P1 agora**: usar Dashboard como cockpit diário/admin.
- **A3/A4 com aprovação**: qualquer mudança via painel que altere credentials, webhooks, canais, gateway, Docker/Traefik, MCP com permissões sensíveis ou API pública.

### 3.3 Provider/model picker e modelos novos

Novidades:

- Fuzzy model picker no Desktop/Web/TUI/CLI.
- Provedores multi-endpoint agrupados.
- Catálogo atualiza de hora em hora.
- Novos modelos citados na release:
  - `deepseek-v4-flash`;
  - `MiniMax-M3` com 1M context;
  - `qwen3.7-plus`;
  - `gemini-3.5-flash`.
- Persistência de troca de modelo no meio da sessão.
- Recuperação de modelo após interrupção.
- Melhor isolamento de credenciais/custom providers.

Valor para Lucas:

- Menos dependência de eu “lembrar” modelo certo.
- Melhor para alternar fast/deep quando necessário.

Decisão de adoção:

- **P1 agora**: auditar catálogo disponível no runtime e criar uma política simples:
  - modelo forte padrão para operações críticas;
  - modelo leve/rápido para triagem simples quando validado;
  - fallback documentado, mas sem trocar defaults de produção sem teste.

### 3.4 `/undo [N]`

Novidades:

- Desfaz os últimos N turnos do usuário.
- Prefill da mensagem anterior para editar e reenviar.
- Soft-delete dos turnos intermediários.
- Paridade CLI/TUI/messaging platforms.

Valor para Lucas:

- Se você manda algo errado, pode mandar:

```text
/undo
```

ou:

```text
/undo 2
```

Uso recomendado:

- Corrigir pedido mal formulado.
- Desfazer direção errada antes de continuar.
- Reduzir necessidade de “não, volta”.

Decisão de adoção:

- **P0 hábito agora**: ensinar Lucas e incluir nos microtreinamentos do digest.
- Smoke já passou em ambiente descartável.

### 3.5 Skills mais enxutas + curator mais forte

Novidades:

- Skill set padrão mais enxuto.
- Skills redundantes/pesadas movidas para opcionais.
- `environments:` relevance gate para reduzir ruído no índice.
- Curator pode podar skills built-in não usadas, com tracking de uso.
- NVIDIA/skills virou trusted skills tap.
- Skills Hub com browse/categorias/source links/copy buttons melhores.
- Novas skills opcionais como `grok` e `antigravity-cli`.

Valor para Lucas:

- Menos prompt/tool noise.
- Mais governança de skills.
- Possibilidade de catálogo NVIDIA se houver uso ML/GPU.

Decisão de adoção:

- **P1 governança**: auditar skills reais usadas por default/profiles e separar:
  - essenciais;
  - opcionais;
  - legadas;
  - pesadas demais para Telegram.
- Não deixar curator podar skills críticas do ecossistema Lucas sem receipt/guardrail.

### 3.6 Core Agent, prompt, tools e sessões

Novidades:

- Progressive tool disclosure para MCP/plugin tools.
- Hook de environment hint no system prompt.
- Universal task completion guidance.
- Probe local de toolchain Python.
- Delegation `max_spawn_depth` sem teto rígido.
- `hermes prompt-size` diagnostic.
- `read_file` com gutter mais compacto, reduzindo tokens.
- Melhor cwd/resume de sessão.
- Proteção contra fork de session-id por compressões concorrentes.
- Sessions optimize / FTS5 VACUUM merge.
- Honcho fail-open.
- Supermemory session ingest.

Valor para Lucas:

- Mais estabilidade em sessões longas.
- Menos tokens desperdiçados lendo arquivos.
- Melhor diagnóstico de prompt/contexto.
- Melhor governança de subagents e memória.

Decisão de adoção:

- **P1 agora**:
  - rodar diagnóstico periódico de tamanho/contexto quando houver lentidão;
  - adicionar `sessions optimize` em checklist local/manual antes de mutar cron;
  - atualizar governança de subagents para usar melhor context budget + handoff.

### 3.7 Kanban / multi-agent

Novidades:

- Cards `goal_mode` rodam workers em loop `/goal`.
- File attachments em tasks.
- Imagens referenciadas em task bodies vão para worker vision.
- Default assignee fallback.
- Per-profile concurrency cap.
- Endpoint para terminar runs.
- Melhor dispatch/config passthrough.

Valor para Lucas:

- Pode melhorar frentes longas: LK Growth, LK Shopify, Collection Optimizer, Mission Control, SPITI.

Decisão de adoção:

- **P2 controlado**: não abrir swarm/kanban amplo agora.
- Usar como base para PRD futuro de “frentes de trabalho duráveis”, com workers restritos e receipts.

### 3.8 Messaging/Gateway

Novidades:

- Structured stream-event protocol.
- Melhor paridade de formatação de rascunho Telegram.
- Streaming defaults por plataforma, Telegram on/Discord off.
- Dashboard toggles de streaming.
- Discord voice mixer.
- Feishu meeting invitations.
- Melhor service restart flow.
- Reconnect/failure cleanup.

Valor para Lucas:

- Telegram pode ficar mais fluido/streaming.
- Mas Lucas prefere Telegram só para decisões/alertas acionáveis, então streaming não deve virar ruído.

Decisão de adoção:

- **P1 UX**: manter Telegram limpo; dashboard para exploração/admin; Telegram para decisões.
- Não ativar features que aumentem ruído sem motivo.

### 3.9 CLI/TUI/Setup

Novidades:

- Default interface configurável: CLI vs TUI.
- TUI com `/model` único e Sessions overlay.
- Quick Setup via Nous Portal.
- Alias `hermes portal`.
- Processo aparece como `hermes` em ps/top/htop.
- TUI não congela com MCP lento/morto.
- Melhor suporte de clipboard/terminal.
- Pickers via curses.

Valor para Lucas:

- Mais útil para operadores técnicos do que para Lucas no Dashboard.
- Ainda melhora diagnóstico/manutenção por mim.

Decisão de adoção:

- **P1 operacional interno**: usar em manutenção, não exigir Lucas aprender CLI/TUI.

### 3.10 Tool system / installer

Novidades:

- Managed `uv` path consolidado.
- Installer com commit pinning opcional.
- Shallow clones.
- Rebuild de venv mais robusto.
- Validação de core deps após install.
- Update stashes/restores por padrão.
- MCP OAuth não reporta sucesso falso se token não existe.
- Vision respeita `model.supports_vision`.
- Melhorias MiniMax TTS e yuanbao media cache.

Valor para Lucas:

- Upgrades futuros ficam mais seguros.
- Menos diagnóstico falso.

Decisão de adoção:

- **P0 governança de upgrade**: toda release nova deve virar adoption matrix + plano, não só update binário.

### 3.11 Docker/deployment

Novidades:

- Reuso de container.
- Cleanup bounded sync e orphan reaper.
- Docker-in-Docker socket group autojoin.
- Boot non-root containers melhorado.
- Skip de chown desnecessário quando ownership já bate.
- Bootstrap de `gateway_state.json`.
- Containers ganham labels Hermes.
- TUI launcher via bundle prebuilt.

Valor para Lucas:

- Muito relevante porque o runtime é Docker-first/Hostinger.
- Confirma que nossa correção para dashboard não-root está alinhada com a direção da release.

Decisão de adoção:

- **P1 observabilidade**: auditar labels/usuário/container policy.
- **A3** se for alterar imagem/compose/container principal.

### 3.12 Segurança e confiabilidade

Novidades:

- CVE-2026-48710 / Starlette BadHost pin.
- SSRF checks fora do event loop em paths async.
- Strip de Bedrock inference bearer token de subprocess env.
- Guard para `bws_cache.json`.
- Neutralização de paths em mutation verifier footer.
- Restore de contexto approval/sudo em `execute_code`.
- `docker restart/stop/kill` como dangerous patterns.
- Sanitização de unicode invisível em skill content.
- Melhor isolamento de tool mutation.
- Sandbox mirror write guard.
- Honcho fail-open.

Valor para Lucas:

- Segurança é P0/P1, especialmente com dashboard público e ferramentas fortes.

Decisão de adoção:

- **P0 já**: manter dashboard protegido e API bruta não pública.
- **P1**: criar checklist de segurança v0.16 recorrente:
  - dashboard auth probes;
  - public route probes;
  - dangerous Docker command guard awareness;
  - secret scan dos receipts;
  - Brain Health.

### 3.13 Bug fixes importantes

Novidades principais:

- Desktop: chats não somem, Stop interrompe, completion menu melhor, IME corrigido.
- Update: stash/restore não clobbera desktop source; rebuild/skills sync mais robustos.
- Voice: melhorias em sound server/SSH e Mistral.
- 399 issues fechadas no ciclo.

Valor para Lucas:

- Justifica usar v0.16 como baseline atual.
- Voice/STT/TTS deve ser revalidado em outro track se Lucas quiser voz no Dashboard/Desktop.

## 4. Matriz de adoção Lucas

### Já adotado / concluído

1. Runtime v0.16 ativo.
2. Config migrada para version 27.
3. Dashboard remoto público com auth.
4. API bruta mantida local/host-local, não pública.
5. Backup/rollback e receipts.
6. `/undo` smoke test.
7. TRACK1/TRACK2.

### P0 — hábitos agora

1. Usar Dashboard como cockpit principal.
2. Usar Telegram para decisões/alertas, não exploração técnica.
3. Ensinar `/undo`:
   - `/undo` para desfazer último pedido.
   - `/undo 2` para voltar dois turnos.
4. Toda novidade Hermes deve virar adoption matrix + receipt, não só update.
5. Manter dashboard/API probes no checklist de segurança.

### P1 — melhorias operacionais seguras

1. Criar “Manual Lucas do Dashboard v0.16” em Brain:
   - onde ver sessões;
   - onde ver skills/tools;
   - onde ver cron/schedules;
   - onde não clicar sem aprovação;
   - como pedir ação segura pelo Telegram.
2. Criar checklist recorrente pós-release:
   - release notes;
   - config check;
   - model catalog;
   - dashboard auth probes;
   - `/undo` smoke;
   - Brain Health;
   - secret scan.
3. Auditar skills com o novo paradigma enxuto:
   - reduzir ruído em Telegram/profile toolsets;
   - preservar skills críticas de Lucas;
   - documentar curator boundaries.
4. Auditar modelos/fallbacks novos sem trocar default automaticamente.
5. Adicionar micro-aulas v0.16 ao digest diário/semanal:
   - Dashboard;
   - `/undo`;
   - model picker;
   - skills curator;
   - sessions/search;
   - quando pedir approval.

### P2 — avaliar depois

1. Desktop App remoto no Mac.
2. Kanban/goal_mode durável para frentes longas.
3. MCP/channel/credentials management pelo Dashboard.
4. OIDC para Dashboard em vez de username/password.
5. Voice/desktop microphone workflow.
6. NVIDIA skills tap se houver demanda ML/GPU.

### A3/A4 — só com aprovação específica

1. Alterar Docker/compose/Traefik/gateway principal.
2. Expor API bruta publicamente.
3. Conectar Desktop remoto por OAuth/username-password sem túnel/sem threat model.
4. Mexer em credentials pelo Dashboard.
5. Criar/remover webhooks públicos.
6. Ativar/desativar MCP com permissões fortes.
7. Trocar modelo default/fallback de produção.
8. Habilitar workers/kanban para tarefas externas/Shopify/ads/clientes.

## 5. Como vamos implementar para ficar cada vez melhor

### Fase 1 — Agora: operacionalizar o Dashboard

Entregáveis:

- Manual Lucas Dashboard v0.16.
- Checklist “onde posso clicar / onde pedir aprovação”.
- Rotina de health check curta:
  - `/` redireciona para login;
  - `/api/config` sem auth = 401;
  - API local health ok;
  - Brain Health ok.

Impacto:

- Lucas usa Dashboard com segurança sem precisar aprender terminal.

### Fase 2 — Esta semana: transformar novidades em hábitos

Entregáveis:

- Micro-aulas no digest:
  1. `/undo`;
  2. Dashboard Admin;
  3. Model picker;
  4. Sessions/search;
  5. Skills/curator.
- Atualizar skill/runbook de upgrades para v0.16+.
- Auditoria de skills/toolsets por perfil para reduzir ruído.

Impacto:

- Menos repetição, menos “seguir”, menos ruído, mais controle.

### Fase 3 — Próxima: segurança/admin avançado

Entregáveis:

- Approval packet para usar Dashboard em operações sensíveis:
  - MCP;
  - channels;
  - credentials;
  - webhooks;
  - gateway controls.
- Separar ações read-only vs writes sensíveis.
- Criar receipts padronizados para mudanças feitas via Dashboard.

Impacto:

- Dashboard vira cockpit real sem virar risco.

### Fase 4 — Opcional: Desktop Mac remoto

Condição para avançar:

- Lucas sentir que Dashboard não basta.

Plano seguro:

- Testar Desktop em Remote Mode.
- Preferir auth nativa remota/OAuth/username-password da v0.16, mas somente após threat model.
- Alternativa segura: SSH tunnel + API local.
- Não criar Hermes local paralelo como fonte de verdade.

Impacto:

- App nativo, mas sem sacrificar segurança.

## 6. Riscos e guardrails

### Risco 1 — Dashboard com poderes demais

Mitigação:

- Tratar Dashboard como admin panel.
- Read-only/exploração ok.
- Credentials/webhooks/channels/MCP/gateway writes precisam approval/receipt.

### Risco 2 — Desktop criar Hermes paralelo

Mitigação:

- Não usar local mode como source of truth.
- Se Desktop for usado, configurar remote mode explicitamente.

### Risco 3 — Telegram virar ruído

Mitigação:

- Telegram só alertas acionáveis, decisões, exceções e resumos desejados.
- Exploração/admin pelo Dashboard.

### Risco 4 — Curator/skills removerem conhecimento crítico

Mitigação:

- Skills críticas Lucas protegidas por governança/receipts.
- Curator só com relatório e reversibilidade.

### Risco 5 — Novos modelos/fallbacks quebrarem operação

Mitigação:

- Smoke tests por provedor/modelo.
- Trocas default só com rollback.
- Separar simple/fast de critical/deep.

## 7. Critérios de sucesso

A v0.16 estará bem adotada quando:

1. Lucas usar Dashboard sem precisar terminal.
2. Lucas souber usar `/undo` quando errar pedido.
3. Toda mudança sensível via Dashboard gerar receipt.
4. Telegram ficar mais limpo, não mais barulhento.
5. Skills/toolsets ficarem mais focadas por perfil.
6. Releases novas gerarem adoption matrix automaticamente.
7. Desktop Mac for opcional, não fonte de confusão.
8. Brain registrar o que foi adotado, o que foi bloqueado e o que precisa aprovação.

## 8. Próximas ações recomendadas

### Executar sem nova aprovação — A0/A1 local/documental

1. Criar Manual Lucas Dashboard v0.16.
2. Atualizar micro-aulas do digest com `/undo` e Dashboard.
3. Criar checklist de segurança Dashboard/API v0.16.
4. Atualizar runbook de release adoption para refletir que v0.16 já está ativo.
5. Fazer auditoria read-only de skills/toolsets por perfil.

### Pedir aprovação antes — A3/A4

1. Ativar ou editar credentials/webhooks/channels/MCP pelo Dashboard.
2. Trocar auth do Dashboard para OIDC.
3. Conectar Desktop Mac remoto sem túnel.
4. Trocar modelos default/fallback de perfis vivos.
5. Ativar Kanban workers para tarefas com impacto externo.

## 9. Recomendação executiva

Para Lucas agora:

- Use **Dashboard** como interface principal.
- Use **Telegram** para mandar pedidos e receber decisões/alertas.
- Aprenda `/undo` como primeiro novo hábito v0.16.
- Não priorize Desktop Mac neste momento; ele é bom, mas o Dashboard já atende o objetivo remoto com menos risco.
- Eu devo continuar transformando releases Hermes em:
  - matriz de adoção;
  - checklist operacional;
  - receipts;
  - micro-aulas;
  - melhorias de skills/Brain;
  - approval packets quando houver risco.
