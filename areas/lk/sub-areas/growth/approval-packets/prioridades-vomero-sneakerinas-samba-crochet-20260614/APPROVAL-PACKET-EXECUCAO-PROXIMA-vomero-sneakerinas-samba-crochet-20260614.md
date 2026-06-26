# Approval Packet — Execução próxima: Vomero + Sneakerinas + Samba Crochet

Data: 2026-06-14  
Status: **pronto para decisão** — artefatos locais preparados, nenhum write Shopify executado.

## Decisão pedida ao Lucas
Aprovar ou ajustar a execução abaixo:

### Opção A — Recomendada agora
Aprovar **somente preview/draft Shopify não publicado** para:
1. Criar/validar página draft `guia-sneakerinas-ballet-sneakers` sem publicar.
2. Preparar alterações Vomero em staging/dev/preview quando aplicável, sem mexer em produção.
3. Não alterar preço, estoque, prazo, disponibilidade nem campanhas.

### Opção B — Produção parcial
Aprovar produção apenas para campos SEO/copy de Vomero listados no candidate payload, com snapshot/readback/rollback.

### Opção C — Segurar writes
Manter tudo local e completar GA4/GSC/GMC antes de qualquer preview externo.

## Artefatos preparados

Pasta:
`approval-packets/prioridades-vomero-sneakerinas-samba-crochet-20260614/final-execution-candidates/`

Arquivos:
- `CANDIDATE-vomero-premium-shopify-seo-faq-payload.json`
- `CANDIDATE-shopify-page-guia-sneakerinas-ballet-sneakers.json`
- `CANDIDATE-samba-crochet-cluster.json`

## Escopo 1 — Vomero Premium P1

### Collection `/collections/nike-vomero-premium`
Proposto:
- SEO title: `Nike Vomero Premium Original | LK Sneakers`
- SEO meta: `Nike Vomero Premium original na curadoria LK: ZoomX, Air Zoom, amortecimento máximo e design running lifestyle com atendimento humano para escolher.`
- Ajustar FAQ inicial para não misturar Vomero 5 com Vomero Premium.
- Reforçar links internos para guia e PDPs prioritários.

### Guia `/pages/nike-vomero-premium-guia`
Proposto:
- SEO title: `Nike Vomero Premium Original | Guia LK`
- SEO meta: `Guia LK do Nike Vomero Premium: ZoomX, Air Zoom, conforto máximo, estética running e como escolher com curadoria.`
- Adicionar/ativar FAQPage schema após QA de template.

### PDPs top
Prioridade por receita:
- `tenis-nike-vomero-premium-black-volt-preto`
- `tenis-nike-vomero-premium-sail-coconut-milk-branco`
- `tenis-nike-vomero-premium-flat-stout-marrom`
- `tenis-nike-vomero-premium-barely-volt-cinza`
- `tenis-nike-vomero-premium-white-bright-crimson-branco`

Atenção: termos de prazo/disponibilidade dependem de `lk-stock`; Growth não altera isso sozinho.

## Escopo 2 — Guia Sneakerinas / Ballet Sneakers

### Page draft proposta
- Handle: `guia-sneakerinas-ballet-sneakers`
- Title/SEO title: `Sneakerinas e Ballet Sneakers | Guia LK`
- Meta: `Guia LK de sneakerinas e ballet sneakers: Adidas Ballerina, Taekwondo Mei Ballet, Tokyo Mary Jane e modelos baixos com curadoria premium.`
- Primary CTA: `/collections/ballet-core`
- Estado recomendado: `published=false` até QA visual e approval final.

### Conteúdo cobre
- O que é sneakerina / ballet sneaker.
- Por que virou tendência.
- Modelos LK: Adidas Ballerina Bad Bunny, Taekwondo Mei Ballet, Tokyo Mary Jane, Speedcat Ballet como tendência se aplicável, Samba Crochet como adjacente.
- Como escolher, styling, fit e FAQ.

## Escopo 3 — Samba Crochet

Proposto agora:
- Não criar guia separado ainda.
- Tratar como mini-cluster comercial/PDP:
  - Sand Strata
  - Orbit Green
- Copy: textura crochet/artesanal + base Samba clássica.
- Próxima validação: GSC para queries `samba crochet`, `adidas samba crochet`, `samba og crochet`.

## Risco e rollback

### Risco
- Baixo se for apenas draft/preview não publicado.
- Médio se alterar SEO/copy em produção.
- Alto se qualquer alteração tocar disponibilidade, prazo, estoque, preço ou campanhas — fora do escopo.

### Rollback obrigatório para write aprovado
1. Snapshot admin/public antes.
2. Aplicar alteração escopada.
3. Readback admin/public.
4. Receipt no Brain.
5. Revisão de impacto em ~7 dias: Shopify + GA4 + GSC.

## O que ainda falta para decision-grade completo
- GA4 por URL/landing: sessões, conversão, receita.
- GSC por query/page: impressões, cliques, CTR, posição.
- GMC read-only para warnings/reprovações dos PDPs Vomero/Samba/Ballet.
- QA visual mobile se page draft for criado.

## Minha recomendação executiva
Aprovar **Opção A**: criar/validar preview/draft não publicado de Sneakerinas e preparar Vomero em ambiente seguro. Depois de QA visual, pedir aprovação separada para produção.
