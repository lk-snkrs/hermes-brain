# Approval packet — Repair render público Curadoria Bestsellers 1–3

- **Data:** 2026-06-25
- **Perfil:** lk-shopify
- **Superfície:** Shopify theme / PDP `lk-variante`
- **Contexto:** após PR #90 mergeado e Shopify Production readback OK, o HTML público imediato continuou sem os markers novos do split snippet.
- **Status:** repair local preparado; **nenhum novo write externo executado neste packet**.

## Histórico verificado

- DEV upload OK: `areas/lk/sub-areas/shopify/receipts/2026-06-25-curadoria-bestsellers-1-3-dev-apply.md`
- Production merge OK: `areas/lk/sub-areas/shopify/receipts/2026-06-25-curadoria-bestsellers-1-3-production-merge.md`
- GitHub PR #90: `https://github.com/lk-snkrs/lk-new-theme/pull/90`
- Shopify Admin/Asset API Production readback: OK para:
  - `snippets/lk-variante-top30-visited-v2.liquid`
  - `snippets/lk-variante-bestsellers-1-3-20260624.liquid`

## Fresh public QA

Relatório:

`/opt/data/profiles/lk-shopify/workdirs/curadoria-bestsellers-1-3-20260624/repair/20260625T101545Z_all19_public_coverage.json`

Resultado dos 19 handles do batch:

- **13/19** já têm algum bloco `data-lk-variante` público por grupos antigos/existentes.
- **6/19** continuam sem Curadoria pública:
  - `tenis-onitsuka-tiger-mexico-66-brich-green-branco`
  - `tenis-onitsuka-tiger-mexico-66-gold-white-dourado`
  - `tenis-new-balance-9060-moonrock-linen-dark-artic-greycinza`
  - `tenis-adidas-samba-og-cream-white-core-black-bege`
  - `tenis-adidas-samba-og-core-black-wonder-white-preto`
  - `tenis-adidas-samba-og-off-white-cyber-metallic-branco`

## Interpretação

O problema não é ausência de source: o source/readback entrou.

O risco do repair original por split snippet é que, quando o lookup/cache do snippet novo estabilizar, ele pode criar duplicidade em PDPs que já têm blocos antigos, por exemplo:

- Sabot e SD já renderizam `top30-mexico66-sabot` / `top30-mexico66-sd`.
- parte de NB9060 já renderiza `top30-nb-9060` ou `top30-new-balance-9060-adult-breadth`.
- Samba Jane já renderiza `samba-jane`.
- parte de Samba OG já renderiza `top30-samba-og` ou `top30-adidas-samba-og-specials-20260608`.

Logo, o repair seguro deve focar **somente os 6 handles publicamente descobertos**, sem duplicar os 13 já cobertos.

## Patch local preparado

Workdir:

`/opt/data/profiles/lk-shopify/workdirs/curadoria-bestsellers-1-3-20260624/repair/`

Arquivos alvo locais:

1. `target_sections__lk-pdp.repair.liquid`
   - Adiciona 3 blocos inline de repair em `sections/lk-pdp.liquid`, logo após o render do `lk-variante-top30-visited-v2`.
   - Usa `lk_current_handles` para renderizar **apenas** nos handles descobertos sem bloco público.
2. `target_snippets__lk-variante-top30-visited-v2.repair.liquid`
   - Remove a render line do split snippet `lk-variante-bestsellers-1-3-20260624` para evitar duplicidade futura.

## Grupos de repair

### 1) Mexico 66 regular — 2 handles

Marker: `repair-mexico66-regular-bestsellers-20260625`

Renderiza apenas nos PDPs:

- `tenis-onitsuka-tiger-mexico-66-brich-green-branco`
- `tenis-onitsuka-tiger-mexico-66-gold-white-dourado`

Caveat: cada PDP renderiza 1 card, porque o grupo regular seguro tem 2 produtos.

### 2) NB9060 Moonrock — 1 handle descoberto

Marker: `repair-nb9060-moonrock-bestsellers-20260625`

Renderiza apenas no PDP:

- `tenis-new-balance-9060-moonrock-linen-dark-artic-greycinza`

Cards usados: Rose Sugar, Angora Sea Salt, Black Cat, Linen Burgundy.

### 3) Samba OG descobertos — 3 handles

Marker: `repair-samba-og-bestsellers-20260625`

Renderiza apenas nos PDPs:

- `tenis-adidas-samba-og-cream-white-core-black-bege`
- `tenis-adidas-samba-og-core-black-wonder-white-preto`
- `tenis-adidas-samba-og-off-white-cyber-metallic-branco`

Cards usados: Cream Black, Black Wonder, Red Leopard, Crochet Green, Cyber Metallic, excluindo o produto atual.

## Static QA local

Relatório:

`/opt/data/profiles/lk-shopify/workdirs/curadoria-bestsellers-1-3-20260624/repair/20260625T101708Z_repair_local_static.json`

Resultado:

- Patch local OK.
- `sections/lk-pdp.liquid`: +8423 bytes.
- `top30-visited-v2`: -72 bytes, removendo só o render do split snippet.
- 3 markers de repair presentes 1/1.
- Current handles são subconjunto dos cards de cada grupo.
- Handles únicos por grupo.
- Simulação de current-product exclusion OK.

## Risco

- É um theme write em Production e deve seguir GitHub PR/merge, não Asset API direto.
- Repair altera `sections/lk-pdp.liquid`, que é mais sensível que criar snippet novo, mas o bloco é isolado por `lk_current_handles` e só ativa nos 6 handles descobertos.
- Como é inline, evita o provável problema de lookup/cache do snippet novo.

## Rollback

- Reverter o PR do repair.
- Isso remove os 3 blocos inline e restaura a render line anterior se necessário conforme diff do PR.
- Confirmar Shopify readback e public QA após sync.

## Aprovação necessária

Para executar este repair em Production pelo fluxo correto:

`Aprovo merge repair Curadoria Bestsellers 1-3`

Execução prevista:

1. Criar PR GitHub com os 2 assets do repair.
2. Merge em `production`.
3. Aguardar Shopify sync.
4. Readback Admin/Asset API.
5. Public QA nos 6 handles descobertos + controles dos 13 já cobertos para garantir que não duplicou.
