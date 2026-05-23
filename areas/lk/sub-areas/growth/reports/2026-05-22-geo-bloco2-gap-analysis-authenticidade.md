# LK Growth OS — Bloco 2 GEO Gap Analysis: Autenticidade e concorrência

Data: 2026-05-22 19:45 UTC
Status: read-only / sem writes externos nesta etapa.
Escopo original: comparar a página atual `https://lksneakers.com.br/pages/autenticidade` e ativos LK relacionados contra sinais públicos de Droper, Vox Sneakers e 90sneakers/players citados no baseline AI Search.

Correção estratégica de Lucas em 2026-05-22:
- LK deve ser posicionada como **boutique premium** / **loja especializada**, não como player de legit-check ou autenticação em vídeo.
- Originalidade/autenticidade não deve ser tratada como dúvida central da compra; na LK, confiança é premissa e o foco é seleção, experiência e atendimento humano.
- Droper é marketplace que conecta vendedores e compradores; não é concorrente direto de loja/boutique.
- Vox saiu do mercado e não deve ser usado como referência competitiva ativa.
- 90sneakers não é uma referência conhecida para Lucas.
- Concorrentes principais para próximos blocos: **Juicy Sneakers**, **Hype Concept** e **PalmTree48**.

## Veredito executivo

A página de Autenticidade LK avançou muito como hub visual e semântico, mas o gap competitivo agora é de **fonte canônica por intenção**, não de layout. Concorrentes e fontes citadas pela IA ganham quando respondem perguntas específicas como:

- como saber se um Air Jordan é original;
- onde comprar um modelo original no Brasil;
- como diferenciar versões, colorways, materiais e sizing;
- quais sinais de loja confiável reduzem risco de falsificação.

A LK já tem base melhor para marca premium e experiência humana, mas ainda precisa transformar isso em páginas-fonte específicas e blocos citáveis por modelo.

## Evidências coletadas

### LK atual — página Autenticidade

Fonte verificada:
- `https://lksneakers.com.br/pages/autenticidade`
- Browser live com cache-busting: `?_hermes_gap=20260522`

Pontos fortes:
- H1 claro: `Tênis original começa antes da compra.`
- Estrutura com H2s úteis:
  - `Como a LK verifica autenticidade?`
  - `Como comprar tênis original no Brasil com mais segurança?`
  - `Páginas-fonte para modelos e marcas desejadas.`
  - `Perguntas frequentes sobre autenticidade.`
- Há JSON-LD `Organization`, `WebPage` e `FAQPage` no DOM.
- O schema de Organization já usa descrição com `Sneaker boutique premium em Sao Paulo`.
- A página já aponta para guias relacionados: Air Jordan Travis Scott, New Balance 204L, Onitsuka Tiger Mexico 66 e Yeezy.

Gaps encontrados:
- O DOM público ainda contém `curadoria` 11 vezes e `boutique` 0 vezes no texto visível, apesar do schema já estar correto. Isso precisa de micro-hotfix aprovado em produção para alinhar linguagem com a correção de Lucas.
- O H2 `O que é avaliado antes de um produto entrar na curadoria?` deve virar `...entrar na seleção LK?`.
- O CTA `Curadoria é confiança antes de ser compra.` deve virar algo como `Autenticidade é confiança antes da compra.`
- O footer/newsletter global ainda usa `curadoria`; como é global, deve ser tratado em pacote separado.
- O hub ainda depende de links para guias que precisam existir como páginas-fonte reais.

### LK existente — blog `O Que é um Sneaker Original?`

Fonte verificada:
- `https://lksneakers.com.br/blogs/novidades/o-que-e-um-sneaker-original-como-identificar-falsificacoes`

Pontos fortes:
- Já aborda caixa, etiqueta, SKU, QR code, materiais, costuras e ofertas suspeitas.
- Tem data e formato de guia prático.
- É um ativo que pode virar link interno forte para o hub de Autenticidade.

Gap:
- Conteúdo é geral. Para AI Search, precisa ser conectado a guias específicos por modelo/brand family.
- Falta “ponte editorial” entre esse blog e a página institucional de Autenticidade.

### Droper

Fontes públicas encontradas:
- `https://droper.app` apareceu em busca como marketplace de sneakers/streetwear/colecionáveis com garantia de originalidade.
- Instagram/Reels e TikTok aparecem para `Legit Check` e autenticação.
- YouTube apareceu para `Como funciona a compra PRO?` com legit check.
- Reddit apareceu com pergunta de confiança: `Comprar na Droper é confiável?`

Força competitiva:
- Droper ocupa o território de `legit check`, marketplace e autenticação social/video.
- Tem presença em plataformas que AI Search tende a usar como validação externa: Instagram, TikTok, YouTube, Reddit.
- A promessa é direta: `100% original`, `100% seguro`, autenticação por especialistas.

Gaps que a LK pode explorar:
- Droper é mais marketplace/escala; LK pode ocupar `boutique premium + atendimento humano + compra assistida`.
- LK deve evitar brigar só em preço/volume e vencer em confiança editorial, loja física, processo humano e guias de decisão.
- Criar páginas-fonte com linguagem mais elegante e confiável, menos “marketplace”.

### Vox Sneakers

Fontes verificadas:
- `https://www.voxsneakers.com`
- `https://www.voxsneakers.com/blogs/journal/como-saber-se-o-air-jordan-e-original`

Força competitiva:
- Homepage comunica rápido: frete grátis, produtos autenticados, parcelamento, devolução gratuita e ajuda.
- Blog `Como saber se o Air Jordan é original?` responde uma intenção exata de compra/segurança.
- O artigo traz 7 dicas práticas: loja autêntica, costuras, cadarços, Jumpman, etiqueta/caixa, entressola e colorways conhecidas.
- O conteúdo menciona tempo de mercado, número de tênis vendidos e fundador, criando sinais de autoridade.
- Possui presença social multi-canal e reviews Loox.

Gaps que a LK pode explorar:
- O artigo da Vox é forte para Jordan, mas tem tom mais genérico e promocional.
- LK pode superar com guias mais precisos por modelo/collab: Travis Scott, Jordan 4, Yeezy, New Balance 204L, Adidas SL 72.
- Incluir loja física Jardins + atendimento humano como camada premium que Vox não destaca com a mesma força editorial.

### 90sneakers

Busca pública executada:
- `"90 sneakers" "tênis" "original" Brasil`
- `"90sneakers" "Air Jordan"`
- `"90sneakers" "sneakers" loja`

Resultado:
- Não encontrei evidência indexada robusta de domínio/guia próprio de 90sneakers nas buscas públicas usadas nesta rodada.
- Os resultados se misturaram com termos genéricos de `90s sneakers`, Nike Air Max 90 e redes sociais.

Leitura:
- Para este bloco, 90sneakers não é decision-grade como concorrente orgânico/GEO sem confirmar domínio exato.
- A ausência/ambiguidade é oportunidade para LK: páginas com nomenclatura clara e entity mapping podem capturar melhor o tema quando o concorrente não está bem estruturado.

## Matriz de gaps por intenção

### 1. `A LK vende produtos originais?`

Estado LK:
- Já tem FAQPage e resposta no hub.

Gap:
- Texto visível ainda usa `curadoria` como definição de negócio.

Ação recomendada:
- Micro-hotfix de copy: `boutique premium`, `loja especializada` e `seleção LK`.

Prioridade: P0 — alinhamento de posicionamento.

### 2. `Como saber se um Air Jordan é original?`

Concorrente forte:
- Vox, com artigo específico e 7 dicas.

Estado LK:
- Blog geral cobre autenticação; hub cita Air Jordan Travis Scott como guia relacionado, mas guia específico ainda precisa existir/publicar.

Gap:
- Falta página-fonte `Air Jordan Travis Scott original no Brasil` com checklist específico.

Ação recomendada:
- Criar guia com H2s sobre etiqueta, SKU, shape, materiais, colorways Travis Scott, embalagem e compra segura.

Prioridade: P1.

### 3. `Onde comprar New Balance 204L original no Brasil?`

Concorrentes/fontes do baseline:
- New Balance Brasil, Authentic Feet, Artwalk, Guadalupe, Farfetch, Droper/merchant card, Reddit.

Estado LK:
- Hub lista NB 204L como guia relacionado.

Gap:
- Falta guia de `New Balance 204L original`, com contexto Miu Miu, U204L, suede/mesh, colorways e sizing.

Ação recomendada:
- Criar página-fonte com FAQ: `O New Balance 204L tem a forma grande ou pequena?` sem claims não sustentados; orientar confirmação humana.

Prioridade: P1.

### 4. `Adidas SL 72 OG ou RS: qual a diferença?`

Concorrentes/fontes do baseline:
- adidas Brasil, Dafiti, Shop2gether, Chloro, Roger's, Reddit.

Estado LK:
- Sem fonte específica encontrada nesta rodada.

Gap:
- Falta comparativo técnico OG vs RS; AI Search premia diferenças de versão.

Ação recomendada:
- Criar guia comparativo com tabela editorial: shape, sola, conforto, visual retrô, proposta de uso e compra original.

Prioridade: P1.

### 5. `Nike Mind 001 original / ISPA Mindbody`

Concorrentes/fontes do baseline:
- Droper, Psico Company e páginas confundindo nomenclatura.

Estado LK:
- Sem fonte específica.

Gap:
- A consulta é ambígua; oportunidade de desambiguação.

Ação recomendada:
- Criar guia curto: `Nike Mind 001, ISPA Mindbody e diferenças de nomenclatura`.

Prioridade: P2.

### 6. `Lululemon original no Brasil`

Estado LK:
- LK ainda não aparece no texto AI Search segundo baseline.

Gap:
- Falta página-fonte de apparel premium/importado com autenticidade e modelagem.

Ação recomendada:
- Criar guia `Lululemon original no Brasil` com FAQ: `A peça tem a modelagem grande ou pequena?`.

Prioridade: P2.

## Pacotes recomendados

### Packet A — micro-hotfix de posicionamento da página Autenticidade

Objetivo:
- Remover definição técnica de LK como `curadoria` do conteúdo visível da página.

Trocas propostas:
- `A LK Sneakers é uma curadoria...` → `A LK Sneakers é uma boutique premium...`
- `curadoria humana` → `seleção humana` ou `atendimento humano` conforme contexto.
- `entrar na curadoria` → `entrar na seleção LK`.
- `Curadoria é confiança antes de ser compra.` → `Autenticidade é confiança antes da compra.`

Risco:
- Baixo, mas é write em Shopify/page production: exige aprovação atual.

### Packet B — páginas-fonte prioritárias

1. Air Jordan Travis Scott original no Brasil.
2. New Balance 204L original no Brasil.
3. Adidas SL 72 OG vs RS.
4. Onitsuka Tiger Mexico 66 original no Brasil.
5. Yeezy original no Brasil.

Cada página deve conter:
- um bloco citável de 134–167 palavras;
- H2 de intenção de compra;
- FAQ natural;
- FAQPage schema proposto;
- link para hub Autenticidade;
- link para collection/PDP quando existir;
- linguagem premium sem taxonomia pública de estoque/encomenda/pronta entrega.

### Packet C — reforço off-site / social signals

Aprendizado Droper/Vox:
- AI Search recompensa sinais de YouTube, TikTok, Instagram, Reddit/reviews e páginas de pergunta/resposta.

Ações futuras:
- Roteiro curto de vídeo `Como a LK verifica um par original`.
- Página/FAQ de loja física Jardins como sinal local.
- Aproveitar reviews/prova social com marcação e links internos.

## Cobertura dos 18 tópicos canônicos nesta etapa

1. GA4: não usado; este bloco é gap GEO/content, não decision-grade comercial completo.
2. GSC: não usado nesta coleta; usar no D+7 e priorização final.
3. GMC: não aplicável nesta etapa.
4. Shopify SEO: avaliado via título/H1/H2/body público da página.
5. Shopify CRO: layout visual já validado anteriormente; nesta etapa foco é conteúdo citável.
6. GEO/AI Search: tópico principal.
7. PageSpeed/CrUX/CWV: não aplicável nesta etapa.
8. Schema: FAQPage/WebPage/Organization detectados no DOM.
9. Reviews/prova social: gap identificado frente Vox/Loox e sinais sociais Droper.
10. Paid media: não usado.
11. Influencer/social demand: identificado como oportunidade de reforço off-site, sem execução.
12. Concorrência/SERP: Droper, Vox e 90sneakers/ambiguidade analisados por busca pública.
13. Google Business/local: oportunidade secundária com loja Jardins, não auditada neste bloco.
14. Klaviyo/CRM signals: não usado.
15. Catálogo/product data quality: relevante para guias por SKU/modelo, não auditado em feed.
16. Conteúdo/taxonomia comercial: principal saída deste bloco.
17. Mensuração/QA de eventos: não aplicável nesta etapa.
18. Impact review/experimentation: recomendado repetir AI Search + GSC/GA4 em D+7 após publicação.

## Status decision-grade

- Decision-grade para direcionamento editorial/GEO: sim, com base em AI Search baseline anterior + SERP/busca pública + inspeção DOM live.
- Não decision-grade para priorização de receita/conversão: ainda não, porque este bloco não cruzou GA4/GSC/Shopify revenue por página.

## Próximo passo recomendado

1. Aprovar micro-hotfix P0 da página Autenticidade para substituir os resíduos de `curadoria` no conteúdo visível.
2. Preparar draft completo do guia P1 `Air Jordan Travis Scott original no Brasil` como primeira página-fonte.
3. Em paralelo, preparar outline do guia `New Balance 204L original no Brasil`.
4. Depois de publicar guias, atualizar `llms.txt` para incluir o hub e páginas-fonte.
5. Repetir AI Search baseline em D+7 e cruzar com GSC/GA4 quando houver dados.
