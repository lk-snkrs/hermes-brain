# LK Shopify — Approval packet: correção da sugestão de coleção para Nike Mind na busca

Data: 2026-06-16
Perfil: lk-shopify
Escopo: tema Shopify `sections/lk-search.liquid`
Tipo: DEV theme write somente após aprovação explícita

## Evidência read-only

Rodada pública realizada em `https://lksneakers.com.br/search` com `type=product`:

- `vomero` → renderiza sugestão correta: `/collections/nike-vomero-premium` / `Nike Vomero Premium`
- `vômero` → renderiza sugestão correta: `/collections/nike-vomero-premium` / `Nike Vomero Premium`
- `vomero 5` → renderiza `Nike Vomero 5` e também `Nike Vomero Premium`
- `204l` → renderiza `/collections/new-balance-204l`
- `9060` → renderiza `/collections/new-balance-9060`
- `530` → renderiza `/collections/new-balance-530`
- `yeezy` → renderiza `/collections/yeezy`
- `samba` → renderiza `/collections/samba`
- `mind` → não renderiza bloco de coleção sugerida
- `nike mind` → renderiza a coleção ampla `/collections/nike-todos-os-modelos`, não a família Mind

Arquivos de evidência:

- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/daily-continuation-20260616/search-suggestion-visible-blocks.json`
- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/daily-continuation-20260616/public-seo-cache-and-search-qa-v2.json`

## Interpretação

A busca está saudável para as famílias recém-trabalhadas de Vomero, 204L, 9060, 530, Yeezy e Samba.

O gap objetivo está em Nike Mind:

1. A query `mind` não bate em nenhuma coleção porque o mapa atual não tem alias simples `mind`.
2. A query `nike mind` bate antes na coleção ampla `Nike`, porque o alias `nike` aparece antes da linha específica `Nike Mind 001 e 002`.

Isso é uma correção de roteamento/UX da busca, não um problema de produto, estoque ou coleção.

## Preview do ajuste proposto

Alterar somente a ordem/aliases no mapa local de `sections/lk-search.liquid`:

- Mover a linha da coleção Mind para antes da linha ampla `nike,nike todos os modelos`.
- Expandir aliases da linha Mind para incluir:
  - `mind`
  - `nike mind`
  - `nike mind 001 e 002`
  - `nike mind 001`
  - `nike mind 002`
  - `mind 001`
  - `mind 002`
  - `001`
  - `002`

Resultado esperado:

- `mind` → `/collections/nike-mind-001` / `Nike Mind 001 e 002`
- `nike mind` → `/collections/nike-mind-001` / `Nike Mind 001 e 002`
- `nike` → continua `/collections/nike-todos-os-modelos` / `Nike`
- controles `vomero`, `vomero 5`, `204l`, `9060`, `530` permanecem iguais

## Risco

Baixo, desde que aplicado primeiro em DEV:

- Afeta apenas sugestão interna da página de busca.
- Não altera resultado orgânico da busca nem cards de produto.
- Não altera produto, preço, estoque, coleção, tag, metafield ou checkout.

Risco principal: colisão de alias com queries genéricas `001`/`002`. Se Lucas preferir mais conservador, remover `001` e `002` soltos e manter apenas aliases com `mind`.

## Rollback

- Reverter a linha do mapa para a versão atual de `sections/lk-search.liquid`.
- Readback de hash do asset DEV/Production.
- QA público/preview nas queries de controle.

## Próxima decisão

Opção recomendada: aprovar DEV com alias conservador:

- incluir `mind`, `nike mind`, `nike mind 001`, `nike mind 002`, `mind 001`, `mind 002`
- não incluir `001`/`002` soltos para evitar colisão genérica

Aprovação necessária para qualquer upload de tema, mesmo DEV.
