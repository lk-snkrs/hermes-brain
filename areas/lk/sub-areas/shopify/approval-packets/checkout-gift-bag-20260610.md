# Approval packet — LK checkout gift bag option

Date: 2026-06-10
Owner: LK Shopify
Surface: Shopify Checkout / Checkout UI Extension / custom app

## Pedido

Adicionar opção de sacola de presente no checkout, se compatível com Shopify Plus / Checkout Extensibility.

## Evidência read-only

- Shopify Admin `shop.json`: loja `LK`, domínio `lk-sneakerss.myshopify.com`.
- Plano: `Shopify Plus` (`plan_name=shopify_plus`).
- App installations read-only: app custom existente `lk-checkout-trust`, developer `LK SNEAKERS LTDA`, handle `lk-checkout-trust`.
- Checkout profiles read-only: existem 2 perfis; `Copy of LK Sneakers configuration` está publicado e `LK Sneakers configuration` não publicado.
- Busca local por `shopify.app.toml` em `/opt/data`: nenhum repositório Shopify app encontrado localmente nesta máquina.
- Busca local por diretórios/app com `checkout`/`trust`: nenhum código do app `lk-checkout-trust` encontrado; apenas artefatos de tema/receipts e o preview local criado para `lk-gift-bag-checkout`.
- GitHub read-only via token Doppler: usuário autenticado `lk-snkrs`; 28 repositórios acessíveis escaneados. Busca por repositórios/código `lk-checkout-trust`, `checkout-trust`, `purchase.checkout`, `ui_extension` encontrou somente referência documental em `lk-snkrs/lk-new-theme/docs/TEST_COVERAGE_SUMMARY.md`, sem código de Checkout UI Extension.
- Repositório `lk-snkrs/LK-Shopify` clonado read-only em `/opt/data/tmp/lk-shopify-repo-readonly`: contém apenas `README.md`; nenhum `shopify.app.toml`, `shopify.extension.toml`, `purchase.checkout` ou código de app/extension.
- Secrets verificados por presença via Doppler: `SHOPIFY_STORE_URL`, `SHOPIFY_ACCESS_TOKEN` e GitHub token disponível; valores não foram impressos.

## Interpretação

A loja tem plano compatível para extensão no checkout. O caminho mais limpo é usar Checkout UI Extension, preferencialmente reaproveitando/alterando o app custom `lk-checkout-trust` se o código-fonte estiver disponível. Sem o repositório do app, é necessário localizar o código no GitHub/Shopify Partners ou criar uma extensão/app novo.

## Preview funcional proposto

No checkout, renderizar um bloco discreto no fluxo de compra:

- Título: `Sacola de presente`
- Texto: `Adicionar sacola de presente ao pedido`
- Se pago: adicionar produto/variant “Sacola de presente” ao carrinho/checkout via extensão, com preço definido no produto Shopify.
- Se grátis: gravar atributo/metafield/nota de pedido para operação separar a sacola no fulfillment.

## Risco

- Checkout UI Extension é app/checkout-adjacent: qualquer deploy/configuração afeta checkout e exige aprovação escopada.
- Se for produto pago, cria dependência de produto/variant, preço e comportamento de quantidade; preço/produto também exigem aprovação.
- Se for só atributo/nota, não cobra do cliente e depende de operação ler o campo corretamente.
- Sem código-fonte do app `lk-checkout-trust`, não dá para alterar com segurança ainda.

## Rollback

- Se for extensão no app existente: reverter commit/deploy da extensão ou desabilitar o bloco no app/config.
- Se for produto pago: remover/desabilitar a extensão e manter/remover o produto “Sacola de presente” conforme decisão.
- Antes de qualquer deploy: snapshot do app/config e readback do checkout.

## Decisões capturadas

- Lucas confirmou que a sacola será grátis.
- Lucas aprovou criar um novo app/extensão para preview/dev, sem ativar em produção.
- Como o código-fonte do app `lk-checkout-trust` não foi encontrado, o caminho aprovado é app/extensão nova.

## Execução aprovada — scaffold local

- Projeto local criado em `/opt/data/projects/lk-gift-bag-checkout-app`.
- Extensão criada em `/opt/data/projects/lk-gift-bag-checkout-app/extensions/gift-bag`.
- Target: `purchase.checkout.block.render`.
- Atributo gravado: `lk_gift_bag`.
- Valores: `yes` quando marcado; `no` quando desmarcado.
- Copy do bloco: `Adicionar sacola de presente ao pedido`.
- Texto auxiliar: `Cortesia LK. A sacola acompanha o pedido quando disponível para o envio.`
- API version usada: `2025-07`, porque a implementação atual é React-based e a documentação Shopify indica 2025-07 como última versão com suporte a componentes React.
- `shopify.app.toml` está com `client_id = "PENDING_SHOPIFY_APP_CLIENT_ID"`; antes do deploy precisa vincular/criar o app real no Shopify Partners/CLI.

## Verificação local

- `npm install`: concluiu com `0 vulnerabilities`.
- `npm run build`: concluiu com `BUILD_EXIT=0`.
- Build reportado pela Shopify CLI: `lk-gift-bag-checkout successfully built in 545ms (114.6 KB original, ~36.9 KB compressed)`.
- Secret scan local do projeto, excluindo `node_modules`: `secret_like_hits=[]`.

## Execução aprovada — login e vínculo Shopify CLI

- Lucas pediu o link de login do Shopify CLI e concluiu o login.
- Shopify CLI confirmou conta atual: `lk@lksneakers.com.br`.
- Projeto vinculado/criado no Shopify Partners sob a organização `LK SNEAKERS LTDA (50805400)`.
- App criado/vinculado: `lk-gift-bag-checkout`.
- Configuração gerada e definida como default: `shopify.app.lk-gift-bag-checkout.toml`.
- Build pós-vínculo: `BUILD_EXIT=0`; Shopify CLI reportou `lk-gift-bag-checkout built!`.

## Execução aprovada — deploy da extensão

- Lucas aprovou: `deploy da extensão agora, sem ativar no checkout ainda`.
- Comando executado: `shopify app deploy --path /opt/data/projects/lk-gift-bag-checkout-app --no-color`.
- Shopify CLI solicitou confirmação de release para nova extensão `lk-gift-bag-checkout`; confirmação aplicada dentro do escopo aprovado.
- Resultado: `New version released to users`.
- Versão/release: `lk-gift-bag-checkout-2`.
- Link do Dev Dashboard: `https://dev.shopify.com/dashboard/50805400/apps/380136325121/versions/1005640450049`.
- `shopify app info` pós-deploy confirmou:
  - configuration file: `shopify.app.lk-gift-bag-checkout.toml`
  - app name: `lk-gift-bag-checkout`
  - user: `lk@lksneakers.com.br`
  - component: `ui_extension`, path `extensions/gift-bag`, config `shopify.extension.toml`
  - dev store: `Not yet configured`

## Bloqueio atual

- A extensão foi deployada no app, mas **não foi ativada/posicionada no Checkout Editor**.
- Para aparecer no checkout, ainda precisa posicionar o bloco no perfil publicado `Copy of LK Sneakers configuration` via Checkout Editor/Admin.
- Ativação/posicionamento no Checkout Editor é checkout live/config write e requer aprovação explícita separada.

## Próxima decisão necessária

1. Aprovar ativar/posicionar o bloco `Sacola de presente` no Checkout Editor do perfil publicado `Copy of LK Sneakers configuration`.
2. Depois disso, aprovar pedido de teste/controlado ou outro método de QA do checkout.

## Não feito

- Nenhuma ativação no Checkout Editor.
- Nenhuma alteração de produto, preço, estoque, tema ou checkout live além do deploy da versão da extensão aprovado.
