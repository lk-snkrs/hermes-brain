# Receipt — Judge.me para WhatsApp pós-entrega LK

Data: 2026-06-13T12:23:24+00:00
Perfil: lk-ops
Escopo: inspeção read-only solicitada por Lucas sobre usar Judge.me/nota no template pós-entrega.

## Fontes consultadas

- Doppler `lc-keys/prd`, somente presença/ausência de secrets.
- Shopify Admin API, read-only:
  - smoke `shopify_lk`: HTTP 200.
  - GraphQL `appInstallations`: HTTP 200.
  - REST themes/assets do tema principal, GET apenas.
- Judge.me API, read-only:
  - `/api/v1/reviews` com token público e privado.
  - `/api/v1/shops/info`.
  - `/api/v1/widgets/settings`.
- Judge.me docs YAML público: `/api/docs.yaml`.

## Evidência sanitizada

- `values_printed=false` em todos os probes de credenciais/API.
- Secrets presentes:
  - `SHOPIFY_STORE_URL`: OK
  - `SHOPIFY_ACCESS_TOKEN`: OK
  - `JUDGEME_API_TOKEN`: OK
  - `JUDGEME_PRIVATE_TOKEN`: OK
- Secrets ausentes esperados apenas como aliases opcionais:
  - `JUDGEME_SHOP_DOMAIN`: missing, não bloqueia porque o domínio vem de `SHOPIFY_STORE_URL`.
  - `JUDGEME_PUBLIC_TOKEN`: missing, não bloqueia porque existe `JUDGEME_API_TOKEN`.
- Shopify apps instalados: 36 apps. Matches de reviews:
  - Reputon Reviews
  - Judge.me Reviews
- Tema principal Shopify:
  - `lk-new-theme/production`, role `main`, id `155065417950`.
  - `config/settings_data.json`: menções Judge.me encontradas, incluindo bloco `judgeme_core/...`.
  - `layout/theme.liquid`: classes/snippets `jdgm-*` encontrados.
  - `templates/product.json`: seção/bloco `judgeme_review_widget` encontrado.
- Judge.me API:
  - `/reviews` com `JUDGEME_API_TOKEN`: HTTP 403, token público sem permissão suficiente para reviews index.
  - `/reviews` com `JUDGEME_PRIVATE_TOKEN`: HTTP 200, retornou 1 review no teste `per_page=1`.
  - `/shops/info`: HTTP 200, retornou objeto `shop` com chaves de configuração/plan/platform/widget_version etc.; PII não copiada.
  - `/widgets/settings`: HTTP 200.
- Docs públicas Judge.me:
  - Caminhos disponíveis relevantes: `/widgets/product_review`, `/widgets/preview_badge`, `/reviews`, `/reviews/count`, `/reviewers/*`, `/shops/info`, `/settings`.
  - Não foi identificado endpoint público/documentado de criação de “review request link” único por pedido.

## Veredito operacional

Judge.me está instalado e funcional como camada de reviews na Shopify LK. Há credencial privada válida para leitura da API e widgets ativos no tema. Para WhatsApp pós-entrega, o caminho mais seguro é CTA para avaliação via página de produto/Judge.me widget ou fluxo configurado do próprio Judge.me, não prometer neste momento URL única por pedido sem validação extra.

## Guardrails

- Nenhum write em Shopify/Judge.me.
- Nenhum envio WhatsApp/campanha.
- Nenhum valor de secret impresso.
- Nenhum dado pessoal copiado para este receipt.

## Probe adicional — descoberta de link de avaliação

Após pergunta do Lucas sobre como descobrir o link do Judge.me, rodei probe read-only em produto ativo Shopify + widget Judge.me:

- Produto de amostra lido via Shopify Admin GET: `accolade-straight-leg-sweatpant-charcoal-green`.
- Judge.me `/widgets/product_review` para o handle: HTTP 200, retornou chaves `product_external_id` e `widget`.
- O HTML retornado pelo widget não expôs `form action` nem link direto de submissão no payload sanitizado.
- Página pública do produto expôs recursos Judge.me, incluindo:
  - `https://app.judge.me/reviews/stores/lksneakers.com.br`
  - `https://api.judge.me`
  - assets `cdn.judge.me` / `cdnwidget.judge.me`
  - app block `judgeme_core/...`
- Conclusão: existe link público geral de reviews da loja e widget por produto, mas ainda não está provado link único por pedido/cliente. Próxima descoberta deve ser via dashboard/configuração de Review Requests do Judge.me ou inspeção autenticada do link usado nos e-mails automáticos, sem enviar mensagem real.

## Recomendação de template

Criar template separado de avaliação pós-entrega, provavelmente categoria Marketing, com CTA `Avaliar minha compra`. Se quiser manter Utility, usar copy de suporte/satisfação sem nota explícita.
