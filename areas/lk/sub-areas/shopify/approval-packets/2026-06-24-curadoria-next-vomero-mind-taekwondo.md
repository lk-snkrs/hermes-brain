# Approval packet — próximos upgrades Curadoria LK PDP (Vomero Premium + Nike Mind 002 + Adidas Taekwondo/CLOT)

- **Data:** 2026-06-24
- **Agente:** lk-shopify
- **Superfície:** Shopify theme / PDP `lk-variante`
- **Pedido Lucas:** fazer as frentes 1, 2 e 3; no item 3, fazer os dois caminhos: Nike Mind 002 e Adidas Taekwondo/CLOT.
- **Status:** read-only concluído; aguardando aprovação explícita para qualquer write DEV/Production.

## 1) QA final Alo — resultado

Fonte: `/opt/data/profiles/lk-shopify/workdirs/curadoria-alo-final-qa-20260624/20260624T154801Z_alo_all_public_qa.json`

| Grupo | Resultado |
|---|---|
| ALO Runner | 18/18 OK; nenhum `never_ok` |
| Alo Sunset | 9/9 OK; nenhum `never_ok` |
| Alo Recovery | 7/9 OK; nenhum `never_ok`, mas nem todos os rounds foram 100% |

Interpretação: **não há handle `never_ok`**. ALO Runner e Sunset estão estáveis; Recovery teve 7/9 OK, então monitorar cache/edge antes de qualquer repair.

## 2) Vomero Premium — gap real encontrado

Fonte: `/opt/data/profiles/lk-shopify/workdirs/curadoria-vomero-expansion-20260624/20260624T154920Z_vomero_audit.json`

- Ativos públicos auditados: **20**
- Sem Curadoria pública: **10**
- Recomendação: criar/expandir grupo `Vomero Premium` com estes 10 novos handles, provavelmente em split snippet próprio para não inflar o snippet gigante.

| Produto | Handle | Status |
|---|---|---|
| Tênis Nike Vomero Premium Hyper Pink Rosa | `tenis-nike-vomero-premium-hyper-pink-rosa` | sem Curadoria pública |
| Tênis Nike Vomero Premium Black Sapphire Rose Preto | `tenis-nike-vomero-premium-black-sapphire-rose-preto` | sem Curadoria pública |
| Tênis Nike Vomero Premium SP Black Mini Chrome Swoosh Preto | `tenis-nike-vomero-premium-sp-black-mini-chrome-swoosh-preto` | sem Curadoria pública |
| Tênis Nike Vomero Premium Realtree Camo Black Preto | `tenis-nike-vomero-premium-realtree-camo-black-preto` | sem Curadoria pública |
| Tênis Nike Vomero Premium White Lapis Total Orange Off White | `tenis-nike-vomero-premium-white-lapis-total-orange-off-white` | sem Curadoria pública |
| Tênis Nike Vomero Premium Volt Tint Sapphire Verde | `tenis-nike-vomero-premium-volt-tint-sapphire-verde` | sem Curadoria pública |
| Tênis Nike Vomero Premium x Melitta Baumeister Total Orange Laranja | `tenis-nike-vomero-premium-x-melitta-baumeister-total-orange-laranja` | sem Curadoria pública |
| Tênis Nike Vomero Premium x Renegade x Cinnamon Marrom | `tenis-nike-vomero-premium-x-renegade-x-cinnamon-marrom` | sem Curadoria pública |
| Tênis Nike Vomero Premium Barely Green Verde | `tenis-nike-vomero-premium-barely-green-verde` | sem Curadoria pública |
| Tênis Nike Vomero Premium Tangerine Tint Laranja | `tenis-nike-vomero-premium-tangerine-tint-laranja` | sem Curadoria pública |

## 3A) Nike Mind 002 — gap real encontrado

Fonte: `/opt/data/profiles/lk-shopify/workdirs/curadoria-mind-taekwondo-20260624/20260624T155018Z_audit.json`

- Ativos públicos: **7**
- Sem Curadoria pública: **7**
- Recomendação: grupo separado `top30-nike-mind-002`, sem misturar com Nike Mind 001.

| Produto | Handle | Status |
|---|---|---|
| Tênis Nike Mind 002 Black Hyper Crimson Preto | `tenis-nike-mind-002-black-hyper-crimson-preto` | sem Curadoria pública |
| Tênis Nike Mind 002 Light Smoke Grey Cinza | `tenis-nike-mind-002-light-smoke-grey-cinza` | sem Curadoria pública |
| Tênis Nike Mind 002 Light Khaki Bege | `tenis-nike-mind-002-light-khaki-bege` | sem Curadoria pública |
| Tênis Nike Mind 002 Light Violet Ore Roxo | `tenis-nike-mind-002-light-violet-ore-roxo` | sem Curadoria pública |
| Tênis Nike Mind 002 Thunder Blue Azul | `tenis-nike-mind-002-thunder-blue-azul` | sem Curadoria pública |
| Tênis Nike Mind 002 Sail Bege | `tenis-nike-mind-002-sail-bege` | sem Curadoria pública |
| Tênis Nike Mind 002 Grey Football Grey Cinza | `tenis-nike-mind-002-grey-football-grey-cinza` | sem Curadoria pública |

## 3B) Adidas Taekwondo / CLOT — gap real encontrado

Fonte: `/opt/data/profiles/lk-shopify/workdirs/curadoria-mind-taekwondo-20260624/20260624T155018Z_audit.json`

### CLOT / Caroline Hu

- Ativos públicos: **3**
- Sem Curadoria pública: **3**
- Recomendação: grupo separado `top30-adidas-taekwondo-clot`, porque collab/cápsula deve ficar separada do regular.

| Produto | Handle | Status |
|---|---|---|
| Tênis Adidas Taekwondo Caroline Hu x CLOT White Royal Branco | `tenis-adidas-taekwondo-caroline-hu-x-clot-white-royal-branco` | sem Curadoria pública |
| Tênis Adidas Taekwondo Caroline Hu x CLOT Pink Silver Rosa | `tenis-adidas-taekwondo-caroline-hu-x-clot-pink-silver-rosa` | sem Curadoria pública |
| Tênis Adidas Taekwondo Caroline Hu x CLOT Black Preto | `tenis-adidas-taekwondo-caroline-hu-x-clot-black-preto` | sem Curadoria pública |

### Taekwondo regular / Mei restantes

- Gaps públicos: **3**
- Recomendação: avaliar como segundo grupo separado ou anexar ao grupo Taekwondo existente somente se semanticamente coerente.

| Produto | Handle | Status |
|---|---|---|
| Tênis adidas Taekwondo Cloud White Branco | `tenis-adidas-taekwondo-cloud-white-branco` | sem Curadoria pública |
| Tênis adidas Taekwondo Core Black Preto | `tenis-adidas-taekwondo-core-black-preto` | sem Curadoria pública |
| Tênis Adidas Taekwondo Mei Ballet Clear Pink Gum Rosa | `sapatilha-onitsuka-tiger-wmns-taekwondo-mei-ballet-clear-pink-gum-camurca` | sem Curadoria pública |

## Ordem recomendada de execução

1. **Vomero Premium expansion** — maior impacto: 10 PDPs sem Curadoria.
2. **Nike Mind 002** — cluster fechado, 7 PDPs, sem misturar com Mind 001.
3. **Adidas Taekwondo CLOT** — collab limpa, 3 PDPs.
4. **Taekwondo regular/Mei leftovers** — tratar com cuidado para não misturar regular, Mei Ballet e CLOT indevidamente.

## Risco

- Todos são theme writes; DEV upload e Production merge exigem aprovação escopada.
- Production deve seguir GitHub PR/merge; sem Asset API direto em Production.
- Vomero tem volume maior; precisa cap de 5 cards por PDP e labels curtos.
- Nike Mind 002 não deve canibalizar/misturar com Nike Mind 001.
- Adidas Taekwondo deve separar collab CLOT/Caroline Hu de regular/Mei.

## Rollback padrão

- Remover render line(s) em `snippets/lk-variante-top30-visited-v2.liquid`.
- Remover split snippet(s) novos.
- Reverter PR/merge correspondente.
- Para DEV, restaurar backup criado antes do upload.

## Aprovação necessária

Para eu preparar/aplicar o próximo batch, aprovar um destes escopos:

- `Aprovo DEV Curadoria Vomero Premium Expansion`
- `Aprovo merge Production Curadoria Vomero Premium Expansion`
- `Aprovo DEV Curadoria Nike Mind 002`
- `Aprovo merge Production Curadoria Nike Mind 002`
- `Aprovo DEV Curadoria Adidas Taekwondo CLOT`
- `Aprovo merge Production Curadoria Adidas Taekwondo CLOT`

Também posso executar em lote se você aprovar explicitamente o batch completo:

- `Aprovo DEV Curadoria Batch Vomero Mind Taekwondo`
- `Aprovo merge Production Curadoria Batch Vomero Mind Taekwondo`

## Writes externos

Nenhum write externo executado neste packet. Apenas read-only, relatório e documentação local/Brain.
