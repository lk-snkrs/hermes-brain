#!/usr/bin/env python3
"""LK Supabase public exposure gate.

Silent OK by default: prints nothing and exits 0 when the security posture is safe.
On failure, prints a sanitized JSON alert with counts/status only; never prints secrets or row values.
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request

PROJECT_REF = "cnjimxglpktznenpbail"
POOLER_CONN = (
    "host=aws-1-sa-east-1.pooler.supabase.com port=6543 dbname=postgres "
    "user=postgres.cnjimxglpktznenpbail sslmode=require"
)
SENSITIVE_PROBE_TABLES = [
    "customers",
    "orders",
    "oauth_tokens",
    "spiti_contacts",
    "checkouts",
    "cart_recovery_links",
]

AUDIT_SQL = r"""
with rels as (
 select c.relname table_name, c.relkind, c.relrowsecurity rls_enabled
 from pg_class c join pg_namespace n on n.oid=c.relnamespace
 where n.nspname='public' and c.relkind in ('r','p')
), grants as (
 select table_name,
 bool_or(grantee in ('anon','public') and privilege_type='SELECT') anon_select,
 bool_or(grantee in ('anon','public') and privilege_type in ('INSERT','UPDATE','DELETE')) anon_write,
 bool_or(grantee='authenticated' and privilege_type='SELECT') auth_select,
 bool_or(grantee='authenticated' and privilege_type in ('INSERT','UPDATE','DELETE')) auth_write
 from information_schema.role_table_grants where table_schema='public' group by table_name
), policies as (
 select count(*) filter (where roles::text ~ '(anon|authenticated|public)') api_policy_count,
        count(*) filter (where roles::text ~ '(anon|authenticated|public)' and (qual='true' or with_check='true')) broad_api_true_count,
        count(*) total_policy_count
 from pg_policies where schemaname='public'
), funcs as (
 select p.oid
 from pg_proc p
 join pg_namespace n on n.oid=p.pronamespace
 left join pg_depend d on d.objid=p.oid and d.deptype='e'
 where n.nspname='public' and d.objid is null
), extension_funcs as (
 select p.oid
 from pg_proc p
 join pg_namespace n on n.oid=p.pronamespace
 join pg_depend d on d.objid=p.oid and d.deptype='e'
 where n.nspname='public'
)
select jsonb_build_object(
 'project_ref', 'cnjimxglpktznenpbail',
 'base_tables_total',(select count(*) from rels where relkind='r'),
 'base_tables_rls_off',(select count(*) from rels where relkind='r' and not rls_enabled),
 'anon_select_granted',(select count(*) from grants where coalesce(anon_select,false)),
 'anon_write_granted',(select count(*) from grants where coalesce(anon_write,false)),
 'auth_select_granted',(select count(*) from grants where coalesce(auth_select,false)),
 'auth_write_granted',(select count(*) from grants where coalesce(auth_write,false)),
 'api_policy_count',(select api_policy_count from policies),
 'broad_api_true_count',(select broad_api_true_count from policies),
 'policy_total',(select total_policy_count from policies),
 'custom_functions_executable_by_anon',(select count(*) from funcs where has_function_privilege('anon',oid,'EXECUTE')),
 'custom_functions_executable_by_auth',(select count(*) from funcs where has_function_privilege('authenticated',oid,'EXECUTE')),
 'extension_functions_executable_by_anon',(select count(*) from extension_funcs where has_function_privilege('anon',oid,'EXECUTE')),
 'oauth_tokens_rows',(select case when to_regclass('public.oauth_tokens') is null then null else (select count(*) from public.oauth_tokens) end),
 'oauth_tokens_nonempty_sensitive',(select case when to_regclass('public.oauth_tokens') is null then null else (select count(*) from public.oauth_tokens where coalesce(access_token::text,'')<>'' or coalesce(refresh_token::text,'')<>'') end)
)::text;
"""


def fail(msg: str, detail: object | None = None) -> int:
    payload = {"status": "fail", "message": msg, "values_printed": False}
    if detail is not None:
        payload["detail"] = detail
    print(json.dumps(payload, sort_keys=True, ensure_ascii=False))
    return 2


def psql_json() -> dict:
    if not os.environ.get("SUPABASE_LK_POSTGRES_PASSWORD"):
        raise RuntimeError("missing SUPABASE_LK_POSTGRES_PASSWORD")
    env = os.environ.copy()
    env["PGPASSWORD"] = env["SUPABASE_LK_POSTGRES_PASSWORD"]
    result = subprocess.run(
        ["psql", POOLER_CONN, "-v", "ON_ERROR_STOP=1", "-At", "-c", AUDIT_SQL],
        env=env,
        text=True,
        capture_output=True,
        timeout=120,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(f"psql audit failed rc={result.returncode}: {result.stderr[:300]}")
    return json.loads(result.stdout)


def rest_status(table: str, key: str) -> int:
    url = os.environ["SUPABASE_LK_URL"].rstrip("/")
    req = urllib.request.Request(
        url + "/rest/v1/" + urllib.parse.quote(table) + "?select=*&limit=0",
        headers={"apikey": key, "Authorization": "Bearer " + key},
    )
    try:
        with urllib.request.urlopen(req, timeout=20) as response:
            response.read(1000)
            return int(response.status)
    except urllib.error.HTTPError as exc:
        exc.read(1000)
        return int(exc.code)


def run_gate() -> tuple[bool, dict]:
    audit = psql_json()
    anon_key = os.environ.get("SUPABASE_LK_ANON_KEY") or os.environ.get("SUPABASE_LK_PUBLISHABLE_KEY")
    service_key = os.environ.get("SUPABASE_LK_SERVICE_KEY")
    if not anon_key or not service_key or not os.environ.get("SUPABASE_LK_URL"):
        raise RuntimeError("missing Supabase URL/anon/service env")

    audit["anon_rest_statuses"] = {t: rest_status(t, anon_key) for t in SENSITIVE_PROBE_TABLES}
    audit["service_rest_statuses"] = {t: rest_status(t, service_key) for t in SENSITIVE_PROBE_TABLES}
    audit["values_printed"] = False

    failures: list[str] = []
    zero_fields = [
        "base_tables_rls_off",
        "anon_select_granted",
        "anon_write_granted",
        "auth_select_granted",
        "auth_write_granted",
        "api_policy_count",
        "broad_api_true_count",
        "custom_functions_executable_by_anon",
        "custom_functions_executable_by_auth",
    ]
    for field in zero_fields:
        if audit.get(field) != 0:
            failures.append(f"{field}={audit.get(field)}")
    if audit.get("oauth_tokens_nonempty_sensitive") not in (0, None):
        failures.append("oauth_tokens_nonempty_sensitive>0")
    bad_anon = {t: s for t, s in audit["anon_rest_statuses"].items() if s == 200}
    if bad_anon:
        failures.append("anon_rest_200=" + ",".join(sorted(bad_anon)))
    bad_service = {t: s for t, s in audit["service_rest_statuses"].items() if s != 200}
    if bad_service:
        failures.append("service_rest_not_200=" + json.dumps(bad_service, sort_keys=True))
    audit["failures"] = failures
    audit["status"] = "pass" if not failures else "fail"
    return not failures, audit


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verbose", action="store_true", help="Print sanitized JSON even when the gate passes")
    args = parser.parse_args()
    try:
        ok, audit = run_gate()
    except Exception as exc:  # sanitized: no env dump, no secrets
        return fail("lk_supabase_security_gate_error", str(exc))
    if ok:
        if args.verbose:
            print(json.dumps(audit, sort_keys=True, indent=2, ensure_ascii=False))
        return 0
    print(json.dumps(audit, sort_keys=True, indent=2, ensure_ascii=False))
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
