# LK tarefa 1 follow-up — OG público, HTML global e alt da home

Data: 2026-05-31
Escopo: continuação read-only da tarefa 1 após aprovação/aplicação do OG da home.

## Fontes consultadas

- Storefront público: `https://lksneakers.com.br/` com cachebuster e UA mobile.
- DataForSEO OnPage Instant Pages: home, `/cart`, `/collections/samba`.
- Shopify Admin Asset API somente GET/read-only para tema produção `lk-new-theme/production` (ID `155065417950`, role `main`).
- Arquivos locais do tema em `/opt/data/hermes_bruno_ingest/lk-new-theme/`.
- W3C Nu Validator com HTML público salvo em `/tmp/lk_home.html`.

## 1. OG público da home

Status: corrigido e propagado.

Evidência pública:

- `og:title`: `LK Sneakers | Jardins SP, Originalidade Garantida, Curadoria Premium`
- `og:description`: `Sneaker boutique premium no Jardins, São Paulo. Nike, Adidas Samba, New Balance e Onitsuka Tiger originais. Até 10x sem juros, frete grátis acima de R$499 e loja física na Rua Melo Alves.`
- DataForSEO também leu os novos valores em `social_media_tags`.

Atenção residual:

- `twitter:title` e `twitter:description` ainda usam os textos antigos/genéricos:
  - `twitter:title`: `LK Sneakers | Tênis Nike Dunk, adidas Samba, New Balance 530 Originais`
  - `twitter:description`: `Na LK Sneakers & Apparels você encontra produtos originais...`

Interpretação:

- A correção de OG foi bem-sucedida.
- Próxima melhoria opcional: alinhar Twitter Card à mesma narrativa premium/local da OG description.

## 2. Imagem sem alt na home

Status: localizada.

Evidência pública:

- Total de imagens na home: 31.
- Imagens sem alt: 1.
- Imagem: `Shopify_Banner_Desktop_6c27171d-a754-4917-8d36-264834544f28.png`
- Classe: `lk-hero__bg-img`.

Evidência do tema produção via GET:

- Asset `templates/index.json`, seção `hero`, primeiro bloco `slide_x7TMBt`:
  - `kicker`: `Onitsuka Tiger x Versace`
  - `title`: vazio
  - `image_alt`: vazio
  - `image`: `shopify://shop_images/Shopify_Banner_Desktop_6c27171d-a754-4917-8d36-264834544f28.png`

Causa provável:

- `sections/lk-hero.liquid` define `hero_alt = block.settings.image_alt | default: block.settings.title | escape`.
- Como o primeiro slide tem `image_alt` vazio e `title` vazio, o fallback também fica vazio.

Correção proposta para aprovação futura:

- Opção A — conteúdo/settings: preencher `image_alt` do primeiro slide com:
  - `Onitsuka Tiger x Versace na LK Sneakers`
- Opção B — tema/Liquid: mudar fallback para `image_alt > title > kicker > shop.name`.

Recomendação:

- Para menor risco visual e semântica melhor: Opção B em dev primeiro, pois evita recorrência quando um slide tiver title vazio.

## 3. Erro HTML global de fechamento de tag

Status: ainda não fechado; origem provável reduzida, mas não confirmada.

Evidência DataForSEO:

- Home: 2 erros `The closing tag and the currently open tag do not match.`
- Cart: 2 erros iguais.
- Coleção Samba: 2 erros iguais.
- As colunas são recorrentes (`2673` e `2984`), o que sugere bloco global/renderizado comum.

Validação cruzada:

- Parser simples de pilha no HTML público não reproduziu mismatch em home/coleção/PDP/busca/cart.
- W3C Nu Validator também não apontou erro explícito de tag de fechamento, mas encontrou muitos erros de `style` em locais inválidos e warnings/erros de HTML gerados por apps/seções.

Pistas relevantes:

- O erro é global e aparece inclusive no carrinho, então é mais provável estar em `layout/theme.liquid`, header/footer/popups/scripts globais ou algum app injectado, não em uma coleção/PDP específica.
- DataForSEO reporta a linha/coluna em HTML renderizado com JS, enquanto o HTML capturado diretamente tem numeração diferente; por isso o mapeamento exato para arquivo ainda precisa de uma etapa de render/headless ou captura do DOM pós-JS.

Próxima etapa recomendada:

- Rodar diagnóstico headless com DOM pós-JS, salvando `document.documentElement.outerHTML`, e cruzar o trecho das colunas DataForSEO contra snippets globais.
- Sem write.

## 4. Carrinho vazio sem H1

Status: origem localizada.

Evidência pública/DataForSEO:

- `/cart` não tem H1.
- H2 atual: `Seu carrinho está vazio`.

Origem no tema:

- `sections/lk-cart.liquid`, linha 334:
  - `<h2 class="cart-empty__title">{{ section.settings.empty_title }}</h2>`

Correção proposta para aprovação futura:

- Trocar para:
  - `<h1 class="cart-empty__title">{{ section.settings.empty_title }}</h1>`

Risco:

- Baixo visualmente se CSS é por classe `.cart-empty__title`, não por tag.
- Baixo SEO, pois `/cart` é bloqueado/noindex; benefício maior é acessibilidade/semântica.

## 5. Outros achados técnicos

W3C Nu Validator encontrou problemas não necessariamente críticos:

- `script type=module` com `defer` vindo de Shopify/app.
- atributos não padrão em scripts/styles de app.
- muitos `<style>` inline dentro de `section`, `div`, `main` ou `body`.
- `link rel="preload"` com atributos `srcset`/`sizes` inválidos para `<link>`.

Interpretação:

- Parte é ruído comum de Shopify/apps.
- Parte pode ser limpa gradualmente em tema próprio, mas não parece ser gargalo comercial imediato.

## Próximo approval packet sugerido

Pacote pequeno, se Lucas aprovar depois:

1. Alinhar Twitter Card da home com o novo OG.
2. Corrigir alt do hero com fallback robusto (`image_alt > title > kicker > shop.name`) ou preencher alt do primeiro slide.
3. Trocar H2 do carrinho vazio para H1.
4. Rodar diagnóstico headless para fechar origem do erro DataForSEO antes de qualquer correção de HTML global.

## Guardrail

Nenhum write em Shopify foi feito nesta etapa. Foram feitos apenas:

- GET/read-only em Shopify Asset API.
- consultas públicas/DataForSEO.
- escrita de relatório local no Brain.
