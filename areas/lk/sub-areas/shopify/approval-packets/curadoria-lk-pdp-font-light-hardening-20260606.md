# Approval Packet — Curadoria LK PDP font light hardening — 2026-06-06

## Pedido
Lucas reportou que a fonte do título/nomes dos produtos em “Outras variações” está parecendo negrito e deve ser light.

## Evidência read-only
- CSS público atual `assets/lk-variante.css` contém override final:
  - `.lk-variante__title { font-weight:300; }`
  - `.lk-variante__label, .lk-variante__item.is-current .lk-variante__label { font-weight:300!important; }`
- QA visual/CDP em Production:
  - `new-balance-530-white-natural-indigo-1`: título `300`; labels `300,300,300,300,300`
  - `tenis-adidas-superstar-x-clot-chinese-new-year-preto`: título `300`; labels `300,300`
- Ponto encontrado: em fontes locais/readbacks antigos, a regra base ainda aparece como:
  - `.lk-variante__title { font-weight:500; }`
  - `.lk-variante__item.is-current .lk-variante__label { font-weight:500; }`
  O CSS live corrige isso por override no final, mas a regra base divergente pode gerar confusão, cache antigo, ou regressão em próximas compilações.

## Correção proposta
Hardening no asset `assets/lk-variante.css`:
1. Trocar a regra base de `.lk-variante__title` para `font-weight:300`.
2. Trocar/remover a regra base de `.lk-variante__item.is-current .lk-variante__label{...font-weight:500}` para não voltar a bold.
3. Manter override final com `font-weight:300!important` para título, labels e pseudo-elementos.

## Escopo
- Apenas CSS de curadoria PDP (`lk-variante.css`).
- Sem alterar produtos, estoque, preços, coleções ou snippet de grupos.

## Risco
- Baixo. Alteração visual localizada no bloco “Outras variações”.
- Possível impacto: labels do item atual deixam de destacar por peso; destaque continua via cor/borda.

## Rollback
- Reverter PR GitHub/asset CSS para versão anterior.

## Decisão necessária
Aprovar write em DEV para hardening da tipografia light e QA visual antes de merge para Production.
