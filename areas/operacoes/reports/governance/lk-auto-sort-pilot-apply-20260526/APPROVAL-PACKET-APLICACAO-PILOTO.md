# Approval packet — Aplicação piloto auto-ordenação coleções LK

Data: 2026-05-26
Destino: LK Growth / Shopify Collections
Status: aprovado por Lucas para piloto, mas execução externa não realizada nesta etapa; documentação e pacote de execução preparados.

## Pedido limpo

Aplicar piloto de auto-ordenação nas 10 coleções aprovadas, com:

- produtos esgotados sempre no final;
- snapshot de rollback antes da aplicação;
- readback pós-aplicação;
- sem criação de cron.

## Coleções aprovadas para piloto

1. Nude Project — https://www.lksneakers.com.br/collections/nude-project
2. Jacquemus — https://www.lksneakers.com.br/collections/jacquemus
3. Saint Studio — https://www.lksneakers.com.br/collections/saint-studio
4. Calça | Apparels — https://www.lksneakers.com.br/collections/calca-streetwear
5. Pace — https://www.lksneakers.com.br/collections/pace
6. Aimé Leon Dore — https://www.lksneakers.com.br/collections/aime-leon-dore
7. Nike Mind — https://www.lksneakers.com.br/collections/nike-mind-001
8. Onitsuka Tiger Mexico 66 — https://www.lksneakers.com.br/collections/onitsuka-tiger-mexico-66
9. Onitsuka Tiger Mexico 66 Sabot — https://www.lksneakers.com.br/collections/onitsuka-tiger-mexico-66-sabot
10. Shorts — https://www.lksneakers.com.br/collections/shorts

## Evidências já existentes

Artefatos base:

- `areas/lk/sub-areas/growth/reports/auto-sort-collections/2026-05-26-v2-guardrails/REPORT-V2-GUARDRAILS.md`
- `areas/lk/sub-areas/growth/reports/auto-sort-collections/2026-05-26-v2-guardrails/dry-run-v2-guardrails.json`
- `areas/lk/sub-areas/growth/reports/auto-sort-collections/2026-05-26-v2-guardrails/top8-preview-v2-guardrails.csv`
- `areas/lk/sub-areas/growth/reports/auto-sort-collections/2026-05-26-v2-guardrails/rollback-snapshot-v2-guardrails.json`
- `areas/lk/sub-areas/growth/reports/auto-sort-collections/2026-05-26-v2-guardrails/APPROVAL-PACKET-PILOT-LINKS.md`

Resumo do dry-run V2:

- 177 coleções lidas.
- 118 elegíveis após guardrails.
- 59 puladas/revisão.
- 104 elegíveis mudariam o top 8.
- 10 pilotos recomendados/aprovados.
- Nenhum Shopify write foi executado no dry-run.
- Nenhum cron foi criado.

## Preview da regra de aplicação

A aplicação final deve gerar a ordem por coleção nesta sequência:

1. separar produtos com estoque Tiny confirmado como zerado;
2. montar top 8 dos produtos não esgotados:
   - mínimo 4 slots protegidos para best-sellers/performance;
   - até 4 slots para novidades dos últimos 90 dias;
   - completar faltantes por performance;
3. ordenar restante dos produtos não esgotados por performance com pequeno boost de recência;
4. anexar produtos esgotados no final;
5. gerar moves somente para produtos cuja posição muda;
6. aplicar `collectionReorderProducts` em lotes seguros;
7. poll do job assíncrono até finalizar;
8. fazer readback da coleção e comparar top 8 + últimos produtos esgotados;
9. registrar receipt.

## Risco

- A ordenação afeta vitrine pública e pode alterar conversão das coleções piloto.
- A regra sem camada de estoque poderia promover produto esgotado; por isso a aplicação final precisa recomputar a ordem com Tiny antes do write.
- Coleções com muitos movimentos podem ter leitura visual bastante diferente após aplicação.
- O dado de acessos/GA4 por produto ainda não entrou no scoring; performance usa unidades + receita 180d.

## Bloqueios / não executado nesta etapa

- Não foi executado `collectionReorderProducts` nesta etapa.
- Não foi criado cron.
- Não houve alteração de produto, preço, estoque, tema, checkout, SEO, tags, campanha ou comunicação.
- Antes da aplicação real, o script de apply deve validar estoque Tiny no momento da execução e gravar receipt/readback.

## Rollback

Rollback aprovado/planejado:

- snapshot base: `rollback-snapshot-v2-guardrails.json`;
- restaurar `current_order_product_ids` das 10 coleções;
- aplicar `collectionReorderProducts` inverso por coleção;
- poll do job;
- readback e comparação com snapshot original;
- registrar receipt de rollback.

## Próxima decisão

Para executar de fato no Shopify, o próximo passo operacional precisa rodar o apply com a camada Tiny/sold-out ativa, gerando:

- snapshot imediatamente antes do write;
- moves calculados por coleção;
- readback pós-aplicação;
- relatório de receipt;
- sem criar cron.

Frase de execução operacional recomendada:

> Executar agora o apply do piloto Shopify nas 10 coleções aprovadas, usando Tiny para empurrar esgotados ao final, com snapshot imediato, readback e sem cron.
