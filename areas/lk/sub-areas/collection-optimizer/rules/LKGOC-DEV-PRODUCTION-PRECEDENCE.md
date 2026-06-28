# LKGOC — precedência DEV, Contract Lock, Admin API e Production

Atualizado: 20260627T165047Z
Status: **regra canônica de precedência** para resolver conflitos históricos.

## Resumo executivo

- **DEV/unpublished/branch pode ser usado para construir preview, QA visual e approval packet LKGOC**, desde que o alvo seja verificado e o estado seja claramente draft/preview.
- **Contract Lock não bloqueia sandbox DEV**, mas continua obrigatório para chamar a entrega de LKGOC aprovada e para qualquer promoção/merge/publicação/customer-facing.
- **Production/main/customer-facing é bloqueado** sem aprovação explícita atual de Lucas + rollback + readback + receipt.
- **Shopify Admin API mutations/write direto são bloqueados por padrão**. Preferir fluxo versionado GitHub/branch/DEV; exceção só com aprovação escopada e readback.

## Ordem de precedência

1. Approval explícita atual de Lucas para Production/main/hotfix/customer-facing vence, desde que haja escopo, rollback e readback.
2. Esta regra vence wording antigo que diga “nenhum write Shopify antes de Contract Lock” quando o destino for DEV/unpublished/branch draft.
3. Esta regra não libera Production, main, deploy público, metafield/tag/page/customer-facing, campanha, GMC/Klaviyo/Meta ou Tiny.
4. Política Shopify CLI oficial e GitHub-first/no Admin writes vence scripts/wrappers antigos.

## DEV/unpublished permitido

Permitido sem nova aprovação quando o pedido de Lucas for seguir/fazer/refazer/normalizar/preview dentro do LKGOC e o destino for seguro:

- tema com `role: unpublished` verificado por API/CLI oficial quando aplicável;
- branch/local preview versionado quando aplicável;
- workdir/packet marcado como draft ou DEV;
- sem publicação customer-facing;
- sem mutação Admin direta salvo exceção aprovada;
- com rollback/readback/QA antes de link de approval.

## Production/main proibido por padrão

Bloqueado sem aprovação explícita atual:

- theme `role: main`;
- merge/deploy para Production;
- Shopify object/metafield/tag/page/SEO field público;
- GMC/feed, Klaviyo, Meta, Tiny, email/WhatsApp ou qualquer write externo customer-facing.

## Contract Lock

Contract Lock é obrigatório para:

- declarar “LKGOC aprovado/pronto”;
- enviar approval packet final;
- promover DEV → Production;
- replicar para lote;
- qualquer mudança customer-facing.

Contract Lock deve conter gold source 204L/Moon Shoe, media manifest, guide pattern, acceptance tests, rollback e QA desktop/mobile.

## Estoque

LKGOC não consulta estoque diretamente. Qualquer disponibilidade, pronta entrega, grade/tamanho, ruptura, reposição ou divergência Tiny/Shopify stock é handoff para `lk-stock`.

## Receipt

Toda execução relevante deve fechar com receipt/handoff/approval packet e declarar:

- fonte verificada;
- writes locais e externos;
- risco;
- rollback;
- próximo passo/owner;
- se Reminder OS loop é necessário.
