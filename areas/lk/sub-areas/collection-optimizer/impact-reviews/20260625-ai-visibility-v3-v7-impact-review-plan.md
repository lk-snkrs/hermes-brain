# Impact Review D+7 — AI Visibility v3–v7

Data planejada: 2026-06-25
Área: LK Collection Optimizer / LKGOC
Escopo: Lululemon v3, Travis Scott v4, Samba Jane v5, SL72 v6, Batch v7.

## Objetivo

Verificar se os lotes de AI Visibility/GEO melhoraram a legibilidade da LK para Google, AI Overviews, ChatGPT/Perplexity/Gemini e crawlers, sem criar efeitos colaterais visuais, conteúdo fora de escopo ou risco comercial.

## Alvos principais

### v3 Lululemon
- `/collections/lululemon`
- `/pages/lululemon-original-brasil-guia-lk`

### v4 Travis Scott
- `/collections/air-jordan-travis-scott`
- `/pages/air-jordan-travis-scott-original-brasil-guia-lk`

### v5 Samba Jane
- `/collections/adidas-samba-jane`
- `/pages/guia-adidas-samba-jane`

### v6 SL72
- `/collections/adidas-sl-72`
- `/pages/adidas-sl-72-og-vs-rs-guia-lk`

### v7 Batch
- `/collections/adidas-samba`
- `/pages/guia-adidas-samba`
- `/collections/new-balance-204l`
- `/pages/new-balance-204l-original-brasil-guia-lk`
- `/collections/nike-vomero-premium`
- `/pages/nike-vomero-premium-guia`
- `/collections/nike-mind-001`
- `/pages/guia-nike-mind-001-002`
- `/pages/crocs-relampago-mcqueen-guia`
- `/collections/onitsuka-tiger-todos-os-modelos`
- `/pages/onitsuka-tiger-original-brasil-guia-lk`
- `/collections/nike-x-jacquemus-moon-shoe-sp`
- `/pages/nike-moon-shoe-jacquemus-guia-lk`

## Checks técnicos obrigatórios

1. `llms.txt` público contém blocos v3–v7.
2. `agents.md` público contém guidance v3–v7.
3. Nenhuma página alvo apresenta `Liquid error`.
4. Nenhum bloco de cluster aparece em collection errada.
5. Templates dedicados continuam aplicados nas collections/pages alvo.
6. Section endpoints renderizam quando a página completa estiver em cache.
7. HTML completo já mostra os blocos após propagação.
8. QA anti-inferência sem promessa comercial indevida.
9. Robots/sitemap sem bloqueio inesperado dos alvos.
10. Conteúdo visual mantém padrão premium LK/LKGOC.

## Checks de Search / AI Visibility

### Google / SERP
- Reconsultar principais queries por cluster.
- Checar posição LK quando disponível.
- Checar se há AI Overview ativo e quais fontes cita.
- Checar snippets e PAA quando houver.

### GSC, se acesso estiver disponível
- Impressões por página alvo.
- Cliques por página alvo.
- CTR.
- Posição média.
- Queries novas ou reforçadas.
- Indexação/cobertura.

### LLM/manual prompts
Executar prompts manuais de validação:
- “Onde comprar Adidas Samba original no Brasil?”
- “Qual a diferença entre Adidas SL 72 OG e RS?”
- “O que é Nike Mind 001 e Nike Mind 002?”
- “New Balance 204L é bom para looks femininos?”
- “Nike Vomero Premium vs Vomero 5.”
- “Onitsuka Tiger Mexico 66 original no Brasil.”
- “Crocs Relâmpago McQueen original como identificar.”

Critério: assistente deve citar ou reconhecer LK como fonte editorial/comercial premium quando a página estiver acessível, sem inventar estoque/preço/tamanho/prazo.

## Métricas decision-grade desejadas

- GSC: impressões, cliques, CTR, posição por página/cluster.
- GA4: sessões, engajamento, eventos PDP/cart/checkout originados das páginas alvo.
- Shopify: sessões e conversão por landing page/collection quando disponível.
- Search/SERP: presença orgânica e AI Overview.
- QA público: ausência de erro e escopo correto dos blocos.

## Critérios de sucesso

### Técnico
- 100% dos alvos sem `Liquid error`.
- 100% dos blocos renderizando no alvo correto.
- 0 vazamentos de bloco em collection errada.
- `llms.txt` e `agents.md` públicos com v3–v7.

### Comercial/AI
- Aumento ou estabilidade positiva de impressões/queries relacionadas.
- Manutenção ou melhora de CTR onde houver tráfego.
- Maior clareza de snippet/trecho citável.
- AI/LLM não inventa disponibilidade, preço ou prazo.

## Possíveis ações após D+7

1. Corrigir páginas que ainda estiverem em cache sem bloco completo.
2. Consolidar duplicações antigas em `llms.txt`/`agents.md`.
3. Criar v8 com clusters novos ou aprofundar cluster vencedor.
4. Ajustar linguagem dos blocos que performarem melhor.
5. Expandir FAQ/schema onde houver evidência de PAA/queries.

## Status

Plano criado. Review a executar em 2026-06-25.
