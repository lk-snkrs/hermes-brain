# LK Growth — Packet B GEO em dev theme (receipt)

Data: 2026-05-22T16:58:08Z

## Escopo aprovado

Lucas aprovou o Packet B para execução em **dev theme**: blocos GEO citáveis + FAQPage nas collections P1, sem publish em produção.

## Superfície alterada

- Store: LK Sneakers Shopify
- Tema alterado: `lk-new-theme/dev`
- Theme ID: `155065450718`
- Role: `unpublished`
- Asset: `sections/lk-collection.liquid`
- Produção: **não alterada**
- Tema production usado só para comparação/read-only: `155065417950`

## O que foi implementado

Bloco `lk-geo-p1` com:

- H2 orientado a pergunta: `O que saber antes de escolher ...?`
- Parágrafo citável por coleção, com 134–167 palavras.
- FAQ visível com 3 perguntas e respostas.
- `FAQPage` JSON-LD válido por coleção.
- Copy premium/comercial: curadoria, originalidade, loja física Jardins, atendimento humano e confirmação via chat quando necessário.

Collections cobertas:

- `onitsuka-tiger-todos-os-modelos`
- `onitsuka-tiger-mexico-66`
- `new-balance-204l`
- `air-jordan-travis-scott`
- `adidas-samba-jane`
- `lululemon`
- `nike-mind-001`
- Alias Liquid também contempla `nike-mind` quando o handle existir.

## Word count dos blocos citáveis

- `onitsuka-tiger-todos-os-modelos`: 134 palavras
- `onitsuka-tiger-mexico-66`: 134 palavras
- `new-balance-204l`: 134 palavras
- `air-jordan-travis-scott`: 139 palavras
- `adidas-samba-jane`: 143 palavras
- `lululemon`: 137 palavras
- `nike-mind-001`: 144 palavras

Todos dentro do alvo GEO de 134–167 palavras.

## Rollback

Snapshot local privado:

`/opt/data/hermes_bruno_ingest/local_sql/lk_theme_rollback_snapshots/lk-geo-p1-dev-theme-155065450718-20260522T165421Z/`

Arquivos:

- `sections__lk-collection.before.liquid`
- `sections__lk-collection.after.liquid`
- `sections__lk-collection.readback.liquid`
- `receipt.json`

Hashes verificados:

- Before SHA256: `2220f83866473ba390cdbac8ee2fb5f21e3565ffc08c9f6d5313c05b40ba85c6`
- After/readback SHA256: `61136fe92f7c6ce58daf787177144e0d3a243c3dfadb60eadb1454d52762f426`
- Production comparison SHA256: `bed43e646534356bfcf183b87ebc8906797404e7d391e8b5a02026f2692d790a`

## Verificação executada

### Admin API / readback

- `Packet B dev-theme preview 2026-05-22`: presente no dev theme.
- Mesmo marcador: ausente no production theme.
- Handles P1: todos presentes no asset readback.
- `FAQPage`: presente no asset.
- Termos proibidos no bloco novo (`pronta entrega`, `encomenda`, `estoque`): ausentes no asset do bloco/alteração.

Observação: a descrição antiga de algumas collections ainda contém linguagem operacional como `estoque` por conteúdo pré-existente. O Packet B novo não introduziu esses termos, mas a collection `new-balance-204l` segue com copy antiga a revisar em outro pacote.

### Browser preview / DOM

Preview inicial aberto para setar contexto do Shopify:

`https://lksneakers.com.br/?preview_theme_id=155065450718`

Página validada em browser:

`https://lksneakers.com.br/collections/new-balance-204l?preview_theme_id=155065450718&geo=20260522`

Evidência DOM:

- `.lk-geo-p1`: presente.
- Texto do bloco New Balance 204L: presente no body.
- `script[type="application/ld+json"]` contendo `FAQPage`: 1.
- JSON-LD parse: OK.

Validação via fetch no browser para todas as P1:

- 7/7 páginas retornaram `lk-geo-p1` + `FAQPage`.
- 7/7 JSON-LD parse OK.

### Visual

Screenshot/vision do preview confirmou:

- Bloco `Guia LK` abaixo da grade/listagem.
- Sem sobreposição com cards, carregar mais, FAQ anterior ou footer.
- Aparência premium/minimalista compatível: respiro, tipografia, linhas discretas, cores neutras.
- Barra do Shopify preview aparece como overlay normal de preview; não é regressão do tema.

Screenshot local:

`/opt/data/profiles/lk-growth/cache/screenshots/browser_screenshot_2f8bdc3439db4981ae47f013112f6163.png`

## Preview URLs para revisão

- New Balance 204L: `https://lksneakers.com.br/collections/new-balance-204l?preview_theme_id=155065450718&geo=20260522`
- Onitsuka todos: `https://lksneakers.com.br/collections/onitsuka-tiger-todos-os-modelos?preview_theme_id=155065450718&geo=20260522`
- Onitsuka Mexico 66: `https://lksneakers.com.br/collections/onitsuka-tiger-mexico-66?preview_theme_id=155065450718&geo=20260522`
- Air Jordan Travis Scott: `https://lksneakers.com.br/collections/air-jordan-travis-scott?preview_theme_id=155065450718&geo=20260522`
- Adidas Samba Jane: `https://lksneakers.com.br/collections/adidas-samba-jane?preview_theme_id=155065450718&geo=20260522`
- Lululemon: `https://lksneakers.com.br/collections/lululemon?preview_theme_id=155065450718&geo=20260522`
- Nike Mind 001: `https://lksneakers.com.br/collections/nike-mind-001?preview_theme_id=155065450718&geo=20260522`

## Próximos passos

1. Lucas revisar visual/copy nos previews.
2. Se aprovado, preparar pacote separado de publish para produção com novo snapshot do tema main e rollback.
3. Revisar copy antiga das descriptions das collections que ainda têm linguagem operacional (`estoque`, entrega etc.) antes de produção, se Lucas quiser limpar o conteúdo visível.
4. D+7: monitorar GSC/AI visibility/ChatGPT/Perplexity/Gemini após produção, não após dev theme.
