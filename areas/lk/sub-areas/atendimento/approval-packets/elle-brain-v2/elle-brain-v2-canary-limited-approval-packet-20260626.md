# Approval Packet — Elle Brain v2 canary limitado

**Data:** 2026-06-26  
**Sistema:** Elle / Chatwoot / WhatsApp LK  
**Solicitação:** ativar canary limitado da Elle Brain v2.  
**Aprovação de Lucas:** “fazer do 1 ao 4”, após recomendação de canary controlado.  
**values_printed:** false

## Evidência técnica

- Gate structured output: `99/100 valid_json`.
- Regressões: `36` testes OK.
- `py_compile`: OK para `/app/app.py`, `/app/elle_brain_v2.py`, testes.
- Writes externos durante shadow: `0`.

## Revisão de risco dos diffs

A rodada-gate tinha:

- `57` diferenças de categoria vs legado;
- `44` diferenças de handoff vs legado;
- `40` candidatos de risco quando analisados de forma conservadora.

Padrões sensíveis:

- `human_handoff → product_clear/allow`: 14
- `human_handoff → greeting/allow`: 9
- `human_handoff → product_clear/clarify`: 6
- `stock_handoff → product_clear/allow`: 6

## Mitigação aplicada antes do canary

1. Candidate v2 com `human_handoff` ou `stock_handoff` agora força `policy_action=handoff`; não aparece mais como `allow`.
2. Canary só pode substituir a decisão legado se:
   - legado **não** for handoff;
   - v2 tiver `parse_status=valid_json`;
   - v2 não tiver `handoff=true`;
   - categoria v2 estiver em allowlist segura: `greeting`, `institutional`, `coupon`, `competitor_safe`, `product_clear`;
   - policy action v2 estiver em `allow`, `rewrite`, `clarify`.
3. Se legado for handoff, canary é pulado (`legacy_handoff_guard`) e a decisão v1 continua.

## Escopo aprovado para ativação

- Percentual: `5%` por hash determinístico de `conversation_id`.
- Somente conversas sem handoff legado.
- Sem estoque/pronta entrega/reserva/loja física/prazo sensível.
- Sem pedido/troca/devolução/reembolso/cancelamento/status.
- Sem produção ampla.

## Kill-switch / rollback

Para desligar canary sem restaurar código:

```bash
docker exec elle-chatwoot sh -lc 'python3 - <<PY
import json
p="/data/elle_brain_v2_canary.json"
c=json.load(open(p)); c["enabled"]=False
open(p,"w").write(json.dumps(c, ensure_ascii=False, indent=2))
PY'
docker restart elle-chatwoot
```

Rollback completo:

- restaurar `/app/app.py`, `/app/elle_brain_v2.py`, testes a partir de `/opt/data/backups/elle-brain-v2-canary-prod/20260626T190428Z`;
- reiniciar `elle-chatwoot`;
- verificar health/readback.

## Critérios de parada imediata

- qualquer promessa de estoque/pronta entrega/reserva/prazo;
- qualquer resposta final em pós-venda sensível;
- cliente reclamando de resposta automática inadequada;
- queda de health;
- erro recorrente `elle_brain_v2_canary_error`;
- `valid_json` em canary real abaixo de 95%.

## Status

**GO para canary limitado 5%, não produção ampla.**
