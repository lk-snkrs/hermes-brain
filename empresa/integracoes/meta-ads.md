# Integração — Meta Ads / Instagram

## Escopo

Meta Ads e Instagram apoiam análise de mídia, públicos, criativos e campanhas.

## Secrets Doppler

- `META_ACCESS_TOKEN`
- IDs de contas/páginas/ad accounts quando documentados no Doppler.

## Read-only

- Consultar contas, páginas, campanhas, conjuntos, anúncios, insights e status.
- Consultar Meta Ads Insights por campanha/adset/ad para gasto, impressões, cliques, compras e valor atribuído pela plataforma.
- Analisar criativos, influenciadores e hipóteses sem alterar entrega.
- Cruzar Meta Ads com GA4 e Shopify antes de recomendar escala/pausa: Meta é atribuição de plataforma; Shopify continua fonte oficial de pedidos/receita.

## Write

- Criar drafts/planejamentos no Brain.
- Criar campanhas/adsets/anúncios na plataforma não é write rotineiro; tratar como external/admin conforme impacto.

## External-send

- Publicar post, anúncio, campanha, mensagem ou comentário exige aprovação/preview de Lucas.

## Admin/destructive

- Alterar orçamento, status de campanhas, públicos, pixels, permissões, billing, tokens ou apagar ativos exige aprovação explícita + rollback.

## Regra

- Não prometer performance sem dados consultados. Separar hipótese, dado observado e recomendação.
- ROAS/compras do Meta Ads não são verdade operacional final; tratar como atribuição da plataforma e reconciliar com Shopify, GA4, UTMs e cupons.
- ROAS extremo com gasto muito baixo é sinal para investigar, não autorização para escalar orçamento.

## Escala de permissões

- Read-only: consultar metadados, status, listas, métricas e registros sem alterar dados.
- Write: criar/atualizar dados internos, tags, notas, segmentos ou configurações não destrutivas.
- External-send: enviar mensagem, email, campanha, notificação ou contato com cliente/lead/parceiro. Exige preview e aprovação de Lucas.
- Admin/destructive: apagar dados, alterar credenciais, webhooks, domínios, billing, permissões, deploys, containers, produção ou integrações críticas. Exige aprovação explícita, plano de backup e rollback.

Regra de secrets: este arquivo lista apenas nomes de secrets no Doppler `lc-keys/prd`; valores reais nunca entram no GitHub.
