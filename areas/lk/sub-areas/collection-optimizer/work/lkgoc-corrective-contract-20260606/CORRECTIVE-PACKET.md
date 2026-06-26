# LKGOC Corrective Contract — Puma/Nike/5 coleções

Data: 2026-06-06T15:58:57.082330+00:00

## Conclusão operacional
A entrega rejeitada não seguiu o LKGOC real porque criou snippets por coleção (`lk-goc-puma-speedcat-hero`, `lk-goc-puma-speedcat-guide-panel`) e fez adaptação visual. O padrão atual aprovado exige **componente único**.

## Fonte de verdade aberta
1. `LKGOC-PADRAO-CANONICO.md`  
   SHA: `3d9f39f182a13c36eb69e93ca8752572e72f8e31577f41984fdd9156215f3897`
2. `standards/LKGOC-PADRAO-CANONICO-COMPONENTE-UNICO.md`  
   SHA: `a32024785e3ade09dba3468f215caa957bbc1b8be5a7b2f8033bafab5dccd8f9`
3. Gold source coleção 204L final aprovado: `references/collection-204l-gold-source-final/README.md`  
   SHA: `2cd8a14442e8330c856c98001c070de9360aad56ce327d3f1d2969d728142cf3`
4. Componente Liquid real: `snippets/lk-goc-collection.liquid` snapshot `dev-readback-final`  
   SHA: `d3520a23efc99e52beda453c9023367c352873183370382fbd68526d9866d207`
5. Section real: `sections/lk-collection.liquid` snapshot `dev-readback-final`  
   SHA: `744d60b85b2d148b55fea5cf9265b7f484e0f1197d0b82bdc4bd796b85964712`

## Contrato correto
- Não criar snippet visual por coleção.
- Usar `snippets/lk-goc-collection.liquid` como único entrypoint.
- Section deve renderizar:
```liquid
{% render 'lk-goc-collection', collection: collection, part: 'hero' %}
{% render 'lk-goc-collection', collection: collection, part: 'guide' %}
```
- Variação por coleção = dados/branch `case collection.handle`, não layout novo.
- Handles já migrados no snapshot real: `new-balance-204l, new-balance-9060, new-balance-530, onitsuka-tiger-mexico-66, adidas-samba, new-balance-204l, new-balance-9060, new-balance-530, onitsuka-tiger-mexico-66, adidas-samba`.

## O que precisa ser desfeito
- Remover do DEV o branch/render do Puma criado fora do componente único.
- Remover snippets rejeitados:
  - `snippets/lk-goc-puma-speedcat-hero.liquid`
  - `snippets/lk-goc-puma-speedcat-guide-panel.liquid`
- Revalidar Nike Dunk porque foi feita antes desta correção de rota.

## Próxima execução permitida
1. Restaurar DEV para o snapshot/contrato do componente único.
2. Adicionar **uma coleção por vez** no `lk-goc-collection.liquid`.
3. Primeiro Puma ou Nike — não lote de 5.
4. Só enviar preview quando o diff provar que:
   - seção usa componente único;
   - não existem snippets novos por coleção;
   - CSS/classes seguem `lk-goc-*` + compat 204L;
   - guia pós-grid é o mesmo contrato visual;
   - QA lado a lado passa.

## Bloqueio técnico atual
Este profile não tem variáveis Shopify Admin no `.env`; portanto ainda não consegui executar rollback DEV por API neste turno. Não há receipt de rollback aplicado.
