# Approval packet — Busca LK: corrigir sugestão de coleção para 204L e demais coleções

Gerado: 2026-06-08 12:20 BRT

## Pedido limpo

Corrigir o módulo compacto de **Coleção sugerida** na página de busca para que pesquisas como `204L` mostrem a coleção correta `New Balance 204L` (`/collections/new-balance-204l`).

Este packet **não executa upload**, **não altera Production**, **não altera produtos/coleções/preços/estoque/apps/Search & Discovery**.

## Evidência do bug

- Screenshot do Lucas: busca `204L` mostra apenas resultados e filtros; não mostra `Coleção sugerida`.
- QA público read-only `/search?q=204L&type=product`:
  - HTTP 200.
  - `Coleção sugerida`: `false`.
- Coleção alvo existe/publica:
  - `/collections/new-balance-204l`: HTTP 200.
- Readback Admin `sections/lk-search.liquid`:
  - Production/main `lk-new-theme/production`: SHA12 `261b18011b56`.
  - DEV/unpublished `lk-new-theme/dev`: SHA12 `261b18011b56`.
  - Ambos estão iguais e só têm regra hardcoded de `9060`.
  - `prod_has_204l_alias=false`; `dev_has_204l_alias=false`.

## Interpretação

Sim: **deveria aparecer**. O projeto amplo de sugestões por coleção tinha mapeamento para `204L`, mas o ativo atual de DEV e Production está no estado antigo, com regra compacta apenas para `9060`.

Evidência local reaproveitável já validada anteriormente:

- Workspace antigo DEV readback válido:
  - `/opt/data/profiles/lk-shopify/workspace/search-collection-suggestions-20260605-153046-v2/dev-apply-20260605-154316/dev_readback_sections__lk-search.liquid`
- Linha do mapa antigo:
  - `new balance 204l,204l,nb 204l::new-balance-204l::New Balance 204L`

## Preview local preparado

Arquivos locais:

- Source atual:
  - `/opt/data/profiles/lk-shopify/workspace/search-204l-collection-suggestion-fix-20260608/production_source_sections__lk-search.liquid`
- Target proposto:
  - `/opt/data/profiles/lk-shopify/workspace/search-204l-collection-suggestion-fix-20260608/target_sections__lk-search.liquid`
- Verificação:
  - `/opt/data/profiles/lk-shopify/workspace/search-204l-collection-suggestion-fix-20260608/verification.json`

## Verificação estática do target

- Source SHA12: `261b18011b56`.
- Target SHA12: `70cb4f3df56b`.
- Tamanho: `37443` bytes.
- Abaixo de 256 KB Shopify: `True`.
- Alias `204L`: `True`.
- Alias `9060`: `True`.
- Alias `530`: `True`.
- Copy compacta preservada: `True`.
- Card antigo grande ausente: `True`.
- Busca segue product-only e grid preservado: `True`.
- Sem sintaxe Liquid inválida `{{%- assign/capture/if`: `True`.
- Delimitador seguro `|#|`: `True`.

## Escopo exato se aprovado DEV

- Shopify DEV/unpublished apenas:
  - theme `155065450718` / `lk-new-theme/dev` / `unpublished`.
- Asset:
  - `sections/lk-search.liquid`.
- Mudança:
  - substituir o bloco hardcoded só de `9060` pelo mapa compacto de coleções já validado, incluindo `204L`.

## QA pós-DEV

1. Asset API readback DEV e SHA target/readback.
2. Confirmar Production SHA inalterado.
3. QA público/preview, sabendo que `preview_theme_id` pode ser removido em headless; usar readback como evidência primária de DEV.
4. Validar pelo menos:
   - `204L` → `New Balance 204L` / `/collections/new-balance-204l`.
   - `9060` → `New Balance 9060` / `/collections/new-balance-9060`.
   - `530` → `New Balance 530` / `/collections/new-balance-530`.
   - busca de produto comum continua mostrando grid.

## Risco

- Baixo/médio: altera apenas a sugestão compacta dentro do banner de busca.
- Risco principal: mapa amplo desatualizado se alguma coleção mudou desde 2026-06-05; mitigação por QA dos aliases principais e readback.

## Rollback

- Reupload do source atual salvo em:
  - `/opt/data/profiles/lk-shopify/workspace/search-204l-collection-suggestion-fix-20260608/production_source_sections__lk-search.liquid`
- Readback DEV e confirmação de SHA anterior.

## Próxima decisão

Para aplicar no DEV/unpublished:

**Aprovo DEV busca coleções 204L**
