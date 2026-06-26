# Receipt — PDP size guide Mind 002 full table DEV to Production

- Data/hora: 2026-06-15T11:09:43.148994+00:00
- Agente/profile/cron: lk-shopify
- Empresa/área: LK Sneakers / Shopify
- Responsável humano: Lucas Cimino
- Pedido original: Subir para DEV e depois fazer merge para Production a tabela especial do Nike Mind 002 no padrão New Balance completo
- Classificação: external-write
- Fontes usadas:
- Shopify theme readback DEV/Production; QA browser mobile; referência LK PDP size guide; aprovação explícita Lucas via Telegram
- O que foi feito:
- Atualizado sections/lk-pdp.liquid no tema DEV e depois Production; Mind 002 masculino com tabela BR|US M|US W|EU|CM; Mind 001 e tabela padrão/New Balance preservados
- Output/artefato:
- DEV SHA b9af606836626f37e8a98ade000b7210927861a1a991931c928fb6c3cb9f04f0; Production SHA b9af606836626f37e8a98ade000b7210927861a1a991931c928fb6c3cb9f04f0; QA DEV e Production pass=true
- Aprovação: Aprovação explícita atual de Lucas para write externo Shopify: Subir para dev; depois fazer merge para Production
- Envio/publicação: Shopify Admin API via Doppler profile lk-shopify; values_printed=false
- Writes externos: Shopify theme asset write: DEV theme 155065450718 and Production theme 155065417950, asset sections/lk-pdp.liquid
- Riscos/bloqueios: Alteração em tema Production; mitigado com backup prod_before, readback SHA e QA mobile pós-merge
- Rollback/mitigação: Reenviar prod_before_sections__lk-pdp.liquid salvo no diretório do receipt para o asset sections/lk-pdp.liquid do tema Production 155065417950
- Próximos passos: Monitorar revisão visual de Lucas; se necessário ajustar copy/tabela e repetir QA
- Onde foi documentado no Brain: receipt.json, prod_before/prod_readback e screenshots mobile salvos no diretório do receipt; values_printed=false
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
