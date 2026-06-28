# Receipt — PDP Product Suggestions v3 DEV family fallback

- Data/hora: 2026-06-27T11:14:38.861733+00:00
- Agente/profile/cron: lk-shopify
- Empresa/área: LK / Shopify
- Responsável humano: lk-shopify
- Pedido original: Lucas aprovou DEV Product Suggestions v3 no PDP com fallback família ALD hats, sem Production merge.
- Classificação: external-write
- Fontes usadas:
- Approval packet areas/lk/sub-areas/shopify/approval-packets/pdp-product-suggestions-v3-dev-family-fallback-20260627.md; DEV Shopify Theme 155065450718; asset sections/lk-pdp.liquid; public preview QA; simulation read-only.
- O que foi feito:
- Snapshot DEV salvo; asset sections/lk-pdp.liquid atualizado no DEV Theme 155065450718; Product Suggestions v3 adiciona marker data-lk-related-v3=family-fallback-20260627, fallback família ald-hats, bloqueio cross-type, dedupe Curadoria LK e eligibility pending_unknown.
- Output/artefato:
- PUT 200; readback 200; SHA12 antes 776e9099ffc8, target/readback abbd4afa0169; node --check OK; preview HTTP 200 e Liquid errors 0 nos PDPs Saint George, AJ1 Panda, Onitsuka Mexico 66, NB9060 Quartz Grey e Vomero Premium; simulação Saint George retorna 4 bonés ALD via family-fallback-ald-hats; values_printed=false.
- Aprovação: Aprovo dev
- Envio/publicação: Telegram
- Writes externos: Shopify DEV theme Asset API only: Theme 155065450718, asset sections/lk-pdp.liquid. Sem Production merge; sem produto/preço/estoque/Tiny/GMC/Klaviyo/ads/WhatsApp/email.
- Riscos/bloqueios: Médio: JS client-side e family fallback; mitigado por strict cross-type block, dedupe Curadoria, hide-if-weak e DEV-only. Elegibilidade Stock ainda pending/unknown, sem promessa de disponibilidade.
- Rollback/mitigação: Restaurar /opt/data/profiles/lk-shopify/workdirs/pdp-product-suggestions-v3-20260627/dev/dev_before_sections__lk-pdp.liquid no DEV Theme 155065450718 ou remover marker data-lk-related-v3, familyFallbacks e data-lk-stock-eligibility, voltando ao Product Suggestions v2.
- Próximos passos: Lucas testar preview DEV; aguardar lk-stock para contrato de elegibilidade antes de qualquer Production merge; se aprovado, preparar PR Production mínimo separado.
- Onde foi documentado no Brain: Workdir /opt/data/profiles/lk-shopify/workdirs/pdp-product-suggestions-v3-20260627/dev; approval packet e reports v3 no Brain.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar. Este arquivo canônico é cópia regularizada do output do writer, porque o writer voltou a salvar no espelho profile-local.
