#!/usr/bin/env python3
"""Execute approved Tiny codigo writes for LK P0 residual candidates.

Guardrails:
- Tiny codigo only.
- No Shopify writes.
- Read back each Tiny item and verify non-code fields unchanged.
- Roll back codigo to previous value if verification fails.
"""
import base64
import json
import pathlib
import time
import urllib.parse
import urllib.request
from copy import deepcopy
from datetime import datetime, timezone

ROOT = pathlib.Path(__file__).resolve().parents[1]
PREVIEW = ROOT / "reports/lk-p0-remaining-tiny-code-preview-2026-05-11.json"
OUT = ROOT / "reports/lk-p0-remaining-tiny-code-execution-2026-05-11.json"
APPROVAL = "Lucas aprovou em Telegram: Aprovado — preencher codigo Tiny dos 7 itens candidatos com os SKUs Shopify propostos, sem alterar Shopify, preço, estoque ou produto."

EXPECTED_IDS = {
    "1069545385": "NKE-9054174-41",
    "1070120736": "ONI-0995678-425",
    "1069544047": "NB-0254942-37",
    "1070119554": "ONI-6772830-38",
    "1069542767": "ALO-8506462-S",
    "1069544315": "SST-4542302-L",
    "1069930823": "PAC-1197278-S",
}

SNAPSHOT_FIELDS = [
    "nome",
    "codigo",
    "preco",
    "preco_promocional",
    "unidade",
    "origem",
    "situacao",
    "tipo",
    "grade",
    "idProdutoPai",
    "sequencia",
]

PRESERVE_FIELDS = [
    "sequencia",
    "id",
    "nome",
    "unidade",
    "preco",
    "preco_promocional",
    "origem",
    "situacao",
    "tipo",
    "grade",
]


def load_tiny_token():
    # Do not print secret values. Token is fetched from Doppler on demand using the locally approved Doppler token file.
    doppler_token = pathlib.Path("/opt/data/hermes_bruno_ingest/.secrets/doppler_token").read_text().strip()
    req = urllib.request.Request(
        "https://api.doppler.com/v3/configs/config/secrets/download?project=lc-keys&config=prd&format=json"
    )
    req.add_header("Authorization", "Basic " + base64.b64encode((doppler_token + ":").encode()).decode())
    with urllib.request.urlopen(req, timeout=60) as resp:
        secrets = json.load(resp)
    return secrets["TINY_API_TOKEN"]


TINY_TOKEN = load_tiny_token()


def tiny_call(method, params):
    data = urllib.parse.urlencode({**params, "token": TINY_TOKEN, "formato": "json"}).encode()
    req = urllib.request.Request(f"https://api.tiny.com.br/api2/{method}.php", data=data, method="POST")
    with urllib.request.urlopen(req, timeout=90) as resp:
        return json.load(resp)


def tiny_obter(item_id):
    # Tiny API blocks bursts; keep spacing conservative for business-critical writes.
    time.sleep(4.0)
    ret = tiny_call("produto.obter", {"id": str(item_id)}).get("retorno", {})
    return ret.get("status"), ret.get("produto") or {}, ret


def tiny_alterar(produto_obj):
    # `sequencia` is required inside the produto record for the bulk/root wrapper.
    # produto.obter does not return it for child variations, so set a safe single-record sequence.
    time.sleep(4.0)
    produto_obj = deepcopy(produto_obj)
    produto_obj.setdefault("sequencia", "1")
    body = {"produtos": [{"produto": produto_obj}]}
    return tiny_call("produto.alterar", {"produto": json.dumps(body, ensure_ascii=False)})


def snapshot(prod):
    return {k: deepcopy(prod.get(k)) for k in SNAPSHOT_FIELDS if k in prod}


def non_code_changes(before, after):
    changes = []
    for k in SNAPSHOT_FIELDS:
        if k == "codigo":
            continue
        if before.get(k) != after.get(k):
            changes.append({"field": k, "before": before.get(k), "after": after.get(k)})
    return changes


def build_payload(before_product, target_codigo):
    payload = {k: deepcopy(before_product.get(k)) for k in PRESERVE_FIELDS if k in before_product}
    payload["id"] = str(before_product.get("id"))
    payload["codigo"] = target_codigo
    return payload


def rollback(before_product, rollback_codigo):
    rb_payload = build_payload(before_product, rollback_codigo)
    rb_ret = tiny_alterar(rb_payload)
    status, after_rb, raw = tiny_obter(before_product.get("id"))
    return {
        "rollback_api_return": rb_ret.get("retorno", rb_ret),
        "rollback_verify_status": status,
        "rollback_after_codigo": after_rb.get("codigo", ""),
        "rollback_success": (after_rb.get("codigo", "") or "") == (rollback_codigo or ""),
        "rollback_raw_status": raw.get("status"),
    }


def main():
    preview = json.loads(PREVIEW.read_text())
    candidates = preview["candidates"]
    if len(candidates) != 7:
        raise SystemExit(f"Refusing: expected 7 candidates, got {len(candidates)}")

    results = []
    for c in candidates:
        tiny_id = str(c["tiny_target_item_id"])
        target = c["tiny_target_codigo"]
        result = {
            "tiny_child_id": tiny_id,
            "product_title": c.get("product_title"),
            "size": c.get("size"),
            "shopify_variant_id": c.get("shopify_variant_id"),
            "shopify_sku_live": c.get("shopify_sku_live"),
            "target_codigo": target,
            "write_attempted": False,
            "success": False,
            "rollback_codigo": None,
        }
        try:
            if EXPECTED_IDS.get(tiny_id) != target:
                raise RuntimeError(f"Candidate not in approved expected set: {tiny_id} => {target}")

            pre_status, before_prod, pre_raw = tiny_obter(tiny_id)
            before_snap = snapshot(before_prod)
            result["precheck_status"] = pre_status
            result["before_snapshot"] = before_snap
            result["rollback_codigo"] = before_prod.get("codigo") or ""

            if pre_status != "OK" or not before_prod:
                raise RuntimeError(f"Tiny produto.obter precheck failed: {pre_raw.get('erros') or pre_raw.get('erro') or pre_raw}")
            current_codigo = before_prod.get("codigo") or ""
            if current_codigo == target:
                result.update({
                    "write_attempted": False,
                    "write_status": "SKIPPED_ALREADY_TARGET",
                    "success": True,
                    "after_snapshot": before_snap,
                    "non_code_changes_detected": [],
                })
                results.append(result)
                continue
            if current_codigo:
                raise RuntimeError(f"Refusing to overwrite non-empty codigo {current_codigo!r}")

            payload = build_payload(before_prod, target)
            result["write_attempted"] = True
            result["method"] = "produto.alterar root produtos[].produto child variation record with required fields + codigo"
            write_raw = tiny_alterar(payload)
            write_ret = write_raw.get("retorno", {})
            result["write_status"] = write_ret.get("status")
            result["write_status_processamento"] = write_ret.get("status_processamento")
            result["write_codigo_erro"] = write_ret.get("codigo_erro")
            result["write_errors"] = write_ret.get("erros") or write_ret.get("erro")

            verify_status, after_prod, verify_raw = tiny_obter(tiny_id)
            after_snap = snapshot(after_prod)
            changes = non_code_changes(before_snap, after_snap)
            result["verify_status"] = verify_status
            result["after_snapshot"] = after_snap
            result["non_code_changes_detected"] = changes
            result["success"] = ((after_prod.get("codigo") or "") == target and not changes)

            if not result["success"]:
                # Only call rollback if Tiny actually changed codigo or a non-code field.
                # If the API rejected the write and read-back is identical, avoid extra rate-limit pressure.
                if (after_prod.get("codigo") or "") != (before_prod.get("codigo") or "") or changes:
                    result["rollback"] = rollback(before_prod, result["rollback_codigo"])
                else:
                    result["rollback"] = {"not_needed": True, "reason": "read-back unchanged after failed write"}
        except Exception as e:
            result["error"] = str(e)[:500]
            # Roll back only if we have a before snapshot and attempted a write.
            if result.get("write_attempted") and result.get("before_snapshot"):
                try:
                    before_status, before_for_rb, _ = tiny_obter(tiny_id)
                    if before_for_rb:
                        # Use original non-code fields preserved from before_snapshot where possible.
                        original_like = deepcopy(before_for_rb)
                        for k, v in result["before_snapshot"].items():
                            original_like[k] = v
                        original_like["id"] = tiny_id
                        result["rollback"] = rollback(original_like, result.get("rollback_codigo") or "")
                except Exception as rb_e:
                    result["rollback_error"] = str(rb_e)[:500]
        results.append(result)

    report = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "approval": APPROVAL,
        "scope": "Execução Tiny codigo para 7 variações P0 aprovadas; sem Shopify; verificação contra alteração de preço/grade/produto.",
        "guardrails": [
            "Tiny codigo only",
            "no Shopify write",
            "before/after non-code fields checked",
            "rollback previous codigo captured and attempted on verification failure",
        ],
        "counts": {
            "candidates": len(candidates),
            "write_attempted": sum(1 for r in results if r.get("write_attempted")),
            "success": sum(1 for r in results if r.get("success")),
            "failed": sum(1 for r in results if not r.get("success")),
        },
        "results": results,
    }
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({
        "report": str(OUT),
        "counts": report["counts"],
        "failed": [
            {"tiny_child_id": r.get("tiny_child_id"), "error": r.get("error"), "after_codigo": (r.get("after_snapshot") or {}).get("codigo")}
            for r in results if not r.get("success")
        ],
        "successes": [
            {"tiny_child_id": r.get("tiny_child_id"), "target_codigo": r.get("target_codigo"), "write_status": r.get("write_status")}
            for r in results if r.get("success")
        ],
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
