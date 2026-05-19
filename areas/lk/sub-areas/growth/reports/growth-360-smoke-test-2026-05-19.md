# LK Growth — Smoke Test 360º

Data: 2026-05-19
Tipo: validação documental/read-only do fluxo completo
Status: base pronta; execução live completa depende de reload/restart para DataForSEO MCP ativo no agente.

## Objetivo

Validar se o LK Growth OS tem um fluxo claro para cruzar dados técnicos, comerciais, paid signals e conteúdo/GEO sem executar writes.

## Camadas verificadas no PR #129

- Shopify Admin: OK read-only.
- GA4 Data API: OK read-only via `GA4_LK_PROPERTY_ID` canônico.
- Google Search Console: OK read-only para `sc-domain:lksneakers.com.br`.
- Google Merchant Center: OK read-only via Content API.
- PageSpeed Insights / CrUX: OK read-only via API key dedicada.
- Klaviyo: OK read-only para accounts/lists/metrics.
- Meta: OK read-only para conta, campanhas e insights básicos.
- Ahrefs: OK read-only para métricas pontuais de domínio.
- Claude SEO: instalado/sincronizado como camada diagnóstica SEO/GEO/técnica.
- Claude Ads: instalado/sincronizado como camada paid/landing/creative.
- Claude Blog: instalado/sincronizado como content engine para brief, outline, FAQ, cluster e GEO/AEO.
- DataForSEO MCP: servidor instalado e list-tools validado; exposição no agente ativo pendente de reload/restart.

## Fluxo 360º esperado

1. Escolher uma página, PDP, collection, query, campanha ou issue GMC.
2. Classificar pelo `growth-decision-router.md`.
3. Buscar dados comerciais e de demanda primeiro.
4. Rodar camada diagnóstica adequada:
   - Claude SEO para técnico/on-page/schema/GEO.
   - Claude Ads para paid signals/landing/creative.
   - Claude Blog para conteúdo/FAQ/cluster/citabilidade.
5. Preencher `growth-audit-output-template.md`.
6. Separar fato, interpretação e recomendação.
7. Produzir approval packet quando houver write.
8. Registrar rollback e review de impacto quando uma mudança for aprovada.

## Smoke test mínimo aprovado para próxima execução live

Quando o agente for recarregado e DataForSEO estiver disponível no toolset ativo, executar uma amostra pequena:

- 1 PDP ou collection com tráfego relevante.
- 1 query informacional do GSC.
- 1 item/issue GMC ou status de produto.
- 1 sinal Meta/Klaviyo como contexto.
- 1 consulta DataForSEO/SERP com custo controlado.

Limites:

- `rowLimit` pequeno em GSC/GA4.
- sem exports grandes Ahrefs/DataForSEO.
- sem Shopify/GMC/Klaviyo/Ads writes.
- sem envio externo.

## Critérios de sucesso

- O relatório final declara se é decision-grade.
- Fontes faltantes são marcadas explicitamente.
- A recomendação é comercial, não apenas técnica.
- Qualquer ação produtiva vira approval packet, não execução automática.
- O impacto esperado e a revisão D+7 ficam definidos.

## Status atual

O sistema está pronto para auditorias 360º em modo read-only, exceto pelo uso nativo do DataForSEO dentro do agente atual, que requer reload/restart. Até lá, DataForSEO pode ser tratado como instalado/validado, mas não como toolset ativo nesta sessão.

## O que não foi feito

- Nenhum write em Shopify, GMC, GSC, GA4, Klaviyo, Meta, tema ou produção.
- Nenhuma campanha, envio, preço, estoque ou checkout alterado.
- Nenhum crawl/export pago em larga escala.
