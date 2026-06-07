# Regra LKGOC — Definition of Done e QA antes de dizer “feito”

Registrado em: 20260606T133050Z

## Erro corrigido
Não confundir página abrindo no preview DEV (`200`) ou presença de hero/editorial genérico com LKGOC concluído.

## Regra obrigatória
O agente só pode dizer que uma coleção/guia LKGOC está **feito**, **pronto**, **aplicado** ou enviar como entrega final quando existir evidência mínima:

1. **DEV/unpublished verificado por API** para qualquer alteração de tema.
2. **Readback Shopify Admin API** do asset/template/metafield/page alterado.
3. **Componente LKGOC específico presente**, não apenas classes globais do tema.
4. **Hero LKGOC real** quando for coleção.
5. **Bloco Guia/FAQ ou estrutura editorial canônica** quando aplicável.
6. **FAQPage schema/Product/Collection schema validado** quando parte do escopo.
7. **QA visual mobile e desktop** ou, se ainda não feito, marcar explicitamente como pendente.
8. **Receipt local** com links DEV, assets alterados, rollback e evidência.

## Linguagem obrigatória
- Se apenas a URL abre em DEV: dizer “link DEV bruto / página existente”, não “feito”.
- Se ainda não houve readback + QA: dizer “em preparação” ou “pendente de QA”.
- Se guia Page Shopify ainda retorna 404: dizer “guia ainda não criado/publicado”.

## Checklist antes de responder ao Lucas
Antes de afirmar conclusão, verificar:
- HTTP 200 do preview;
- marcador `lk-goc-*` específico do componente alvo;
- conteúdo textual da coleção/guia alvo;
- schema quando aplicável;
- readback do asset/template/page;
- screenshot/QA ou pendência explícita.

## Aplicação
Esta regra se aplica a todo lote LKGOC, incluindo Nike Dunk, Puma Speedcat, Adidas Gazelle, Yeezy, Labubu e qualquer futuro guia/coleção.
