# Receipt — PDP pi-preorder-card encomenda copy fix

- Data/hora: 2026-06-27T19:08:19.997787+00:00
- Agente/profile/cron: lk-shopify
- Empresa/área: LK / Shopify
- Responsável humano: lk-shopify
- Pedido original: Lucas reportou que produto com tag encomenda nunca deve mostrar Atendimento humano no card pi-preorder-card; correto é Sujeito a encomenda.
- Classificação: external-write
- Fontes usadas:
- URL pública reportada; GitHub production source; public HTML before/after QA. Shopify CLI Admin GraphQL foi tentado, mas OAuth oficial não estava armazenado neste runtime; não foi usado Admin raw.
- O que foi feito:
- PR #115 criado e mergeado em production com patch mínimo em sections/lk-pdp.liquid: dentro de div.pi-preorder-card, texto alterado de Atendimento humano LK/Fale com a equipe para Sujeito a encomenda. Classe pi-preorder-card e condição product.tags contains encomenda/pre-order preservadas.
- Output/artefato:
- PR #115 MERGED; merge commit 996fba6a8cd2e4617dd14e44d32577af702c1543; GitHub production readback match=true; old_copy_removed=true; new_copy_present=true; class_preserved=true; tag_condition_preserved=true. QA público na PDP Salomon XT-6 Vanilla Ice Oxford Tan: tentativa 2 HTTP 200, Liquid errors 0, pi-preorder-card=true, has_old_copy=false, has_new_copy=true; values_printed=false.
- Aprovação: Aprovação explícita de Lucas no Telegram: CORRIGIR POR FAVOR, para corrigir o card pi-preorder-card do produto com tag encomenda para sempre exibir Sujeito a encomenda no lugar de Atendimento humano.
- Envio/publicação: Telegram
- Writes externos: GitHub production PR merge. Sem produto/preço/estoque/Tiny/GMC/Klaviyo/ads/WhatsApp/email/checkout.
- Riscos/bloqueios: Baixo: copy-only no PDP preorder/encomenda card. Mitigado por PR mínimo, GitHub readback e QA público. Shopify Admin GraphQL CLI precisa renovar OAuth para próximos readbacks Admin oficiais.
- Rollback/mitigação: Reverter PR #115 / merge commit 996fba6a8cd2e4617dd14e44d32577af702c1543; não recomendado salvo regressão visual.
- Próximos passos: Para próximos edits no pi-preorder-card, manter Sujeito a encomenda para tag encomenda; usar Shopify CLI oficial quando OAuth for renovado.
- Onde foi documentado no Brain: Workdir /opt/data/profiles/lk-shopify/workdirs/pi-preorder-card-encomenda-fix-20260627; skill lk-shopify-theme-cro atualizada; receipt canônico no Brain.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
