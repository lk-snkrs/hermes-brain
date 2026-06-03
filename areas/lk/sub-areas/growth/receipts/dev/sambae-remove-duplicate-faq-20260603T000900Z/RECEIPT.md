# Receipt — Sambae DEV remove duplicate FAQ/content

Data UTC: 2026-06-02T23:58:43Z
Tema: `155065450718` (`lk-new-theme/dev`, unpublished)
Produção alterada: **não**.

## Correção aplicada
Adicionado `lk_desc_override` para `collection.handle == 'adidas-sambae'` em `sections/lk-collection.liquid`.

Efeito:
- o banner não puxa mais o HTML longo antigo da descrição da coleção;
- o bloco nativo/rico abaixo do grid é pulado pela regra já existente `collection.description != blank and lk_desc_override == blank`;
- permanece apenas o FAQ novo dentro do Guia LK (`#lk-guia-adidas-sambae`).

## QA render depois
```json
{
  "url": "https://lksneakers.com.br/collections/adidas-sambae?preview_theme_id=155065450718&qa=remove-dupe-faq-2",
  "status": 200,
  "final_url": "https://lksneakers.com.br/collections/adidas-sambae?qa=remove-dupe-faq-2",
  "bytes": 562369,
  "counts": {
    "lk-guia-adidas-sambae": 27,
    "Perguntas frequentes": 2,
    "Sobre Adidas Sambae": 1,
    "Como Escolher o Melhor Adidas Sambae": 0,
    "coll-rich-content": 0,
    "Qual a diferença entre Adidas Samba e Sambae": 2,
    "O Adidas Sambae é feminino": 2,
    "lk-collection-v2--adidas-sambae": 1,
    "open204LReveal": 3,
    "Sambae traduz a família Samba": 1
  }
}
```

## Screenshot
- `preview-after-desktop.png`: exists=True bytes=866634

## Rollback
Reaplicar `section.before.liquid` no asset `sections/lk-collection.liquid` do tema DEV.
