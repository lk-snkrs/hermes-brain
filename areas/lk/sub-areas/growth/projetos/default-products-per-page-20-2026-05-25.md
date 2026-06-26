# Frente de trabalho — reduzir produtos por página de 24 para 20

- Data: 2026-05-25
- Área: LK / Growth / Shopify CRO
- Status: aberta
- Pedido Lucas: mudar o default da quantidade base de produtos mostrados nas coleções de 24 para 20.

## Pedido limpo

Alterar o padrão do tema LK Collection para que coleções novas/sem override exibam 20 produtos por página em vez de 24.

## Evidência técnica inicial

Arquivo/seção identificada em snapshots locais do tema:

- Asset: `sections/lk-collection.liquid`
- Paginação usa: `{%- paginate collection.products by section.settings.products_per_page -%}`
- Setting atual no schema da seção:
  - `id`: `products_per_page`
  - `label`: `Produtos por página`
  - `min`: 8
  - `max`: 48
  - `step`: 4
  - `default`: 24

Achado nos snapshots locais:

- Produção/main: `tmp/lk-collection.155065417950.current.liquid`
- Dev/unpublished: `tmp/lk-collection.155065450718.current.liquid`

## Mudança proposta

Trocar apenas o default do schema:

```liquid
{ "type": "range", "id": "products_per_page", "label": "Produtos por página", "min": 8, "max": 48, "step": 4, "default": 20 }
```

## Atenção / QA necessário

- Verificar se templates JSON existentes já gravaram `products_per_page: 24`; se sim, mudar o schema default não altera páginas que já têm valor persistido no template/configuração.
- Se houver valor persistido no template de coleção, o pacote deve incluir também a atualização do template JSON correspondente ou confirmação via Theme Editor.
- Validar em dev primeiro:
  - grid de coleção desktop;
  - grid mobile;
  - paginação;
  - lazy loading/imagens;
  - coleções com menos de 20 produtos;
  - coleções com mais de 20 produtos;
  - performance percebida/CWV, especialmente mobile.

## Impacto esperado

- Menos produtos carregados na primeira página.
- Potencial melhora de performance/percepção de velocidade em coleções pesadas.
- Layout mais editorial e menos saturado antes dos blocos GEO/FAQ.
- Pode reduzir exposição inicial de produtos; precisa acompanhar conversão, cliques em paginação/filtros e scroll depth.

## Risco

Baixo a médio.

- Baixo tecnicamente se for apenas schema/default.
- Médio comercialmente se reduzir descoberta de produtos sem compensação por filtros/ordenação/coleções bem curadas.

## Rollback

Reverter `default: 20` para `default: 24` no mesmo asset e/ou restaurar backup do asset antes da alteração.

## Aprovação necessária

- Dev theme: pode ser preparado e testado sem nova aprovação, conforme autorização permanente para preview dev.
- Produção: exige aprovação explícita de Lucas no turno de publicação.

## Próximo passo recomendado

1. Auditar o tema dev e os templates JSON para confirmar se o valor 24 está persistido fora do schema.
2. Aplicar em dev com receipt/readback.
3. Validar em pelo menos 2 coleções: uma coleção grande e uma coleção editorial recém-criada.
4. Se aprovado visualmente, preparar pacote de produção com rollback.
