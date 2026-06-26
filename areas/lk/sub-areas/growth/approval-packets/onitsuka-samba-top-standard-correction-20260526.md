# Approval packet — correção de padrão visual Onitsuka + Samba

Status: preparado localmente; sem write Shopify neste turno.

## Contexto

Lucas apontou que o padrão aprovado para as próximas coleções não foi aplicado corretamente: Onitsuka Tiger Mexico 66 e Adidas Samba ficaram sem o topo editorial com fotos/moodboard.

## Falha reconhecida

A execução anterior aplicou principalmente o padrão de conteúdo pós-grid:

- produtos primeiro;
- guia editorial depois do grid;
- FAQ única;
- FAQPage schema;
- blocos citáveis;
- sem CTA `ver produtos`.

Mas faltou aplicar o padrão visual completo do topo:

- H1 nativo preservado;
- descrição editorial curta;
- composição com fotos/moodboard;
- mobile comprimido para não empurrar produtos demais;
- paridade visual com coleções já aprovadas.

## Evidência verificada

### Onitsuka Tiger Mexico 66

Preview verificado: `https://lksneakers.com.br/collections/onitsuka-tiger-mexico-66?preview_theme_id=155065450718`

- Topo tem H1 + descrição + `LER MAIS +`.
- Topo não tem imagem/moodboard.
- Bloco `Sinal editorial` ainda aparece no DOM.
- Guia pós-grid existe com id `lk-guia-onitsuka-tiger-mexico-66`.

### Adidas Samba

Preview verificado: `https://lksneakers.com.br/collections/adidas-samba?preview_theme_id=155065450718`

- Topo tem H1 + descrição + `LER MAIS +`.
- Topo não tem imagem/moodboard.
- Bloco `Sinal editorial` ainda aparece no DOM.
- Guia pós-grid existe com id `lk-guia-adidas-samba`.

## Escopo correto da correção em dev theme

Aplicar somente no tema dev `lk-new-theme/dev`:

1. Remover `Sinal editorial` de Onitsuka e Samba.
2. Criar/ligar guia editorial separado por coleção:
   - Onitsuka: `/pages/guia-onitsuka-tiger-mexico-66`
   - Samba: `/pages/guia-adidas-samba`
3. Trocar o guia longo embutido na coleção por CTA/link discreto para o guia completo.
4. Aplicar topo visual padronizado nos dois handles:
   - descrição curta;
   - fotos/moodboard;
   - sem duplicar H1;
   - sem linguagem operacional pública;
   - mobile comprimido.
5. Validar por DOM + screenshot/vision antes de apresentar novo preview.

## QA obrigatório antes de reenviar preview

- `topHasImages = true` para os dois handles.
- `Sinal editorial` ausente no body text/DOM.
- Apenas um H1 visível por coleção.
- Produtos continuam acessíveis rapidamente no mobile.
- Nenhuma ocorrência de `pronta entrega`, `encomenda`, `estoque imediato`, `ver produtos da coleção` nos inserts novos.
- Guia completo existe como destino ou permanece claramente como pendência antes de produção.
- FAQ visível única por coleção.
- FAQPage schema sem duplicação.

## Rollback planejado

Antes de qualquer write dev:

- backup de `sections/lk-collection.liquid`;
- backup de templates/pages se usados;
- receipt com hash before/after/readback;
- restauração via asset anterior se o preview ficar fora do padrão.

## Nota operacional

Este turno está limitado a pesquisa/síntese/documentação local. Nenhum write Shopify foi executado aqui. O próximo turno executável deve aplicar a correção em dev theme com backup/readback/visual QA.
