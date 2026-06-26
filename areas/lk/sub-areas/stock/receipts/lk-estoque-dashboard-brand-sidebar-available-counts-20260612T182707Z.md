# Receipt — LK Estoque dashboard — contadores de marca por disponíveis

- Data/hora: 2026-06-12T18:27:07.996732+00:00
- Agente/profile/cron: lk-stock
- Empresa/área: LK Sneakers / Stock OS
- Responsável humano: Hermes lk-stock
- Pedido original: Corrigir sidebar do dashboard: filtro por marca deve contar produtos disponíveis, não total bruto de produtos.
- Classificação: external-write
- Fontes usadas:
- Código/testes do dashboard LK-Estoque-Web-inicial; produção https://estoque.lkskrs.online autenticada; Stock OS API read-only.
- O que foi feito:
- Adicionado helper buildAvailableBrandCounts; sidebar, silhueta, tamanho e cor passam a usar apenas estoque > 0; testes TDD adicionados; deploy aplicado no container lk-estoque-web; imagem latest atualizada; commit 3945142 pushado e verificado.
- Output/artefato:
- Produção validada: HTML 200, API 200, total API 5192, total disponível sidebar esperado 323, top marcas disponíveis Nike 168, Onitsuka 48, New Balance 46, Adidas 29, Outros 24; guardrails Tiny/Shopify/public availability = 0.
- Aprovação: Aprovado por Lucas no contexto de 'seguir tudo aprovado' e pedido direto de correção no sidebar.
- Envio/publicação: Telegram: resumo final nesta conversa.
- Writes externos: Docker/container web: deploy/restart; GitHub push branch feat/stock-os-api-adapter. Tiny write 0; Shopify write 0; public availability 0.
- Riscos/bloqueios: Sem alteração de estoque real; risco limitado a apresentação do dashboard. Backup: /opt/data/lk-estoque-web-backups/20260612T182440Z-brand-sidebar-available-counts.
- Rollback/mitigação: Restaurar /app/src a partir do backup ou reverter commit 3945142; imagem anterior disponível tag operational-control-20260612T181253Z.
- Próximos passos: Nenhum obrigatório; opcional abrir PR/merge conforme fluxo do repo se desejado.
- Onde foi documentado no Brain: Skill lk-stock atualizado com pitfall UI/sidebar: marca/silhueta/tamanho/cor contam disponíveis.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
