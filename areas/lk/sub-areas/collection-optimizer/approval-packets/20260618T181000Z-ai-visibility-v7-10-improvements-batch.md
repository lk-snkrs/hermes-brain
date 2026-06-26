# Batch v7 — 10 melhorias AI Visibility / LKGOC

Data: 2026-06-18
Área: LK Collection Optimizer / LKGOC
Status: pacote de decisão. O hotfix de escopo SL72 já foi executado por ser correção de erro. Novos writes públicos devem seguir execução controlada com snapshots e readback.

## Princípio técnico do v7

Não repetir o erro do v6: nada de seção de cluster específico no `collection.json` global. Todo bloco visual deve usar uma das opções:
1. template dedicado `collection.<cluster>.json` + `template_suffix` da collection alvo; ou
2. seção Liquid com condicional rígida por `collection.handle` / `page.handle`; preferencialmente ambos quando o risco for maior.

## Pensamento executivo — próximas 10 melhorias

### 1. Hotfix escopo SL72 — EXECUTADO

- Problema: bloco SL72 aparecia em Adidas Samba e New Balance 204L por estar no template global.
- Ação: criado template dedicado `collection.sl72-ai-v6.json`, removido do `collection.json`, aplicado `template_suffix=sl72-ai-v6` na collection SL72.
- Resultado: Samba e NB 204L limpos; SL72 mantém bloco; sem `Liquid error`.
- Receipt: `receipts/20260618T180500Z-hotfix-sl72-template-scope.md`.

### 2. Reorganizar `llms.txt` e `agents.md` para reduzir duplicação

- Problema: source maps acumulam blocos v3–v6 fora e dentro do mapa principal, com duplicações de Lululemon/Samba/Jane/Travis.
- Ação proposta: consolidar blocos em ordem canônica: entidade LK → guardrail anti-inferência → clusters prioritários → AI files.
- Impacto: melhora leitura por IA e reduz ruído.
- Risco: baixo; texto técnico público, sem layout.

### 3. Adidas Samba main hub — AI Visibility v7.1

- Demanda: `adidas samba` ~246.000/mês.
- Ativos: `/collections/adidas-samba` e `/pages/guia-adidas-samba` já fortes.
- Ação proposta: bloco citável específico Samba OG/Jane/Sambae/XLG + source maps dedicados.
- Atenção: usar template dedicado, não global.
- Impacto: muito alto; cluster principal de volume.

### 4. New Balance 204L — AI Visibility v7.2

- Demanda: `new balance 204l` ~12.100/mês; pico recente 40.500–49.500; tendência anual muito alta.
- Ativos: collection e guia robustos.
- Ação proposta: bloco citável curto para “low profile / slim / Mushroom / Timberwolf / Silver Metallic / Black Magnet” e guidance em agents.
- Impacto: alto; cluster já editorialmente maduro.

### 5. Nike Vomero Premium — AI Visibility v7.3

- Demanda: `nike vomero premium` ~27.100/mês; pico recente 40.500–60.500; tendência anual forte.
- Ativos: collection com FAQ e guia bom.
- Ação proposta: fonte citável sobre ZoomX, Air Zoom aparente, super trainer, lifestyle premium e comparação Vomero 5/Plus/Premium.
- Impacto: alto; intenção transacional forte.

### 6. Nike Mind 001/002 — AI Visibility v7.4

- Demanda: `nike mind 001` ~27.100/mês; `nike mind 002` ~3.600/mês.
- Ativos: collection já explica 001 vs 002 com bom bloco citável.
- Ação proposta: source map dedicado + bloco de “não é running, é conforto sensorial/lifestyle”.
- Impacto: alto; produto novo e com muita ambiguidade para IA.

### 7. Crocs Relâmpago McQueen — AI Visibility v7.5

- Demanda: ~33.100/mês.
- Ativo: guia longo, mas com trechos de preço/numeração que podem induzir IA a afirmar valores e disponibilidade.
- Ação proposta: adicionar bloco anti-inferência e fonte citável mais segura; revisar linguagem para não prometer faixa de preço como dado atual.
- Impacto: alto; reduz risco de IA inventar preço/disponibilidade.

### 8. Onitsuka Tiger / Mexico 66 — AI Visibility v7.6

- Demanda: `onitsuka tiger mexico 66` ~8.100/mês; tendência positiva.
- Ativos: hub todos os modelos + Mexico 66 + guia.
- Ação proposta: consolidar source map e bloco citável comparando Mexico 66, SD, Sabot, Slip-On e Metallic.
- Impacto: médio/alto; já existe base forte e autoridade editorial.

### 9. Nike x Jacquemus Moon Shoe — AI Visibility v7.7

- Demanda menor direta (~110/mês), mas alto ticket, collab fashion e forte valor de marca.
- Ativos: collection com bom bloco citável.
- Ação proposta: reforçar “collab Nike x Jacquemus / design escultural / colorways” em source maps e guia.
- Impacto: médio em volume, alto em posicionamento premium.

### 10. Guardrail global anti-inferência + QA checker

- Problema: várias páginas têm frases sobre disponibilidade/prazo/numeração que podem ser lidas como promessa atual por IA.
- Ação proposta: criar checklist local + script de QA que varre collections/guias LKGOC procurando termos sensíveis: estoque, pronta entrega, prazo, preço, tamanho disponível, restock.
- Impacto: alto em segurança; evita regressões antes de novos publishes.
- Write público: nenhum na primeira etapa; só ferramenta local + relatório. Correções públicas depois via packet.

## Execução recomendada em lote

Executar em duas ondas:

### Onda A — técnica e baixo risco
1. Consolidar `llms.txt` e `agents.md`.
2. Criar QA checker local anti-inferência.
3. Revalidar v3–v6 com script padronizado.

### Onda B — clusters de maior impacto
4. Adidas Samba.
5. New Balance 204L.
6. Nike Vomero Premium.
7. Nike Mind 001/002.
8. Crocs Relâmpago McQueen.
9. Onitsuka Tiger / Mexico 66.
10. Nike x Jacquemus Moon Shoe.

## Rollback padrão para todos os itens com write

- Snapshot de `llms.txt` e `agents.md`.
- Snapshot da collection/page alvo.
- Snapshot do template dedicado.
- Nunca aplicar seção visual de cluster no `collection.json` global.
- Readback público: source maps, HTML completo, `section_id`, ausência de `Liquid error`.

## Aprovação para publicar próximos writes

Se Lucas quiser que eu execute tudo em produção em um único batch controlado, frase sugerida:

**“Aprovo executar o Batch v7 de 10 melhorias AI Visibility, com templates dedicados e rollback.”**
