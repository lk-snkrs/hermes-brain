# Diagnóstico robots.txt — SEMrush format error

Data UTC: `2026-06-18T22:32:57Z`
Escopo: read-only; writes externos = 0; values_printed=false

## Evidência pública

- URL: `https://lksneakers.com.br/robots.txt`
- HTTP: `200`
- Content-Type: `text/plain; charset=utf-8`
- `www` redireciona corretamente para domínio raiz.

## Causa provável do erro SEMrush

O arquivo tem linhas em branco dentro dos blocos `User-agent` antes de diretivas `Allow`.

Trechos críticos:

- Linha 41 em branco encerra o grupo `User-agent: *` para parsers estritos.
- Linhas 42–44 ficam como `Allow` fora de qualquer grupo.
- Linha 64 em branco encerra o grupo `User-agent: Googlebot` para parsers estritos.
- Linhas 65–68 ficam como `Allow` fora de qualquer grupo.

Um parser mais permissivo pode aceitar; um parser estrito, como o SEMrush aparenta usar, marca como erro de formato.

## Segundo ponto importante

O arquivo também contém:

```txt
User-agent: SemrushBot
Disallow: /
```

Isso bloqueia o SemrushBot. Não é erro de formato por si só, mas pode limitar auditorias do SEMrush. Decidir liberar ou não é decisão comercial/técnica separada.

## Correção recomendada de baixo risco

Remover apenas as linhas em branco internas dentro dos grupos, mantendo as mesmas regras.

Antes:

```txt
Disallow: /password

Allow: /products/
Allow: /collections/
Allow: /blogs/
```

Depois:

```txt
Disallow: /password
Allow: /products/
Allow: /collections/
Allow: /blogs/
```

E o mesmo no bloco `Googlebot`.

## Aprovação necessária

Alterar `templates/robots.txt.liquid` em production theme é write público em Shopify. Exige aprovação explícita.

## Rollback

Restaurar backup do asset `templates/robots.txt.liquid` antes do PUT.
