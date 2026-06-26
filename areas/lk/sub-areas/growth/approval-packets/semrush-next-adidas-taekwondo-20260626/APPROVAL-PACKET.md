# Approval Packet — SEMrush next — Adidas Taekwondo

Data: 20260626T002529Z
Status: read-only concluído; **nenhum write externo executado neste packet**.

## Contexto da fila

- Lucas sinalizou que `Nike Shox TL` não é necessário porque a LK não vende esse foco agora.
- Alo Yoga já está trabalhado e deve ficar em medição.
- Higiene Asics geral foi executada e validada.
- Próximo candidato SEMrush com superfície pronta e fit comercial: **Adidas Taekwondo**.

## Por que Adidas Taekwondo agora

Dados SEMrush/DataForSEO anteriores:
- `adidas taekwondo` — volume aprox. 6.600.
- Caudas/intent SERP: `adidas taekwondo feminino`, `mei`, `ballet`, `lace`, `branco`, `preto`, `prata`, `rosa`.

Readback LK:
- URL: `/collections/adidas-taekwondo`
- Público: 200 OK.
- Admin: collection existe, legacy id `440811880670`.
- Produtos na collection: 16 no Admin / 15 públicos no fetch.
- Sem `Liquid error`.
- Sem termos proibidos na description Admin (`sob encomenda`, `4 a 6 semanas`, `pronta entrega`).

Gaps atuais:
- SEO title público fraco: `Adidas Taekwondo - LK`.
- Meta atual genérica: `Compre Adidas Taekwondo na LK Sneakers. 100% originais · Parcele em 10x · Frete grátis · Loja Jardins SP.`
- FAQ público existe, mas `FAQPage schema = 0`.
- Copy pública é funcional, mas não captura bem a intenção fashion/sneakerina: Taekwondo Mei, Ballet, Lace, perfil baixo, diferença vs Samba/Tokyo, styling feminino.

## SERP atual

DataForSEO mobile BR/PT para `adidas taekwondo`:
- Adidas oficial em #1 com sitelinks para Taekwondo, Taekwondo Lace, Taekwondo Mei e mulher.
- Short videos fortes na SERP.
- Concorrentes com páginas categoria: YourID, Authentic Feet, Bulldog Store.
- PAA/intenção:
  - história do Adidas Taekwondo;
  - como lavar Adidas Taekwondo;
  - Taekwondo feminino;
  - categorias/variações.

## Recomendação

Executar em duas etapas seguras:

### Etapa A — Production SEO title/meta da collection

Proposta SEO title:
`Adidas Taekwondo Original Feminino | Curadoria LK`

Proposta meta description:
`Adidas Taekwondo original na curadoria LK: Taekwondo Mei, Ballet e Lace em silhueta baixa, estética sneakerina e atendimento humano para escolher.`

### Etapa B — DEV preview de guia/FAQ/schema

Preparar em dev/preview um bloco restrito à collection `adidas-taekwondo`, sem publicar produção, cobrindo:
- Adidas Taekwondo Mei / Ballet / Lace;
- feminino e sneakerina;
- diferença Taekwondo vs Samba/Tokyo;
- branco, preto, prata e rosa;
- ajuste/forma em linguagem não operacional;
- autenticidade LK;
- FAQPage schema.

## Risco

- Baixo para SEO title/meta, com rollback simples por campos SEO.
- Médio para guia/FAQ/schema porque a collection já tem FAQ textual na description; no dev precisamos evitar duplicidade visual ou optar por schema-only/compacto.

## Escopo negativo

Não alterar:
- handle/canonical;
- descrição da collection em produção nesta primeira etapa;
- produtos;
- preço;
- estoque/Tiny/inventory;
- ordenação;
- GMC;
- campanhas;
- Klaviyo;
- checkout;
- theme production na etapa de preview.

## Aprovação sugerida

`Aprovo ajustar em produção somente SEO title/meta da collection Adidas Taekwondo (/collections/adidas-taekwondo) para os textos propostos, e preparar em dev/preview um guia/FAQ/schema restrito à mesma collection, sem publicar o guia/schema em produção ainda, sem alterar handle, descrição da collection, produtos, preço, estoque, ordenação, GMC, campanhas, Klaviyo ou checkout, com backup, rollback e readback público.`

## Próximos depois de Taekwondo

1. Se aprovado: executar SEO title/meta e preparar dev/preview.
2. Depois: avaliar se publica schema/guia ou se faz apenas schema-only por já existir FAQ textual.
3. Candidatos seguintes sem Nike Shox TL:
   - Adidas Tokyo: já tem guia público e SEO bom; gap principal é `FAQPage schema=0`, então só schema/impact review.
   - Puma Speedcat: já tem guia público e SEO bom; gap principal é `FAQPage schema=0`.
   - New Balance 9060: já tem guia + FAQPage; manter em medição.
