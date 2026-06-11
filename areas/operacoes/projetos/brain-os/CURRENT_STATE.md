# Brain OS — Current State

**Atualizado em:** 2026-06-11T13:55:54.899501+00:00
**Modo:** local/documental + GitHub docs-as-code
**Última publicação base:** PR #144 merged em `main` (`cb4a31e`)
**Runtime:** não tocado

## Estado atual

Brain OS v1 está publicado como camada de organização canônica sobre o Brain existente. O pós-merge mudou a prioridade: o scanner já cobre os principais hubs, então a melhoria mais valiosa agora é maturidade/qualidade, não criar hubs duplicados.

## Evidência publicada pós-merge

- Repo publicado: `lk-snkrs/hermes-brain`.
- Branch base reconciliada: `main`.
- HEAD verificado antes desta evolução: `cb4a31e`.
- Scanner publicado: `reports/governance/brain-os/brain-os-candidates-latest.json`.
- Scanner version: `brain-os-v1`.
- Candidatos no scanner: `53`.
- Hub manifests publicados no pacote PR #144: todos com pacote mínimo esperado conforme validação local da onda.

## Estado lógico

- **Hubs canônicos:** vivem nas áreas donas (`areas/lk/...`, `areas/operacoes/...`, `areas/zipper/...`, `areas/spiti/...`).
- **Core Brain OS:** vive aqui em `areas/operacoes/projetos/brain-os/`.
- **Receipts/backups/reports:** são evidência, não hubs vivos, salvo promoção explícita.
- **Fonte viva externa:** Tiny, Shopify, GMC, Meta, Klaviyo, Chatwoot, Supabase etc. vencem snapshots/documentos quando a pergunta depende de estado atual.

## Próxima regra operacional

Novas frentes de alto volume devem receber hub canônico antes de novas expansões de agentes, crons ou rotinas. Se o scanner estiver limpo, priorizar:

1. qualidade de hubs existentes;
2. status executivo;
3. semântica de manifests/artefatos;
4. scanner com melhor classificação;
5. só depois novos hubs.
