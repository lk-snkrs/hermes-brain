# Receipt — GitHub reconciliation check no-op — AJ4 unavailable cleanup

Data UTC: 2026-06-07T21:16Z

## Escopo

Verificar se o hotfix AJ4 anterior no Shopify Production precisava ser reconciliado no GitHub `lk-snkrs/lk-new-theme`, branch `production`.

## Evidência

- Repo: `lk-snkrs/lk-new-theme`
- Base verificada: `origin/production`
- Fetch executado com token GitHub via Doppler/askpass temporário; `values_printed=false`
- Shopify readback: theme Production `155065417950`
- Asset: `snippets/lk-variante-top30-visited-v2.liquid`
- SHA12 GitHub `origin/production`: `811dbe5bdec7`
- SHA12 Shopify live readback: `811dbe5bdec7`
- Full diff GitHub x Shopify live: `0 bytes`
- Handle exato removido: `tenis-air-jordan-4-retro-military-blue-branco`
- Handle exato em GitHub: `false`
- Handle exato em Shopify live: `false`
- Grupo `top30-air-jordan-4-regular`: handles/labels/images = `15/15/15` em GitHub e Shopify live
- Substring parecida ainda existe apenas como produto distinto: `tenis-air-jordan-4-retro-military-blue-branco-copia`
- Commits recentes no asset em `origin/production` indicam sync automático do Shopify: `344f2e6 Update from Shopify for theme lk-new-theme/production` entre os últimos commits.

## Interpretação

Não há divergência atual entre GitHub `production` e Shopify live para esse asset. O GitHub já está reconciliado com o estado live do Shopify, provavelmente por sync automático posterior do tema.

## Decisão operacional

- Nenhum PR de reconciliação AJ4 é necessário agora.
- Nenhum write externo foi executado nesta etapa.
- Não houve merge/deploy/publish.

## Caveat

A busca simples por substring do handle pode dar falso positivo porque existe o handle distinto com sufixo `-copia`. A validação correta é por token exato dentro das arrays Liquid e por contagem do grupo.

## Próximo passo seguro

Manter a regra nova: próximas mudanças em Production theme devem nascer no GitHub/PR antes do Shopify readback. Se uma mudança direta antiga aparecer divergente no futuro, abrir PR de reconciliação antes de qualquer novo write.
