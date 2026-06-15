# Approval packet — Guias editoriais Adidas Samba e Onitsuka Tiger Mexico 66

## Diagnóstico

Os guias estão atualmente dentro das próprias páginas de coleção, como seção pós-grid, com links de âncora:

- Adidas Samba: `https://lksneakers.com.br/collections/adidas-samba#lk-guia-adidas-samba`
- Onitsuka Tiger Mexico 66: `https://lksneakers.com.br/collections/onitsuka-tiger-mexico-66#lk-guia-onitsuka-tiger-mexico-66`

Isso não atende completamente ao pedido de criar um guia editorial separado para adicionar na coleção via link.

## Drafts preparados localmente

- `adidas-samba-guia-editorial.md`
- `onitsuka-tiger-mexico-66-guia-editorial.md`

## Publicação necessária

Criar duas páginas Shopify em produção:

- `/pages/guia-adidas-samba`
- `/pages/guia-onitsuka-tiger-mexico-66`

Depois, atualizar o CTA das coleções para apontar para essas páginas, em vez da âncora interna.

## Aprovação necessária

Requer aprovação explícita de produção porque envolve:

- criação de páginas visíveis no Shopify;
- alteração de links visíveis nas coleções em produção.

## Rollback proposto

- Remover/ocultar as duas páginas criadas; ou
- Reverter o CTA das coleções para as âncoras atuais:
  - `#lk-guia-adidas-samba`
  - `#lk-guia-onitsuka-tiger-mexico-66`

## Próximo passo

Se Lucas aprovar, publicar as duas páginas e trocar os CTAs das coleções para os slugs finais.

## Complemento de completude do approval packet — 2026-06-14

### Decisão solicitada / ação proposta
- Decisão solicitada: Lucas deve aprovar, ajustar ou bloquear explicitamente o packet `Approval packet — Guias editoriais Adidas Samba e Onitsuka Tiger Mexico 66` antes de qualquer execução sensível.
- Ação proposta: usar este documento apenas como approval packet/preview; execução só pode ocorrer no escopo exato aprovado e com receipt/readback posterior.

### Target / owner
- Target: `Approval packet — Guias editoriais Adidas Samba e Onitsuka Tiger Mexico 66` no caminho `areas/lk/sub-areas/growth/approval-packets/collection-guides-20260526-124324/APPROVAL-PACKET.md`.
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
