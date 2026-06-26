# LK PDP CRO hotfix — QA read-only

Data: 2026-05-26T13:20:15-0300  
Escopo: validação read-only do hotfix de CRO aplicado no PDP em 2026-05-19.  
PDP testado: `https://lksneakers.com.br/products/tenis-adidas-samba-jane-black-white-gum-preto`

## Resultado executivo

Status: **aprovado com observações**.

O hotfix segue ativo e funcional em PDP público. A trustbar mostra Google 4.9 com 400+ avaliações, substitui Frete Grátis por Loja Física Jardins, SP sem duplicação indevida, mantém o Provador Virtual com CSS de 52px, abre modal/fallback de avaliações de produto e abre modal próprio de Google reviews. No mobile, a área de compra/trustbar está visualmente estável, sem regressão crítica observada.

## Evidências read-only

### 1. Trustbar Google

- Encontrado: `GOOGLE\n4.9 · 400+ AVALIAÇÕES`.
- Desktop: botão `#lk-reviews-trigger`, visível.
- Mobile iPhone 13: `x=21`, `y=1079`, `w=88`, `h=50`, `display=flex`, `visibility=visible`.
- Contagem no texto principal mobile: 1 ocorrência.

### 2. Loja Física Jardins, SP

- Encontrado: `LOJA FÍSICA\nJARDINS, SP`.
- Contagem no texto principal desktop/mobile: 1 ocorrência.
- Não encontrei duplicação indevida no PDP testado.
- No bloco de trustbar do PDP, não encontrei `Frete Grátis` substituindo o item de loja física.

### 3. Provador Virtual 52px

- Elemento encontrado: botão `.pi-atc` com texto `Provador Virtual`.
- CSS medido: `height: 52px`, `min-height: 52px`, `font-size: 11px`.
- Observação: no PDP testado ele estava com `display: none` no estado inicial, mas a regra de altura permanece aplicada conforme solicitado.

### 4. Avaliações de produto / Judge.me com fallback

- Clique programático read-only no link `.pi-rating-link` abriu o modal: `.pdp-reviews-modal is-open`.
- Após aguardar carregamento, fallback ficou visível: `display=block`, altura aproximada `227px`.
- Texto renderizado no fallback: `0 avaliações deste produto` + CTA `Ver avaliações no Google`.
- Console registrou warning do Judge.me: `Cannot load Judge.me widget contents due to missing jdgm key...`; por isso o fallback é importante e funcionou.

### 5. Modal Google

- Clique read-only em `#lk-reviews-trigger` abriu modal `.lk-reviews-modal is-open`.
- Conteúdo renderizado: `AVALIAÇÕES DO GOOGLE`, nota `4.9`, `400+ avaliações no Google` e cards de reviews.
- Em mobile, modal ocupou a viewport (`modalH=664`) e abriu sem quebra crítica.

### 6. QA visual mobile

Viewport testado: iPhone 13 / 390px.  
Capturas locais geradas para evidência:

- `/opt/data/tmp/lk_pdp_hotfix_mobile_20260526.png`
- `/opt/data/tmp/lk_pdp_hotfix_mobile_trustbar_20260526.png`

Leitura visual da área de compra/trustbar:

- CTAs `ADICIONAR AO CARRINHO` e `COMPRE JÁ` aparecem alinhados e sem sobreposição.
- Trustbar compacta aparece logo abaixo dos CTAs com Google, Autenticidade, Parcele em e Loja Física.
- Aviso `Sujeito a encomenda · 4-6 semanas · Confirme no WhatsApp` aparece discreto abaixo da trustbar.
- Sem regressão visual crítica na área testada.

Pontos de atenção não bloqueantes:

- Trustbar mobile está compacta e com texto pequeno, mas legível.
- No primeiro viewport/topo do PDP, os elementos de confiança não aparecem ainda; aparecem após a área de tamanho/CTA, o que é aceitável para o escopo do hotfix, mas pode ser testado futuramente contra uma versão ainda mais próxima do preço.
- Console apresentou erros/warnings de terceiros já observáveis em QA: Judge.me sem key, Variant King selector, CORS em endpoints de tracking/WhatsApp. Não identifiquei impacto visual direto no hotfix validado, mas vale tratar como backlog técnico separado.

## Checklist do pedido

- [x] Trustbar mostra Google 4.9 · 400+ avaliações.
- [x] Há Loja Física Jardins, SP.
- [x] Não há duplicação indevida de Loja Física no PDP testado.
- [x] Não há Frete Grátis substituindo Loja Física na trustbar do PDP testado.
- [x] Provador Virtual mantém CSS de 52px.
- [x] Clique nas avaliações de produto abre modal/fallback.
- [x] Clique no Google abre modal Google.
- [x] Sem regressão visual mobile crítica observada.

## Recomendação

- **Manter o hotfix em produção.** Não há evidência para rollback.
- Abrir apenas backlog técnico não urgente para investigar warnings de terceiros no console, especialmente Judge.me key/Variant King/CORS de tracking, porque o fallback está cobrindo a experiência de avaliações, mas o ideal é reduzir ruído e dependência de fallback.
- Para decisão comercial de impacto, usar a revisão D+7 já registrada em `reports/theme-production-pdp-cro-impact-d7-2026-05-26.md`; este QA é funcional/visual, não altera priorização por receita sozinho.

## Guardrail

- Ações executadas: navegação pública, inspeção DOM, clique programático local/read-only, screenshot local e relatório interno.
- Writes externos: 0.
- Não executado: Shopify/theme write, produto, preço, estoque, campanha, Klaviyo, GMC/feed ou envio externo.
