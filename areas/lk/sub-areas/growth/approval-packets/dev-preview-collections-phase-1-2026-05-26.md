# LK dev preview packet — coleções fase 1

Data: 2026-05-26
Modo: preparação local. Não executado em Shopify.

## Escopo sugerido para o próximo turno executável

Coleções:
1. `onitsuka-tiger-mexico-66`
2. `adidas-samba`

## Objetivo

Criar previews no tema Dev com o padrão aprovado em 204L/Samba Jane:

- produto primeiro;
- guia editorial depois do grid;
- FAQ única, útil e sem duplicação;
- bloco GEO citável;
- mobile comprimido;
- spacing pós-grid medido;
- lightbox funcional quando houver cards/imagens editoriais.

## O que fazer no Dev Theme

### Onitsuka Tiger Mexico 66

- Manter H1 nativo como único título principal.
- Criar/ajustar guia pós-grid com tom boutique premium.
- Usar FAQ única com perguntas de busca/compra:
  - Quanto custa um Onitsuka Tiger no Brasil?
  - Qual a diferença entre ASICS e Onitsuka Tiger?
  - O Onitsuka Tiger Mexico 66 é da ASICS?
  - Como escolher entre Mexico 66, SD, Sabot e Slip-on?
  - O Mexico 66 tem a forma grande ou pequena?
- Validar se o template já emite FAQ nativa; se sim, suprimir duplicação antes de adicionar qualquer schema.
- Se incluir imagens, usar assets LK/CDN ou marcar risco; validar lightbox.

### Adidas Samba

- Resolver o estado atual de FAQ: ou inserir Q&A real ou remover heading vazio.
- Criar guia pós-grid para coleção-mãe com comparação Samba OG / Samba Jane / Sambae / XLG.
- FAQ única:
  - Como saber se o Adidas Samba é original?
  - Qual a diferença entre Samba OG, Sambae, Samba Jane e Samba XLG?
  - Quanto custa um Adidas Samba original?
  - O Adidas Samba feminino muda forma/tamanho?
  - Qual Samba escolher para rotina?
- Evitar posicionamento de preço; competir por seleção especializada, originalidade assumida e atendimento humano.
- Herdar linguagem visual da Samba Jane sem duplicar o guia da própria Samba Jane.

## QA obrigatório antes de enviar preview

### DOM/texto

- Um H1 principal por collection.
- Uma ocorrência visível de `Perguntas Frequentes`.
- `FAQPage` ausente se FAQ invisível/duplicada; presente apenas se pergunta JSON-LD = pergunta visível.
- Nenhuma ocorrência pública de taxonomia operacional sensível como `sob encomenda`, `estoque imediato`, `envio em até 2 dias úteis` dentro do guia editorial novo.
- Sem CTA `Ver produtos da coleção` dentro do guia.

### Layout/mobile

- Produtos aparecem rapidamente no mobile.
- Guia aparece depois do grid.
- Gap pós-grid medido:
  - se `coll-loadmore` existe, não inventar spacer;
  - se não existe, aplicar spacer scoped e comprimido.
- Gutter alinhado ao padrão LK: desktop ~40px, mobile ~16px salvo exceção visual.

### Lightbox

Se houver card de imagem:

- Desktop: clique abre modal direto.
- Mobile colapsado: primeiro toque revela.
- Mobile expandido: segundo toque abre modal.
- Validar `modal img naturalWidth > 0` e `naturalHeight > 0`.
- Sem erro JS no console.

## Rollback/receipt esperado

Para cada asset alterado no dev theme:

- salvar `asset.before`, `asset.after`, `asset.readback`;
- registrar hashes;
- gerar preview URL com `preview_theme_id=155065450718` e cache-buster;
- registrar instrução de rollback.

## Boundary

Este arquivo é um packet local. Produção/live theme não está aprovado neste turno.
