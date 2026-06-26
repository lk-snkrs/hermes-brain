# LKGOC — Mapa do que já foi feito / não sugerir como “próxima frente nova”

Atualizado em: 2026-06-06T12:53:24Z

Uso obrigatório: antes de sugerir próxima coleção/guia LKGOC, consultar este mapa + `LKGOC-LEDGER-COLECOES-OTIMIZADAS.md` + receipts/reports relacionados. Não sugerir como “nova” uma frente já trabalhada; se sugerir, declarar como **refinamento/impact review**, não como implantação inicial.

## Production / otimizações fortes confirmadas

- `new-balance-204l`
  - Status: gold source visual/editorial LKGOC.
  - Evidências: `LKGOC-LEDGER-COLECOES-OTIMIZADAS.md`, handoff 204L, receipts production 2026-05-27, approval `lkgoc-standard-v1-204l-dev-to-production-approval-20260603T162846Z.md`.
  - Próximo tipo de trabalho: refinamento, QA, impact review; não tratar como nova frente.

- `new-balance-9060`
  - Status: full LKGOC em Production; coleção pública já tem hero + guia pós-grid + FAQ/schema.
  - URL verificada: `https://lksneakers.com.br/collections/new-balance-9060`.
  - Evidências: `LKGOC-LEDGER-COLECOES-OTIMIZADAS.md`, `work/new-balance-9060-lkgoc-full-20260605/`, `reports/lkgoc-nb9060-dev-preview-incident-20260605.md`.
  - Próximo tipo de trabalho: refinamento, QA, impact review; não tratar como nova frente.

- `new-balance-530`
  - Status: full LKGOC em Production; hero + guia pós-grid + FAQ/schema; FAQ legado suprimido.
  - Evidências: `LKGOC-LEDGER-COLECOES-OTIMIZADAS.md`, work/receipts ligados a 530 e next-wave.
  - Próximo tipo de trabalho: refinamento, QA, impact review; não tratar como nova frente.

## Trabalhadas com histórico relevante / verificar antes de propor

- `onitsuka-tiger` / Onitsuka Tiger / Mexico 66
  - Status: coleção pública já otimizada com bloco editorial/FAQ; guia dedicado existe.
  - URLs verificadas:
    - `https://lksneakers.com.br/collections/onitsuka-tiger`
    - `https://lksneakers.com.br/pages/onitsuka-tiger-original-brasil`
  - Evidências: `receipts/onitsuka-guide-production-publish-20260530.md`, `receipts/onitsuka-guide-fix-dev-20260530.md`, `approval-packets/onitsuka-mexico66-guide-top-approval-20260526.md`, `approval-packets/onitsuka-tiger-collection-corrections-20260526.md`, `reports/onitsuka-collection-faq-schema-geo-audit-20260528.md`.
  - Próximo tipo de trabalho: impact review/refino, não nova frente.

- `adidas-samba` / `guia-adidas-samba-jane` / `sambae`
  - Status: há histórico extenso de LKGOC, correções, guia e snippets; antes de sugerir ou mexer, abrir receipts/work específicos.
  - Evidências: `approval-packets/adidas-samba-lkgoc-full-dev-approval-20260602.md`, `approval-packets/samba-jane-lkgoc-correction-hero-guide-20260602.md`, `approval-packets/sambae-lkgoc-full-dev-approval-20260602.md`, receipts 2026-06-01/02, `work/sambae-lkgoc-20260602T214029Z/`.
  - Próximo tipo de trabalho: refino/QA/production hotfix com cuidado, não nova frente.

- `nike-mind` / `guia-nike-mind-001-002`
  - Status: guia dedicado refeito no LKGOC em DEV e merge tentado/aplicado em Production/Admin; storefront público teve cache/render antigo pendente no último poll.
  - URL: `https://lksneakers.com.br/pages/guia-nike-mind-001-002`.
  - Evidências: `handoffs/handoff-nike-mind-guide-lkgoc-rewrite-20260606T094233Z.md`, `drafts/nike-mind-guide-lkgoc-rewrite-20260606T094233Z/`, `receipts/theme-dev/nike-mind-guide-page-lkgoc-dev-20260606T100703Z/`, `receipts/theme-prod/nike-mind-guide-page-lkgoc-prod-merge-20260606T101421Z/`.
  - Próximo tipo de trabalho: resolver/validar cache público e impact review; não nova frente.

- `nike-moon-shoe` / Moon Shoe Jacquemus
  - Status: histórico forte como referência/padrão de shell/guia; não sugerir como novo sem confirmar lacuna.
  - Evidências: `references/moon-shoe-jacquemus-canonical-guide-pattern.html`, approval packets e reports 2026-05-23 a 2026-05-26.

## Operacional / não confundir com LKGOC de coleção nova

- `gifts-by-lk` / giftable / Gifts
  - Status: muitos receipts operacionais de ordenação, stock/promo/visual. Não é automaticamente LKGOC canônico de coleção; tratar como frente comercial/operacional separada e checar escopo.

## Regra de recomendação

Antes de responder “qual próxima?”, executar:

1. Ler `LKGOC-MAPA-JA-FEITO.md`.
2. Ler `LKGOC-LEDGER-COLECOES-OTIMIZADAS.md`.
3. Buscar no Brain pelo termo candidato.
4. Fetch público da collection/page candidata.
5. Só então classificar:
   - **Nova frente LKGOC**;
   - **Refinamento/QA/impact review**;
   - **Operacional não-LKGOC**;
   - **Bloqueado por falta de dados comerciais**.

## Erro corrigido

Em 2026-06-06, o agente sugeriu Onitsuka Tiger e NB 9060 como próximas sem checar o histórico completo. Lucas corrigiu. Este mapa existe para evitar repetição.


## Nota de QA — 20260606T133050Z

Não marcar nenhuma frente como feita apenas por URL 200/preview. Exigir Definition of Done LKGOC: readback + componente específico + schema/FAQ quando aplicável + QA visual + receipt.
