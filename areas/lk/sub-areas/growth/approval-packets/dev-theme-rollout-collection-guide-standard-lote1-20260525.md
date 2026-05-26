# Packet — Dev theme rollout do padrão Moon Shoe nas próximas coleções

Data: 2026-05-25
Destino: LK Growth / Shopify dev theme
Status: aguardando aprovação operacional para escrita em dev theme

## Pedido limpo

Aplicar em ordem o padrão aprovado no Nike x Jacquemus Moon Shoe às outras coleções já melhoradas, começando por um preview em tema dev. Depois da aprovação visual do Lucas, publicar em produção com rollback.

## Ordem recomendada

### Lote 1 — primeiro preview

1. New Balance 204L
2. Adidas Samba Jane

### Lote 2 — após aprovação/QA do lote 1

3. Onitsuka Tiger Mexico 66
4. Onitsuka Tiger geral / Todos os modelos
5. New Balance 9060
6. New Balance 530

## Evidências já verificadas read-only

Tema produção verificado: `lk-new-theme/production`.

Estado atual detectado:

- `nike-x-jacquemus-moon-shoe-sp`: padrão completo; é a referência.
- `new-balance-204l`: possui página guia estável (`new-balance-204l-original-brasil-guia-lk`), mas ainda precisa padronizar linkagem/CTA pós-grid/FAQ/mídia no mesmo formato Moon Shoe.
- `adidas-samba-jane`: possui copy editorial de coleção, mas não possui guia estável detectado no padrão Moon Shoe.
- `onitsuka-tiger`: possui guia estável, mas não foi confirmado no fluxo completo coleção ↔ guia.
- `onitsuka-tiger-todos-os-modelos`: copy melhorada, sem guia estável detectado.
- `onitsuka-tiger-mexico-66`: copy melhorada, sem guia estável dedicado detectado.
- `new-balance-9060`: possui guia (`new-balance-9060-guia`) e bloco visual, mas não está padronizado como Moon Shoe.
- `new-balance-530`: possui sinais de bloco/link editorial, mas sem página estável própria detectada.

## Preview a preparar no tema dev

Tema alvo esperado:

- `lk-new-theme/dev`
- tipo: unpublished/dev theme

URLs de preview esperadas após execução:

- New Balance 204L:
  - `https://lksneakers.com.br/collections/new-balance-204l?preview_theme_id=155065450718&_ab=0&_fd=0&_sc=1`

- Adidas Samba Jane:
  - `https://lksneakers.com.br/collections/adidas-samba-jane?preview_theme_id=155065450718&_ab=0&_fd=0&_sc=1`

## Mudanças previstas no dev theme — sem produção

Para cada coleção do lote 1:

1. Inserir CTA pós-grid para `Guia editorial LK`.
2. Garantir que a coleção continue product-first.
3. Criar/ajustar bloco de guia com CTA de volta para a coleção.
4. Repensar FAQ por objeções reais de compra:
   - autenticidade/originalidade;
   - como escolher versão/colorway;
   - forma/tamanho com linguagem canônica: `tem a forma grande ou pequena?`;
   - onde comprar original no Brasil;
   - por que comprar com curadoria humana.
5. Adicionar bloco de mídia/contexto quando houver fonte confiável.
6. Rodar forbidden-term scan:
   - `estoque`
   - `encomenda`
   - `pronta entrega`
7. QA mobile:
   - produtos aparecem rápido;
   - guia não compete com grid;
   - FAQ não duplica;
   - CTA visível e funcional.

## Risco

- Baixo em dev theme: não altera produção.
- Médio se criar páginas públicas em Shopify durante o preview, porque Page é objeto global e não theme-specific.
- Mitigação: no preview, preferir template/section dev ou páginas não publicadas/rascunho quando possível; produção só após aprovação explícita.

## Bloqueios atuais

Este turno foi roteado como `preparar approval packet`, então não foi executada escrita externa em Shopify/dev theme.

Para executar o upload no tema dev no próximo passo, Lucas precisa aprovar especificamente:

> “Aprovado subir no tema dev o Lote 1: New Balance 204L e Adidas Samba Jane, sem produção.”

## Rollback

Para qualquer upload no dev theme:

1. baixar asset atual antes do PUT;
2. salvar `asset.before` local;
3. aplicar patch mínimo;
4. ler de volta via Admin API;
5. salvar `asset.after` e `receipt.json`;
6. rollback = reenviar `asset.before` ao dev theme.

Para produção futura:

1. redescobrir theme `role=main`;
2. snapshot antes;
3. publicar somente assets aprovados;
4. validar DOM público por URL;
5. agendar revisão D+7.

## Decisão necessária

Autorizar o próximo passo seguro:

**Subir no tema dev o Lote 1 — New Balance 204L + Adidas Samba Jane — sem produção.**
