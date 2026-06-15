# Receipt / approval packet — Correções produção coleção New Balance 204L

Data: 2026-05-27
Status: aprovado por Lucas no Telegram; execução externa pendente de ferramenta Shopify Admin no runtime atual
URL: https://lksneakers.com.br/collections/new-balance-204l

## Pedido aprovado

Lucas aprovou aplicar em produção as correções na página de coleção New Balance 204L:

1. Título/H1: `New Balance 204L` — aumentar fonte em 3pt.
2. Subtítulo/kicker: remover duplicação do nome da coleção.
   - De: `CURADORIA LK · NEW BALANCE 204L`
   - Para: `CURADORIA LK`
3. Paginação/grid: mudar de 24 para 20 produtos por página.

## Evidência pública antes da execução

Inspeção pública em `https://lksneakers.com.br/collections/new-balance-204l?hermes_qa=20260527`:

- H1 detectado: `New Balance 204L`
- Fonte H1 detectada via computed style: `48px`
- Kicker visível: `CURADORIA LK · NEW BALANCE 204L`
- Produtos renderizados na primeira página: 24
- Total da coleção visível: 32 itens

## Correção canônica para o template

- H1 deve ficar dominante e limpo.
- Se o H1 já contém o nome da coleção, o kicker não repete o nome.
- Coleções produto-first usam 20 produtos por página como padrão, salvo exceção aprovada.

## Escopo autorizado

Pode alterar apenas o necessário para esta coleção/padrão:

- collection template/section responsável pelo hero/kicker da coleção 204L;
- configuração de paginação para coleção produto-first/204L;
- CSS/setting do H1 para +3pt.

## Fora de escopo

Não autorizado neste approval:

- mudar preço, estoque, produto, imagens, ordem comercial, filtros, menus, campanhas, Klaviyo, Meta/Google Ads ou qualquer página fora do padrão 204L sem nova aprovação.

## Rollback

Antes de aplicar no Shopify production, salvar backup do asset/theme setting atual. Rollback é re-aplicar o asset/settings anteriores e verificar:

- H1 volta ao tamanho anterior;
- kicker volta ao texto anterior;
- paginação volta a 24.

## QA pós-write obrigatório

- Readback do asset/settings alterado.
- Abrir URL pública com cachebuster.
- Confirmar H1 `New Balance 204L` com fonte aproximadamente 3pt maior que o baseline atual.
- Confirmar kicker `CURADORIA LK` sem `NEW BALANCE 204L`.
- Confirmar primeira página com 20 produtos.

## Complemento de completude do approval packet — 2026-06-14

### Decisão solicitada / ação proposta
- Decisão solicitada: Lucas deve aprovar, ajustar ou bloquear explicitamente o packet `Receipt / approval packet — Correções produção coleção New Balance 204L` antes de qualquer execução sensível.
- Ação proposta: usar este documento apenas como approval packet/preview; execução só pode ocorrer no escopo exato aprovado e com receipt/readback posterior.

### Target / owner
- Target: `Receipt / approval packet — Correções produção coleção New Balance 204L` no caminho `areas/lk/sub-areas/growth/approval-packets/colecao-204l-correcao-production-2026-05-27.md`.
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
