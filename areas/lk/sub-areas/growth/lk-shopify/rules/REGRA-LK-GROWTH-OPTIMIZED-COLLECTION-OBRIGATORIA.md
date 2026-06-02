# REGRA — LK Growth Optimized Collection obrigatória

Criado em: 2026-06-01 19:50:47

## Regra absoluta

Toda coleção da LK Sneakers que for otimizada, melhorada, refeita, atualizada para SEO/GEO/CRO, ou receber guia/layout editorial deve obrigatoriamente passar pelo fluxo:

**LK Growth Optimized Collection**

Isso vale para qualquer pedido futuro de:

- otimizar coleção;
- melhorar SEO de coleção;
- melhorar GEO/AI Search/LLM de coleção;
- melhorar CRO de coleção;
- reescrever descrição de coleção;
- criar guia de coleção;
- atualizar layout de coleção;
- aplicar padrão 204L/Moon Shoe;
- atualizar hero/collage;
- adicionar Guia Editorial LK;
- melhorar coleção por ordem de visitas;
- atualizar coleções já otimizadas.

## O que é obrigatório

Uma coleção só pode ser tratada como otimizada se seguir o contrato completo **LK Growth Optimized Collection**:

1. passar pela skill `lk-superpowers-collection-optimizer`;
2. passar pela camada pensante **CLAUDE-SEO**;
3. usar texto de coleção no padrão SEO/GEO LK;
4. ter primeiro parágrafo forte antes do “Ler mais”;
5. usar layout `lk-collection-v2`/204L gold source quando aplicável;
6. ter hero/collage atualizado;
7. usar imagens editoriais reais, não PDP/packshot;
8. ter Guia Editorial LK pós-grid;
9. ter guia dedicado `/pages/guia-[handle]`;
10. ter seção visível “Referências editoriais e contexto”;
11. ter FAQ/schema correto;
12. preparar tag Shopify `LK Growth Optimized Collection`;
13. preparar metafields `lk_growth.*`;
14. registrar/atualizar ledger local;
15. validar em DEV;
16. gerar approval packet;
17. ter rollback/receipt;
18. publicar em produção apenas com aprovação explícita.

## Proibição

Não é permitido fazer “otimização parcial” de coleção e chamar de otimizada.

Se o pedido parecer pequeno — por exemplo, “melhorar só o texto da coleção” — o agente deve:

- avisar que isso toca o padrão LK Growth Optimized Collection;
- verificar se a coleção já é tagueada/registrada;
- se não for, propor entrada no fluxo completo ou registrar como exceção temporária;
- nunca esquecer guia dedicado, tag/metafield e ledger quando a otimização for final.

## Atualização em lote

Quando uma coleção tiver a tag/registro **LK Growth Optimized Collection**, qualquer atualização de layout/padrão deve considerar todas as coleções tagueadas.

Fluxo obrigatório:

1. consultar ledger/tag/metafields;
2. listar coleções afetadas;
3. aplicar alteração em todas no DEV;
4. gerar QA em lote;
5. pedir aprovação para produção;
6. publicar só com aprovação explícita.

## Fonte operacional

Skill principal:

`skills/lk-superpowers-collection-optimizer/SKILL.md`

Ledger:

`ledgers/lk-optimized-collections-ledger.json`

## Status

Regra aprovada por Lucas e obrigatória para LK Growth.


---

Nota LK Shopify (2026-06-01 19:51:55): esta regra também se aplica ao agente/área LK Shopify. Qualquer alteração de Shopify collection relacionada a otimização SEO/GEO/CRO/layout/guia deve respeitar o fluxo LK Growth Optimized Collection e exigir aprovação para produção.
