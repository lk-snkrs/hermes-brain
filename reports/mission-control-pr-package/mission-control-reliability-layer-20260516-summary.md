# Mission Control Reliability Layer — 2026-05-16

Escopo aprovado por Lucas: “fazer tudo acima”.

## Implementado

### 1. Fonte/PR package local
- Novo pacote local gerado em `reports/mission-control-pr-package/mission-control-reliability-layer-20260516.patch`.
- Sem `git push`/PR remoto automático.
- Deploy publicado em `mission.lucascimino.com` conforme permissão operacional do Mission Control.

### 2. Event Ledger real
- Criado ledger append-only local no Brain: `reports/mission-control-event-ledger.jsonl`.
- Eventos sanitizados aparecem no Mission Control em **Event Ledger**.
- Nenhum segredo no ledger.

### 3. Action Packet schema único
- `opsState.actionPackets` padroniza decisão, empresa, gate, status, confiança, fonte, expiração, payloadHash, ação segura, ação bloqueada e rollback.
- Novo endpoint público sanitizado: `GET /api/mission/packets`.

### 4. Waiting Lucas dinâmico
- Fila agora carrega `packetId`, idade e expiração.
- Cada decisão aponta para pacote executável/registrável.

### 5. Health Center
- Nova seção consolidando Mission Control, crons, Kanban, Approval API e secrets.
- Mantém checks granulares em grid secundário.

### 6. Kanban dispatcher por lanes
- `opsState.kanbanPolicy` define:
  - Backlog: never
  - Ready Read-only: allowed para perfis restritos
  - Doing: claimed-only
  - Waiting Lucas: never
  - Waiting External: never
  - QA: review-only
  - Done: never
- Smoke real executado no board `lk-growth-ops`:
  - Card: `t_5c5e6103`
  - Assignee: `hermes-ops-readonly`
  - Resultado: done; sem writes/externo/Docker/Vercel/GitHub/Shopify/Tiny/Merchant/secrets.

### 7. Rollback Registry
- Nova seção lista rollback para Vercel, Approval API, Kanban dispatch, Event Ledger e LK Operating Intelligence.

### 8. LK Operating Intelligence read-only
- Nova seção com sinais:
  - stockout/margem
  - influencer performance
  - GMC anomalies
  - sourcing
- Todos read-only; compra/preço/campanha/write/fornecedor continuam A4.

### 9. API hardening
- `/api/mission/approvals` e `/api/mission/kanban` agora validam:
  - allowlist de packetId
  - expiration
  - redaction
  - payloadHash
  - rate-limit in-memory 30/min por client key
  - token opcional via `MISSION_CONTROL_APPROVAL_TOKEN_HASH` se configurado
- Browser/API continuam sem executar comando arbitrário e sem writes externos.

## QA

Passou:
- `npm run lint`
- `npm run build`
- local API smoke:
  - `/api/mission/state`
  - `/api/mission/approvals`
  - `/api/mission/kanban`
  - `/api/mission/packets`
- POST local approvals com redaction de `sk-*`
- POST local kanban packet
- secret scan repo: 0 hits reais
- secret scan Brain ledger/state: 0 hits
- Vercel deploy prebuilt prod
- produção HTTP 200 na home e nos 4 endpoints
- POST produção approvals com redaction de `sk-*`
- browser render com Health Center, Action Packets, Rollback Registry e LK Operating Intelligence
- browser console: 0 erros
- Mission Control watchdog: silent OK
- `.vercel/.env.production.local`: removido

## Produção

URL validada:
`https://mission.lucascimino.com/?debug=reliability-layer-20260516`

## Rollback

1. Promover deployment Vercel anterior.
2. Aplicar patch reverso do pacote local.
3. Remover/disable:
   - `src/app/api/mission/packets/route.ts`
   - novas validações em `mission-control-api.ts`
   - novas seções do `MissionPages.tsx`
   - novas entradas geradas em `ops-state.generated.ts`
4. Para Kanban: unassign/reclaim cards e pausar dispatch se necessário.
5. Para token opcional: remover `MISSION_CONTROL_APPROVAL_TOKEN_HASH` se vier a ser configurado.

## Guardrails mantidos

- Sem GitHub push/PR remoto.
- Sem Docker/host/gateway restart.
- Sem Shopify/Tiny/Merchant write.
- Sem Meta/Google campanha.
- Sem email/WhatsApp/cliente.
- Sem segredo impresso ou salvo em artefato público.
