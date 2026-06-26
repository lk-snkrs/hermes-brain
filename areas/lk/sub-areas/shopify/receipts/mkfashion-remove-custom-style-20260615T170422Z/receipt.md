# Receipt — Remove MK Provador custom style override

- Data/hora: 2026-06-15T17:04:38.270858+00:00
- Agente/profile/cron: lk-shopify
- Empresa/área: LK Sneakers / Shopify
- Responsável humano: Lucas Cimino
- Pedido original: Remover a modificação LK do botão Provador MK com fundo branco/opacidade 70%, pois a MK atualizou o layout nativo
- Classificação: external-write
- Fontes usadas:
- Pedido explícito de Lucas no Telegram; repo lk-snkrs/lk-new-theme branch production; Shopify Production Asset API readback; browser mobile live QA
- O que foi feito:
- Removido style override de window.__MK.anchor, removido script lk-mk-tryon-open-shadow-style-20260613 e removido runtime tuneButton; SDK MK e anchor placement preservados
- Output/artefato:
- PR #77 merged em production; Shopify production layout/theme.liquid SHA igual ao Git target; SDK e anchor presentes; marcadores de background rgba .7, open-shadow patch e tuneButton ausentes; live HTML mobile verificado em múltiplos PDPs
- Aprovação: Aprovação explícita atual de Lucas para write externo Shopify/theme via GitHub Production: Pode remover ok?
- Envio/publicação: GitHub PR/merge para production e deploy/sync Shopify; values_printed=false
- Writes externos: GitHub production branch PR #77 merged; Shopify theme Production 155065417950 atualizado por sync/deploy do tema
- Riscos/bloqueios: Botão passa a depender do layout nativo MK; em headless QA o host #mk-tryon-button-host não apareceu, mas SDK/anchor e remoção dos overrides foram validados no HTML/readback
- Rollback/mitigação: Reverter PR #77/merge commit 4fc40a4 e aguardar sync Shopify; alternativa emergencial só com aprovação explícita: restaurar layout/theme.liquid anterior
- Próximos passos: Lucas revisar visual no celular real; se o botão nativo não aparecer ou ficar fora do esperado, acionar MK ou preparar novo ajuste mínimo separado
- Onde foi documentado no Brain: shopify-readback.json, live-qa.json, live-scan.json e screenshots salvos no diretório do receipt; skill mkfashion production promotion atualizada com padrão de remoção/vendor-native
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
