# Template — HTML de produto / PDP Shopify LK

Status: template inicial para aprovação visual e lógica; não publicado na Shopify.
Arquivo HTML: `lk-product-pdp-html-preview.html`

## Objetivo

Quando o LK Operating System gerar uma oportunidade de produto, ele deve produzir também um **layout HTML de PDP/produto** para aprovação, não apenas um Markdown/copy solta.

## Regra

Todo output de produto deve incluir:

- layout/HTML de PDP seguindo DesignMD LK;
- bloco de curadoria;
- detalhes do produto;
- disponibilidade por tamanho/variante;
- status comercial: pronta entrega aparente, encomenda BR, encomenda US ou a confirmar;
- preço sugerido LK, quando aplicável;
- campos auxiliares Shopify: SEO title, meta description, handle, tags, coleções, alt text, FAQ;
- nota de aprovação antes de publicar.

## Restrições

- Não prometer pronta entrega sem validar Tiny.
- Não publicar Shopify sem aprovação explícita.
- Não alterar tema publicado sem PR/diff/preview/aprovação.
- HTML é draft de layout e precisa ser adaptado ao tema real da LK antes de produção.

## Aprendizado registrado

Lucas aprovou o PRD/MD, mas corrigiu que o que precisava aprovar agora era o **layout em HTML do produto**, não outro Markdown por e-mail. Portanto, próximos testes de produto devem entregar artefato visual HTML direto para aprovação.
