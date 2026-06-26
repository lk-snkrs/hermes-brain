# Receipt — mKFashion symmetric spacing adjustment

Data: 2026-06-09
Perfil: LK Shopify
Repo: `lk-snkrs/lk-new-theme`

## Pedido

Lucas pediu aumentar o espaçamento em cima do botão do Provador e deixar o espaçamento de baixo igual ao de cima.

## Implementação

Ajuste aplicado no botão mKFashion / Provador Virtual:

- `window.__MK.anchor.*.style` agora usa:
  - `margin-top:8px`
  - `margin-bottom:8px`
- Runtime tuner do host agora usa:
  - `host.style.margin = '8px 0';`

Mantido:

- CTA limpo com texto `Provar Virtualmente`.
- Sem ícone.
- Sem badge `NEW`.
- Fundo branco, texto preto, borda clara.
- `Compre Já` visível.

## Fluxo

### DEV primeiro

PR: https://github.com/lk-snkrs/lk-new-theme/pull/53
Merge commit: `bd224f8bc984`

Verificações DEV:

```text
PASS origin/dev symmetric spacing verification
PASS shopify_dev_symmetric_spacing_readback
```

Readback DEV:

- Theme: `155065450718`
- Name: `lk-new-theme/dev`
- Role: `unpublished`
- `anchor_symmetric`: 3
- `host_symmetric`: 1
- `old_top_only`: 0
- `old_host`: 0
- `cta_style`: 3
- `button_text`: 1
- `NEW`: 0
- `width:24px`: 0

### Production depois

PR: https://github.com/lk-snkrs/lk-new-theme/pull/54
Merge commit: `df8ddd3bb9f0`

Verificações Production:

```text
PASS origin/production symmetric spacing verification
PASS shopify_production_symmetric_spacing_readback
```

Readback Production:

- Theme: `155065417950`
- Name: `lk-new-theme/production`
- Role: `main`
- `anchor_symmetric`: 3
- `host_symmetric`: 1
- `old_top_only`: 0
- `old_host`: 0
- `cta_style`: 3
- `button_text`: 1
- `NEW`: 0
- `width:24px`: 0

## Public storefront status

Após o merge/readback correto, o preview/público ainda retornou HTML stale nos rounds da sessão:

```text
FAIL main_theme_preview_symmetric_spacing_retry
```

Sinais do HTML stale:

- `anchor_symmetric`: 0
- `host_symmetric`: 0
- `cta_style`: 0
- `button_text`: 0
- `icon24`: 1

Conclusão honesta: GitHub + Shopify Admin/main theme estão atualizados, mas a camada pública/preview consultada pela ferramenta ainda estava servindo versão antiga em cache/edge no momento da verificação. Não declarar storefront público 100% até nova checagem pública passar.

## Non-actions

- Não houve write direto via Shopify Admin/Asset API.
- Não houve alteração de produto, preço, estoque, checkout, app config, GMC, Klaviyo, WhatsApp ou campanha.
- Segredos não foram impressos.

## Rollback

- Reverter DEV spacing: `bd224f8bc984`
- Reverter Production spacing: `df8ddd3bb9f0`

## Referência atualizada

Referência `lk-mkfashion-zero-touch-button-placement-20260609.md` atualizada com o padrão: espaçamento do Provador deve ser simétrico, alvo `8px` em cima e `8px` embaixo.
