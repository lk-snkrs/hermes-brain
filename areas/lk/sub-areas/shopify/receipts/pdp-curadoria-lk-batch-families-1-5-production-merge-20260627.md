# Receipt — PDP Curadoria LK batch families 1-5 Production merge

- Data/hora: 2026-06-27T15:34:38.628180+00:00
- Agente/profile/cron: lk-shopify
- Empresa/área: LK / Shopify
- Responsável humano: lk-shopify
- Pedido original: Lucas aprovou levar para Production o batch DEV Curadoria LK famílias 1–5.
- Classificação: external-write
- Fontes usadas:
- DEV receipt pdp-curadoria-lk-batch-families-1-5-dev-20260627.md; GitHub PR #112; Shopify Production Admin readback; public production QA.
- O que foi feito:
- PR #112 criado e mergeado contra production com diff mínimo: snippet snippets/lk-variante-batch-families-1-5-20260627.liquid e uma render line em sections/lk-pdp.liquid. Aplicado em Production para Onitsuka Mexico 66, New Balance 9060, Nike Vomero e Adidas Samba. NB530 permaneceu fora por pool público insuficiente.
- Output/artefato:
- PR #112 MERGED; merge commit 17f925acf66bf6f70c10b0ec15090acce02f5334; Shopify Production Theme 155065417950 readback 200/200; section SHA12 target/readback 5529c7e39105; snippet SHA12 target/readback 89bcb46d9a75; QA público Production HTTP 200 e Liquid errors 0 em 10 PDPs; markers presentes nas famílias aplicadas; NB530 sem marker conforme esperado; 22 links de cards HTTP 200; values_printed=false.
- Aprovação: Aprovo
- Envio/publicação: Telegram
- Writes externos: GitHub production PR merge + Shopify Production theme sync/readback. Assets: sections/lk-pdp.liquid e snippets/lk-variante-batch-families-1-5-20260627.liquid. Sem produto/preço/estoque/Tiny/GMC/Klaviyo/ads/WhatsApp/email.
- Riscos/bloqueios: Baixo-médio: Curadoria editorial no PDP. Mitigação: GitHub source-of-truth, diff mínimo, readback por SHA, QA público, cap até 5 cards, produto atual excluído. NB530 bloqueado/fora do release.
- Rollback/mitigação: Reverter PR #112 / merge commit 17f925acf66bf6f70c10b0ec15090acce02f5334; ou remover render line em sections/lk-pdp.liquid e remover snippet novo via PR.
- Próximos passos: Monitorar PDPs publicados e reabrir NB530 quando houver pool público válido >=3.
- Onde foi documentado no Brain: Workdir /opt/data/profiles/lk-shopify/workdirs/curadoria-batch-families-1-5-dev-20260627/prod-merge; receipt canônico no Brain.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
