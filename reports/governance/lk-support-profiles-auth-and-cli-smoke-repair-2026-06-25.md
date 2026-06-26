# LK support profiles — auth repair + CLI smoke/core-dump investigation (2026-06-25)

Generated at: `2026-06-25T18:55:00Z`

## Pedido

Lucas pediu “fazer 1 e 2” após a Fase 2 dos agents LK:

1. investigar/corrigir a lacuna `exit 134/core dumped` do Hermes CLI smoke;
2. corrigir `HTTP 401 token_expired` em `lk-analyst-readonly` e `lk-content-reviewer`.

## Escopo

Perfis afetados:

- `lk-analyst-readonly`
- `lk-content-reviewer`

Não foi feito:

- Docker/VPS/Traefik/Main/default restart;
- write externo em Shopify/Tiny/Klaviyo/Google/Meta/Supabase/e-mail/WhatsApp;
- exposição de secrets/token values.

## 1) Auth/token_expired — corrigido

### Evidência inicial

Os logs dos dois perfis mostravam:

```text
HTTP 401: Provided authentication token is expired
code: token_expired
```

### Ação executada

- Backup dos arquivos antes da mudança:

```text
/opt/data/backups/lk-support-profile-auth-repair-20260625T183639Z
```

- Para cada perfil:
  - `auth.json`: substituído apenas o credential pool `openai-codex` pelo pool funcional do `default`;
  - removido o bloco legado `providers.openai-codex`, que continha token/estado expirado;
  - `config.yaml`: `delegation.api_mode` alinhado com `codex_responses`;
  - `values_printed=false`.

### Resultado

Smokes reais pós-reparo responderam sem `HTTP 401`/`token_expired`, mas o processo ainda abortava no shutdown por outro bug (`exit 134`).

Smokes isolados finais com harness seguro:

```text
/opt/data/backups/lk-support-profile-identity-smoke-after-authfix-20260625T185137Z.json
```

Resultado:

| Profile | Smoke | Identidade correta |
|---|---:|---|
| `lk-analyst-readonly` | OK / rc 0 | LK Analyst Readonly |
| `lk-content-reviewer` | OK / rc 0 | LK Content Reviewer |

## 2) `exit 134/core dumped` — root cause isolado + workaround seguro criado

### Reprodução

O crash acontece mesmo no `default` com pergunta mínima:

```text
hermes chat -Q --max-turns 1 -q 'Responda apenas OK.'
# resposta: OK
# depois: Fatal Python error: Aborted
# rc=134
```

Com `--ignore-rules`, o mesmo comando retorna `rc=0`.

### Isolamento

Testes em temp profiles mostraram:

- sem `honcho.json` ou com Honcho disabled: `rc=0`;
- com `honcho.json` enabled: resposta sai correta e o processo aborta no shutdown (`rc=134`);
- `writeFrequency=async|turn|session` não elimina o abort;
- o erro ocorre depois da resposta, no caminho de finalização/cleanup do CLI, não durante a chamada do modelo.

Hipótese confirmada: **o core dump é bug do Hermes CLI single-query com Honcho enabled no caminho de shutdown/finalize**, não falha de identidade dos profiles e não falha de provider auth.

### Workaround seguro criado

Script local/read-only:

```text
/opt/data/scripts/hermes_profile_identity_smoke.py
```

Comportamento:

1. cria um `HERMES_HOME` temporário do profile;
2. copia `SOUL.md`, `AGENTS.md`, `MAPA.md`, `MEMORY.md`, `memories/`, `skills/`, `auth.json`, `config.yaml`;
3. desativa Honcho apenas na cópia temporária;
4. remove variáveis herdadas de gateway/session (`HERMES_SESSION_*`, `_HERMES_GATEWAY`, `HERMES_REAL_HOME`) para evitar contaminação de identidade;
5. roda `hermes chat -Q` no cwd temporário;
6. retorna JSON sanitizado com `values_printed=false`.

Esse script não altera o profile original e permite validar identidade/guardrails sem o core dump do Honcho CLI.

## Validações finais

- Brain health: `FAIL=0 WARN=0`.
- `hermes_profile_identity_smoke.py`: lint OK no write.
- Smokes isolados finais: `2/2 OK`, `rc=0`.
- Auth files continuam contendo secrets por natureza, mas valores não foram impressos; isso não é leak. Artefatos de smoke/report foram sanitizados.

## Pendências remanescentes

- Corrigir upstream/localmente o bug real do Hermes CLI + Honcho enabled no shutdown/finalize, idealmente com teste automatizado no código do Hermes. Isso exigiria patch no runtime Hermes e nova validação; não foi feito nesta etapa para não mexer no core/gateway além do escopo aprovado.
- Se esses support profiles precisarem virar gateways ativos, fazer activation packet separado. Nesta etapa eles continuam dormant/support.

## Conclusão

- `HTTP 401 token_expired` dos dois support profiles: **corrigido**.
- Smokes de identidade dos dois support profiles: **OK via harness seguro**.
- `exit 134/core dumped`: **root cause isolado como bug do CLI + Honcho enabled no shutdown**, com workaround seguro criado para smokes de profile. Não bloqueia gateway Telegram nem a identidade dos agentes LK ativos.
