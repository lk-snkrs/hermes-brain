# Auditoria — SOUL/docs/runtime do `[LK] Otimização de Coleções`

Data: 2026-06-25
Escopo: verificação read-only de SOUL, docs canônicos do Brain e sinais de runtime/profile local.
Writes externos: 0

## Verificado

Arquivos centrais lidos:

- `SOUL.md`
- `AGENTS.md`
- `MAPA.md`
- `TOOLS.md`
- `MEMORY.md`
- `HEARTBEAT.md`
- `references/ownership-and-handoff-20260606.md`
- `rules/REGRA-LKGOC-CLAUDE-SEO-COMO-CAMADA-DE-APOIO.md`
- `standards/LKGOC-GUIA-LK-EDITORIAL-LOGIC-204L.md`
- `policies/SHOPIFY-GITHUB-FIRST-NO-ADMIN-WRITES.md`
- `playbooks/shopify-collections-standardization-lkgoc.md`
- `projetos/lkgoc-collection-optimizer/README.md`
- `projetos/lkgoc-collection-optimizer/DECISIONS_AND_GUARDRAILS.md`
- profile local: `/opt/data/home/.hermes/profiles/lk-collection-optimizer/MEMORY.md`

## Resultado curto

A documentação Brain do LKGOC está majoritariamente correta quanto a ownership e fronteiras: o agente é dono de LKGOC/coleções/Guia LK/QA, enquanto Growth, Shopify e Stock são pares/handoffs.

Há, porém, dois problemas importantes:

1. **Runtime/prompt ativo incompatível:** a sessão carregou instrução de developer intitulada `LK Growth OS — Hermes Specialist`, com escopo amplo de GA4/GSC/GMC/CRO/Growth. Isso contradiz o profile ativo `lk-collection-optimizer` e explica respostas contaminadas por Growth.
2. **Skill local esperada não aparece no profile:** o documento `agentic-os/FASE-1B...` diz que a skill local do profile deveria refletir o OS, mas no profile local foi encontrado apenas `MEMORY.md`. Não foi encontrada skill local LKGOC sob `/opt/data/home/.hermes/profiles/lk-collection-optimizer/`.

## Estado por área

| Área | Status | Evidência |
|---|---|---|
| Ownership LKGOC | OK | `SOUL.md`, `MAPA.md`, `MEMORY.md`, `AGENTS.md` dizem que `[LK] Otimização de Coleções` é dono do LKGOC. |
| Growth | OK no Brain; risco no runtime | Brain roteia sinais/priorização/SEO-GEO amplo para `LK Growth`. Runtime atual injeta persona Growth. |
| Stock | OK | `AGENTS.md` e Guia LK proíbem consulta direta de estoque e exigem handoff para `lk-stock`. |
| Shopify | Parcial/OK com nuance | Brain define Shopify como par/handoff técnico. Política GitHub-first proíbe writes diretos via Admin API. |
| CRO | OK com fronteira | CRO geral não é dono do LKGOC; LKGOC só cuida de experiência de collection/template/guia. |
| Production writes | OK | Docs exigem DEV/branch/readback/approval; sem production/main sem aprovação. |
| Padrão visual | OK | Gold Source 204L, shared shell, não inventar layout, pós-grid após todos os produtos. |
| Runtime/profile local | NÃO OK | Instrução ativa é Growth; profile local não tem skill LKGOC encontrada. |
| Memória injetada | Risco | Contexto Honcho trouxe dados Zipper/order/pessoais irrelevantes para este profile; deve ser ignorado/higienizado. |

## Correção recomendada

1. Ajustar a SOUL/prompt executável do profile `lk-collection-optimizer` para começar como `[LK] Otimização de Coleções / LKGOC`, não `LK Growth OS`.
2. Criar/instalar skill local LKGOC no profile, refletindo `SOUL.md`, `MAPA.md`, regras e playbooks.
3. Adicionar teste/smoke de boot: se `Active Hermes profile = lk-collection-optimizer`, a primeira linha de identidade não pode conter `Growth OS` como papel principal.
4. Higienizar Honcho/auto-context para este profile: não injetar memórias Zipper/order/customer em LKGOC, salvo pedido explícito multiempresa.
5. Manter Brain docs como fonte canônica; não mover ownership para Growth/Shopify.

## Veredito

**Não está 100% correto em runtime.**

A documentação canônica do Brain está alinhada com a decisão do Lucas, mas a SOUL/prompt efetivamente carregada nesta conversa está contaminada por Growth. Isso deve ser corrigido antes de considerar o agente operacionalmente confiável como Collection Optimizer puro.
