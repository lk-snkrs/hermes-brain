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

- Header preto com logo branco centralizado.
- Barra de contexto/microcopy logo abaixo do header.
- Fundo geral off-white quente.
- Conteúdo central em largura de e-mail aproximada de 640px.
- Títulos serifados, com itálico bege para emoção/sofisticação.
- Corpo em sans-serif pequeno, cinza quente, com bastante entrelinha.
- Microcopy uppercase com letter-spacing alto.
- CTAs pretos, retangulares, pequenos e firmes.
- Produto como protagonista cromático; interface neutra.
- Grid 2 colunas para ranking/top produtos.
- Badge de ranking preto com texto branco.
- Bloco manifesto preto com frase editorial.
- Footer preto com slogan `Less Noise, More Identity.`

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
