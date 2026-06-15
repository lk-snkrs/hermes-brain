# Approval Packet — Coleção Sneakers (/collections/sneakers)

Data: 2026-05-31

## Escopo

Preparar melhoria de SEO/GEO/CRO para a coleção pública `/collections/sneakers`, mantendo a experiência mobile-first e produto-first.

Este packet é **read-only / preparação**. Não houve alteração em Shopify, tema, coleção, produto, preço, estoque, GMC, Klaviyo, WhatsApp ou campanha.

## Evidência base

Fonte: diagnóstico `lk-phase1-collections-seo-geo-20260531.md`.

- URL: `https://lksneakers.com.br/collections/sneakers`
- Handle: `sneakers`
- Tipo: smart collection
- Views GA4 90d: `92.351`
- Views GA4 30d: `8.085`
- Title público atual: `Sneakers: tênis adidas, nike e mais | LK Sneakers`
- H1 atual: `Tênis e Sneakers Originais`
- Meta description atual: 151 caracteres
- Body words Shopify: 484
- FAQ visível: sim
- FAQPage schema: não detectado
- Achados: FAQ visível sem FAQPage; imagens sem alt

## Decisão criativa validada com Lucas

Para esta coleção ampla, **não usar** linguagem como “sneakers selecionados pela curadoria LK” no topo, porque a página representa o catálogo amplo de sneakers, não uma edição curada fechada.

Direção aprovada:

> Sneakers originais para diferentes estilos, marcas e momentos

Princípio:

- Produto primeiro.
- Texto curto antes do grid.
- Conteúdo editorial e FAQ depois do grid.
- Curadoria como camada de organização/orientação, não como promessa de que todos os itens da coleção são uma seleção individual.

## Proposta de estrutura

1. H1 atual preservado ou ajustado somente se necessário.
2. Intro curta antes do grid, no máximo 2–3 linhas no mobile.
3. Grid de produtos imediatamente depois.
4. Bloco editorial compacto depois do grid.
5. Links internos para marcas/áreas estratégicas.
6. FAQ comercial abaixo do editorial.
7. FAQPage JSON-LD somente se a FAQ ficar visível.

## Copy proposta — topo antes do grid

### Headline

**Sneakers originais para diferentes estilos, marcas e momentos**

### Texto curto

Explore o catálogo da LK com modelos de marcas como Nike, Adidas, New Balance, Air Jordan e Onitsuka Tiger. Encontre tênis originais para o dia a dia, lançamentos, clássicos e pares premium.

### Observação CRO

Este bloco deve ser visualmente compacto. No mobile, a primeira fileira de produtos deve aparecer com pouca rolagem. Não inserir imagem editorial, FAQ, banner alto ou bloco de cards antes do grid.

## Copy proposta — bloco pós-grid

### Título

**Encontre o sneaker ideal na LK**

### Texto

A coleção de sneakers da LK reúne diferentes propostas em um só lugar: modelos casuais para rotina, clássicos que atravessam temporadas, lançamentos recentes e pares premium com forte presença no universo streetwear.

Por ser uma página ampla, ela funciona como ponto de partida para explorar marcas, silhuetas e estilos antes de escolher o modelo ideal.

### Links internos compactos

**Explore também:** New Balance · Adidas · Nike · Air Jordan · Onitsuka Tiger · Lançamentos · Sale

Links sugeridos:

- New Balance: `/collections/new-balance-todos-os-modelos`
- Adidas: `/collections/adidas-todos-os-modelos`
- Nike: `/collections/nike-todos-os-modelos`
- Air Jordan: `/collections/air-jordan`
- Onitsuka Tiger: `/collections/onitsuka-tiger`
- Lançamentos: `/collections/lancamentos`
- Sale: `/collections/sale`

Validar handles antes de implementação.

## FAQ proposta

### 1. Os sneakers vendidos pela LK são originais?

Sim. A LK trabalha com sneakers originais e produtos de procedência acompanhada pela loja, reunindo modelos de diferentes marcas, estilos e momentos de uso.

### 2. Como escolher o sneaker ideal?

A melhor escolha depende do seu estilo, rotina e preferência de marca. Para o dia a dia, modelos casuais e versáteis costumam funcionar bem. Para quem busca destaque, lançamentos, clássicos do streetwear e pares premium podem ser boas opções.

### 3. Quais marcas de sneakers encontro na LK?

A LK reúne sneakers de marcas como Nike, Adidas, New Balance, Air Jordan, Onitsuka Tiger e outras referências do universo streetwear e lifestyle, conforme disponibilidade do catálogo.

### 4. A LK tem lançamentos e modelos premium?

Sim. Além de modelos casuais e clássicos, o catálogo pode incluir lançamentos recentes, pares premium e sneakers com maior procura no mercado.

### 5. Posso comprar sneakers parcelados?

Sim. As opções de parcelamento aparecem no checkout conforme as condições disponíveis no momento da compra.

### 6. A LK entrega para todo o Brasil?

Sim. Os pedidos realizados no site podem ser enviados para diferentes regiões do Brasil, conforme disponibilidade logística informada no checkout.

## FAQPage JSON-LD proposto

Usar somente se as perguntas/respostas acima estiverem visíveis na página.

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Os sneakers vendidos pela LK são originais?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Sim. A LK trabalha com sneakers originais e produtos de procedência acompanhada pela loja, reunindo modelos de diferentes marcas, estilos e momentos de uso."
      }
    },
    {
      "@type": "Question",
      "name": "Como escolher o sneaker ideal?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A melhor escolha depende do seu estilo, rotina e preferência de marca. Para o dia a dia, modelos casuais e versáteis costumam funcionar bem. Para quem busca destaque, lançamentos, clássicos do streetwear e pares premium podem ser boas opções."
      }
    },
    {
      "@type": "Question",
      "name": "Quais marcas de sneakers encontro na LK?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A LK reúne sneakers de marcas como Nike, Adidas, New Balance, Air Jordan, Onitsuka Tiger e outras referências do universo streetwear e lifestyle, conforme disponibilidade do catálogo."
      }
    },
    {
      "@type": "Question",
      "name": "A LK tem lançamentos e modelos premium?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Sim. Além de modelos casuais e clássicos, o catálogo pode incluir lançamentos recentes, pares premium e sneakers com maior procura no mercado."
      }
    },
    {
      "@type": "Question",
      "name": "Posso comprar sneakers parcelados?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Sim. As opções de parcelamento aparecem no checkout conforme as condições disponíveis no momento da compra."
      }
    },
    {
      "@type": "Question",
      "name": "A LK entrega para todo o Brasil?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Sim. Os pedidos realizados no site podem ser enviados para diferentes regiões do Brasil, conforme disponibilidade logística informada no checkout."
      }
    }
  ]
}
```

## Meta SEO opcional

Meta atual tem tamanho bom. Não é obrigatório trocar.

Se quiser alinhar com o novo território:

> Sneakers originais para diferentes estilos, marcas e momentos. Encontre Nike, Adidas, New Balance, Air Jordan e mais na LK Sneakers.

Observação: validar tamanho final antes de aplicar.

## Risco

Baixo, se aplicado primeiro em dev/preview.

Riscos principais:

- Empurrar produtos para baixo no mobile se o topo ficar longo.
- Repetir conteúdo já existente no tema/coleção e criar redundância.
- Usar FAQPage sem FAQ visível ou com divergência de texto.
- Links internos apontarem para handles incorretos/redirecionados.
- Tom parecer promessa excessiva sobre curadoria ou autenticação.

## Rollback

Antes de qualquer write aprovado:

1. Exportar snapshot da coleção atual: title, handle, body_html, metafields relevantes, template, SEO title/meta.
2. Exportar asset/template/seção do tema se houver alteração em Liquid/JSON.
3. Aplicar primeiro em dev/unpublished theme ou ambiente de preview.
4. Validar mobile público/preview.
5. Se necessário, restaurar body/metafields/template a partir do snapshot.

## Critérios de aceite em dev/preview

- Produtos continuam aparecendo rapidamente no mobile.
- Topo textual antes do grid fica compacto.
- Nenhuma alteração em preço, estoque, disponibilidade, ordenação ou tags.
- FAQ visível bate exatamente com FAQPage JSON-LD.
- Links internos funcionam e apontam para coleções corretas.
- Title, canonical, robots e H1 continuam saudáveis.
- Sem quebra visual no desktop/mobile.

## Próxima decisão

Aprovar preparação técnica em dev/preview para `/collections/sneakers` com:

- intro compacta antes do grid;
- bloco editorial pós-grid;
- links internos compactos;
- FAQ comercial;
- FAQPage JSON-LD condicionado à FAQ visível;
- sem mexer em preço, estoque, ordenação, produtos ou produção.

Frase de aprovação sugerida:

> Aprovado preparar preview dev da coleção Sneakers conforme packet, sem production.

## Complemento de completude do approval packet — 2026-06-14

### Decisão solicitada / ação proposta
- Decisão solicitada: Lucas deve aprovar, ajustar ou bloquear explicitamente o packet `Approval Packet — Coleção Sneakers (/collections/sneakers)` antes de qualquer execução sensível.
- Ação proposta: usar este documento apenas como approval packet/preview; execução só pode ocorrer no escopo exato aprovado e com receipt/readback posterior.

### Target / owner
- Target: `Approval Packet — Coleção Sneakers (/collections/sneakers)` no caminho `areas/lk/sub-areas/growth/approval-packets/collections-sneakers/2026-05-31/lk-collection-sneakers-copy-geo-cro-approval-packet-20260531.md`.
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
