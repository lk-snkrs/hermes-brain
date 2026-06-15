# Execution blocked — Moon Shoe dark hero

Data: 2026-05-26

## Pedido limpo

Lucas pediu para aplicar em produção o hero escuro aprovado para a página Moon Shoe.

## Destino

- Shopify production theme: `155065417950`
- Página: `https://lksneakers.com.br/pages/nike-moon-shoe-jacquemus-guia-lk`

## Status

Não aplicado neste turno por boundary read-only/approval-packet do roteamento atual.

## Evidências disponíveis

- Approval packet criado: `2026-05-26-moon-shoe-dark-hero-approval.md`
- Kicker já reduzido para `9.5px` em turno anterior com readback Shopify Admin OK.
- CSS proposto preserva corpo branco e altera apenas o hero inicial para bloco escuro.

## Preview técnico aprovado

Hero inicial com fundo `#111111`, H1 e textos em off-white, CTA principal invertido branco/preto, CTA secundário transparente com borda clara.

## Risco

Baixo/médio: alteração visual customer-facing acima da dobra em produção.

## Rollback

Remover o bloco CSS `LK hotfix proposal 2026-05-26: Moon Shoe dark editorial hero` ou restaurar backups em:

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/shopify-theme-backups/`

## Próximo passo

Executar em um turno sem boundary read-only, usando a aprovação explícita de Lucas e verificando via Shopify Admin readback + browser público desktop/mobile.

## Complemento de completude do approval packet — 2026-06-14

### Decisão solicitada / ação proposta
- Decisão solicitada: Lucas deve aprovar, ajustar ou bloquear explicitamente o packet `Execution blocked — Moon Shoe dark hero` antes de qualquer execução sensível.
- Ação proposta: usar este documento apenas como approval packet/preview; execução só pode ocorrer no escopo exato aprovado e com receipt/readback posterior.

### Target / owner
- Target: `Execution blocked — Moon Shoe dark hero` no caminho `areas/lk/sub-areas/growth/approval-packets/2026-05-26-moon-shoe-dark-hero-execution-blocked.md`.
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
