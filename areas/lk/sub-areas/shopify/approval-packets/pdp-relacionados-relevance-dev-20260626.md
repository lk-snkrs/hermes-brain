# Approval packet — PDP Relacionados relevância — DEV

Data: 2026-06-26  
Agente: lk-shopify  
Superfície: Shopify theme DEV/unpublished / `sections/lk-pdp.liquid`

## Pedido

Lucas apontou no mobile que o bloco **Você também pode gostar / Relacionados** do PDP está ruim, misturando produtos sem relação clara. Exemplo visual: PDP de boné mostrando New Balance 9060 junto de bonés.

## Diagnóstico read-only

Fonte atual no tema `sections/lk-pdp.liquid`:

```liquid
{%- assign related_collection = product.collections.first -%}
{%- for related in related_collection.products limit: 4 -%}
  {%- unless related.id == product.id -%}
    {% render 'lk-product-card', product: related %}
  {%- endunless -%}
{%- endfor -%}
```

Problema:

- usa `product.collections.first`, que pode ser uma coleção ampla ou ambígua;
- pega os 4 primeiros produtos sem checar tipo, vendor, família ou contexto;
- filtra o produto atual só depois do `limit: 4`, podendo deixar grade fraca;
- para bonés, a coleção pode conter produtos cujo texto inclui “Bone/Bone Sparrow” mas que são tênis, então o bloco fica editorialmente errado.

## Evidência pública read-only

PDP Saint George Bege/Marrom:

- URL: `https://lksneakers.com.br/products/bone-aime-leon-dore-saint-george-logo-hat-bege-marrom`
- Relacionados atuais detectados:
  - `/products/bone-5-panel-aime-leon-dore-unisphere-branco`
  - `/products/tenis-new-balance-9060-bone-sparrow-marrom` ← ruim para PDP de boné
  - `/products/bone-slyce-vintage-stadium-off-white`
  - `/products/bone-slyce-championship-2-0-navy-azul-marinho`
- HTTP `200`
- Liquid errors `0`

## Proposta DEV

Trocar a lógica do bloco `Relacionados` por uma seleção filtrada e mais segura, sem mexer em Curadoria LK:

1. Ainda usar a coleção existente como fonte, mas não aceitar qualquer item.
2. Renderizar em passagens, até 4 cards:
   - prioridade 1: mesmo `product.type` + mesmo `vendor`;
   - prioridade 2: mesmo `product.type`;
   - prioridade 3: mesmo `vendor` somente se ainda faltarem cards.
3. Excluir produto atual antes de contar.
4. Aumentar o scan da coleção para `limit: 32`, mas renderizar no máximo 4.
5. Se não houver ao menos 2 relacionados razoáveis, esconder o bloco em vez de mostrar grade ruim.

## Escopo aprovado nesta solicitação

Proposto para DEV/unpublished apenas:

- `sections/lk-pdp.liquid`
- lógica Liquid do bloco `Related products` / `Relacionados`

## Fora de escopo

- Sem produto/preço/estoque/Tiny/checkout/GMC/Klaviyo/ads/WhatsApp.
- Sem alterar Curadoria LK (`lk-variante`) já publicada.
- Sem Production merge nesta etapa.
- Sem prometer disponibilidade.

## QA DEV

Testar pelo menos:

1. PDP boné Saint George Bege/Marrom:
   - não pode aparecer `tenis-new-balance-9060-bone-sparrow-marrom` em Relacionados;
   - deve manter bonés/ALD/Slyce se forem tipo compatível;
   - Liquid errors `0`.
2. PDP Air Jordan 1 Low:
   - relacionados não devem virar acessórios/apparel;
   - produto atual excluído.
3. PDP Onitsuka Mexico 66:
   - relacionados não devem puxar NB/Samba se houver Onitsuka ou tipo/família melhor disponível.
4. Mobile grid continua 2 colunas.

## Risco

Baixo/médio:

- melhora relevância sem mudar produto ou estoque;
- pode reduzir quantidade de cards em alguns PDPs se a coleção estiver muito ruim;
- preferível a mostrar recomendações incoerentes.

## Rollback

Restaurar o bloco atual:

```liquid
{%- assign related_collection = product.collections.first -%}
{%- for related in related_collection.products limit: 4 -%}
  {%- unless related.id == product.id -%}
    {% render 'lk-product-card', product: related %}
  {%- endunless -%}
{%- endfor -%}
```

## Aprovação necessária

Para aplicar em DEV:

> Aprovo DEV correção do bloco Relacionados do PDP com filtro por tipo/vendor, sem Production merge.

## Reminder OS

- loop needed: yes
- owner: lk-shopify
- next action: aguardar aprovação DEV; se aprovada, aplicar patch em `sections/lk-pdp.liquid`, fazer readback e QA nos PDPs âncora.
- review trigger: resposta do Lucas aprovando DEV ou ajustando regra de recomendação.
- evidence: este approval packet + diagnóstico read-only público.
