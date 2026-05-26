# LK Collections — SEO/GEO/CRO/FAQ audit packet

Data: 2026-05-26
Modo: read-only/local. Nenhum write em Shopify, tema, feed, campanhas ou produção.

## Veredito executivo

Vamos usar como padrão para as próximas coleções:

1. **Critério de escolha**: GSC + sessões + receita + volume externo + margem editorial/comercial.
2. **Estrutura visual**: paridade 204L/Samba Jane, mas só quando fizer sentido por coleção.
3. **FAQ repensada**: uma FAQ visível por coleção, com perguntas reais de busca/compra; sem FAQ decorativa, sem duplicação e com `FAQPage` apenas quando bater exatamente com o conteúdo visível.
4. **GEO**: cada coleção precisa ter pelo menos um bloco citável, curto, auto-contido e útil para AI Overview/ChatGPT/Perplexity.
5. **CRO**: produto primeiro; guia depois do grid; mobile comprimido; imagens editoriais com reveal + lightbox validado.

## Ranking do lote seguinte

### 1. Onitsuka Tiger Mexico 66 — prioridade máxima

URL: https://lksneakers.com.br/collections/onitsuka-tiger-mexico-66

**Dados usados**
- GA4 histórico: 748 sessões, 0 compras, CVR landing 0,0%, receita R$ 0,00.
- GSC histórico: 31.659 impressões, CTR 1,96%, posição 4,2.
- Volume externo BR: `onitsuka tiger mexico 66` 6.600/mês; `onitsuka tiger` 33.100/mês.
- SERP live: LK aparece em orgânico e também citada no AI Overview / product surfaces para consulta de originalidade.

**SEO/GEO audit**
- Pontos fortes: página já tem texto citável, intenção clara e presença de AI Overview.
- Gap: precisa estruturar melhor perguntas e respostas com H2/FAQ visível; aproveitar a presença em AI Overview sem soar marketplace.
- Bloco citável recomendado: definição do Mexico 66 + por que comprar na LK + orientação de escolha por material/modelo.

**FAQ recomendada**
- Quanto custa um Onitsuka Tiger no Brasil?
- Qual a diferença entre ASICS e Onitsuka Tiger?
- O Onitsuka Tiger Mexico 66 é da ASICS?
- Como escolher entre Mexico 66, SD, Sabot e Slip-on?
- O Mexico 66 tem a forma grande ou pequena?

**CRO/visual**
- Aplicar padrão 204L/Samba Jane: H1 nativo único, bloco editorial compacto, guia pós-grid, FAQ única.
- Como é coleção grande, medir se existe `coll-loadmore`; não inserir spacer artificial se a paginação real já cria ritmo.
- Imagens editoriais só se houver asset LK ou imagem com direito/segurança; se usar cards, lightbox obrigatório.

**Risco**
- Não tratar Droper como concorrente-store direto; é marketplace/contexto.
- Evitar copy operacional pública sobre estoque/prazo.

**Próxima ação segura**
- Preparar dev preview primeiro.

---

### 2. Adidas Samba — prioridade alta

URL: https://lksneakers.com.br/collections/adidas-samba

**Dados usados**
- Volume externo BR: `adidas samba` 246.000/mês; `adidas samba feminino` 60.500/mês.
- SERP live: PAA com originalidade, preço, diferença Samba/Sambae e aparência do Samba original.
- HTML público: heading `Perguntas Frequentes` aparece, mas a extração não mostrou Q&A útil; conteúdo atual tem termos operacionais e generalistas.

**SEO/GEO audit**
- Ponto forte: enorme demanda externa e variedade de modelos.
- Gap: página deveria responder melhor a intenção de comparação: Samba OG vs Sambae vs Samba Jane vs XLG.
- Oportunidade GEO: capturar perguntas de AI/PAA com respostas curtas e citáveis.

**FAQ recomendada**
- Como saber se o Adidas Samba é original?
- Qual a diferença entre Samba OG, Sambae, Samba Jane e Samba XLG?
- Quanto custa um Adidas Samba original?
- O Adidas Samba feminino muda forma/tamanho?
- Qual Samba escolher para rotina: couro, camurça ou versões plataforma?

**CRO/visual**
- Herdar a família visual da Samba Jane, mas com copy de coleção-mãe.
- Produto primeiro; guia editorial depois do grid.
- Se houver coleção grande com paginação real, não usar spacer.
- Remover/evitar FAQ fantasma: se o título de FAQ existe, precisa ter perguntas reais ou ser removido.

**Risco**
- Concorrência forte de Adidas, marketplaces e varejistas grandes; LK deve competir por curadoria, autenticidade assumida, atendimento humano e seleção especializada — não por preço.

**Próxima ação segura**
- Preparar dev preview com guia + FAQ consolidada.

---

### 3. Onitsuka Tiger — todos os modelos

URL: https://lksneakers.com.br/collections/onitsuka-tiger

**Dados usados**
- GA4 histórico: 1.132 sessões, 1 compra, CVR landing 0,09%, receita R$ 2.499,99.
- GSC histórico: 55.903 impressões, CTR 1,14%, posição 6,9.
- HTML público: já tem bloco `Curadoria LK · Onitsuka Tiger`, guia e FAQ visível.

**SEO/GEO audit**
- Ponto forte: já funciona como hub amplo.
- Gap: precisa evitar duplicação entre descrição nativa + bloco guia; checar se há duas FAQs/schema.
- Papel estratégico: hub de navegação para Mexico 66, SD, Sabot, Slip-on e colaborações.

**FAQ recomendada**
- Qual Onitsuka Tiger escolher primeiro?
- A LK trabalha com Onitsuka Tiger original?
- Como usar Onitsuka Tiger em looks casuais e fashion?
- A forma muda entre Mexico 66, SD e Sabot?

**CRO/visual**
- Não competir com Mexico 66; direcionar por intenção de escolha.
- Manter mobile comprimido; produtos devem aparecer rápido.

**Próxima ação segura**
- Dev preview depois de Mexico 66/Samba.

---

### 4. New Balance 9060

URL: https://lksneakers.com.br/collections/new-balance-9060

**Dados usados**
- Volume externo BR: `new balance 9060` 246.000/mês.
- HTML público: 51 itens e bloco `Curadoria LK` já existente.

**SEO/GEO audit**
- Ponto forte: demanda enorme e boa profundidade de catálogo.
- Gap: texto atual contém termos operacionais sensíveis (`estoque imediato`, `sob encomenda`, `envio em até 2 dias úteis`) e erro de digitação (`ganrou`).
- Oportunidade: padrão visual New Balance alinhado à 204L, com foco em proporção, conforto e escolha de colorway.

**FAQ recomendada**
- O New Balance 9060 é confortável para uso diário?
- Qual a diferença entre New Balance 9060 e outros modelos New Balance?
- Como escolher a cor do New Balance 9060?
- O New Balance 9060 tem a forma grande ou pequena?

**CRO/visual**
- Aplicar padrão 204L com cuidado de paginação real.
- Limpar linguagem operacional antes de produção.

**Próxima ação segura**
- Fase 2 do lote, após Onitsuka/Samba.

---

### 5. New Balance 530

URL: https://lksneakers.com.br/collections/new-balance-530

**Dados usados**
- Volume externo BR: `new balance 530` 201.000/mês.
- HTML público: 23/24 itens; bloco `Curadoria LK · New Balance 530` já existente.

**SEO/GEO audit**
- Ponto forte: volume alto e posicionamento fácil de entender: running retrô, uso real, conforto.
- Gap: texto atual traz frase com erro gramatical (`do silhueta`) e termos operacionais; resumo público também apontou inconsistência de troca 7 dias vs 30 dias.
- Como é coleção menor, verificar ausência/presença de `coll-loadmore`; pode precisar de spacer pós-grid como Samba Jane, mas medido.

**FAQ recomendada**
- O New Balance 530 é bom para rotina?
- Qual cor de New Balance 530 é mais versátil?
- Qual a diferença entre New Balance 530 e 9060?
- O New Balance 530 tem a forma grande ou pequena?

**CRO/visual**
- Aplicar padrão de guia compacto e FAQ única.
- Se não houver paginação real, medir gap e usar spacer scoped; não inserir controle fake.

**Próxima ação segura**
- Fase 2 do lote, após 9060.

---

## Checklist dos 18 tópicos canônicos

- GA4: usado parcialmente via relatório histórico; precisa refresh atual para decisão final.
- GSC: usado parcialmente via relatório histórico; precisa refresh atual para decisão final.
- GMC: não aplicável nesta etapa, exceto se a coleção expuser product cards com warnings; não auditado agora.
- Shopify SEO: auditado por HTML/texto público; sem write.
- Shopify CRO/theme: auditado por padrão visual/FAQ/guia; sem write.
- GEO/AI Search: auditado com SERP/AI Overview/PAA e robots/llms.
- PageSpeed/CrUX/CWV: não auditado neste pacote; necessário antes de produção se houver novo bloco pesado/imagens.
- Schema: recomendado FAQPage condicional; não validado via rich result neste pacote.
- Reviews/prova social: não aplicável diretamente às collections, mas pode entrar como prova de loja se não inventar review.
- Paid media: não usado; sinal contextual ausente.
- Influencer/social demand: parcialmente observado por SERP de vídeos/shorts para Samba/Onitsuka; sem dados proprietários.
- Concorrência/SERP: auditado para Samba e Mexico 66; precisa ampliar para NB 9060/530 na fase 2.
- Google Business/local: não aplicável direto à coleção, mas loja Jardins pode reforçar confiança se usado discretamente.
- Klaviyo/CRM signals: não usado.
- Catálogo/product data quality: risco textual/operacional identificado; feed/SKU não auditado.
- Conteúdo/taxonomia comercial: auditado; manter linguagem boutique premium e evitar taxonomia pública de estoque/encomenda.
- Mensuração/QA de eventos: não auditado; se houver dev preview, validar cliques de guia, reveal, lightbox e product grid.
- Impact review/experimentation: recomendado D+7 após qualquer produção.

## Próximo pacote de execução em dev preview

Fase 1 recomendada:
1. `onitsuka-tiger-mexico-66`
2. `adidas-samba`

Escopo do dev preview:
- Consolidar FAQ única.
- Inserir/ajustar guia pós-grid.
- Medir gap pós-grid vs paginação real.
- Aplicar visual 204L/Samba Jane onde fizer sentido.
- Validar mobile: produto aparece rápido, sem blocos duplicados.
- Validar lightbox se houver cards de imagem.
- Gerar receipt/rollback.

Produção: somente com aprovação explícita depois do preview.
