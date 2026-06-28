# Receipt — PDP Curadoria LK hotfix remove duplicate Samba

- Data/hora: 2026-06-27T15:40:57.695400+00:00
- Agente/profile/cron: lk-shopify
- Empresa/área: LK / Shopify
- Responsável humano: lk-shopify
- Pedido original: Lucas reportou duplicação visual de Curadoria LK no PDP Samba após o batch famílias 1-5.
- Classificação: external-write
- Fontes usadas:
- Imagem enviada por Lucas; PR #113; Shopify DEV/Production readback; public QA/cache poll.
- O que foi feito:
- Removido o bloco Adidas Samba do snippet batch snippets/lk-variante-batch-families-1-5-20260627.liquid para evitar segunda Curadoria em PDPs que já têm Curadoria própria. Mantidos Onitsuka Mexico 66, New Balance 9060 e Nike Vomero. DEV sincronizado diretamente; Production via PR #113.
- Output/artefato:
- PR #113 MERGED; snippet SHA12 5f29022c9425 em DEV e Production; DEV Samba HTTP 200, Liquid errors 0, 1 seção lk-variante, 0 batch markers; Production Samba estabilizou após cache poll com 1 seção lk-variante, 0 batch markers, has_batch_samba=false; Onitsuka/NB9060/Vomero mantêm batch marker 1; values_printed=false.
- Aprovação: Correção de bug reportado no escopo do batch aprovado
- Envio/publicação: Telegram
- Writes externos: GitHub production PR merge #113; Shopify DEV snippet write; Shopify Production readback. Sem produto/preço/estoque/Tiny/GMC/Klaviyo/ads/WhatsApp/email.
- Riscos/bloqueios: Baixo: remoção seletiva do bloco Samba do snippet batch. Cache público alternou por alguns probes e estabilizou limpo após polling.
- Rollback/mitigação: Reverter PR #113 para reintroduzir Samba no batch, se desejado; ou restaurar snippet anterior SHA12 89bcb46d9a75. Não recomendado enquanto Samba já tiver Curadoria própria.
- Próximos passos: Não incluir famílias com Curadoria pública existente em batch genérico; usar source/public marker gate antes de merge.
- Onde foi documentado no Brain: Workdir /opt/data/profiles/lk-shopify/workdirs/curadoria-batch-families-1-5-dev-20260627/fix-duplicate-samba; receipt canônico no Brain.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
