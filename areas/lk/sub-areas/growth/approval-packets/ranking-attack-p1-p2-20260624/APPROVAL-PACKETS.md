# Ranking Attack — Etapas 1, 2 e 3 — 2026-06-24

Pedido Lucas: executar sequencialmente:
1. **No-rework audit / histórico verificado**
2. **Read-only live check**
3. **Approval packets curtos para ataque**

Escopo: SEMrush Position Tracking 2026-06-24 + histórico Brain + readback público + DataForSEO demanda/SERP.  
Status: **sem writes externos nesta rodada**.

---

## Etapa 1 — No-rework audit / histórico verificado

### Veredito executivo
- **Não devemos retrabalhar Onitsuka/Mexico 66 agora**: já houve guias/source page/coleção, meta do PDP Kill Bill foi corrigida em 2026-06-24 e precisa D+7/D+14.
- **Vomero Premium e Nike Mind continuam P1**, mas não como “criar do zero”: já há superfícies boas; o ataque é refino de snippet/PDP/FAQ/linkagem.
- **New Balance 9060 é o maior gap bruto**, mas a collection já existe e está tecnicamente razoável; o problema parece ser autoridade/intenção/competição + PDPs com meta operacional/dinâmica, não ausência total de página.
- **Alo Yoga é oportunidade de activewear premium**, mas a collection está rasa: title curto, meta curta e sem FAQPage.
- **Samba tem histórico enorme de execução**; qualquer novo ataque precisa ser no-rework granular por URL/keyword antes de write.

### Histórico por frente

| Frente | Histórico encontrado | Interpretação no-rework |
|---|---|---|
| Onitsuka / Mexico 66 | Muitos receipts, guias, source pages, ranking reports, ajuste SEO meta do PDP Kill Bill em 2026-06-24 | **Defender/medir**, não mexer pesado antes D+7/D+14 |
| Nike Mind 001/002 | Approval packets, reports GSC/CTR, PDP FAQ/GEO Top50, recomendação recente de CTR + FAQ/schema único | **Atacar com cuidado**: validar o que já foi aplicado por handle antes de novo write |
| Nike Vomero Premium | Reports e public hub audit; Command Center 2026-06-22 marcou P1 com demanda + possível duplicidade/limpeza FAQ/schema | **Atacar agora** com packet específico, sem mexer em collection boa se não precisar |
| New Balance 9060 | Histórico de LKGOC/dev/collection, Top50 PDP; SEMrush mostra maior gap | **Diagnóstico + packet P2**, foco em PDPs e reforço sem refazer scaffold |
| Alo Yoga / Lululemon | Lululemon já trabalhado e ranqueando; Alo Yoga aparece menos maduro | **Lululemon defender; Alo Yoga melhorar superfície** |
| Adidas Samba | Histórico muito extenso de Samba/Samba Jane; alta competição | **Backlog P2**, só com no-rework por URL |

Evidência de histórico indexada em: `work/ranking-attack-no-rework-20260624/history-index.json`.

---

## Etapa 2 — Read-only live check

### Readback público das superfícies principais

| Superfície | HTTP | Title atual | Meta atual | FAQPage | Observação |
|---|---:|---|---|---:|---|
| Vomero collection | 200 | `Nike Vomero Premium — Comprar | LK Sneakers` | `Nike Vomero Premium original na LK: super trainer com ZoomX, Air Zoom aparente, amortecimento máximo, curadoria premium e atendimento humano.` | 1 | Boa; não parece prioridade mexer em collection SEO field |
| Vomero PDP Black Volt | 200 | `Tênis Nike Vomero Premium Black Volt | LK Sneakers` | `Nike Vomero Premium Black Volt original. Amortecimento premium, visual running moderno, curadoria LK e compra segura em até 10x.` | 1 | Meta usa linguagem de parcelamento; oportunidade de snippet premium |
| Nike Mind collection | 200 | `Nike Mind 001 e 002 Original no Brasil | LK` | `Nike Mind 001 e 002 original no Brasil: compare slides e sneakers Nike Mind com curadoria LK, autenticidade e atendimento humano para escolher modelo.` | 1 | Boa; collection já está alinhada |
| Nike Mind PDP Light Bone | 200 | `Slide Nike Mind 001 Light Bone | LK Sneakers` | `Nike Mind 001 Light Bone original. Slide escultural Nike, curadoria LK, atendimento humano para tamanho e compra segura em até 10x.` | 1 | Meta usa parcelamento; oportunidade de limpar snippet |
| NB 9060 collection | 200 | `New Balance 9060 original | Curadoria LK Sneakers` | `New Balance 9060 original na curadoria LK: silhueta escultural, conforto urbano e colorways selecionadas com atendimento humano para escolher melhor.` | 1 | Técnica boa; desafio é autoridade/intenção e PDPs |
| NB 9060 PDP Bisque | 200 | `Tênis New Balance 9060 Bisque Sea Salt Bege | LK Sneakers` | `Tênis New Balance 9060 Bisque Sea Salt Bege original. a partir de R$ 2400 em 10x sem juros. Curadoria LK · Frete grátis +R$500 · LK Sneakers` | 1 | Meta muito operacional/dinâmica: preço, 10x, frete |
| Alo Yoga collection | 200 | `Alo Yoga | LK Sneakers` | `Alo Yoga na LK Sneakers: curadoria premium, produtos originais e atendimento humano para uma escolha segura.` | 0 | Rasa: title curto, sem FAQPage, handle `-1` |
| Samba collection | 200 | `Adidas Samba Original | LK Sneakers` | `Adidas Samba original na curadoria LK: colorways desejadas, autenticidade e atendimento humano para escolher tamanho, estilo e melhor modelo.` | 1 | Boa; backlog, não P1 imediato |
| Lululemon collection | 200 | `Lululemon Original | Curadoria Athleisure LK` | `Lululemon original na curadoria LK: peças athleisure selecionadas, autenticidade, atendimento humano e compra segura no Jardins ou online.` | 1 | Boa; defender e cruzar conversão |

Arquivo readback: `work/ranking-attack-no-rework-20260624/live-readback-public.json`.

### Demanda / SERP adicionada

- DataForSEO Brasil/pt confirmou volumes altos:
  - `new balance 9060`: **246.000/mês**, transacional.
  - `adidas samba feminino`: **60.500/mês**, transacional.
  - `nike vomero premium`: **27.100/mês**, transacional.
  - `nike mind 001`: **27.100/mês**, transacional e pico recente forte.
  - `alo yoga`: **27.100/mês**, intenção principal informacional.
  - `lululemon`: **40.500/mês**, intenção principal navegacional.
- SERP mobile `nike vomero premium`: Nike/Centauro dominam orgânico; LK aparece em shopping/merchant para produto Vomero, mas não no orgânico Top 10 textual do DataForSEO.
- SERP mobile `new balance 9060`: New Balance/Netshoes/Artwalk dominam; SERP tem PAA sobre preço/originalidade/comparação 530 vs 9060 e Popular Products. LK não apareceu no Top 10 orgânico textual.

---

## Etapa 3 — Approval packets curtos

## Packet A — P1 Nike Vomero Premium — snippet/PDP cleanup + links

### Status
**needs-approval** para qualquer write em Shopify.  
**Recomendação:** aprovar primeiro este packet, por melhor combinação de volume + posição atacável + fit premium.

### Fatos
- SEMrush: `nike vomero premium` posição 15, volume 14.800 no export; DataForSEO atual mostra 27.100/mês.
- `vomero premium` posição 14, volume 9.900.
- Collection atual está boa: title/meta fortes e 1 FAQPage.
- PDP Black Volt tem meta: `compra segura em até 10x`, linguagem mais operacional e menos premium.
- SERP mostra PAA: existência do Vomero Premium, função do Vomero, se é bom, preço no Brasil.

### Interpretação
Não precisa refazer collection. O ganho mais seguro é melhorar **PDP/snippet + bloco citável + linkagem**, com cuidado para não mexer em preço/estoque/campanha.

### Proposta exata — write mínimo
**PDP:** `/products/tenis-nike-vomero-premium-black-volt-preto`

- SEO title proposto:
`Nike Vomero Premium Black Volt Original | LK`

- Meta description proposta:
`Nike Vomero Premium Black Volt original na LK: super trainer com ZoomX, Air Zoom aparente, curadoria exclusiva e atendimento humano para escolher.`

### Opcional em dev/packet posterior
- Adicionar/refinar FAQ visível e FAQPage se o readback mostrar desalinhamento:
  - O que é o Nike Vomero Premium?
  - O Vomero Premium serve para corrida ou lifestyle?
  - Qual a diferença entre Vomero Premium, Vomero Plus e Vomero 5?
  - Como escolher tamanho no Vomero Premium?
- Link interno collection → PDP Black Volt/Volt Tint/White Bright Crimson.

### Risco / esforço / rollback
- Esforço: baixo se for só SEO title/meta.
- Risco: baixo.
- Rollback: salvar SEO fields anteriores e reverter campo a campo.
- Medição: D+7/D+14 em SEMrush + GSC query/page + sessões orgânicas.

### Aprovação sugerida
`Aprovo ajustar somente SEO title e meta description do PDP Nike Vomero Premium Black Volt para os textos propostos, com rollback e readback, sem alterar preço, estoque, descrição visível, FAQ, schema, theme, campanha, Klaviyo ou WhatsApp.`

---

## Packet B — P1 Nike Mind 001 — CTR/snippet cleanup sem retrabalho

### Status
**needs-approval**, mas antes do write recomendo confirmar handles exatos já alterados no pacote anterior de Nike Mind.

### Fatos
- SEMrush: `nike mind 001` posição 11; `nike mind` posição 15.
- DataForSEO: `nike mind 001` 27.100/mês, maio 110.000, transacional.
- Collection `/collections/nike-mind-001` está boa: title/meta alinhados e 1 FAQPage.
- PDP Light Bone, landing atual do SEMrush para `nike mind 001`, tem meta com `compra segura em até 10x`.

### Interpretação
A collection já está forte; a oportunidade é PDP/snippet e consistência com queries de decisão: original, Brasil, chinelo/slide.

### Proposta exata — write mínimo
**PDP:** `/products/slide-nike-mind-001-light-bone-bege`

- SEO title proposto:
`Nike Mind 001 Light Bone Original | LK`

- Meta description proposta:
`Nike Mind 001 Light Bone original na LK: slide escultural da linha Nike Mind, curadoria exclusiva e atendimento humano para orientar tamanho e escolha.`

### Antes de executar
- Readback Admin dos PDPs Black Chrome/Pearl Pink/Light Bone para evitar retrabalho.
- Se Black Chrome/Pearl Pink já foram otimizados, não repetir.

### Risco / rollback
- Esforço baixo; risco baixo; rollback por SEO fields.

### Aprovação sugerida
`Aprovo preparar readback Admin dos PDPs Nike Mind 001 e, se Light Bone ainda estiver com SEO meta operacional, ajustar somente SEO title/meta do PDP Light Bone para os textos propostos, com rollback/readback, sem alterar preço, estoque, descrição visível, FAQ, schema, theme, campanha, Klaviyo ou WhatsApp.`

---

## Packet C — P2 New Balance 9060 — superfície + PDP cleanup

### Status
**needs-attention / needs-approval após validação**, porque é o maior gap bruto, mas não é simples title/meta.

### Fatos
- SEMrush/DataForSEO indicam volume massivo: `new balance 9060` 165.000–246.000/mês.
- LK tem collection `/collections/new-balance-9060` com title/meta bons e 1 FAQPage.
- PDP Bisque tem meta operacional: preço, 10x, frete.
- SERP é dominada por New Balance, Netshoes, Artwalk e Popular Products. PAA: preço EUA, 530 vs 9060, valor original, como saber se é original.

### Interpretação
O problema não é “não existe página”. É força competitiva + alinhamento de conteúdo/PDP + merchant/popular products + long-tail feminino/original/sea salt/bege.

### Proposta etapa 1 — sem write imediato
- Fazer readback Admin da collection e Top PDPs 9060.
- Mapear PDPs 9060 com meta operacional/dinâmica.
- Ver se collection tem bloco comparativo 9060 vs 530/204L e FAQ real-intent.

### Proposta exata — primeiro write candidato
**PDP:** `/products/tenis-new-balance-9060-bisque-sea-salt-bege`

- SEO title proposto:
`New Balance 9060 Bisque Sea Salt Original | LK`

- Meta description proposta:
`New Balance 9060 Bisque Sea Salt original na LK: silhueta escultural, conforto urbano, curadoria premium e atendimento humano para escolher.`

### Risco / rollback
- Risco baixo para PDP meta; médio para mexer em collection/FAQ.
- Medir D+7/D+14, mas 9060 pode exigir horizonte maior por competição.

### Aprovação sugerida
`Aprovo somente readback Admin e auditoria dos Top PDPs New Balance 9060 para mapear metas operacionais e oportunidades de collection/FAQ, sem write. Depois quero o packet final antes de executar.`

---

## Packet D — P2 Alo Yoga — activewear premium surface

### Status
**needs-attention** porque há demanda e ranking atacável, mas superfície está rasa.

### Fatos
- SEMrush: `alo yoga` posição 14, volume 14.800.
- DataForSEO: `alo yoga` 27.100/mês; intenção principal informacional, com potencial comercial em `brasil`, `top`, `calça`, `bolsa`.
- Collection atual: title `Alo Yoga | LK Sneakers`, meta curta, 0 FAQPage, canonical `/collections/alo-yoga-1`.

### Interpretação
Alo Yoga é oportunidade real, mas deve virar um mini-hub premium de activewear, não só title/meta. O handle `-1` merece investigação antes de qualquer mudança estrutural.

### Proposta exata — write mínimo candidato
**Collection:** `/collections/alo-yoga-1`

- SEO title proposto:
`Alo Yoga Original no Brasil | Curadoria LK`

- Meta description proposta:
`Alo Yoga original na curadoria LK: activewear premium, tops, calças e peças selecionadas com autenticidade e atendimento humano para escolher.`

### Proposta conteúdo/FAQ posterior
- O que é Alo Yoga?
- A Alo Yoga vende no Brasil?
- Como escolher peças Alo Yoga originais?
- Diferença entre Alo Yoga e Lululemon.

### Risco / rollback
- SEO title/meta: baixo.
- FAQ/conteúdo/handle: médio; handle/canonical exige cuidado e não deve ser alterado sem plano de redirect/rollback.

### Aprovação sugerida
`Aprovo preparar um packet completo de Alo Yoga collection com readback Admin, proposta de SEO title/meta, FAQ e plano de canonical/handle, sem executar write até minha aprovação final.`

---

## Priorização final

1. **Executar Packet A — Nike Vomero Premium PDP meta**: maior chance de ganho rápido com baixo risco.
2. **Preparar/validar Packet B — Nike Mind 001 PDPs**: evitar retrabalho, depois limpar snippet do PDP que ainda estiver operacional.
3. **Auditar Packet C — New Balance 9060**: maior upside, mas precisa mapa de superfície/PDPs.
4. **Preparar Packet D — Alo Yoga**: boa frente premium, mas precisa conteúdo/FAQ e decisão sobre handle.
5. **Samba**: backlog após no-rework específico.
6. **Onitsuka/Lululemon/Crocs**: defender e medir, não mexer pesado agora.

---

## Dados faltantes para decision-grade completo

- GSC query/page atualizado para cada URL candidata.
- GA4/Shopify por landing: sessões orgânicas, CVR, receita, add-to-cart.
- Readback Admin dos campos SEO por handle antes de qualquer write.
- Merchant/Popular Products para 9060/Vomero se formos atacar shopping visibility.

