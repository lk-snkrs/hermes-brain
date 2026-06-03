# Approval packet — Correção LKGOC Samba Jane hero + guia

Data: 2026-06-02

## Causa raiz

A implementação anterior saiu errada por dois motivos:

1. **Hero errado:** foi usado collage/packshot de produto no hero da coleção Samba Jane. Isso viola o padrão LKGOC aprovado por Lucas para guia/editorial, que exige imagem de pessoa usando o produto ou contexto editorial forte.
2. **Guia pós-grid errado:** o bloco "Guia editorial LK" estava vindo de trecho inline antigo em `sections/lk-collection.liquid`, não do padrão clonado corretamente da gold source New Balance 204L.

## O que foi verificado

- `snippets/lk-samba-jane-lkgoc-v2.liquid` tinha/servia hero com produto.
- `sections/lk-collection.liquid` continha bloco inline antigo para `collection.handle == 'adidas-samba-jane'` com H2 antigo: `Adidas Samba Jane: Mary Jane sneaker, perfil baixo e curadoria LK`.
- O preview público/Section Rendering API ainda retornou código antigo, mesmo após readback correto do dev theme, indicando cache/render path contaminado no preview.

## Correção preparada em DEV

Theme: `155065450718` — `lk-new-theme/dev`.

- Criado snippet novo: `snippets/lk-samba-jane-editorial-v3.liquid`.
- Section dev alterada para renderizar `lk-samba-jane-editorial-v3` em vez do snippet antigo.
- Snippet novo remove packshots e usa slot editorial pendente, sem copiar/hotlinkar Vogue/ELLE/GQ.
- Guia inline dev atualizado para novo H2 e bullets mais alinhados ao padrão 204L.

## Guardrail de imagem

Vogue/ELLE/GQ podem ser usados como referência editorial/pesquisa de styling. Não copiar nem hotlinkar imagem editorial de terceiros sem licença. Para produção, usar:

- asset LK próprio; ou
- imagem licenciada; ou
- imagem autorizada/baixada de fornecedor com direito de uso; ou
- manter slot editorial/hero sem imagem até Lucas aprovar asset.

## Aprovação necessária

Para corrigir produção:

- aprovar substituição do hero atual com packshots por versão editorial sem imagem/slot pendente; ou
- fornecer/aprovar URL de imagem licenciada/asset LK de pessoa usando Samba Jane; e
- aprovar update em `sections/lk-collection.liquid` production + snippet novo production.

## Rollback

- Restaurar backups dos assets antes do write.
- Remover render `lk-samba-jane-editorial-v3` e voltar ao estado anterior, se necessário.

## Status

Não publicar produção sem aprovação explícita atual de Lucas.
