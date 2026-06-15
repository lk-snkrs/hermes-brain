# Packet — Dev theme rollout do padrão Moon Shoe nas próximas coleções

Data: 2026-05-25
Destino: LK Growth / Shopify dev theme
Status: aguardando aprovação operacional para escrita em dev theme

## Pedido limpo

Aplicar em ordem o padrão aprovado no Nike x Jacquemus Moon Shoe às outras coleções já melhoradas, começando por um preview em tema dev. Depois da aprovação visual do Lucas, publicar em produção com rollback.

## Ordem recomendada

### Lote 1 — primeiro preview

1. New Balance 204L
2. Adidas Samba Jane

### Lote 2 — após aprovação/QA do lote 1

3. Onitsuka Tiger Mexico 66
4. Onitsuka Tiger geral / Todos os modelos
5. New Balance 9060
6. New Balance 530

## Evidências já verificadas read-only

Tema produção verificado: `lk-new-theme/production`.

Estado atual detectado:

- `nike-x-jacquemus-moon-shoe-sp`: padrão completo; é a referência.
- `new-balance-204l`: possui página guia estável (`new-balance-204l-original-brasil-guia-lk`), mas ainda precisa padronizar linkagem/CTA pós-grid/FAQ/mídia no mesmo formato Moon Shoe.
- `adidas-samba-jane`: possui copy editorial de coleção, mas não possui guia estável detectado no padrão Moon Shoe.
- `onitsuka-tiger`: possui guia estável, mas não foi confirmado no fluxo completo coleção ↔ guia.
- `onitsuka-tiger-todos-os-modelos`: copy melhorada, sem guia estável detectado.
- `onitsuka-tiger-mexico-66`: copy melhorada, sem guia estável dedicado detectado.
- `new-balance-9060`: possui guia (`new-balance-9060-guia`) e bloco visual, mas não está padronizado como Moon Shoe.
- `new-balance-530`: possui sinais de bloco/link editorial, mas sem página estável própria detectada.

## Preview a preparar no tema dev

Tema alvo esperado:

- `lk-new-theme/dev`
- tipo: unpublished/dev theme

URLs de preview esperadas após execução:

- New Balance 204L:
  - `https://lksneakers.com.br/collections/new-balance-204l?preview_theme_id=155065450718&_ab=0&_fd=0&_sc=1`

- Adidas Samba Jane:
  - `https://lksneakers.com.br/collections/adidas-samba-jane?preview_theme_id=155065450718&_ab=0&_fd=0&_sc=1`

## Mudanças previstas no dev theme — sem produção

Para cada coleção do lote 1:

1. Inserir CTA pós-grid para `Guia editorial LK`.
2. Garantir que a coleção continue product-first.
3. Criar/ajustar bloco de guia com CTA de volta para a coleção.
4. Repensar FAQ por objeções reais de compra:
   - autenticidade/originalidade;
   - como escolher versão/colorway;
   - forma/tamanho com linguagem canônica: `tem a forma grande ou pequena?`;
   - onde comprar original no Brasil;
   - por que comprar com curadoria humana.
5. Adicionar bloco de mídia/contexto quando houver fonte confiável.
6. Rodar forbidden-term scan:
   - `estoque`
   - `encomenda`
   - `pronta entrega`
7. QA mobile:
   - produtos aparecem rápido;
   - guia não compete com grid;
   - FAQ não duplica;
   - CTA visível e funcional.

## Risco

- Baixo em dev theme: não altera produção.
- Médio se criar páginas públicas em Shopify durante o preview, porque Page é objeto global e não theme-specific.
- Mitigação: no preview, preferir template/section dev ou páginas não publicadas/rascunho quando possível; produção só após aprovação explícita.

## Bloqueios atuais

Este turno foi roteado como `preparar approval packet`, então não foi executada escrita externa em Shopify/dev theme.

Para executar o upload no tema dev no próximo passo, Lucas precisa aprovar especificamente:

> “Aprovado subir no tema dev o Lote 1: New Balance 204L e Adidas Samba Jane, sem produção.”

## Rollback

Para qualquer upload no dev theme:

1. baixar asset atual antes do PUT;
2. salvar `asset.before` local;
3. aplicar patch mínimo;
4. ler de volta via Admin API;
5. salvar `asset.after` e `receipt.json`;
6. rollback = reenviar `asset.before` ao dev theme.

Para produção futura:

1. redescobrir theme `role=main`;
2. snapshot antes;
3. publicar somente assets aprovados;
4. validar DOM público por URL;
5. agendar revisão D+7.

## Decisão necessária

Autorizar o próximo passo seguro:

**Subir no tema dev o Lote 1 — New Balance 204L + Adidas Samba Jane — sem produção.**

## Complemento de completude do approval packet — 2026-06-14

### Decisão solicitada / ação proposta
- Decisão solicitada: Lucas deve aprovar, ajustar ou bloquear explicitamente o packet `Packet — Dev theme rollout do padrão Moon Shoe nas próximas coleções` antes de qualquer execução sensível.
- Ação proposta: usar este documento apenas como approval packet/preview; execução só pode ocorrer no escopo exato aprovado e com receipt/readback posterior.

### Target / owner
- Target: `Packet — Dev theme rollout do padrão Moon Shoe nas próximas coleções` no caminho `areas/lk/sub-areas/growth/approval-packets/dev-theme-rollout-collection-guide-standard-lote1-20260525.md`.
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
