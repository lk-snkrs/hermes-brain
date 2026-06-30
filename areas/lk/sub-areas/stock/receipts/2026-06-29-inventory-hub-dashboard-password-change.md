# Receipt — Inventory Hub dashboard password changed

- Data/hora: 2026-06-29T11:43:58.613482+00:00
- Agente/profile/cron: lk-stock
- Empresa/área: LK Sneakers / Inventory Hub / Vercel
- Responsável humano: lk-stock
- Pedido original: Lucas pediu mudar a senha de entrada do Inventory Hub para um valor específico.
- Classificação: external-write
- Fontes usadas:
- Vercel project inventory-hub via Doppler/Vercel CLI; produção alias https://hub.lksnk.dev; verificação HTTP Basic auth sem imprimir senha.
- O que foi feito:
- Atualizado DASHBOARD_PASSWORD em Vercel production, redeploy production executado e alias hub.lksnk.dev atualizado.
- Output/artefato:
- Deploy production Ready em inventory-j6214ydim-lk-snkrs-projects.vercel.app, aliased https://hub.lksnk.dev. Verificação autenticada: /estoque/cockpit?qa=password-change 200 com Stock Cockpit e search input; /api/stock-cockpit/v2/summary 200 source Stock OS API freshness tiny_full_sync_nightly guardrails tiny_write=0 shopify_write=0 writes_externos=0 public_availability_safe=0. values_printed=false.
- Aprovação: Aprovação explícita no Telegram: "Mude a senha para entrar ..."; valor não registrado no receipt.
- Envio/publicação: Vercel production deploy para hub.lksnk.dev; sem mensagem externa/customer-facing.
- Writes externos: Vercel env var production DASHBOARD_PASSWORD alterada; Vercel production redeploy executado; nenhum Shopify/Tiny/Supabase data write.
- Riscos/bloqueios: Senha solicitada é curta/fraca; usada conforme pedido explícito. Recomenda-se trocar depois para valor mais forte se o link for compartilhado amplamente.
- Rollback/mitigação: Alterar DASHBOARD_PASSWORD novamente na Vercel production e redeploy; deployment anterior pode ser promovido, mas env var atual precisaria ser ajustada separadamente.
- Próximos passos: Lucas pode acessar https://hub.lksnk.dev/estoque/cockpit com usuário normal do Hub e a nova senha.
- Onde foi documentado no Brain: Receipt canônico no Brain; nenhum segredo salvo.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
