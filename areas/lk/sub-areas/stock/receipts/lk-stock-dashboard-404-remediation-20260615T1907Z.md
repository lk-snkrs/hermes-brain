# Receipt — LK Stock dashboard 404 remediation

- Data/hora: 2026-06-15T19:07:43.310641+00:00
- Agente/profile/cron: lk-stock
- Empresa/área: LK / Stock OS dashboard
- Responsável humano: lk-stock
- Pedido original: Lucas reportou que https://estoque.lkskrs.online caiu e retornava 404 page not found.
- Classificação: infra-sensitive
- Fontes usadas:
- HTTPS curl externo; SSH VPS lc.vps 72.60.150.124; Docker ps/events/logs; Stock API health; smoke autenticado interno/externo.
- O que foi feito:
- Diagnosticado 404 público, verificado DNS para 72.60.150.124, acesso SSH por chave, containers lk-estoque-web e lk-estoque-stock-api. Durante remediação o container web foi recriado/restaurado no compose /opt/lk-estoque-web com labels Traefik corretas Host(`estoque.lkskrs.online`); container anterior preservado como lk-estoque-web-pre404-20260615T190413Z para rollback/forense. Nenhum secret impresso.
- Output/artefato:
- Produção recuperada: sem auth retorna 401 Basic realm LK Estoque; com auth / retorna 200 HTML LK Sneakers — Estoque; /api/estoque?limit=3 retorna 200 total=3746 source Stock OS API; /api/vendas/executive-summary retorna 200; Stock API /health ok db_exists=true. Guardrails tiny_write=0 shopify_write=0 writes_externos=0 public_availability_safe=0.
- Aprovação: Aprovação escopada implícita/atual pelo pedido direto de Lucas para corrigir site caído; ação limitada a restaurar disponibilidade do dashboard/containers, sem DNS/secrets/Tiny/Shopify/Notion write.
- Envio/publicação: Telegram final summary após verificação.
- Writes externos: Docker/prod remediation no VPS; nenhum write Tiny, Shopify, Notion, cliente, fornecedor ou campanha.
- Riscos/bloqueios: Container anterior saiu com SIGTERM durante restauração; Notion status endpoint respondeu missing_token/503, não bloqueia estoque/vendas mas requer ajuste separado se Lucas quiser usar botão Notion agora.
- Rollback/mitigação: Container anterior preservado como lk-estoque-web-pre404-20260615T190413Z; imagens Docker existentes podem ser retagueadas/reiniciadas se necessário; compose em /opt/lk-estoque-web.
- Próximos passos: Monitorar estabilidade; se 404 voltar, auditar gatilho externo/cron/compose que destruiu/renomeou container e corrigir persistência do deploy. Ajustar token Notion separadamente apenas com aprovação/escopo.
- Onde foi documentado no Brain: areas/lk/sub-areas/stock/receipts/lk-stock-dashboard-404-remediation-20260615T1907Z.md
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
