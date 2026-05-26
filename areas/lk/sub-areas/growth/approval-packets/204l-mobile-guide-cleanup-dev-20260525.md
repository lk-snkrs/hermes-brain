# Packet — ajustes mobile 204L guia editorial dev

Data: 2026-05-25
Área: LK / Growth / Shopify Theme
Coleção: New Balance 204L
Ambiente pretendido: Dev theme `155065450718` (`lk-new-theme/dev`)

## Pedido limpo

Lucas revisou o mobile da coleção 204L e pediu:

1. Micro-label `Curadoria LK` menor no mobile: `9px`.
2. Remover o bloco preto de `Guia editorial LK`, por duplicar o resumo do guia editorial logo abaixo.
3. Remover CTA `Ver produtos da coleção` dentro do guia da própria coleção; manter apenas CTA para o guia completo.

## Evidências do print

- O bloco preto aparece imediatamente acima do painel bege do guia, com o mesmo contexto editorial e CTA `Ler guia editorial`.
- O painel bege já contém o resumo/guia editorial completo, portanto o bloco preto é redundante.
- O CTA para produtos é redundante dentro da própria collection page.

## Patch local preparado

Arquivo ajustado localmente:

- `scripts/lk_collection_guide_standard_lote1_dev_20260525.py`

Mudanças preparadas:

- CSS mobile:
  - `.lk-guide-standard-panel__eyebrow { font-size: 9px !important; }`
- Bloco preto:
  - escondido para `collection.handle == 'new-balance-204l'`
  - mantido temporariamente para `adidas-samba-jane` até revisão específica.
- CTA 204L:
  - removido `/collections/new-balance-204l` / `Ver produtos da coleção`
  - mantido apenas `/pages/new-balance-204l-original-brasil-guia-lk` / `Abrir guia completo`

## Bloqueio

A escrita no dev theme via Admin API não foi executada neste turno porque o roteamento de segurança bloqueou chamadas de terminal/API como ação externa/escrita.

## Risco

Baixo, se aplicado apenas no tema dev. Validar depois:

- ausência do bloco preto na 204L;
- mobile eyebrow em 9px;
- CTA único para guia completo;
- produção intacta;
- scan de termos proibidos.

## Rollback

Restaurar o asset `sections/lk-collection.liquid` do backup pré-write do dev theme ou reverter este patch local.

## Próximo passo

Quando a escrita dev estiver liberada neste fluxo, aplicar o patch no tema dev e reenviar o link de preview da 204L para Lucas; se permitido, enviar também ao Renan Fortini.
