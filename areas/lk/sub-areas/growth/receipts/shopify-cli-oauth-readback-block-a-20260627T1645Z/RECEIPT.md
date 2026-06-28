# Receipt — Bloco A concluído: OAuth Shopify CLI + readback Admin/theme

Data: 2026-06-27T16:45Z
Owner: [LK] Growth
Aprovação: Lucas aprovou `bloco a` e enviou callback OAuth.
Modo: read-only
Writes externos: 0
values_printed=false

## Status OAuth / integração

- OAuth oficial Shopify CLI concluído para `lk-sneakerss.myshopify.com`.
- Smoke governado `hermes-cli-integrations smoke shopify_lk`: `status=ok`, `method=shopify_store_execute`, `values_printed=false`.
- A partir daqui, comandos Shopify Admin GraphQL read-only devem usar o caminho oficial:
  `/opt/data/home/.local/bin/hermes-cli-run shopify store execute --store lk-sneakerss.myshopify.com --json --query '<GraphQL>'`

## Readback Admin — collections

Query read-only: collections por handle para `adidas-tokyo`, `puma-speedcat`, `asics-gel-nyc`, `new-balance-740`.

| Handle | Admin existe | Collection ID | Title | Template suffix | SEO title | SEO description | Products count | UpdatedAt |
|---|---:|---|---|---|---|---|---:|---|
| `adidas-tokyo` | sim | `447368823006` | Adidas Tokyo | vazio/default | `Adidas Tokyo original \| Curadoria LK Sneakers` | preenchida | 11 | 2026-06-26T09:12:40Z |
| `puma-speedcat` | sim | `438203777246` | Puma Speedcat | `puma-speedcat` | `Puma Speedcat Original Feminino e Ballet \| LK` | preenchida | 13 | 2026-06-26T09:12:33Z |
| `asics-gel-nyc` | sim | `1128952955102` | ASICS Gel NYC | null/default | null | null | 1 | 2026-06-26T01:02:54Z |
| `new-balance-740` | **não retornou** | — | — | — | — | — | — | — |

Observações:

- `new-balance-740` ausente no Admin query por handle; confirma que a URL pública cai/finaliza na coleção geral e não é superfície canônica própria.
- `asics-gel-nyc` existe, mas sem SEO title/description Admin; por isso a página usa fallback público/genérico.
- Tokyo e Speedcat têm descriptions com FAQ textual no Admin, mas isso não gera `FAQPage` JSON-LD sozinho.

## Readback theme — production

Theme principal identificado via GraphQL:

- ID: `155065417950`
- Nome: `lk-new-theme/production`
- Role: `MAIN`
- UpdatedAt: `2026-06-26T15:53:40Z`

Arquivos lidos via `OnlineStoreTheme.files`:

| Arquivo | Existe | Size | UpdatedAt | Achado |
|---|---:|---:|---|---|
| `snippets/lk-goc-schema-extra.liquid` | sim | 4910 | 2026-06-26T00:57:51Z | Contém condicionais de `adidas-tokyo` e `puma-speedcat`; contém `FAQPage`. |
| `sections/lk-collection.liquid` | sim | 263273 | 2026-06-26T08:18:33Z | **Não contém render** de `lk-goc-schema-extra`; por isso o snippet existe mas não entra no HTML público. |
| `templates/collection.puma-speedcat.json` | não retornou nesta query | — | — | Não necessário para concluir schema gap; Speedcat usa template suffix `puma-speedcat`. |
| `templates/collection.adidas-tokyo.json` | não retornou nesta query | — | — | Tokyo usa template default. |

Conclusão técnica: a divergência Tokyo/Speedcat está explicada. O snippet de schema existe em production, mas o section principal não renderiza o snippet atualmente. Provável overwrite/regressão após o receipt de 2026-06-26.

## QA público confirmado após readback

| URL | Status | Canonical/final | FAQPage | Liquid error |
|---|---:|---|---:|---:|
| `/collections/adidas-tokyo` | 200 | canonical correto | 0 | false |
| `/collections/puma-speedcat` | 200 | canonical correto | 0 | false |
| `/collections/asics-gel-nyc` | 200 | canonical correto | 1 | false |
| `/collections/new-balance-740` | 200 | final/canonical `/collections/new-balance-todos-os-modelos` | 0 | false |

ASICS Gel NYC público:

- meta description: `1 ASICS Gel NYC originais na LK Sneakers. Parcele em 10x, frete grátis acima de R$ 500. Confira os modelos disponíveis.`
- og:description global contém termo operacional: `Envio imediato e troca grátis.`
- Guardrail: recomendado cleanup, mas exige aprovação separada.

## Recomendação Bloco B — pedir aprovação separada

1. **Tokyo/Speedcat schema restore**
   - Reintroduzir render único do snippet `lk-goc-schema-extra` em `sections/lk-collection.liquid` no production theme.
   - Validar público: `FAQPage=1` para Tokyo e Speedcat; sem duplicar `FAQPage` em outras collections.
   - Risco: baixo-médio porque o arquivo section é grande e já teve limite 256KB; usar patch mínimo e backup/readback.

2. **ASICS Gel NYC SEO/meta cleanup**
   - Definir SEO title/meta Admin ou ajustar fonte OG/global somente para remover termos operacionais.
   - Validar público head/meta/OG sem `envio imediato`/`troca grátis`.
   - Risco: baixo-médio; sem alterar visual/produtos.

3. **NB740 canônico — handoff LK Shopify**
   - Criar/validar collection canônica `new-balance-740` com produtos ativos já existentes.
   - Growth depois prepara guia/FAQ/schema em DEV.
   - Sem consulta/alteração de estoque.

## Non-actions

Não alterado:
- theme production;
- collection SEO/meta/description;
- produtos;
- preço;
- estoque/Tiny/inventory/grade;
- ordenação;
- GMC/feed;
- campanhas;
- Klaviyo/WhatsApp/e-mail;
- checkout.
