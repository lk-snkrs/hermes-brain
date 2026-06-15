# Packet — ajustes mobile 204L guia editorial dev

Data: 2026-05-25
Área: LK / Growth / Shopify Theme
Coleção: New Balance 204L
Ambiente pretendido: Dev theme `155065450718` (`lk-new-theme/dev`)

## Pedido limpo

Lucas revisou o mobile da coleção 204L e pediu:

1. Micro-label `Curadoria LK` menor no mobile: `9px`.
2. Remover o bloco preto de `Guia editorial LK`, por duplicar o resumo do guia editorial logo abaixo.
3. Remover CTA `Ver produtos da coleção` dentro do guia da própria coleção; manter apenas CTA para o guia completo.

## Evidências do print

- O bloco preto aparece imediatamente acima do painel bege do guia, com o mesmo contexto editorial e CTA `Ler guia editorial`.
- O painel bege já contém o resumo/guia editorial completo, portanto o bloco preto é redundante.
- O CTA para produtos é redundante dentro da própria collection page.

## Patch local preparado

Arquivo ajustado localmente:

- `scripts/lk_collection_guide_standard_lote1_dev_20260525.py`

Mudanças preparadas:

- CSS mobile:
  - `.lk-guide-standard-panel__eyebrow { font-size: 9px !important; }`
- Bloco preto:
  - escondido para `collection.handle == 'new-balance-204l'`
  - mantido temporariamente para `adidas-samba-jane` até revisão específica.
- CTA 204L:
  - removido `/collections/new-balance-204l` / `Ver produtos da coleção`
  - mantido apenas `/pages/new-balance-204l-original-brasil-guia-lk` / `Abrir guia completo`

## Bloqueio

A escrita no dev theme via Admin API não foi executada neste turno porque o roteamento de segurança bloqueou chamadas de terminal/API como ação externa/escrita.

## Risco

Baixo, se aplicado apenas no tema dev. Validar depois:

- ausência do bloco preto na 204L;
- mobile eyebrow em 9px;
- CTA único para guia completo;
- produção intacta;
- scan de termos proibidos.

## Rollback

Restaurar o asset `sections/lk-collection.liquid` do backup pré-write do dev theme ou reverter este patch local.

## Próximo passo

Quando a escrita dev estiver liberada neste fluxo, aplicar o patch no tema dev e reenviar o link de preview da 204L para Lucas; se permitido, enviar também ao Renan Fortini.

## Complemento de completude do approval packet — 2026-06-14

### Decisão solicitada / ação proposta
- Decisão solicitada: Lucas deve aprovar, ajustar ou bloquear explicitamente o packet `Packet — ajustes mobile 204L guia editorial dev` antes de qualquer execução sensível.
- Ação proposta: usar este documento apenas como approval packet/preview; execução só pode ocorrer no escopo exato aprovado e com receipt/readback posterior.

### Target / owner
- Target: `Packet — ajustes mobile 204L guia editorial dev` no caminho `areas/lk/sub-areas/growth/approval-packets/204l-mobile-guide-cleanup-dev-20260525.md`.
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
