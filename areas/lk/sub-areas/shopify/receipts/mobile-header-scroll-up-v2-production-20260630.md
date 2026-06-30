# Receipt — Mobile header scroll-up reveal v2 Production

- Data/hora: 2026-06-30T16:58:05.085370+00:00
- Agente/profile/cron: lk-shopify
- Empresa/área: LK Sneakers / Shopify / Theme
- Responsável humano: Lucas Cimino / lk-shopify
- Pedido original: Promover para Production a correção v2 validada no DEV para o menubar/header mobile reaparecer imediatamente ao rolar para cima.
- Classificação: external-write
- Fontes usadas:
- Telegram Lucas 2026-06-30; DEV Shopify readback; Lucas validação 'Agora funcionou'; GitHub PR #125; Shopify Production Admin readback; public HTML static QA.
- O que foi feito:
- Criado PR #125 com alteração limitada a sections/lk-header.liquid; merge em production; sincronizado asset exato sections/lk-header.liquid no Shopify Production theme 155065417950 após PR merged; readback Admin OK.
- Output/artefato:
- Production contém __lkMobileHeaderScrollUpV2, lk-scroll-fixed, lk-scroll-hidden, lk-scroll-visible, lk-mobile-header-fixed, data-lk-scroll-state, delta < 0 e hideHeader(). Public HTML contém a v2; layout antigo ainda tem script desativado com return, mas a v2 em sections/lk-header.liquid é a lógica funcional validada no DEV e tem CSS com maior especificidade/important.
- Aprovação: APROVAÇÃO EXPLÍCITA ATUAL: Lucas Telegram 2026-06-30 validou o DEV com 'Agora funcionou, faça merge'. Escopo limitado ao header/menubar mobile em sections/lk-header.liquid.
- Envio/publicação: Telegram DM
- Writes externos: GitHub PR #125 merge em production; Shopify themeFilesUpsert Production para sections/lk-header.liquid.
- Riscos/bloqueios: Public QA funcional em device real foi validada por Lucas no DEV; Production foi verificada por readback/Admin e presença pública estática. Se cache/device mostrar comportamento antigo, limpar cache/reabrir sessão e revalidar; rollback via PR.
- Rollback/mitigação: Reverter PR #125 e/ou restaurar /opt/data/profiles/lk-shopify/workdirs/mobile-header-scroll-up-20260630/prod_before_sections__lk-header.liquid via DEV-first + PR; em emergência aprovada, reupsert do snapshot no Production theme.
- Próximos passos: Lucas testar em Production no mobile; se houver regressão específica de device/browser, coletar modelo/browser e ajustar seletor/threshold no DEV.
- Onde foi documentado no Brain: Receipt Brain e workdir /opt/data/profiles/lk-shopify/workdirs/mobile-header-scroll-up-20260630.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
