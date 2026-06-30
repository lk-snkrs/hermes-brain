# Receipt — Footer LK Flagship DEV→Production

- Data/hora: 2026-06-30T15:52:24.569934+00:00
- Agente/profile/cron: lk-shopify
- Empresa/área: LK Sneakers / Shopify / Theme
- Responsável humano: Lucas Cimino / lk-shopify
- Pedido original: Adicionar informações da loja física LK Flagship ao footer, corrigindo Sábx para Sáb, respeitando fluxo DEV antes de Production.
- Classificação: external-write
- Fontes usadas:
- Telegram Lucas 2026-06-30; GitHub PR #122; Shopify Admin GraphQL readback; public section render endpoint; public full-page curl.
- O que foi feito:
- Honcho conclusion salvo; skill lk-shopify-theme-cro patchada com DEV-first obrigatório; PR #120 revertido por ter pulado DEV; patch aplicado no tema DEV 155065450718; PR #122 mergeado em production; assets exatos sincronizados no tema Production 155065417950 após DEV readback + PR merge.
- Output/artefato:
- Footer config/assets em Shopify Production readback OK: Rua Melo Alves, 344; Jardins — São Paulo, SP; Seg–Sex 10h–19h; Sáb 10h–18h; Tel (11) 2367-1467; Google Maps URL. Section render público atualizado. Full-page HTML público ainda retornou cache antigo no footer em curl, apesar de Admin/section render OK.
- Aprovação: APROVAÇÃO EXPLÍCITA ATUAL: Lucas Telegram 2026-06-30 confirmou 'Sim, corrigir para Sáb e executar em Production'; depois determinou o escopo/processo 'sempre, deve subir no DEV, depois, fazer o MERGE para o PRODUCTION' e em seguida 'fazer do 1 ao 5'. Escopo limitado aos assets sections/lk-footer.liquid e sections/footer-group.json dos temas DEV e Production.
- Envio/publicação: Telegram DM
- Writes externos: GitHub PR #122 merge; Shopify themeFilesUpsert DEV e Production para sections/lk-footer.liquid e sections/footer-group.json; Honcho conclusion; skill patch; user memory add.
- Riscos/bloqueios: Full-page Shopify/public cache ainda pode mostrar footer antigo por curto período; section render público e Admin readback já estão corretos. Processo DEV-first foi registrado para evitar repetição.
- Rollback/mitigação: Reverter PR #122 e/ou restaurar snapshots em /opt/data/profiles/lk-shopify/workdirs/footer-store-info-20260630/prod_before_* via DEV-first + PR; para Shopify Production, reupsert dos snapshots exatos se necessário com aprovação.
- Próximos passos: Rechecar full-page public footer até substituir cache antigo; se persistir, abrir investigação específica de cache/render de footer-group sem alterar escopo.

## Follow-up mobile — 2026-06-30

- Pedido adicional de Lucas: no mobile, adicionar as informações da LK Flagship logo abaixo da descrição `Curadoria de sneakers e lifestyle premium desde 2023. Jardins, São Paulo — onde o estilo encontra autenticidade.`
- Processo correto seguido: patch aplicado primeiro no DEV theme `lk-new-theme/dev` (`155065450718`), readback DEV OK, depois PR GitHub `#123` mergeado em `production`, e asset exato `sections/lk-footer.liquid` sincronizado/readback no Shopify Production theme `155065417950`.
- Mudança: criado bloco mobile-only `.ft__brand-mobile-store` abaixo de `.ft__brand-desc`; no mobile, a coluna accordion duplicada da loja (`.ft__col--store`) fica oculta; desktop preserva a coluna normal.
- QA público: section render `?sections=sections--20761715572958__footer` confirmou `ft__brand-desc` antes de `ft__brand-mobile-store` e presença de `Rua Melo Alves, 344`, `Jardins — São Paulo, SP`, `Seg–Sex: 10h–19h`, `Sáb: 10h–18h`, `Tel:`, `(11) 2367-1467`, `maps.google.com` e `Como chegar`.
- Rollback adicional: reverter PR `#123` e/ou restaurar `/opt/data/profiles/lk-shopify/workdirs/footer-store-info-20260630/mobile-followup/prod_before_root_lk-footer.liquid` via DEV-first + PR.

- Onde foi documentado no Brain: Honcho conclusion + Memory + skill lk-shopify-theme-cro + AGENTS + este receipt Brain.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
