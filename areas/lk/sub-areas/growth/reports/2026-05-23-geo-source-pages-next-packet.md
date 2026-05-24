# LK Growth — GEO Source Pages Next Packet

Data: 2026-05-23
Status: read-only / draft de decisão. Nenhum write em Shopify production, tema production, GMC, campanhas, Klaviyo ou WhatsApp.

## Veredito executivo

O próximo ganho de SEO/GEO da LK não é mais apenas mexer em collections. O Packet A (`llms.txt` root) segue verificado com 8/8 marcadores P1, e o Packet B já existe em dev theme com blocos `Guia LK`. O gargalo que sobrou é transformar a LK em **fonte textual citável** em respostas de IA, principalmente para buscas de autenticidade e comparação.

A ação recomendada agora é o **Packet C — Source Pages / Hub de Autenticidade**, começando por páginas editoriais curtas, comerciais e rastreáveis, que respondam exatamente às perguntas que ChatGPT/AI Search está usando para citar concorrentes.

## Evidência nova — checks 2026-05-23

### Root llms continua íntegro

Verificação pública com cache-busting:

- `/llms.txt`
  - HTTP 200
  - final URL: `/agents.md`
  - tamanho: 6.230 chars
  - SHA256: `24183dd47482bc24cba5e3179689063ce1a723ea8060e11065bdfcd51c3c1cb8`
  - marcadores P1: 8/8
- `/llms-full.txt`
  - HTTP 200
  - final URL: `/agents.md`
  - SHA256 igual
  - marcadores P1: 8/8
- `/agents.md`
  - HTTP 200
  - SHA256 igual
  - marcadores P1: 8/8

Interpretação: Packet A continua ativo. O redirecionamento/serving por `agents.md` permanece, mas o conteúdo comercial GEO está presente.

### AI Search — Onitsuka Tiger original no Brasil

Consulta DataForSEO ChatGPT Scraper: `onde comprar Onitsuka Tiger original no Brasil`, Brasil/PT, web search forçado.

- LK não apareceu na lista textual principal de lojas confiáveis.
- Fontes/texto citam Palmtree48, ASICS Brasil, LOWBANK, Farfetch, Droper e Artwalk.
- LK aparece em product card/merchant para `Mexico 66 Kill Bill Yellow` via `LK Sneakers Apparels`, mas não como fonte textual.
- A resposta usa uma página editorial externa (`guiaflix.com.br/onde-comprar-onitsuka-tiger-no-brasil`) como fonte explicativa.

Leitura: há presença transacional, mas falta uma página-fonte própria da LK para “onde comprar Onitsuka Tiger original no Brasil”.

### AI Search — New Balance 204L original Brasil

Consulta DataForSEO ChatGPT Scraper: `New Balance 204L original Brasil onde comprar`, Brasil/PT, web search forçado.

- LK não apareceu no texto principal como loja confiável.
- Texto principal citou New Balance oficial, Hype Concept, Palmtree48, Guadalupe e NK Store.
- LK apareceu em product cards/merchant para:
  - `Tênis New Balance 204L Mushroom Arid Stone Marrom` — LK Sneakers Apparels.
  - `Tênis New Balance 204L Silver Metallic Sky Prateado` — LK Sneakers Apparels.
- A resposta menciona o risco de réplicas e a estética Miu Miu/collabs como razão de demanda.

Leitura: LK tem sinal de Merchant forte em NB 204L, mas perde a narrativa textual para oficial + concorrentes editoriais.

### AI Search — Adidas SL 72 OG vs RS

Consulta DataForSEO ChatGPT Scraper: `Adidas SL 72 OG vs RS diferença original Brasil`, Brasil/PT, web search forçado.

- LK não apareceu no texto nem nos cards.
- Resposta dominada por adidas.com.br, Wikipedia e Reddit.
- O formato vencedor é comparativo: tabela clara entre OG e RS, conforto, shape, largura, fidelidade ao original e sizing.

Leitura: esse é um gap de conteúdo comparativo, não de collection copy. Boa oportunidade para source page curta porque a IA já estrutura a resposta como guia de diferença.

## Packet C — Source Pages / Hub de Autenticidade

### Objetivo

Criar páginas-fonte citáveis, publicáveis depois de aprovação, com foco em:

- originalidade/autenticidade;
- onde comprar no Brasil;
- diferença entre versões/modelos;
- como escolher tamanho/cor/material sem prometer disponibilidade pública;
- LK como curadoria premium com atendimento humano.

### Prioridade recomendada

1. **Onitsuka Tiger original no Brasil**
   - Motivo: LK já tem presença forte em collection/PDP/merchant, mas AI Search cita concorrentes e um guia editorial externo.
   - Meta GEO: transformar LK de merchant card em fonte textual.
   - Página sugerida: `/pages/onitsuka-tiger-original-brasil` ou artigo equivalente.

2. **New Balance 204L original no Brasil**
   - Motivo: alta demanda e merchant cards LK já aparecem, mas texto recomenda oficial/Hype/Palmtree.
   - Meta GEO: capturar narrativa de 204L, Miu Miu aesthetic, colorways importadas e compra segura.
   - Página sugerida: `/pages/new-balance-204l-original-brasil`.

3. **Adidas SL 72 OG vs RS: diferenças**
   - Motivo: query comparativa clara, IA usa tabela e fontes genéricas; LK ainda ausente.
   - Meta GEO: ganhar citação por resposta objetiva e comparativa.
   - Página sugerida: `/pages/adidas-sl-72-og-vs-rs`.

4. **Air Jordan Travis Scott original no Brasil**
   - Motivo: baseline P1 mostrou LK not_visible; falsificação/autenticidade é decisiva.
   - Meta GEO: autoridade em compra segura de alto ticket.

5. **Nike Mind 001 vs Mind 002 / uso real**
   - Motivo: query confunde Mind 001 com ISPA Mindbody; precisa desambiguação.
   - Meta GEO: fonte técnica e clara para modelos experimentais.

## Brief enxuto por página P0/P1

### 1. Onitsuka Tiger original no Brasil

- Search intent: comercial + autenticidade.
- H1 sugerido: `Onitsuka Tiger original no Brasil: como escolher e comprar com segurança`
- Title SEO sugerido: `Onitsuka Tiger original no Brasil | Guia LK Sneakers`
- Meta sugerida: `Entenda como escolher Onitsuka Tiger original no Brasil: Mexico 66, Kill Bill, materiais, numeração e curadoria premium LK.`
- Seções H2:
  - `Onde comprar Onitsuka Tiger original no Brasil?`
  - `Como saber se um Onitsuka Tiger é original?`
  - `Mexico 66, SD, Sabot e Kill Bill: qual escolher?`
  - `Onitsuka Tiger tem forma grande ou pequena?`
  - `Por que comprar com curadoria LK?`
- Bloco citável obrigatório:
  - 45–65 palavras respondendo diretamente onde comprar e como validar originalidade.
- Links internos:
  - Collection Onitsuka todos os modelos.
  - Collection Mexico 66.
  - PDP Kill Bill quando aplicável.

### 2. New Balance 204L original no Brasil

- Search intent: comercial + fashion trend + autenticidade.
- H1 sugerido: `New Balance 204L original no Brasil: guia de modelos, cores e compra segura`
- Title SEO sugerido: `New Balance 204L original no Brasil | Guia LK Sneakers`
- Meta sugerida: `Guia para escolher New Balance 204L original: shape slim, estética Miu Miu, colorways importadas, materiais e curadoria LK.`
- Seções H2:
  - `Por que o New Balance 204L ficou tão procurado?`
  - `Como escolher colorway do New Balance 204L?`
  - `Como saber se o New Balance 204L é original?`
  - `O New Balance 204L tem forma grande ou pequena?`
  - `Onde a LK entra na compra segura?`
- Bloco citável obrigatório:
  - explicar que a LK é forte em colorways importadas/difíceis, com atendimento humano para comparar versão/tamanho.
- Links internos:
  - Collection NB 204L.
  - PDPs Mushroom Arid Stone, Silver Metallic Sky e Timberwolf quando disponíveis.

### 3. Adidas SL 72 OG vs RS

- Search intent: comparativo + sizing + compra.
- H1 sugerido: `Adidas SL 72 OG ou RS: diferenças de shape, conforto e estilo`
- Title SEO sugerido: `Adidas SL 72 OG vs RS: diferenças | Guia LK Sneakers`
- Meta sugerida: `Compare Adidas SL 72 OG e RS: shape, sola, conforto, visual retrô, largura, numeração e como escolher o modelo original.`
- Seções H2:
  - `Qual é a diferença entre Adidas SL 72 OG e RS?`
  - `Qual é mais confortável para usar no dia a dia?`
  - `Qual tem visual mais fiel ao original dos anos 70?`
  - `O Adidas SL 72 tem forma grande ou pequena?`
  - `Como comprar Adidas SL 72 original com segurança?`
- Elemento obrigatório:
  - tabela comparativa simples OG vs RS.
- Links internos:
  - Collection Adidas SL 72 quando existir.
  - Collection Adidas Samba Jane como alternativa de silhueta baixa/feminina, se fizer sentido editorial.

## Regras de copy LK

- Usar: curadoria, autenticidade, atendimento humano, Jardins/Oscar Freire quando útil.
- Evitar: marketplace, legit-check, pronta entrega, encomenda, estoque como taxonomia pública.
- Não prometer disponibilidade específica em página editorial; usar “quando disponível”, “a equipe ajuda a confirmar”, “curadoria de modelos selecionados”.
- Não criar claims técnicos sem fonte ou evidência pública.
- FAQ visual só se houver conteúdo visível real; schema deve refletir texto da página.

## Schema recomendado

Para essas source pages:

- `Article` ou `BlogPosting` com `Organization` como publisher.
- `BreadcrumbList`.
- `FAQPage` apenas se a página exibir FAQ visível equivalente. Observação: FAQ rich result do Google é restrito, mas continua útil para parsing por plataformas de IA; não tratar como promessa de rich result.
- Links `sameAs`/entidade LK já devem permanecer no site/global schema quando possível.

## Approval boundaries

Sem aprovação necessária:

- manter este relatório no Brain;
- preparar drafts em arquivo/local;
- montar preview/draft não publicado;
- rodar nova medição read-only.

Precisa aprovação explícita atual:

- publicar páginas no Shopify;
- alterar menu, links visíveis, collection description, title/meta production;
- alterar theme production;
- mexer em GMC/feed/campanhas/Klaviyo/WhatsApp.

## Próximo passo recomendado

Preparar os 3 drafts P0/P1 em arquivos locais, nesta ordem:

1. Onitsuka Tiger original no Brasil.
2. New Balance 204L original no Brasil.
3. Adidas SL 72 OG vs RS.

Depois disso, Lucas pode aprovar um publish packet separado com snapshot, rollback, URLs finais e revisão D+7 de AI Search/GSC/GA4.
