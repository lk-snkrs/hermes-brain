# Approval packet — Curadoria LK PDP DEV: New Balance 9060 adult expansion

Data: 2026-06-08 06:35 BRT

## Escopo

- Pedido interpretado: `Seguir` após merge Production ASICS/Wales = continuar com **read-only next-batch scan** e preparar próximo packet.
- Superfície: Shopify theme / Curadoria LK PDP.
- Ação executada neste turno: **somente leitura/análise**.
- Shopify/DEV/Production write: **não executado**.

## Worker receipt compacto

- `demand_classification`: Curadoria LK PDP next-batch continuation.
- `canonical_playbook`: lk-shopify-variant-thumbnails / read-only next-batch continuation after Production merge.
- `workers_selected`: Parser/Readback, Curadoria Semântica, Validação de Imagens, QA Público básico.
- `workers_skipped`: delegate_task real indisponível/não necessário; execução consolidada no LK Shopify com lanes internas.
- `delegation_tool_used`: no.
- `reason_if_no_delegation`: tarefa curta o suficiente para scan local + API read-only; sem ferramenta delegate_task disponível neste runtime.
- `owner_agent_final_decision`: preparar DEV approval packet; bloquear qualquer write até aprovação explícita.

## Evidências read-only

### Manutenção pós-merge

Relatório forçado read-only gerado:

- Arquivo: `/opt/data/profiles/lk-shopify/cron/output/curadoria-lk-pdp-maintenance/curadoria-lk-pdp-maintenance-20260608T062643-0300.md`
- Semáforo: verde `50` · amarelo `11` · vermelho `0` · cinza `0`
- Handles públicos checados: `260`
- Fonte: `origin/production` + público `/products/<handle>.js`
- Writes: `0`

### Scan próximo lote

Artefatos locais:

- `/opt/data/tmp/lk_curadoria_next_batch_readonly_20260608.json`
- `/opt/data/tmp/lk_curadoria_next_batch_broad_readonly_20260608.json`

Leitura Production detectou snippets ativos:

- `lk-variante-cortez-speedcat-20260607`
- `lk-variante-onitsuka-versace-gazelle-collabs-20260607`
- `lk-variante-top30-visited-v2`
- `lk-variante-aj1-low-high-20260606`
- `lk-variante-asics-gt2160-walesbonner-20260608`

Cobertura Production parseada:

- Marcadores Production: `53`
- Handles já cobertos: `724`
- Catálogo Shopify lido: `2331` produtos

## Próximo lote recomendado

### Recomendação: expandir New Balance 9060 adulto via split snippet DEV

Motivo:

- Mesmo modelo/silhueta: New Balance 9060 adulto.
- Evita misturar infantil/Kids.
- Evita collab/cápsula ambígua.
- Existem `14` produtos adultos 9060 ainda descobertos pelo scan como não cobertos e com imagem admin limpa.
- Amostra validada: `10/10` com `/products/<handle>.js` público OK, `available=true`, sem placeholder.
- CDN image preflight: `10/10` retornaram HTTP `200` e `image/jpeg`.

Importante técnico:

- O main snippet ativo está muito próximo do limite Shopify 256 KB; último readback pós-merge tinha `259970` bytes.
- Portanto o caminho seguro para DEV é **split snippet**, não inflar o array principal:
  - criar snippet dedicado, por exemplo `snippets/lk-variante-nb9060-expansion-20260608.liquid`;
  - adicionar só uma linha `{% render ... %}` no `lk-variante-top30-visited-v2` do DEV;
  - manter Production inalterado.

## Preview proposto — handles e labels

Grupo técnico sugerido: `top30-new-balance-9060-expansion-20260608`

1. `tenis-new-balance-9060-slate-grey-arid-stone-cinza` — label: `Slate Grey Arid`
2. `tenis-new-balance-9060-olivine-verde` — label: `Olivine`
3. `tenis-new-balance-9060-sea-salt-new-spruce-dark-artic-grey-cinza` — label: `Sea Salt New Spruce`
4. `tenis-new-balance-9060-sparrow-flat-taupe-marrom` — label: `Sparrow Flat Taupe`
5. `tenis-new-balance-9060-slate-grey-cinza` — label: `Slate Grey`
6. `tenis-new-balance-9060-team-away-grey-cinza` — label: `Team Away Grey`
7. `tenis-new-balance-9060-reflection-raincloud-quarry-blue-bege` — label: `Reflection Raincloud`
8. `tenis-new-balance-9060-triple-black-preto` — label: `Triple Black`
9. `tenis-new-balance-9060-pink-granite-silver-metallic-silver-cinza` — label: `Pink Granite`
10. `tenis-new-balance-9060-nori-verde` — label: `Nori`

Expected render behavior:

- O bloco aparece somente nesses PDPs.
- Cada PDP exclui o produto atual.
- Com `10` handles, cada PDP tem até `9` alternativas; o layout deve exibir as 5 primeiras cards úteis conforme padrão atual.
- Copy preservada: `CURADORIA LK` / `Outras variações`.
- Tipografia preservada: título e labels light (`font-weight: 300`) via CSS existente.

## Candidatos não escolhidos agora

- `nike-dunk-low`: muito amplo; a amostra mistura Dunk regular, SB, Supreme, Off-White e collabs. Precisa split semântico antes.
- `air-jordan-1-low`: amplo e há histórico de blocker semântico em AJ1 Low/OG; não forçar sem review manual novo.
- `adidas-samba-og`: amplo e já coberto parcialmente; amostra mistura Pony Hair, Liberty, Cow Print, Leopard, Year of Snake. Precisa split por capsule/material antes.
- `air-jordan-4`: amostra mistura Retro regular, SB, Nigel Sylvester, Travis Scott, RM e Undefeated. Bom potencial, mas requer split manual por linha/cápsula antes.
- `new-balance-1000` / `740`: limpos, mas com densidade insuficiente (`2` e `1` válidos); no-go para Curadoria de 5 cards.

## Risco

- Baixo se aplicado primeiro em DEV/unpublished.
- Principal risco técnico: limite 256 KB do main snippet; mitigado por split snippet.
- Principal risco UX: se um PDP novo renderizar menos de 5 cards por regra de exclusão/ordem; mitigado por grupo com 10 handles.
- Public preview pode ser inconclusivo se Shopify remover `preview_theme_id`; nesse caso readback Asset API + static QA serão fonte primária.

## Rollback DEV

Se aprovado e aplicado em DEV, rollback seria:

1. Remover a render line do `lk-variante-top30-visited-v2` no DEV.
2. Remover/ignorar o snippet `lk-variante-nb9060-expansion-20260608.liquid` no DEV.
3. Verificar readback DEV e confirmar Production hash inalterado.

## Próxima decisão

Para executar **somente DEV/unpublished**, Lucas pode aprovar:

`Aprovo DEV Curadoria NB9060 expansion`

Isso não autoriza Production/merge. Production exigiria aprovação separada depois do readback/QA DEV.
