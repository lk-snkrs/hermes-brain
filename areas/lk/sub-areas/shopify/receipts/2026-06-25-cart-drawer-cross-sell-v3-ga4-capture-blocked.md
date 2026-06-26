# Receipt/blocked — GA4/GTM capture cart drawer cross-sell v3

- **Data:** 2026-06-25
- **Perfil:** lk-shopify
- **Superfície:** GA4/GTM analytics config / LK Sneakers
- **Status:** **blocked parcial** — tentativa aprovada executada, mas GA4 Admin API retornou permissão insuficiente para writes.

## Aprovação

Lucas aprovou explicitamente:

`Aprovo configurar captura GA4/GTM dos eventos cart drawer cross-sell v3`

## O que foi verificado

### HTML público

- `dataLayer` presente.
- GA4 ID público detectado: `G-HVFGK8SQQT`.
- GTM `GTM-...` não detectado por HTML estático/runtime.
- Código v3 e eventos `lk_cart_cross_sell_view`, `lk_cart_cross_sell_click`, `lk_cart_cross_sell_add` presentes no HTML.
- `/collections/all/products.json` ausente.

### Runtime tag

- Runtime Chromium detectou `dataLayer` como object.
- Runtime detectou `gtag` como `undefined` apesar de `googletagmanager.com/gtag/js` aparecer no HTML.
- Isso indica que push `dataLayer.push({ event: ... })` pode não virar evento GA4 automaticamente sem GTM ou sem adapter `gtag('event', ...)`.

### GA4 Admin API

Credencial usada via Doppler:

- `GA4_LK_SERVICE_ACCOUNT` presente.
- Property ID: `348553567`.
- Property read OK: `Lk Sneakers`, timezone `America/Sao_Paulo`.
- Custom dimensions read OK: 4 existentes.
- Custom metrics read OK: 0 existentes.

Tentativa de criar custom definitions:

| Tipo | Parameter | Resultado |
|---|---|---:|
| dimension | `surface` | 403 permission denied |
| dimension | `map_version` | 403 permission denied |
| dimension | `strategy` | 403 permission denied |
| dimension | `recommended_handle` | 403 permission denied |
| dimension | `score_bucket` | 403 permission denied |
| dimension | `status` | 403 permission denied |
| metric | `position` | 403 permission denied |
| metric | `rendered_count` | 403 permission denied |

Readback após tentativa:

- nenhuma dimensão nova criada;
- nenhuma métrica nova criada;
- estado GA4 permanece unchanged.

## Evidência local

- Discovery/readback: `/opt/data/profiles/lk-shopify/workdirs/cart-drawer-cross-sell-xy-20260625/ga4_admin_discover_cross_sell.py`
- Resultado tentativa config: `/opt/data/profiles/lk-shopify/workdirs/cart-drawer-cross-sell-xy-20260625/ga4_admin_configure_cross_sell_custom_defs_result.json`
- Probe OAuth: `/opt/data/profiles/lk-shopify/workdirs/cart-drawer-cross-sell-xy-20260625/ga4_oauth_candidate_probe.py`
- Detecção runtime tag: `/opt/data/profiles/lk-shopify/workdirs/cart-drawer-cross-sell-xy-20260625/runtime_google_tag_presence.json`

`values_printed=false`; nenhum segredo impresso.

## Interpretação

A credencial GA4 atual tem acesso de leitura à propriedade, mas não tem permissão para alterar custom dimensions/metrics.

Para a captura ficar 100% operacional, faltam dois pontos:

1. **Permissão GA4/GTM de write:** conceder Editor/Admin à service account usada (`GA4_LK_SERVICE_ACCOUNT`) ou fornecer/autorizAR uma credencial OAuth/GTm com permissão de edição.
2. **Transporte para GA4:** como GTM não foi detectado e `gtag` está undefined no runtime, pode ser necessário um ajuste de tema/pixel para converter os eventos do `dataLayer` em chamadas GA4 `gtag('event', ...)`. Esse ajuste é Shopify/theme write e precisa de aprovação própria se for o caminho escolhido.

## Próxima decisão

Opção A — permissões GA4:

- conceder Editor/Admin à service account de GA4 já usada e pedir para repetir a configuração.

Opção B — GTM:

- fornecer/autorizar container GTM com permissão de edição e instalar/validar container se necessário.

Opção C — theme adapter:

- aprovar explicitamente um ajuste no tema para encaminhar os três eventos para GA4 via Google tag/gtag, com DEV + PR Production + rollback.

## Rollback

Nenhum rollback necessário porque nenhum write GA4 foi aplicado; todos os `POST` falharam com 403.
