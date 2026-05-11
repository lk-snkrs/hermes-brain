# Rotina — LK Creative Pipeline

## Loop
Hipótese → criativo/campanha → teste → dados Meta/Klaviyo/Shopify → conclusão → próxima ação.

## Aprovação
Qualquer campanha/envio externo precisa aprovação Lucas.

## Gate visual obrigatório

Imagens de criativos continuam fora de e-mail/relatório executivo por padrão. Para qualquer inclusão visual:

1. Usar apenas asset local já auditado, sem URL com token e sem thumbnail 64×64.
2. Exigir resolução mínima, arquivo decodificável, contraste suficiente, sem frame preto e sem barras laterais pretas.
3. Considerar check automático como triagem, não aprovação.
4. Exigir aprovação humana explícita de Lucas/equipe antes de promover para e-mail, relatório executivo, campanha ou cron.
5. Atribuir produto ao criativo somente com ponte Shopify por `ad_id` exato; cupom/texto fica no nível influencer.

Artefato validado: `areas/lk/sub-areas/trafego-pago/rotinas/creative-visual-approval-gate-readonly-2026-05-11.md`.

## Observação
Meta Ads token constava inválido no snapshot antigo; verificar Doppler e autenticação antes de usar.
