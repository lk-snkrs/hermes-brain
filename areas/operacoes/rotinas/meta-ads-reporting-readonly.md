# Rotina — Meta Ads Reporting Read-only

Objetivo: consultar performance de Meta Ads/Instagram sem alterar campanhas, orçamentos ou criativos.

## Integração

- Doc: `empresa/integracoes/meta-ads.md`.
- Secret: `META_ACCESS_TOKEN`.
- Áreas: LK tráfego pago; Zipper comunicação quando aplicável.

## Permissões

- Read-only: insights, campanhas, conjuntos, anúncios, spend, métricas e criativos existentes.
- Write: criar draft de campanha/criativo em documento é permitido; criar no Meta Ads exige aprovação.
- External-send: publicar anúncio, post ou campanha exige preview e aprovação Lucas.
- Admin/destructive: orçamento, pause/enable, billing, pixel, permissões, deletes exigem aprovação explícita + rollback.

## Procedimento

1. Definir conta, período e métrica.
2. Consultar insights read-only.
3. Comparar com GA4/Shopify quando necessário.
4. Entregar análise com ressalvas de atribuição.
5. Se houver recomendação operacional, separar como proposta; não executar alteração.

## Saída esperada

Resumo com período, fonte, métricas principais, hipótese e próxima recomendação para aprovação.
