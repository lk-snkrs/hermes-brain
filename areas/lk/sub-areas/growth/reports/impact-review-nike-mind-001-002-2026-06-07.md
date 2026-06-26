# Impact review ~7 dias — Guia Nike Mind 001/002 + coleção Nike Mind

Data: 2026-06-07
Escopo: read-only, sem writes externos.
URLs:
- Guia: https://www.lksneakers.com.br/pages/guia-nike-mind-001-002
- Coleção: https://www.lksneakers.com.br/collections/nike-mind-001

## Evidências coletadas

- Script obrigatório executado via Doppler: `lk_growth_impact_review.py` com Shopify Admin, GA4 REST, GSC, GMC e fetch público.
- Fetch público adicional executado via Python requests/parser stdlib.
- DataForSEO SERP live executado para `nike mind 001` Brasil/pt-BR, custo reportado pela API: 0.002.

## Status resumido

- Guia: HTTP 200, canonical correto, indexável, conteúdo Nike Mind 001/002 presente, FAQPage JSON-LD único, links para coleção e produtos presentes.
- Coleção: HTTP 200, canonical correto, indexável, grid público com links de produtos, Shopify Admin encontrou coleção ativa com 18 produtos.
- GA4: dados read-only disponíveis para sessões/users/views; conversão/receita não foram retornadas pelo script por fallback de métrica inválida.
- GSC: acesso disponível, mas sem linhas para as URLs nos períodos consultados.
- GMC: acesso disponível; amostra de 250 itens trouxe 1 match Nike Mind, sem issues retornadas nesse item; não valida o feed completo.
- Classificação: parcialmente decision-grade para saúde pública/tráfego; não decision-grade para impacto comercial final por falta de conversão/receita/pedidos e GSC sem volume por URL.

## Métricas GA4

Período atual: 2026-05-31 a 2026-06-06. Comparativo anterior: 2026-05-24 a 2026-05-30.

- Coleção `/collections/nike-mind-001`: 158 sessões vs 141 (+17 / +12,1%); 146 usuários vs 137 (+9 / +6,6%); 177 views vs 154 (+23 / +14,9%).
- Guia `/pages/guia-nike-mind-001-002`: 13 sessões vs 2 (+11 / +550%); 10 usuários vs 1 (+9 / +900%); 18 views vs 4 (+14 / +350%).

## GSC

- Site property: `sc-domain:lksneakers.com.br`.
- Período atual consultado: 2026-05-28 a 2026-06-04.
- Resultado: sem linhas para guia e coleção; portanto sem cliques, impressões, CTR ou posição atribuíveis no recorte.

## SERP/DataForSEO

Consulta: `nike mind 001`, Google organic live, Brasil/pt, desktop, depth 10.

- LK não apareceu no top 10 retornado.
- Top resultados: Nike Brasil posições 1 e 2; Instagram posição 3; Mercado Livre posição 4; JR Tênis posição 5; Droper posição 6; Nike.com posição 7.
- Sinal: há SERP competitiva e ainda sem visibilidade orgânica top 10 para a LK na keyword exata no snapshot.

## Riscos

- Janela curta e baixo volume do guia: crescimento percentual alto, mas base muito pequena.
- Sem conversão/receita no GA4 retornado pelo script; não dá para afirmar impacto comercial.
- GSC sem dados por URL no recorte; pode ser atraso/baixo volume/indexação recente.
- GMC validado apenas por amostra; full feed Nike Mind ainda não está coberto por este review.
- Parser público detectou links/produtos, mas navegação global inclui link de produto não Nike Mind; contagem de grid deve considerar os 18 produtos da coleção no Shopify Admin.

## Recomendações

1. Manter guia e coleção publicados como estão; não há quebra pública crítica.
2. Rodar nova revisão em 7–14 dias com GSC mais maduro e GA4 corrigido para métricas de compra/receita compatíveis.
3. Corrigir o script/consulta GA4 para usar métricas válidas de ecommerce antes de chamar impacto de venda.
4. Fazer QA full do GMC/feed para todos os produtos Nike Mind, sobretudo atributos de produto/GTIN quando aplicável.
5. Preparar, sem publicar, pacote de otimização SERP para tentar entrar no top 10 da keyword exata: reforço de links internos, snippets citáveis e possível ajuste de title/meta/FAQ após dados GSC.

## Aprovação

- Sem aprovação necessária para nova auditoria read-only, relatório interno, QA público ou preparação de pacote.
- Exige aprovação explícita de Lucas antes de qualquer alteração visível em produção: title/meta, conteúdo do guia, coleção, theme, feed/GMC, campanhas ou CRM.
