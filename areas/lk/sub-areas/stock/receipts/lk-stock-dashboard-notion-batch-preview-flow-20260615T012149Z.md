# Receipt — LK Stock dashboard Notion batch preview flow

- Data/hora: 2026-06-15T01:22:18.785935+00:00
- Agente/profile/cron: Hermes Agent default
- Empresa/área: LK / Stock
- Responsável humano: Lucas Cimino
- Pedido original: Fazer em sequência a integração do botão Notion no dashboard de Stock com preview, confirmação e lote.
- Classificação: external-write
- Fontes usadas:
- Dashboard estoque.lkskrs.online; Brain/skill lk-stock; Notion database [LK] Encomenda | Estoque; testes locais e smoke em produção.
- O que foi feito:
- Adicionado endpoint dry-run /api/vendas/notion/preview-compra; modal de prévia; confirmação antes do write; seleção em lote na Lista para Julio; split por modelo x tamanho com quantidade unificada; dedupe por fingerprint; deploy Docker local.
- Output/artefato:
- Dashboard em produção com fluxo de preview e batch Notion. Imagem lk-estoque-web-web:sales-notion-batch-20260615T012042Z.
- Aprovação: Lucas autorizou explicitamente no Telegram: Fazer tudo em sequência, pode fazer em lote. Escopo limitado a dashboard autenticado e criação de tarefas de compra no Notion para Júlio; sem compra automática.
- Envio/publicação: Sem envio/publicação externa; evidência local no Brain.
- Writes externos: github push dashboard; docker local redeploy; Notion write habilitado somente por confirmação autenticada do usuário no dashboard; nenhum Tiny/Shopify/customer write
- Riscos/bloqueios: Write Notion exige confirmação humana; preview não escreve; rota protegida por auth; sem expor secrets.
- Rollback/mitigação: Reverter para imagem anterior registrada em /tmp/lk_estoque_web_prev_image_sales-notion-batch-20260615T012042Z ou git revert do commit do dashboard; remover cards Notion criados manualmente se necessário.
- Próximos passos: Ciclo fechado; próximos ajustes só se Lucas quiser alterar status/campos no Notion ou bulk update em vez de dedupe.
- Onde foi documentado no Brain: Receipt criado; skill lk-stock já contém regra: 1 card por modelo x tamanho.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
