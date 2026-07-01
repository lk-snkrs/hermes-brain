# Receipt — Elle store-location institutional fix

- Data/hora: 2026-07-01T10:59:30.156100+00:00
- Agente/profile/cron: lk-ops
- Empresa/área: LK / atendimento / Elle Chatwoot
- Responsável humano: Lucas Cimino approval; lk-ops execution
- Pedido original: Lucas pediu corrigir a falha da Elle que tratava pergunta institucional de loja física/SP como stock_handoff.
- Classificação: external-write
- Fontes usadas:
- Auditoria Elle 26h; app.py runtime; elle_brain_v2.py policy; regression local/container; health público; HMAC signed/unsigned; OpenRouter verifier; autonomy gate; learner smoke.
- O que foi feito:
- Separada intenção institucional de loja física/endereço/SP de intenção de estoque/disponibilidade/retirada/pronta entrega; adicionada função is_store_location_institutional_question em app.py; ajustado hard_stock e is_stock_availability_request; removido loja fisica de STOCK_TERMS do Elle Brain v2 e adicionada política de pure location; adicionada regressão 24b; buildada e recriada imagem canonical-20260701-store-location-fix.
- Output/artefato:
- Imagem ativa elle-chatwoot:canonical-20260701-store-location-fix; container elle-chatwoot Up; perguntas “vocês têm loja física em SP?”, “A loja de vocês fica em SP?” e “tem loja física?” => category=institutional handoff=false com Rua Melo Alves, 344 — Jardins/SP; “tem na loja física o tamanho 37?” e “tem pronta entrega no tamanho 37?” => stock_handoff handoff=true; py_compile OK; regression 45/45 OK; health ok=true; hmac signed=202 ignored unsigned=401 unauthorized; drift status=ok; OpenRouter 1h OK; autonomy 1h go eval_bad=0; learner status=ok auto_apply=false writes_external=0.
- Aprovação: Aprovado por Lucas no Telegram: “Corrigir por favor” após auditoria apontar over-conservative loja física vs estoque.
- Envio/publicação: Sem envio ativo WhatsApp/e-mail/campanha. HMAC smoke usou payload no-op/outgoing que retorna ignored.
- Writes externos: Docker runtime rebuild/recreate da Elle aprovado pelo pedido; nenhum Chatwoot/WhatsApp/Shopify/Tiny write de cliente; HMAC smoke no-op.
- Riscos/bloqueios: Perguntas institucionais de loja física agora respondem endereço; se cliente mencionar tamanho/disponibilidade/retirada/pronta entrega/reserva, permanece lk-stock/Larissa. Não consultar estoque direto.
- Rollback/mitigação: Rollback image: elle-chatwoot:rollback-before-store-location-fix-20260701T1048Z-store-location-fix. Backup source: /opt/data/backups/elle-store-location-fix-20260701T1048Z-store-location-fix. Para rollback: restaurar compose image/tag anterior e recriar via Doppler, ou docker tag rollback como canonical e compose up -d --no-build --force-recreate.
- Próximos passos: Monitorar próximas 24h para confirmar 0 eval_bad relacionado a loja física; se surgir pergunta de endereço com retirada/reserva, manter stock_handoff.
- Onde foi documentado no Brain: Receipt no Brain e regressão em /opt/elle-chatwoot/tests/elle_brain_v2_regression.py.
- Source confidence: runtime-verificado

## Memory OS v1.4

Este receipt foi criado pelo wrapper local `/opt/data/scripts/hermes_memory_os_receipt_writer.py`, que valida campos mínimos e chama o hook Memory OS após salvar.
