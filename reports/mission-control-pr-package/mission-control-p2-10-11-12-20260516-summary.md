# Mission Control P2 10/11/12 — Command System ativo

Data: 2026-05-16
Escopo aprovado por Lucas: desbloquear itens 10, 11 e 12.

## Implementado

1. **Clickable approval backend**
   - UI com botões reais: `Aprovar escopo P2`, `Preview only`, `Ajustar`, `Bloquear`, `Kanban packet`.
   - Endpoint `POST /api/mission/approvals`.
   - Validação por allowlist de `packetId` e ações.
   - Redação automática de padrões de segredo e email.
   - Recibo SHA-256 curto por submissão.
   - Não executa envio externo, Docker/host, Shopify/Tiny/Merchant, secret print ou comando arbitrário pelo browser.

2. **Public API/proxy**
   - `GET /api/mission/state`: feed sanitizado/no-store do `opsState`.
   - `GET /api/mission/approvals`: capacidades e guardrails do backend de aprovação.
   - `GET/POST /api/mission/kanban`: capacidades Kanban e geração de pacote restrito.
   - Headers: `no-store`, `x-mission-control`, `x-robots-tag: noindex`.

3. **Kanban workers**
   - Board `lk-growth-ops` validado.
   - Perfis restritos expostos no contrato: `hermes-ops-readonly`, `brain-process`, `lk-analyst-readonly`, `lk-content-reviewer`.
   - Criado e despachado smoke card real `t_11602feb` para `hermes-ops-readonly`.
   - Resultado: `done`; smoke read-only concluído; sem necessidade A3/A4 adicional.

## QA

- `npm run lint`: passou.
- `npm run build`: passou; rotas API dinâmicas incluídas.
- Local API smoke: passou para `/api/mission/state`, `/api/mission/approvals`, `/api/mission/kanban`.
- Redaction smoke: `sk-*` virou `[REDACTED]`.
- Secret scan: 0 hits.
- Vercel deploy produção: concluído e alias `mission.lucascimino.com` atualizado.
- Produção HTTP/API: 200 em home e nas 3 rotas.
- Browser: UI renderiza Command System e botões; POST via browser retornou recibo.
- Console browser: 0 erros.
- Watchdog Mission Control: silent OK.
- `.vercel/.env.production.local`: removido.

## Rollback

- Reverter para deploy anterior no Vercel ou aplicar patch reverso deste pacote.
- Remover/disable rotas `src/app/api/mission/*` e `CommandActionPanel`.
- Unassign/pausar cards Kanban ou desabilitar dispatch local/gateway se necessário.
- Nenhuma mutação externa foi feita por endpoints públicos.

## Artefatos

- Patch: `reports/mission-control-pr-package/mission-control-p2-10-11-12-20260516.patch`
- Summary: `reports/mission-control-pr-package/mission-control-p2-10-11-12-20260516-summary.md`
- Kanban smoke card: `t_11602feb`
