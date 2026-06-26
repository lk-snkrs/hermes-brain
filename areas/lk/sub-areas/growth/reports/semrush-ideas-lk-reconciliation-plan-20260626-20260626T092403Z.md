# LK — SEMrush Ideas + reconciliação Salomon XT-6

Data UTC: 20260626T092403Z
Fonte: arquivo enviado por Lucas `ideas_lksneakers.com.br_20260626.xlsx` + Shopify Admin read-only + GA4 read-only + HTML público.

## 1. Reconciliação Shopify vs GA4 — Salomon XT-6

### Shopify pedidos encontrados, sem PII
- 2 pedidos pagos com item Salomon XT-6 nos últimos 45 dias.
- Pedido #147923 — 2026-06-25 — landing Google Shopping/CPC em URL antiga Cloudburst; item comprado: Vanilla Ice Almond Milk; total pedido R$ 2.280,00.
- Pedido #147821 — 2026-06-15 — landing homepage com Google Ads; item comprado: Vanilla Ice Oxford Tan; total pedido R$ 2.160,00.

### GA4 item-level
- Período: 2026-05-12 a 2026-06-25.
- Salomon total: 275 item views, 8 add-to-cart, 2 itemsPurchased, R$ 4.799,98 itemRevenue.
- Conclusão: GA4 mede compras no nível de item; o relatório anterior por pagePath deu 0 porque atribuição/pagePath não era o eixo correto.

### Implicação Growth
- As 2 vendas são reais e conectadas a Google/paid signals.
- Precisamos tratar Salomon XT-6 como oportunidade Search/Shopping, mas otimizar collection + feed antes de escalar mídia.

## 2. SEMrush Ideas — resumo do arquivo

- Total de ideias lidas: 78.
- Principais grupos:
  - 13x baixo tempo na página.
  - 11x bounce rate alto.
  - 17x sugestão de aggregate rating/schema.
  - 7x suposta falta de internal links.
  - 8x cannibalization/keyword assigned to a better page.
  - Várias sugestões de backlinks, muitas genéricas/baixa qualidade.

## 3. Leitura crítica — o que NÃO devemos fazer cegamente

- Não adicionar `AggregateRating` falso. Só usar rating se vier de fonte real/verificada, ex: Judge.me/reviews reais.
- Não perseguir backlinks de diretórios/sítios aleatórios sugeridos pelo SEMrush como prioridade premium.
- Não otimizar homepage para tudo. SEMrush apontou homepage para muitos termos, mas várias keywords têm collection/PDP melhor.
- Não consultar estoque/disponibilidade para priorização; qualquer necessidade de disponibilidade deve ir para LK Stock.

## 4. Oportunidades P1/P2

### P1 — Salomon XT-6, já iniciado
- Handles antigos `draft-rebuild` foram limpos e redirects 301 criados.
- Guia com imagem quebrada corrigido/restaurado.
- Próximo: GMC/Merchant health dos 4 produtos + links internos para collection.

### P1 — Schema/reviews com fonte real
- Validar Judge.me/review snippets existentes.
- Se houver review real por produto/collection, preparar patch de schema; se não houver, não inventar rating.

### P1 — Internal links/cannibalization
Aplicar, com aprovação, um bloco de links internos editorial/comercial em páginas prioritárias:
- Home → Onitsuka Tiger, New Balance 204L, Nike Mind 001/002, Vomero Premium, Jacquemus Nike, Salomon XT-6.
- Nike Dunk SB/Panda/Dunk collections → parent Nike Dunk, Dunk SB, Panda product e related collections.
- Onitsuka keywords → consolidar para collections corretas: Mexico 66, Sabot, Todos os Modelos.

### P2 — Homepage bounce/low time
- Verificar GA4 por landing page + channel + device antes de mexer visual.
- Possíveis ações: blocos acima da dobra com hubs SEO/collection, menos dispersão, CTA claro para categorias com demanda.

### P2 — Backlinks/PR
- Priorizar editorial premium: SneakersBR, Vogue/Highsnobiety/Hypebeast quando cabível, creators e press mentions.
- Despriorizar domínios aleatórios de baixa relevância.

## 5. Approval packet sugerido

### Pacote A — sem risco técnico alto
Escopo: links internos e copy editorial em superfícies selecionadas.
- Impacto: médio/alto em SEO e discovery.
- Esforço: médio.
- Risco: baixo/médio; customer-facing.
- Rollback: restaurar snippets/assets/SEO fields anteriores.
- Aprovação necessária: sim, Shopify production/theme/content.

### Pacote B — schema/review
Escopo: validar fonte de reviews e só então schema real.
- Impacto: CTR potencial.
- Risco: médio se schema não for real; deve ser fonte-verificada.
- Aprovação necessária: sim para production.

## 6. Próximo passo recomendado

1. Rodar read-only GMC/Merchant para Salomon XT-6.
2. Preparar patch dev/preview de links internos P1 sem publicar direto.
3. Validar Judge.me/reviews reais antes de qualquer AggregateRating.
4. Fazer impact review D+7 para Salomon XT-6.

Reminder OS loop needed: yes
Reminder OS owner: lk-growth + lk-collection-optimizer, com handoff para lk-shopify se houver theme/content production write.
Reminder OS next action: preparar approval packet Pacote A de internal links + GMC read-only Salomon XT-6.
Reminder OS review trigger: após aprovação do Lucas ou D+7 do patch Salomon XT-6.
Reminder OS evidence: este relatório + Shopify/GA4 read-only + arquivo SEMrush parseado.
