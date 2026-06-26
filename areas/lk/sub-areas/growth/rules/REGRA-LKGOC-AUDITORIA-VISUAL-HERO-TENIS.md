# Regra LKGOC — Hero de coleção deve usar prova social editorial/on-foot, não foto de produto

Atualizada em: 2026-06-05T17:31:43

## Correção de Lucas
Em heroes LKGOC de coleção de tênis, **não usar foto isolada de produto/catalogo** como imagem principal do hero/collage.

A função do hero é gerar desejo, validação social e leitura editorial premium. Portanto, a imagem deve mostrar **alguém usando o produto** ou uma cena editorial/lifestyle em que o tênis apareça com clareza.

## Fonte preferencial
Priorizar imagens editoriais de grandes portais/veículos de moda e cultura, por exemplo:
- Vogue;
- GQ;
- Hypebeast;
- Highsnobiety;
- W Magazine;
- Harper's Bazaar;
- veículos equivalentes de moda/streetwear/cultura.

## Regras obrigatórias para seleção visual
1. Hero/collage LKGOC deve usar imagem on-foot/lifestyle/editorial, nunca foto de produto isolado.
2. O sneaker precisa estar visível no crop real mobile e desktop.
3. A imagem deve funcionar como validador social: pessoa usando, styling, contexto de moda ou cultura.
4. Imagem editorial externa é preferível a catálogo interno quando cumpre os critérios acima.
5. Se o tênis não aparece, a imagem é reprovada mesmo vindo de veículo premium.
6. Quando necessário, ajustar crop para preservar a base do sneaker:
   - `object-position: center bottom` pode ser usado.
   - evitar `object-fit: contain` se deixar a imagem com aparência de catálogo/produto; usar apenas como exceção aprovada.
7. Produtos do catálogo LK podem servir como referência de modelo/cor, mas não como imagem de hero, salvo aprovação explícita.

## QA mínimo
- Validar screenshot mobile e desktop.
- Confirmar que há pessoa usando o produto ou cena editorial/lifestyle.
- Confirmar que o sneaker está visível e não cortado de forma comercialmente ruim.
- Registrar fonte/URL da imagem quando externa.

## Aplicação
A correção anterior da Mexico 66 usando imagens de produto do catálogo LK foi marcada como errada. Próximo ajuste deve voltar para imagens editoriais/on-foot de fontes premium, garantindo que o tênis esteja visível no render.
