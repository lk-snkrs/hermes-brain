# Approval Packet — PDP SEO Estratégico — 2026-06-16

## Escopo

Pacote read-only para ajustar SEO fields de PDPs estratégicos LK.

Superfície afetada se aprovado:

- Shopify Product SEO title
- Shopify Product SEO description

Nenhum write foi executado neste pacote.

## Evidência coletada

Fonte read-only:

- Shopify Admin GraphQL `productByHandle`
- HTML live dos PDPs públicos

Arquivos de evidência:

- `reports/assets/pdp-seo-package-20260616/pdp-seo-expanded-readonly.json`
- `reports/assets/pdp-seo-package-20260616/pdp-seo-recommendations.json`

## Diagnóstico resumido

Pior classe encontrada: produtos Nike Mind com SEO title/description vazios no Admin, fazendo o tema gerar title/meta com preço/parcelamento e descrições longas.

Principais problemas:

- Titles acima de 60 caracteres
- Meta descriptions acima de 155 caracteres
- SEO fields vazios no Admin em produtos Mind recentes
- Titles com reticência literal em alguns New Balance (`…`), ruim para snippet e controle editorial

## P1 — Aplicar primeiro

### 1. Tênis Nike Mind 002 Sail Bege

Handle:

`tenis-nike-mind-002-sail-bege`

URL:

`https://lksneakers.com.br/products/tenis-nike-mind-002-sail-bege`

Atual:

- SEO title Admin: vazio
- SEO description Admin: vazia
- Document title live: `Tênis Nike Mind 002 Sail Bege por R$ 3.199,99 em até 10x | LK Sneakers`
- Title length: `70`
- Meta length: `320`

Proposto:

- SEO title: `Tênis Nike Mind 002 Sail Bege | LK Sneakers`
- Title length: `43`
- SEO description: `Nike Mind 002 Sail Bege original. Design escultural Nike, curadoria LK, atendimento humano e compra segura em até 10x sem juros.`
- Description length: `128`

### 2. Tênis Nike Mind 002 Thunder Blue Azul

Handle:

`tenis-nike-mind-002-thunder-blue-azul`

Atual:

- SEO title Admin: vazio
- SEO description Admin: vazia
- Title length: `78`
- Meta length: `319`

Proposto:

- SEO title: `Tênis Nike Mind 002 Thunder Blue | LK Sneakers`
- Title length: `46`
- SEO description: `Nike Mind 002 Thunder Blue original. Modelo lifestyle Nike com design escultural, curadoria LK, compra segura e até 10x sem juros.`
- Description length: `130`

### 3. Tênis Nike Mind 002 Light Violet Ore Roxo

Handle:

`tenis-nike-mind-002-light-violet-ore-roxo`

Atual:

- SEO title Admin: vazio
- SEO description Admin: presente
- Title length: `82`
- Meta length: `141`

Proposto:

- SEO title: `Tênis Nike Mind 002 Light Violet Ore | LK Sneakers`
- Title length: `50`
- SEO description: `Nike Mind 002 Light Violet Ore original. Design escultural Nike, curadoria LK, atendimento humano e compra segura em até 10x sem juros.`
- Description length: `135`

### 4. Slide Nike Mind 001 Sail Bege

Handle:

`slide-nike-mind-001-sail-bege`

Atual:

- SEO title Admin: vazio
- SEO description Admin: vazia
- Title length: `78`
- Meta length: `320`

Proposto:

- SEO title: `Slide Nike Mind 001 Sail Bege | LK Sneakers`
- Title length: `43`
- SEO description: `Nike Mind 001 Sail Bege original. Slide escultural Nike com curadoria LK, atendimento humano para tamanho e compra em até 10x sem juros.`
- Description length: `136`

### 5. Slide Nike Mind 001 Geode Teal Verde

Handle:

`slide-nike-mind-001-geode-teal-verde`

Atual:

- SEO title Admin: vazio
- SEO description Admin: vazia
- Title length: `85`
- Meta length: `320`

Proposto:

- SEO title: `Slide Nike Mind 001 Geode Teal | LK Sneakers`
- Title length: `44`
- SEO description: `Nike Mind 001 Geode Teal original. Slide escultural Nike com curadoria LK, atendimento humano para tamanho e compra em até 10x sem juros.`
- Description length: `137`

### 6. Slide Nike Mind 001 Light Bone Bege

Handle:

`slide-nike-mind-001-light-bone-bege`

Atual:

- SEO title Admin: `Nike Mind 001 Slide Light Bone Original — Slide Premium | LK Sneakers`
- Title length: `69`
- Meta length: `114`

Proposto:

- SEO title: `Slide Nike Mind 001 Light Bone | LK Sneakers`
- Title length: `44`
- SEO description: `Nike Mind 001 Light Bone original. Slide escultural Nike, curadoria LK, atendimento humano para tamanho e compra segura em até 10x.`
- Description length: `131`

## P2 — Corrigir controle editorial

### 7. New Balance 204L Mushroom Arid Stone Marrom

Handle:

`tenis-new-balance-204l-mushroom-arid-stone-marrom`

Atual:

- SEO title Admin contém reticência: `Tênis New Balance 204L Mushroom Arid Stone Ma… | LK Sneakers`
- Document title length: `60`
- Meta length: `146`

Proposto:

- SEO title: `Tênis New Balance 204L Mushroom | LK Sneakers`
- Title length: `45`
- SEO description: `New Balance 204L Mushroom Arid Stone original. Silhueta retrô premium, curadoria LK, atendimento humano e compra segura em até 10x.`
- Description length: `131`

### 8. New Balance 530 White Natural Indigo

Handle:

`new-balance-530-white-natural-indigo-1`

Atual:

- SEO title Admin contém reticência: `Tênis New Balance 530 White Natural Indigo Br… | LK Sneakers`
- Document title length: `60`
- Meta length: `146`

Proposto:

- SEO title: `Tênis New Balance 530 White Indigo | LK Sneakers`
- Title length: `48`
- SEO description: `New Balance 530 White Natural Indigo original. Clássico running lifestyle, curadoria LK, atendimento humano e compra segura em até 10x.`
- Description length: `135`

## P3 — Opcional / já aceitável

Estes estão aceitáveis, mas podem receber padronização editorial se você quiser deixar a família mais consistente:

### Nike Mind 002 Light Khaki Bege

- Handle: `tenis-nike-mind-002-light-khaki-bege`
- Status atual: OK/ajuste fino
- Proposto: `Tênis Nike Mind 002 Light Khaki Bege | LK Sneakers`
- Meta proposta: `Nike Mind 002 Light Khaki Bege original. Design escultural Nike, curadoria LK, atendimento humano e compra segura em até 10x sem juros.`

### Nike Mind 001 Pearl Pink Rosa

- Handle: `slide-nike-mind-001-pearl-pink-rosa`
- Status atual: OK/ajuste fino
- Proposto: `Slide Nike Mind 001 Pearl Pink | LK Sneakers`
- Meta proposta: `Nike Mind 001 Pearl Pink original. Slide de design sensorial Nike com curadoria LK, atendimento humano e compra segura em até 10x.`

### Nike Vomero Premium Black Volt

- Handle: `tenis-nike-vomero-premium-black-volt-preto`
- Status atual: OK/ajuste fino
- Proposto: `Tênis Nike Vomero Premium Black Volt | LK Sneakers`
- Meta proposta: `Nike Vomero Premium Black Volt original. Amortecimento premium, visual running moderno, curadoria LK e compra segura em até 10x.`

### New Balance 204L Timberwolf Bege

- Handle: `tenis-new-balance-204l-timberwolf-bege`
- Status atual: OK/ajuste fino
- Proposto: `Tênis New Balance 204L Timberwolf | LK Sneakers`
- Meta proposta: `New Balance 204L Timberwolf Bege original. Silhueta retrô premium, curadoria LK, atendimento humano e compra segura em até 10x.`

### Yeezy Slide Glow Green

- Handle: `yeezy-slide-glow-green`
- Status atual: OK/ajuste fino
- Proposto: `Yeezy Slide Glow Green Original | LK Sneakers`
- Meta proposta: `Yeezy Slide Glow Green original. Slide adidas Yeezy com curadoria LK, guia de tamanho dedicado e compra segura em até 10x sem juros.`

## Recomendações de aplicação

### Opção A — Conservadora

Aplicar somente P1:

- 6 produtos Nike Mind com problema claro.

Vantagem:

- maior impacto e menor risco.

### Opção B — Recomendada

Aplicar P1 + P2:

- 6 produtos Nike Mind críticos
- 2 New Balance com reticência em SEO title

Vantagem:

- corrige problemas objetivos e padroniza snippets estratégicos.

### Opção C — Full polish

Aplicar P1 + P2 + P3:

- todos os 13 PDPs auditados.

Vantagem:

- máxima consistência editorial.

Risco:

- mexe em produtos que já estão aceitáveis.

## Risco

Baixo-médio.

- Não altera preço, estoque, disponibilidade, imagens ou variantes.
- Altera apenas campos SEO de produto.
- Pode alterar snippet exibido pelo Google com atraso/crawl.
- Requer readback pós-write e QA live dos PDPs principais.

## Rollback

Antes de qualquer aplicação, salvar snapshot dos campos atuais:

- product id
- handle
- SEO title atual
- SEO description atual

Rollback:

- restaurar os valores do snapshot nos mesmos produtos.
- readback Shopify Admin.
- conferir HTML live de pelo menos Mind 002 Sail, Mind 001 Sail, 204L Mushroom e NB530.

## Aprovação necessária

Qualquer aplicação exige aprovação explícita de Lucas, porque é write em Shopify Product SEO fields.

Decisão sugerida:

- Aprovar Opção B — P1 + P2.
