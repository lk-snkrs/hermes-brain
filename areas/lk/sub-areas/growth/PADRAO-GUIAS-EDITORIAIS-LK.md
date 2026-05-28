# Padrão LK — Guias editoriais, source pages e páginas de coleção

Este documento define o padrão obrigatório para qualquer guia editorial, source page, guia linkado em coleção ou página de apoio SEO/GEO da LK Sneakers.

## Regra central

O padrão visual e editorial canônico é o guia **Nike x Jacquemus Moon Shoe**:

- URL pública de referência: `https://lksneakers.com.br/pages/nike-moon-shoe-jacquemus-guia-lk`
- Snapshot canônico local: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/references/moon-shoe-jacquemus-canonical-guide-pattern.html`
- Referência interna: guia Moon Shoe / Jacquemus / “Monshu”

Atenção: se o navegador estiver preso em **Shopify dev preview** (`lk-new-theme/dev`, barra “Draft”), a URL pública pode renderizar só o título/rodapé porque o preview usa outro tema/template. Para auditoria de padrão, usar a URL fora do preview ou o snapshot local acima.

Nenhum novo guia deve ser criado como página textual genérica. Antes de criar ou alterar guias, o executor deve abrir/analisar o padrão Moon Shoe e reutilizar sua lógica visual, editorial e estrutural.

## Lei anti-invenção

A LK não cria páginas “da cabeça”. Todo novo guia, página de marca, source page ou coleção editorial deve nascer de um dos moldes aprovados abaixo. Se o pedido não encaixar em um molde existente, o executor deve primeiro propor um **novo padrão/template para aprovação** e só depois criar a página.

Regras obrigatórias:

- reutilizar estrutura, hierarquia visual, espaçamento e componentes aprovados;
- declarar qual molde está sendo usado antes de escrever ou montar a página;
- consultar fontes reais antes de afirmar contexto de marca, cultura, collab, materiais ou origem do modelo;
- nunca inventar nomes de seções, labels visíveis, CTAs ou formatos novos sem aprovação;
- quando houver dúvida entre “coleção” e “guia”, separar: coleção vende primeiro; guia aprofunda depois;
- toda exceção precisa ficar registrada no brief, com motivo comercial/SEO/CRO claro.

## Moldes canônicos

1. **Coleção Shopify produto-first**
   - Produtos aparecem antes de qualquer texto longo.
   - Topo minimalista: H1 limpo e dominante; kicker curto sem repetir o nome da coleção; parágrafo breve e, quando aprovado, mídia/fotos no padrão existente.
   - Se o H1 já mostra o nome da coleção, o kicker não repete esse nome. Exemplo correto: `CURADORIA LK`; evitar `CURADORIA LK · NEW BALANCE 204L` quando o H1 já é `New Balance 204L`.
   - Grid padrão: 20 produtos por página para preservar respiro, performance e leitura premium; exceções precisam ser aprovadas no brief.
   - Guia/FAQ/schema ficam depois do grid ou em página linkada.
   - Padrão visual de referência quando aplicável: New Balance 204L.

2. **Guia editorial linkado à coleção**
   - Página independente em `/pages/guia-...`.
   - Visual e estrutura no padrão Moon Shoe.
   - A coleção pode ter CTA discreto apontando para o guia, mas não deve virar uma matéria longa antes dos produtos.

3. **Source page / matéria de marca ou collab**
   - Página editorial premium para contexto de marca, collab, origem, matérias externas e leitura de curadoria.
   - Hero forte, fontes externas, cards de referência, blocos citáveis LK e CTA discreto.
   - Não pode ser artigo simples de texto corrido.

4. **Página de apoio SEO/GEO / autenticidade / comparação**
   - Usa o padrão editorial quando for customer-facing.
   - Deve ter fontes, tabela ou checklist útil, FAQ e blocos citáveis.
   - Não pode virar página genérica de palavras-chave.

## Ordem obrigatória de criação

1. Classificar o tipo: coleção produto-first, guia linkado, source page ou apoio SEO/GEO.
2. Abrir o padrão canônico correspondente: Moon Shoe para guias/source pages; 204L para coleção produto-first quando aplicável.
3. Preencher `templates/brief-guia-editorial-colecao-lk.md`.
4. Listar fontes reais que serão usadas.
5. Produzir rascunho/preview no molde escolhido.
6. Fazer QA contra este documento antes de pedir aprovação.
7. Só fazer write em Shopify produção com aprovação explícita.

## O que torna o padrão correto

O guia correto tem aparência de matéria editorial premium, não de bloco SEO simples. Ele combina:

- curadoria de produto;
- narrativa de moda;
- fontes externas relevantes;
- comparação clara;
- visual rico;
- FAQ estruturada;
- CTA comercial discreto.

## Estrutura obrigatória

Todo guia novo deve conter, salvo justificativa explícita:

1. **Hero editorial**
   - layout visual forte;
   - imagem contextual/editorial;
   - eyebrow curto;
   - H1 com leitura premium;
   - introdução curada, não genérica.

2. **Fonte/tipografia com cara editorial**
   - uso de fonte serifada para H1 e headings quando aplicável;
   - espaçamento de matéria;
   - hierarquia visual refinada;
   - nada com aparência de texto corrido básico.

3. **Imagem ou módulo visual relevante**
   - imagem de produto, campanha, street style ou contexto cultural;
   - alt text descritivo;
   - não usar imagem apenas decorativa sem contexto.

4. **Tabela comparativa**
   - obrigatória sempre que houver versões, colorways, materiais, proporções ou usos diferentes;
   - formato similar ao Moon Shoe: `Colorway / Leitura visual / Por que importa` ou equivalente;
   - a tabela deve ajudar a comprar melhor, não apenas preencher SEO.

5. **Sinais editoriais e fontes externas**
   - cards com links para fontes como Vogue, GQ, Hypebeast, Hypebae, Highsnobiety, Adidas/Nike/Onitsuka oficial etc.;
   - explicar por que a fonte importa para a leitura do produto;
   - usar `rel="nofollow noopener"` quando link externo;
   - nunca inventar fonte ou citação.

6. **Blocos citáveis LK**
   - blocos próprios com frases que uma IA ou Google AI Overview conseguiria citar;
   - linguagem clara, factual e premium;
   - sem parecer briefing interno.

7. **Contexto de moda/cultura**
   - origem do modelo;
   - por que voltou ou importa hoje;
   - como aparece em styling, cultura pop, runway, street style ou collabs;
   - relação com o olhar de curadoria da LK.

8. **Orientação comercial real**
   - explicar diferença entre versões, materiais, proporção, cor e contexto de uso;
   - ajudar o cliente a escolher;
   - manter a LK como boutique premium com atendimento humano.

9. **FAQ em acordeão ou estrutura equivalente**
   - perguntas úteis para compra;
   - respostas objetivas;
   - compatível com Schema/FAQ quando aplicável.

10. **CTA discreto**
   - botão preto/limpo ou equivalente premium;
   - direcionar para coleção/produtos relevantes ou atendimento;
   - não usar CTA grosseiro ou repetitivo.

## Linguagem obrigatória

Usar:

- curadoria exclusiva;
- boutique premium;
- seleção especializada;
- produto original;
- atendimento humano;
- orientação de escolha;
- versão, material, proporção, cor, contexto de uso.

Evitar:

- “pronta entrega”, “encomenda”, “estoque” como taxonomia pública;
- texto genérico de SEO;
- blocos visíveis com rótulos internos como “Sinal editorial”;
- promessa operacional que deve ficar no atendimento;
- linguagem de marketplace ou busca por menor preço.

## Checklist antes de publicar

Antes de qualquer guia ir para produção, verificar:

- [ ] O guia Moon Shoe foi usado como referência visual.
- [ ] Há hero editorial com imagem.
- [ ] Há tabela comparativa útil.
- [ ] Há pelo menos uma seção de fontes externas/fashion signals quando o tema permitir.
- [ ] Há blocos citáveis LK.
- [ ] Há FAQ.
- [ ] Há CTA discreto.
- [ ] A copy evita linguagem operacional proibida.
- [ ] O topo da coleção foi revisado quando o guia for linkado em coleção.
- [ ] O guia não é apenas texto corrido.
- [ ] O link da coleção aponta para `/pages/...`, não só para âncora interna.
- [ ] Existe rollback/backup antes de qualquer alteração em produção.

## Fluxo obrigatório para próximos guias

1. Pesquisar o produto/modelo em fontes de moda, cultura sneaker, site oficial e SERP.
2. Abrir o guia Moon Shoe e mapear a estrutura visual.
3. Criar rascunho HTML no padrão Moon Shoe.
4. Validar se há tabelas, imagens, fonte editorial, cards de referência e FAQ.
5. Gerar preview/local ou dev quando possível.
6. Só publicar em produção com aprovação explícita quando houver alteração visível.
7. Após publicar, validar HTML público, mobile e links.
8. Registrar receipt e rollback.

## Aplicação imediata

As páginas atuais abaixo precisam ser refeitas para esse padrão antes de serem consideradas finais:

- `https://lksneakers.com.br/pages/guia-adidas-samba`
- `https://lksneakers.com.br/pages/guia-onitsuka-tiger-mexico-66`

Problema identificado nelas:

- sem tabelas;
- sem cards de fontes externas;
- sem estrutura visual Moon Shoe;
- muito textuais para o padrão LK.

## Status

Este padrão é mandatório para LK Growth, SEO/GEO, Shopify collection pages e qualquer guia editorial ligado a coleção ou produto.
