# Receipt — Dashboard consulta filter-first

- Data/hora: 2026-06-25T20:13:50.891942+00:00
- Agente/profile/cron: lk-stock
- Empresa/área: LK / Stock OS
- Responsável humano: Hermes lk-stock
- Pedido original: Lucas pediu corrigir /estoque/consulta para ser uma tela real de consulta + filtro, não cockpit/fila operacional.
- Classificação: infra-sensitive
- Fontes usadas:
- Código LK-Estoque-Web-inicial; npm test; Impeccable; smoke Docker lk-estoque-web; skill lk-stock atualizada.
- O que foi feito:
- Rota /estoque/consulta ganhou workspace próprio de consulta, busca principal, filtros Com estoque/Último par/Zerados/Todos, esconde Estoque hoje/overview/operations/quick-filter de decisão, usa filtro default available e pageSize inicial 96; cards seguem image-first.
- Output/artefato:
- Commit 88dc54f em feat/stock-os-api-adapter; container lk-estoque-web reiniciado; backup /opt/data/profiles/lk-stock/backups/lk-estoque-web-consulta-filter-surface-final-20260625T201240Z.
- Aprovação: Aprovação escopada pelo pedido direto de Lucas para corrigir especificamente a UI da URL https://estoque.lkskrs.online/estoque/consulta; escopo limitado a dashboard local/container e GitHub, sem Tiny/Shopify/Notion/cliente/compra.
- Envio/publicação: Telegram: resumo final após verificação.
- Writes externos: GitHub push e Docker local restart; Tiny 0; Shopify 0; Notion 0; WhatsApp/email/cliente 0; compra 0
- Riscos/bloqueios: Mudança visual e restart Docker do dashboard; rollback disponível por backup Docker e git revert.
- Rollback/mitigação: Restaurar /app/src a partir do backup listado ou fazer git revert 88dc54f e recopy/restart do container.
- Próximos passos: Se Lucas ainda achar a consulta pesada, próximo passo é endpoint ainda mais leve para facets/search-first ou render server-side inicial menor.
- Onde foi documentado no Brain: Skill lk-stock references/stock-dashboard-uiux-pro-minimal-redesign-20260625.md atualizada com regra de /estoque/consulta como consulta real.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
