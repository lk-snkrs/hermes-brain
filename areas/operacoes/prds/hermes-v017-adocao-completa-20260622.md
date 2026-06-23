# PRD — Adoção completa Hermes Agent v0.17.0 no ecossistema Lucas/Cimino

Data: 2026-06-22
Runtime base: Hermes Agent v0.17.0 (`v2026.6.19`)
Fonte primária: release notes oficiais GitHub `NousResearch/hermes-agent/releases/tag/v2026.6.19`
Status: iniciado — runtime atualizado e adoção mapeada; ativações sensíveis pendentes de pacotes escopados.

## Pedido de Lucas

> “Eu quero adotar, todas as melhorias do Hermes 0.17.”

Interpretação operacional: adotar a v0.17 em máximo aproveitamento, sem confundir “desejo estratégico de adoção total” com autorização irrestrita para credenciais, canais externos, dashboard público, Docker/VPS/Traefik, WhatsApp, iMessage, Raft, MCPs ou writes externos.

## Guardrails obrigatórios

- Telegram para Lucas continua apenas para decisão real, bloqueio concreto, risco, erro operacional, falha de ferramenta ou ação que exija input.
- Brain é a fonte canônica para adoption matrix, receipts, PRDs e governança.
- Doppler `lc-keys/prd` é a fonte de verdade de secrets. Reportar só presença/ausência/status; `values_printed=false`.
- Docker/VPS/Traefik/secrets/exposição pública/canais externos/writes de negócio exigem aprovação escopada + backup/rollback + verificação.
- Não adotar tudo como “ligar tudo”; adotar como trilhas: automático, local seguro, sensível com aprovação, não aplicável/agendado.

## Release summary oficial

Hermes v0.17.0 — “The Reach Release”:

- ~1.475 commits, ~800 PRs, 1.693 arquivos alterados, 300+ issues fechadas.
- Novos canais/superfícies: iMessage via Photon Spectrum, Raft gateway channel, WhatsApp Business Cloud API oficial, SimpleX.
- Desktop App amadurecido: shortcuts, notificações, watch-windows para subagentes, seletor de modelo, terminal redimensionável, temas VS Code, drafts por thread, remote media relay.
- Subagentes assíncronos/background: `delegate_task(background=true)`.
- `image_generate` com image-to-image/editing.
- Automation Blueprints.
- xAI/Grok Composer (`grok-composer-2.5-fast`) via OAuth.
- Dashboard: profile builder, multi-profile global, Skills Hub reformulado, security scan de skills, login seguro.
- `memory` tool: operações atômicas em lote.
- Telegram: Bot API 10.1 rich messages, mensagens longas melhores, markdown/progressos melhores.
- MCP: catálogo/instalação melhorados, elicitation handler, keepalive, late-connecting tools, hardening contra stdio suspeito.
- Segurança/confiabilidade: redaction, fail-closed, cron env sanitization, CVEs, Docker/s6/installer fixes.
- Curator: consolidação LLM opt-in; pruning determinístico permanece, custo rotineiro zero.

## Evidência local já coletada

Run directory:
- `/opt/data/backups/hermes-v017-adoption-20260622T105834Z`

Arquivos:
- `feature_command_probe.log`
- `feature_help_probe2.log`
- `doppler_new_surfaces_probe.log`

Runtime:
- `Hermes Agent v0.17.0 (2026.6.19)` ativo.
- Comandos detectados: `whatsapp-cloud`, `dashboard`, `curator`, `photon`, `mcp catalog/install`, `profile`, `plugins`, `cron`.
- `photon --help` disponível com `setup/status/install-sidecar/telemetry`.
- `dashboard --help` disponível com host/port/local/insecure/status/stop/register.
- `whatsapp-cloud --help` disponível; requer Business account e public webhook URL.
- `curator --help` confirma prune/backup/rollback/status/run.
- Doppler candidate probe para novas superfícies: `XAI_API_KEY` presente; Photon/Raft/WhatsApp Cloud/Dashboard password candidates ausentes sob os nomes testados. Isso não prova integração impossível; prova que nomes esperados ainda não estão no mapa/segredo atual.
- `values_printed=false`.

## Matriz de adoção

### A. Já adotado/ativo automaticamente

1. Runtime v0.17 no gateway Telegram default.
   - Status: ativo.
   - Evidência: health `version=0.17.0`, config `30 ✓`, Telegram conectado, cron ativo.

2. Telegram rich text / Bot API 10.1.
   - Status: disponível/ativo por padrão conforme release.
   - Ação: observar regressões de renderização, especialmente relatórios longos e blocos de código.

3. `memory` tool batch operations.
   - Status: disponível no runtime/tools.
   - Ação: orientar agentes a usar operações em lote quando memória estiver cheia.

4. Curator custo-zero por padrão.
   - Status: config migrada inclui `curator.consolidate: false` conforme staging.
   - Ação: manter consolidação LLM opt-in; rodar `curator status`/`backup` quando necessário.

5. Security/reliability fixes gerais.
   - Status: herdados pela versão instalada.
   - Ação: monitorar watchdogs e logs; sem mudança de política.

### B. Adotar agora com segurança local/read-only/documental

1. Background subagents.
   - Ação: atualizar práticas de Hermes Geral: usar `delegate_task(background=true)` para research/build longo sem travar Telegram.
   - Guardrail: background só para tarefas sem input interativo e sem side effects externos não aprovados.
   - Verificação: disparar uma tarefa local/read-only curta e confirmar retorno assíncrono em sessão futura ou quando fizer sentido.

2. Image-to-image/editing.
   - Ação: documentar uso para LK/Zipper como preview local de criativo, nunca como publicação automática.
   - Guardrail: geração/edição local OK; uso externo/anúncio/site/Klaviyo/Shopify exige aprovação.

3. MCP catalog/install readiness.
   - Ação: inventariar catálogo e MCPs já configurados; instalar apenas MCPs que resolvem gaps reais.
   - Guardrail: MCP com OAuth, pagamento, terminal, stdio suspeito ou write externo exige approval packet.

4. Dashboard local-only evaluation.
   - Ação: testar dashboard em `127.0.0.1`/porta local ou status, sem `--insecure` e sem Traefik.
   - Guardrail: público/Traefik/API remoto é A3/A4 separado.

5. Skills Hub rehaul.
   - Ação: usar preview/security scan antes de instalar skills; atualizar skill de Hermes com adoption notes.
   - Guardrail: instalação de skill/plugin com permissões amplas requer revisão.

6. Automation Blueprints.
   - Ação: verificar comandos/catálogos disponíveis; transformar automações recorrentes em blueprints/documentação antes de criar cron novo.
   - Guardrail: cron novo/cadência nova exige escopo, kill criteria e silent-OK.

7. Session/search/file extraction improvements.
   - Ação: usar leitura nativa de `.ipynb`, `.docx`, `.xlsx` e search_files densificado em auditorias.

### C. Adotar com aprovação escopada/credencial/infra

1. Hermes Desktop remoto.
   - Objetivo: usar Desktop como cliente do Hermes VPS/Telegram.
   - Caminho seguro: API raw host-local + SSH tunnel; não expor publicamente.
   - Requer: confirmar API key via Doppler/secret local sem imprimir; instruções para Mac; teste `/health`/modelo.
   - Bloqueado sem: escopo de acesso do Mac/SSH e decisão se quer Desktop como cockpit.

2. Dashboard operacional/profile builder.
   - Objetivo: cockpit para perfis, skills, MCPs, cron.
   - Caminho seguro: primeiro local-only/SSH tunnel; depois, se necessário, público com auth forte.
   - Requer aprovação separada para Traefik/public URL/container/reverse proxy.

3. WhatsApp Business Cloud API oficial.
   - Objetivo: substituir/alternar bridge por caminho oficial Meta quando houver caso real.
   - Requer: Meta Business, phone number id, access token, verify token, webhook público, política de atendimento.
   - Guardrail: não enviar mensagens nem configurar webhook público sem PRD e approval.

4. iMessage via Photon Spectrum.
   - Objetivo: canal iMessage sem Mac relay.
   - Requer: `hermes photon setup`, device-code login, projeto Photon/sidecar, allowlist.
   - Guardrail: canal pessoal externo; precisa decisão de uso e privacy policy.

5. Raft agent network.
   - Objetivo: Hermes como agente externo em rede Raft.
   - Requer: `RAFT_PROFILE`, bridge, contrato de privacidade, teste de wake payload metadata-only.
   - Guardrail: não ativar sem caso de uso claro.

6. xAI Grok Composer.
   - Objetivo: fast coding model via xAI/Grok OAuth/API.
   - Evidência: `XAI_API_KEY` presente no Doppler candidate probe.
   - Próximo: smoke read-only/model-picker antes de trocar qualquer default.
   - Guardrail: não mudar modelo default dos perfis sem smoke + rollback.

7. Managed scope `/etc/hermes`, gateway multiplex, Chronos managed cron, gateway-gateway relay.
   - Objetivo: operação de frota/multi-profile mais centralizada.
   - Guardrail: alto impacto em runtime; primeiro estudo/PoC local, depois aprovação infra.

### D. Não adotar literalmente agora / apenas manter conhecimento

- Cron per-job profile support: release notes dizem que foi revertido, portanto não é shipping.
- `html-artifact` skill revertido: não adotar como feature v0.17.
- Novos canais que não têm caso de uso imediato devem ficar em backlog com approval packet.

## Plano de execução por ondas

### Onda 0 — Fechamento da atualização base

Status: concluída.

- Runtime default v0.17 ativo.
- Receipt de ativação salvo.
- PRD de adoção criado.

### Onda 1 — Adoção local segura sem novo restart sensível

Objetivo: absorver tudo que não exige secrets, canal externo, Docker/VPS/Traefik ou write externo.

Tarefas:
1. Atualizar skill/reference Hermes com policy de adoção v0.17 para Lucas.
2. Criar rotina interna de uso de background subagents para pesquisas/builds longos.
3. Criar referência de image-to-image para criativos LK/Zipper em modo preview.
4. Verificar `curator status` e confirmar consolidação LLM off por padrão.
5. Inventariar MCP catalog e skills hub apenas em modo read-only/list.
6. Testar dashboard local status/help sem exposição pública.
7. Criar relatório local de adoção sem Telegram spam.

Critério de aceite:
- Artefatos Brain/skills atualizados.
- Nenhum segredo impresso.
- Nenhum canal externo ativado.
- Nenhum Docker/VPS/Traefik alterado.

### Onda 2 — Desktop/Dashboard control surface

Objetivo: transformar v0.17 em melhor superfície operacional para Lucas.

Tarefas:
1. Preparar packet Desktop remoto via SSH tunnel.
2. Preparar packet dashboard local-only.
3. Definir se Mission Control continua camada executiva e dashboard Hermes vira camada técnica/admin.
4. Só depois considerar public dashboard/Traefik.

Requer aprovação antes de qualquer exposição pública.

### Onda 3 — Canais novos

Objetivo: adotar iMessage, WhatsApp Cloud, Raft e SimpleX somente com caso de uso e governança.

Sequência recomendada:
1. WhatsApp Cloud: PRD de canal oficial Meta antes de credenciais/webhook.
2. Photon/iMessage: PRD pessoal/allowlist antes de login.
3. Raft: PoC metadata-only antes de conectar à rede.
4. SimpleX: avaliar necessidade real.

### Onda 4 — Modelos/provedores

Objetivo: aproveitar xAI Grok Composer e novos catálogos sem quebrar runtime.

Tarefas:
1. Smoke read-only do xAI/Grok com `XAI_API_KEY` presente.
2. Testar Composer em perfil/CLI isolado.
3. Definir se vira ferramenta de coding fast-lane, não default global.
4. Manter `gpt-5.5`/modelo forte como default até prova real.

### Onda 5 — Fleet/infra avançada

Objetivo: avaliar managed scope, gateway multiplex, Chronos, gateway relay.

Tarefas:
1. Estudo técnico/risco.
2. PoC isolada.
3. Approval packet para runtime/infra.
4. Backup/rollback + janela de restart.

## Backlog operacional imediato

- [ ] Atualizar skill `hermes-agent` com “Lucas v0.17 adoption policy”.
- [ ] Criar reference `hermes-v017-adoption-lucas-20260622.md` em skill/runtime.
- [ ] Rodar `curator status` e registrar sem Telegram se OK.
- [ ] Rodar `hermes mcp catalog`/list read-only e registrar MCP candidates úteis.
- [ ] Avaliar dashboard local status sem exposição pública.
- [ ] Smoke xAI/Grok sem trocar default.
- [ ] Criar approval packet Desktop/Dashboard, se Lucas quiser seguir essa frente primeiro.
- [ ] Criar approval packet WhatsApp Cloud, se Lucas quiser priorizar canal oficial.
- [ ] Criar approval packet Photon/iMessage, se Lucas quiser canal pessoal.

## Pergunta de priorização para Lucas

Como Lucas pediu “todas”, a adoção deve seguir em paralelo onde seguro e em pacotes onde sensível. A primeira decisão real é escolher a frente sensível prioritária:

1. Desktop/Dashboard como cockpit operacional.
2. WhatsApp Business Cloud API oficial.
3. iMessage/Photon.
4. xAI/Grok Composer para coding fast-lane.
5. MCP/Skills Hub expansion.

Até essa decisão, a Onda 1 pode seguir autonomamente por ser local/read-only/documental.

## Não-ações desta PRD

- Não alterou Docker/VPS/Traefik.
- Não expôs dashboard/API publicamente.
- Não ativou WhatsApp Cloud, iMessage/Photon, Raft ou SimpleX.
- Não criou cron novo.
- Não trocou modelo default.
- Não imprimiu secrets.

`values_printed=false`
