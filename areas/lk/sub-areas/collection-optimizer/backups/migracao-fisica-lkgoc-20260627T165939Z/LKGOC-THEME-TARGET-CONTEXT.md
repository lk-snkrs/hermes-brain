# LKGOC — contexto de tema alvo

Atualizado em UTC: 20260603T164243Z

## Decisão Lucas
O tema correto/alvo para o LKGOC é:

- Theme ID: `155065450718`
- Nome: `lk-new-theme/dev`
- Role verificado anteriormente via Shopify API: `main`

Instrução de Lucas: **"O correto é esse 0718… esquecer todos os outros"**.

## Implicação operacional
- Todos os outros temas usados em testes anteriores devem ser considerados fora de escopo para a execução oficial LKGOC, salvo nova instrução explícita.
- Como `155065450718` está com role `main`, ele deve ser tratado como Production/live para fins de segurança.
- Não executar write direto nesse tema sem aprovação explícita atual e escopo de produção.
- Fluxo recomendado: criar/usar uma cópia `unpublished` a partir do `155065450718`, aplicar LK-GOC Standard v1 nela, QA, approval Lucas, depois merge/promoção.

## Observação
As alterações anteriores feitas no tema `156623372510` não devem ser consideradas base oficial do LKGOC. Elas servem apenas como sandbox/receipts técnicos, não como branch correta.

## Regra operacional — sempre alterar o tema DEV

Registrado em UTC: 20260603T170929Z

Instrução Lucas: **"você deve sempre alterar o tema dev"**.

Implicações:
- O destino oficial de execução LKGOC é sempre o tema DEV indicado por Lucas.
- Não usar sandboxes/temas alternativos como destino oficial sem instrução explícita.
- Não aplicar LKGOC em tema aleatório só porque é `unpublished`.
- Se houver conflito entre nome do tema e `role` da Shopify API, parar e confirmar o destino antes de write.
- Para segurança, qualquer tema com `role: main` continua exigindo confirmação explícita de escopo antes de write, porque tecnicamente é o tema publicado pela Shopify.

