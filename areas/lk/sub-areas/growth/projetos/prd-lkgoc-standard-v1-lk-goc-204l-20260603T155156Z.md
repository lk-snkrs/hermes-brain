# PRD — LK-GOC Standard v1 (`lk-goc-*`) a partir do 204L

Data UTC: 20260603T155156Z

## Objetivo
Transformar a coleção **New Balance 204L** e o guia completo **New Balance 204L Original Brasil — Guia LK** na referência canônica do **LK Growth Optimized Collections** para futuras otimizações de collections/guias da LK.

## Princípio central
O LKGOC deixa de ser uma correção pontual por coleção e passa a ser um **padrão reutilizável da LK**.

Se no futuro o tema X otimizado receber melhoria estrutural aprovada, o tema Y otimizado deve poder receber a mesma melhoria por contrato de classe/componente, sem reescrever layout do zero.

## Namespace padrão
- Preferencial novo: `lk-goc-*`.
- Legado visual permitido quando necessário: `lk-204l-*`.
- Namespace transitório/obsoleto: `lk-lkgoc-*`.

## Contrato de componentes
### Collection editorial block
- `lk-goc-coll-preview`
- `lk-goc-coll-preview--{ collection_handle }`
- `lk-goc-coll-preview__inner`
- `lk-goc-copy`
- `lk-goc-kicker`
- `lk-goc-headline`
- `lk-goc-body`
- `lk-goc-read-more`
- `lk-goc-collage`
- `lk-goc-card`
- `lk-goc-card--large`
- `lk-goc-open-photo`
- `lk-goc-photo-modal`
- `lk-goc-photo-modal__close`

### Guide/editorial page
- `lk-goc-guide`
- `lk-goc-guide--{ guide_handle }`
- `lk-goc-guide-hero`
- `lk-goc-guide-section`
- `lk-goc-guide-grid`
- `lk-goc-guide-card`
- `lk-goc-guide-faq`
- `lk-goc-guide-faq-item`
- `lk-goc-guide-cta`

## Assets auditados
### Público/production read-only
- Coleção: https://lksneakers.com.br/collections/new-balance-204l
- Guia: https://lksneakers.com.br/pages/new-balance-204l-original-brasil-guia-lk

### DEV/unpublished mapeado
Tema: `156623372510` — `LK Curadoria Force Fix Preview 2026-06-03` — role `unpublished`.

Arquivos chave:
- `sections/lk-collection.liquid`
- `sections/lk-nb204l-guide-lkgoc.liquid`
- `templates/page.nb204l-guide.json`
- `assets/lk-204l-hero-fix-20260527-1545.css`
- assets/snippets legados relacionados a Samba/Sambae devem ser tratados como dependentes, não como gold source.

## Diagnóstico do audit inicial
- Produção da collection ainda não usa `lk-goc-*`; usa `lk-lkgoc-*` + `lk-204l-*`.
- Guia público não expõe classes `lk-goc-*`, `lk-lkgoc-*` ou `lk-204l-*` de forma relevante; precisa receber contrato LK-GOC completo.
- DEV já tem parte da migração da collection para `lk-goc-*`, mas ainda há assets/snippets com `lk-lkgoc-*` que devem ser normalizados.
- A migração deve acontecer em DEV/unpublished, com QA e aprovação antes de production.

## Plano de execução seguro
1. Congelar o contrato `lk-goc-*` acima como Standard v1.
2. Migrar no DEV `sections/lk-collection.liquid` para o contrato final `lk-goc-*` + fallback `lk-204l-*` quando necessário.
3. Migrar no DEV `sections/lk-nb204l-guide-lkgoc.liquid` para `lk-goc-guide-*` completo.
4. Consolidar CSS compartilhável em asset/section padrão, evitando estilos exclusivos por handle quando possível.
5. QA técnico:
   - role `unpublished`;
   - readback API;
   - preview renderizado;
   - sem `Liquid error`;
   - sem placeholder editorial;
   - sem FAQ/schema duplicado;
   - selectors JS válidos.
6. QA visual desktop/mobile.
7. Approval Lucas.
8. Merge/promoção para Production somente após approval.

## Regra de evolução futura
Toda melhoria aprovada em um LKGOC deve ser avaliada como melhoria do **Standard LK-GOC**, não como patch isolado.

Implementação esperada:
- manter contrato de classe estável;
- criar receipts por mudança;
- documentar breaking changes;
- reaplicar melhorias em themes/collections já otimizados via diff controlado;
- nunca editar production direto.

## Não escopo imediato
- mudar preço/estoque/produtos;
- mexer em campaigns;
- alterar production sem approval;
- inventar layout novo.
