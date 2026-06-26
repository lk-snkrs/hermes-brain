# Approval packet — LK Collection Suggestion DEV completo

Gerado: 2026-06-08 12:45 BRT

## Pedido limpo

Aplicar no **DEV via GitHub/dev** o projeto **LK Collection Suggestion**: mapa completo de coleções públicas elegíveis para sugerir até 2–3 coleções compactas na busca.

Este packet não executa upload/merge. Nenhum produto, coleção, preço, estoque, app, Search & Discovery, GMC, ads, Klaviyo ou campanha será alterado por este packet.

## Artefatos locais

- PRD: `areas/lk/sub-areas/shopify/prd/lk-collection-suggestion-prd-20260608.md`
- Workspace: `/opt/data/profiles/lk-shopify/workspace/lk-collection-suggestion-20260608`
- Source atual: `/opt/data/profiles/lk-shopify/workspace/lk-collection-suggestion-20260608/production_source_sections__lk-search.liquid`
- Target proposto: `/opt/data/profiles/lk-shopify/workspace/lk-collection-suggestion-20260608/target_sections__lk-search.liquid`
- Mapa: `/opt/data/profiles/lk-shopify/workspace/lk-collection-suggestion-20260608/collection_search_map.json`
- Verificação: `/opt/data/profiles/lk-shopify/workspace/lk-collection-suggestion-20260608/verification.json`

## Descoberta read-only

- Source Production SHA12: `261b18011b56`
- Source DEV SHA12: `261b18011b56`
- DEV = Production no asset atual: `True`
- Coleções públicas lidas: `178`
- Coleções elegíveis mapeadas: `167`
- Coleções rejeitadas por regra: `11`

## Verificação estática

- Target SHA12: `384fff2e6d3c`
- Tamanho: `38998` bytes
- Abaixo do limite Shopify 256 KB: `True`
- Alias 204L presente: `True`
- Alias 9060 presente: `True`
- Alias 530 presente: `True`
- Queries genéricas sem hit (`sneakers`, `roupas`, `sale`, `lançamentos`): `True`
- Card antigo grande ausente: `True`
- Busca product-only/grid preservados: `True`
- Sem tags Liquid inválidas `{{%- assign/capture/if`: `True`
- Delimitador seguro `|#|`: `True`

## QA simulado de queries

```json
{
  "204L": [
    {
      "handle": "new-balance-204l",
      "title": "New Balance 204L",
      "score": 100
    }
  ],
  "9060": [
    {
      "handle": "new-balance-9060",
      "title": "New Balance 9060",
      "score": 100
    }
  ],
  "530": [
    {
      "handle": "new-balance-530",
      "title": "New Balance 530",
      "score": 100
    }
  ],
  "Samba": [
    {
      "handle": "samba",
      "title": "Adidas Samba",
      "score": 100
    }
  ],
  "samba verde": [
    {
      "handle": "samba",
      "title": "Adidas Samba",
      "score": 100
    }
  ],
  "Dunk Low": [
    {
      "handle": "nike-dunk",
      "title": "Nike Dunk",
      "score": 100
    }
  ],
  "On Running": [
    {
      "handle": "on-running-todos-os-modelos",
      "title": "On Running",
      "score": 100
    }
  ],
  "Wales Bonner": [],
  "Loewe": [
    {
      "handle": "loewe-x-on-running",
      "title": "Loewe x On Running",
      "score": 0
    }
  ],
  "Loewe On Running": [
    {
      "handle": "on-running-todos-os-modelos",
      "title": "On Running",
      "score": 100
    },
    {
      "handle": "loewe-x-on-running",
      "title": "Loewe x On Running",
      "score": 0
    }
  ],
  "Jordan 1": [
    {
      "handle": "air-jordan-1",
      "title": "Air Jordan 1",
      "score": 100
    }
  ],
  "Air Max 1": [
    {
      "handle": "nike-air-max",
      "title": "Nike Air Max",
      "score": 100
    }
  ],
  "sneakers": [],
  "roupas": [],
  "sale": [],
  "lançamentos": []
}
```

## Observação de score

O target local v1 já ordena por score, mas nesta geração local os componentes disponíveis foram menu/produtos/principalidade. Os campos `sales` e `visits` ficam reservados como `0` no mapa para serem conectados na rotina recorrente de sexta 18h BRT com Data Spine/GA4/vendas.

## Escopo DEV se aprovado

- Criar branch GitHub a partir de `dev`.
- Alterar apenas `sections/lk-search.liquid`.
- Abrir PR para `dev`.
- Fazer merge DEV conforme padrão aprovado.
- Aguardar/validar sync no tema DEV/unpublished.
- Readback DEV e QA visual/funcional.

## Não-ações

- Nenhum Asset API write direto foi executado.
- Nenhum write em Production.
- Nenhum produto/coleção/preço/estoque/app/campanha alterado.

## Rollback

Rollback completo via GitHub revert no branch `dev`, ou restaurar source atual salvo em:

`/opt/data/profiles/lk-shopify/workspace/lk-collection-suggestion-20260608/production_source_sections__lk-search.liquid`

## Próxima decisão

Para executar a etapa DEV via GitHub/dev:

**Aprovo DEV LK Collection Suggestion**
