# SUPERSEDED — NÃO EXECUTAR

Este packet foi invalidado pelo Lucas em 2026-06-05 porque propunha subir snippets legados `lk-samba-204l-*`.

Correção correta: usar namespace canônico `lk-goc-*` e render `lk-goc-adidas-samba` com `part: hero`/`part: guide`.

---

# Approval packet — hotfix Production Adidas Samba LKGOC missing snippets

Data: 2026-06-05T18:25:29

## Problema reportado
URL production: `https://lksneakers.com.br/collections/adidas-samba?readmore_fix=1`

Erro visível: `Liquid error (sections/lk-collection line ...): Could not find asset snippets/lk-samba-204l-hero-v2.liquid`.

## Diagnóstico read-only
Tema Production `155065417950`:
- `sections/lk-collection.liquid`: existe e renderiza `lk-samba-204l-hero-v2` e `lk-samba-204l-guide-v2` para `collection.handle == 'adidas-samba'`.
- `snippets/lk-samba-204l-hero-v2.liquid`: AUSENTE.
- `snippets/lk-samba-204l-guide-v2.liquid`: AUSENTE.

Tema DEV `155065450718`:
- `snippets/lk-samba-204l-hero-v2.liquid`: presente.
- `snippets/lk-samba-204l-guide-v2.liquid`: presente.

## Hotfix proposto
Copiar do DEV para Production apenas estes dois snippets:
- `snippets/lk-samba-204l-hero-v2.liquid`
- `snippets/lk-samba-204l-guide-v2.liquid`

Sem alterar `sections/lk-collection.liquid`, preços, produtos, coleção, campanha ou checkout.

## Impacto esperado
- Remover erro Liquid visível em production.
- Restaurar Hero e guia LKGOC da coleção Adidas Samba.

## Risco
Baixo/médio: write em production, mas escopo restrito a dois snippets ausentes já referenciados pelo section live.

## Rollback
Remover os dois snippets de production ou restaurar estado anterior (ausência), se houver regressão — embora isso volte a exibir o erro Liquid.

## Evidências locais
- Workdir: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/adidas-samba-production-missing-snippet-20260605`
- Production pull: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/adidas-samba-production-missing-snippet-20260605/prod`
- DEV source: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/work/adidas-samba-production-missing-snippet-20260605/dev`

## Complemento de completude do approval packet — 2026-06-14

### Decisão solicitada / ação proposta
- Decisão solicitada: Lucas deve aprovar, ajustar ou bloquear explicitamente o packet `SUPERSEDED — NÃO EXECUTAR` antes de qualquer execução sensível.
- Ação proposta: usar este documento apenas como approval packet/preview; execução só pode ocorrer no escopo exato aprovado e com receipt/readback posterior.

### Target / owner
- Target: `SUPERSEDED — NÃO EXECUTAR` no caminho `areas/lk/sub-areas/growth/approval-packets/adidas-samba-production-missing-snippets-hotfix-20260605.md`.
- Owner operacional: LK Growth / GMC / SEO-CRO, com governança Hermes Geral e aprovação final Lucas.

### Escopo permitido
- Escopo permitido somente após aprovação explícita: executar apenas os itens, IDs, fluxos, mensagens, campos, coleções, arquivos ou rotinas descritos neste packet, sem ampliar alvo por inferência.
- Pode fazer localmente sem nova aprovação: validação documental, preview, auditoria read-only, receipt e classificação de blockers.

### O que continua bloqueado
- Não pode fazer Merchant/Shopify/Tiny/feed/campanha/cliente/fornecedor, preço, estoque, tema, anúncios ou envio externo fora do escopo exato aprovado.
- Aprovação genérica como `seguir`, `fazer tudo` ou contexto antigo não amplia escopo; novo alvo exige novo approval packet.

### Risco
- Risco principal: transformar preview/packet em autorização ampla e executar ação sensível fora do escopo exato.
- Mitigação: fail-closed, approval textual específica, backup/snapshot quando aplicável, readback e receipt com contagens.

### Rollback
- Rollback obrigatório: reverter somente a alteração aprovada usando backup/snapshot/artefato anterior quando aplicável; se a ação foi apenas preview/read-only, rollback é manter sem execução e registrar o bloqueio.
- Qualquer rollback que toque sistema externo exige o mesmo escopo aprovado, readback e receipt.

### Verificação / readback
- Verificação obrigatória: readback da fonte afetada quando aplicável, comparação com preview/CSV/JSON, contagem de aplicados/bloqueados/divergentes e receipt com `values_printed=false`.
- Se houver divergência de identidade, fonte, escopo ou aprovação, bloquear execução e registrar causa sanitizada.

### Opções de aprovação
- Aprovar exatamente o escopo descrito neste packet.
- Aprovar apenas preview/dry-run/read-only.
- Ajustar alvo/limite antes de executar.
- Bloquear execução e manter como histórico/rascunho.

### Secret hygiene
- Usar credenciais somente via Doppler/wrapper seguro quando houver integração; não imprimir tokens, refresh tokens, passwords, service-account JSON, API keys ou connection strings.
- Relatórios e receipts devem manter `values_printed=false` e redigir qualquer valor sensível como `[REDACTED]`.
