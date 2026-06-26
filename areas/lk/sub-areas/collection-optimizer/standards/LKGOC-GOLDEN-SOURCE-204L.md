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


## Regra operacional adicionada — 20260608T174338Z
Lucas confirmou que este modelo é o **LAYOUT/TEMPLATE BASE** das próximas coleções LKGOC.

Regra:
- copiar este layout/template da 204L Golden;
- trocar apenas texto, fotos, links, produtos/FAQ e nuances comerciais;
- não criar novo layout, nova hierarquia ou novo comportamento sem aprovação explícita;
- classe legacy `lk-204l-kicker` foi removida e não deve voltar;
- kicker padrão: `lk-goc-kicker`.


## Correção GOLDEN — mobile image teaser — 20260608T175005Z
Lucas corrigiu o comportamento mobile: no estado collapsed, a imagem editorial **não deve aparecer íntegra**.

Regra GOLDEN atualizada:
- mobile collapsed deve mostrar apenas uma prévia/corte com sombra/gradiente;
- objetivo: usuário percebe que existe imagem/editorial, mas precisa clicar em `Ler mais` para ver completo;
- manter lógica product-first;
- após `Ler mais`, collage pode abrir completa;
- não usar imagem principal 16:9 inteira no collapsed.

Implementação DEV aprovada para revisão:
- collapsed collage: `max-height:96px`, `overflow:hidden`;
- sombra: gradient bottom overlay;
- expanded `.is-open`: remove corte, remove sombra e mostra collage completa.
- Commit dev: `1c00853`.


## Ajuste GOLDEN — mobile teaser height 50px — 20260608T175630Z
Lucas pediu reduzir ainda mais a prévia da imagem no collapsed mobile.

Regra atual:
- `max-height:50px` no teaser collapsed;
- imagem deve aparecer só como sombra/faixa de prévia;
- clique em `Ler mais` continua necessário para ver a collage completa;
- `.is-open` continua com `max-height:none`.

Commit dev: `8afd6b5`.


## Ajuste GOLDEN — mobile teaser mais curto 28px — 20260608T180351Z
Lucas pediu mostrar ainda menos imagem no mobile collapsed.

Regra atual:
- teaser collapsed da 204L: `max-height:28px`;
- card principal collapsed travado em altura curta e deslocado para cima (`translateY(-28px)`);
- objetivo: mostrar apenas uma sombra/faixa da imagem, não imagem completa;
- `Ler mais` continua obrigatório para abrir a collage completa.

Commits dev:
- `f11bc4f` — reduz teaser strip no override mobile;
- `c47d158` — alinha regra-base da seção.


## Ajuste GOLDEN — mobile teaser 48px — 20260608T191317Z
Lucas pediu mostrar aproximadamente 20px a mais que o ajuste anterior, pois 28px estava mostrando quase nada.

Regra atual aprovada para revisão:
- teaser collapsed: `height/max-height:48px`;
- card interno: `height/max-height:104px`;
- deslocamento: `translateY(-36px)`;
- mantém sombra/corte e botão `Ler mais`;
- `.is-open` continua abrindo a collage completa.

Commit dev: `f634dff`.
