# Approval packet — Curadoria LK PDP batch de gaps (100 auditados) — DEV

Data: 2026-06-26  
Agente: lk-shopify  
Superfície: Shopify theme DEV/unpublished / PDP `lk-variante`

## Pedido

Lucas pediu continuar adicionando produtos faltantes na Curadoria LK dentro do PDP, com audit de 100 produtos faltantes e intenção de adicionar tudo em lote.

## Guardrail aplicado

- Esta etapa executou **auditoria read-only** e preparou escopo.
- Não houve write externo, upload DEV, PR, merge Production, metafield, produto, preço, estoque ou checkout.
- Estoque/disponibilidade não foi consultado nem prometido; curadoria é editorial/relacional.

## Fontes

- `/collections/all?sort_by=best-selling` público para ordem de prioridade.
- Shopify Admin read-only para título/vendor/tags/imagem/status.
- GitHub `production` do tema: `sections/lk-pdp.liquid` + 19 snippets `lk-variante*`.
- Probe público de marker `data-lk-variante` quando não bloqueado por challenge.

Artefatos locais:

- `/opt/data/profiles/lk-shopify/workdirs/curadoria-audit-100-missing-20260626/audit_100_missing_v2.json`
- `/opt/data/profiles/lk-shopify/workdirs/curadoria-audit-100-missing-20260626/audit_100_missing_v2.md`
- `/opt/data/profiles/lk-shopify/workdirs/curadoria-audit-100-missing-20260626/source_full_check_summary.json`

## Resultado do audit

- Produtos varridos: `260`.
- Gaps públicos até corte: `120`.
- Top 100 gaps analisados contra fonte completa do tema: `100`.
- Já estavam em fonte `lk-variante*` mas não apareceram no probe público: `51` — tratar como render/QA/repair, não duplicar grupo.
- Ausentes também da fonte `lk-variante*`: `49` — candidatos reais para novos grupos/lotes.

## Clusters ausentes da fonte — candidatos reais

| Família | Qtd | Melhor rank | Handles |
|---|---:|---:|---|
| Outros / avaliar | 10 | 68 | `tenis-adidas-samba-cardboard-marrom, tenis-onitsuka-tiger-moage-co-cream-black-bege, tenis-adidas-ballerina-bad-bunny-black-chalk-preto, tenis-onitsuka-tiger-tiger-corsair-a55-black-cream-preto, tenis-onitsuka-tiger-mexico-mid-runner-birch-indian-ink-bege, tenis-onitsuka-tiger-gsm-cream-black-gum-off-white, onitsuka-tiger-california-78-ex-black-oatmel-preto, calca-pace-pf-sweatpants-preto` |
| Air Jordan 1 Low | 6 | 98 | `tenis-air-jordan-1-low-se-paw-print-pink-foam-rosa, tenis-air-jordan-1-low-se-silver-metallic-cinza, air-jordan-1-low-se-vivid-orange, tenis-air-jordan-1-low-nike-sail-soft-pearl-sequins-couro-nobuck, tenis-air-jordan-1-low-se-gs-glitter-swoosh-branco-1, air-jordan-1-low-panda-2023` |
| Rhode | 5 | 18 | `the-peptide-lip-tints-rhode-multicolor, rhode-pocket-blush, lip-case-rhode-by-hailey-bieber, lip-case-rhode-by-hailey-bieber-grey-cinza, the-peptide-lip-tints-rhode-limited-edition-shade-dourado` |
| Onitsuka Tiger Mexico 66 | 5 | 112 | `tenis-onitsuka-tiger-mexico-66-cream-light-sage-bege, tenis-onitsuka-tiger-mexico-66-triple-black-preto, onitsuka-tiger-mexico-66-paraty-natural-navy-bege, tenis-onitsuka-tiger-mexico-66-slip-on-birch-midnight-bege, tenis-onitsuka-tiger-mexico-66-oatmeal-ginger-peach-rosa` |
| Saint Studio Apparel | 3 | 36 | `camiseta-saint-studio-classy-suedine-supima-chairs-branco, bolsa-saint-studio-tote-museo-preto, calca-saint-studio-alfaiataria-leve-prega-dupla-marrom` |
| MASP Apparel | 3 | 43 | `camiseta-masp-x-leonilson-sem-titulo-marrom, camiseta-masp-x-leonilson-34-com-cicatrizes-branco, camiseta-masp-x-leonilson-o-grande-rio-branco` |
| Havaianas | 3 | 65 | `chinelo-havaianas-x-dolce-gabanna-leopard-marrom, chinelo-havaianas-x-dolce-gabanna-blue-mediterraneo-azul, chinelo-havaianas-x-dolce-gabanna-carreto-ciciliano-vermelho` |
| Alo Apparel/Accessories | 3 | 105 | `top-alo-yoga-aspire, short-alo-yoga-match-point, bone-alo-yoga-off-duty-preto` |
| Sufgang Apparel | 2 | 107 | `camiseta-sufgang-basic-pack-5-8-azul, camiseta-sufgang-basic-pack-5-8-verde` |
| Crocs | 1 | 50 | `crocs-classic-clog-x-the-cars-lightning-mcqueen-vermelho` |
| Aimé Leon Dore Hats | 1 | 82 | `bone-5-panel-aime-leon-dore-unisphere-branco` |
| Adidas Campus | 1 | 117 | `adidas-campus-00s-kids-black-white-gum` |
| Nude Project Apparel | 1 | 123 | `camiseta-nude-project-global-soon` |
| Jason Markk | 1 | 139 | `jason-markk-delicates-cleaning-brush` |
| New Balance 9060 | 1 | 156 | `tenis-new-balance-9060-kids-rose-sugar-ice-wine-rosa` |
| Onitsuka Tiger Mexico 66 SD | 1 | 162 | `onitsuka-tiger-mexico-66-sd-metallic-series-metropolis-cream-cinza` |
| Adidas Gazelle | 1 | 167 | `tenis-adidas-gazelle-x-clot-linen-khaki-light-blue-marrom` |
| Adidas Samba OG | 1 | 168 | `tenis-adidas-samba-og-metallic-silver-prata` |

## Separação operacional

### Lote A — adicionar/expandir `lk-variante` em DEV

Priorizar grupos de sneaker/acessório com família clara e 2+ produtos ausentes, por exemplo:

- Air Jordan 1 Low / Mid-High repair;
- Adidas Samba/Cardboard/Disney especiais se fizer sentido editorial;
- Rhode / Jason Markk / Havaianas / Crocs ficam fora do `lk-variante` sneaker por padrão, salvo decisão explícita de criar módulos próprios.

### Lote B — repair de render público

Há `51` handles no top 100 que já aparecem nos arquivos `lk-variante*`, mas o probe público não confirmou marker. Não duplicar esses grupos antes de verificar a causa: challenge público, cache, render condition ou snippet antigo.

## Risco

- Médio se tentar “100 de uma vez” sem separar por famílias: risco de falsa relação editorial e Liquid grande/difícil de revisar.
- Baixo/médio se executar em DEV por batches agrupados, com snippets isolados e render line única no top30/router.
- Production continua bloqueado sem aprovação separada após preview.

## Plano DEV recomendado

1. Criar um batch DEV com grupos claros e snippets isolados.
2. Não criar curadoria para itens que não são PDP sneaker/variante sem decisão explícita.
3. Para os 48 source/public divergentes, primeiro rodar QA focado e reparar render, sem duplicar.
4. Upload DEV/unpublished, readback por asset SHA, QA público dos handles âncora, relatório.

## Aprovação necessária para write DEV

Para executar o próximo passo com write em DEV/unpublished, responder:

> Aprovo DEV batch Curadoria LK dos gaps auditados, começando pelos grupos acionáveis de sneaker e repair source/public, sem Production merge.

## Reminder OS

- loop needed: yes
- owner: lk-shopify
- next action: aguardar aprovação DEV; se aprovada, gerar snippets/patch DEV com batch agrupado e QA.
- review trigger: resposta do Lucas com aprovação/ajuste de escopo.
- evidence: este approval packet + artefatos do audit local.