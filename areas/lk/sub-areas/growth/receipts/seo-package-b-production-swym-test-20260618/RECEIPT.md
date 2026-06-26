# Receipt — Pacote B: teste controlado SWYM em produção com rollback

Data: 2026-06-18

## Escopo aprovado

Lucas aprovou: “teste controlado SWYM em produção com rollback”.

## Status final

- Teste executado com snapshot antes da alteração.
- Produção foi restaurada ao estado anterior no final do teste.
- Nenhum token/secret foi impresso (`values_printed=false`).
- Não há recomendação de manter a alteração em produção ainda, porque a via de app embed via `disabled=true` não se comportou de forma plenamente estável/publicamente previsível no storefront.

## Snapshot / rollback

Snapshot principal criado antes do teste:

`/opt/data/profiles/lk-shopify/cron/output/seo_package_b_20260618/production_swym_test/rollback-before-swym-test-20260618T150119Z.json`

O snapshot contém o estado original de `config/settings_data.json` do tema production `155065417950`.

## Ação testada

Tema production:

- `155065417950` — `lk-new-theme/production`

Blocos SWYM/Wishlist Plus alvo:

- `5946647744298494267` — `wishlist-app-embed`
- `2734250573734242505` — `storefront-ui-elements`

Primeira tentativa controlada:

- alterar `disabled: false` para `disabled: true` nos dois blocos SWYM/Wishlist Plus.

Readback Admin posterior confirmou `disabled: true` nos blocos durante o teste.

## Evidência de teste

Baseline anterior produção mobile:

- Performance: 43
- LCP: 4.4s
- TBT: 12.950ms
- Third-party blocking: 4.800ms
- SWYM verdadeiro: 38 requests / ~304.6KB

Teste production com SWYM mexido:

- Em uma medição, SWYM verdadeiro caiu para 0 requests e TBT caiu para ~6.510ms; porém a URL de teste continha `swym` no query param e isso poluiu algumas heurísticas de busca textual.
- Em nova medição com query neutra, a produção ainda carregou SWYM verdadeiro: 38 requests / ~304.6KB, apesar dos blocos estarem `disabled: true` no Admin readback.
- TBT ainda melhorou parcialmente no run neutro: 12.950ms → 6.970ms; performance 43 → 48; LCP 4.4s → 3.8s. Porém, como SWYM continuou presente, essa melhoria não pode ser atribuída de forma limpa e suficiente à alteração.

## Segunda tentativa — remoção dos blocos

Foi tentada remoção temporária dos blocos SWYM do `config/settings_data.json`, com snapshot intermediário.

Resultado:

- PUT retornou OK, mas readback Admin manteve os blocos presentes.
- Interpretação: Shopify/app embed parece reconciliar ou proteger esses blocos de forma que a edição direta do asset não é uma forma confiável de desativação permanente/controlada.

## Rollback executado

Rollback aplicado restaurando o snapshot original.

Readback final Admin:

- `wishlist-app-embed`: `disabled: false`
- `storefront-ui-elements`: `disabled: false`

Readback público final via Chromium:

- SWYM voltou/presente no DOM público.
- `LK Wishlist — localStorage` presente.
- `.pc__wishlist` presente.
- Title da home válido.

## Interpretação

O preview dev mostrou benefício claro quando o SWYM não está presente, mas o teste em produção mostrou que mexer diretamente no `settings_data.json` do tema main não é o controle ideal/confiável para esse app embed. O caminho correto deve ser um dos seguintes:

1. Criar um novo tema dev duplicado da produção sem os blocos SWYM e usar esse tema como candidato de publicação futura após QA completo; ou
2. Usar configuração do próprio app/Shopify Theme Editor para desativar os app embeds, se Lucas quiser fazer essa etapa manualmente ou aprovar uma automação via endpoint compatível; ou
3. Implementar uma estratégia alternativa no tema que mantenha o app ativo mas bloqueie/lazy-load somente a camada pesada, se tecnicamente possível sem quebrar `_swat`.

## Risco

- A alteração direta por API em `config/settings_data.json` não é estável para governar SWYM em produção.
- Como rollback foi feito, o risco operacional atual foi removido.
- O gargalo de performance continua existindo em produção.

## Próxima recomendação

Não insistir em edição direta do app embed no tema main.

Próximo passo seguro recomendado:

- Preparar um tema candidato baseado em `lk-new-theme/dev`, validar visual + funcional completo, e se aprovado publicar em janela controlada; ou abrir no Shopify Theme Editor a configuração de App embeds e desligar Wishlist Plus manualmente para teste supervisionado.
