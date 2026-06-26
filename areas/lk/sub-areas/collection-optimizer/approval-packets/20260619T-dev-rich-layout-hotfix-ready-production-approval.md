# Approval packet — Hotfix visual rich content coleções C1+C2

- Data UTC: 2026-06-19T14:59:04.081589+00:00
- Status: DEV validado / Production bloqueada aguardando aprovação explícita Lucas
- Tema DEV: `155065450718` / `lk-new-theme/dev` / role `unpublished`
- Tema Production: `155065417950` / `lk-new-theme/production` / role `main`

## Problema
As coleções da onda C1+C2 foram publicadas com copy/SEO/AI Visibility correto, mas parte do `descriptionHtml` renderiza no bloco padrão `coll-rich-content`, com aparência de texto corrido/sem layout premium.

## Escopo do hotfix proposto
Aplicar somente CSS de contenção visual para `coll-rich-content`/`coll-rich-content__inner`, deixando o conteúdo com:
- largura controlada;
- grid editorial desktop;
- espaçamento premium;
- bullets limpos;
- blockquote destacado;
- FAQ com separadores;
- fallback mobile legível.

## O que NÃO muda
- Preço: não
- Estoque: não
- Produtos: não
- Campanhas: não
- Feed/GMC: não
- SEO text/copy: não
- Template estrutural: não

## Evidência DEV
Preview precisa ser aberto com cookie de tema DEV. Acesso recomendado:
1. Abrir primeiro: `https://lk-sneakerss.myshopify.com/?preview_theme_id=155065450718`
2. Depois abrir as coleções no mesmo navegador:
   - `https://lk-sneakerss.myshopify.com/collections/adidas-handball-spezial?lkqa=devcookie`
   - `https://lk-sneakerss.myshopify.com/collections/new-balance-1906l?lkqa=devcookie`
   - `https://lk-sneakerss.myshopify.com/collections/alo-yoga-1?lkqa=devcookie`
   - `https://lk-sneakerss.myshopify.com/collections/air-jordan-1-low?lkqa=devcookie`
   - `https://lk-sneakerss.myshopify.com/collections/new-balance-204l?lkqa=devcookie`
   - `https://lk-sneakerss.myshopify.com/collections/onitsuka-tiger-mexico-66?lkqa=devcookie`

Readback técnico DEV com cookie: as 6 URLs carregaram asset DEV `t/92/assets/lk-collection-v2.css`.

## Risco
Baixo/médio. CSS é global para `coll-rich-content` em páginas de collection. Pode melhorar páginas similares, mas pode afetar visual de qualquer collection que use o mesmo bloco. Por isso exige aprovação antes de production.

## Rollback
Restaurar backup do asset CSS production anterior ou remover o bloco do hotfix.

## Aprovação necessária
Para executar em production, Lucas precisa aprovar explicitamente no turno atual. Frase sugerida:

**Aprovo aplicar o hotfix visual em production nas coleções C1+C2.**
