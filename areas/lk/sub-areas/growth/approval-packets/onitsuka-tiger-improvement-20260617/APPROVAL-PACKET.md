# Approval Packet — melhorar coleção Onitsuka Tiger — 2026-06-17

Status: pronto para aprovação explícita. **Nenhum write executado.**

Página: `/collections/onitsuka-tiger-todos-os-modelos`  
Collection ID: `gid://shopify/Collection/458490904798`

## Por que mexer agora

- GSC 2026-05-18→2026-06-14: 861 cliques / 66.479 impressões / CTR 1,30% / posição 6,8.
- Query `onitsuka tiger`: 102 cliques / 29.510 impressões / CTR 0,35% / posição 8,2.
- Histórico comercial registrado no packet: 194 unidades / R$ 488.898,06 recentes na coleção; combinado local + recente: 836 unidades / R$ 2.013.531,68.
- Readback atual Shopify: 160 produtos na coleção; Online Store publicado; template `onitsuka-tiger-todos`.

## Mudança proposta — escopo pequeno e reversível

Executar somente:

1. `seo.title`
2. `seo.description`
3. `descriptionHtml` da coleção

Não executar:

- produtos, preço, estoque, feed/GMC, campanhas, theme, Klaviyo/WhatsApp, desconto, checkout.

## SEO title

Atual: `Onitsuka Tiger Original | Mexico 66 e Curadoria LK`  
Proposto: `Onitsuka Tiger Original no Brasil | Mexico 66 e LK`

Racional: inclui `Brasil`, mantém `Original`, `Mexico 66` e LK; busca aumentar CTR sem exagerar no snippet.

## Meta description

Atual: `Onitsuka Tiger original na LK Sneakers: Mexico 66 e modelos selecionados com curadoria premium, autenticidade e atendimento humano.`

Proposta: `Onitsuka Tiger original no Brasil: Mexico 66, SD, Sabot e modelos selecionados com curadoria LK, autenticidade e atendimento humano para escolher.`

Racional: cobre `Onitsuka Tiger original no Brasil`, modelos principais e atendimento humano; evita promessa de disponibilidade/prazo.

## Description/FAQ — diretriz

Substituir o texto atual por bloco mais premium e citável, com:

- abertura sobre curadoria e modelos;
- bloco “Como escolher seu Onitsuka Tiger”;
- bloco “Onitsuka Tiger original no Brasil”;
- bloco “Diferença entre Onitsuka Tiger e ASICS”;
- FAQ único com 5 perguntas:
  - Qual Onitsuka Tiger escolher: Mexico 66, SD ou Sabot?
  - O Onitsuka Tiger tem forma grande ou pequena?
  - Qual a diferença entre Onitsuka Tiger e ASICS?
  - Onitsuka Tiger combina com que tipo de look?
  - Onde comprar Onitsuka Tiger original no Brasil com segurança?

Payload exato salvo em: `approval-packets/onitsuka-tiger-improvement-20260617/proposed-payload.json`

## Limpeza de guardrail

O texto atual contém pontos que eu removeria:

- `numerações completas` — soa como promessa operacional de disponibilidade;
- `prazo e disponibilidade antes da compra` — disponibilidade pertence ao atendimento/stock, não à taxonomia pública de SEO;
- repetição `curadoria verificada` — menos premium e redundante.

## QA obrigatório se aprovado

- Backup antes: `seo.title`, `seo.description`, `descriptionHtml`.
- Mutation Shopify limitada à collection ID acima.
- Readback Admin confirmando os três campos.
- QA público:
  - HTTP 200 na coleção;
  - title/meta renderizados;
  - H1 não quebrado;
  - FAQ visível sem duplicação grosseira;
  - JSON-LD `FAQPage`, se renderizado pelo tema, com perguntas compatíveis.
- Secret hygiene: `values_printed=false`.

## Rollback

Restaurar os campos atuais:

- SEO title: `Onitsuka Tiger Original | Mexico 66 e Curadoria LK`
- SEO description: `Onitsuka Tiger original na LK Sneakers: Mexico 66 e modelos selecionados com curadoria premium, autenticidade e atendimento humano.`
- `descriptionHtml`: snapshot salvo antes da mutation.

## Impact review

- D+7 e D+14:
  - GSC page-level CTR: 1,30% → meta inicial ≥1,60%.
  - Query `onitsuka tiger`: CTR 0,35% → meta inicial ≥0,60% sem perda relevante de posição.
  - GA4/Shopify: sessões orgânicas, PDP views a partir da collection, add-to-cart e receita atribuída/assistida.

## Aprovação necessária

Para executar produção, preciso de aprovação explícita neste formato:

> Aprovo aplicar na coleção `/collections/onitsuka-tiger-todos-os-modelos` somente `seo.title`, `seo.description` e `descriptionHtml` conforme o packet `onitsuka-tiger-improvement-20260617`, sem mexer em produtos, preço, estoque, feed/GMC, campanhas, theme, Klaviyo/WhatsApp ou checkout, com backup, QA, rollback e revisão D+7/D+14.
