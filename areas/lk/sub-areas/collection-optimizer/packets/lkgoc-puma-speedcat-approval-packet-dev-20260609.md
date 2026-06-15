# Approval Packet — Puma Speedcat LKGOC DEV

Status: pronto para revisão em DEV, não Production.

## Preview
`https://lksneakers.com.br/collections/puma-speedcat?preview_theme_id=155065450718`

## Mudança proposta
Aplicar na coleção Puma Speedcat o padrão LKGOC/204L já aprovado:
- mesmo template base da collection 204L;
- mesmo shell visual escuro/premium;
- texto, imagens e FAQ adaptados para Puma Speedcat;
- guia pós-grid;
- sem linguagem pública de pronta entrega/estoque.

## Impacto esperado
- Melhor leitura editorial da coleção;
- melhora de SEO/GEO para `puma speedcat`, `puma speedcat original`, `puma speedcat feminino`, `puma speedcat vermelho`, `puma speedcat preto`;
- redução de ruído de copy antiga com estoque/entrega;
- experiência mobile mais próxima da 204L.

## Risco
Baixo no DEV. Para Production, risco visual moderado porque envolve tema/collection customer-facing.

## Rollback
Reverter snippet `snippets/lk-goc-collection.liquid`, section `sections/lk-collection.liquid` e template `templates/collection.puma-speedcat.json` para backups locais/estado anterior.

## Approval necessário
Aprovação explícita de Lucas para promover para Production após revisão visual mobile/desktop.

## Complemento de completude do approval packet — 2026-06-14

### Decisão solicitada / ação proposta
- Decisão solicitada: Lucas deve aprovar, ajustar ou bloquear explicitamente o packet `Approval Packet — Puma Speedcat LKGOC DEV` antes de qualquer execução sensível.
- Ação proposta: usar este documento apenas como approval packet/preview; execução só pode ocorrer no escopo exato aprovado e com receipt/readback posterior.

### Target / owner
- Target: `Approval Packet — Puma Speedcat LKGOC DEV` no caminho `areas/lk/sub-areas/collection-optimizer/packets/lkgoc-puma-speedcat-approval-packet-dev-20260609.md`.
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
