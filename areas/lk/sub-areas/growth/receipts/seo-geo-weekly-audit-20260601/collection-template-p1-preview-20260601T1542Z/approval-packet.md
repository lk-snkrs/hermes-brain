# LK Sneakers — Collection Template P1 Payload Preview

Data UTC: 20260601T1542Z
Escopo: preview local/read-only para template Shopify de collection. Nenhum upload para Shopify foi feito.

## Veredito

O próximo ganho seguro está em `sections/lk-collection.liquid`, mas o corte possível sem mexer em apps obrigatórios ainda é moderado: cerca de **29.6 KB** de HTML decodificado por página de collection, convertendo CSS/JS inline do próprio template para assets cacheáveis.

O maior bloco de CSS da collection continua vindo de Variant King/StarApps no storefront público (~188 KB inline) e não deve ser removido sem mexer em app/admin.

## Evidência pública atual — collection `/collections/sale`

- HTML decodificado: 1,305,036 bytes
- Transferência medida: 125,576 bytes
- Inline scripts: 798,937 bytes
- Inline CSS: 323,545 bytes
- Maior style block público: Variant King/StarApps `app="vsk"` com ~188,112 bytes
- Style block do `lk-collection`: ~66,842 bytes
- Judge.me preloader: 0
- `lk-footer.css`: 1
- `lk-footer.js`: 1
- Liquid errors: 0

## Evidência do arquivo Shopify template

Arquivo local analisado:

`/opt/data/hermes_bruno_ingest/lk-new-theme/sections/lk-collection.liquid`

Métricas:

- Tamanho Liquid: 244,698 bytes
- Linhas: 3,186
- Style blocks: 5
- Style bytes no arquivo: 68,667
- Script blocks: 16
- Script bytes no arquivo: 39,383
- Render calls: 3
- Schema JSON-LD presente: sim

## Preview preparado localmente

Diretório:

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/receipts/seo-geo-weekly-audit-20260601/collection-template-p1-preview-20260601T1542Z/`

Arquivos candidatos:

- `sections.lk-collection.candidate.liquid`
- `assets.lk-collection-p1-extracted.css`
- `assets.lk-collection-p1-extracted.js`
- `candidate-meta.json`

## O que a candidate change faz

1. Mantém o primeiro CSS grande inline por segurança, porque ele contém Liquid conditional e pode ter risco de cascata se for movido inteiro.
2. Extrai CSS puro sem Liquid dos style blocks menores para `lk-collection-p1-extracted.css`.
3. Extrai JS puro sem Liquid, não-JSON-LD, para `lk-collection-p1-extracted.js` com `defer`.
4. Mantém Schema JSON-LD inline, como deve ser para SEO.
5. Não mexe em Variant King, Rivo, Simprosys, Judge.me ou configurações de app.

## Impacto estimado

- Liquid original: 244,698 bytes
- Liquid candidato: 215,906 bytes
- Redução no Liquid: 28,792 bytes
- CSS extraído: 3,280 bytes
- JS extraído: 26,468 bytes
- Redução esperada de HTML decodificado: ~29,600 bytes por collection page

Aplicando no `/collections/sale`, estimativa:

- Atual: 1,305,036 bytes
- Estimado após P1: ~1,275,436 bytes
- Delta estimado: ~-2.27% no HTML decodificado da collection

## Validação local da candidate

- Link para CSS candidato aparece 1 vez.
- Link para JS candidato aparece 1 vez.
- CSS extraído não contém Liquid.
- JS extraído não contém Liquid.
- Candidate não contém literal `Liquid error` / `Liquid syntax error`.
- JSON-LD permanece no Liquid.

## Risco

Baixo a médio.

Riscos específicos:

- JS extraído com `defer` pode rodar em momento diferente do script inline original. A maior parte está em IIFE com guards por DOM, mas precisa QA mobile.
- Interações de filter drawer, load-more, FAQ accordion e source/guide collages precisam teste visual.
- Como é collection template, qualquer erro afeta múltiplas collections.

Mitigação:

1. Subir primeiro no theme dev `155065450718` somente após aprovação.
2. Validar preview mobile em pelo menos:
   - `/collections/sale`
   - `/collections/sneakers`
   - `/collections/new-balance-204l` ou uma guide/source collection
3. Verificar DOM/console visual:
   - filtros abrem/fecham
   - load more funciona
   - FAQ accordion funciona
   - trust strip aparece correto
   - zero `Liquid error`
4. Só promover para production depois de aprovação separada.

## Rollback proposto

- Dev: re-upar o `sections/lk-collection.liquid` original e remover/ignorar os dois assets candidatos.
- Production: se aprovado futuramente, criar backup/readback antes do upload e rollback por reupload dos assets originais.

## Próxima decisão necessária

Para eu executar o preview no tema dev, preciso de aprovação explícita:

**“Aprovado subir P1 collection payload no tema dev 155065450718 para preview.”**

Sem essa frase, mantenho apenas o preview local/read-only.

## Não realizado

- Nenhum upload para Shopify.
- Nenhum write em theme dev ou production.
- Nenhuma alteração em produtos, preço, estoque, checkout, app, GMC, Klaviyo, Meta, WhatsApp ou e-mail.
