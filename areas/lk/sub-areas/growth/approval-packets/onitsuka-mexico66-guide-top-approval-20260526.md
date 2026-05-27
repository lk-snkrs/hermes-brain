# Approval packet — Onitsuka Tiger Mexico 66 collection + guia editorial

Status: preparação local concluída. Nenhum write externo executado nesta etapa.

## Pedido de Lucas

1. Remover o rótulo `Sinal editorial` da coleção.
2. Criar guia editorial para adicionar/linkar na coleção.
3. Ajustar a parte de cima da coleção com descrição + fotos, não apenas texto.

## Entregáveis preparados

### 1. Guia editorial completo — página/snippet

Arquivo local:

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/drafts/guias-editoriais/lk-onitsuka-mexico66-guide-page-20260526.liquid`

Conteúdo:

- página editorial em HTML/Liquid pronta para `/pages/guia-onitsuka-tiger-mexico-66`;
- padrão visual tipo source page, inspirado no padrão Moon Shoe;
- H1 editorial;
- hero escuro premium;
- CTA para coleção;
- blocos citáveis, sem rótulo técnico visível;
- tabela comparativa Mexico 66 clássico vs SD vs Sabot vs Slip-on;
- seção de sinais de moda com Vogue, Vogue HK e Hypebeast;
- FAQ visível;
- FAQPage schema;
- copy focada em versão, material, proporção, cor e contexto de uso.

Meta sugerida:

- Title: `Guia Onitsuka Tiger Mexico 66: versões, materiais e como escolher | LK Sneakers`
- Description: `Entenda o Onitsuka Tiger Mexico 66, diferenças entre materiais, versões e colorways icônicas com a curadoria premium da LK Sneakers.`

### 2. Patch do topo da coleção — dev/preview

Arquivo local:

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/approval-packets/onitsuka-mexico66-top-patch-draft-20260526.liquid`

O patch propõe:

- esconder a descrição padrão textual do topo atual;
- inserir bloco visual premium no topo com copy + 3 imagens/moodboard;
- usar imagens de produto LK-owned/CDN Shopify:
  - Mexico 66 Kill Bill;
  - Mexico 66 SD Beige Beet Juice;
  - Mexico 66 Sabot Beige Green;
- manter produtos como prioridade da coleção;
- trocar o guia longo pós-grid por chamada curta: `Abrir guia completo`;
- link alvo: `/pages/guia-onitsuka-tiger-mexico-66`;
- remover qualquer rótulo editorial indevido visível.

## Evidências e verificações locais

- Guia novo verificado localmente contra termos proibidos públicos:
  - `Sinal editorial`: ausente;
  - `pronta entrega`: ausente;
  - `encomenda`: ausente;
  - `estoque`: ausente;
  - `Bloco citável`: ausente.
- Patch do topo não contém linguagem pública de pronta entrega/encomenda/estoque.
- O termo de remoção do rótulo editorial aparece apenas como comentário operacional no patch, não como texto renderizado.
- Nenhum write Shopify foi feito.

## Impacto esperado

- Corrige a crítica principal: a coleção deixa de parecer um bloco genérico e passa a explicar diferença entre versão, material, proporção e uso.
- Melhora SEO/GEO com conteúdo mais citável e FAQ estruturado.
- Melhora CRO ao orientar escolha antes do usuário ir para atendimento ou PDP.
- Mantém linguagem premium: curadoria exclusiva, autenticidade e orientação humana.

## Risco

- Baixo se aplicado somente no tema dev/preview.
- Médio se a página `/pages/guia-onitsuka-tiger-mexico-66` for criada já pública sem revisão visual.
- Baixo/médio no topo: depende de validar visual mobile para não empurrar demais o grid.
- As imagens do guia editorial incluem fonte Vogue como referência externa no hero; para produção, mais seguro usar hero com asset LK/CDN ou manter a imagem externa somente como card de referência.

## Rollback

Para dev theme:

- Antes de aplicar via API, gerar backup de `sections/lk-collection.liquid`.
- Rollback: restaurar o asset anterior por Shopify Admin API.
- Referência de rollback já existente para estado anterior: `areas/lk/sub-areas/growth/receipts/theme-dev/dev-phase1-onitsuka-samba-guides-20260526-013141/sections__lk-collection.before.liquid`.

Para Page Shopify, se criada:

- Antes de criar/editar, salvar JSON/body/template da página.
- Rollback: remover a página criada ou restaurar body/SEO/template anterior.

## Decisão recomendada

Aprovar aplicação **somente no tema dev/preview** para:

1. inserir o topo visual da coleção Onitsuka Tiger Mexico 66;
2. remover o rótulo editorial indevido;
3. encurtar o guia pós-grid e linkar para `/pages/guia-onitsuka-tiger-mexico-66`;
4. criar a página guia em ambiente controlado/preview, preferencialmente sem produção até validação visual.

## Aprovação necessária

Preciso de aprovação explícita para executar write via Shopify API no tema dev/preview.

Frase suficiente: `Aprovo aplicar no dev/preview Onitsuka Mexico 66`.

Produção continua fora deste pacote, salvo aprovação separada.
