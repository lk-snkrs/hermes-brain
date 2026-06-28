# Receipt — PDP pi-preorder-card encomenda full historical copy restore

- Data/hora: 2026-06-27T19:18:33.738101+00:00
- Agente/profile/cron: lk-shopify
- Empresa/área: LK / Shopify
- Responsável humano: lk-shopify
- Pedido original: Lucas corrigiu que o pi-preorder-card ainda estava errado: o correto antigo é Sujeito a encomenda, Confirme no WhatsApp, 4-6 semanas; pediu procurar como era e deixar como antigamente.
- Classificação: external-write
- Fontes usadas:
- Histórico Git de sections/lk-pdp.liquid; URL pública reportada; GitHub PR #116; public HTML after QA. Shopify Admin raw não usado.
- O que foi feito:
- PR #116 criado e mergeado em production restaurando o copy histórico completo do div.pi-preorder-card: Sujeito a encomenda · 4-6 semanas · Confirme no WhatsApp, com link wa.me/5511949565000 para confirmar disponibilidade. Preservadas classe pi-preorder-card e condição product.tags contains encomenda/pre-order.
- Output/artefato:
- PR #116 MERGED; merge commit b62fcf406ceee8e77ad5245f39b9809526f33977; GitHub production readback match=true; full_copy_present=true; whatsapp_link_present=true; wrong_atendimento_absent=true; class_preserved=true; tag_condition_preserved=true. QA público na PDP Salomon XT-6 Vanilla Ice Oxford Tan: tentativa 2 HTTP 200, Liquid errors 0, pi-preorder-card=true, has_sujeito=true, has_4_6=true, has_whatsapp=true, has_wrong_atendimento=false; values_printed=false.
- Aprovação: Aprovação/correção explícita de Lucas no Telegram: continua errado; o correto é sujeito a encomenda, confirme no whatsapp, 4-6 semanas; procure como era e deixe como era antigamente.
- Envio/publicação: Telegram
- Writes externos: GitHub production PR merge. Sem produto/preço/estoque/Tiny/GMC/Klaviyo/ads/WhatsApp send/email/checkout.
- Riscos/bloqueios: Baixo: copy-only no PDP preorder/encomenda card. Mitigado por histórico Git, PR mínimo, GitHub readback e QA público. Skill e memória corrigidas para exigir copy completo, não apenas Sujeito a encomenda.
- Rollback/mitigação: Reverter PR #116 / merge commit b62fcf406ceee8e77ad5245f39b9809526f33977; não recomendado porque restaura o padrão histórico correto.
- Próximos passos: Nenhum; ciclo fechado. Para futuros edits, manter sempre o copy completo histórico do pi-preorder-card.
- Onde foi documentado no Brain: Workdir /opt/data/profiles/lk-shopify/workdirs/pi-preorder-card-encomenda-restore-20260627; skill lk-shopify-theme-cro e memória atualizadas; receipt canônico no Brain.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
