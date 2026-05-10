# Rotina — LK Weekly Influencer Sales Email

## Status

Ativa a partir de 2026-05-10.

## Cadência

- Toda quarta-feira às 10h BRT.
- Cron Hermes em UTC: `0 13 * * 3`.
- Janela principal: últimos 7 dias completos em America/Sao_Paulo, encerrando no dia anterior ao envio.
- Comparativo: 7 dias imediatamente anteriores.

## Objetivo

Enviar por e-mail um relatório comparativo de vendas por influencer para entender:

- quais influencers geraram venda Shopify com ponte verificável;
- quais influencers tiveram sinal Meta forte sem ponte Shopify;
- variação semana contra semana;
- produtos vendidos por influencer quando houver ponte Shopify;
- lacunas de tracking/cupom/UTM que impedem leitura operacional.

## Script

- `scripts/lk_weekly_influencer_sales_report.py`

Execução manual read-only sem envio:

```bash
/opt/hermes/.venv/bin/python scripts/lk_weekly_influencer_sales_report.py
```

Execução com envio por Gmail:

```bash
/opt/hermes/.venv/bin/python scripts/lk_weekly_influencer_sales_report.py --send
```

O script grava artefatos locais em:

```text
/opt/data/lk_weekly_influencer_sales_reports/
```

## Metodologia

### Meta Ads

- Fonte: Meta Ads direto, conta `act_1242062509867163`.
- Nível: `ad`.
- Campos de identificação: `campaign_id`, `adset_id`, `ad_id`, `campaign_name`, `adset_name`, `ad_name`.
- Regra Maicon/Pareto: o nome da influencer vem primeiro de `ad_name`; `adset_name`/`campaign_name` ficam só como fallback/discovery. Como pode haver múltiplos anúncios por influencer, o cálculo soma todas as linhas/ad_ids matched no nível `ad`.
- Métrica de compra: uma action key canônica por anúncio, preferindo `offsite_conversion.fb_pixel_purchase`.
- Nunca somar aliases Meta como compras diferentes:
  - `purchase`;
  - `omni_purchase`;
  - `offsite_conversion.fb_pixel_purchase`.
- Quando houver comparação mensal com Maicon/Pareto, usar modo `Pareto-compatible`: seguir naming/agrupamento Pareto, aceitar 99%+ como correto e não consolidar nomes que a Pareto separou.
- Regra conhecida do modo Pareto-compatible: separar `Maria`, `Maria Fernanda` e `Mariah`; a regra ampla `maria` não pode capturar `maria fernanda` nem `mariah`.

### Shopify

- Fonte: Shopify Admin API, read-only.
- Atribuição por influencer somente quando existe ponte verificável em:
  - discount code;
  - UTM/landing site/referrer com nome/código textual do influencer;
  - note attributes;
  - note;
  - tags;
  - `ad_id` Meta exato em `utm_content`, `ad_id` ou `fb_ad_id`, quando esse `ad_id` pertence a anúncio identificado como influencer no Meta.
- `campaign_id` e `adset_id` genéricos não são ponte suficiente para produto/influencer, porque vários influencers podem compartilhar a mesma campanha/adset.
- Quando houver `ad_id` Meta exato, ele prevalece sobre matches textuais fracos que possam vir de fornecedor, tag interna ou texto de produto.
- Produtos vendidos só aparecem quando há ponte Shopify verificável.
- Sempre mostrar nome do produto + SKU + variante/tamanho quando disponível.

## Output do e-mail

O e-mail deve conter:

1. Período atual e período comparativo.
2. Visual fiel ao DesignMD da LK Sneakers: editorial, premium, fundo `paper`, header preto, títulos serifados e UI em sans minimalista.
3. Ranking principal produto-first: cada linha é `influencer × produto vendido × SKU × tamanho`, agregado por influencer + SKU + variante/tamanho.
4. Shopify com ponte: quantidade vendida, receita e tipo de ponte (`texto` vs `ad_id Meta`).
5. Meta canônico como sinal secundário: compras atribuídas, spend e valor Meta por influencer.
6. Seção separada para `meta_signal_only`: influencers com compra/valor Meta sem produto Shopify atribuível.
7. Corpo do e-mail como `Content-Type: text/html`, não apenas multipart/texto.
8. Não incluir thumbnails/criativos Meta borrados ou de baixa qualidade no e-mail semanal.
9. Criativos reais podem aparecer em preview HTML local somente com flag explícita `--include-creative-assets`; o cron semanal permanece sem criativos por padrão.
10. Quando criativos forem exibidos, a estrutura correta é `influencer → criativo → vendas → produtos`: cada card deve mostrar imagem do criativo, compras/spend/valor Meta, pedidos/receita Shopify por `ad_id` exato e produtos vendidos ligados ao criativo quando houver ponte segura.

## Auditoria visual de criativos

Criativos continuam fora do e-mail semanal por padrão. Para curadoria interna, usar:

```bash
/opt/hermes/.venv/bin/python scripts/lk_weekly_creative_audit.py
```

O script gera JSON + HTML DesignMD LK em `/opt/data/lk_weekly_creative_audits/`. A rotina agora tenta imagens reais antes de iframe: campos de `creative`, `video.thumbnails` e `asset_feed_spec.images[].hash` via `/{ad_account}/adimages`; baixa os assets localmente, escolhe a melhor imagem por resolução, evita fallback 64×64 quando houver alternativa, detecta frames pretos/sidebars com `ffmpeg` e renderiza imagem local no HTML. A saída é `local_only`: não envia e-mail, não muda campanhas e não persiste URLs-fonte com tokens/secrets no JSON/HTML versionado.

Para prévia executiva local do relatório semanal com criativos reais já colhidos, usar explicitamente:

```bash
/opt/hermes/.venv/bin/python scripts/lk_weekly_influencer_sales_report.py \
  --include-creative-assets \
  --creative-assets-json /opt/data/lk_weekly_creative_audits/lk-weekly-meta-creative-assets-YYYY-MM-DD.json
```

Guardrail: `--include-creative-assets` continua bloqueado junto com `--send` por padrão. Para preparar o caminho de e-mail com imagens reais, o script suporta MIME `multipart/related` com imagens inline por CID, mas exige flag explícita `--allow-send-creative-assets-inline` depois de QA/aprovação. Antes de qualquer envio externo com criativos, gerar o `.eml` sem enviar e auditar:

```bash
/opt/hermes/.venv/bin/python scripts/lk_weekly_influencer_sales_report.py \
  --include-creative-assets \
  --allow-send-creative-assets-inline \
  --email-mime-preview /tmp/lk-weekly-inline-preview.eml \
  --creative-assets-json /opt/data/lk_weekly_creative_audits/lk-weekly-meta-creative-assets-YYYY-MM-DD.json
```

O `.eml` deve ser `multipart/related`, conter `src="cid:..."`, anexar as imagens como `Content-ID`, ter zero `file://` no HTML e zero query params sensíveis. A prévia local cruza o `ad_id` do criativo com Shopify: produtos entram no card do criativo somente quando existe `ad_id` Meta exato no pedido; pontes por texto/cupom continuam no nível influencer para não inventar qual vídeo gerou a venda. Só promover um criativo para e-mail/relatório executivo depois de QA visual; duplicados ou frames fracos devem ser removidos/substituídos.

## Guardrails

- Read-only: não muda campanha, orçamento, Shopify, Tiny, Klaviyo, WhatsApp, banco ou produção.
- Não expõe tokens, e-mails sensíveis, refresh tokens ou secrets.
- Gmail usa credenciais via Doppler no processo; valores não são gravados no repo.
- Meta ROAS/valor é sinal de plataforma, não ROAS operacional final da LK.
- O e-mail semanal não deve usar layout genérico de dashboard nem thumbnails Meta de baixa qualidade; qualquer artefato visual deve seguir `areas/lk/design/DESIGN.md`.
- Produto vendido sem ponte Shopify não deve ser inventado.

## Mission Control

Este módulo entra no Mission Control como:

- Negócio: LK Sneakers.
- Área: Tráfego Pago / Influencer Intelligence.
- Tipo: relatório recorrente externo aprovado por Lucas.
- Frequência: semanal, quarta 10h BRT.
- Risco: L4 apenas pelo envio externo de e-mail; coleta é read-only.
- Evidência: arquivo gerado em `/opt/data/lk_weekly_influencer_sales_reports/` e cron Hermes ativo.
