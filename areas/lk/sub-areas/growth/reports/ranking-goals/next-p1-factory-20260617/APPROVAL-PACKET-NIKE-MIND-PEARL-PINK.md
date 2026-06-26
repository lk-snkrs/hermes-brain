# Approval Packet — Nike Mind 001 Pearl Pink — Lote 2

Status: **preparado, não executado**.

Motivo para não executar agora: o Black Chrome está OK no Admin Shopify, mas o HTML público ainda está com propagação mista. Recomendo esperar consistência pública antes de novo write.

## URL

`/products/slide-nike-mind-001-pearl-pink-rosa`

## Evidência

- Mesmo cluster de demanda do Nike Mind 001.
- GSC baseline citado pela factory: **11 cliques / 30.802 impressões / CTR 0,04% / posição 9,0**.
- Produto ativo no Shopify e sem FAQ no Admin read-only.
- SEO atual é genérico: `Slide Nike Mind 001 Pearl Pink | LK Sneakers`.

## Escopo proposto

Executar somente:

- `seo.title`
- `seo.description`
- `descriptionHtml` com bloco answer-first + FAQ

Bloqueado:

- preço
- estoque
- desconto
- feed/GMC
- campanhas
- theme production fora do escopo
- checkout
- Klaviyo/WhatsApp
- outros produtos

## Campos propostos

Title:
`Nike Mind 001 Pearl Pink Original no Brasil | LK`

Meta:
`Nike Mind 001 Pearl Pink original no Brasil: slide sensorial Nike em rosa claro, com curadoria exclusiva LK, autenticidade e atendimento humano.`

Bloco copy:

> O Nike Mind 001 Pearl Pink é a leitura mais suave e escultural do slide Nike Mind 001, combinando forma anatômica, design sensorial e acabamento rosa claro com presença de moda. A colorway Pearl Pink funciona para quem busca um Nike Mind original no Brasil com visual mais leve, mas ainda futurista. Na LK, a curadoria prioriza pares autênticos, seleção premium e atendimento humano para orientar modelo, tamanho e proposta de uso. O Pearl Pink combina bem com looks monocromáticos, denim claro, alfaiataria casual e produções minimalistas em que o slide entra como ponto de design.

FAQ:

### O Nike Mind 001 Pearl Pink é original?
Sim. A LK trabalha com curadoria de produtos originais e atendimento humano para orientar a compra com segurança em modelos Nike Mind de alta procura.

### Onde comprar Nike Mind 001 Pearl Pink no Brasil?
Procure uma curadoria que detalhe modelo, colorway, fotos, autenticidade e suporte para escolha de tamanho. A LK reúne seleção premium e atendimento humano para uma compra mais segura.

### O Nike Mind 001 Pearl Pink tem forma grande ou pequena?
A percepção de forma pode variar conforme o pé e a referência que você usa em slides ou sneakers. Para uma escolha mais segura, confirme a numeração com atendimento humano antes da compra.

### Qual a diferença entre Nike Mind 001 Pearl Pink e Black Chrome?
A estrutura do Nike Mind 001 mantém a proposta de slide escultural. A diferença principal está na colorway: Pearl Pink tem leitura mais clara e suave; Black Chrome tem visual mais escuro, técnico e impactante.

### Como usar o Nike Mind 001 Pearl Pink?
A colorway Pearl Pink combina com denim claro, tons neutros, alfaiataria casual e looks minimalistas. O modelo funciona melhor quando aparece como peça de design no styling.


## Rollback

Antes de qualquer write:

- backup de `seo.title`, `seo.description`, `descriptionHtml`;
- mutation limitada ao produto Pearl Pink;
- readback Admin + HTML público/cache-bust;
- se QA falhar, restaurar backup.

## Critério para avançar

Só executar depois de:

1. Black Chrome público consistente em nova rodada de QA; ou
2. aprovação explícita de Lucas para seguir mesmo com propagação mista do storefront.

values_printed=false
