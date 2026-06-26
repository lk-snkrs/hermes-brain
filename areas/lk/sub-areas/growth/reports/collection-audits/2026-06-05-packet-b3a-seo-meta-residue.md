# Packet B3A — limpeza de resíduo SEO/meta após B3

Status: aguardando aprovação explícita para write em produção.

Origem: QA público do B3 mostrou 7 collections ainda com `Pronta entrega`/`Entrega SP` em meta description. Diagnóstico Admin confirmou que o resíduo está em `seo.description`, não no `descriptionHtml` aplicado no B3.

Escopo proposto: alterar somente `seo.description` das 7 collections abaixo, mantendo `seo.title` inalterado.

Fora do escopo: descriptionHtml, produto, preço, estoque, campo/mensagem `Sujeito a encomenda`, tags, metafields operacionais, theme, checkout, campanhas, GMC, Klaviyo.

Guardrail encomenda: nenhuma proposta contém `Sujeito a encomenda`; não tocar fonte operacional de encomenda.

## Propostas

### `adidas-gazelle`
- Title: manter `Adidas Gazelle Original | Todos Colorways | LK Sneakers`
- Meta atual: Adidas Gazelle originais: 32 colorways clássicos em 10x sem juros. Pronta entrega · Frete grátis +R$500 · Loja Jardins SP · 100% autêntico.
- Meta proposta: Adidas Gazelle original na curadoria LK: silhueta clássica, colorways desejadas, autenticidade verificada e atendimento humano para orientar tamanho e prazo.

### `jaqueta-streetwear`
- Title: manter `Jaquetas Streetwear Originais | Essentials, Nude | LK Sneakers`
- Meta atual: Jaquetas streetwear originais: Fear of God Essentials, Nude Project, Represent. 27 modelos em 10x sem juros · Pronta entrega · Frete grátis +R$500.
- Meta proposta: Jaquetas streetwear originais na curadoria LK: Essentials, Nude Project, Represent e peças premium com autenticidade verificada e atendimento humano.

### `aime-leon-dore-x-porsche`
- Title: manter `Aimé Leon Dore x Porsche | Collab Rara | LK Sneakers`
- Meta atual: Aimé Leon Dore x Porsche: 27 peças da collab mais desejada de 2026. Pronta entrega em 10x sem juros · Frete grátis · Autenticidade garantida.
- Meta proposta: Aimé Leon Dore x Porsche na curadoria LK: peças raras da collab, autenticidade verificada e atendimento humano para orientar tamanho e disponibilidade.

### `dane-se`
- Title: manter `Dane-se Original Brasil | Streetwear Nacional | LK Sneakers`
- Meta atual: Dane-se original no Brasil: streetwear nacional premium. 27 peças em 10x sem juros · Pronta entrega · Frete grátis +R$500 · Loja SP.
- Meta proposta: Dane-se original na curadoria LK: streetwear nacional premium, peças desejadas, autenticidade verificada e atendimento humano para orientar escolha e prazo.

### `nike-air-max`
- Title: manter `Nike Air Max Original | 26 Modelos | LK Sneakers`
- Meta atual: Nike Air Max originais: 26 modelos clássicos e modernos em 10x sem juros. Pronta entrega · Frete grátis +R$500 · Loja Jardins SP · 100% autêntico.
- Meta proposta: Nike Air Max original na curadoria LK: modelos clássicos e modernos, autenticidade verificada e atendimento humano para orientar tamanho e prazo.

### `adidas-gazelle-indoor`
- Title: manter `Adidas Gazelle Indoor Original | 23 Colorways | LK Sneakers`
- Meta atual: Adidas Gazelle Indoor originais: 23 colorways exclusivos em 10x sem juros. Pronta entrega SP · Frete grátis +R$500 · 100% autêntico.
- Meta proposta: Adidas Gazelle Indoor original na curadoria LK: silhueta baixa, colorways desejadas, autenticidade verificada e atendimento humano para orientar tamanho e prazo.

### `calcas-alo-yoga`
- Title: manter `Calças Alo Yoga Originais | Airlift, Accolade | LK Sneakers`
- Meta atual: Calças Alo Yoga originais: Airlift, Accolade, 7/8, todos os colorways. 20 modelos em 10x sem juros · Pronta entrega · Frete grátis +R$500.
- Meta proposta: Calças Alo Yoga originais na curadoria LK: Airlift, Accolade e modelos desejados, autenticidade verificada e atendimento humano para orientar tamanho e prazo.

## QA local
- Propostas limpas dos termos-alvo: sim
- Arquivo: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/drafts/collection-packet-b3a-seo-meta-residue-20260605/proposed-seo-meta-b3a.json`

Aprovação textual sugerida: **Aprovo B3A**