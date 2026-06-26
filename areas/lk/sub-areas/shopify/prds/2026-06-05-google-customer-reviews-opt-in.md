# PRD — Google Avaliações do Consumidor: integração de permissão / opt-in

Data: 2026-06-05  
Empresa: LK Sneakers  
Merchant Center ID: `5297679409`  
Superfície: Shopify Plus / Google Merchant Center / Simprosys Google Shopping Feed  
Status: PRD + pacote de aprovação; sem write externo executado neste documento.

## 1. Problema

O Google Merchant Center informa que o Google Avaliações do Consumidor não exibe a notificação de permissão para clientes há mais de 30 dias. O programa exige que o módulo de opt-in seja renderizado na página de confirmação do pedido, com dados reais do pedido.

Snippet-base fornecido pelo Google:

```html
<script src="https://apis.google.com/js/platform.js?onload=renderOptIn" async defer></script>
<script>
  window.renderOptIn = function() {
    window.gapi.load('surveyoptin', function() {
      window.gapi.surveyoptin.render({
        "merchant_id": 5297679409,
        "order_id": "ORDER_ID",
        "email": "CUSTOMER_EMAIL",
        "delivery_country": "COUNTRY_CODE",
        "estimated_delivery_date": "YYYY-MM-DD",
        "products": [{"gtin":"GTIN1"}, {"gtin":"GTIN2"}]
      });
    });
  }
</script>
```

## 2. Evidência coletada

### Google

Fonte: Google Merchant Center Help — “Integrate the survey opt-in module”.

Requisitos relevantes:

- O módulo de opt-in deve estar em todas as páginas de confirmação de pedido.
- Deve usar HTTPS.
- Deve passar dados reais e precisos: `merchant_id`, `order_id`, `email`, `delivery_country`, `estimated_delivery_date`.
- A data estimada de entrega deve estar no formato `YYYY-MM-DD`.
- O `delivery_country` deve ser ISO 3166-1 alpha-2, exemplo `BR`, e não `ZZ`.
- O código deve ficar próximo ao fechamento do `</body>` quando há controle da página.
- A página precisa usar `<!DOCTYPE html>`.
- O e-mail de pesquisa só é enviado depois da data estimada de entrega.

### Shopify / Checkout Extensibility

Fontes: discussões Shopify Developer Community e Shopify Community sobre Google Customer Reviews pós-Checkout Extensibility.

Achados:

- O método antigo “Order Status Page > Additional Scripts” foi depreciado/removido em lojas migradas para Checkout Extensibility.
- Custom Pixels são sandboxed e não são uma solução confiável para renderizar o pop-up nativo do Google Customer Reviews.
- A própria comunidade aponta falta de suporte oficial direto para o snippet nativo em Checkout Extensibility, especialmente sem app dedicado.

### Estado LK lido via Shopify Admin — read-only

- Loja: `LK` / `lk-sneakerss.myshopify.com`.
- Plano: Shopify Plus (`shopifyPlus: true`).
- App instalado: `Simprosys Google Shopping Feed` (`handle: google-shopping-feed`).
- App instalado: `lk-checkout-trust`.
- App Google & YouTube não apareceu na lista lida.
- Home pública usa `<!DOCTYPE html>` e HTTPS.
- Home pública não contém `surveyoptin` nem `https://apis.google.com/js/platform.js`, o que é esperado porque o opt-in precisa estar na confirmação do pedido, não na home.

### Simprosys — correção de escopo após checagem no Admin

Fonte: suporte Simprosys + feedback operacional Lucas em 2026-06-05.

Achados atualizados:

- A documentação antiga/externa do Simprosys descreve Google Customer Reviews/SMPS, mas o app instalado `Simprosys Google Shopping Feed` na LK não expõe uma área visível de **Google Customer Reviews / Store Ratings / GCR**.
- O link encontrado no Admin aponta para `Proviews - Product Reviews Q&A` (`https://apps.shopify.com/proviews?...`), que é outro app de reviews da Simprosys, não a configuração nativa do opt-in gratuito do Google Customer Reviews no Merchant Center.
- Portanto, a hipótese “configurar pelo Simprosys Google Shopping Feed já instalado” fica rebaixada: só vale se o suporte Simprosys confirmar um módulo oculto/legado; não deve ser tratada como caminho garantido.
- A verificação correta ainda exige pedido-teste e confirmação de que o pop-up aparece na página de confirmação.
- O teste não deve usar e-mail do domínio da loja nem e-mail do Merchant Center.
- O pedido deve usar país/endereço suportado e sem VPN/proxy.

## 3. Hipótese de causa raiz

A integração do opt-in provavelmente não está ativa na confirmação de pedido após mudança/uso de Checkout Extensibility, ou está ativa em uma camada que não consegue renderizar o pop-up nativo do Google.

Como a LK é Shopify Plus e tem Simprosys instalado, o caminho mais seguro é primeiro configurar/validar o módulo via Simprosys, porque o app já é parte do stack de feed/GMC e tem documentação própria para Google Customer Reviews em Shopify.

## 4. Objetivo

Restabelecer a exibição do opt-in de Google Avaliações do Consumidor na página de confirmação de pedido da LK, usando Merchant ID `5297679409`, sem quebrar checkout, pagamento, rastreamento, feed, Simprosys, Appmax, Klaviyo, Rebuy, Judge.me ou demais apps.

## 5. Não-objetivos

- Não alterar preço, estoque, frete real, checkout de pagamento, fulfillment ou status de pedidos.
- Não mudar feed de produtos ou GMC ProductInput.
- Não enviar campanhas, e-mails, WhatsApp ou pesquisas manualmente.
- Não remover Simprosys, Judge.me, Reputon, Rivo, Klaviyo, Appmax ou app de checkout.
- Não mexer em produção sem backup/rollback e aprovação explícita do escopo.

## 6. Abordagens avaliadas

### Opção A — Recomendada: habilitar/configurar Google Customer Reviews pelo Simprosys

Resumo:

- Usar o app Simprosys Google Shopping Feed / SMPS Google Customer Reviews para ativar o opt-in.
- Configurar Merchant Center ID `5297679409`.
- Definir prazo estimado de entrega conservador para o Brasil, em dias corridos/úteis conforme opção do app.
- Validar por pedido-teste real controlado.

Prós:

- App já instalado na LK.
- Alinha com a documentação Simprosys para Shopify.
- Evita injeção manual de script em Checkout Extensibility.
- Menor risco de violar sandbox do Shopify.

Contras:

- Exige write/configuração dentro de app/GMC/checkout-adjacent.
- Pode exigir acesso administrativo ao app e/ou Merchant Center.
- Confirmação final depende de pedido-teste chegando à página de obrigado.

### Opção B — Custom checkout extension / app próprio

Resumo:

- Investigar `lk-checkout-trust` para incluir bloco/extensão de thank-you/order-status.

Risco:

- Checkout UI Extensions normalmente não permitem injetar arbitrary third-party script no top window.
- Pode não cumprir o formato nativo exigido pelo Google (`gapi.surveyoptin.render`).
- Maior tempo, maior risco e possivelmente solução não aceita pelo Google.

Uso recomendado:

- Apenas se Simprosys não suportar a conta/loja atual.

### Opção C — Custom Pixel

Resumo:

- Tentar adaptar snippet para Customer Events / Custom Pixel.

Veredito:

- Não recomendado. Comunidade Shopify reporta que o sandbox do pixel impede renderização correta do opt-in; pixel é melhor para tracking, não para popup nativo pós-compra.

### Opção D — Additional Scripts antigo

Resumo:

- Colar snippet na área antiga de Additional Scripts.

Veredito:

- Só é viável se a loja ainda tiver campo legado disponível. Em lojas migradas para Checkout Extensibility, esse caminho é depreciado/removido.

## 7. Requisitos funcionais

1. O opt-in deve aparecer na página de confirmação do pedido para pedidos elegíveis.
2. O Merchant ID deve ser `5297679409`.
3. `order_id` deve ser único e corresponder ao pedido Shopify.
4. `email` deve usar o e-mail real do cliente do pedido.
5. `delivery_country` deve usar o país de entrega, ex.: `BR`.
6. `estimated_delivery_date` deve ser calculado de forma conservadora e no formato `YYYY-MM-DD`.
7. Quando disponível, `products` deve passar GTINs reais; se GTIN estiver ausente, não inventar GTIN.
8. A integração não deve bloquear o carregamento do checkout/thank-you page.

## 8. Requisitos de segurança/privacidade

- Não expor tokens, e-mails reais ou dados pessoais em Telegram/Brain.
- Pedido-teste deve usar e-mail externo que não seja domínio LK e não seja e-mail do Merchant Center.
- Dados de pedido usados somente para o módulo oficial do Google Customer Reviews.
- Nenhum customer-facing send além do próprio fluxo esperado do Google após opt-in.

## 9. Plano de execução recomendado

### Fase 0 — Aprovação de escopo

Aprovação necessária de Lucas para:

- configurar o app Simprosys / Google Customer Reviews para Merchant ID `5297679409`;
- alterar configuração checkout-adjacent/app;
- fazer 1 pedido-teste controlado se necessário;
- reverter/desativar a configuração se o pop-up não aparecer ou houver efeito colateral.

### Fase 1 — Configuração Simprosys

1. Abrir app Simprosys Google Shopping Feed no Admin Shopify.
2. Localizar seção Google Customer Reviews / Store Ratings / GCR.
3. Confirmar conta Merchant Center vinculada à LK.
4. Configurar Merchant ID `5297679409`.
5. Definir país principal: Brasil / `BR`.
6. Definir prazo estimado de entrega. Sugestão inicial segura: data estimada de entrega = data do pedido + janela conservadora de entrega nacional usada pela LK. Se o app pede dias, usar valor conservador e depois calibrar.
7. Salvar.

### Fase 2 — QA por pedido-teste

1. Usar navegador sem VPN/proxy.
2. Usar e-mail de teste que não seja do domínio `lksneakers.com.br` e não seja e-mail do Merchant Center.
3. Usar endereço de entrega no Brasil.
4. Criar pedido-teste de baixo risco, usando método aprovado.
5. Na página de confirmação, validar:
   - popup de permissão do Google aparece;
   - nenhuma sobreposição bloqueia popup;
   - console sem erro crítico de `surveyoptin`;
   - pedido segue normal no Shopify;
   - nenhum pixel/app crítico quebra.

### Fase 3 — Readback e monitoramento

1. Confirmar no Simprosys/GMC se opt-in tracking/metric começa a registrar.
2. Aguardar janela do Google; a pesquisa em si não chega imediatamente, apenas depois da data estimada de entrega.
3. Revalidar no GMC se o alerta de “30 dias sem notificação” desaparece após processamento.

## 10. Rollback

Rollback primário:

- Desativar o módulo Google Customer Reviews no Simprosys ou remover Merchant ID/configuração GCR.

Rollback secundário:

- Se pedido-teste gerou pedido real indesejado, cancelar/estornar conforme procedimento LK — isso exige aprovação própria porque afeta pedido/pagamento.

Critério de rollback imediato:

- Erro visual ou funcional na página de confirmação.
- App interferindo em pagamento, confirmação, pixels críticos ou dados do pedido.
- Merchant ID errado ou popup renderizando incorretamente.

## 11. Critérios de aceite

- Pedido-teste elegível exibe o opt-in do Google na página de confirmação.
- Merchant ID usado é `5297679409`.
- País de entrega enviado como `BR` para pedidos Brasil.
- Data estimada enviada em `YYYY-MM-DD`.
- Checkout e confirmação seguem funcionando sem erro crítico.
- Configuração tem rollback documentado.
- Receipt final contém evidência visual/console/readback sem expor PII.

## 12. Bloqueios atuais

- Não executei write no Simprosys, Shopify Admin, GMC ou checkout porque a mudança é externa/checkout-adjacent e precisa de aprovação explícita escopada no turno.
- A confirmação técnica final depende de acesso ao app Simprosys e pedido-teste/thank-you page, que não é publicamente acessível.

## 13. Aprovação sugerida para execução

Texto de aprovação recomendado:

> Aprovado configurar Google Customer Reviews no Simprosys para a LK, Merchant ID 5297679409, com rollback por desativação do módulo, e fazer QA com um pedido-teste controlado. Não alterar preço, estoque, feed, tema production, campanhas ou outros apps.

