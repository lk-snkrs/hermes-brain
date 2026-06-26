# Shopify-first correction — GMC link_template

- Criado UTC: 2026-06-22T17:49:55.280874+00:00
- Correção Lucas: “tecnicamente, temos que corrigir na Shopify, depois o GMC sincroniza de lá”.
- Decisão: lote 100 via Merchant API direto **não executado**.
- values_printed=false.

## O que mudou no fluxo

Antes, o micro-piloto 10 provou que `productInputs.patch` direto no Merchant API remove a issue no readback imediato. Porém isso não garante correção durável se o feed/Simprosys/Shopify for o upstream que sincroniza novamente.

A partir desta correção, o fluxo canônico é:

1. Identificar fonte upstream Shopify/Simprosys/feed.
2. Corrigir a fonte upstream.
3. Aguardar/sincronizar GMC.
4. Usar Merchant API para readback/status, não como write primário.
5. Merchant API direct patch só como exceção documentada.

## Evidência read-only coletada

### Micro-piloto 10

- 10/10 com `linkTemplate`, `mobileLinkTemplate`, `adsRedirect` OK.
- 0/10 com `mhlsf_full_missing_valid_link_template` no readback follow-up.
- Usar como diagnóstico técnico, não como padrão de escala.

### Shopify sample inspect

Arquivo:
- `shopify-source-inspect-sample-variants.json`

Amostra de 3 variants do micro-piloto mostrou:
- metafields `mm-google-shopping` de produto/variante existem para `color`, `gender`, `age_group`, `google_product_category`, `condition`, etc.
- não apareceu metafield Shopify óbvio para `linkTemplate`, `mobileLinkTemplate`, `adsRedirect` ou `store_code`.

Interpretação: o campo provavelmente nasce em configuração de feed/Simprosys/local feed, não em metafield simples de produto. Ainda assim, o dono upstream continua sendo Shopify/app/feed, não patch direto no GMC.

## Artefato canônico atualizado

- `areas/lk/sub-areas/growth/AGENTS.md`
- Backup: `AGENTS.md.bak-20260622T174804Z`
- Regra adicionada: `Correção Lucas — GMC/feed link_template é Shopify-first`.

## Próximo passo permitido

Read-only:
- mapear configuração Simprosys/local feed e campos Shopify usados pelo app;
- identificar se existe metafield/configuração Shopify que controla local link template;
- preparar approval packet de correção upstream.

## Próximo passo bloqueado

- Não executar `GMC lote 100 link_template` via Merchant API direto.
- Não escalar micro-piloto direto para 100/500/1000 até fonte upstream estar confirmada.

## Approval boundary

Qualquer write em Shopify app/config/feed/Simprosys/supplemental feed/Shopify metafield exige aprovação explícita nova com escopo upstream definido.
