# Report + Approval Packet — Revalidação 2026-06-17 e SEO PDP lote 4
Data: 2026-06-17  
Modo: read-only + preparação de pacote; nenhum write Shopify executado nesta rodada.  
Sistema: Shopify Admin GraphQL read-only + storefront público.  
values_printed=false
## 1. Revalidação do que foi publicado ontem
### Evidência — Admin/API
- PDPs revalidados: **30**
- Admin `seo.title` bate com alvo: **True**
- Admin `seo.description` bate com alvo: **True**
- Coleção Nike Vomero 5: SEO title/meta no Admin continuam batendo com o alvo aprovado.

### Evidência — storefront público
- PDPs com ao menos uma amostra pública batendo title + meta após retry lento: **30/30**
- Coleção Nike Vomero 5: marker/FAQPage/title/meta batendo em **3/3** tentativas lentas.
- Liquid errors detectados: **0** no retry lento; **0** na rodada inicial.
- Observação: a rodada inicial gerou HTTP 429 por volume de chamadas; o retry lento confirmou os handles que tinham ficado bloqueados.

### Interpretação
- Estado aplicado ontem permanece **correto no Admin/API**.
- Storefront público está **ok nas amostras de validação**; o ruído foi rate-limit 429, não evidência de erro Liquid ou rollback necessário.
- Nike Vomero 5 estabilizou no público nas tentativas lentas: title/meta e marker do FAQ/schema apareceram corretamente.

### Arquivos
- Revalidação principal: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/seo-pdp-fourth-scan-20260617/revalidation_yesterday_20260617.json`
- Retry público lento: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/seo-pdp-fourth-scan-20260617/revalidation_public_slow_retry_20260617.json`

## 2. SEO PDP — lote 4 preparado

### Critério
- Escaneei produtos ativos, excluindo os 30 PDPs já aplicados ontem.
- Produtos ativos escaneados: **700**
- Candidatos restantes com defeito objetivo de SEO: **435**
- Defeitos: `seo.title` vazio, `seo.description` vazio, title longo, description longa ou fragmento gerado/reticências.
- Lote 4 selecionado: **10 PDPs** com title/meta revisados manualmente.

### Preview do lote 4

1. `tenis-adidas-samba-og-crystal-linen-ivory-gum-branco`
   - URL: https://lksneakers.com.br/products/tenis-adidas-samba-og-crystal-linen-ivory-gum-branco
   - Defeito atual: seo_title_empty, seo_description_empty
   - Title proposto (50): `Adidas Samba OG Crystal Linen Branco | LK Sneakers`
   - Meta proposta (119): `Adidas Samba OG Crystal Linen original na LK Sneakers. Curadoria premium, loja física nos Jardins e atendimento humano.`

2. `tenis-nike-kobe-11-protro-mamba-day-dourado`
   - URL: https://lksneakers.com.br/products/tenis-nike-kobe-11-protro-mamba-day-dourado
   - Defeito atual: seo_title_empty, seo_description_empty
   - Title proposto (51): `Nike Kobe 11 Protro Mamba Day Dourado | LK Sneakers`
   - Meta proposta (119): `Nike Kobe 11 Protro Mamba Day original na LK Sneakers. Curadoria premium, loja física nos Jardins e atendimento humano.`

3. `tenis-nike-shox-tl-black-cave-stone-preto`
   - URL: https://lksneakers.com.br/products/tenis-nike-shox-tl-black-cave-stone-preto
   - Defeito atual: seo_title_empty, seo_description_empty
   - Title proposto (49): `Nike Shox TL Black Cave Stone Preto | LK Sneakers`
   - Meta proposta (119): `Nike Shox TL Black Cave Stone original na LK Sneakers. Curadoria premium, loja física nos Jardins e atendimento humano.`

4. `tenis-adidas-by-stella-mccartney-sportswear-x-trainers-brown-mauve-gum`
   - URL: https://lksneakers.com.br/products/tenis-adidas-by-stella-mccartney-sportswear-x-trainers-brown-mauve-gum
   - Defeito atual: seo_title_empty, seo_description_empty
   - Title proposto (52): `Adidas by Stella McCartney Brown Mauve | LK Sneakers`
   - Meta proposta (128): `Adidas by Stella McCartney Brown Mauve original na LK Sneakers. Curadoria premium, loja física nos Jardins e atendimento humano.`

5. `tenis-adidas-by-stella-mccartney-sportswear-x-trainers-bold-gold-amarelo`
   - URL: https://lksneakers.com.br/products/tenis-adidas-by-stella-mccartney-sportswear-x-trainers-bold-gold-amarelo
   - Defeito atual: seo_title_empty, seo_description_empty
   - Title proposto (50): `Adidas by Stella McCartney Bold Gold | LK Sneakers`
   - Meta proposta (126): `Adidas by Stella McCartney Bold Gold original na LK Sneakers. Curadoria premium, loja física nos Jardins e atendimento humano.`

6. `tenis-adidas-stella-mccartney-x-adidas-wmns-sportswear-x-trainers-core-black-preto`
   - URL: https://lksneakers.com.br/products/tenis-adidas-stella-mccartney-x-adidas-wmns-sportswear-x-trainers-core-black-preto
   - Defeito atual: seo_title_empty, seo_description_empty
   - Title proposto (51): `Adidas by Stella McCartney Core Black | LK Sneakers`
   - Meta proposta (127): `Adidas by Stella McCartney Core Black original na LK Sneakers. Curadoria premium, loja física nos Jardins e atendimento humano.`

7. `tenis-adidas-by-stella-mccartney-sportswear-x-trainers-cloud-white-ivory-branco`
   - URL: https://lksneakers.com.br/products/tenis-adidas-by-stella-mccartney-sportswear-x-trainers-cloud-white-ivory-branco
   - Defeito atual: seo_title_empty, seo_description_empty
   - Title proposto (52): `Adidas by Stella McCartney Cloud White | LK Sneakers`
   - Meta proposta (128): `Adidas by Stella McCartney Cloud White original na LK Sneakers. Curadoria premium, loja física nos Jardins e atendimento humano.`

8. `tenis-adidas-tokyo-mary-jane-sandy-pink-earth-strata-rosa`
   - URL: https://lksneakers.com.br/products/tenis-adidas-tokyo-mary-jane-sandy-pink-earth-strata-rosa
   - Defeito atual: seo_title_empty, seo_description_empty
   - Title proposto (52): `Adidas Tokyo Mary Jane Sandy Pink Rosa | LK Sneakers`
   - Meta proposta (123): `Adidas Tokyo Mary Jane Sandy Pink original na LK Sneakers. Curadoria premium, loja física nos Jardins e atendimento humano.`

9. `tenis-onitsuka-tiger-mexico-66-fringe-yellow-black-amarelo`
   - URL: https://lksneakers.com.br/products/tenis-onitsuka-tiger-mexico-66-fringe-yellow-black-amarelo
   - Defeito atual: seo_title_empty, seo_description_empty
   - Title proposto (58): `Onitsuka Tiger Mexico 66 Fringe Yellow Black | LK Sneakers`
   - Meta proposta (134): `Onitsuka Tiger Mexico 66 Fringe Yellow Black original na LK Sneakers. Curadoria premium, loja física nos Jardins e atendimento humano.`

10. `tenis-onitsuka-tiger-mexico-66-sabot-black-black-preto`
   - URL: https://lksneakers.com.br/products/tenis-onitsuka-tiger-mexico-66-sabot-black-black-preto
   - Defeito atual: seo_title_empty, seo_description_empty
   - Title proposto (50): `Onitsuka Tiger Mexico 66 Sabot Black | LK Sneakers`
   - Meta proposta (126): `Onitsuka Tiger Mexico 66 Sabot Black original na LK Sneakers. Curadoria premium, loja física nos Jardins e atendimento humano.`

### Risco
- Baixo: alteração proposta é limitada a campos SEO de Product.
- Não altera preço, estoque, disponibilidade, descrição de PDP, tags, coleções ou tema.
- Public HTML pode demorar/alternar por cache após eventual apply; Admin readback deve ser a fonte autoritativa imediata.

### Rollback planejado, se aprovado e aplicado
- Antes de qualquer write: snapshot dos 10 produtos.
- Rollback: restaurar somente `seo.title` e `seo.description` por handle a partir do snapshot.
- Verificação: Admin readback exato + QA público title/meta + ausência de `Liquid error`.

### Bloqueio / próxima decisão
Este pacote ainda **não foi aplicado**. Para aplicar, preciso de aprovação explícita do lote 4 de 10 PDPs acima.

## Arquivos do pacote
- Candidatos brutos: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/seo-pdp-fourth-scan-20260617/seo_pdp_fourth10_candidates.json`
- Candidatos revisados: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/shopify/reports/assets/seo-pdp-fourth-scan-20260617/seo_pdp_fourth10_candidates_reviewed.json`
