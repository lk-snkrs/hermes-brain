# Skill Surface Diet — proposta documental LKGOC (`lk-collection-optimizer`)

Data: 2026-06-29T10:33:04Z  
Escopo: proposta documental/read-only. **Nenhuma skill, config, toolset, profile, cron, gateway ou runtime foi alterado.**

## Interpretação do “Seguir”

Como Lucas pediu “Seguir” após a classificação read-only, a continuação segura é transformar o P0 `lk-collection-optimizer` em uma **proposta de superfície ideal por tiers**, não aplicar mudanças no profile.

## Fontes verificadas

- `profiles/lk-collection-optimizer/AGENTS.md`: fronteiras LKGOC, handoff Shopify/Stock, Honcho, Task OS e hygiene de credenciais.
- `areas/lk/sub-areas/collection-optimizer/MAPA.md`: identidade, fronteiras, fonte canônica e leitura mínima.
- `areas/lk/sub-areas/collection-optimizer/canon/INDEX.md`: ownership, ordem obrigatória de leitura e handoffs.
- `reports/governance/skill-surface-diet-classificacao-readonly-2026-06-29.md/.json`: 243 skills, 7 >=50k, 4 >=90k, P0 curadoria.
- `profiles/lk-collection-optimizer/skills/.usage.json`: uso histórico por skill; proxy, não prova utilidade/inutilidade.

## Diagnóstico

| Métrica | Valor | Leitura |
|---|---:|---|
| Skills no profile | 243 | superfície alta demais para especialista com fronteira estreita |
| Skills >=50k bytes | 7 | candidatas a proposta de split/baixo escopo |
| Skills >=90k bytes | 4 | custo potencial só quando carregadas |
| Uso observado no state.db do profile | 4 chamadas, 1 skill | histórico local ainda pouco representativo |
| Uso em `.usage.json` | alto para LK/SEO/Shopify | melhor proxy inicial, mas imperfeito |

## Proposta de superfície documental por tiers

### Tier 1 — Core LKGOC mínimo

Candidatas a superfície primária. **Não é alteração aplicada.**

| Skill | Uso/view | Por quê |
|---|---:|---|
| `lk-superpowers-collection-optimizer` | 5/4 | Identidade/rotina principal do profile LKGOC. |
| `lk-collection-patterns` | 119/119 | Padrões de collection page e Guia LK; alto uso histórico. |
| `lk-shopify-readonly` | 214/207 | Consulta segura/read-only Shopify quando necessária para coleção/catalog evidence. |
| `multiempresa-routing-lucas` | 231/127 | Evita contaminação Zipper/SPITI/Growth e preserva fronteiras multiempresa. |
| `verification-before-completion` | 75/71 | Gate antes de declarar LKGOC concluído/passando. |

### Tier 2 — Lentes LKGOC sob demanda obrigatória por tipo de tarefa

#### SEO/GEO de collection, Guia LK, FAQ/schema, AI Visibility

| Skill | Uso/view | Quando carregar |
|---|---:|---|
| `seo-page` | 11/7 | Aplicar quando a tarefa envolver title/meta/H1/canonical/schema/on-page de coleção. |
| `seo-content` | 14/10 | Aplicar para estrutura, E-E-A-T, helpfulness, entidade LK e legibilidade IA. |
| `seo-ecommerce` | 18/11 | Aplicar para collection/PDP/listing e Product/Collection/ItemList/FAQPage. |
| `seo-geo` | 38/35 | Aplicar para AI Overview/AEO/citabilidade e FAQ extractable. |
| `seo-schema` | 6/6 | Aplicar para JSON-LD/FAQPage/ItemList/schema validation. |
| `seo-dataforseo` | 8/8 | Usar somente quando SERP/PAA/concorrentes live forem necessários. |

#### Conteúdo/Guia LK sob demanda

| Skill | Uso/view | Quando carregar |
|---|---:|---|
| `blog-brief` | 2/2 | Brief/estrutura quando a tarefa virar Guia LK/source page. |
| `blog-write` | 3/3 | Redação longa somente quando pedido/escopo exigir. |
| `blog-rewrite` | 1/1 | Melhorar texto existente. |
| `blog` | 4/4 | Umbrella blog apenas para tarefa editorial ampla. |
| `blog-schema` | 0/0 | Schema de conteúdo quando não coberto por seo-schema. |
| `blog-factcheck` | 0/0 | Checagem de claims/citações. |
| `blog-image` | 1/1 | Brief de assets SEO/OG/hero quando a tarefa pedir; produção/uso real de imagem depende de fonte aprovada/approval. |

#### Governança/execução local sob demanda

| Skill | Uso/view | Quando carregar |
|---|---:|---|
| `brainstorming` | 7/7 | Antes de LKGOC não-trivial. |
| `executing-plans` | 12/12 | Quando houver plano de execução. |
| `hermes-brain-governance` | 0/0 | Quando mexer em Brain docs/receipts/governança. |
| `hermes-agent` | 1/1 | Somente para configurar/troubleshoot Hermes. |
| `honcho-memory-operations` | 0/0 | Somente ao investigar/configurar/avaliar Honcho. |
| `doppler-secrets-operations` | 363/272 | Somente se houver credencial/integração/secret hygiene. |
| `hermes-central-integration-auth-broker` | 0/0 | Somente quando integração CLI/MCP estiver no escopo. |

#### Handoff obrigatório / não execução LKGOC

| Skill | Uso/view | Quando carregar |
|---|---:|---|
| `lk-shopify-product-upload` | 16/16 | Quando surgir produto novo/listagem: handoff para lk-shopify, não executar no LKGOC. |
| `shopify` | 0/0 | Política/consulta Admin read-only via CLI oficial quando necessário; mutation segue bloqueada. |
| `lk-growth-operations` | 132/132 | Growth amplo/GA4/GSC/GMC/paid/influencer/PageSpeed fora de collection: handoff. |
| `lk-seo-weekly-improvement` | 257/246 | Consulta/handoff Growth para SEO/CRO/GEO amplo, não core LKGOC. |
| `lk-operational-intelligence` | 292/288 | Dados operacionais LK sob demanda; estoque/disponibilidade continua handoff para lk-stock. |

## Candidatas a fora do core LKGOC

Estas não devem desaparecer automaticamente; recomendação é não ficarem como superfície primária. Remoção/arquivamento só com approval específico.

| Skill | Motivo |
|---|---|
| `pytorch-fsdp` | ML training; 160k bytes; sem relação direta com LKGOC. |
| `research-paper-writing` | Paper acadêmico; gigante; sem relação direta com coleção LK. |
| `bruno-openclaw-hermes-brain-adaptation` | Governança/Brain ampla; sob demanda, não superfície primária LKGOC. |
| `mission-control-development` | Produto Mission Control; fora de collection optimizer. |
| `claude-code` | Coding agent; só se houver tarefa de código aprovada. |
| `airtable` | Produtividade externa; não LKGOC por padrão. |
| `apple-notes` | Pessoal/Apple; fora de LKGOC. |
| `ascii-art` | Criativo irrelevante para otimização de coleção. |
| `audiocraft-audio-generation` | Áudio/ML; fora de LKGOC. |
| `pokemon-player` | Gaming; fora de LKGOC. |

## Skills gigantes — tratamento recomendado

| Skill | Tamanho observado | Ação segura |
|---|---:|---|
| `pytorch-fsdp` | 160,170 bytes | fora do core; não splitar aqui, apenas propor baixa de superfície se houver approval futuro |
| `research-paper-writing` | 103,375 bytes | fora do core; manter arquivada/sob demanda |
| `lk-operational-intelligence` | 100,458 bytes | sob demanda para evidência operacional LK; não core LKGOC |
| `lk-seo-weekly-improvement` | 98,163 bytes | handoff/consulta Growth; proposta futura de split se continuar carregada |
| `bruno-openclaw-hermes-brain-adaptation` | 88,352 bytes | governança ampla; sob demanda |
| `hermes-agent` | 50,850 bytes | suporte Hermes; não carregar em tarefa LKGOC trivial |

## Regra proposta de roteamento

- **LKGOC core:** coleção, Guia LK, FAQ/schema de collection, scorecard, evidence packet, QA visual/editorial, DEV preview/handoff.
- **Handoff LK Growth:** SEO técnico amplo, GA4/GSC/GMC, paid, influencer, PageSpeed, AI visibility fora de collection.
- **Handoff LK Shopify:** product upload/listagem, PDP/theme geral, metafields/tags/deploy técnico.
- **Handoff LK Stock:** estoque, disponibilidade, grade/tamanho, Tiny/Shopify stock.

## QA independente

QA inicial marcou **FAIL antes de patch** porque o primeiro draft chamava coisas demais de “always-on”: blog-write/blog-image, Shopify/upload, Honcho/Doppler/broker/governança. Patches aplicados: seção virou tiers; core mínimo reduzido; SEO/blog viraram lentes sob demanda; auth/secrets/Honcho/governança viraram suporte sob demanda; Shopify/upload virou handoff/on-demand; claims “obrigatório” foram condicionados ao tipo de tarefa.

## Próxima decisão possível

Se Lucas quiser aplicar depois, criar **approval packet A2** para mudança real de surface/config do profile, com backup/readback/rollback. Até lá, esta proposta serve só como checklist manual para o agente escolher skills com menos ruído.

## Não realizado

- Nenhuma skill editada, movida, arquivada ou deletada.
- Nenhum `config.yaml`, toolset, profile ou runtime alterado.
- Nenhum cron/gateway/Docker/VPS tocado.
- Nenhuma credencial lida/impressa.
- Nenhum write externo ou mutação Shopify/Tiny/GMC/Klaviyo/etc.

## Limitações

- `.usage.json` e `state.db` são proxies; baixo uso não prova inutilidade.
- Algumas skills “sob demanda” podem ser obrigatórias em tarefas específicas por regra de sistema/AGENTS.
- Bytes de `SKILL.md` não medem custo real se a skill não for carregada.
