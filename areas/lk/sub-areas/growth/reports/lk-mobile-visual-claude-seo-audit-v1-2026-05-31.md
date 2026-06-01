# LK Mobile/Visual + Claude SEO audit v1 — read-only

Data: 2026-05-31
Escopo: páginas públicas LK, user-agent mobile, análise read-only com DataForSEO OnPage/Lighthouse + lógica Claude SEO (`seo`, `seo-page`) + QA exploratório (`dogfood`).

## URLs analisadas

- Home: https://lksneakers.com.br/
- Coleção Samba: https://lksneakers.com.br/collections/samba
- Coleção Todos os Produtos: https://lksneakers.com.br/collections/ultimos-lancamentos-2
- PDP exemplo: https://lksneakers.com.br/products/nike-dunk-low-rose-whisper
- Busca Samba: https://lksneakers.com.br/search?q=samba
- Carrinho vazio: https://lksneakers.com.br/cart
- Robots: https://lksneakers.com.br/robots.txt
- LLMs: https://lksneakers.com.br/llms.txt

## Evidência resumida

### Performance / Lighthouse

- Home: Performance ~0.89, Accessibility ~0.92, Best Practices ~0.73, SEO ~0.92.
- Coleção Samba: Performance ~0.94, Accessibility ~0.95, Best Practices ~0.73, SEO ~0.92, CLS ~0.109.
- PDP exemplo: Performance ~0.96, Accessibility ~0.93, Best Practices ~0.73, SEO ~0.92, Agentic Browsing ~0.67.

Interpretação: performance pública está saudável. O gargalo não parece ser velocidade bruta; as oportunidades estão em semântica, consistência SEO/social, HTML/tema e experiência mobile acima da dobra.

### On-page / SEO básico

- Home:
  - Title: `LK Sneakers São Paulo | Tênis Originais no Jardins — Nike, Adidas, New Balance` — 78 caracteres segundo DataForSEO.
  - Description: 187 caracteres, longa para snippet.
  - H1 único presente.
  - OG title: `LK`, genérico demais.
  - 31 imagens; DataForSEO sinalizou imagem sem alt.
  - Schema: Organization/ShoeStore/ClothingStore + WebSite.

- Coleção Samba:
  - Title: `Samba - LK Sneakers`, curto e menos rico que o H1.
  - H1: `Adidas Samba`.
  - Description: 101 caracteres.
  - Conteúdo editorial e FAQ presentes.
  - Schema: BreadcrumbList + CollectionPage.
  - 42 imagens; alt ok na amostra.

- Coleção Todos os Produtos:
  - Title adequado em intenção genérica, 58 caracteres segundo DataForSEO.
  - H1: `Todos os Produtos`.
  - Description: 144 caracteres.
  - Links internos muito altos, compatível com coleção grande.

- PDP Nike Dunk Low Rose Whisper:
  - Title longo: 78 caracteres segundo DataForSEO.
  - H1 único presente.
  - Conteúdo forte: guia, fit, especificações, FAQ, reviews, confiança.
  - Schema: Product + BreadcrumbList + FAQPage.
  - Product schema inclui offers, price, availability, gtin, shippingDetails e returnPolicy.
  - Agentic Browsing Lighthouse menor (~0.67), candidato para revisão de markup/semântica.

- Busca `/search?q=samba`:
  - Meta robots: `noindex,follow` — correto para busca interna.
  - H1 presente: `Resultados para "samba"`.
  - Title/description usam padrão genérico/longos.

- Carrinho vazio:
  - Status 200.
  - Sem H1; principal mensagem é H2 `Seu carrinho está vazio`.
  - Robots.txt bloqueia `/cart`, correto.
  - Exibe “Os mais procurados”, boa recuperação de navegação.

### Técnico / crawl / GEO

- Robots.txt está presente e bloqueia áreas sensíveis: admin, cart, checkout, account, search etc.
- Produtos, coleções e blogs são permitidos.
- `llms.txt` existe, responde 200 e tem conteúdo extenso (~49 KB), incluindo browse, guias editoriais e páginas citáveis.
- Padrão recorrente no DataForSEO: erro de HTML parser “closing tag and currently open tag do not match” em várias páginas, provavelmente componente global/footer/newsletter.
- Páginas grandes: ~1.1 MB a ~1.4 MB HTML/DOM renderizado; coleções/PDP com mais de 1500 nós.

## Issues priorizados

### Alta prioridade

1. **OG/social da home inconsistente**
   - Evidência: `og:title` = `LK`, enquanto SEO title é muito mais informativo.
   - Impacto: compartilhamento social/WhatsApp e preview de marca ficam fracos.
   - Recomendação: alinhar OG title/description da home com posicionamento local/premium.
   - Exige write: Shopify/theme/metafield, depende da origem do OG.
   - Rollback: restaurar valores atuais do tema/configuração.

2. **Erro HTML global de tag de fechamento**
   - Evidência: DataForSEO acusou o mesmo erro em home, coleções, PDP, busca e carrinho.
   - Impacto: risco de comportamento inconsistente em mobile, acessibilidade, parsers SEO/LLM e manutenção do tema.
   - Recomendação: inspecionar footer/newsletter/componentes globais no tema, corrigir em dev theme primeiro.
   - Exige write: theme dev/prod; bloqueado sem aprovação.
   - Rollback: snapshot do arquivo Liquid/CSS antes da alteração.

3. **Carrinho vazio sem H1**
   - Evidência: `/cart` tem H2 `Seu carrinho está vazio`, sem H1.
   - Impacto: baixo para SEO por robots bloquear carrinho, mas médio para semântica/acessibilidade.
   - Recomendação: converter mensagem principal para H1 ou adicionar H1 invisível/acessível coerente.
   - Exige write: theme.
   - Rollback: restaurar seção original do carrinho.

### Média prioridade

4. **Titles longos em home/PDP e title curto na Samba**
   - Evidência: Home e PDP com 78 caracteres segundo DataForSEO; Samba com `Samba - LK Sneakers` apenas.
   - Impacto: snippets podem truncar; Samba perde chance de capturar “Adidas Samba original”.
   - Recomendação proposta:
     - Home: `LK Sneakers Jardins SP | Nike, Adidas e New Balance Originais`
     - Samba: `Adidas Samba Original | Samba OG, XLG e Collabs | LK Sneakers`
     - PDP: `Nike Dunk Low Rose Whisper Rosa Original | LK Sneakers`
   - Exige write: SEO fields/Shopify.
   - Rollback: restaurar titles atuais.

5. **Best Practices Lighthouse ~0.73 recorrente**
   - Evidência: home/coleção/PDP.
   - Impacto: não é gargalo comercial imediato, mas aponta oportunidades técnicas e de dependências/apps.
   - Recomendação: auditoria específica de recursos externos/apps antes de mexer em qualquer script.
   - Exige write: não no diagnóstico; qualquer remoção/configuração de app exige aprovação.

6. **CLS da coleção Samba em ~0.109**
   - Evidência: Lighthouse coleção Samba.
   - Impacto: acima do ideal <=0.1, borderline.
   - Recomendação: verificar elementos acima da dobra, product grid, filtros, banners e imagens sem dimensões fixas.
   - Exige write: possivelmente CSS/theme.

### Baixa prioridade

7. **Meta descriptions genéricas/longas em páginas utilitárias**
   - Evidência: busca e carrinho usam description genérica de loja.
   - Impacto: baixo porque busca/carrinho são noindex/bloqueados; mas melhora consistência.
   - Recomendação: só mexer se vier junto de pacote de SEO fields.

8. **Imagem sem alt na home**
   - Evidência: DataForSEO `no_image_alt` na home.
   - Impacto: baixo/médio em acessibilidade e image SEO.
   - Recomendação: identificar asset e adicionar alt descritivo, se for imagem editorial relevante.

## O que está bom

- Performance pública acima do esperado para Shopify com muitos apps.
- H1 único em home, coleções, PDP e busca.
- PDP exemplo tem conteúdo profundo, FAQ, fit, especificações, reviews e confiança.
- Product schema está bem completo, incluindo offer, GTIN, shipping e return policy.
- Robots.txt correto para bloquear busca/carrinho/checkout/admin.
- `llms.txt` existe e está forte para GEO/AI-readiness.
- Coleção Samba já segue padrão editorial/FAQ, boa base para replicar.

## Não decision-grade / limitações

- Auditoria não usou sessão autenticada Shopify nem dados GA4/GSC/Shopify conversion.
- Sem screenshot real de browser móvel nesta etapa; a evidência visual foi inferida por HTML/render/Lighthouse, não por captura manual.
- A priorização comercial ainda precisa de dados de tráfego, venda, conversão e GSC para escolher páginas definitivas.

## Próximas ações recomendadas

1. Abrir dev theme e fazer read-only diff dos componentes globais/footer/newsletter para localizar erro HTML.
2. Preparar approval packet para ajustes de baixo risco: OG home, titles principais, H1 do carrinho e alt faltante.
3. Rodar próxima frente: 20 PDPs prioritários por dados reais de Shopify/GA4/GSC.

## Guardrail

Nenhum write Shopify/theme/GMC/Klaviyo/ads foi executado. Qualquer alteração em theme, SEO field, collection, product, app ou feed exige aprovação explícita atual de Lucas.
