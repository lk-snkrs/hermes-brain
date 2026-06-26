# SEMrush/CNRUSH cross-check — LK Growth

Data UTC: `2026-06-19T00:11:00Z`
values_printed=false

## Pedido

Lucas pediu para considerar também a outra provedora de tecnologia/API — interpretada aqui como `SEMrush`/`CNRUSH` pela fala — e verificar insights e EANs.

## Status de integração

Verificações feitas:

- runtime Doppler `lk-growth`: nenhum env/secret com nomes `SEMRUSH`, `SEM_RUSH`, `CNRUSH`, `CN_RUSH` ou `AHREFS` apareceu injetado.
- inventário `hermes-cli-integrations`: nenhum conector SEMrush/CNRUSH/Ahrefs listado.

Conclusão: análise SEMrush/CNRUSH live ainda não é decision-grade porque não há integração/secret disponível neste perfil. Não foi impresso nenhum valor de secret.

## O que dá para fazer sem SEMrush API

1. Usar os exports/prints/CSV do SEMrush se Lucas enviar.
2. Rodar validação pública contra os mesmos blocos: robots, status code, canonical, links quebrados, parâmetros, schema.
3. Cruzar SEMrush vs Ahrefs para detectar divergências reais vs crawler-specific.
4. Separar falsos positivos causados por bloqueio de bot, ex.: `SemrushBot` bloqueado no robots.

## Observação sobre SemrushBot

O `robots.txt` foi corrigido em formato, mas ainda contém bloqueio conservador:

```txt
User-agent: SemrushBot
Disallow: /
```

Isso pode limitar auditorias SEMrush. Não é erro de sintaxe; é regra de bloqueio. Se quisermos SEMrush como auditor recorrente, precisa decisão separada para liberar SemrushBot ou permitir rotas específicas.

## EAN/GTIN — checagem Shopify read-only

Fonte: Shopify Admin GraphQL read-only. Não consulta estoque.

Amostra coletada:

- produtos ativos checados: `1000`
- variantes checadas: `7391`
- variantes com barcode/EAN/GTIN presente e comprimento válido: `4596`
- variantes sem barcode/EAN/GTIN: `2795`
- variantes com comprimento inválido: `0`
- missing rate: `37.82%`

Leitura: existe oportunidade grande de qualidade de dados para Merchant/feed. Isso deve ser tratado como `Shopify/GMC product data quality`, não como issue SEMrush puro.

## Recomendação

P1 — Decision packet EAN/GTIN:

- exportar lista priorizada de variantes sem barcode por marca/coleção/produto com tráfego/receita/GMC impact;
- cruzar com GMC diagnostics quando disponível;
- mapear origem de preenchimento: Shopify variant barcode, Simprosys mapping, supplemental feed;
- NÃO preencher EAN em massa sem fonte confiável por risco de GTIN incorreto.

P2 — SEMrush live:

- se Lucas tiver CSV/export ou API key, importar read-only;
- comparar issue-by-issue contra Ahrefs;
- separar `real`, `crawler-specific`, `blocked by robots`, `already fixed awaiting recrawl`.

## Próxima ação anexada ao recheck 12h

Adicionar ao job `lkahrefswave2r12h`:

- considerar SEMrush/CNRUSH se integração/export estiver disponível;
- reportar explicitamente que SemrushBot está bloqueado se a ferramenta continuar acusando limitação;
- incluir EAN/GTIN como trilha separada de Merchant/product data quality.
