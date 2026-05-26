# Packet — correção micro-label 204L dev + envio de previews ao Renan

Data: 2026-05-25
Área: LK / Growth / Shopify Theme

## Pedido limpo

Lucas apontou que o micro-label aparece como `CURADORIA LK · NEW BALANCE 204L`, com fonte/volume visual grande demais, e lembrou que o padrão já corrigido era remover `New Balance 204L` do label.

Também pediu que, toda vez que um link de dev/preview for gerado para algo feito pela Hermes, o link seja enviado ao Renan Fortini no Telegram para acompanhamento.

## Padrão correto

- Micro-label/eyebrow: `Curadoria LK`
- Não usar: `Curadoria LK · New Balance 204L`
- Manter label discreto, sem competir com H1/título da coleção.
- Produção só após aprovação visual.

## Evidência local aplicada

Arquivo local ajustado:

- `scripts/lk_204l_mobile_reveal_dev_20260524.py`

Alteração:

```diff
- <p class="lk-204l-kicker">Curadoria LK · New Balance 204L</p>
+ <p class="lk-204l-kicker">Curadoria LK</p>
```

## Bloqueio operacional neste turno

O envio externo ao Renan e a escrita/validação no tema dev não foram executados neste turno porque o roteamento de segurança bloqueou ações externas/escritas. Nenhuma alteração em production foi feita.

## Risco

Baixo se aplicado apenas no dev theme. O risco é visual: label ainda pode parecer grande caso exista CSS público/cache antigo vencendo; deve ser verificado por DOM/computed style após aplicar no dev.

## Rollback

Reverter o micro-label para o texto anterior no asset/script ou restaurar backup do asset do dev theme.

## Próximo passo

Aplicar a correção no dev theme LK, verificar que o micro-label renderiza apenas `Curadoria LK`, reenviar link de preview ao Lucas e, quando o destino Telegram do Renan estiver disponível e o envio externo estiver permitido, enviar o mesmo link ao Renan.
