# Approval packet — Moon Shoe guia LK: hero escuro

Data: 2026-05-26
Superfície: Shopify production theme `155065417950`, página `/pages/nike-moon-shoe-jacquemus-guia-lk`

## Pedido Lucas

Aplicar mais drama no topo do guia: seção hero com fundo escuro e letras brancas.

## Status já aplicado antes deste packet

- Kicker `GUIA LK · NIKE X JACQUEMUS`: reduzido de `12px` para `9.5px` no snippet e com override nas sections.
- Readback Shopify Admin: OK.
- HTML público já contém override `9.5px`, mas ainda também contém a regra base antiga `12px`; por cascade/override, a regra específica final deve vencer quando a página renderiza completa.

## Proposta visual

Transformar apenas o hero inicial em bloco editorial escuro:

- fundo: `#111111` / quase preto;
- texto principal e kicker: branco/off-white;
- intro: cinza claro;
- botões invertidos:
  - botão principal branco com texto preto;
  - botão secundário transparente com borda branca;
- legenda da imagem em cinza claro;
- manter imagem original à direita;
- manter corpo do guia branco abaixo.

## CSS proposto

```css
/* LK hotfix proposal 2026-05-26: Moon Shoe dark editorial hero */
article.lk-source-page--moon-shoe .lk-source-page__header {
  max-width: none !important;
  margin: 0 !important;
  padding: clamp(56px, 7vw, 92px) max(20px, calc((100vw - 1120px) / 2 + 20px)) 44px !important;
  background: #111111 !important;
  color: #f7f3ed !important;
}

article.lk-source-page--moon-shoe .lk-source-page__header h1 {
  color: #f7f3ed !important;
}

article.lk-source-page--moon-shoe .lk-source-page__eyebrow {
  color: rgba(247, 243, 237, .76) !important;
  font-size: 9.5px !important;
  letter-spacing: .16em !important;
}

article.lk-source-page--moon-shoe .lk-source-page__intro {
  color: rgba(247, 243, 237, .82) !important;
}

article.lk-source-page--moon-shoe .lk-source-hero-actions a:first-child {
  background: #f7f3ed !important;
  color: #111111 !important;
  border-color: #f7f3ed !important;
}

article.lk-source-page--moon-shoe .lk-source-hero-actions a:last-child {
  background: transparent !important;
  color: #f7f3ed !important;
  border-color: rgba(247, 243, 237, .72) !important;
}

article.lk-source-page--moon-shoe .lk-source-hero-media span {
  color: rgba(247, 243, 237, .62) !important;
}

@media (max-width: 749px) {
  article.lk-source-page--moon-shoe .lk-source-page__header {
    padding: 36px 22px 34px !important;
  }
}
```

## Risco

Baixo/médio:

- É customer-facing e em produção.
- Pode melhorar percepção editorial/premium, mas altera bastante o impacto visual acima da dobra.
- Precisa checagem desktop e mobile após aplicar.

## Rollback

Reverter os assets salvos em:

`/opt/data/hermes_bruno_ingest/hermes-brain/areas/lk/sub-areas/growth/shopify-theme-backups/`

ou remover o bloco CSS `LK hotfix proposal 2026-05-26: Moon Shoe dark editorial hero` das sections/snippet.

## Aprovação necessária

Aplicar em produção exige aprovação explícita de Lucas no turno atual.

Frase de aprovação sugerida:

`Aprovo aplicar o hero escuro na página Moon Shoe em produção.`

## Complemento de completude do approval packet — 2026-06-14

### Decisão solicitada / ação proposta
- Decisão solicitada: Lucas deve aprovar, ajustar ou bloquear explicitamente o packet `Approval packet — Moon Shoe guia LK: hero escuro` antes de qualquer execução sensível.
- Ação proposta: usar este documento apenas como approval packet/preview; execução só pode ocorrer no escopo exato aprovado e com receipt/readback posterior.

### Target / owner
- Target: `Approval packet — Moon Shoe guia LK: hero escuro` no caminho `areas/lk/sub-areas/growth/approval-packets/2026-05-26-moon-shoe-dark-hero-approval.md`.
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
