# Approval packet — padrão Guia Editorial LK para outras coleções melhoradas

Data: 2026-05-25
Status: aguardando aprovação explícita de produção

## Pedido

Aplicar o padrão aprovado no Moon Shoe às outras coleções/páginas da LK que já passaram por melhoria editorial/CRO/GEO.

## Padrão canônico a replicar

1. Coleção continua product-first:
   - Hero/H1 nativo
   - Produtos/grid
   - CTA pós-grid para Guia Editorial LK
   - FAQ sem duplicação

2. Guia Editorial estável em Shopify Page:
   - URL dedicada `/pages/{modelo}-guia-lk` ou equivalente
   - CTA de volta para a coleção: `Comprar produtos da coleção` e/ou `Ver produtos da coleção`
   - Bloco de relevância editorial/moda quando houver fontes confiáveis: Vogue, Hypebeast, Hypebae, Highsnobiety, WWD, GQ, Sneaker News etc.
   - FAQ reescrita para objeções reais de compra e answerability em IA
   - Links externos `rel="nofollow noopener"` e nova aba
   - Sem termos públicos proibidos: `encomenda`, `pronta entrega`; evitar taxonomia pública de estoque/disponibilidade

3. Auditoria obrigatória por coleção antes de publicar:
   - SEO/GEO/AI citation readiness
   - FAQ dedupe
   - schema/FAQPage quando aplicável
   - mobile CRO
   - links internos coleção ↔ guia
   - forbidden-term scan
   - rollback e D+7 review

## Coleções detectadas como candidatas já melhoradas no tema

- `new-balance-204l` — coleção já tem copy editorial e padrão visual/reveal; prioridade alta para guia estável.
- `adidas-samba-jane` — já passou por piloto CRO; precisa avaliar se guia editorial/source page faz sentido agora ou se primeiro fecha QA da coleção.
- `onitsuka-tiger`
- `onitsuka-tiger-todos-os-modelos`
- `onitsuka-tiger-mexico-66`
- `new-balance-9060`
- `new-balance-530`
- `nike-x-jacquemus-moon-shoe-sp` — já publicado como referência/padrão.

## Rollout recomendado

### Lote 1 — aplicar agora após aprovação

1. New Balance 204L
   - Criar página guia estável.
   - Link pós-grid da coleção para a página.
   - Buscar fontes de moda/sneaker para bloco de relevância.
   - Revalidar FAQ.

2. Adidas Samba Jane
   - Reusar aprendizado do piloto CRO.
   - Confirmar se o guia deve ser `Adidas Samba Jane` ou mais amplo `Adidas Samba`.
   - Criar/ajustar guia com CTAs de compra.

### Lote 2 — após QA do lote 1

3. Onitsuka Tiger / Mexico 66
4. New Balance 9060
5. New Balance 530

## O que posso fazer sem nova aprovação

- Pesquisa de fontes editoriais por coleção.
- Draft local dos guias.
- Approval packets com título/meta/H1/FAQ/schema/rollback.
- Auditoria SEO/GEO/FAQ/CRO read-only de cada coleção.

## O que exige aprovação explícita

- Criar/editar Shopify Pages públicas.
- Alterar links/copy/section no tema de produção.
- Publicar guias ou mudar coleções públicas.

## Frase de aprovação sugerida

“Pode publicar o padrão Guia Editorial LK nas coleções `new-balance-204l` e `adidas-samba-jane`, criando páginas estáveis e links pós-grid, com rollback e QA.”

## QA de produção exigido por URL

- HTTP 200 público.
- H1 único ou sem duplicação visual.
- CTA guia → coleção funcionando.
- CTA coleção → guia funcionando.
- Bloco de fontes editoriais presente quando aplicável.
- FAQ não duplicada.
- Sem `encomenda`/`pronta entrega` no bloco novo.
- Mobile render OK.
- Receipt local + D+7 review.

## Complemento de completude do approval packet — 2026-06-14

### Decisão solicitada / ação proposta
- Decisão solicitada: Lucas deve aprovar, ajustar ou bloquear explicitamente o packet `Approval packet — padrão Guia Editorial LK para outras coleções melhoradas` antes de qualquer execução sensível.
- Ação proposta: usar este documento apenas como approval packet/preview; execução só pode ocorrer no escopo exato aprovado e com receipt/readback posterior.

### Target / owner
- Target: `Approval packet — padrão Guia Editorial LK para outras coleções melhoradas` no caminho `areas/lk/sub-areas/growth/approval-packets/collection-guide-standard-rollout-other-improved-pages-20260525.md`.
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
