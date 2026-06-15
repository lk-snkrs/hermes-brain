# Approval packet — Padrão LK para coleções produto-first

Data: 2026-05-27
Status: rascunho para aprovação

## Pedido limpo

Aprovar o padrão canônico para **coleções LK produto-first** antes de eu transformar isso em template oficial reutilizável para novas coleções.

## O que este padrão resolve

Evita que cada coleção nova seja montada “da cabeça”. A coleção passa a seguir um molde fixo:

- produtos primeiro;
- topo minimalista e premium;
- guia editorial/FAQ/schema depois do grid;
- CTA discreto para guia ou atendimento;
- mobile comprimido para não travar descoberta de produto.

## Molde proposto

### 1) Topo da coleção

- H1 limpo;
- kicker curto;
- parágrafo breve de curadoria;
- sem labels inventadas;
- sem excesso de narrativa antes do grid.

### 2) Grid de produtos

- produtos aparecem antes de bloco editorial longo;
- ordem comercial preservada;
- visual direto e premium.

### 3) Guia/apoio depois do grid

- guia editorial linkado ou embedado abaixo do grid;
- FAQ;
- schema quando aplicável;
- bloco citável/comercial útil.

### 4) CTA

- um CTA discreto;
- apontando para guia/página de apoio ou atendimento;
- sem duplicar CTAs no topo.

## Regras anti-invenção

- não criar nova linguagem visual para cada coleção;
- não inventar nome de seção, label visível ou CTA novo sem aprovação;
- se a coleção não encaixar neste molde, primeiro propor novo template.

## Referência canônica

- Coleção 204L como molde-base de produto-first;
- Guias editoriais seguem o padrão Moon Shoe;
- este padrão fica entre os dois: coleção primeiro, guia depois.

## O que eu farei depois da aprovação

1. Transformar este pacote em template canônico no Brain.
2. Criar o brief obrigatório para coleções produto-first.
3. Criar o checklist de QA para impedir variações inventadas.
4. Reusar esse padrão nas próximas coleções LK.

## Risco

Baixo. É uma padronização documental/interna. Não mexe em Shopify produção.

## Rollback

Se você não aprovar, eu não transformo isso em template oficial nem uso como padrão base.

## Próximo passo

Aprovação deste pacote para eu seguir com o template oficial de coleção produto-first.

## Complemento de completude do approval packet — 2026-06-14

### Decisão solicitada / ação proposta
- Decisão solicitada: Lucas deve aprovar, ajustar ou bloquear explicitamente o packet `Approval packet — Padrão LK para coleções produto-first` antes de qualquer execução sensível.
- Ação proposta: usar este documento apenas como approval packet/preview; execução só pode ocorrer no escopo exato aprovado e com receipt/readback posterior.

### Target / owner
- Target: `Approval packet — Padrão LK para coleções produto-first` no caminho `areas/lk/sub-areas/growth/approval-packets/colecao-produto-first-padrao-lk-2026-05-27.md`.
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
