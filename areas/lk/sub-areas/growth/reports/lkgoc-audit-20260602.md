# Audit LKGOC — 2026-06-02

## Veredito

O LKGOC tinha problemas reais de governança e execução que explicam o LK Growth criar coleções fora do padrão aprovado.

O erro principal não é a ideia do padrão: é a forma como ele estava espalhado entre documentos, com regras antigas ainda concorrendo com correções novas, e com o profile `lk-growth` sem uma `SKILL.md` própria para `lk-superpowers-collection-optimizer` — existe apenas um `README.md` ponteiro.

## Achados críticos

### A1 — Nome errado no documento canônico

- Antes: `LKGOC-PADRAO-CANONICO.md` dizia `LK Growth Organic Collection`.
- Correto: `LK Growth Optimized Collection`.
- Risco: o agente pode tratar LKGOC como conceito editorial/orgânico genérico, não como pacote operacional completo.
- Status: corrigido no canônico.

### A2 — Fonte única de verdade não estava na primeira posição da skill

- A skill listava vários documentos canônicos, mas não abria com `LKGOC-PADRAO-CANONICO.md` como prioridade absoluta.
- Risco: o agente pode seguir `PADRAO-CANONICO-GUIA-E-COLECAO-LK.md`, `PADRAO-LK-COLLECTION-V2.md` ou regras antigas e ignorar correções recentes de Lucas.
- Status: corrigido na skill do Brain; agora a primeira regra é abrir `LKGOC-PADRAO-CANONICO.md` e tratar divergências como obsoletas.

### A3 — Contradição de tamanho do texto hero

- Regra antiga ainda ativa: primeiro parágrafo 350–450 caracteres.
- Correção Lucas: primeiro bloco/parágrafo hero LKGOC deve ter 500–700 caracteres.
- Risco: Adidas Samba Jane e outras coleções saem com texto curto, sem densidade narrativa/SEO/GEO.
- Status: corrigido na skill, checklist e regra de criação de texto.

### A4 — Regras visuais recentes não estavam concentradas no canônico

O canônico não explicitava no topo os gates que mais causam reprovação:

- hero/topo escuro/preto quando padrão LKGOC visual é aplicado;
- guia dedicado sempre no shell Moon Shoe;
- coleção + guia como pacote único;
- pesquisa na internet antes de escrever;
- FAQ único;
- CTA claro + botão escuro com fonte branca;
- preview Shopify DEV obrigatório;
- QA visual desktop + mobile com screenshot.

Status: adicionados como `Gates executivos obrigatórios — não negociar` em `LKGOC-PADRAO-CANONICO.md`.

### A5 — Profile LK Growth não tem a skill LKGOC como SKILL.md carregável

Evidência read-only:

- `/opt/data/profiles/lk-growth/skills/lk-superpowers-collection-optimizer/README.md` existe.
- `/opt/data/profiles/lk-growth/skills/lk-superpowers-collection-optimizer/SKILL.md` não existe.

Risco provável: quando o agente LK Growth roda dentro do profile próprio, ele pode não carregar `lk-superpowers-collection-optimizer` como skill Hermes normal; pode cair em skills antigas como `lk-seo-weekly-improvement`/`lk-collection-patterns`, que têm histórico de padrões anteriores e exceções.

Status: não corrigido automaticamente porque isso altera skill de outro profile (`lk-growth`). Recomendação: criar/sincronizar uma `SKILL.md` curta no profile LK Growth apontando para o Brain canônico, ou instalar a skill canônica no diretório de skills do profile.

### A6 — Skill antiga `lk-seo-weekly-improvement` ainda contém memória de padrão off-white/hero claro

Evidência encontrada no profile `lk-growth`: a skill `lk-seo-weekly-improvement` ainda tem pitfall antigo dizendo que, em certos previews de collection, preferir `off-white hero`/hierarquia limpa após rejeição de um `heavy black hero`.

Risco: para Samba Jane, o agente pode estar obedecendo essa memória antiga em vez da correção mais nova de Lucas: 204L/Moon Shoe com hero preto/escuro como padrão LKGOC.

Status: não alterado por enquanto porque é skill de outro profile. A correção segura é acrescentar uma regra de override: “para LKGOC, `LKGOC-PADRAO-CANONICO.md` vence qualquer pitfall antigo de off-white/hero claro”.

## Correções já aplicadas no Brain

Arquivos modificados localmente:

1. `LKGOC-PADRAO-CANONICO.md`
   - corrigiu `Organic` → `Optimized`;
   - adicionou 12 gates executivos obrigatórios.

2. `skills/lk-superpowers-collection-optimizer/SKILL.md`
   - colocou `LKGOC-PADRAO-CANONICO.md` como primeira fonte obrigatória;
   - adicionou regra de conflito;
   - atualizou texto hero para 500–700 caracteres.

3. `skills/lk-superpowers-collection-optimizer/checklists/qa-checklist.md`
   - atualizou QA do primeiro parágrafo/bloco hero para 500–700 caracteres.

4. `rules/PADRAO-CRIACAO-TEXTO-COLECOES-SEO-GEO-LK.md`
   - marcou a régua antiga 350–450 como obsoleta para LKGOC final.

## Próximo passo recomendado

Para resolver a execução do agente LK Growth de verdade, aplicar um patch no profile `lk-growth`:

1. Criar `/opt/data/profiles/lk-growth/skills/lk-superpowers-collection-optimizer/SKILL.md` como skill carregável Hermes, apontando para o Brain canônico e repetindo apenas os 12 gates executivos.
2. Patch em `/opt/data/profiles/lk-growth/skills/productivity/lk-seo-weekly-improvement/SKILL.md` para inserir override explícito: em LKGOC, o canônico vence padrões antigos como off-white hero.
3. Verificar com inventário de skills do profile que `lk-superpowers-collection-optimizer` aparece carregável.

## Critério de aceite para Adidas Samba Jane

Uma nova tentativa da Adidas Samba Jane só passa se entregar:

- coleção no contrato visual 204L;
- guia dedicado no shell Moon Shoe;
- pesquisa web/SERP e fontes internacionais reconhecíveis;
- texto hero 500–700 chars;
- FAQ único;
- CTA claro + botão escuro/branco;
- preview Shopify DEV com link direto;
- screenshots desktop/mobile;
- approval packet único coleção + guia;
- produção somente após aprovação explícita.
