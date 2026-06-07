# REGRA LKGOC — Guia dedicado sem imagem de produto ou pessoa usando produto

Data: 2026-06-06
Origem: correção direta Lucas após reprovação do Guia Nike Dunk.

## Regra

Para **Guia LK / página dedicada LKGOC** (`/pages/guia-*`), não usar:

- imagem de pessoa usando o produto;
- imagem do produto isolado / packshot / PDP;
- card visual baseado em foto de produto;
- hero com produto ou pessoa usando o produto.

## Como executar

- O guia deve ser sustentado por hierarquia editorial, tipografia, cards textuais, comparativos, FAQ, CTA e blocos citáveis.
- Se houver seleção de produtos, usar cards textuais/linkados, sem `<img>`.
- QA técnico obrigatório: `body_html` do guia precisa ter `0` ocorrências de `<img` antes de enviar link ao Lucas.
- QA visual obrigatório: print mobile/desktop após a correção.

## Motivo

Lucas reforçou que isso já faz parte do LKGOC e que o uso de imagem de produto/pessoa usando produto reprova o padrão.
