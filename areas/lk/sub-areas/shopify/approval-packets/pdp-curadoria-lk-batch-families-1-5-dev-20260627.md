# Approval packet — DEV batch Curadoria LK gaps famílias 1–5

- Data: 2026-06-27
- Agente/profile: lk-shopify
- Superfície: PDP `.lk-variante` / Curadoria LK
- Origem: monitoria read-only dos 100 primeiros best-selling públicos
- Pedido: Lucas pediu seguir do 1 ao 5 após a fila de prioridade
- Status: packet pronto; **sem write externo executado**
- Writes externos: 0
- Consulta direta de estoque: 0
- values_printed=false

## Escopo proposto

Criar/aplicar em DEV um batch pequeno para as famílias:

1. Onitsuka Mexico 66
2. New Balance 9060
3. Nike Vomero
4. New Balance 530
5. Adidas Samba

Regra do Lucas preservada: **Curadoria LK visível com até 5 cards**. Candidatos extras entram como pool/backup editorial, não como mais cards na tela.

## Contagem por família

| Família | missing real | source/public divergence | total para tratar |
|---|---:|---:|---:|
| Onitsuka Mexico 66 | 10 | 0 | 10 |
| New Balance 9060 | 7 | 2 | 9 |
| Nike Vomero | 4 | 0 | 4 |
| New Balance 530 | 3 | 1 | 4 |
| Adidas Samba | 14 | 4 | 18 |

## Detalhe por família

### Onitsuka Mexico 66

**Observação:** separar visualmente regular / SD / Sabot quando a amostra permitir; não misturar só para completar 5.

| rank | handle | status | título |
|---:|---|---|---|
| 32 | `tenis-onitsuka-tiger-mexico-66-sd-brich-peacoat-bege` | `missing_curadoria_candidate` | tenis-onitsuka-tiger-mexico-66-sd-brich-peacoat-bege |
| 37 | `tenis-onitsuka-tiger-mexico-66-sabot-birch-peacoat-bege` | `missing_curadoria_candidate` | tenis-onitsuka-tiger-mexico-66-sabot-birch-peacoat-bege |
| 46 | `tenis-onitsuka-tiger-mexico-66-brich-green-branco` | `missing_curadoria_candidate` | tenis-onitsuka-tiger-mexico-66-brich-green-branco |
| 49 | `tenis-onitsuka-tiger-mexico-66-black-and-white-preto` | `missing_curadoria_candidate` | tenis-onitsuka-tiger-mexico-66-black-and-white-preto |
| 53 | `tenis-onitsuka-tiger-mexico-66-white-blue-branco` | `missing_curadoria_candidate` | tenis-onitsuka-tiger-mexico-66-white-blue-branco |
| 55 | `tenis-onitsuka-tiger-mexico-66-chrome-silver-prata` | `missing_curadoria_candidate` | tenis-onitsuka-tiger-mexico-66-chrome-silver-prata |
| 65 | `tenis-onitsuka-tiger-mexico-66-sd-birch-silver-bege` | `missing_curadoria_candidate` | tenis-onitsuka-tiger-mexico-66-sd-birch-silver-bege |
| 72 | `tenis-onitsuka-tiger-mexico-66-birch-rust-orange-bege` | `missing_curadoria_candidate` | tenis-onitsuka-tiger-mexico-66-birch-rust-orange-bege |
| 79 | `tenis-onitsuka-tiger-mexico-66-kill-bill-slip-on-amarelo` | `missing_curadoria_candidate` | tenis-onitsuka-tiger-mexico-66-kill-bill-slip-on-amarelo |
| 91 | `tenis-onitsuka-tiger-mexico-66-sd-brich-green-bege` | `missing_curadoria_candidate` | tenis-onitsuka-tiger-mexico-66-sd-brich-green-bege |

**Pool DEV sugerido:**

1. `tenis-onitsuka-tiger-mexico-66-sd-brich-peacoat-bege` — label curto sugerido: `onitsuka-tiger-mexico-66-sd-brich-peacoat-bege`
2. `tenis-onitsuka-tiger-mexico-66-sabot-birch-peacoat-bege` — label curto sugerido: `onitsuka-tiger-mexico-66-sabot-birch-peacoat-beg`
3. `tenis-onitsuka-tiger-mexico-66-brich-green-branco` — label curto sugerido: `onitsuka-tiger-mexico-66-brich-green-branco`
4. `tenis-onitsuka-tiger-mexico-66-black-and-white-preto` — label curto sugerido: `onitsuka-tiger-mexico-66-black-and-white-preto`
5. `tenis-onitsuka-tiger-mexico-66-white-blue-branco` — label curto sugerido: `onitsuka-tiger-mexico-66-white-blue-branco`
- Backup editorial: 3 candidato(s) extras para substituição, sem aumentar cards visíveis.

### New Balance 9060

| rank | handle | status | título |
|---:|---|---|---|
| 41 | `tenis-new-balance-9060-sea-salt-raincloud-cinza` | `missing_curadoria_candidate` | tenis-new-balance-9060-sea-salt-raincloud-cinza |
| 42 | `tenis-new-balance-9060-sea-salt-concrete-branco` | `missing_curadoria_candidate` | tenis-new-balance-9060-sea-salt-concrete-branco |
| 45 | `tenis-new-balance-9060-bone-sparrow-marrom` | `missing_curadoria_candidate` | tenis-new-balance-9060-bone-sparrow-marrom |
| 56 | `tenis-new-balance-9060-rich-oak-marrom` | `missing_curadoria_candidate` | tenis-new-balance-9060-rich-oak-marrom |
| 82 | `tenis-new-balance-9060-rose-sugar-ice-wine-rosa` | `missing_curadoria_candidate` | tenis-new-balance-9060-rose-sugar-ice-wine-rosa |
| 97 | `tenis-new-balance-9060-moonrock-linen-dark-artic-greycinza` | `source_public_divergence` | tenis-new-balance-9060-moonrock-linen-dark-artic-greycinza |
| 98 | `tenis-new-balance-9060-moonrock-linen-dark-artic-greycinza-735245` | `source_public_divergence` | tenis-new-balance-9060-moonrock-linen-dark-artic-greycinza-735245 |
| 99 | `tenis-new-balance-9060-moonrock-linen-dark-artic-greycinza-454378` | `missing_curadoria_candidate` | tenis-new-balance-9060-moonrock-linen-dark-artic-greycinza-454378 |
| 100 | `tenis-new-balance-9060-angora-sea-salt-bege` | `missing_curadoria_candidate` | tenis-new-balance-9060-angora-sea-salt-bege |

**Pool DEV sugerido:**

1. `tenis-new-balance-9060-sea-salt-raincloud-cinza` — label curto sugerido: `new-balance-9060-sea-salt-raincloud-cinza`
2. `tenis-new-balance-9060-sea-salt-concrete-branco` — label curto sugerido: `new-balance-9060-sea-salt-concrete-branco`
3. `tenis-new-balance-9060-bone-sparrow-marrom` — label curto sugerido: `new-balance-9060-bone-sparrow-marrom`
4. `tenis-new-balance-9060-rich-oak-marrom` — label curto sugerido: `new-balance-9060-rich-oak-marrom`
5. `tenis-new-balance-9060-rose-sugar-ice-wine-rosa` — label curto sugerido: `new-balance-9060-rose-sugar-ice-wine-rosa`
- Backup editorial: 2 candidato(s) extras para substituição, sem aumentar cards visíveis.

**Repair/QA source-public:**

- `tenis-new-balance-9060-moonrock-linen-dark-artic-greycinza` — está em source/snippet mas sem marker público; checar render/condição antes de duplicar. Fonte: source detectado
- `tenis-new-balance-9060-moonrock-linen-dark-artic-greycinza-735245` — está em source/snippet mas sem marker público; checar render/condição antes de duplicar. Fonte: lk-variante-bestsellers-1-3-20260624.liquid

### Nike Vomero

| rank | handle | status | título |
|---:|---|---|---|
| 29 | `tenis-nike-vomero-premium-white-bright-crimson-branco` | `missing_curadoria_candidate` | tenis-nike-vomero-premium-white-bright-crimson-branco |
| 44 | `tenis-nike-vomero-premium-black-volt-preto` | `missing_curadoria_candidate` | tenis-nike-vomero-premium-black-volt-preto |
| 60 | `tenis-nike-vomero-premium-sail-coconut-milk-branco` | `missing_curadoria_candidate` | tenis-nike-vomero-premium-sail-coconut-milk-branco |
| 78 | `tenis-nike-vomero-premium-barely-volt-cinza` | `missing_curadoria_candidate` | tenis-nike-vomero-premium-barely-volt-cinza |

**Pool DEV sugerido:**

1. `tenis-nike-vomero-premium-white-bright-crimson-branco` — label curto sugerido: `nike-vomero-premium-white-bright-crimson-branco`
2. `tenis-nike-vomero-premium-black-volt-preto` — label curto sugerido: `nike-vomero-premium-black-volt-preto`
3. `tenis-nike-vomero-premium-sail-coconut-milk-branco` — label curto sugerido: `nike-vomero-premium-sail-coconut-milk-branco`
4. `tenis-nike-vomero-premium-barely-volt-cinza` — label curto sugerido: `nike-vomero-premium-barely-volt-cinza`

### New Balance 530

| rank | handle | status | título |
|---:|---|---|---|
| 34 | `new-balance-530-white-natural-indigo-1` | `missing_curadoria_candidate` | new-balance-530-white-natural-indigo-1 |
| 35 | `new-balance-530-white-natural-indigo-515064` | `source_public_divergence` | new-balance-530-white-natural-indigo-515064 |
| 36 | `new-balance-530-white-natural-indigo-424861` | `missing_curadoria_candidate` | new-balance-530-white-natural-indigo-424861 |
| 80 | `tenis-new-balance-530-silver-white-branco` | `missing_curadoria_candidate` | Tênis New Balance 530 Silver White Branco |

**Pool DEV sugerido:**

1. `new-balance-530-white-natural-indigo-1` — label curto sugerido: `new-balance-530-white-natural-indigo-1`
2. `new-balance-530-white-natural-indigo-424861` — label curto sugerido: `new-balance-530-white-natural-indigo-424861`
3. `tenis-new-balance-530-silver-white-branco` — label curto sugerido: `NB 530 Silver White Branco`

**Repair/QA source-public:**

- `new-balance-530-white-natural-indigo-515064` — está em source/snippet mas sem marker público; checar render/condição antes de duplicar. Fonte: lk-variante-top30-visited-v2.liquid, lk-variante-top30-visited.liquid

### Adidas Samba

**Observação:** Samba tem muitos duplicados/sufixos e divergências. Entrará como família 5 por último: primeiro repair/limpeza, depois batch DEV, para evitar rail redundante.

| rank | handle | status | título |
|---:|---|---|---|
| 50 | `tenis-adidas-samba-og-cream-white-core-black-bege` | `source_public_divergence` | tenis-adidas-samba-og-cream-white-core-black-bege |
| 51 | `tenis-adidas-samba-og-cream-white-core-black-bege-617365` | `source_public_divergence` | tenis-adidas-samba-og-cream-white-core-black-bege-617365 |
| 52 | `tenis-adidas-samba-og-cream-white-core-black-bege-162444` | `missing_curadoria_candidate` | tenis-adidas-samba-og-cream-white-core-black-bege-162444 |
| 61 | `tenis-adidas-samba-og-maroon-cream-white-vinho` | `missing_curadoria_candidate` | tenis-adidas-samba-og-maroon-cream-white-vinho |
| 62 | `tenis-adidas-samba-og-maroon-cream-white-vinho-969393` | `source_public_divergence` | tenis-adidas-samba-og-maroon-cream-white-vinho-969393 |
| 63 | `tenis-adidas-samba-og-maroon-cream-white-vinho-728065` | `missing_curadoria_candidate` | tenis-adidas-samba-og-maroon-cream-white-vinho-728065 |
| 69 | `tenis-adidas-samba-og-core-black-wonder-white-preto` | `missing_curadoria_candidate` | tenis-adidas-samba-og-core-black-wonder-white-preto |
| 70 | `tenis-adidas-samba-og-core-black-wonder-white-preto-396986` | `source_public_divergence` | tenis-adidas-samba-og-core-black-wonder-white-preto-396986 |
| 71 | `tenis-adidas-samba-og-core-black-wonder-white-preto-466107` | `missing_curadoria_candidate` | tenis-adidas-samba-og-core-black-wonder-white-preto-466107 |
| 73 | `tenis-adidas-samba-og-earth-strata-wonder-white-marrom` | `missing_curadoria_candidate` | tenis-adidas-samba-og-earth-strata-wonder-white-marrom |
| 83 | `tenis-adidas-samba-og-preloved-red-leopard-pack-marrom` | `missing_curadoria_candidate` | Tênis adidas Samba Og Preloved Red Leopard Pack Marrom |
| 84 | `tenis-adidas-samba-cardboard-marrom` | `missing_curadoria_candidate` | tenis-adidas-samba-cardboard-marrom |
| 86 | `tenis-adidas-samba-jane-scarlet-gum-vermelho` | `missing_curadoria_candidate` | Tênis Adidas Samba Jane 'Scarlet Gum' Vermelho |
| 87 | `tenis-adidas-samba-jane-white-black-branco` | `missing_curadoria_candidate` | tenis-adidas-samba-jane-white-black-branco |
| 88 | `tenis-adidas-samba-jane-black-white-gum-preto` | `missing_curadoria_candidate` | tenis-adidas-samba-jane-black-white-gum-preto |
| 90 | `tenis-adidas-samba-og-cream-white-cardboard-creme` | `missing_curadoria_candidate` | tenis-adidas-samba-og-cream-white-cardboard-creme |
| 95 | `tenis-adidas-samba-og-crochet-pack-orbit-green-verde` | `missing_curadoria_candidate` | tenis-adidas-samba-og-crochet-pack-orbit-green-verde |
| 96 | `tenis-adidas-samba-og-off-white-cyber-metallic-branco` | `missing_curadoria_candidate` | Tênis adidas Samba Og Off White Cyber Metallic Branco |

**Pool DEV sugerido:**

1. `tenis-adidas-samba-og-cream-white-core-black-bege-162444` — label curto sugerido: `adidas-samba-og-cream-white-core-black-bege-1624`
2. `tenis-adidas-samba-og-maroon-cream-white-vinho` — label curto sugerido: `adidas-samba-og-maroon-cream-white-vinho`
3. `tenis-adidas-samba-og-maroon-cream-white-vinho-728065` — label curto sugerido: `adidas-samba-og-maroon-cream-white-vinho-728065`
4. `tenis-adidas-samba-og-core-black-wonder-white-preto` — label curto sugerido: `adidas-samba-og-core-black-wonder-white-preto`
5. `tenis-adidas-samba-og-core-black-wonder-white-preto-466107` — label curto sugerido: `adidas-samba-og-core-black-wonder-white-preto-46`
- Backup editorial: 3 candidato(s) extras para substituição, sem aumentar cards visíveis.

**Repair/QA source-public:**

- `tenis-adidas-samba-og-cream-white-core-black-bege` — está em source/snippet mas sem marker público; checar render/condição antes de duplicar. Fonte: source detectado
- `tenis-adidas-samba-og-cream-white-core-black-bege-617365` — está em source/snippet mas sem marker público; checar render/condição antes de duplicar. Fonte: lk-variante-bestsellers-1-3-20260624.liquid
- `tenis-adidas-samba-og-maroon-cream-white-vinho-969393` — está em source/snippet mas sem marker público; checar render/condição antes de duplicar. Fonte: lk-variante-top30-visited-v2.liquid, lk-variante-top30-visited.liquid
- `tenis-adidas-samba-og-core-black-wonder-white-preto-396986` — está em source/snippet mas sem marker público; checar render/condição antes de duplicar. Fonte: lk-variante-bestsellers-1-3-20260624.liquid

## Implementação DEV proposta

- Criar snippet isolado `snippets/lk-variante-batch-gaps-20260627.liquid`.
- Inserir uma única render line em `sections/lk-pdp.liquid`.
- Preservar todos os snippets/grupos existentes.
- Para `source_public_divergence`, fazer repair/QA pontual; não duplicar grupo.
- Para cada PDP, renderizar no máximo 5 cards e excluir o produto atual.
- Usar labels curtos e imagens públicas válidas.
- Sem consulta/promessa de estoque; sem preço/produto/metafield/checkout.

## QA DEV obrigatório

- Preview DEV theme `155065450718`.
- Pelo menos 2 PDPs por família quando houver volume.
- HTTP `200`, Liquid errors `0`.
- Marker `.lk-variante` presente quando esperado.
- Produto atual ausente dos links da própria Curadoria.
- Máximo 5 cards visíveis.
- Links únicos e HTTP `200`.
- Mobile sem quebra visual.
- Production não alterado.

## Fora de escopo

- Production merge.
- Product Suggestions v3.
- Estoque/Tiny/disponibilidade.
- Produto, preço, checkout, GMC, Klaviyo, ads, WhatsApp/e-mail.

## Rollback DEV

- Remover render line do batch em `sections/lk-pdp.liquid`.
- Remover/ignorar `snippets/lk-variante-batch-gaps-20260627.liquid`.
- Restaurar snapshot DEV anterior se necessário.

## Aprovação necessária para aplicar em DEV

> Aprovo DEV batch Curadoria LK famílias 1 a 5, mantendo até 5 cards visíveis por PDP, sem Production merge.

## Reminder OS

- loop needed: yes
- owner: lk-shopify
- next action: aguardar aprovação DEV para aplicar o batch ou ajustar famílias/candidatos
- review trigger: resposta de Lucas aprovando DEV ou pedindo ajuste
- evidence: monitoria `pdp-curadoria-missing-monitor-100-20260627.md` + este packet
