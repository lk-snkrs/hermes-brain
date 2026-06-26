# LKGOC Gold Source — NB204L Guide / Source Page

Registrado em: 2026-06-03T18:37:40.151852+00:00

## Status

Este diretório salva o padrão aprovado por Lucas para **páginas guia/source page LKGOC**, usando a página:

- Página: New Balance 204L Original Brasil | LK Sneakers
- Handle: `new-balance-204l-original-brasil-guia-lk`
- Preview DEV aprovado: `https://lksneakers.com.br/pages/new-balance-204l-original-brasil-guia-lk?preview_theme_id=155065450718&lkgoc_gold=20260603T183737Z`
- Tema fonte: `lk-new-theme/dev` `155065450718`
- Role verificado no registro: `unpublished`

## Decisão Lucas

Lucas aprovou o layout como **perfeito** e pediu para salvar como padrão no LKGOC.

## Regra canônica para novas guide/source pages LKGOC

Copiar e adaptar este padrão, sem inventar layout novo:

- Hero editorial escuro, premium e full-width.
- Conteúdo abaixo com largura editorial consistente.
- Tabela de colorways/atributos quando aplicável.
- Cards de styling em grid.
- Bloco **Sinais editoriais** em grid.
- Cards de produtos em grid.
- FAQ visual + FAQ JSON-LD em paridade.
- CTA final para coleção.
- Tom LK: premium, humano, minimalista e comercialmente inteligente.

## Regra mobile aprovada

No mobile, os blocos abaixo devem manter **2 colunas**:

- `lk-style-grid` / Como usar.
- `lk-media-grid` / Sinais editoriais.
- `lk-products` / Produtos.
- `section.lk-faq` / Perguntas frequentes.

Não voltar esses blocos para `1fr` no mobile sem aprovação explícita de Lucas.

## FAQ

- FAQ visual deve ficar com número par de perguntas quando estiver em 2 colunas.
- FAQ schema deve refletir o mesmo conjunto de perguntas do HTML.
- Nesta versão: 6 perguntas no HTML e 6 perguntas no JSON-LD.

## Namespace e transição

- Para guide/source page, namespace visual atual: `lk-source-page--nb204l` e classes internas `lk-*` do padrão da página.
- Para collections LKGOC, gold source separado continua sendo 204L collection com `lk-goc-*`.
- Não usar `lk-lkgoc-*`.

## Arquivos

- `gold-source-dev-nb204l-guide-section.liquid`: fonte canônica atual.
- `snapshot-20260603T183737Z.liquid`: snapshot imutável do registro.
- `preview-snapshot-20260603T183737Z.html`: HTML público do preview no momento do registro, quando disponível.

## Checks do registro

```json
{
  "dev_unpublished": true,
  "has_v2_marker": true,
  "has_mobile_two_col_marker": true,
  "has_faq_two_col_marker": true,
  "has_article": true,
  "has_style_grid": true,
  "has_media_grid": true,
  "has_products_grid": true,
  "has_faq": true,
  "has_faq_schema": true,
  "faq_6_details": true,
  "no_lkgoc_class": true,
  "under_limit": true,
  "public_preview_200": true,
  "public_two_col_seen": true,
  "public_no_liquid": true,
  "public_no_imagem_pendente": true
}
```

## Hash

- SHA256 section: `2106b816edfb063c8c9678a8b451c1934b0442bcc99257c28c4a549171d1ceae`
- Bytes: `27683`
