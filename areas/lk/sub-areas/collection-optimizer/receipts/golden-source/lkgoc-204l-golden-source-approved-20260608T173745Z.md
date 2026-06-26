# LKGOC Golden Source — New Balance 204L

Status: APROVADO POR LUCAS como GOLDEN / Gold Source LKGOC
Data UTC: 20260608T173745Z
Tema DEV validado: `lk-new-theme/dev` — Shopify theme ID `155065450718` — role `unpublished`
Preview validado: https://lk-sneakerss.myshopify.com/collections/new-balance-204l?preview_theme_id=155065450718

## Decisão Lucas
A coleção **New Balance 204L** corrigida no DEV/unpublished passa a ser o **padrão GOLDEN** para LKGOC.

## O que deve ser copiado nos próximos modelos

### Hero desktop
- Desktop da 204L está aprovado como referência visual.
- Não redesenhar.
- Copiar estrutura, proporção, hierarquia, densidade editorial e comportamento.
- Adaptar apenas textos, links, imagens e nuances comerciais da coleção alvo.

### Hero mobile
- Product-first obrigatório.
- Espaçamento superior do título mobile aprovado após correção: `padding-top:18px` no escopo da 204L.
- Botão `Ler mais` deve aparecer no mobile.
- Estado collapsed:
  - produto/grid continua prioridade;
  - imagem principal visível em card 16:9;
  - imagens secundárias escondidas;
  - botão `Ler mais` visível.
- Estado expanded após clique:
  - botão some;
  - imagens secundárias aparecem;
  - collage expande.

### Namespace/classes
- Preferir namespace limpo `lk-goc-*`.
- Kicker aprovado deve ser limpo:
  - correto: `lk-goc-kicker`
  - Aliases antigos só quando tecnicamente necessários para compatibilidade, não como padrão novo.

### Guide panel
- `lk-goc-guide-panel` está aprovado por Lucas como perfeito em mobile e desktop.
- Deve ser copiado exatamente nos outros modelos, mudando apenas o texto/conteúdo.
- Não criar novo layout de guide sem aprovação explícita.

## Commits/PR base
- PR GitHub: https://github.com/lk-snkrs/lk-new-theme/pull/39
- Merge dev: `c117b8d`
- Ajuste final de espaçamento dev: `6b1b030`

## Guardrail
Este padrão é DEV/unpublished aprovado visualmente por Lucas como Golden Source. Production continua exigindo aprovação explícita antes de qualquer promoção/deploy live.
