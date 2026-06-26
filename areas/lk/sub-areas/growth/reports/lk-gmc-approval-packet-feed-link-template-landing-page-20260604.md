# LK GMC Approval Packet — feed link template + landing page errors

Data: 2026-06-04 09:50 UTC  
Modo: read-only / approval packet  
Fonte principal: `reports/lk-merchant-center-feed-readonly-router-2026-05-11.json`  
Escopo: Google Merchant Center / feed / Simprosys / product data quality

## Veredito executivo

Merchant Center tem volume material de reprovação P1, concentrado em dois gargalos:

- `mhlsf_full_missing_valid_link_template`: 10.441 ocorrências; maior grupo com 10.399 itens reprovados em Shopping.
- `landing_page_error`: 4.270 ocorrências; grupo principal com 1.322 itens reprovados em Shopping, DisplayAds e SurfacesAcrossGoogle.

Recomendação: não fazer correção global às cegas. Aprovar uma investigação/correção por lote piloto, com preview antes de qualquer write, porque o risco central é contrato de feed/Simprosys e overwrite posterior.

## Fatos verificados

- Produtos/status lidos: 21.402.
- Itens P1/P2: 12.773.
- P1: 12.773.
- P2: 0.
- Produtos com issue: 12.773.
- Produtos com destino reprovado: 11.909.
- Cruzamentos com GSC: 4.
- Writes liberados agora: 0.
- Escopo de leitura: full catalog esperado até 30k linhas; não comparar diretamente com snapshots antigos limitados a 5k sem rotular mudança metodológica.

## Top issues

- `mhlsf_full_missing_valid_link_template`: 10.441.
- `landing_page_error`: 4.270.
- `missing_item_attribute_for_product_type`: 1.719.
- `price_updated`: 681.
- `strikethrough_price_updated`: 648.
- `local_stores_lack_inventory`: 54.
- `item_missing_required_attribute`: 36.
- `restricted_gtin`: 30.

## Pacote A — Link template / LIA feed

### Problema

Grande bloco de itens `local:pt:BR:LIA_*` aparece com `mhlsf_full_missing_valid_link_template`, reprovando Shopping.

### Evidência

- Grupo P1: 10.399 itens.
- Issue: `mhlsf_full_missing_valid_link_template`.
- Destino reprovado: Shopping.
- Exemplos de product IDs:
  - `local:pt:BR:LIA_LK-5524446-L`
  - `local:pt:BR:LIA_LK-5524446-XS`
  - `local:pt:BR:LIA_LK-5524446-M`
  - `local:pt:BR:LIA_JR7031`
  - `local:pt:BR:LIA_BASICSUF58-3`
- Exemplos de links retornados:
  - `https://lksneakers.com.br/products/accolade-straight-leg-sweatpant-charcoal-green?variant=48065003454686&country=BR`
  - `https://lksneakers.com.br/products/accolade-straight-leg-sweatpant-charcoal-green?variant=48065003389150&country=BR`

### Interpretação

Provável problema de configuração/contrato do feed local ou Merchant hosted local storefront/link template, não de SEO textual. Como envolve itens LIA/local, a correção pode estar em Simprosys/GMC feed config/template/supplemental feed, não necessariamente em PDP Shopify.

### Ação proposta — sem write ainda

1. Abrir diagnóstico de lote piloto com 20–50 ofertas `LIA_*`.
2. Mapear para cada oferta:
   - product ID GMC;
   - SKU/variant Shopify correspondente;
   - link atual;
   - campos de feed ligados a link/template;
   - origem do campo: Simprosys, feed principal, supplemental feed ou Merchant config.
3. Gerar preview de correção antes de qualquer mutation.
4. Só depois aprovar write escopado, se a origem e rollback estiverem claros.

### Impacto esperado

Alto. Se confirmado, destrava visibilidade Shopping de milhares de ofertas locais/LIA. Impacto comercial depende de elegibilidade real dos itens e campanhas/Surfaces, mas o volume é material.

### Esforço

Médio. Diagnóstico piloto é curto; correção massiva depende de onde mora o template.

### Risco

Alto se corrigir direto em massa:

- overwrite pela Simprosys;
- quebra de tracking/country/variant;
- inconsistência entre online feed e local inventory;
- alteração ampla em Shopping sem validação incremental.

### Rollback

- Backup/export do estado de campos afetados antes do write.
- Aplicar primeiro em lote pequeno.
- Reverter valores/template ao snapshot anterior se aumentar reprovação ou se Merchant acusar novo erro.
- Validar Merchant item status 24–72h depois.

### Aprovação necessária

Lucas precisa aprovar explicitamente qualquer:

- alteração de feed/Simprosys/GMC;
- supplemental feed write;
- Content API mutation;
- Shopify product/metafield write.

## Pacote B — Landing page error

### Problema

`landing_page_error` aparece em 4.270 ocorrências, com grupo P1 de 1.322 itens reprovados em DisplayAds, Shopping e SurfacesAcrossGoogle.

### Evidência

- Grupo P1: 1.322 itens.
- Destinos reprovados: DisplayAds, Shopping, SurfacesAcrossGoogle.
- Exemplos:
  - `online:pt:BR:2162246425358063315` — `https://lksneakers.com.br/products/tenis-nike-air-rift-triple-black-preto`
  - `online:pt:BR:JCQ007` — bolsa Jacquemus Le Bambino Long Flap Bag Leopard Print.
  - `online:pt:BR:JCQ005` — bolsa Jacquemus Le Bambino Long Shoulder Bag Black.
- Amostras adicionais em queue incluem páginas com UTM/tracking e variantes específicas.

### Interpretação

Pode ser um mix de:

- URL PDP retornando erro para Googlebot/Merchant;
- variante inexistente/indisponível no link;
- redirect/canonical/tracking conflitante;
- bloqueio intermitente, timeout ou parâmetro problemático;
- produto/handle alterado sem atualização de feed.

Não tratar como problema de copy. Primeiro precisa QA técnico de URLs e variantes.

### Ação proposta — sem write ainda

1. Rodar checker público de 50 URLs amostrais:
   - HTTP status;
   - redirect chain;
   - canonical;
   - noindex/robots;
   - variant param válido;
   - resposta sem depender de sessão/cookie;
   - diferença URL limpa vs URL com UTM/country/currency/stkn.
2. Separar causas:
   - URL 404/redirect quebrado;
   - variant inválida;
   - página OK publicamente, mas erro só no Merchant;
   - timeout/bloqueio/intermitência.
3. Gerar preview de correção por causa raiz.

### Impacto esperado

Alto/médio. Menos volume que link template, mas afeta três destinos e pode liberar Shopping/Surfaces para produtos online.

### Esforço

Baixo para diagnóstico; médio para correção dependendo da causa.

### Risco

Médio:

- mexer em links/handles pode afetar SEO/canonical;
- mexer em variantes pode afetar PDP e feed;
- correção isolada no feed pode ser sobrescrita pela Simprosys.

### Rollback

- Salvar lista de URLs/IDs antes de qualquer alteração.
- Aplicar em lote pequeno.
- Validar URL pública + Merchant status.
- Reverter campo de link/variant/handle se houver regressão.

### Aprovação necessária

Aprovação explícita antes de qualquer alteração em:

- link no feed;
- product handle/canonical/meta em Shopify;
- supplemental feed;
- reprocess/fetch se alterar estado operacional;
- campanhas.

## Pacote C — Product type / atributos faltantes

### Problema

`missing_item_attribute_for_product_type` aparece em 1.719 ocorrências. Há grupo de 614 itens sem destino reprovado, mas com issue relevante de qualidade.

### Evidência

- Grupo P1: 614 itens.
- Destino reprovado no grupo: nenhum informado.
- Exemplos:
  - Adidas Samba OG Silver Metallic Cracked Leather.
  - Onitsuka Tiger Mexico 66 Slip-On White Pure Silver.
  - Nike Zoom Vomero 5 Metallic Silver Blue Tint.

### Interpretação

É oportunidade de qualidade/estrutura de feed, mas menor prioridade que link template e landing page error porque parte do grupo ainda está aprovado nos destinos principais.

### Ação proposta

Criar supplemental feed/preview de product_type por taxonomia comercial, após resolver ou pelo menos diagnosticar os bloqueios que causam reprovação efetiva.

## Recomendação de priorização

1. **Aprovar diagnóstico piloto do Pacote A** — maior volume e reprovação Shopping.
2. **Em paralelo, rodar checker público do Pacote B** — baixo risco e rápido para separar URL quebrada de erro Merchant.
3. **Deixar Pacote C como backlog** — qualidade de feed, mas menor urgência comercial imediata.

## Pedido de aprovação para Lucas

Aprovar somente a próxima etapa read-only/preview:

- Diagnóstico piloto de 20–50 ofertas `LIA_*` com `mhlsf_full_missing_valid_link_template`.
- Checker público de 50 URLs com `landing_page_error`.
- Geração de um preview de correção, sem executar write.

Sem aprovação adicional, continuam bloqueados:

- Content API writes;
- supplemental feed writes;
- Simprosys/feed changes;
- Shopify writes;
- reprocess/fetch com efeito de estado;
- campanhas/envios externos.

## Cobertura dos 18 tópicos canônicos

- GA4: não usado; não necessário para health issue de feed neste packet.
- GSC: lido no router como cruzamento; 4 produtos cruzando prioridade GSC.
- GMC: fonte principal verificada.
- Shopify SEO: não alterado; possível impacto indireto apenas se handle/canonical for causa.
- Shopify CRO/theme: não aplicável nesta etapa.
- GEO/AI Search: não aplicável ao packet GMC.
- PageSpeed/CrUX/CWV: não aplicável salvo se landing page error virar timeout/performance.
- Schema: pendente; pode impactar Merchant, mas não é causa-raiz confirmada aqui.
- Reviews: não aplicável.
- Paid media: contexto; destinos Shopping/Display/Surfaces afetados, sem alteração de campanha.
- Influencer/social demand: não aplicável.
- Concorrência/SERP: não aplicável.
- Google Business/local: relevante para LIA/local; precisa mapear se store_code/GBP está envolvido no diagnóstico piloto.
- Klaviyo/CRM: não aplicável.
- Catálogo/product data quality: foco principal.
- Conteúdo/taxonomia comercial: relevante para product_type, backlog.
- Mensuração/QA de eventos: não aplicável nesta etapa; QA é de URL/feed.
- Impact review/experimentation: obrigatório 24–72h após qualquer write aprovado.

## Status

Approval packet pronto. Nenhuma ação externa executada.
