# Receipt — Dashboard image-first cards e vendas desktop progressivo

- Data/hora: 2026-06-25T19:51:29.524847+00:00
- Agente/profile/cron: lk-stock
- Empresa/área: LK / Stock OS
- Responsável humano: Hermes lk-stock
- Pedido original: Lucas pediu que cards de busca/estoque tenham obrigatoriamente foto acima do card e que a página Vendas deixe de parecer mobile/lenta.
- Classificação: infra-sensitive
- Fontes usadas:
- Código LK-Estoque-Web-inicial; testes npm; Impeccable; smoke Docker lk-estoque-web; skill lk-stock atualizada.
- O que foi feito:
- Cards stock-card e grade-card ficaram image-first; /vendas ganhou workspace desktop; endpoints pesados de score/cobertura/reposição foram movidos para carregamento sob demanda; testes e smoke container passaram; branch GitHub sincronizada.
- Output/artefato:
- Commits f86da8f e c9f8684 em feat/stock-os-api-adapter; container lk-estoque-web reiniciado; backups em /opt/data/profiles/lk-stock/backups/lk-estoque-web-card-images-sales-layout-20260625T193832Z e /opt/data/profiles/lk-stock/backups/lk-estoque-web-defer-heavy-sales-queues-20260625T195003Z.
- Aprovação: Aprovado pelo pedido direto de Lucas para corrigir UI local/dashboard; sem writes externos comerciais.
- Envio/publicação: Telegram: resumo final após verificação.
- Writes externos: GitHub push e Docker local restart; Tiny 0; Shopify 0; Notion 0; WhatsApp/email/cliente 0; compra 0.
- Riscos/bloqueios: Mudança visual e restart Docker do dashboard; rollback por backup Docker e commits anteriores.
- Rollback/mitigação: Restaurar /app/src a partir dos backups listados ou fazer git revert c9f8684/f86da8f e recopy/restart do container.
- Próximos passos: Se Lucas ainda achar Vendas pesada, medir no browser real e criar endpoints summary-first adicionais para os painéis sob demanda.
- Onde foi documentado no Brain: Skill lk-stock references/stock-dashboard-uiux-pro-minimal-redesign-20260625.md atualizada com regra image-first e Vendas progressivo.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
