
> **Superseded status — 2026-06-28:** do not use this historical artifact as current Shopify auth truth. The Central Integration Auth Broker now forces central CLI `HOME=/opt/data/home` plus central XDG paths, and `hermes-cli-integrations smoke shopify_lk` uses `method=broker_shopify_store_execute`. Fresh control-plane and profile smoke returned `rc=0/status=ok` with `values_printed=false`. Reauth/OAuth is not currently pending unless a fresh broker smoke fails again after retry outside a reload window.

# Approval Packet — próximo passo pós QA sábado: schema Tokyo/Speedcat + ASICS meta + NB740 canônico

Data: 2026-06-27
Owner: [LK] Growth
Modo executado até aqui: read-only / preview-only
Writes externos executados agora: 0
values_printed=false

## Por que existe este packet

O cron `LK QA + Impact Review Saturday` encontrou achados materiais após mudanças recentes. Lucas respondeu: `Seguir próximo`.

Growth executou continuidade segura em read-only:

- QA público cache-bust de Tokyo, Speedcat, ASICS Gel NYC e NB740.
- Tentativa de readback Admin Shopify via CLI oficial obrigatório.
- Checagem DataForSEO BR para demanda/intenção dos handles envolvidos.

## Evidência read-only de hoje

### QA público storefront

| URL | Status/final | Canonical | Title head | FAQPage | Observação |
|---|---:|---|---|---:|---|
| `/collections/adidas-tokyo` | 200 | `/collections/adidas-tokyo` | `Adidas Tokyo original \| Curadoria LK Sneakers` | 0 | Confirma divergência contra receipt 2026-06-26, que registrava FAQPage=1. |
| `/collections/puma-speedcat` | 200 | `/collections/puma-speedcat` | `Puma Speedcat Original Feminino e Ballet \| LK` | 0 | Confirma divergência contra receipt 2026-06-26, que registrava FAQPage=1. |
| `/collections/asics-gel-nyc` | 200 | `/collections/asics-gel-nyc` | `ASICS Gel NYC: 1 modelos \| LK Sneakers` | 1 | Schema/guia público OK; precisa confirmar meta/OG operacional em Admin antes de cleanup. |
| `/collections/new-balance-740` | 200 → final `/collections/new-balance-todos-os-modelos` | `/collections/new-balance-todos-os-modelos` | `New Balance Todos os Modelos \| LK Sneakers` | 0 | Não é superfície canônica própria; lacuna confirmada. |

Testes públicos foram repetidos com query normal, `_qa=20260627b` e filtro cache-bust. Resultado Tokyo/Speedcat permaneceu `FAQPage=0`.

### Shopify CLI/Admin readback

Comando tentado conforme política oficial Shopify CLI:

```bash
/opt/data/home/.local/bin/hermes-cli-run shopify store execute --store lk-sneakerss.myshopify.com --json --query '<GraphQL read-only>'
```

Resultado sanitizado:

- Status: bloqueado.
- Causa: `No stored app authentication found for lk-sneakerss.myshopify.com`.
- Tokens/cache OAuth: não impressos.
- values_printed=false.

Conclusão: não há readback Admin decision-grade até renovar/restaurar OAuth oficial do Shopify CLI. Growth não deve usar Admin HTTP raw como atalho normal.

### DataForSEO — demanda BR

| Keyword | Volume BR | Tendência | Intenção DataForSEO keyword overview | Observação |
|---|---:|---:|---|---|
| `asics gel nyc` | 60.500 | mensal +22% | transactional | Maior demanda; já tem schema, mas há risco de meta/OG operacional. |
| `new balance 740` | 27.100 | anual +235%; mensal +49% | transactional no overview / info+trans em intent endpoint | Lacuna mais clara de superfície canônica. |
| `puma speedcat` | 18.100 | anual +83%; mensal +22% | transactional no overview | Schema deveria existir; público atual não mostra. |
| `adidas tokyo` | 9.900 | anual +123%; mensal +50% | navigational no overview / informational no intent endpoint | Schema-only é útil para AI answerability; precisa correção técnica. |
| `adidas handball spezial` | 4.400 | anual +83% | transactional no overview | Continua boa candidata schema-only, mas abaixo das correções. |

## Diagnóstico

1. **Tokyo/Speedcat:** provável regressão/render gap no snippet `snippets/lk-goc-schema-extra.liquid` ou no render condicional em `sections/lk-collection.liquid`.
   - Receipt de 2026-06-26 diz que o render estava em produção e público com `FAQPage=1`.
   - QA público de 2026-06-27 confirma `FAQPage=0` com e sem cache-bust.
   - Sem Admin readback, ainda não é seguro afirmar se o problema é asset removido, condição não batendo, cache/template diferente ou outro overwrite.

2. **ASICS Gel NYC:** guia/schema público OK, mas cron apontou termo operacional `Envio imediato e troca grátis` em meta/OG global da página.
   - Precisa readback Admin SEO/metafields antes de alterar title/meta/OG.
   - Cleanup é recomendado se confirmado, por guardrail LK.

3. **NB740:** `/collections/new-balance-740` cai na coleção geral.
   - A oportunidade é grande por volume e crescimento.
   - Growth deve handoff para LK Shopify validar/criar collection canônica e produtos ativos, sem consultar estoque e sem mexer em preço/ordenação/campanhas.

## Próxima ação recomendada

### Bloco A — desbloqueio técnico read-only

1. Renovar/restaurar OAuth oficial Shopify CLI para `lk-sneakerss.myshopify.com`.
2. Reexecutar readback Admin GraphQL de:
   - collection SEO/metafields de `adidas-tokyo`, `puma-speedcat`, `asics-gel-nyc`, `new-balance-740`;
   - confirmar se NB740 existe no Admin;
   - confirmar SEO/meta ASICS.
3. Readback de theme assets pelo caminho oficial/governado disponível; se não houver caminho CLI oficial para asset, encaminhar para LK Shopify fazer readback técnico com receipt.

### Bloco B — se readback confirmar problema

Preparar execução separada, com aprovação atual, para:

- restaurar/corrigir schema-only condicional Tokyo/Speedcat em produção;
- limpar meta/OG ASICS Gel NYC removendo termo operacional, sem mudar produto/preço/estoque;
- abrir handoff LK Shopify para NB740 collection canônica; Growth entra depois com guia/FAQ/schema em DEV.

## Escopo negativo

Não alterar:

- preço;
- estoque/Tiny/inventory/grade/disponibilidade;
- produtos/ordenação;
- GMC/feed;
- campanhas Google/Meta;
- Klaviyo/WhatsApp/e-mail;
- checkout.

## Risco / rollback

| Ação | Risco | Rollback |
|---|---|---|
| Readback Admin/Theme | baixo | Sem write; apenas reautenticação/read-only. |
| Schema-only Tokyo/Speedcat | médio-baixo | Restaurar `snippets/lk-goc-schema-extra.liquid` e render anterior de `sections/lk-collection.liquid` a partir dos backups do receipt; readback público FAQPage. |
| Cleanup meta/OG ASICS | baixo-médio | Restaurar SEO title/meta/metafields anteriores via backup Admin; readback público head/meta/OG. |
| NB740 canônica | médio | LK Shopify criar/validar em escopo separado com rollback de collection/template/metafields; Growth sem estoque. |

## Aprovação sugerida para Lucas

`Aprovo o Bloco A: renovar/restaurar OAuth oficial Shopify CLI e fazer somente readback técnico/Admin/theme de Adidas Tokyo, Puma Speedcat, ASICS Gel NYC e New Balance 740, sem nenhum write externo.`

Depois do readback, se confirmar o diagnóstico, pedir aprovação separada para o Bloco B de correções.
