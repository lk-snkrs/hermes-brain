# Status atual — limpeza editorial de PDPs

Data: 2026-06-05T17:16:46.617157+00:00

## O que está sendo alterado

- Campo alterado: somente `product.descriptionHtml` — o texto editorial/descrição visível na PDP.
- Não está sendo alterado: produto, variante, estoque, preço, SKU, tag `encomenda`, inventoryPolicy, SEO title/meta, tema, checkout ou badge operacional `Sujeito a encomenda`.

## Tipos de troca

1. Prazo/estoque no FAQ da descrição:

> De: `Produtos em estoque: envio em até 2 dias úteis. Produtos sob encomenda: 4 a 6 semanas...`

> Para: `O prazo varia conforme a disponibilidade confirmada e a região de entrega. Itens sob encomenda seguem prazo estimado de 4 a 6 semanas...`

2. Fit/tamanho:

> De: `roda fiel`, `roda grande`, `rodar grande`

> Para: `tem forma fiel`, `tem forma grande`, `ter forma grande/ampla`

## Por quê

- Evitar promessa operacional errada em massa.
- Reduzir conflito entre descrição editorial e badge/fluxo de encomenda.
- Melhorar tom premium e clareza de atendimento.
- Tornar PDPs mais seguras para SEO/GEO/IA sem alterar operação.

## Estado atual após lotes já aplicados

- Produtos ainda com frase exata antiga de prazo: 698
- Produtos ainda com `roda/rodar/rodam`: 722

## Próximo passo recomendado

Pausar writes automáticos e seguir em lotes com resumo antes/depois mais explícito, para Lucas validar o padrão com clareza.

### Exemplos remanescentes de prazo
- `tenis-asics-gel-kayano-14-x-senna-black-gold-preto` — Tênis Asics Gel-Kayano 14 x Senna Black Gold Preto
- `tenis-asics-gel-kayano-14-x-senna-white-red-branco` — Tênis Asics Gel-Kayano 14 x Senna White Red Branco
- `tenis-asics-gel-nyc-x-pleasures-barely-rose-rosa` — Tênis Asics Gel-NYC x Pleasures Barely Rose Rosa
- `tenis-asics-gt-2160-white-putty-branco` — Tênis Asics GT-2160 White Putty Branco
- `tenis-asics-gt-2160-x-above-the-clouds-white-pure-silver-branco` — Tênis Asics GT-2160 x Above the Clouds White Pure Silver Branco
- `tenis-asics-gt-2160-x-gallery-dept-complexcon-cinza` — Tênis Asics GT-2160 x Gallery Dept. ComplexCon Cinza
- `tenis-asics-gt-2160-x-jjjound-white-branco` — Tênis Asics GT-2160 x JJJJound White Branco
- `tenis-asics-gt-2160-x-kith-marvel-villains-spider-man-venom-colorido` — Tênis Asics GT-2160 x Kith Marvel Villains Spider-Man/Venom Colorido
- `tenis-asics-gt-2160-x-papergirl-beams-white-silver-branco` — Tênis Asics GT-2160 x PaperGirl Beams White Silver Branco
- `tenis-adidas-badbo-1-0-rise-branco` — Tênis Bad Bunny x Adidas BADBO 1.0 Rise Branco

### Exemplos remanescentes de fit
- `ambush-x-nike-air-force-1-low-phantom` — Tênis Ambush x Nike Air Force 1 Low Phantom Branco
- `april-skateboards-x-nike-sb-dunk-low-turbo-green` — Tênis April Skateboards x Nike SB Dunk Low Turbo Green Azul
- `tenis-asics-gel-kayano-14-x-senna-black-gold-preto` — Tênis Asics Gel-Kayano 14 x Senna Black Gold Preto
- `tenis-asics-gel-kayano-14-x-senna-white-red-branco` — Tênis Asics Gel-Kayano 14 x Senna White Red Branco
- `tenis-asics-gel-nyc-x-pleasures-barely-rose-rosa` — Tênis Asics Gel-NYC x Pleasures Barely Rose Rosa
- `tenis-asics-gt-2160-white-putty-branco` — Tênis Asics GT-2160 White Putty Branco
- `tenis-asics-gt-2160-x-above-the-clouds-white-pure-silver-branco` — Tênis Asics GT-2160 x Above the Clouds White Pure Silver Branco
- `tenis-asics-gt-2160-x-gallery-dept-complexcon-cinza` — Tênis Asics GT-2160 x Gallery Dept. ComplexCon Cinza
- `tenis-asics-gt-2160-x-jjjound-white-branco` — Tênis Asics GT-2160 x JJJJound White Branco
- `tenis-asics-gt-2160-x-kith-marvel-villains-spider-man-venom-colorido` — Tênis Asics GT-2160 x Kith Marvel Villains Spider-Man/Venom Colorido