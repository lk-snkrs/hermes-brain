---
version: alpha
name: LK Sneakers
lastUpdated: "2026-05-09"
description: "Sistema visual LK derivado dos últimos e-mails enviados no Klaviyo: editorial, premium, silencioso, curatorial e orientado a produto como objeto de desejo."
colors:
  primary: "#0A0A0A"
  secondary: "#8A8580"
  tertiary: "#C8A98A"
  neutral: "#F0ECE8"
  ink: "#0A0A0A"
  ink-soft: "#1A1A1A"
  paper: "#F0ECE8"
  paper-soft: "#F5F4F2"
  surface: "#FFFFFF"
  bone: "#FDF9F5"
  line: "#E8E6E2"
  line-warm: "#DDD0C0"
  muted: "#8A8580"
  muted-light: "#B5B0A8"
  accent: "#C8A98A"
  accent-soft: "#E8D8C4"
  accent-warm: "#D4B896"
typography:
  display:
    fontFamily: "Cormorant Garamond, Georgia, serif"
    fontSize: 56px
    fontWeight: 400
    lineHeight: 0.95
    letterSpacing: "-0.03em"
  display-italic:
    fontFamily: "Cormorant Garamond, Georgia, serif"
    fontSize: 52px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: "-0.03em"
    fontStyle: italic
  headline:
    fontFamily: "Cormorant Garamond, Georgia, serif"
    fontSize: 34px
    fontWeight: 400
    lineHeight: 1.05
    letterSpacing: "-0.02em"
  body:
    fontFamily: "DM Sans, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.75
    letterSpacing: "0em"
  micro:
    fontFamily: "DM Sans, Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: "0.22em"
  product-name:
    fontFamily: "Cormorant Garamond, Georgia, serif"
    fontSize: 25px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: "-0.015em"
  price:
    fontFamily: "DM Sans, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.3
rounded:
  none: 0px
  subtle: 2px
spacing:
  xs: 8px
  sm: 12px
  md: 20px
  lg: 32px
  xl: 48px
  xxl: 72px
  section: 96px
components:
  header-brand:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface}"
    padding: 26px 44px
  context-bar:
    backgroundColor: "{colors.ink-soft}"
    textColor: "{colors.accent-soft}"
    typography: "{typography.micro}"
    padding: 11px 44px
  button-primary:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface}"
    typography: "{typography.micro}"
    rounded: "{rounded.none}"
    padding: 14px 22px
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.micro}"
    rounded: "{rounded.none}"
    padding: 13px 20px
  ranking-badge:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface}"
    typography: "{typography.micro}"
    rounded: "{rounded.none}"
    padding: 7px 9px
  product-card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: 24px
---

## Overview

A comunicação visual da LK Sneakers é **editorial, premium, silenciosa e curatorial**. O produto deve aparecer como objeto de desejo em uma galeria, não como item de varejo genérico. O sistema foi derivado dos últimos e-mails enviados no Klaviyo, especialmente:

- `Dia das Mães — NB 204L — LK Sneakers` — campanha enviada em 2026-05-08.
- `Top 10 Sneakers Abril 2026 — LK Sneakers` — campanha enviada em 2026-05-05.
- `Dia das Mães by Lala Noleto — LK Sneakers` — campanha enviada em 2026-04-30.

A assinatura conceitual observada é: **Less Noise, More Identity.**

O design deve vender por curadoria, intenção, silêncio visual e autoridade editorial. Evitar qualquer estética de promoção agressiva, marketplace, tech startup, dashboard ou ecommerce genérico.

## Colors

- **Ink `#0A0A0A`:** preto institucional. Usar em header, footer, CTAs, badges e blocos manifesto.
- **Ink Soft `#1A1A1A`:** preto secundário/grafite para barras contextuais.
- **Paper `#F0ECE8`:** fundo geral quente, herdado dos e-mails Klaviyo.
- **Paper Soft `#F5F4F2`:** fundo editorial claro para respiro.
- **Surface `#FFFFFF`:** área de produto, cards e imagens.
- **Bone `#FDF9F5`:** variação quente para blocos de leitura.
- **Line `#E8E6E2`:** divisórias sutis.
- **Line Warm `#DDD0C0`:** divisórias com calor editorial.
- **Muted `#8A8580`:** texto secundário.
- **Muted Light `#B5B0A8`:** microcopy discreta.
- **Accent `#C8A98A`:** bege/dourado claro usado com parcimônia em subtítulos, labels e detalhes emocionais.
- **Accent Soft `#E8D8C4`:** acento suave para barras e selos.

Regra: a interface quase não deve competir cromaticamente com o produto. As cores mais fortes devem vir do tênis/foto.

## Typography

A LK usa contraste entre **serifa editorial** e **sans-serif minimalista**.

- Títulos: `Cormorant Garamond, Georgia, serif`, peso regular, tracking levemente negativo.
- Destaques emocionais: mesma serifa em itálico, geralmente em bege/acento.
- Corpo e UI: `DM Sans, Arial, sans-serif`.
- Microcopy/labels/botões: uppercase, letter-spacing alto, tamanho pequeno.
- Evitar negritos pesados, grotesks largas, fontes arredondadas ou aparência tech.

Vocabulário visual/textual preferido:

- `curadoria`
- `mais escolhidos`
- `intenção`
- `permanência`
- `disponível`
- `explorar`
- `ver modelo`
- `pronta entrega`

Evitar:

- `imperdível`
- `mega oferta`
- `corre`
- `últimas unidades` como pressão agressiva
- excesso de exclamações

## Layout

- Largura editorial padrão de e-mail: `640px`.
- Para PDP/HTML web preview: conteúdo central com largura máxima entre `1120px` e `1240px`, mas mantendo a lógica de respiro dos e-mails.
- Header institucional preto com logo centralizado.
- Barra de contexto logo abaixo, com microcopy uppercase espaçada.
- Seções com muito espaço vertical: `72px–120px`.
- Divisórias finas de `1px`, sempre em tons quentes claros.
- Cards sem sombras fortes e sem radius evidente.
- Grid de produto: 2 colunas em desktop; 1 coluna em mobile.
- Produto isolado em fundo branco/off-white, grande, centralizado e com respiro.

## Elevation & Depth

A LK quase não usa elevação. A profundidade vem de:

- contraste entre preto institucional e fundos claros;
- divisórias finas;
- escala tipográfica;
- imagem de produto;
- blocos manifesto.

Evitar sombras, glassmorphism, gradientes e cards flutuantes.

## Shapes

- Botões retangulares, sem arredondamento visível.
- Badges retangulares pequenos.
- Imagens e cards com cantos retos.
- Ornamentos lineares curtos e discretos.

## Components

### Header institucional

Fundo preto, logo branco centralizado, sem menu excessivo.

### Barra de contexto

Microcopy uppercase com letter-spacing alto. Exemplos:

- `+ PRONTA ENTREGA · ENTREGA EXPRESSA PARA SÃO PAULO CAPITAL +`
- `ABRIL 2026 · OS MAIS ESCOLHIDOS`
- `CURADORIA LK · PRODUTO DIFÍCIL DE ENCONTRAR`

### Hero editorial

Estrutura:

1. Eyebrow uppercase.
2. Linha ornamental curta.
3. Título serifado.
4. Subtítulo itálico em bege.
5. Texto curto em cinza quente.
6. Selo/CTA logístico discreto.

### Card de produto

Anatomia:

1. Imagem grande em fundo branco.
2. Marca/categoria em microcopy uppercase.
3. Nome do produto em serifa.
4. Preço claro.
5. Parcelamento menor em cinza.
6. CTA preto pequeno: `COMPRAR`, `VER MODELO` ou `EXPLORAR`.

### Ranking badge

Pequeno badge preto com texto branco (`#1`, `#2`, etc.). Usar para Top 10, mais escolhidos, favoritos ou rankings por mês.

### Bloco manifesto

Fundo preto, frase serifada centralizada, assinatura pequena.

Exemplo:

> O que é escolhido com intenção, permanece.  
> — LK Sneakers

### CTA

Principal: fundo preto, texto branco, uppercase, letter-spacing alto, sem radius.

Secundário: link textual discreto com seta `→`, preferencialmente para WhatsApp.

## Do's and Don'ts

### Do

- Tratar produto como peça de curadoria.
- Usar bastante respiro.
- Manter paleta neutra e quente.
- Deixar o produto carregar a cor.
- Usar serifa editorial para desejo e intenção.
- Usar microcopy uppercase para estrutura.
- Usar CTAs pequenos, firmes e pretos.
- Construir narrativa: por que este produto importa para a LK.
- Usar rankings como prova social editorial, não como liquidação.

### Don't

- Não usar estética promocional agressiva.
- Não usar botões coloridos, arredondados ou grandes demais.
- Não usar sombra forte, gradiente ou glassmorphism.
- Não encher de badges, selos e urgência.
- Não parecer marketplace.
- Não parecer dashboard SaaS.
- Não publicar layout/PDP sem HTML visual de aprovação.
- Não comunicar produto sem status por tamanho/variante quando a ação for comercial.
