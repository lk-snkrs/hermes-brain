# Follow-up — Curadoria Bestsellers 1–3 / Samba OG Cream White

- **Data:** 2026-06-25
- **Perfil:** lk-shopify
- **Superfície:** Shopify theme / PDP Curadoria LK
- **Contexto:** após PR #91 repair, 5/6 handles descobertos passaram no public QA ou retry. O handle `tenis-adidas-samba-og-cream-white-core-black-bege` permaneceu sem bloco público.

## Fresh public QA após “seguir”

Relatório:

`/opt/data/profiles/lk-shopify/workdirs/curadoria-bestsellers-1-3-20260624/followup/20260625T103135Z_cream_followup_public.json`

Resultados:

| Handle | Resultado |
|---|---:|
| `tenis-adidas-samba-og-cream-white-core-black-bege` | 0/4 tries com marker |
| `tenis-adidas-samba-og-core-black-wonder-white-preto` | 3/4 tries com marker |
| `tenis-adidas-samba-og-off-white-cyber-metallic-branco` | 3/4 tries com marker |
| `tenis-adidas-samba-og-preloved-red-leopard-pack-marrom` | 4/4 tries com marker antigo |

## Admin/product read-only

Consulta Shopify Admin GraphQL comparou o handle problemático com controles.

- Produto problemático: ACTIVE, templateSuffix `null`, onlineStoreUrl público, handle correto.
- Controles também têm templateSuffix `null`.
- Diferença notada: o produto problemático não possui tag `Samba OG` explícita, mas o repair atual é por `product.handle`, não por tag, então isso não explica a ausência do marker.

## Interpretação

- Source/readback Production do PR #91 está correto.
- O mesmo repair renderiza em controles sob o mesmo grupo.
- O handle problemático retorna HTML público 200 mas continua sem `data-lk-variante`.
- Isso aponta para cache/render específico do produto/rota, ou para uma diferença de render pipeline que não aparece como `templateSuffix`.

## Recomendação

Não fazer novo write imediato só para forçar cache. Próximo passo seguro:

1. Rodar QA atrasado/monitor focado nesse handle.
2. Se continuar 0/N depois da janela, preparar um targeted packet com uma solução mais forte e explícita, evitando mexer nos 5 handles já OK.

## Writes externos

Nenhum nesta análise. Apenas read-only público/Admin e documentação.
