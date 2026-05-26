# LK Collections — lote seguinte SEO/CRO/GEO readiness

Data: 2026-05-26
Escopo: preparação read-only/local para aplicar o padrão 204L/Samba Jane nas próximas coleções.

## Padrão obrigatório herdado

- Priorizar por GSC + sessões + receita + volume externo + margem editorial/comercial.
- Produto primeiro; guia editorial depois do grid.
- Uma FAQ visível só; FAQ dentro do guia quando fizer sentido.
- Sem CTA `Ver produtos da coleção` dentro do guia.
- Sem botão/contador fake quando a coleção não renderiza `Carregar mais`.
- Espaço pós-grid deve ser medido, não copiado cegamente.
- Imagens editoriais: reveal mobile + lightbox funcional; validar `naturalWidth/naturalHeight` do modal.
- Dev preview permitido no fluxo local; produção exige aprovação explícita.

## Fontes consultadas

- Relatório LK SEO/CRO Weekly Improvement 2026-05-18, correção comercial.
- HTML público de coleções LK via `web_extract`.
- DataForSEO Google Ads Search Volume Brasil/pt.
- DataForSEO SERP live para `adidas samba original feminino` e `onitsuka tiger mexico 66 original`.

## Fila recomendada

### 1) Onitsuka Tiger Mexico 66

URL: https://lksneakers.com.br/collections/onitsuka-tiger-mexico-66

Sinais:
- GA4 histórico: 748 sessões, 0 compras, CVR landing 0,0%, receita R$ 0,00.
- GSC histórico: 31.659 impressões, CTR 1,96%, posição 4,2.
- Volume externo: `onitsuka tiger mexico 66` 6.600 buscas/mês BR; `onitsuka tiger` 33.100 buscas/mês BR.
- SERP: LK aparece em orgânico rank 1/3 e também como referência em AI Overview/produtos para consulta de originalidade.

Diagnóstico:
- Maior prioridade porque já tem visibilidade orgânica/AI e baixa conversão de landing.
- Deve virar coleção padrão 204L/Samba Jane: H1 nativo único, bloco editorial compactado, guia pós-grid, FAQ única.
- Perguntas FAQ recomendadas pela SERP:
  - Quanto custa um Onitsuka Tiger no Brasil?
  - Qual a diferença entre ASICS e Onitsuka Tiger?
  - O Onitsuka Tiger Mexico 66 é da ASICS?
  - O que observar ao escolher o Mexico 66 original?

Risco:
- Não tratar Droper como concorrente-store direto; pode aparecer como marketplace/contexto, mas posicionamento LK deve ser boutique premium/loja especializada.
- Evitar linguagem operacional pública de estoque/prazo.

Ação dev recomendada:
- Criar/ajustar preview com padrão 204L/Samba Jane, usando conteúdo já forte da página + bloco citável GEO.
- Validar FAQPage se a FAQ visível existir e não duplicar.

### 2) Adidas Samba

URL: https://lksneakers.com.br/collections/adidas-samba

Sinais:
- Volume externo: `adidas samba` 246.000 buscas/mês BR; `adidas samba feminino` 60.500 buscas/mês BR.
- SERP para `adidas samba original feminino`: Adidas, Netshoes, Centauro, Buscapé, Mercado Livre, Amazon, Authentic Feet; PAA inclui autenticidade, preço e diferença Samba/Sambae.
- HTML público atual: produto forte, mas conteúdo/FAQ fracos; FAQ aparece como heading sem respostas úteis no resumo extraído.

Diagnóstico:
- Muito volume externo; oportunidade clara de estrutura GEO/FAQ.
- Deve herdar padrão visual da Samba Jane, mas com copy mais ampla: Samba OG, Samba Jane, Sambae, colaborações e acabamentos.
- Como é coleção grande, provavelmente possui zona real de `Carregar mais`; espaçamento pós-grid deve seguir DOM real, não spacer artificial.

FAQ recomendada:
- Como saber se o Adidas Samba é original?
- Qual a diferença entre Samba OG, Sambae e Samba Jane?
- Quanto custa um Adidas Samba original?
- Adidas Samba feminino muda forma/tamanho?

Ação dev recomendada:
- Criar guia pós-grid com FAQ única e bloco citável.
- Verificar se descrição antiga/FAQ nativa está duplicando.
- Usar lightbox/reveal se houver imagem editorial.

### 3) Onitsuka Tiger — todos os modelos

URL: https://lksneakers.com.br/collections/onitsuka-tiger

Sinais:
- GA4 histórico: 1.132 sessões, 1 compra, CVR landing 0,09%, receita R$ 2.499,99.
- GSC histórico: 55.903 impressões, CTR 1,14%, posição 6,9.
- HTML público: coleção grande, 151 itens; já possui copy editorial relevante.

Diagnóstico:
- Boa oportunidade, mas deve vir depois de Mexico 66, porque Mexico 66 é mais específica e já aparece forte em SERP/AI Overview.
- Guia pode explicar árvore de escolha: Mexico 66, Mexico 66 SD, Sabot, Slip-on, colaborações.

Ação dev recomendada:
- Refinar coleção-mãe como hub de navegação editorial, sem competir com Mexico 66.
- FAQ única e schema somente se perguntas visíveis estiverem consolidadas.

### 4) New Balance 9060

URL: https://lksneakers.com.br/collections/new-balance-9060

Sinais:
- Volume externo: 246.000 buscas/mês BR.
- HTML público: 51 itens; conteúdo razoável, mas contém termos operacionais sensíveis (`estoque imediato`, `sob encomenda`, `envio em até 2 dias úteis`) que não devem ser taxonomia pública LK.

Diagnóstico:
- Alto volume; já tem coleção grande e paginação real.
- Precisa limpeza de linguagem operacional e padronização do guia/FAQ antes de produção.

Ação dev recomendada:
- Reescrever bloco editorial com linguagem boutique premium e tirar operacional do conteúdo público principal.
- Comparar com padrão 204L por ser New Balance.

### 5) New Balance 530

URL: https://lksneakers.com.br/collections/new-balance-530

Sinais:
- Volume externo: 201.000 buscas/mês BR.
- HTML público: 24 itens; conteúdo razoável, mas também mostra divergência de troca 7 dias vs 30 dias e termos operacionais.

Diagnóstico:
- Alto volume, mas menor urgência que 9060/Onitsuka/Samba no histórico comercial disponível.
- Deve receber padronização depois do primeiro lote.

Ação dev recomendada:
- Ajustar copy de guia e FAQ; resolver inconsistência 7/30 dias antes de produção.

## Ordem de execução sugerida

1. Onitsuka Tiger Mexico 66
2. Adidas Samba
3. Onitsuka Tiger todos os modelos
4. New Balance 9060
5. New Balance 530

## Approval boundary

Nenhum write Shopify/produção executado neste relatório.
Próximo passo seguro: preparar dev preview das duas primeiras coleções (`onitsuka-tiger-mexico-66` e `adidas-samba`) com recibo/rollback e QA. Produção somente após aprovação explícita.
