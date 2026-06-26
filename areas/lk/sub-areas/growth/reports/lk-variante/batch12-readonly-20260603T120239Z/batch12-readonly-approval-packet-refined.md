# Batch 12 Curadoria LK — pacote read-only refinado

- Timestamp original UTC: `20260603T120239Z`
- Operação: read-only. Não houve upload/theme write/produto/preço/estoque/apps/campanha.
- Production snippet SHA12: `13133993edf5`
- Dev snippet SHA12: `13133993edf5`
- Produtos ativos/publicados lidos: `1807`
- Pedidos lidos janela 180d: `2759`
- Handles ativos já cobertos no source Production: `362`

## Veredito refinado
**Não recomendo aplicar Batch 12 no Dev agora** com o critério seguro atual. O único grupo que passava volume técnico era `Air Jordan 1 Low OG`, mas ele está bloqueado por decisão/hotfix anterior e não deve ser recriado automaticamente.

## Por que não aplicar agora
- `Air Jordan 1 Low OG`: apesar de ter 12 públicos/disponíveis, já foi removido/desativado por problema semântico/UX; a lista ainda mistura cápsula/collab como Nigel Sylvester. Recriar seria risco de repetir erro anterior.
- `Gazelle Indoor`: continua com sinal baixo e histórico de poluição por collabs/cápsulas.
- `Vomero 5`, `Air Jordan 3`, `Samba LT`, `Kayano 14`, `NB 550`, `Air Max 95`: têm menos de 5–6 descobertos públicos/disponíveis limpos, então não renderizam 5 alternativas sem forçar itens fracos.
- `Taekwondo Mei`: só 2 descobertos; um handle/título apresenta inconsistência semântica, então não vale expansão automática.

## Candidatos bloqueados principais
- `top30-air-jordan-1-low-og-regular` — Air Jordan 1 Low OG regular: bloqueado por decisão anterior: grupo Air Jordan 1 Low OG foi removido/desativado por problema semântico/UX; inclui cápsula/collab (ex. Nigel Sylvester) e não deve ser recriado sem revisão manual específica. | descobertos `14` | disponíveis checados `12` | units180d `18`
- `top30-adidas-gazelle-indoor-regular` — Adidas Gazelle Indoor: pool descoberto insuficiente/baixo para renderizar 5 sem poluir semântica | descobertos `4` | disponíveis checados `4` | units180d `6`
- `top30-nike-vomero-5-regular` — Nike Vomero 5: pool descoberto insuficiente/baixo para renderizar 5 sem poluir semântica | descobertos `4` | disponíveis checados `3` | units180d `2`
- `top30-air-jordan-3-regular` — Air Jordan 3: pool descoberto insuficiente/baixo para renderizar 5 sem poluir semântica | descobertos `4` | disponíveis checados `4` | units180d `1`
- `top30-adidas-samba-lt-regular` — Adidas Samba LT: pool descoberto insuficiente/baixo para renderizar 5 sem poluir semântica | descobertos `4` | disponíveis checados `4` | units180d `1`
- `top30-asics-gel-kayano-14-regular` — ASICS Gel-Kayano 14: pool descoberto insuficiente/baixo para renderizar 5 sem poluir semântica | descobertos `3` | disponíveis checados `3` | units180d `2`
- `top30-new-balance-550-regular` — New Balance 550: pool descoberto insuficiente/baixo para renderizar 5 sem poluir semântica | descobertos `3` | disponíveis checados `3` | units180d `1`
- `top30-nike-air-max-95-regular` — Nike Air Max 95: pool descoberto insuficiente/baixo para renderizar 5 sem poluir semântica | descobertos `3` | disponíveis checados `3` | units180d `0`
- `top30-adidas-taekwondo-mei-regular` — Adidas Taekwondo Mei: apenas 2 descobertos; um handle tem inconsistência semântica/nome (sapatilha-onitsuka-tiger... com título Adidas), não vale write automático. | descobertos `2` | disponíveis checados `2` | units180d `10`
- `top30-new-balance-1000-regular` — New Balance 1000: pool descoberto insuficiente/baixo para renderizar 5 sem poluir semântica | descobertos `2` | disponíveis checados `2` | units180d `2`
- `top30-adidas-campus-00s-regular` — Adidas Campus 00s: pool descoberto insuficiente/baixo para renderizar 5 sem poluir semântica | descobertos `1` | disponíveis checados `0` | units180d `0`
- `top30-nike-air-max-plus-regular` — Nike Air Max Plus: pool descoberto insuficiente/baixo para renderizar 5 sem poluir semântica | descobertos `1` | disponíveis checados `1` | units180d `0`

## Próxima decisão segura
Opção A — aguardar catálogo crescer e continuar varredura em outro ciclo.
Opção B — fazer revisão manual específica do Air Jordan 1 Low OG para separar regular/collab antes de qualquer Dev write.
Opção C — mudar o critério para permitir blocos com menos cobertura, mas isso aumenta risco de grupo fraco/incompleto; não recomendo agora.