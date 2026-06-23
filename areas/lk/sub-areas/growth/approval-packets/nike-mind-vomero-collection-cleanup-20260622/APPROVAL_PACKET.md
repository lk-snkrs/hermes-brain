# Approval Packet — Nike Mind + Vomero collection cleanup — 2026-06-22

**Status:** preparado para decisão; nenhum write externo executado.  
**Gerado em:** 2026-06-22T15:22:19.749300+00:00  
**Modo:** read-only / approval packet.  
**values_printed:** false.

## 1. Direção do Lucas

Lucas confirmou continuar as melhorias após os ajustes da semana passada, com foco comercial em:

- Nike Mind 001;
- Nike Mind 002;
- Nike Vomero Premium;
- Onitsuka Tiger;
- 204L como benchmark/proteção.

Este packet cobre a próxima ação mais segura: **limpar/consolidar collections e schema**, sem reabrir PDPs já corrigidos antes do D+7.

## 2. Contexto — o que já foi feito

### Nike Mind 001 PDPs — não mexer agora salvo bug

Na semana passada foram aplicados e depois estabilizados:

- SEO title/meta nos PDPs `slide-nike-mind-001-light-smoke-grey-cinza` e `slide-nike-mind-001-pearl-pink-rosa`;
- nomenclatura corrigida para **Nike Mind Slide 001**;
- FAQ7 no `custom.faq`;
- limpeza de `body_html`;
- patch de parity no PDP: `custom.faq` alimenta FAQ visual + FAQPage JSON-LD; FAQ institucional só fallback;
- QA público 2026-06-20: HTTP 200, H1 único, 7 FAQs visíveis e 7 em schema nos 2 PDPs.

**Decisão operacional:** não reescrever esses PDPs antes do D+7 (~2026-06-26). Próxima melhoria deve ficar em collection/hub.

### Nike Mind 002

- Não está vazio: `Nike Mind 002 Black Hyper Crimson` já tem receipt aprovado de SEO/FAQ em 2026-06-17.
- A collection/hub deve organizar Mind 001 vs Mind 002 sem duplicar ou canibalizar PDPs.

### Vomero Premium PDP

- O PDP `tenis-nike-vomero-premium-white-bright-crimson-branco` entrou no Pacote B em 2026-06-19.
- Readback inicial oscilou por cache; não recomendamos novo write no PDP antes de revalidar impacto.

## 3. Evidência read-only atual — 2026-06-22

QA público via fetch/HTML:

| Página | HTTP | Title/meta | H1 | FAQPage JSON-LD | Conteúdo duplicado | Veredito |
|---|---:|---|---:|---:|---|---|
| `/collections/nike-mind-001` | 200 | `Nike Mind 001 e 002 Original no Brasil | LK` | 1 | **2** | 2× “Guia editorial LK”, 2× “Bloco citável LK” | precisa cleanup |
| `/pages/guia-nike-mind-001-002` | 200 | `Nike Mind 001 e 002: Guia LK de Escolha` | 1 | 1 | guia final também aparece com bloco extra no fim | revisar, mas menor risco que collection |
| `/collections/nike-vomero-premium` | 200 | `Nike Vomero Premium — Comprar | LK Sneakers` | 1 | **3 strings / 2 blocos funcionais** | 2× “Guia editorial LK”, 2× FAQ | precisa cleanup |

## 4. Diagnóstico

As melhorias anteriores parecem já publicadas, mas houve efeito colateral/legado: as collections renderizam **conteúdo editorial duplicado** e múltiplos blocos FAQ/schema.

Isso pode prejudicar:

- clareza para Google rich results/schema parsing;
- leitura de LLMs/AI Overviews;
- qualidade visual premium;
- foco de CTR, porque duas respostas competem na mesma página;
- manutenção futura, pois fica difícil saber qual bloco é fonte canônica.

## 5. Escopo proposto — Packet A

### Ação A1 — Collection Nike Mind 001/002

**URL:** `https://lksneakers.com.br/collections/nike-mind-001`  
**Handle:** `nike-mind-001`  
**Tipo:** collection produto-first; padrão 204L/collection, não página editorial longa.

Aplicar somente:

1. manter title/meta atuais, porque já estão bons e incluem `Brasil`;
2. consolidar descrição/guia para **um bloco canônico**;
3. manter apenas **um bloco citável LK**;
4. manter apenas **uma FAQ visual**;
5. garantir que o HTML público tenha **1 FAQPage JSON-LD**, não 2;
6. manter CTA discreto para o guia dedicado `/pages/guia-nike-mind-001-002`;
7. reforçar links internos para 001/002 sem alterar produtos, ordenação, preço ou estoque.

#### Conteúdo canônico sugerido para a collection

```html
<h3>Nike Mind 001 e 002: escolha por uso, não por hype.</h3>
<p>Nike Mind 001 e Nike Mind 002 são duas leituras da mesma proposta de conforto sensorial da Nike. O Mind 001 funciona como slide aberto, escultural e mais relaxado; o Mind 002 traduz a mesma linguagem em um sneaker fechado, mais urbano e fácil de usar fora de casa.</p>
<blockquote><p>Na curadoria LK, a escolha entre Nike Mind 001 e 002 começa pelo uso: 001 para descanso, styling e presença escultural; 002 para rotina urbana, viagem e formato sneaker.</p></blockquote>
<ul>
  <li><strong>Mind 001</strong> slide aberto, descanso, viagem e styling escultural.</li>
  <li><strong>Mind 002</strong> sneaker fechado, rua, rotina casual premium e proporção mais familiar.</li>
  <li><strong>Primeira compra</strong> tons neutros como Light Smoke Grey, Light Bone, Black Chrome, Sail e Khaki tendem a entrar melhor no guarda-roupa.</li>
  <li><strong>Mais presença</strong> Team Red, Solar Red, Geode Teal, Blackened Blue e Hyper Crimson funcionam quando o par é o ponto focal.</li>
  <li><strong>Ajuste</strong> a percepção muda entre construção aberta e fechada; a LK orienta modelo, tamanho e uso antes da decisão.</li>
</ul>
<h4>Qual a diferença entre Nike Mind 001 e Nike Mind 002?</h4>
<p>O Mind 001 é um slide aberto, mais próximo de descanso, recuperação e styling relaxado. O Mind 002 é um sneaker fechado, com leitura urbana e mais facilidade para rotina fora de casa.</p>
<h4>Nike Mind é tênis de corrida?</h4>
<p>Não. A proposta do Nike Mind é conforto sensorial e lifestyle. Para corrida ou treino técnico, a escolha deve ser feita em linhas de performance próprias.</p>
<h4>Qual Nike Mind é mais fácil de usar na rua?</h4>
<p>O Mind 002 tende a ser mais fácil para rua porque é fechado e se aproxima de um sneaker. O Mind 001 funciona melhor quando a intenção é slide, descanso ou uma peça mais escultural.</p>
<h4>O Nike Mind da LK Sneakers é original?</h4>
<p>Sim. A LK trabalha com curadoria de pares originais e atendimento humano para comparar modelo, cor, tamanho e melhor uso antes da decisão.</p>
<p><a href="/pages/guia-nike-mind-001-002">Abrir guia LK Nike Mind 001/002</a></p>
```

### Ação A2 — Guia Nike Mind 001/002

**URL:** `https://lksneakers.com.br/pages/guia-nike-mind-001-002`

Não reescrever o guia inteiro agora. Ação segura:

- remover o bloco final duplicado que repete “Guia editorial LK / Resposta curta / Como escolher / Abrir guia LK” dentro do próprio guia;
- preservar a estrutura editorial principal, tabela comparativa e FAQ;
- manter 1 FAQPage JSON-LD.

## 6. Escopo proposto — Packet B

### Collection Nike Vomero Premium

**URL:** `https://lksneakers.com.br/collections/nike-vomero-premium`  
**Handle:** `nike-vomero-premium`

Aplicar somente:

1. manter title/meta atuais se o Admin confirmar que são os campos mais recentes;
2. consolidar conteúdo pós-grid para **um guia curto**;
3. deixar **uma FAQ visual** e **um FAQPage JSON-LD**;
4. preservar conteúdo técnico factual: ZoomX, Air Zoom aparente, plataforma alta, diferença vs Vomero Plus/Vomero 5;
5. manter CTA para `/pages/nike-vomero-premium-guia`;
6. não mexer no PDP White Bright Crimson antes do D+7/readback.

#### Conteúdo canônico sugerido para a collection

```html
<h3>Nike Vomero Premium: ZoomX, Air Zoom aparente e máximo amortecimento</h3>
<p>O Nike Vomero Premium leva a família Vomero para uma leitura de super trainer: plataforma alta, espuma ZoomX, unidades Air Zoom aparentes e presença lifestyle premium. Na curadoria LK, o modelo faz sentido para quem busca conforto generoso, tecnologia visível e uma silhueta protagonista.</p>
<blockquote><p>Na curadoria LK, o Vomero Premium é o Vomero mais alto, tecnológico e expressivo: mais maximalista que o Vomero 5 e mais visual que o Vomero Plus.</p></blockquote>
<ul>
  <li><strong>Vomero Premium</strong> máximo amortecimento, plataforma alta e tecnologia visível.</li>
  <li><strong>Vomero Plus</strong> leitura mais direta para corrida diária macia.</li>
  <li><strong>Vomero 5</strong> retrô/lifestyle mais discreto.</li>
  <li><strong>Styling</strong> funciona melhor com bases limpas, peças amplas, denim reto, alfaiataria casual e elementos técnicos.</li>
</ul>
<h4>O que é o Nike Vomero Premium?</h4>
<p>É a versão mais maximalista da família Vomero, com foco em amortecimento alto, espuma ZoomX, unidades Air Zoom aparentes e uma plataforma de visual futurista.</p>
<h4>Vomero Premium serve para corrida ou é mais lifestyle?</h4>
<p>Ele nasce do universo running e funciona para conforto, treinos leves, recuperação e rotina. Na curadoria LK, o apelo principal é a combinação de tecnologia visível, conforto generoso e presença lifestyle premium.</p>
<h4>Qual a diferença entre Vomero Premium, Vomero Plus e Vomero 5?</h4>
<p>O Vomero 5 é mais retrô e lifestyle; o Vomero Plus é mais direto para corrida diária macia; o Vomero Premium é o mais alto, tecnológico e visualmente expressivo da família.</p>
<h4>O Nike Vomero Premium da LK é original?</h4>
<p>Sim. A LK trabalha com curadoria de pares originais e atendimento humano para orientar versão, cor e numeração antes da compra.</p>
<p><a href="/pages/nike-vomero-premium-guia">Abrir guia LK Nike Vomero Premium</a></p>
```

## 7. Fora do escopo / bloqueios

Não alterar:

- preço;
- estoque;
- disponibilidade;
- desconto;
- ordem de produtos;
- produtos da coleção;
- imagens;
- menu;
- checkout;
- GMC/feed;
- campanhas Google/Meta;
- Klaviyo/WhatsApp;
- PDPs Mind 001 já corrigidos;
- PDP Vomero White Bright Crimson antes do D+7;
- theme production fora do necessário para schema se a duplicação vier de theme.

Se a duplicação de `FAQPage` estiver no theme e não no body da collection/page, parar e abrir sub-packet de theme/dev preview antes de produção.

## 8. QA obrigatório pós-aplicação

Admin/readback:

- backup de `seo.title`, `seo.description`, `descriptionHtml`/body de cada objeto;
- mutation sem `userErrors`;
- readback dos campos alterados;
- confirmar que preço, estoque, produtos e ordenação não foram tocados.

Público:

- HTTP 200 nas 4 URLs envolvidas;
- H1 único;
- `/collections/nike-mind-001`: `FAQPage` count = 1; “Guia editorial LK” count ideal <= 1; “Bloco citável LK” count ideal <= 1;
- `/pages/guia-nike-mind-001-002`: `FAQPage` count = 1; sem bloco final auto-linkado para si mesmo;
- `/collections/nike-vomero-premium`: `FAQPage` count = 1; uma área de FAQ e um guia curto;
- sem `Liquid error`;
- sem promessa pública de prazo/disponibilidade/estoque.

## 9. Impacto esperado

| Frente | Impacto esperado | Métrica |
|---|---|---|
| Nike Mind 001/002 | melhor parsing Google/LLM e CTR do hub para queries `nike mind`, `nike mind 001`, `nike mind 002` | GSC CTR, cliques, posição, landing sessions |
| Vomero Premium | redução de ruído e reforço de snippet/citação | GSC CTR `vomero premium`, schema QA, sessões collection |
| PDPs já corrigidos | preservar aprendizado até D+7 | GSC/GA4/Shopify D+7 |

## 10. Risco

- **Baixo/médio** se for apenas collection/page body/SEO fields.
- **Médio** se exigir theme production para resolver duplicidade schema; nesse caso, fazer dev preview/sub-packet.
- Risco comercial baixo: não mexe em preço/estoque/produtos.
- Risco SEO controlado: consolidar duplicação tende a melhorar clareza, mas qualquer mudança em conteúdo público pode oscilar snippet.

## 11. Rollback

Antes de aplicar:

1. salvar backup JSON dos objetos Shopify alterados;
2. salvar HTML público antes;
3. aplicar apenas campos aprovados;
4. readback Admin;
5. QA público;
6. se QA falhar, restaurar backups dos campos alterados.

## 12. Aprovação sugerida

> Aprovo aplicar somente o cleanup de conteúdo/schema descrito no packet `nike-mind-vomero-collection-cleanup-20260622`, nas URLs `/collections/nike-mind-001`, `/pages/guia-nike-mind-001-002` e `/collections/nike-vomero-premium`, sem mexer em preço, estoque, disponibilidade, produtos, ordenação, desconto, GMC/feed, campanhas, Klaviyo/WhatsApp, checkout, PDPs Mind 001 já corrigidos ou theme production fora do escopo; se a duplicação de schema exigir theme, parar e trazer sub-packet/dev preview. Executar com backup, readback, QA público, rollback e revisão D+7/D+14.

