# CRO Mobile P1 — read-only — 2026-06-17

Status: auditoria pública/read-only. Nenhum write. values_printed=false.

## Páginas verificadas

- `/collections/nike-x-jacquemus-moon-shoe-sp`
- `/products/tenis-nike-moon-shoe-sp-jacquemus-off-white`
- `/products/tenis-nike-moon-shoe-sp-jacquemus-medium-brown`
- `/products/tenis-onitsuka-tiger-mexico-66-kill-bill-amarelo`
- `/collections/air-jordan-travis-scott`
- `/collections/new-balance-204l`

## Evidências públicas

### PDP Moon Shoe Off White

- Title público: `Tênis Nike Moon Shoe SP Jacquemus Off White | LK Sneakers`.
- Meta pública contém produto, marca/collab, preço e benefícios comerciais.
- FAQ público detectado: o que é, por que é desejado, como usar, cor, originalidade.
- Simprosys/GSF detectado com dados da variante renderizada.
- Judge.me detectado no HTML.
- Scripts/app blocks pesados detectados: Shopify, Crisp, Judge.me, Simprosys, MK SDK, quick-add/hotfix/recovery beacon.

### PDP Moon Shoe Medium Brown

- Conteúdo público estruturado e FAQ semelhante ao Off White.
- Boa base GEO, mas risco de copy muito igual entre colorways; pode reduzir especificidade perceptiva no mobile.

### PDP Onitsuka Kill Bill

- Conteúdo público forte e FAQ específico: Mexico 66, diferença Onitsuka/ASICS, forma estreita, como usar, originalidade.
- Bom benchmark de PDP answer-first.

### Collection Moon Shoe

- Guia editorial forte e FAQ detectado.
- Gap: há duplicidade/repetição de bloco FAQ/editorial: um `### Perguntas frequentes` dentro do guia e outro `## Perguntas Frequentes` depois. Em mobile isso pode alongar a página e diluir foco de compra.

### Collection Travis

- Collection pública mostra 22 itens e FAQ.
- Não é ausência de conteúdo; o gap é deixar o bloco mais answer-first e compatível com AI Overview/PAA.

## Diagnóstico CRO mobile

### P0 — confiança antes do CTA

Para PDPs de ticket alto, o primeiro viewport mobile precisa responder rapidamente:

- originalidade/curadoria;
- atendimento humano para tamanho e compra;
- pagamento/frete/troca de forma clara;
- CTA sem ruído.

Hoje esses sinais existem, mas parte deles pode ficar espalhada entre descrição, FAQ, apps e área inferior.

### P1 — reduzir redundância de guias

Collections com guia + FAQ duplicado podem ficar longas em mobile. A prioridade é manter:

- grid primeiro;
- bloco editorial curto;
- FAQ com perguntas reais e headings claros;
- evitar dois blocos FAQ com respostas parecidas.

### P1 — colorways vencedoras precisam copy menos genérica

Moon Shoe Off White e Medium Brown têm estrutura boa, mas muito parecida. Em PDP vencedor, cada colorway deve explicar:

- por que aquela cor específica vende;
- com que styling funciona;
- diferença de presença visual;
- quem deve escolher aquela cor.

### P2 — performance/script hygiene

HTML público mostra muitos apps/scripts. Sem PageSpeed/field data na execução atual, o risco é qualitativo, não numérico:

- Crisp;
- Judge.me;
- Simprosys;
- MK SDK;
- quick-add/hotfix/recovery beacon;
- CSS inline/hotfixes acumulados.

Recomendação: auditoria de waterfall/PageSpeed em dev antes de qualquer theme write.

## Recomendações sem write imediato

1. Gerar um padrão de bloco PDP mobile P1:
   - `Autenticidade e curadoria LK`;
   - `Atendimento humano para tamanho`;
   - `Compra segura / parcelamento / frete`;
   - CTA principal limpo.
2. Revisar duplicidade de FAQ em collections com guia editorial.
3. Priorizar Moon Shoe Off White + Medium Brown como CRO PDPs por receita.
4. Medir antes/depois por GA4/Shopify: PDP view → add-to-cart → checkout → receita.

## Approval necessário para qualquer execução

- Theme production: exige aprovação.
- Product description visível em produção: exige aprovação.
- Apps/checkout/cart: exige aprovação.
