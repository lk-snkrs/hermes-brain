# Approval packet — Curadoria LK PDP — expandir AF1 Special/Collabs em DEV

## Status
- Data: `2026-06-06T14:13:42+00:00`.
- Tipo: preparação read-only + candidato local.
- Nenhum write externo executado neste passo.

## Baseline lido
- Tema Production fonte para baseline: `155065417950`.
- Asset: `snippets/lk-variante-top30-visited-v2.liquid`.
- Grupo existente: `top30-nike-air-force-1-low-special`.
- SHA256 baseline Production: `dc30f0059f131a3b326698edc3094eb02db4a949bbac91a5b3b900571353b2a8`.
- Arrays atuais: 29 grupos alinhados.
- Grupo AF1 Special atual: 7 handles / 7 labels / 7 imagens.

## Proposta
Expandir o grupo existente `top30-nike-air-force-1-low-special` com 11 produtos AF1 Low ainda não cobertos, mantendo a separação de colaborações/specials sem misturar com grupos generalistas.

### Novos itens propostos
1. `tenis-a-ma-maniere-x-air-force-1-low-triple-white-branco` — label: `A Ma Maniére White`
2. `tenis-nike-air-force-1-low-protro-kobe-bryant-mamba-mentality-amarelo` — label: `Kobe Mamba`
3. `tenis-nike-air-force-1-low-protro-kobe-bryant-siempre-hermanos-marrom` — label: `Kobe Hermanos`
4. `nike-air-force-1-low-shadow-light-soft-pink` — label: `Shadow Pink`
5. `tenis-nike-air-force-1-low-valentines-day-2025` — label: `Valentines 2025`
6. `nike-air-force-1-low-world-champ` — label: `World Champ`
7. `nike-air-force-1-low-world-champ-lakers` — label: `World Champ Lakers`
8. `tenis-nike-air-force-1-low-x-a-ma-maniere-while-you-were-sleeping-rose` — label: `A Ma Maniére Rose`
9. `tenis-nike-air-force-1-low-x-g-dragon-peaceminusone-para-noise-3-0-preto` — label: `G-Dragon Para-Noise`
10. `tenis-nike-air-force-1-low-x-nocta-certified-lover-boy-branco` — label: `NOCTA CLB`
11. `tenis-nike-air-force-1-low-x-supreme-wheat-marrom` — label: `Supreme Wheat`

## Validação read-only dos candidatos
Todos os 11 novos itens passaram em checks públicos nesta rodada:
- PDP HTML público: `200`.
- Endpoint `.js`: `200`.
- Imagem CDN: `200`.

Observação: `Supreme Wheat` e `NOCTA CLB` já tinham sido instáveis em rodada anterior; nesta rodada passaram nos 3 checks. Se Lucas quiser abordagem ultraconservadora, posso excluir esses 2 antes do DEV.

## QA estático do candidato local
Candidato local: `/opt/data/tmp/lk_curadoria_af1_special_expansion_candidate.liquid`.

- SHA256 candidato: `83d10c80e6fe674e01ed924cb136e6aaa742e0b59b2c7eafb3c396ca87e59a3f`.
- Marker count `top30-nike-air-force-1-low-special`: `1`.
- Arrays Curadoria: 29 grupos em todos os 5 arrays.
- Grupo AF1 Special pós-expansão: 18 handles / 18 labels / 18 imagens.
- Duplicados: `0`.
- URLs malformadas: não detectado.

## Impacto esperado
- O grupo AF1 Special/Collabs passa de 7 para 18 itens.
- Cada PDP continua excluindo o produto atual e renderizando até 5 cards no bloco.
- Não altera preço, estoque, produto, checkout, coleção, GMC, Klaviyo, ads, Tiny ou campanhas.

## Plano se aprovado para DEV
1. Backup/readback do asset no tema DEV `155065450718`.
2. Aplicar somente o patch escopado no asset `snippets/lk-variante-top30-visited-v2.liquid` do DEV.
3. Polling de readback até marker/arrays refletirem o candidato.
4. QA estático: arrays, duplicados, malformed URLs, contagem 18 no grupo, exclusão do produto atual.
5. QA visual via CDP em 3 PDPs:
   - A Ma Maniére White
   - Kobe Mamba
   - Supreme Wheat ou NOCTA CLB
6. Validar labels com `fontWeight: 300` no `span` e no `::after`.
7. Registrar receipt DEV.

## Rollback DEV
- Restaurar backup do snippet DEV antes do write.
- Como o patch é escopado ao grupo AF1 Special, rollback também pode remover os 11 novos handles/labels/imagens do grupo.

## Aprovação necessária
Para aplicar no DEV, Lucas precisa aprovar explicitamente:

`Aprovo DEV AF1 Special Expansion`
