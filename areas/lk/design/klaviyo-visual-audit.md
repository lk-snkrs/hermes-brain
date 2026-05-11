# Auditoria visual Klaviyo — base do DesignMD LK

Data: 2026-05-09
Modo: leitura via API Klaviyo, sem envio, sem alteração de campanha, sem publicação.

## E-mails usados como referência

1. `Dia das Mães — NB 204L — LK Sneakers`
   - Status: enviado
   - Envio: 2026-05-08
   - Assunto: `O presente que a sua mãe merece — NB 204L, pronta entrega e entrega expressa SP.`
   - Template Klaviyo: `R2xnnC`

2. `Top 10 Sneakers Abril 2026 — LK Sneakers`
   - Status: enviado
   - Envio: 2026-05-05
   - Assunto: `Top 10 Sneakers de Abril — os mais escolhidos da LK.`
   - Template Klaviyo: `UQiUim`

3. `Dia das Mães by Lala Noleto — LK Sneakers`
   - Status: enviado
   - Envio: 2026-04-30
   - Assunto: `O presente perfeito para ela — Dia das Mães by Lala Noleto.`
   - Template Klaviyo: `WbRxEi`

## Padrões observados

- Fundo geral branco/off-white muito claro, com divisórias `#EEEEEE` sutis. Evitar fundo cinza forte no corpo do e-mail.
- Header preto alto com logo branco centralizado, referência mobile/Klaviyo: cerca de 150px de altura e logo 70–80px.
- Barra de contexto/microcopy logo abaixo do header em fundo branco, uppercase, cinza claro, letter-spacing alto.
- Conteúdo central em largura de e-mail aproximada de 600px.
- Títulos serifados, com itálico bege para emoção/sofisticação.
- Corpo em sans-serif pequeno, cinza quente, com bastante entrelinha.
- Microcopy uppercase com letter-spacing alto.
- CTAs pretos, retangulares, pequenos e firmes.
- Produto como protagonista cromático; interface neutra.
- Para CRM/curadoria, o layout empilhado mobile-first ficou melhor que o card split: imagem em bloco branco amplo, texto em bloco bege abaixo e CTA centralizado. Usar split só quando a composição realmente ficar equilibrada.
- Grid 2 colunas para ranking/top produtos.
- Badge de ranking preto com texto branco.
- Bloco manifesto preto com frase editorial.
- Footer preto com slogan `O que é raro, merece ser encontrado`.
- O slogan deve aparecer apenas no footer, não no header.

## Feedback Lucas — 2026-05-09

- Direção geral aprovada como boa primeira opção, ainda não 100%.
- Corrigir preview para usar o logo real branco da LK no topo e no rodapé.
- Produto/imagens precisam carregar no HTML de aprovação; usar imagens reais e, quando necessário, embutidas no HTML para evitar falha de carregamento.
- Fonte ainda não está 100% igual à usada nas newsletters; manter como hipótese v0.1 e refinar depois contra Klaviyo/Shopify.
- Seguir nesse caminho e refinar progressivamente.
- Lucas esclareceu que o preview serve para aprovar estética/global design direction; não está pronto para envio ao cliente nem publicação.

## Tokens extraídos dos templates

### Cores recorrentes

- `#0A0A0A`
- `#1A1A1A`
- `#F0ECE8`
- `#F5F4F2`
- `#FFFFFF`
- `#E8E6E2`
- `#DDD0C0`
- `#C8A98A`
- `#D4B896`
- `#8A8580`
- `#B5B0A8`

### Fontes observadas

- `DM Sans`
- `Cormorant Garamond`
- fallback serif: `Georgia`
- fallback sans: `Arial`

## Decisão

O DesignMD v0.1 da LK deve seguir a lógica dos e-mails Klaviyo, não um visual premium genérico. O primeiro HTML anterior falhou justamente por não ancorar na comunicação real da LK.
