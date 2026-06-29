# Fase 2 — Hermes Central Integration Auth Broker — broker patch — 2026-06-28

- Criado em: 2026-06-28T15:07:56Z
- Escopo aprovado: patch local do broker `hermes_cli_run.py` + testes/smokes
- External writes: 0
- values_printed: false

## Mudanças implementadas

- Registry declarativo `IntegrationPolicy`.
- Denylist de login/auth interativo para `shopify login`, `shopify auth`, `shopify store auth` e `hermes mcp login`.
- Gate de mutation Shopify: bloqueia GraphQL `mutation` sem `--allow-mutations` + referência de aprovação.
- Lock por integração para Shopify e wrapper legado Shopify Admin GraphQL.
- `--audit-json` sanitizado com `values_printed=false`.
- Testes unitários em `/opt/data/scripts/tests/test_hermes_cli_run.py`.

## Arquivos alterados/criados

- Modificado: `/opt/data/scripts/hermes_cli_run.py`
- Criado: `/opt/data/scripts/tests/test_hermes_cli_run.py`
- Backup pré-patch: `/opt/data/backups/hermes-cli-run-pre-auth-broker-20260628T145647Z.py`

## Verificações

### py_compile
- Command: `python3 -m py_compile /opt/data/scripts/hermes_cli_run.py /opt/data/scripts/tests/test_hermes_cli_run.py`
- Exit code: `0`

### unit_tests
- Command: `python3 -m unittest /opt/data/scripts/tests/test_hermes_cli_run.py -v`
- Exit code: `0`
- Stderr sanitizado:
```text
test_allow_mutation_requires_approval_reference (scripts.tests.test_hermes_cli_run.HermesCliRunPolicyTests.test_allow_mutation_requires_approval_reference) ... ok
test_audit_json_emits_sanitized_audit_record_for_read_only_command (scripts.tests.test_hermes_cli_run.HermesCliRunPolicyTests.test_audit_json_emits_sanitized_audit_record_for_read_only_command) ... ok
test_blocks_shopify_mutation_without_allow_flag (scripts.tests.test_hermes_cli_run.HermesCliRunPolicyTests.test_blocks_shopify_mutation_without_allow_flag) ... ok
test_blocks_shopify_store_auth_without_executing_cli (scripts.tests.test_hermes_cli_run.HermesCliRunPolicyTests.test_blocks_shopify_store_auth_without_executing_cli) ... ok
test_read_only_shopify_command_still_executes (scripts.tests.test_hermes_cli_run.HermesCliRunPolicyTests.test_read_only_shopify_command_still_executes) ... ok

----------------------------------------------------------------------
Ran 5 tests in 0.011s

OK
```

### deny_store_auth
- Command: `/opt/data/home/.local/bin/hermes-cli-run shopify store auth --store lk-sneakerss.myshopify.com`
- Exit code: `64`
- Stderr sanitizado:
```text
policy_blocked: direct interactive/auth command is not allowed via agents: shopify store auth
```

### mutation_block
- Command: `/opt/data/home/.local/bin/hermes-cli-run shopify store execute --store lk-sneakerss.myshopify.com --json --query mutation { __typename }`
- Exit code: `64`
- Stderr sanitizado:
```text
mutation_blocked: Shopify GraphQL mutation requires --allow-mutations and scoped approval reference
```

### audit_readonly
- Command: `/opt/data/home/.local/bin/hermes-cli-run --audit-json shopify store execute --store lk-sneakerss.myshopify.com --json --query { shop { name myshopifyDomain } }`
- Exit code: `0`
- Stdout sanitizado:
```text
{
  "shop": {
    "name": "LK",
    "myshopifyDomain": "lk-sneakerss.myshopify.com"
  }
}
{"command_family": "store execute", "deprecated": false, "exit_code": 0, "integration": "shopify", "mode": "read_only", "secret_values_printed": false, "status": "ok", "values_printed": false}
```
- Stderr sanitizado:
```text
Loading stored store auth ...
[2K[1A[2K[G
Executing GraphQL operation ...
[2K[1A[2K[G
```

### smoke_shopify
- Command: `/opt/data/home/.local/bin/hermes-cli-integrations smoke shopify_lk`
- Exit code: `0`
- Stdout sanitizado:
```text
{
  "results": {
    "shopify_lk": {
      "method": "shopify_store_execute",
      "rc": 0,
      "status": "ok"
    }
  },
  "values_printed": false
}
```

### smoke_selected
- Command: `/opt/data/home/.local/bin/hermes-cli-integrations smoke shopify_lk github notion google_workspace klaviyo supabase`
- Exit code: `0`
- Stdout sanitizado:
```text
{
  "results": {
    "github": {
      "method": "gh_api",
      "rc": 0,
      "status": "ok"
    },
    "google_workspace": {
      "method": "gws_gmail_users_getProfile",
      "rc": 2,
      "status": "failed"
    },
    "klaviyo": {
      "method": "klaviyo_get_flows_stdout",
      "rc": 124,
      "status": "failed"
    },
    "notion": {
      "method": "ntn_whoami",
      "rc": 0,
      "status": "ok"
    },
    "shopify_lk": {
      "method": "shopify_store_execute",
      "rc": 0,
      "status": "ok"
    },
    "supabase": {
      "project_count": null,
      "rc": 0,
      "status": "ok"
    }
  },
  "values_printed": false
}
```

## Secret scan

- Files checked: 2
- Real secret findings: 0
- values_printed: false

## Observações

- `google_workspace` permanece `rc=2` no smoke selecionado; item separado de health, não causado pelo patch Shopify broker.
- `shopify_lk` segue OK pelo caminho oficial `shopify store execute`.
- Mutation e auth interativo foram bloqueados localmente antes de execução externa.
