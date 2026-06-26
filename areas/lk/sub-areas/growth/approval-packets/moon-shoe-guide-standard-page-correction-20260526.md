# Approval packet — Moon Shoe guide as LK standard page

Status: aguardando aprovação de Lucas para write Shopify
Data: 2026-05-26

## Destino

Shopify / página editorial LK:

- https://lksneakers.com.br/pages/nike-moon-shoe-jacquemus-guia-lk

## Pedido limpo

Corrigir a página Nike x Jacquemus Moon Shoe para virar a página padrão de curadoria LK, usando-a como referência canônica para próximas páginas editoriais/guia.

## Evidências read-only

Inspeção pública via storefront mostrou:

- Hero editorial existe, com fundo escuro, H1, parágrafo, imagem e CTAs.
- Conteúdo editorial é forte, mas está denso e com hierarquia irregular.
- Há rótulos/linguagem operacional de estrutura como “Bloco citável LK” que aparecem para o cliente e devem virar tratamento visual editorial ou ser removidos.
- FAQ/accordion apresenta risco de baixa legibilidade/contraste.
- CTA “Comprar a coleção” perto do FAQ aparenta contraste/texto inadequado.
- Cards de produto relacionados aparecem com risco de imagem vazia/incompleta.
- Popup/newsletter pode interferir na primeira impressão do hero em avaliação visual.

## Correção proposta

Transformar a página em padrão LK Guide Page:

1. Hero canônico
   - Kicker discreto.
   - H1 editorial curto e premium.
   - Parágrafo único, denso e citável.
   - Imagem editorial à direita.
   - CTA primário para coleção e CTA secundário para FAQ, se mantidos, com contraste correto.

2. Miolo editorial canônico
   - Remover label visível “Bloco citável LK”.
   - Transformar blocos citáveis em cards editoriais sem jargão interno.
   - Reduzir repetição e criar hierarquia clara: origem, Jacquemus, colorways, leitura LK, matérias externas.
   - Manter linguagem premium: curadoria, autenticidade, orientação humana.

3. Colorways
   - Manter tabela ou converter para cards, mas com visual mais editorial e menos técnico.

4. Matérias/sinais editoriais
   - Manter cards de fontes externas.
   - Link text padronizado: “Acesse a matéria”.
   - Sem excesso de labels internas.

5. FAQ
   - Corrigir contraste.
   - Garantir accordion legível e clicável.
   - Manter FAQPage schema alinhado ao conteúdo visível.

6. Seleção relacionada
   - Garantir 4 produtos no máximo.
   - Garantir imagens visíveis.
   - Se não houver fonte de produtos renderizando corretamente, ocultar a seção até correção.

7. Padrão de aprovação
   - Toda aprovação deve usar link Shopify storefront/preview.
   - Código local/Brain não substitui aprovação visual pelo link.

## Preview / link de aprovação

Link atual a ser corrigido e reaprovado:

- https://lksneakers.com.br/pages/nike-moon-shoe-jacquemus-guia-lk

Após correção, gerar novo link Shopify de preview/storefront para aprovação final.

## Risco

- Médio se aplicado direto em produção, porque muda página customer-facing.
- Baixo se aplicado primeiro em preview/dev ou com backup da page atual.

## Bloqueios

- Sem aprovação explícita atual para write Shopify em produção.
- Precisa backup/readback da page atual antes de qualquer alteração.

## Rollback

- Snapshot da page atual antes do write.
- Reverter body/template/SEO fields via Shopify Admin API caso o padrão não seja aprovado.

## Decisão necessária

Lucas aprovar: “pode aplicar essa correção na página Moon Shoe e me mandar o link Shopify corrigido para aprovação final”.
