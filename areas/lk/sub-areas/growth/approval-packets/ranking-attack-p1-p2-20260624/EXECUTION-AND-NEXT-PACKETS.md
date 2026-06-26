# Ranking Attack — execução aprovada 1–5 — 2026-06-24

Aprovação Lucas: “aprovo do 1 ao 5”.

## Status geral

- **Writes executados:** somente os escopos mínimos previamente propostos para Packet A e Packet B.
- **Writes não executados:** New Balance 9060, Alo Yoga, Samba — ficaram em auditoria/packet, pois o próprio plano previa diagnóstico/packet antes de alteração.
- **Nenhum preço, estoque, descrição visível, FAQ, schema, theme, campanha, Klaviyo ou WhatsApp foi alterado.**

---

## 1) Packet A — Nike Vomero Premium — executado

**Produto:** `tenis-nike-vomero-premium-black-volt-preto`

### Antes
- Title: `Tênis Nike Vomero Premium Black Volt | LK Sneakers`
- Meta: `Nike Vomero Premium Black Volt original. Amortecimento premium, visual running moderno, curadoria LK e compra segura em até 10x.`

### Depois
- Title: `Nike Vomero Premium Black Volt Original | LK`
- Meta: `Nike Vomero Premium Black Volt original na LK: super trainer com ZoomX, Air Zoom aparente, curadoria exclusiva e atendimento humano para escolher.`

### Verificação
- Shopify Admin GraphQL: OK.
- Descrição visível: inalterada.
- Público com `view=`/variant: OK.
- URL canônica limpa: ainda pode mostrar cache antigo temporariamente.

---

## 2) Packet B — Nike Mind 001 — executado condicionalmente

Readback Admin confirmou que Black Chrome/Pearl Pink/Light Bone deveriam ser verificados; Light Bone ainda estava com snippet operacional.

**Produto ajustado:** `slide-nike-mind-001-light-bone-bege`

### Antes
- Title: `Slide Nike Mind 001 Light Bone | LK Sneakers`
- Meta: `Nike Mind 001 Light Bone original. Slide escultural Nike, curadoria LK, atendimento humano para tamanho e compra segura em até 10x.`

### Depois
- Title: `Nike Mind 001 Light Bone Original | LK`
- Meta: `Nike Mind 001 Light Bone original na LK: slide escultural da linha Nike Mind, curadoria exclusiva e atendimento humano para orientar tamanho e escolha.`

### Verificação
- Shopify Admin GraphQL: OK.
- Descrição visível: inalterada.
- Público com `view=`/variant: OK.
- URL canônica limpa: ainda pode mostrar cache antigo temporariamente.

Receipt/rollback dos writes: `receipts/shopify-production/ranking-attack-approved-1-2-20260624T135820Z/`.

---

## 3) New Balance 9060 — auditoria executada; packet final recomendado

### Achados
- Collection `new-balance-9060` está boa: title/meta fortes e FAQPage único.
- Problema principal: PDPs com metas operacionais/dinâmicas e truncadas.
- Exemplos:
  - `tenis-new-balance-9060-bisque-sea-salt-bege`: meta com preço/10x/frete.
  - `tenis-new-balance-9060-cortado-marrom`: meta com preço/10x/frete.
  - `tenis-new-balance-9060-angora-sea-salt-bege`: meta com frete/10x.
  - alguns PDPs têm meta truncada por limite de caracteres.

### Próximo packet recomendado
Lote de PDP SEO meta 9060, começando por:
1. `tenis-new-balance-9060-bisque-sea-salt-bege`
2. `tenis-new-balance-9060-cortado-marrom`
3. `tenis-new-balance-9060-angora-sea-salt-bege`

Primeiro candidato:
- Title: `New Balance 9060 Bisque Sea Salt Original | LK`
- Meta: `New Balance 9060 Bisque Sea Salt original na LK: silhueta escultural, conforto urbano, curadoria premium e atendimento humano para escolher.`

**Status:** precisa aprovação específica antes de write.

---

## 4) Alo Yoga — packet completo preparado; não executado

### Achados
- Collection `alo-yoga-1` é rasa:
  - Title: `Alo Yoga | LK Sneakers`
  - Meta curta
  - 0 FAQPage
- Vários PDPs Alo Yoga têm metas operacionais agressivas:
  - “Compra agora”
  - “parcelamento sem juros”
  - “envio imediato”
  - checkmarks/benefícios logísticos

### Proposta collection
- Title: `Alo Yoga Original no Brasil | Curadoria LK`
- Meta: `Alo Yoga original na curadoria LK: activewear premium, tops, calças e peças selecionadas com autenticidade e atendimento humano para escolher.`

### Proposta conteúdo/FAQ posterior
- O que é Alo Yoga?
- A Alo Yoga vende no Brasil?
- Como escolher peças Alo Yoga originais?
- Diferença entre Alo Yoga e Lululemon.

**Status:** precisa aprovação específica antes de qualquer write; não mexer em handle/canonical sem plano.

---

## 5) Samba — no-rework específico executado; sem write

### Achados SEMrush
- Já ranqueia bem para termos específicos:
  - `adidas samba jane` pos. 2
  - `samba vermelho` pos. 3
  - `adidas samba crochet` pos. 3
- Oportunidades 11–30:
  - `samba branco` pos. 17
  - `samba verde` pos. 18, landing no blog
  - `adidas samba marrom` pos. 19
  - `adidas samba feminino` pos. 26, volume alto
  - `tenis adidas samba` pos. 28, volume alto
- Sem ranking:
  - `adidas samba masculino`
  - `adidas samba og`
  - `adidas samba preto`
  - `adidas samba original`
  - `adidas samba xlg`

### Leitura
Samba tem muito histórico e alta concorrência; não fazer write genérico. Melhor próximo passo é um packet por landing:
1. collection `adidas-samba` para `adidas samba feminino` e `tenis adidas samba`;
2. PDP Marrom para `adidas samba marrom`;
3. blog/collection para `samba verde`.

**Status:** sem write; preparar packet específico se virar P2.

---

## Prioridade próxima recomendada

1. Aguardar cache público canônico de Vomero/Mind ou revalidar em algumas horas.
2. Pedir aprovação para lote mínimo New Balance 9060 PDP meta, se quiser atacar maior gap.
3. Em paralelo, preparar Alo Yoga collection packet completo com FAQ/SEO, sem handle change.
4. Samba fica P2 após 9060/Alo.

## Evidências

- History index: `work/ranking-attack-no-rework-20260624/history-index.json`
- Public live readback: `work/ranking-attack-no-rework-20260624/live-readback-public.json`
- Admin read-only 9060/Alo/Samba: `work/ranking-attack-no-rework-20260624/admin-readonly-collections-nb9060-alo-samba.fixed.json`
- Write receipt/rollback: `receipts/shopify-production/ranking-attack-approved-1-2-20260624T135820Z/`
