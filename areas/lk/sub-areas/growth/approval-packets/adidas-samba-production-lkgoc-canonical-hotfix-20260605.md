# Approval packet — Adidas Samba Production LKGOC canonical hotfix

Data: 2026-06-05T18:36:19

## Correção de rota
O packet anterior que sugeria subir `lk-samba-204l-*` foi marcado como **SUPERSEDED — NÃO EXECUTAR**.

Lucas corrigiu corretamente: Adidas Samba deve seguir o padrão padronizado **LK-GOC**, não snippets legados `lk-samba-204l-*`.

## Problema atual em Production
URL: `https://lksneakers.com.br/collections/adidas-samba?readmore_fix=1`

O tema Production `155065417950` está com `sections/lk-collection.liquid` renderizando nomes antigos:
- `lk-samba-204l-hero-v2`
- `lk-samba-204l-guide-v2`

Esses snippets estão ausentes em Production, causando Liquid error visível.

## Correção correta proposta
1. Subir o snippet canônico do DEV para Production:
   - `snippets/lk-goc-adidas-samba.liquid`
2. Alterar Production `sections/lk-collection.liquid` somente nos renders da Adidas Samba:
   - Hero: `render 'lk-goc-adidas-samba', part: 'hero'`
   - Guide: `render 'lk-goc-adidas-samba', part: 'guide'`
3. Não subir `lk-samba-204l-*`.

## Arquivos candidatos preparados
- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/adidas-samba-production-lkgoc-correct-20260605/candidate/sections/lk-collection.liquid`
- `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/adidas-samba-production-lkgoc-correct-20260605/candidate/snippets/lk-goc-adidas-samba.liquid`

## Validações locais do candidate
- refs antigas no section candidato: `0`
- refs novas `lk-goc-adidas-samba`: `2`
- snippet canônico presente e com comentário: `Namespace: lk-goc-* only`

## Escopo
- Production theme write: sim, exige aprovação explícita do Lucas.
- Sem alteração de preço/produto/checkout/campanha/metafields.
- Correção restrita a Liquid/snippet da coleção Adidas Samba.

## Rollback
- Restaurar `sections/lk-collection.liquid` a partir de `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/adidas-samba-production-lkgoc-correct-20260605/prod/sections/lk-collection.liquid`.
- Remover/ignorar `snippets/lk-goc-adidas-samba.liquid` se necessário.

## QA pós-apply obrigatório
- URL production sem `Liquid error`.
- Hero renderizando `.lk-goc-coll-preview--adidas-samba`.
- Guia renderizando `#lk-guia-adidas-samba` / `.lk-goc-guide-panel`.
- `.coll-rich-content` legado ausente se coleção estiver optimized.
- Desktop: “Ler mais” não visível se regra LKGOC desktop se aplicar ao componente.
- Screenshot desktop/mobile.

## Complemento de completude do approval packet — 2026-06-14

### Decisão solicitada / ação proposta
- Decisão solicitada: Lucas deve aprovar, ajustar ou bloquear explicitamente o packet `Approval packet — Adidas Samba Production LKGOC canonical hotfix` antes de qualquer execução sensível.
- Ação proposta: usar este documento apenas como approval packet/preview; execução só pode ocorrer no escopo exato aprovado e com receipt/readback posterior.

### Target / owner
- Target: `Approval packet — Adidas Samba Production LKGOC canonical hotfix` no caminho `areas/lk/sub-areas/growth/approval-packets/adidas-samba-production-lkgoc-canonical-hotfix-20260605.md`.
- Owner operacional: LKGOC / LK Growth, com governança Hermes Geral e aprovação final Lucas.

### Escopo permitido
- Escopo permitido somente após aprovação explícita: executar apenas os itens, IDs, fluxos, mensagens, campos, coleções, arquivos ou rotinas descritos neste packet, sem ampliar alvo por inferência.
- Pode fazer localmente sem nova aprovação: validação documental, preview, auditoria read-only, receipt e classificação de blockers.

### O que continua bloqueado
- Não pode fazer Shopify/theme production write, publish, alteração de coleção pública, sort automático, Liquid/snippet/theme, preço, estoque, campanha ou envio externo fora do escopo aprovado.
- Aprovação genérica como `seguir`, `fazer tudo` ou contexto antigo não amplia escopo; novo alvo exige novo approval packet.

### Risco
- Risco principal: transformar preview/packet em autorização ampla e executar ação sensível fora do escopo exato.
- Mitigação: fail-closed, approval textual específica, backup/snapshot quando aplicável, readback e receipt com contagens.

### Rollback
- Rollback obrigatório: reverter somente a alteração aprovada usando backup/snapshot/artefato anterior quando aplicável; se a ação foi apenas preview/read-only, rollback é manter sem execução e registrar o bloqueio.
- Qualquer rollback que toque sistema externo exige o mesmo escopo aprovado, readback e receipt.

### Verificação / readback
- Verificação obrigatória: preview/readback do artefato/coleção afetada, comparação com baseline quando aplicável, contagem de arquivos/coleções alteradas e receipt com zero execução externa não aprovada.
- Se houver divergência de identidade, fonte, escopo ou aprovação, bloquear execução e registrar causa sanitizada.

### Opções de aprovação
- Aprovar exatamente o escopo descrito neste packet.
- Aprovar apenas preview/dry-run/read-only.
- Ajustar alvo/limite antes de executar.
- Bloquear execução e manter como histórico/rascunho.

### Secret hygiene
- Usar credenciais somente via Doppler/wrapper seguro quando houver integração; não imprimir tokens, refresh tokens, passwords, service-account JSON, API keys ou connection strings.
- Relatórios e receipts devem manter `values_printed=false` e redigir qualquer valor sensível como `[REDACTED]`.
