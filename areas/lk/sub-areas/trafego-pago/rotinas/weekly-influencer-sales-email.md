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

- quais influencers geraram venda Shopify com ponte textual verificável;
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
- Campos de identificação: `campaign_name`, `adset_name`, `ad_name`.
- Métrica de compra: uma action key canônica por anúncio, preferindo `offsite_conversion.fb_pixel_purchase`.
- Nunca somar aliases Meta como compras diferentes:
  - `purchase`;
  - `omni_purchase`;
  - `offsite_conversion.fb_pixel_purchase`.

### Shopify

- Fonte: Shopify Admin API, read-only.
- Atribuição por influencer somente quando existe ponte textual verificável em:
  - discount code;
  - UTM/landing site;
  - referrer;
  - note attributes;
  - note;
  - tags.
- Produtos vendidos só aparecem quando há essa ponte Shopify.
- Sempre mostrar nome do produto + SKU + variante/tamanho quando disponível.

## Output do e-mail

O e-mail deve conter:

1. Período atual e período comparativo.
2. Ranking por influencer.
3. Shopify com ponte: pedidos, receita e variação WoW.
4. Meta canônico: compras atribuídas, spend e valor Meta.
5. Produtos vendidos por influencer com nome + SKU + tamanho.
6. Indicação explícita quando o influencer tem sinal Meta, mas ponte Shopify ausente.

## Guardrails

- Read-only: não muda campanha, orçamento, Shopify, Tiny, Klaviyo, WhatsApp, banco ou produção.
- Não expõe tokens, e-mails sensíveis, refresh tokens ou secrets.
- Gmail usa credenciais via Doppler no processo; valores não são gravados no repo.
- Meta ROAS/valor é sinal de plataforma, não ROAS operacional final da LK.
- Produto vendido sem ponte Shopify não deve ser inventado.

## Mission Control

Este módulo entra no Mission Control como:

- Negócio: LK Sneakers.
- Área: Tráfego Pago / Influencer Intelligence.
- Tipo: relatório recorrente externo aprovado por Lucas.
- Frequência: semanal, quarta 10h BRT.
- Risco: L4 apenas pelo envio externo de e-mail; coleta é read-only.
- Evidência: arquivo gerado em `/opt/data/lk_weekly_influencer_sales_reports/` e cron Hermes ativo.
