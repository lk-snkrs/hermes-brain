# PRD — Hermes Central Integration Auth Broker — 2026-06-28

- **Status:** PRD v1 aprovado para documentação / aguardando aprovação separada para implementação runtime
- **Owner:** Operações Hermes / Integrações
- **Solicitante:** Lucas Cimino
- **Criado em:** 2026-06-28T14:47:40Z
- **Classificação:** arquitetura operacional / segurança de integrações
- **values_printed:** false
- **External writes:** 0
- **Secrets/tokens impressos:** 0

## 1. Resumo executivo

O problema atual é arquitetural: agentes Hermes especializados estão sendo levados a autenticar individualmente CLIs, MCPs e integrações como Shopify CLI. Isso cria duplicidade, drift entre profiles, risco de secrets espalhados, sessões OAuth inconsistentes e manutenção manual por agente.

A correção proposta é criar um **Hermes Central Integration Auth Broker**: uma camada central de execução autenticada, com secrets resolvidos por Doppler no momento do comando, estado de login CLI centralizado e auditável, política read-only/write-gated por integração, logs sanitizados e contratos claros para agents, subagents e crons.

A ideia central: **centralizar execução autenticada, não copiar arquivos de token entre profiles**.

## 2. Contexto e evidência

### 2.1 Evidência interna já existente

- Política vigente: `areas/operacoes/rotinas/cli-mcp-first-integration-policy.md`.
- Shopify CLI oficial autorizado para `lk-sneakerss.myshopify.com` em `reports/governance/shopify-official-oauth-2026-06-27.md`.
- Regra canônica atual no Brain/AGENTS: leituras Shopify Admin GraphQL devem usar:

```bash
/opt/data/home/.local/bin/hermes-cli-run shopify store execute --store lk-sneakerss.myshopify.com --json --query '<GraphQL>'
```

- Receipt anterior: `areas/operacoes/receipts/shopify-cli-auth-bridge-20260627.md` registrou a ponte Shopify Doppler-first e o bloqueio de mutations por padrão.
- Gateway main/default já foi reiniciado e validado em 2026-06-28 para carregar a política Shopify CLI oficial.

### 2.2 Pesquisa em documentação oficial Hermes

A documentação oficial do Hermes confirma estes pontos relevantes:

| Recurso Hermes | Comportamento documentado | Implicação para este PRD |
|---|---|---|
| Profiles | Cada profile tem seu próprio `config.yaml`, `.env`, `auth.json`, MCP tokens, sessões, memória e estado. | Profiles são isolados por design; não devemos depender de login individual por profile para integrações compartilhadas. |
| `terminal.home_mode` | No backend local, `auto` preserva o `HOME` real para subprocessos; `profile` usa `{HERMES_HOME}/home`. | Para CLIs compartilhadas, o modo real/auto permite um auth home central; `profile` força isolamento e tende a exigir login por agente. |
| MCP | MCPs podem usar stdio/HTTP; OAuth HTTP salva tokens em `~/.hermes/mcp-tokens/<server>.json`; `${ENV_VAR}` é resolvido no connect. | MCP direto por profile ainda pode duplicar tokens; MCP sensível deve ser centralizado ou ter ownership explícito. |
| `hermes auth` / Credential Pools | Pools são para provedores LLM; compartilham pool com `delegate_task` children. | Resolve subagents do mesmo runtime/provedor, mas não resolve CLIs/MCPs genéricos entre profiles independentes. |
| Secrets | Hermes suporta secret managers externos no startup; hoje oficial: Bitwarden; arquitetura permite backends. | Nosso padrão local continua Doppler-first via `/opt/data/scripts/hermes_doppler.py`; não copiar secrets para `.env` dos profiles. |
| Managed Scope | `/etc/hermes` pode pinçar config/env por máquina, mas managed `.env` é world-readable no modelo v1. | Útil para policy/config não sensível; inadequado como cofre de secrets. |

## 3. Problema

### 3.1 Sintomas

- Cada profile/agente tenta autenticar Shopify CLI, MCPs ou CLIs próprias.
- Mesma integração passa por rotas diferentes: CLI oficial, wrapper legado, raw HTTP, MCP, `.env` local ou token cache privado.
- OAuth expira ou falta em apenas um agente, gerando falhas inconsistentes.
- Secrets e estado de auth podem ser copiados manualmente para profiles.
- Crons e subagents podem divergir da política `CLI/MCP-first`.
- Fica difícil responder: “qual credencial está em uso?”, “onde está logado?”, “quem pode escrever?”, “o que rodou?”.

### 3.2 Causa raiz

O Hermes usa profiles isolados por design. Esse isolamento é correto para memória, identidade, skills e cron state, mas não deve virar **fragmentação de credenciais operacionais compartilhadas**. Integrações empresariais precisam de um plano de controle central.

## 4. Objetivos

1. Centralizar login/estado de execução de CLIs e MCPs governados.
2. Fazer todos os agents, subagents e crons usarem uma interface única para integrações autenticadas.
3. Manter Doppler `lc-keys/prd` como fonte de verdade de secrets.
4. Impedir que agents façam `shopify login`, `hermes mcp login`, OAuth ou cópia de token por conta própria fora de exceção aprovada.
5. Garantir logs sanitizados e `values_printed=false`.
6. Preservar isolamento de profiles para memória/config/skills, mas remover drift de autenticação.
7. Bloquear writes externos por padrão e exigir aprovação escopada + rollback/readback.

## 5. Não objetivos

- Não criar um cofre de secrets alternativo ao Doppler.
- Não copiar `DOPPLER_TOKEN`, Shopify tokens, `auth.json`, `.env`, `mcp-tokens` ou caches OAuth para todos os profiles.
- Não symlinkar indiscriminadamente diretórios internos de auth entre profiles.
- Não substituir a arquitetura de profiles do Hermes.
- Não liberar mutation/write Shopify automaticamente.
- Não usar Managed Scope `/etc/hermes/.env` para secrets sensíveis.

## 6. Proposta de produto

Criar o **Hermes Central Integration Auth Broker**, composto por quatro camadas:

```text
Agents / Subagents / Crons
        |
        v
Policy Contract: "não login direto; use broker"
        |
        v
hermes-cli-run / integration broker
        |-------------------------------|
        |                               |
        v                               v
Doppler Secret Resolver          Central CLI/Auth Home
(process-scoped env)             (OAuth/cache CLI controlado)
        |                               |
        |-------------------------------|
        v
Official CLI / Governed MCP / Exception Raw API
        |
        v
Sanitized output + audit receipt + readback
```

## 7. Arquitetura funcional

### 7.1 Central CLI/Auth Home

Um local controlado, pertencente ao runtime Hermes, mantém estado de login para CLIs que dependem de cache local/OAuth, por exemplo Shopify CLI.

**Diretriz:** agents não acessam nem editam esse estado diretamente. Eles executam por wrapper central.

Requisitos:

- Permissões restritas (`0600` para arquivos sensíveis; diretórios `0700` quando aplicável).
- Inventário de arquivos e CLIs que usam o auth home central.
- Health/smoke read-only periódico.
- Lock por integração quando o CLI não for seguro para concorrência.

### 7.2 Broker/wrapper único

Base atual: `/opt/data/home/.local/bin/hermes-cli-run` → `/opt/data/scripts/hermes_cli_run.py`.

Evoluir para contrato formal:

```bash
hermes-cli-run <integration> <command...>
```

Exemplos:

```bash
hermes-cli-run shopify store execute --store lk-sneakerss.myshopify.com --json --query '<GraphQL>'
hermes-cli-run gh auth status
hermes-cli-run vercel whoami
hermes-cli-run supabase db query --linked --file /path/query.sql
```

Responsabilidades do broker:

- Resolver aliases de env por integração.
- Chamar Doppler-first sem imprimir valores.
- Redigir stdout/stderr.
- Aplicar allow/deny rules por integração.
- Bloquear comandos interativos/login por agents.
- Bloquear mutations/writes sem flag + approval packet.
- Gerar audit log sanitizado.
- Retornar códigos de erro classificados.

### 7.3 Doppler Secret Resolver

Fonte de verdade continua:

```bash
/opt/data/scripts/hermes_doppler.py run -- <command>
```

Contrato:

- Secrets existem no Doppler `lc-keys/prd`.
- Wrapper injeta env temporário só no subprocesso.
- Não gravar valores em `.env`, Brain, receipts, logs ou Telegram.
- Readback reporta apenas presença/ausência/status, nome do secret e `values_printed=false`.

### 7.4 MCP Centralization

MCPs devem seguir três padrões, em ordem:

1. **MCP tool nativo já exposto no profile atual:** usar se read-only e governado.
2. **MCP central/brokered:** quando tokens/OAuth/estado devem ser compartilhados.
3. **MCP login por profile:** só por exceção documentada quando a integração é realmente profile-specific.

Regras:

- Não fazer `hermes mcp login <server>` em cada agente como rotina normal.
- Para OAuth MCP remoto sensível, definir um owner central e arquivo de token controlado.
- Se o MCP só existe no profile especialista, o orchestrator deve chamar o especialista como executor, não duplicar login.

### 7.5 Policy contract para agents

Adicionar aos prompts/skills/rotinas relevantes:

- Para Shopify/Admin GraphQL: usar Shopify CLI oficial via `hermes-cli-run shopify store execute` primeiro.
- Proibido executar login interativo por iniciativa própria.
- Proibido copiar token/cache de auth.
- Raw API apenas como exceção aprovada e justificada.
- Writes externos exigem aprovação escopada, rollback e readback.

## 8. Requisitos funcionais

### RF1 — Inventário central

O sistema deve listar integrações conhecidas, status de CLI instalada, status de secret no Doppler, status de autenticação read-only e owner.

Comando base existente:

```bash
/opt/data/home/.local/bin/hermes-cli-integrations inventory
```

### RF2 — Smoke central read-only

O sistema deve validar integrações sem side effects:

```bash
/opt/data/home/.local/bin/hermes-cli-integrations smoke
/opt/data/home/.local/bin/hermes-cli-integrations smoke shopify_lk github notion google_workspace klaviyo supabase
```

### RF3 — Execução centralizada

Todos os agents devem chamar integrações por:

```bash
/opt/data/home/.local/bin/hermes-cli-run <cli> <args...>
```

ou ferramenta MCP nativa governada.

### RF4 — Shopify CLI oficial

Para Shopify LK:

```bash
/opt/data/home/.local/bin/hermes-cli-run shopify store execute --store lk-sneakerss.myshopify.com --json --query '<GraphQL>'
```

- Read-only permitido.
- Mutations bloqueadas sem approval e `--allow-mutations`.
- Wrapper/raw API são fallback/incidente aprovado.

### RF5 — Bloqueio de login direto

Agents não devem rodar:

```bash
shopify login
shopify store auth
hermes mcp login <server>
```

sem task/approval específico de reauth.

### RF6 — Auditoria

Cada execução material deve registrar:

- integration name;
- command family;
- read-only vs write;
- status/exit code;
- secrets present/absent, sem valores;
- `values_printed=false`;
- se houve raw API exception;
- artifact/receipt quando relevante.

### RF7 — Concorrência e lock

Para CLIs com cache OAuth/state local, o broker deve usar lock por integração/store para evitar corrupção/condição de corrida.

Exemplo conceitual:

```text
/opt/data/runtime/locks/integrations/shopify_lk.lock
```

### RF8 — Reauth controlado

Quando auth expirar:

1. Smoke classifica `auth_expired`.
2. Broker bloqueia writes e login automático.
3. Gera approval packet de reauth.
4. Lucas aprova janela/escopo.
5. Operador executa login interativo uma vez no auth home central.
6. Smoke/readback confirma.

## 9. Requisitos não funcionais

| Categoria | Requisito |
|---|---|
| Segurança | Nenhum secret impresso; redaction obrigatória; permissões restritas; sem cópia para profiles. |
| Auditabilidade | Toda mudança de política/auth tem receipt ou approval packet. |
| Confiabilidade | Smokes read-only antes/depois de mudanças; rollback local claro. |
| Compatibilidade Hermes | Respeitar profiles isolados; usar `terminal.home_mode` conscientemente; não hackear internals sem necessidade. |
| Observabilidade | Status por integração, último smoke, causa sanitizada de falha. |
| Operação Telegram | Silent-OK; alertar só falha acionável, expiração auth, aprovação necessária ou write gate. |

## 10. Modelo de permissões

### Leitura A0/A1 permitida

- `whoami`, `auth status`, `store execute` read-only, listagens, health checks.
- Sem approval individual, desde que via broker e sem impressão de secret.

### Write A2/A3/A4 bloqueado por padrão

Exige:

- escopo claro;
- payload/diff;
- approval packet;
- rollback plan;
- readback pós-write;
- receipt.

### Login/reauth

Login interativo é mudança sensível de runtime/auth. Exige approval packet, mesmo se não houver write externo de negócio.

## 11. Migração proposta

### Fase 0 — PRD e freeze de abordagem

- Aprovar este PRD.
- Declarar regra: não autenticar agents individualmente.
- External writes: 0.

### Fase 1 — Inventário e detecção de drift

- Rodar inventory/smoke read-only.
- Procurar uso de login direto, raw Shopify Admin HTTP e `mcp login` em scripts/skills/crons/prompts.
- Classificar: canônico, fallback, exceção, obsoleto.

### Fase 2 — Endurecer broker

Evoluir `hermes_cli_run.py` com:

- registry declarativo de integrações;
- bloqueio de comandos de login direto por default;
- lock por integração;
- allowlist/denylist por CLI;
- modo `--audit-json` sanitizado;
- classificação de erro (`missing_secret`, `cli_missing`, `auth_expired`, `write_blocked`, `ok`).

### Fase 3 — Policy propagation

- Atualizar skills/AGENTS/cron prompts relevantes.
- Padronizar contrato de `integration_access_path` em receipts.
- Garantir que subagents recebam a regra Doppler-first/CLI-broker.

### Fase 4 — Readback e validação

- Smoke central read-only.
- Smoke Shopify LK read-only.
- Teste de mutation bloqueada sem approval.
- Teste de login direto bloqueado por policy.
- Secret scan dos artefatos.

### Fase 5 — Operação contínua

- Watchdog de auth drift silent-OK.
- Alerta Telegram só quando houver ação requerida.
- Receipt mensal/por mudança relevante.

## 12. Critérios de aceite

- [ ] Nenhum agente precisa autenticar Shopify CLI individualmente.
- [ ] Shopify Admin GraphQL read-only funciona via `hermes-cli-run shopify store execute`.
- [ ] Mutations Shopify sem approval são bloqueadas.
- [ ] Login direto por agente é bloqueado ou explicitamente classificado como exceção aprovada.
- [ ] Inventory central mostra CLI instalado, secret presente/ausente, auth read-only OK/falha.
- [ ] Smokes não imprimem secrets (`values_printed=false`).
- [ ] Não há secrets copiados para `.env` de profiles especialistas.
- [ ] MCPs sensíveis têm owner central ou justificativa de profile-specific.
- [ ] Receipts materiais incluem `integration_access_path`.
- [ ] Rollback documentado e testado localmente.

## 13. Riscos e mitigação

| Risco | Mitigação |
|---|---|
| Broker vira single point of failure | Fallback governado com modo read-only e rollback para versão anterior. |
| OAuth expira | Health/smoke detecta; reauth com approval packet. |
| Concorrência corrompe cache CLI | Locks por integração/store. |
| Profiles precisam de identidades diferentes | Permitir exceção profile-specific documentada. |
| Managed Scope expõe secret se mal usado | Não usar managed `.env` para secrets sensíveis. |
| Raw API volta por conveniência | Gate obrigatório: CLI/wrapper → MCP → raw exception com justificativa. |
| Agente imprime token por erro | Redaction central + secret scan de receipts/reports. |

## 14. Rollback

Rollback de implementação local:

1. Restaurar `/opt/data/scripts/hermes_cli_run.py` do backup pré-mudança.
2. Remover apenas novos policy files se causarem problema.
3. Manter OAuth/login oficial Shopify intacto, salvo se uma mudança específica nele for aprovada para reversão.
4. Rodar smoke read-only pós-rollback.
5. Registrar receipt com `values_printed=false`.

## 15. Decisões pendentes para implementação runtime

Antes de alterar código/runtime, Lucas deve aprovar separadamente:

1. Criar lock/audit state local em `/opt/data/runtime/integrations/`?
2. Bloquear hard `shopify login/store auth` no wrapper ou apenas em policy/lint inicialmente?
3. Centralizar MCP OAuth por broker agora ou deixar para fase 2 após inventory?
4. Reiniciar gateway depois de mudanças de prompt/skills, se necessário?

## 16. Recomendação

Seguir com implementação incremental segura:

1. Primeiro: inventory + detection + PRD/plan/receipts.
2. Depois: endurecer `hermes-cli-run` localmente com testes e backup.
3. Só então: propagar policy para crons/skills/prompts e reiniciar runtimes com approval quando necessário.

**Decisão de arquitetura:** usar recursos nativos Hermes (`HOME` real/`terminal.home_mode`, MCP config, `hermes auth` onde aplicável, secret manager pattern) sem quebrar isolamento de profiles; centralizar o controle no broker/wrapper e no Doppler, não em cópias de token.
