# Approval packet — Winter by LK

Data: 2026-06-22
Solicitação: criar coleção Shopify de inverno somente vestuário.
Nome: Winter by LK

## Escopo solicitado
- Somente vestuário.
- Incluir apenas: camisetas manga longa, moletons, calças e jaquetas.
- Produtos esgotados sempre por último.

## Read-only verificado
- Shopify LK smoke read-only: OK, HTTP 200, values_printed=false.
- Coleção existente `Winter by LK`: não encontrada.
- Product types relevantes encontrados: `Calça`, `Camisa`, `Camiseta`, `Jaqueta`, `Moletom`, `Vestido`.
- Tags/estrutura para manga longa encontradas em amostra: `Camiseta Manga Longa` e `Camiseta manga longa`.

## Implementação recomendada
Criar uma smart collection/automated collection com regras OR:
- product_type = `Calça`
- product_type = `Moletom`
- product_type = `Jaqueta`
- tag = `Camiseta Manga Longa`
- tag = `Camiseta manga longa`

Não incluir `Camisa Manga Longa`, pois o pedido foi camisetas manga longa.
Não incluir `Vestido`, `Camisa` genérica ou `Camiseta` genérica.

## Ordenação esgotados por último
Opção segura recomendada:
1. Criar coleção dinâmica com os critérios acima.
2. Confirmar se o tema/collection template da LK já aplica `available products first` nas páginas de coleção.
3. Se não aplicar, preparar ajuste em dev theme/preview para ordenar disponíveis antes de esgotados, sem consultar estoque diretamente fora do dono `lk-stock`.

## Aprovação necessária
Write em Shopify production: exige aprovação explícita atual de Lucas.

## Rollback
- Excluir/despublicar a coleção `Winter by LK`.
- Remover link de navegação se houver publicação em menu.
- Se houver ajuste de tema, reverter pelo dev theme/backup antes de produção.

## Evidência
- Integração Shopify LK read-only OK.
- Nenhuma coleção existente com o nome/handle foi encontrada.
