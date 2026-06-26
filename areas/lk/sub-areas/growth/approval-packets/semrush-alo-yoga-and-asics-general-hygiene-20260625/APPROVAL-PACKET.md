# Approval Packet — SEMrush follow-up — Alo Yoga + higiene Asics geral

Data: 20260625T233658Z
Status: read-only concluído; **nenhum write executado neste packet**.

## 1) Cache público dos 3 recém-publicados

Readback público da URL base, sem query funcional:

| Collection | HTTP | Guia presente | FAQPage | Liquid error |
|---|---:|---:|---:|---:|
| Adidas Samba Marrom | 200 | sim | 1 | não |
| Lululemon Define Jacket | 200 | sim | 1 | não |
| ASICS Gel-1130 | 200 | sim | 1 | não |

Conclusão: cache/propagação resolvida nas URLs base. Não precisa cache-touch.

## 2) Alo Yoga

Histórico verificado antes de sugerir ação:

- SEO meta Alo Yoga já executado em `receipts/shopify-production/alo-yoga-collection-seo-meta-20260624T143046Z/`.
- LKGOC/guia Alo Yoga já publicado/validado em `receipts/theme-production/alo-yoga-lkgoc-lite-prod-merge-retry-20260624T151214Z/`.
- Há histórico de rollback/ajuste anterior, então evitar novo write sem necessidade clara.

Readback atual:

- URL: `/collections/alo-yoga-1`
- Público: 200 OK, 109 itens no fetch público.
- Admin: collection existe, 116 produtos no Admin.
- SEO title: `Alo Yoga Original no Brasil | Curadoria LK`
- SEO description: `Alo Yoga original na curadoria LK: activewear premium, tops, calças e peças selecionadas com autenticidade e atendimento humano para escolher.`
- Guia editorial público presente.
- Admin description não contém `sob encomenda`, `4 a 6 semanas` ou `Frete grátis acima de R$ 499`.

Conclusão Alo Yoga:

- **Não recomendo novo write agora.**
- A superfície já está melhorada e o alerta `alo yoga brasil` estava positivo; `alo yoga roupa` já mostrava LK orgânico.
- Próximo correto: monitorar GSC/SEMrush D+7/D+14, não mexer de novo hoje.

## 3) Higiene — Asics geral `/collections/asics-todos-os-modelos`

Readback atual:

- URL: `/collections/asics-todos-os-modelos`
- Público: 200 OK, 13 itens no fetch público.
- Admin: collection existe, 17 produtos no Admin.
- SEO title/meta atuais preservados.
- A descrição pública/admin contém termos operacionais antigos:
  - `sob encomenda`
  - `4 a 6 semanas`
  - `Frete grátis acima de R$ 499`

Trecho público problemático:

> O prazo varia conforme a disponibilidade confirmada e a região de entrega. Itens sob encomenda seguem prazo estimado de 4 a 6 semanas. Frete grátis acima de R$ 499.

## Recomendação segura — Asics geral

Fazer apenas higiene editorial da FAQ da collection geral Asics:

Substituir a resposta de prazo por linguagem premium/neutra, sem promessa operacional:

> O prazo varia conforme a região e os detalhes do pedido. Quando necessário, o atendimento humano da LK confirma as informações antes da finalização da compra.

Não mexer em:
- SEO title/meta;
- handle/canonical;
- produtos;
- preço;
- estoque/Tiny/inventory;
- ordenação;
- GMC;
- campanhas;
- Klaviyo;
- checkout;
- tema.

## Aprovação sugerida

`Aprovo aplicar em produção a higiene editorial da collection geral Asics (/collections/asics-todos-os-modelos), limitada a remover/normalizar os termos públicos sob encomenda, 4 a 6 semanas e Frete grátis acima de R$ 499 da FAQ de prazo, substituindo por linguagem neutra de atendimento humano LK, sem alterar SEO title/meta, handle, descrição fora desse trecho, produtos, preço, estoque, ordenação, GMC, campanhas, Klaviyo, checkout ou tema, com backup, rollback e readback público.`

## Próximos passos

1. Se aprovado: executar higiene Asics geral com backup/readback.
2. Alo Yoga: deixar em medição; não fazer write agora.
3. Manter D+7/D+14 para Adidas Samba Marrom, Lululemon Define, ASICS Gel-1130 e Alo Yoga.
