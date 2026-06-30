# Auditoria provider authentication — todos os agentes Hermes — 2026-06-30

- generated_at_utc: `2026-06-30T16:59:26Z`
- pedido: `⚠️ Provider authentication failed... auditar todos os agentes`
- escopo: read-only/sanitizado; nenhum restart, nenhuma cópia de credencial, nenhum Docker/VPS/Traefik, nenhum write externo
- values_printed: false

## Conclusão executiva

A falha **atual e reproduzível em log** foi encontrada no profile `lk-ops`: `openai-codex` retornou HTTP 401 / `token_expired` em `2026-06-30 16:47–16:48 UTC`.

Outros profiles têm histórico antigo de 401 ou `auth.json` divergente, mas sem evidência atual equivalente nesta auditoria. Vários smokes retornaram `OK` antes de um `rc=134`, que foi classificado como **modelo funcionando com abort/shutdown não fatal** conhecido do Hermes v0.17 CLI.

## Matriz resumida

| Profile | Live gateways | Auth/config evidence | Smoke atual | Classificação |
|---|---:|---|---|---|
| `default` | 2 | codex_pool_hash=51e2e5091ab2; matches_default=True | `OK_output; rc=134` | **FUNCTIONING_NOW** |
| `brain-process` | 0 | codex_pool_hash=80b5efb18326; matches_default=False; stale_provider_block_present=true | `no_final_response; rc=1` | **DORMANT_OR_SUPPORT; historical only** |
| `hermes-ops-readonly` | 0 | codex_pool_hash=6d6e9d8b3302; matches_default=False | `no_final_response; rc=1` | **DORMANT_OR_SUPPORT; historical only** |
| `lc-claude-cli` | 1 | sem pool local ou não aplicável | `timeout` | **INCONCLUSIVE_NO_CURRENT_401** |
| `lk-analyst-readonly` | 0 | codex_pool_hash=6d6e9d8b3302; matches_default=False | `no_final_response; rc=1` | **DORMANT_OR_SUPPORT; historical only** |
| `lk-collection-optimizer` | 1 | sem pool local ou não aplicável | `OK_output; rc=134` | **FUNCTIONING_NOW** |
| `lk-content` | 1 | sem pool local ou não aplicável | `OK_output; rc=134` | **FUNCTIONING_NOW** |
| `lk-content-reviewer` | 0 | codex_pool_hash=6d6e9d8b3302; matches_default=False | `no_final_response; rc=1` | **DORMANT_OR_SUPPORT; historical only** |
| `lk-finance` | 1 | sem pool local ou não aplicável | `OK_output; rc=134` | **FUNCTIONING_NOW** |
| `lk-growth` | 1 | codex_pool_hash=a60c231b87b3; matches_default=False; stale_provider_block_present=true | `OK_output; rc=134` | **FUNCTIONING_NOW** |
| `lk-ops` | 1 | codex_pool_hash=8f5ea53eb3e3; matches_default=False; stale_provider_block_present=true | `no_final_response; rc=1` | **CURRENT_AUTH_FAIL** |
| `lk-shopify` | 1 | codex_pool_hash=51e2e5091ab2; matches_default=True | `OK_output; rc=134` | **FUNCTIONING_NOW** |
| `lk-stock` | 1 | codex_pool_hash=69af524af031; matches_default=False | `OK_output; rc=134` | **FUNCTIONING_NOW** |
| `lk-trends` | 1 | codex_pool_hash=6d6e9d8b3302; matches_default=False | `no_final_response; rc=1` | **INCONCLUSIVE_NO_CURRENT_401** |
| `mordomo` | 1 | codex_pool_hash=2310c22848d5; matches_default=False; stale_provider_block_present=true | `OK_output; rc=134` | **FUNCTIONING_NOW** |
| `spiti` | 1 | codex_pool_hash=48131cdf6207; matches_default=False; stale_provider_block_present=true | `no_final_response; rc=1` | **INCONCLUSIVE_NO_CURRENT_401** |
| `spiti-atendimento` | 1 | sem pool local ou não aplicável | `OK_output; rc=134` | **FUNCTIONING_NOW** |

## Evidência do caso atual — lk-ops

- log profile: `/opt/data/profiles/lk-ops/logs/agent.log`
- timestamp observado: `2026-06-30 16:47:59–16:48:00 UTC`
- provider/model: `openai-codex` / `gpt-5.5`
- erro sanitizado: `HTTP 401`, `token_expired`, `No Codex OAuth token found`, `Fallback ... provider not configured`
- `auth.json` do `lk-ops`: `credential_pool.openai-codex` diverge do default e existe bloco local `providers.openai-codex`; valores não impressos

## Causa provável

O `lk-ops` está sombreando ou usando credencial Codex profile-local expirada/divergente. O default responde `OK`; o profile `lk-ops` tem hash de credential pool diferente e provider block local. Isso casa com o padrão já documentado de reparo `profile-codex-default-auth-sync` / `lk-shopify-codex-auth-sync-runtime-fix`.

## Não classificados como falha atual

- `hermes-ops-readonly`, `lk-analyst-readonly`, `lk-content-reviewer`: logs de 25/06 com 401; sem gateway vivo; classificar como histórico/dormant até alguém usar.
- `lk-trends`, `spiti`: smoke CLI retornou `no final response`, mas logs recentes não mostram 401 atual; precisa observação se o usuário reportar falha nesses bots.
- `lk-growth`, `lk-shopify`, `lk-stock`, `lk-content`, `lk-finance`, `mordomo`, `spiti-atendimento`, `lk-collection-optimizer`, `default`: smoke produziu `OK`; rc 134 tratado como warning de shutdown CLI, não falha de provider.

## Correção proposta — pendente de aprovação

Para `lk-ops` somente:
1. backup de `/opt/data/profiles/lk-ops/auth.json` e `config.yaml`;
2. copiar **somente** `credential_pool.openai-codex` do default para o `lk-ops`;
3. remover `providers.openai-codex` local se default não tiver equivalente;
4. rodar smoke profile-local;
5. reiniciar **somente** o gateway `lk-ops`;
6. verificar PID/env booleans, Telegram connected, API/Webhook off, `DOPPLER_TOKEN` ausente, e log sem 401 novo;
7. receipt sanitizado.

Não executar batch global agora: há divergências de hash em outros profiles, mas sem falha atual; copiar credenciais em massa sem necessidade aumentaria blast radius.
