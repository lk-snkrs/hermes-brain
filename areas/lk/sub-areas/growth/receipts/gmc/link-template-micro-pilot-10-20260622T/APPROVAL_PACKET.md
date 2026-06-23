# Approval packet — GMC micro-piloto link_template LIA/local

- Criado UTC: 2026-06-22T17:21:57.363778+00:00
- Modo: read-only packet; writes externos até aqui: 0; values_printed=false.
- Fonte: `lk-gmc-product-data-ranking-review-2026-06-18`.
- Objetivo: validar menor surface correto para `mhlsf_full_missing_valid_link_template` sem mexer em páginas já otimizadas.

## Anti-retrabalho

- Não altera PDP/collection/theme/copy/SEO.
- Não consulta estoque.
- Amostra inicial exclui links das páginas em quarentena operacional quando possível.
- O problema é de feed/local offer `link_template`, não de conteúdo da página.

## Problema

- Issue: `mhlsf_full_missing_valid_link_template`.
- Escala: `11.267` offers locais/LIA.
- CSV de base: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/reports/gmc/lk-gmc-link-template-packet-2026-06-18.csv`.
- Fonte de feed detectada: `Simprosys Local Feed (Merchant API)` / `Simprosys Feed (Merchant API)`.

## Amostra proposta — 10 offers

| Offer | Título | Canal |
|---|---|---|
| `LIA_JI0324-6` | Tênis Adidas Gazelle Indoor Maroon Almost Yellow Marrom | `local` |
| `LIA_OXV-2785246-39` | Tênis Onitsuka Tiger x Versace Sakura Leather Loafers Brown Blue Marrom | `local` |
| `LIA_SLCRCVOW-1` | Camiseta Slyce Racquet Club Off White | `local` |
| `LIA_f99715` | Tênis Adidas Yeezy Boost 350 V2 Sesame Cinza | `local` |
| `LIA_ALD-2515934-L` | Camiseta Aimé Leon Dore Musician Graphic Preta | `local` |
| `LIA_w6289r_02-4` | Saia Alo Yoga Grand Slam Tennis Azul Marinho | `local` |
| `LIA_ST19-2` | Calça Saint Studio Plissada Tech Preto | `local` |
| `LIA_1183C529.200-1` | Tênis Onitsuka Tiger Tsunahiki Slip-On Birch/Indigo Navy Bege | `local` |
| `LIA_CT08561000-5` | Tênis Nike Dunk Low x Off-White Pine Green Verde | `local` |
| `LIA_w9681r-15` | Top Alo Yoga Airlift Line Up | `local` |

## Hipótese

O campo `link_template` dos local offers/LIA está vazio ou inválido, bloqueando surface local/Shopping. O ajuste deve acontecer no **surface dono** — provável Simprosys Local Feed/configuração de local inventory — para não ser sobrescrito no próximo sync.

## Plano de micro-piloto

1. Snapshot read-only dos 10 offers no Merchant.
2. Identificar se o write correto é:
   - configuração Simprosys Local Feed; ou
   - Merchant/ProductInput local offer field; ou
   - supplemental/local inventory feed.
3. Aplicar em 10 offers somente se o surface dono for confirmado.
4. Sem `fetchNow`/reprocessamento em massa sem nova aprovação.
5. Readback após sync/reprocess controlado.
6. Se funcionar, escalar packet para lote maior.

## Rollback

- Restaurar/remover `link_template` no mesmo surface usado no piloto.
- Readback Merchant por offer.
- Registrar receipt por offer, HTTP status e antes/depois.

## Risco

- Alto se aplicado fora do surface dono, pois Simprosys pode sobrescrever.
- Médio por mexer em Merchant/local feed, mesmo sem alterar PDP.
- Sem impacto direto em preço/estoque/copy se restrito a `link_template`.

## Aprovação necessária

Qualquer GMC/feed/ProductInput/dataSource/Simprosys write exige aprovação explícita atual.

Frase segura:

> aprovado GMC micro-piloto link_template 10 offers readback e rollback
