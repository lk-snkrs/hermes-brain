# Batch 12 Curadoria LK — pacote read-only

- Timestamp UTC: `20260603T120239Z`
- Operação: read-only. Não houve upload/theme write/produto/preço/estoque/apps/campanha.
- Production snippet SHA12: `13133993edf5`
- Dev snippet SHA12: `13133993edf5`
- Produtos ativos/publicados lidos: `1807`
- Pedidos lidos janela 180d: `2759`
- Handles ativos já cobertos no source Production: `362`

## Recomendação
### 1. `top30-air-jordan-1-low-og-regular` — Air Jordan 1 Low OG regular
- Tipo: `candidate_new_or_rebuild_dev`
- Motivo: mais de 5 handles públicos/disponíveis ainda descobertos
- Grupo já existe no source Production: `False`
- Produtos no grupo: `15`
- Descobertos: `14`
- Descobertos públicos/disponíveis checados: `12`
- Sinal 180d: `18` units / `18` orders / R$ `42999.82`
- Top descobertos:
  - `tenis-air-jordan-1-low-og-obsidian-unc-azul` — Tênis Nike Air Jordan 1 Low OG Obsidian UNC Azul — units `8` — public available `True`
  - `tenis-nike-air-jordan-1-low-og-olive-verde` — Tênis Nike Air Jordan 1 Low OG Olive Verde — units `4` — public available `True`
  - `tenis-air-jordan-1-low-og-x-nigel-sylvester-better-with-time-preto` — Tênis Nike Air Jordan 1 Low OG x Nigel Sylvester Better With Time Preto — units `1` — public available `True`
  - `tenis-air-jordan-1-low-og-rookie-of-year-marrom` — Tênis Nike Air Jordan 1 Low Og Rookie of Year Marrom — units `1` — public available `True`
  - `air-jordan-1-low-og-black-toe-2023` — Tênis Nike Air Jordan 1 Low OG Black Toe (2023) Vermelho — units `0` — public available `True`
  - `air-jordan-1-low-og-bleached-coral` — Tênis Nike Air Jordan 1 Low OG Bleached Coral Rosa — units `0` — public available `True`
  - `tenis-nike-air-jordan-1-low-og-chinese-new-year-2026-cinza` — Tênis Nike Air Jordan 1 Low OG Chinese New Year 2026 Cinza — units `0` — public available `True`
  - `air-jordan-1-low-og-ex-black-and-smoke-grey` — Tênis Nike Air Jordan 1 Low OG EX Black and Smoke Grey Cinza — units `0` — public available `True`


## Bloqueados / não recomendados agora
- `top30-adidas-gazelle-indoor-regular` — Adidas Gazelle Indoor: pool descoberto insuficiente/baixo para renderizar 5 sem poluir semântica | descobertos `4` | disponíveis checados `4` | units180d `6`
- `top30-nike-vomero-5-regular` — Nike Vomero 5: pool descoberto insuficiente/baixo para renderizar 5 sem poluir semântica | descobertos `4` | disponíveis checados `3` | units180d `2`
- `top30-air-jordan-3-regular` — Air Jordan 3: pool descoberto insuficiente/baixo para renderizar 5 sem poluir semântica | descobertos `4` | disponíveis checados `4` | units180d `1`
- `top30-adidas-samba-lt-regular` — Adidas Samba LT: pool descoberto insuficiente/baixo para renderizar 5 sem poluir semântica | descobertos `4` | disponíveis checados `4` | units180d `1`
- `top30-asics-gel-kayano-14-regular` — ASICS Gel-Kayano 14: pool descoberto insuficiente/baixo para renderizar 5 sem poluir semântica | descobertos `3` | disponíveis checados `3` | units180d `2`
- `top30-new-balance-550-regular` — New Balance 550: pool descoberto insuficiente/baixo para renderizar 5 sem poluir semântica | descobertos `3` | disponíveis checados `3` | units180d `1`
- `top30-nike-air-max-95-regular` — Nike Air Max 95: pool descoberto insuficiente/baixo para renderizar 5 sem poluir semântica | descobertos `3` | disponíveis checados `3` | units180d `0`
- `top30-adidas-taekwondo-mei-regular` — Adidas Taekwondo Mei: pool descoberto insuficiente/baixo para renderizar 5 sem poluir semântica | descobertos `2` | disponíveis checados `2` | units180d `10`
- `top30-new-balance-1000-regular` — New Balance 1000: pool descoberto insuficiente/baixo para renderizar 5 sem poluir semântica | descobertos `2` | disponíveis checados `2` | units180d `2`
- `top30-adidas-campus-00s-regular` — Adidas Campus 00s: pool descoberto insuficiente/baixo para renderizar 5 sem poluir semântica | descobertos `1` | disponíveis checados `0` | units180d `0`

## Próxima decisão
Se Lucas aprovar, aplicar somente no Dev o(s) grupo(s) recomendados acima, com snapshot, upload no Dev, readback, QA estático e Production unchanged. Production continua exigindo aprovação separada.