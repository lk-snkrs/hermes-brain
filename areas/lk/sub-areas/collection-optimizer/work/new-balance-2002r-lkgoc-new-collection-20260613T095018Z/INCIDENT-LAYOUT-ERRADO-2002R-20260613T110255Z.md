# Incident — Layout errado New Balance 2002R

Data UTC: 20260613T110255Z
Status: INCIDENTE ABERTO / SEM NOVO WRITE

## Report Lucas
"Está tudo errado o layout"

## Verificação read-only pública
URL: https://lksneakers.com.br/collections/new-balance-2002r
Theme público: `lk-new-theme/production`, role `main`, ID `155065417950`.

Read-only HTML check:
- hero 2002R (`lk-goc-coll-preview--2002r`): ausente
- headline 2002R (`Retrô running, presença urbana.`): ausente
- guide 2002R (`lk-guia-new-balance-2002r`): ausente
- sinais 204L/global aparecem no HTML
- toolbar/grid e contador de produtos aparecem

## Diagnóstico
A página pública não está renderizando a experiência 2002R correta. O layout não pode ser considerado aprovado nem estabilizado.

## Guardrail vigente
Não fazer novo write direto via Shopify Admin API.
Qualquer correção/rollback deve seguir GitHub-first: branch → commit → PR/pacote → aprovação → deploy/merge versionado.

## Caminhos seguros
1. Rollback/hide via fluxo GitHub/deploy owner para retirar a experiência errada do ar.
2. Rebuild correto em branch GitHub a partir da 204L golden, com QA antes de qualquer nova promoção.
3. Reconciliation do estado atual para registrar e desfazer os writes feitos fora do fluxo.
