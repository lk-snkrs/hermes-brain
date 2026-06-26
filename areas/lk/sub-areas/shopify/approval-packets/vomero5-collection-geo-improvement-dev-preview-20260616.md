# Approval packet — melhoria da coleção Nike Vomero 5

Data: 2026-06-16  
Alvo: `/collections/nike-vomero-5`  
Modo executado: read-only / preparação. **Nenhum write Shopify foi feito.**

## Evidência atual

Fonte pública:
- URL: `https://lksneakers.com.br/collections/nike-vomero-5`
- HTTP: 200
- Liquid error: não detectado
- H1: `Nike Vomero 5`
- Title público/Admin SEO: `Tênis Nike Vomero 5 | Curadoria Exclusiva | LK Sneakers` — 55 caracteres
- Meta atual: `Compre Nike Vomero 5 na LK Sneakers. 100% originais · Parcele em 10x · Frete grátis · Loja Jardins SP.` — 102 caracteres
- Produtos públicos em `/products.json`: 4
- FAQ visível: sim, mas **FAQPage JSON-LD não foi detectado**

Produtos públicos lidos:
- `tenis-nike-zoom-vomero-5-metallic-silver-platinum-violet-prateado-violeta`
- `tenis-nike-zoom-vomero-5-photon-dust-metallic-silver-cinza`
- `tenis-nike-zoom-vomero-5-metallic-silver-blue-tint-prateado-azul`
- `tenis-nike-air-zoom-vomero-5-doernbecher-2023-laranja`

Achados relevantes:
- A coleção já tem conteúdo editorial e FAQ na descrição.
- A meta description é curta para a intenção de busca/modelo.
- O FAQ aparece visível no HTML, mas não está pareado com FAQPage JSON-LD.
- A resposta atual da terceira FAQ aparece truncada no Admin read-only: termina em `a recomendação g`, indicando oportunidade de limpeza/correção textual.
- A copy atual usa linguagem de “autenticidade verificada”/“verificação de autenticidade”; para alinhar ao posicionamento LK, recomendo trocar para “produtos originais”, “curadoria especializada” e “loja física nos Jardins”, sem parecer uma operação de legit-check.

Dados brutos:
- `assets/vomero5-collection-improvement-20260616/vomero5_collection_improvement_packet.json`

## Interpretação

A página está funcional e indexável, mas pode melhorar em GEO/SXO por três motivos:

1. **FAQ sem schema:** a informação existe para o usuário, mas está menos legível para Google/AI Overviews.
2. **Meta curta:** 102 caracteres; há espaço para reforçar intenção “Nike Vomero 5 original”, curadoria e loja física.
3. **FAQ truncada/linguagem antiga:** a descrição atual mistura disponibilidade/frete/parcelamento e verificação; melhor deixar o bloco mais perene, premium e citável.

## Proposta de melhoria

### SEO fields da coleção

Title proposto:

`Nike Vomero 5 Original | LK Sneakers`

- 37 caracteres

Meta description proposta:

`Nike Vomero 5 original na LK Sneakers: modelos premium, curadoria especializada, loja física nos Jardins e atendimento humano.`

- 125 caracteres
- sem promessa de estoque/disponibilidade
- sem depender de preço, frete ou parcelamento
- reforça entidade, originalidade, curadoria e loja física

## Bloco editorial pós-grade proposto

```html
<section class="lk-collection-guide" id="guia-nike-vomero-5">
  <div class="lk-collection-guide__inner">
    <p class="lk-eyebrow">Guia LK</p>
    <h2>Nike Vomero 5 original: conforto running com visual premium</h2>
    <p>O Nike Vomero 5 é uma das silhuetas running mais procuradas da Nike para quem busca conforto, acabamento técnico e estética urbana. Na LK Sneakers, a coleção reúne pares originais com curadoria especializada, atendimento humano e suporte para escolher tamanho, cor e proposta de uso.</p>
    <p>A linha é conhecida pela mistura de mesh, sobreposições estruturadas e amortecimento macio, criando um sneaker versátil para uso diário. Para comprar com mais segurança, observe a numeração habitual em Nike, o material do cabedal e a combinação de cores que melhor conversa com seu guarda-roupa.</p>
    <h3>Como escolher seu Nike Vomero 5?</h3>
    <ul>
      <li><strong>Para uso diário:</strong> prefira cores neutras como cinza, preto, bege ou branco.</li>
      <li><strong>Para destaque visual:</strong> escolha versões com contraste, textura ou colorways sazonais.</li>
      <li><strong>Para presente:</strong> confirme a numeração Nike habitual antes da compra.</li>
    </ul>
  </div>
</section>
```

## FAQ visível proposta

```html
<section class="lk-collection-faq" id="faq-nike-vomero-5">
  <h2>Perguntas frequentes sobre Nike Vomero 5</h2>
  <details><summary>O Nike Vomero 5 é original na LK Sneakers?</summary><p>Sim. A LK Sneakers trabalha com produtos originais e curadoria especializada, além de loja física nos Jardins, em São Paulo.</p></details>
  <details><summary>O Nike Vomero 5 é confortável para o dia a dia?</summary><p>Sim. O Vomero 5 é uma silhueta running da Nike conhecida pelo amortecimento macio, cabedal respirável e construção estável para uso urbano.</p></details>
  <details><summary>Como escolher o tamanho do Nike Vomero 5?</summary><p>Em geral, comece pela sua numeração Nike habitual. Se estiver entre dois tamanhos ou preferir mais espaço, consulte o guia de tamanhos antes de finalizar a compra.</p></details>
  <details><summary>Qual cor de Nike Vomero 5 combina melhor com uso diário?</summary><p>Cores como cinza, preto, branco e bege são mais fáceis de combinar no dia a dia. Versões com contraste ou textura funcionam melhor quando o sneaker é o destaque do look.</p></details>
</section>
```

## FAQPage JSON-LD proposto

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "O Nike Vomero 5 é original na LK Sneakers?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Sim. A LK Sneakers trabalha com produtos originais e curadoria especializada, além de loja física nos Jardins, em São Paulo."
      }
    },
    {
      "@type": "Question",
      "name": "O Nike Vomero 5 é confortável para o dia a dia?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Sim. O Vomero 5 é uma silhueta running da Nike conhecida pelo amortecimento macio, cabedal respirável e construção estável para uso urbano."
      }
    },
    {
      "@type": "Question",
      "name": "Como escolher o tamanho do Nike Vomero 5?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Em geral, comece pela sua numeração Nike habitual. Se estiver entre dois tamanhos ou preferir mais espaço, consulte o guia de tamanhos antes de finalizar a compra."
      }
    },
    {
      "@type": "Question",
      "name": "Qual cor de Nike Vomero 5 combina melhor com uso diário?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Cores como cinza, preto, branco e bege são mais fáceis de combinar no dia a dia. Versões com contraste ou textura funcionam melhor quando o sneaker é o destaque do look."
      }
    }
  ]
}
```

## Opções de implementação

### Opção A — recomendada: DEV preview primeiro

Escopo:
- preservar grid/produtos acima
- substituir/limpar bloco editorial/FAQ da coleção ou renderizar bloco pós-grade específico
- adicionar FAQPage JSON-LD pareado com a FAQ visível
- ajustar SEO title/meta da coleção, se aprovado no mesmo lote ou em etapa separada

Exige:
- Shopify collection write se mexer na descrição/SEO fields
- theme write se a FAQPage JSON-LD for implementada no tema por handle/template
- DEV preview + QA antes de Production

### Opção B — só SEO fields

Escopo:
- alterar apenas `seo.title` e `seo.description` da coleção

Vantagem:
- mais simples e reversível

Limitação:
- não resolve FAQPage JSON-LD nem a FAQ truncada.

### Opção C — só conteúdo/FAQ

Escopo:
- limpar description/FAQ visível
- deixar SEO fields como estão

Limitação:
- perde o ganho simples da meta description.

## Risco

Baixo, desde que entre primeiro em DEV/preview ou seja separado por write pequeno.

Riscos específicos:
- duplicar FAQ se o tema já renderizar outro bloco da coleção
- FAQPage JSON-LD não corresponder exatamente à FAQ visível
- mexer em descrição de coleção pode alterar espaçamento/altura pós-grade no mobile
- theme write em Production exige promoção controlada e rollback

## Rollback

Antes de aplicar:
- snapshot de `collection.descriptionHtml`
- snapshot de `collection.seo.title`
- snapshot de `collection.seo.description`
- se houver theme edit, backup do asset alvo e hash de DEV/Production

Rollback:
- restaurar description/SEO anteriores via Admin GraphQL
- restaurar asset anterior se houver alteração de tema
- readback Admin + HTML público + teste de schema

## QA necessário pós-DEV

- Admin readback da coleção
- HTML público/preview sem Liquid error
- H1/title/meta/canonical corretos
- FAQ visível aparece uma única vez
- FAQPage JSON-LD válido e com perguntas iguais às visíveis
- mobile: grid continua acima do guia; bloco pós-grade não empurra produto para baixo
- desktop: espaçamento e hierarquia visual consistentes

## Próxima decisão

Recomendação: aprovar **Opção A em DEV preview**, com escopo limitado à coleção `nike-vomero-5`.

Texto de aprovação sugerido:

`Aprovo DEV preview da melhoria da coleção Nike Vomero 5: limpar/atualizar conteúdo pós-grade e FAQ, adicionar FAQPage JSON-LD pareado, e preparar SEO title/meta propostos. Sem Production.`
