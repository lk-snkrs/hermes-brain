# LK — Auditoria de reconciliação com relatório Pareto/Maicon — Abril 2026

## Fonte auditada

- Arquivo: `Resultados-de-Marketing-e-E-commerce-or-LK-Sneakers.pdf`
- Período do PDF: `2026-04-01` a `2026-04-30`
- Responsável citado por Lucas: Maicon / Pareto
- Extração local: `/opt/data/lk_pareto_april_pdf_extract/extracted.txt`

## Conclusão curta

Os números de **Meta Ads do relatório Pareto batem exatamente** com a consulta direta no Meta Ads quando a conta `act_1242062509867163` é consultada em nível de anúncio para abril/2026 e usando compra/valor canônicos. Para Lucas, uma aderência de **99%+** já é operacionalmente correta; diferenças pequenas de poucos reais não devem travar a análise se a lógica/metodologia estiver igual à Pareto.

A divergência principal está em **Shopify/receita total**: o PDF mostra `233 pedidos` e `R$ 722.636,36`; a Shopify Admin API retorna os mesmos `233 pedidos web pagos/parcialmente reembolsados`, mas `R$ 772.659,42` em `total_price`. Isso indica que Maicon/Pareto provavelmente usou uma métrica de receita líquida/Shopify Analytics/GA4 ajustada, não o `total_price` bruto do Admin API.

## Números globais — PDF vs auditoria Hermes

### Meta Ads

- PDF Pareto:
  - Investimento: `R$ 38.954,76`
  - Compras: `229`
  - Receita Meta: `R$ 797.654,65`
  - ROAS: `20,48`
  - CPA: `R$ 170,11`

- Hermes via Meta Marketing API:
  - Investimento: `R$ 38.954,76`
  - Compras canônicas: `229`
  - Valor Meta canônico: `R$ 797.654,65`
  - ROAS: `20,48`
  - CPA: `R$ 170,11`

Status: **bate exatamente**.

### Shopify / e-commerce

- PDF Pareto:
  - Receita total: `R$ 722.636,36`
  - Pedidos: `233`
  - Ticket médio: `R$ 3.101,44`
  - Sessões: `166K`
  - Conversão: `0,14%`

- Hermes via Shopify Admin API:
  - `source_name=web` + `financial_status in paid/partially_refunded`: `233 pedidos`
  - `total_price`: `R$ 772.659,42`
  - `subtotal_price`: `R$ 771.688,97`

Status: **contagem de pedidos bate; receita não bate**. Hipótese operacional: Pareto usa Shopify Analytics/GA4/receita líquida ajustada; Hermes estava usando Admin API `total_price`, que é bruto demais para reproduzir o painel.

## Ranking de influencers — Pareto vs Hermes

Critério do PDF: “soma de todas as compras registradas nos anúncios vinculados a cada influencer no CSV do Meta Ads”.

Consulta Hermes: Meta API, nível `ad`, abril/2026, fields `campaign_name`, `adset_name`, `ad_name`, `spend`, `actions`, `action_values`; compra canônica preferindo `offsite_conversion.fb_pixel_purchase`.

### Linhas que batem exatamente

- Ju Mesquita:
  - PDF: `9 anúncios`, `20 compras`, `R$ 2.663,19 spend`, `R$ 58.595,44 receita`, ROAS `22,00`
  - Hermes: `9 anúncios`, `20 compras`, `R$ 2.663,19 spend`, `R$ 58.595,44 receita`

- Arlindo:
  - PDF: `3 anúncios`, `16 compras`, `R$ 2.071,87 spend`, `R$ 75.312,65 receita`, ROAS `36,35`
  - Hermes: `3 anúncios`, `16 compras`, `R$ 2.071,87 spend`, `R$ 75.312,65 receita`

- Fiorela:
  - PDF: `9 anúncios`, `12 compras`, `R$ 1.833,69 spend`, `R$ 42.691,50 receita`, ROAS `23,28`
  - Hermes: `9 anúncios`, `12 compras`, `R$ 1.833,69 spend`, `R$ 42.691,50 receita`

- Maria:
  - PDF: `2 anúncios`, `2 compras`, `R$ 907,85 spend`, `R$ 741,54 receita`, ROAS `0,82`
  - Hermes, quando filtrado para `Maria` sem misturar `Maria Fernanda/Mariah`: `2 anúncios`, `2 compras`, `R$ 907,85 spend`, `R$ 741,54 receita`

### Linhas com diferença explicável

- Silvia:
  - PDF: `32 anúncios`, `38 compras`, `R$ 10.829,11 spend`, `R$ 144.971,35 receita`
  - Hermes por padrão textual `silvia`: `31 anúncios`, `38 compras`, `R$ 10.829,11 spend`, `R$ 144.971,35 receita`
  - Hermes com alias ampliado `Silvia Henz` capturou `35 anúncios`, `39 compras`, `R$ 11.181,85 spend`, `R$ 147.131,35 receita`, porque incluiu uma linha `AD02 [EST] Onitsuka México` com compra e provável creative/campanha associada a Silvia. Para bater Pareto, usar exatamente o naming `silvia` do CSV e não aliases ampliados demais.

- Lala Noleto:
  - PDF: `4 anúncios`, `55 compras`, `R$ 7.104,56 spend`, `R$ 166.660,76 receita`
  - Hermes pegando todos os anúncios com `lala`: `15 anúncios`, `55 compras`, `R$ 7.155,62 spend`, `R$ 166.660,76 receita`
  - Os `55` e a receita batem. A diferença de `R$ 51,06` vem de anúncios Lala ativos no fim de abril com zero compra/zero receita, principalmente variações `Lala-Nolleto start 30-04-2026`. Pareto aparentemente contou menos anúncios/spend zero-conversão no ranking.

- Helena:
  - PDF separa:
    - `Helena`: `18 anúncios`, `20 compras`, `R$ 1.885,82`, `R$ 52.569,88`
    - `Helena 4 camp. abril`: `9 anúncios`, `12 compras`, `R$ 2.066,94`, `R$ 54.844,88`
    - Total consolidado declarado no PDF: `32 compras`
  - Hermes consolidado por pessoa: `23 anúncios`, `32 compras`, `R$ 3.952,76`, `R$ 107.414,76`
  - Compras e receita total batem com a soma do PDF; diferença é apenas agrupamento/nomenclatura.

## Aprendizado metodológico

1. Para reproduzir o relatório Pareto de Meta, consultar **Meta Ads direto**, nível `ad`, no período fechado do mês.
2. Usar compra/valor canônico, preferindo `offsite_conversion.fb_pixel_purchase`, sem somar aliases.
3. Para bater Pareto por influencer, o agrupamento deve respeitar o naming do CSV/Pareto, não consolidar tudo automaticamente por pessoa. Exemplo: Helena foi separada em dois blocos no PDF, apesar de poder ser consolidada para leitura gerencial. **Maria/Maria Fernanda/Mariah devem ficar separadas** no modo Pareto-compatible; a regra ampla `maria` não pode engolir `maria fernanda` nem `mariah`.
4. Para leitura operacional LK, são necessárias duas visões:
   - **Pareto-compatible**: reproduz exatamente o CSV/naming do Maicon.
   - **Lucas-operacional**: consolida aliases por pessoa e cruza com Shopify/produto/SKU/tamanho.
5. Shopify como ponte funciona para produto vendido, mas não deve ser confundido com total de receita do painel. A ponte segura é pedido/produto via texto/cupom/UTM/referrer/note/tag ou `ad_id` exato; `campaign_id`/`adset_id` continuam inseguros.
6. Para bater a receita total do relatório mensal, Hermes precisa usar a mesma métrica do painel de origem: Shopify Analytics/GA4/net sales. Admin API `total_price` é útil para pedido/produto, mas não reproduz automaticamente o `R$ 722.636,36` do PDF.

## Criativos/imagens

O erro anterior foi usar `thumbnail_url` do Meta. Auditei agora:

- `thumbnail_url` retornado pela Marketing API para criativos ativos veio em `64×64 px`.
- Isso explica as imagens borradas/erradas no e-mail.
- `image_url` muitas vezes não existe para criativos de post/story/video.
- Query de `effective_object_story_id` exige permissão `pages_read_engagement` / Page Public Content Access, então o token atual não consegue puxar asset/post completo por esse caminho.
- A API `/AD_ID/previews` funciona e retorna iframes de preview de anúncio. Teste local carregou alguns criativos de forma nítida, mas outros ficaram em branco; serve para auditoria interna/screenshot, não como fonte direta estável para e-mail de produção sem captura/validação.

Regra aprendida: **não colocar thumbnail 64×64 do Meta em e-mail LK**. Para incluir criativos rodando, usar uma destas fontes:

1. screenshot validado do endpoint `/previews` por `ad_id`;
2. asset exportado/fornecido pela Pareto/Maicon;
3. permissão Page/Instagram suficiente para baixar mídia do post/story em qualidade real;
4. ou auditoria visual separada, não o e-mail semanal produto-first.

## Próxima correção recomendada

- E-mail semanal: manter DesignMD LK + ranking produto-first.
- Adicionar seção “Criativos rodando” apenas quando houver screenshot nítido validado por `ad_id`/preview, nunca `thumbnail_url` 64×64.
- Criar modo mensal “Pareto-compatible” para abril/meses fechados, com duas abas/seções:
  - Meta/Pareto: números que batem exatamente com Ads Manager.
  - Shopify/produto: produto vendido por influencer somente com ponte segura.
