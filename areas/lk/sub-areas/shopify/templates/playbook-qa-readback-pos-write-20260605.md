# Playbook — QA/readback pós-write LK Shopify

Data: 2026-06-05
Status: template operacional para execução aprovada; read-only/verificação local quando possível.

## Quando usar

Use depois de qualquer execução Shopify aprovada: produto, variante, preço, coleção, page, SEO field, metafield, menu, theme/dev theme, app/config/tracking ou feature de site.

## Worker principal

Readback/Receipt Verifier, com apoio de:

- Shopify QA Visual Worker, se houve mudança visual/theme/page/cart.
- Rollback/Risk Reviewer, se houver divergência ou regressão.
- SEO/Metafield Checker, se campos SEO/metafields foram alterados.

## Fluxo

1. **Resgatar packet aprovado**
   - Link/path do packet:
   - Frase exata de aprovação:
   - Escopo permitido:
   - Ações explicitamente não aprovadas:

2. **Readback fonte viva**
   - Recurso/ID/handle:
   - Campos lidos:
   - Valor esperado:
   - Valor vivo:
   - Match: sim/não/parcial.

3. **QA técnico/visual**
   - URLs testadas:
   - Mobile:
   - Desktop:
   - Fluxo de compra, se aplicável:
   - Tracking/app check, se aplicável:

4. **Comparar escopo**
   - Confirmar que só os objetos aprovados mudaram.
   - Registrar qualquer divergência.
   - Se algo não bate, pausar e preparar rollback/diagnóstico; não ampliar escopo automaticamente.

5. **Receipt Brain**
   - Antes/depois.
   - IDs/handles.
   - Resultado do readback.
   - Screenshots/artefatos, quando houver.
   - Rollback disponível.
   - Pendências/follow-up.

## Resultado padrão

- `OK`: execução bate com approval packet; receipt salvo.
- `OK com ressalva`: execução bate, mas há QA/follow-up menor.
- `Divergente`: campo/objeto difere do aprovado; recomendar rollback ou correção escopada.
- `Bloqueado`: não foi possível ler fonte viva; não afirmar sucesso.

## Mensagem curta para Lucas

- Executado/verificado:
- Alvo:
- Readback:
- QA:
- Receipt:
- Pendência:
- Nenhuma ação fora do escopo aprovada foi executada.
