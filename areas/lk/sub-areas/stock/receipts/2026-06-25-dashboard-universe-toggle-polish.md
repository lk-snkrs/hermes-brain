# Receipt — Dashboard Stock OS toggle Estoque Vendas sem underline

- Data/hora: 2026-06-25T18:20:57.951011+00:00
- Agente/profile/cron: Hermes Agent default
- Empresa/área: LK / Stock OS / UI
- Responsável humano: lk-stock
- Pedido original: Lucas enviou screenshot apontando que o botão Estoque/Vendas estava desenhado/feio, com aparência de link sublinhado e contorno interno.
- Classificação: external-write
- Fontes usadas:
- Screenshot Lucas; src/public/index.html; npm test; Impeccable; smoke container /estoque/hoje.
- O que foi feito:
- Corrigido CSS do segmented control .topbar-universe-toggle/.universe-btn: removido underline de links com text-decoration none, removido box-shadow inset do ativo, adicionado estado visited/focus sem sublinhado, alinhamento inline-flex e sombra leve externa.
- Output/artefato:
- Commit b0f6f52 em feat/stock-os-api-adapter; container lk-estoque-web atualizado e reiniciado. Smoke: status 200, noTextDecoration=true, noInset=true, activeVisited=true, links /estoque/hoje e /vendas preservados.
- Aprovação: Pedido direto de Lucas para corrigir botão na UI. Escopo CSS/HTML do dashboard.
- Envio/publicação: Telegram final para Lucas
- Writes externos: GitHub push na branch feat/stock-os-api-adapter; atualização de src/public/index.html no container lk-estoque-web e restart. Tiny write 0; Shopify write 0; Notion write 0; contato externo 0.
- Riscos/bloqueios: Mudança restrita ao visual do toggle Estoque/Vendas; rotas diretas preservadas.
- Rollback/mitigação: Backup local .hermes/backups/universe-toggle-polish-20260625T181907Z.html; backup container /opt/data/profiles/lk-stock/backups/lk-estoque-web-universe-toggle-polish-20260625T181954Z; rollback via git revert b0f6f52.
- Próximos passos: Nenhum, salvo se Lucas pedir refinamento visual adicional.
- Onde foi documentado no Brain: Receipt operacional criado; regra de UI link-addressable preservada.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
