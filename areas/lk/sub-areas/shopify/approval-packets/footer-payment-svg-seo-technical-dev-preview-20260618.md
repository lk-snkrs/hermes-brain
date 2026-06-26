# Approval packet — SEO técnico footer/payment SVG — 20260618T1731Z

- values_printed: false
- escopo executado: read-only
- nenhum write Shopify/Git/tema foi executado

## Objetivo

Revalidar o ruído técnico de HTML associado aos SVGs de formas de pagamento no footer LK e preparar uma correção segura para DEV, se Lucas quiser limpar esse ponto da auditoria.

## Evidência pública atual

Validação em 3 superfícies não relacionadas:

1. Home — `https://lksneakers.com.br/`
2. Collection — `https://lksneakers.com.br/collections/sneakers`
3. Cart — `https://lksneakers.com.br/cart`

Artefatos:

- Diretório: `/opt/data/profiles/lk-shopify/cron/output/footer_svg_seo_20260618`
- Summary público: `/opt/data/profiles/lk-shopify/cron/output/footer_svg_seo_20260618/summary-20260618T173020Z.json`

Resultados comuns nas 3 páginas:

- status HTTP: `200`
- `.ft__payments` encontrado: `true`
- SVGs de pagamento renderizados: `7`
- `pi-discover` presente: `true`
- title/canonical/H1 presentes: `true`

W3C/Nu validator encontrou erros relevantes globais no footer:

- `.ft__payments` usa `aria-label` em `div` sem role semântico;
- SVG Discover contém `stop` sem atributo `offset` em gradientes;
- esse padrão aparece em Home, Collection e Cart com linhas diferentes, o que confirma origem global/footer.

Amostra dos erros relevantes:

- Home:
  - `The “aria-label” attribute must not be specified on any “div” element unless the element has a “role” value...`
  - `Element “stop” is missing required attribute “offset”.`
- Collection: mesmos tipos de erro no bloco `.ft__payments`.
- Cart: mesmos tipos de erro no bloco `.ft__payments`.

## Readback Admin Production

Arquivo:

`/opt/data/profiles/lk-shopify/cron/output/footer_svg_seo_20260618/production-footer-source-readback-20260618T173110Z.json`

Theme:

- production_theme_id: `155065417950`
- asset: `sections/lk-footer.liquid`
- footer_hash: `03a9ec6e388871d7f32f383826c3d534606f1033fe5c7d2f4daa959d02278117`

Origem exata no Liquid:

```liquid
<div class="ft__payments" aria-label="Formas de pagamento aceitas">
  {%- for type in shop.enabled_payment_types limit: 6 -%}
    {{ type | payment_type_svg_tag: class: 'ft__payment' }}
  {%- endfor -%}
</div>
```

Interpretação:

- O erro não é específico da Home, coleção ou cart.
- A origem é global: `sections/lk-footer.liquid`.
- Parte do HTML problemático é gerado pelo filtro Shopify `payment_type_svg_tag`, especialmente o SVG Discover.

## Severidade

Classificação: baixa para SEO real, média para higiene técnica/auditoria.

Por quê:

- As páginas retornam `200`.
- Tags primárias estão presentes: title, canonical, H1.
- O problema é no footer, em badges de pagamento.
- O ruído aparece em validadores/crawlers e pode reduzir score técnico/percepção de limpeza.

## Proposta recomendada — Opção B

Fazer preview em DEV de um ajuste mínimo no footer:

1. Trocar:

```liquid
<div class="ft__payments" aria-label="Formas de pagamento aceitas">
```

por:

```liquid
<div class="ft__payments" role="group" aria-label="Formas de pagamento aceitas">
```

2. Pular apenas o tipo `discover`, que é o SVG que traz os `stop` sem `offset`:

```liquid
{%- assign lk_payment_rendered = 0 -%}
{%- for type in shop.enabled_payment_types -%}
  {%- unless type == 'discover' -%}
    {{ type | payment_type_svg_tag: class: 'ft__payment' }}
    {%- assign lk_payment_rendered = lk_payment_rendered | plus: 1 -%}
    {%- if lk_payment_rendered >= 6 -%}{%- break -%}{%- endif -%}
  {%- endunless -%}
{%- endfor -%}
```

Diff local preparado:

`/opt/data/profiles/lk-shopify/cron/output/footer_svg_seo_20260618/proposed-lk-footer-skip-discover-role-group.diff`

Target local preparado:

`/opt/data/profiles/lk-shopify/cron/output/footer_svg_seo_20260618/proposed-lk-footer-skip-discover-role-group.liquid`

## Preview/QA proposto para DEV, se aprovado

Após aprovação explícita para DEV theme upload:

1. Snapshot do `sections/lk-footer.liquid` em DEV e Production.
2. Upload apenas em DEV/unpublished theme.
3. Readback hash/linhas do asset DEV.
4. Confirmar Production unchanged.
5. Preview público/autenticado ou API readback:
   - footer visível;
   - formas de pagamento ainda renderizam;
   - Discover ausente;
   - `.ft__payments` com `role="group"`;
   - validar Home/Collection/Cart DEV no W3C/Nu quando possível.

## Risco

- Pequena alteração visual no footer: Discover pode deixar de aparecer.
- Se a lista de payment types tiver poucos itens, pode renderizar menos ícones.
- Baixo risco funcional: não altera checkout, pagamento real, preço, produto, estoque ou carrinho.
- É uma mudança visual/theme, então Production precisa aprovação separada depois de DEV.

## Rollback

- Reverter `sections/lk-footer.liquid` para o snapshot anterior.
- Diff é isolado em um único bloco do footer.
- Sem alteração em app, checkout, produtos, preços ou estoque.

## Decisão recomendada

Recomendação: aprovar **DEV preview da Opção B**.

Não recomendo aplicar direto em Production. Primeiro validar visual e auditoria em DEV.
