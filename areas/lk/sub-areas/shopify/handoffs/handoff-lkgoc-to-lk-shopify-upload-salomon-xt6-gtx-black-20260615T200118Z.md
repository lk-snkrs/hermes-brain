## 2026-06-15 — LKGOC → LK Shopify — upload produto Salomon XT-6 GTX Black

- Pedido/evento: Lucas aprovou usar `LK-SHOPIFY-UPLOAD` para subir o 4º produto da coleção Salomon XT-6.
- Fonte viva consultada: LK Trends Brain; DataForSEO BR/US; KicksDB/GOAT; Shopify read-only; fonte oficial Salomon XT-6 GORE-TEX.
- Item/SKU/tamanho/cliente/pedido/fornecedor: Salomon XT-6 GORE-TEX Black/Ebony/Lunar Rock; SKU referência `L41663500`; tamanhos pendentes Lucas/LK Shopify; preço pendente Lucas/LK Shopify.
- Resultado verificado: KicksDB/GOAT encontrou `Salomon XT-6 GORE-TEX 'Black'`, slug `xt-6-gore-tex-black-l41663500`, colorway `Black/Ebony/Lunar Rock`, release 2022-10-19. Shopify duplicate check por `L41663500`, `Salomon XT-6 Gore-Tex Black Lunar Rock`, `XT-6 GTX Black Ebony Lunar Rock`: 0 resultados.
- Output/rascunho: approval packet abaixo.
- Writes externos: não. Nenhum produto foi criado porque preço/tamanhos ainda não foram aprovados e a skill exige preview antes do write.
- Aprovação: Lucas aprovou iniciar upload via LK-SHOPIFY-UPLOAD; aprovação final de criação draft com campos exatos ainda pendente.
- Snapshot/readback/receipt: este handoff; Shopify read-only duplicate check sem produtos encontrados.
- Risco/bloqueio: preço e numerações não informados; não consultar estoque direto; se envolver disponibilidade real, acionar `lk-stock`.
- Próximo passo: LK Shopify pedir/receber preço e tamanhos, então criar draft Shopify com campos abaixo, fazer readback e devolver link admin/preview.
- Onde ficou documentado: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/handoffs/handoff-lkgoc-to-lk-shopify-upload-salomon-xt6-gtx-black-20260615T200118Z.md`

# Approval Packet — LK Shopify Product Upload

## 1. Veredito curto

- Tipo de ação: criar produto Shopify em **draft**.
- Alvo exato: `Tênis Salomon XT-6 GORE-TEX Black Ebony Lunar Rock Preto`.
- Risco: A3 write externo Shopify se executado.
- Status recomendado: `draft`, não active.

## 2. Fonte viva e evidências

- GOAT/KicksDB: `xt-6-gore-tex-black-l41663500`; SKU `L41663500`; colorway `Black/Ebony/Lunar Rock`; release_date `2022-10-19T23:59:59.999Z`.
- GOAT URL: `https://www.goat.com/sneakers/xt-6-gore-tex-black-l41663500`.
- Oficial Salomon XT-6 GORE-TEX: confirma GORE-TEX, quickLACE™, textile lining, synthetic/textile upper, agileCHASSIS, OrthoLite®, Mud Contagrip®, protective toecap, sensiFIT™.
- DataForSEO: `salomon xt-6 gore tex` BR ~260/mês; US ~14.800/mês; intenção transacional.
- Shopify duplicate check: 0 produtos encontrados nas buscas por SKU/nome.
- Lacunas: preço, tamanhos, política de publicação/canais e eventual stock truth.

## 3. Snapshot antes

- Produto atual: não encontrado no Shopify por SKU/nome.
- Existing collection: `/collections/salomon-xt-6`.
- Backup/rollback: se draft for criado, rollback é deletar o product ID criado e imagens/variants associadas.

## 4. Alteração proposta

- Produto: novo product Shopify.
- Title: `Tênis Salomon XT-6 GORE-TEX Black Ebony Lunar Rock Preto`.
- Vendor: `Salomon`.
- Product type: `Tênis`.
- Shopify standard category: `gid://shopify/TaxonomyCategory/aa-8-8` — Apparel & Accessories > Shoes > Sneakers.
- Google/GMC product category: `Apparel & Accessories > Shoes` / mapear para Sneakers quando disponível.
- Status: `draft`.
- Tags: `Salomon`, `Salomon XT-6`, `XT-6`, `XT-6 GORE-TEX`, `GORE-TEX`, `Gorpcore`, `Tênis`, `Sneakers`, `encomenda`.
- Collection proposta: `salomon-xt-6`.
- Handle proposto: `tenis-salomon-xt-6-gore-tex-black-ebony-lunar-rock-preto`.
- SEO title: `Tênis Salomon XT-6 GORE-TEX Black Ebony Lunar Rock Preto | LK Sneakers`.
- Meta description: `Salomon XT-6 GORE-TEX Black/Ebony/Lunar Rock: sneaker técnico com membrana GORE-TEX, quickLACE™ e estética gorpcore premium na curadoria LK.`
- Body HTML:

```html
<h2>Salomon XT-6 GORE-TEX Black/Ebony/Lunar Rock</h2>
<p>O Salomon XT-6 nasceu como um ícone técnico de trail running e se consolidou fora das trilhas como uma das silhuetas mais fortes do movimento gorpcore: funcional, precisa e visualmente reconhecível. A versão XT-6 GORE-TEX preserva essa linguagem técnica, mas adiciona uma camada de proteção waterproof que aproxima o modelo de um uso urbano mais versátil, sem perder a leitura outdoor que tornou o XT-6 relevante na moda contemporânea.</p>
<p>Na curadoria da LK, o Black/Ebony/Lunar Rock entra como o contraponto escuro e mais utilitário da seleção Salomon XT-6. Enquanto as colorways claras trabalham uma estética mais suave e sofisticada, esta versão preta entrega presença, contraste e uma leitura mais técnica — ideal para quem quer um sneaker premium com construção de performance, mas fácil de combinar com alfaiataria casual, jeans amplo, cargos, nylon, moletom estruturado e sobreposições minimalistas.</p>
<p>A construção combina cabedal sintético e têxtil, membrana GORE-TEX, quickLACE™ para ajuste rápido, sensiFIT™ para encaixe firme, palmilha OrthoLite® moldada e solado Mud Contagrip® com tração marcada. O resultado é um tênis com aparência robusta, mas acabamento limpo, equilibrando estabilidade, conforto e apelo visual.</p>
<p>Por ser uma versão GTX em paleta Black/Ebony/Lunar Rock, o modelo funciona como peça de entrada para quem quer um Salomon XT-6 menos chamativo e mais atemporal. É o quarto produto ideal para fechar a coleção com uma opção preta, técnica e comercialmente forte.</p>
<ul>
  <li>Modelo: Salomon XT-6 GORE-TEX</li>
  <li>Colorway: Black/Ebony/Lunar Rock</li>
  <li>SKU referência: L41663500</li>
  <li>Membrana: GORE-TEX</li>
  <li>Sistema de amarração: quickLACE™</li>
  <li>Solado: Mud Contagrip®</li>
  <li>Categoria: sneaker técnico / gorpcore premium</li>
</ul>
```

## 5. Imagens GOAT — ordem aprovada sugerida

Regra aplicada: preservar ordem GOAT/KicksDB e filtrar sufixos `_02`, `_05`, `_07`.

1. https://image.goat.com/1000/attachments/product_template_pictures/images/080/054/344/original/1040052_00.png.png
2. https://image.goat.com/attachments/product_template_additional_pictures/images/080/054/345/medium/1040052_01.jpg.jpeg
3. https://image.goat.com/attachments/product_template_additional_pictures/images/080/054/341/medium/1040052_03.jpg.jpeg
4. https://image.goat.com/attachments/product_template_additional_pictures/images/080/054/340/medium/1040052_04.jpg.jpeg
5. https://image.goat.com/attachments/product_template_additional_pictures/images/080/054/337/medium/1040052_06.jpg.jpeg
6. https://image.goat.com/attachments/product_template_additional_pictures/images/080/054/336/medium/1040052_08.jpg.jpeg


Observação: tentativa de trocar `/medium/` por `/original/` retornou 404 para imagens adicionais; usar URLs GOAT originais válidas.

## 6. Variantes/SKU

Pendente Lucas/LK Shopify.

- SKU base referência: `L41663500`.
- Padrão proposto se não houver Tiny: `L41663500-<TAMANHO>` marcado como **SKU proposto**, não canonical Tiny.
- Tamanhos: pendentes.
- Preço: pendente.
- Inventory/stock: não consultar/prometer neste fluxo; se precisar, acionar `lk-stock`.

## 7. Padrão canônico aplicado

- Produto/upload: `lk-shopify-product-upload`.
- GOAT/photo/SKU/product upload pattern: aplicado.
- Description/curadoria quality gate: aplicado, 300+ palavras, story/contexto/curadoria/specs.
- Category gate: aplicado, category id incluído.
- Sales channel gate: pendente; default LK se Lucas aprovar publish depois: POS, Linktree, Pinterest, Online Store, Facebook & Instagram, Google & YouTube. Não ativar TikTok/Attentive.

## 8. Readback esperado após write aprovado

- Produto criado em `draft`.
- `category.id` não nulo e igual a `gid://shopify/TaxonomyCategory/aa-8-8`.
- Title, vendor, tags, handle, SEO fields conforme preview.
- Image count esperado: 6.
- Variants/SKUs conforme tamanhos aprovados.
- Nenhum inventory quantity alterado.

## 9. Rollback

- Deletar produto draft criado pelo product ID.
- Confirmar busca por handle/SKU retornando 0 ou status removido.
- Registrar receipt com product ID deletado.

## 10. O que NÃO está aprovado

- Publicar active.
- Definir preço sem Lucas/LK Shopify confirmar.
- Criar tamanhos sem Lucas/LK Shopify confirmar.
- Prometer disponibilidade/estoque.
- Tiny write.
- GMC feed write manual fora do product data no Shopify.
- Campanha/anúncio/Klaviyo/WhatsApp.

## 11. Texto de aprovação para Telegram

> Aprovo LK Shopify criar como DRAFT o produto `Tênis Salomon XT-6 GORE-TEX Black Ebony Lunar Rock Preto`, SKU base `L41663500`, com tag `encomenda`, categoria Shopify Sneakers `gid://shopify/TaxonomyCategory/aa-8-8`, coleção `salomon-xt-6`, 6 imagens GOAT filtradas, descrição/SEO acima, preço R$____ e tamanhos ____. Não aprovo active, estoque/Tiny, campanhas ou canais de venda ainda.

Reminder OS loop needed: yes
Owner: LK Shopify (`lk-shopify`)
Próxima ação concreta: receber preço+tamanhos e executar draft Shopify via `lk-shopify-product-upload`, com readback/link preview.
Gatilho de revisão: assim que Lucas informar preço e tamanhos/aprovar texto acima.
Evidência verificável: KicksDB/GOAT SKU `L41663500`; Shopify duplicate check 0; DataForSEO demanda BR/US.
Status e writes externos: nenhum write externo executado neste handoff.
