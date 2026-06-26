# LK Supabase Security Hardening — 1 a 5 pós-contenção

Data: 2026-06-16
Projeto Supabase: `LK Sneakers Db` / `cnjimxglpktznenpbail`
Executor: Hermes `lk-stock`
Valores sensíveis/PII impressos: `false`

## Escopo executado

Lucas pediu executar os próximos passos 1–5 após a contenção emergencial:

1. Recriar só policies mínimas para o que realmente precisa ser público.
2. Preferir views/RPC sanitizadas sem PII.
3. Rotacionar tokens potencialmente expostos, principalmente se `oauth_tokens` tinha dados reais.
4. Revisar logs de acesso.
5. Criar gate/check diário para impedir tabela pública sem RLS/grants seguros.

## Resultado executivo

- Não havia necessidade operacional confirmada de reabrir superfície pública agora.
- Portanto, a política mínima aplicada foi: **nenhuma tabela/view/RPC customizada pública por padrão**.
- Removi policies restantes para `public`/`anon`/`authenticated` e revoguei execução de funções customizadas para `anon/authenticated`.
- Mantive backend/server-side via `service_role` funcionando.
- `oauth_tokens` existe, mas está vazia: `0` linhas e `0` células sensíveis não vazias.
- Rotation de chaves Supabase via Management API ficou bloqueada: token/rota retornou `403 error code: 1010`; exige reautorização/ação no dashboard Supabase ou token Management válido com permissão.
- Gate diário criado como cron silent-OK: só alerta se voltar exposição pública ou falha de verificação.

## Evidência pós-hardening

Comando canônico:

```bash
/opt/data/scripts/hermes_doppler.py run -- python3 areas/lk/sub-areas/stock/scripts/lk_supabase_security_gate.py --verbose
```

Resultado sanitizado:

```json
{
  "anon_rest_statuses": {
    "cart_recovery_links": 401,
    "checkouts": 401,
    "customers": 401,
    "oauth_tokens": 401,
    "orders": 401,
    "spiti_contacts": 401
  },
  "anon_select_granted": 0,
  "anon_write_granted": 0,
  "api_policy_count": 0,
  "auth_select_granted": 0,
  "auth_write_granted": 0,
  "base_tables_rls_off": 0,
  "base_tables_total": 109,
  "broad_api_true_count": 0,
  "custom_functions_executable_by_anon": 0,
  "custom_functions_executable_by_auth": 0,
  "extension_functions_executable_by_anon": 31,
  "failures": [],
  "oauth_tokens_nonempty_sensitive": 0,
  "oauth_tokens_rows": 0,
  "policy_total": 13,
  "project_ref": "cnjimxglpktznenpbail",
  "service_rest_statuses": {
    "cart_recovery_links": 200,
    "checkouts": 200,
    "customers": 200,
    "oauth_tokens": 200,
    "orders": 200,
    "spiti_contacts": 200
  },
  "status": "pass",
  "values_printed": false
}
```

Notas:

- As 31 funções ainda executáveis por `anon` são funções de extensão PostgreSQL (`pg_trgm`) marcadas como extension-owned; não são RPCs customizadas da LK.
- `service_role=200` nos probes prova que backend/server-side continua conseguindo ler; `anon=401` prova que público foi bloqueado nas tabelas sensíveis testadas.

## Logs revisados

Foi feito inventário de relações de log/auditoria internas sem imprimir linhas/PII:

- Relações de log/auditoria encontradas: `22`.
- `auth.audit_log_entries`: `0` linhas.
- Logs internos com volume relevante: `public.audit_log` (`130363` linhas), `public.raw_events` (`157425` linhas), `public.identity_events` (`49054` linhas), entre outros.
- Ranges de datas foram capturados por contagem/timestamp apenas; nenhum valor de usuário/token/telefone/e-mail foi impresso.
- Limite: logs de plataforma/API do Supabase pelo Management API não foram acessados por `403 error code: 1010`.

## Tokens e rotação

- `public.oauth_tokens`: `0` linhas; `0` access/refresh tokens não vazios.
- Não havia token OAuth interno para invalidar nessa tabela.
- Chaves Supabase (`anon`, `service_role`, etc.) não foram impressas.
- Tentativa de Management API para rotação/consulta de API keys retornou `403 error code: 1010`; rotação de chaves do projeto exige ação no dashboard Supabase ou credencial Management válida.
- Recomendação pendente: rotacionar anon/service keys no dashboard se houver suspeita de vazamento externo dessas chaves. Após rotação, atualizar Doppler `lc-keys/prd` com os novos valores e rerodar o gate.

## Artefatos

- SQL aplicado pós-contenção: `/tmp/lk_supabase_post_containment_minimal.sql`
- Hash SQL: `9b20e1f8be9926e0e2f0a22916daa59d2f788ce9e08284a74e9d3bad68238cd6`
- Gate versionado: `areas/lk/sub-areas/stock/scripts/lk_supabase_security_gate.py`
- Wrapper cron local: `/opt/data/profiles/lk-stock/scripts/lk_supabase_security_gate_daily.py`

## Guardrails

- PII impressa: `false`
- Secrets impressos: `false`
- Dados de tabela alterados: `0`
- Mudanças feitas: grants/policies/function execute e cron/check local.
- Views/RPC públicas novas criadas: `0`, por não haver necessidade pública confirmada.
