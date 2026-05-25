# Publicação Production — collection reveals

Destino: LK Sneakers / Shopify Production

Pedido limpo: Publicar no tema Production os blocos editoriais aprovados no dev para Onitsuka Tiger, New Balance 9060, New Balance 530, New Balance 204L e Nike x Jacquemus Moon Shoe SP.

Evidências:
- Tema Production: `155065417950` / `lk-new-theme/production` / `main`.
- Asset alterado: `sections/lk-collection.liquid`.
- Snapshot/rollback salvo em `sections__lk-collection.production.before.liquid`.
- Readback Shopify OK: todos os blocos copiados do dev existem no asset de produção.
- SHA antes: `6957409c344bd2a769aa5e245365139667fdd0ecb45d253df00fbbf849da5409`.
- SHA depois: `800241976d7d1107819178c0530c65aaf03c3d96bd8b14888ddb44397c5895bd`.
- Verificação pública por browser:
  - Onitsuka Tiger: bloco editorial aparece; descrição padrão escondida; título 58px.
  - New Balance 9060: bloco editorial aparece; descrição padrão escondida; título 58px.
  - New Balance 530: bloco editorial aparece; descrição padrão escondida; título 58px.
  - Nike x Jacquemus Moon Shoe SP: bloco editorial aparece; descrição padrão escondida; título 58px; kicker 4px.
  - New Balance 204L: bloco reveal aparece; descrição padrão escondida; porém o H1 público mediu 48px no desktop, porque o bloco 204L de origem dev ainda não contém a regra `coll-banner__title{font-size:58px}`.

Preview / URLs públicas:
- https://lksneakers.com.br/collections/onitsuka-tiger-todos-os-modelos
- https://lksneakers.com.br/collections/new-balance-9060
- https://lksneakers.com.br/collections/new-balance-530
- https://lksneakers.com.br/collections/new-balance-204l
- https://lksneakers.com.br/collections/nike-x-jacquemus-moon-shoe-sp

Risco:
- Baixo/médio: alteração concentrada em um único section asset, mas em tema main.
- Ponto aberto: ajuste visual fino da 204L para igualar o H1 desktop/mobile das demais.

Bloqueios:
- Nenhum para o que já foi publicado.
- Para corrigir o H1 da 204L em produção, precisa novo micro-write CSS no mesmo asset.

Rollback:
- Reenviar `sections__lk-collection.production.before.liquid` para o tema Production `155065417950`, asset `sections/lk-collection.liquid`.

Decisão recomendada:
- Aprovar micro-correção 204L: adicionar `body:has(.lk-204l-coll-preview) .coll-banner__title{font-size:58px!important}` e versão mobile `38px`, além de kicker 4px/3px, para fechar 100% de consistência.
