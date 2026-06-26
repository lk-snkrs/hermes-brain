# Regra LKGOC — alinhamento das imagens pelo bottom

Registrado em: 2026-06-05T21:23:18.806566+00:00

## Regra

Em heroes LKGOC com imagens editoriais/de uso, o enquadramento deve preservar a base visual pelo **bottom**.

Padrão CSS obrigatório quando a imagem estiver em card/collage com `object-fit: cover`:

```css
object-position: center bottom;
```

Não usar como padrão:

- `object-position: center center`;
- enquadramento pelo meio;
- crop que corta a base/pé/produto em uso sem decisão explícita.

## Motivo

A leitura comercial do LKGOC precisa mostrar o produto em uso com a base/footwear ancorada. Centralizar pelo meio pode priorizar tronco/cenário e perder o tênis, enfraquecendo o objetivo da coleção.

## Aplicação

- QA visual deve checar não só presença de imagem, mas o crop: produto em uso visível e ancorado pelo bottom.
- Se CSS legado sobrescrever `object-position`, aplicar regra mais específica ou inline no DEV, e registrar no receipt.
- Production apenas após QA com `object-position` efetivo em `center bottom` / `50% 100%`.
