# Approval packet — padrão Guia Editorial LK para outras coleções melhoradas

Data: 2026-05-25
Status: aguardando aprovação explícita de produção

## Pedido

Aplicar o padrão aprovado no Moon Shoe às outras coleções/páginas da LK que já passaram por melhoria editorial/CRO/GEO.

## Padrão canônico a replicar

1. Coleção continua product-first:
   - Hero/H1 nativo
   - Produtos/grid
   - CTA pós-grid para Guia Editorial LK
   - FAQ sem duplicação

2. Guia Editorial estável em Shopify Page:
   - URL dedicada `/pages/{modelo}-guia-lk` ou equivalente
   - CTA de volta para a coleção: `Comprar produtos da coleção` e/ou `Ver produtos da coleção`
   - Bloco de relevância editorial/moda quando houver fontes confiáveis: Vogue, Hypebeast, Hypebae, Highsnobiety, WWD, GQ, Sneaker News etc.
   - FAQ reescrita para objeções reais de compra e answerability em IA
   - Links externos `rel="nofollow noopener"` e nova aba
   - Sem termos públicos proibidos: `encomenda`, `pronta entrega`; evitar taxonomia pública de estoque/disponibilidade

3. Auditoria obrigatória por coleção antes de publicar:
   - SEO/GEO/AI citation readiness
   - FAQ dedupe
   - schema/FAQPage quando aplicável
   - mobile CRO
   - links internos coleção ↔ guia
   - forbidden-term scan
   - rollback e D+7 review

## Coleções detectadas como candidatas já melhoradas no tema

- `new-balance-204l` — coleção já tem copy editorial e padrão visual/reveal; prioridade alta para guia estável.
- `adidas-samba-jane` — já passou por piloto CRO; precisa avaliar se guia editorial/source page faz sentido agora ou se primeiro fecha QA da coleção.
- `onitsuka-tiger`
- `onitsuka-tiger-todos-os-modelos`
- `onitsuka-tiger-mexico-66`
- `new-balance-9060`
- `new-balance-530`
- `nike-x-jacquemus-moon-shoe-sp` — já publicado como referência/padrão.

## Rollout recomendado

### Lote 1 — aplicar agora após aprovação

1. New Balance 204L
   - Criar página guia estável.
   - Link pós-grid da coleção para a página.
   - Buscar fontes de moda/sneaker para bloco de relevância.
   - Revalidar FAQ.

2. Adidas Samba Jane
   - Reusar aprendizado do piloto CRO.
   - Confirmar se o guia deve ser `Adidas Samba Jane` ou mais amplo `Adidas Samba`.
   - Criar/ajustar guia com CTAs de compra.

### Lote 2 — após QA do lote 1

3. Onitsuka Tiger / Mexico 66
4. New Balance 9060
5. New Balance 530

## O que posso fazer sem nova aprovação

- Pesquisa de fontes editoriais por coleção.
- Draft local dos guias.
- Approval packets com título/meta/H1/FAQ/schema/rollback.
- Auditoria SEO/GEO/FAQ/CRO read-only de cada coleção.

## O que exige aprovação explícita

- Criar/editar Shopify Pages públicas.
- Alterar links/copy/section no tema de produção.
- Publicar guias ou mudar coleções públicas.

## Frase de aprovação sugerida

“Pode publicar o padrão Guia Editorial LK nas coleções `new-balance-204l` e `adidas-samba-jane`, criando páginas estáveis e links pós-grid, com rollback e QA.”

## QA de produção exigido por URL

- HTTP 200 público.
- H1 único ou sem duplicação visual.
- CTA guia → coleção funcionando.
- CTA coleção → guia funcionando.
- Bloco de fontes editoriais presente quando aplicável.
- FAQ não duplicada.
- Sem `encomenda`/`pronta entrega` no bloco novo.
- Mobile render OK.
- Receipt local + D+7 review.
