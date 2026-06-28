# Receipt — Bloco A aprovado: tentativa de OAuth Shopify CLI + readback

Data: 2026-06-27T16:20:47Z
Owner: [LK] Growth
Aprovação: Lucas respondeu `Aprovo bloco a`.
Escopo aprovado: renovar/restaurar OAuth oficial Shopify CLI e fazer somente readback técnico/Admin/theme de Adidas Tokyo, Puma Speedcat, ASICS Gel NYC e New Balance 740, sem write externo.
Writes externos: 0
values_printed=false

## Ações executadas

1. Verificado help do comando oficial:

```bash
/opt/data/home/.local/bin/hermes-cli-run shopify store auth --help
```

Resultado: comando disponível; exige `--store` e `--scopes`.

2. Tentativa de autenticação oficial com escopos read-only:

```bash
/opt/data/home/.local/bin/hermes-cli-run shopify store auth   --store lk-sneakerss.myshopify.com   --scopes read_products,read_content,read_themes,read_metaobjects --json
```

Resultado: timeout após 120s, sem conclusão de OAuth e sem saída útil.

3. Tentativa sem `--json` e com PTY:

```bash
/opt/data/home/.local/bin/hermes-cli-run shopify store auth   --store lk-sneakerss.myshopify.com   --scopes read_products,read_content,read_themes,read_metaobjects
```

Resultado: timeout após 30s, sem URL/código exibido.

4. Tentativa em background com `--verbose` para capturar prompt:

```bash
/opt/data/home/.local/bin/hermes-cli-run shopify store auth   --store lk-sneakerss.myshopify.com   --scopes read_products,read_content,read_themes,read_metaobjects --verbose
```

Resultado: processo ficou em execução sem output; foi encerrado manualmente para não deixar auth pendente.

5. Smoke governado Shopify LK:

```bash
/opt/data/home/.local/bin/hermes-cli-integrations smoke shopify_lk
```

Resultado sanitizado: `status=failed`, `method=shopify_store_execute`, `values_printed=false`.

6. Inventário governado:

```bash
/opt/data/home/.local/bin/hermes-cli-integrations inventory
```

Resultado sanitizado: CLI `shopify=true`; secrets Shopify presentes por nome (`SHOPIFY_STORE`, `SHOPIFY_STORE_URL`, `SHOPIFY_ACCESS_TOKEN`, `SHOPIFY_ADMIN_TOKEN`); `values_printed=false`.

7. Verificação local de cache OAuth Shopify sem ler valores:

- `/opt/data/home/.config/shopify`: ausente.
- `/opt/data/home/.shopify`: ausente.
- `/opt/data/home/.cache/shopify`: ausente.
- `/opt/data/home/.local/share/shopify`: ausente.
- equivalentes em `/opt/data/profiles/lk-growth/home`: ausentes.

## Status

**Bloco A parcialmente executado e bloqueado no OAuth oficial.**

- Não foi possível completar OAuth oficial Shopify CLI no runtime atual.
- Não foi feito readback Admin/theme porque a política canônica exige CLI oficial primeiro e o token OAuth oficial não está armazenado.
- Não foi usado Admin HTTP raw como fallback, porque isso exigiria exceção explícita ao guardrail Shopify CLI oficial.

## Evidência pública já confirmada antes do bloqueio

- `/collections/adidas-tokyo`: HTTP 200, canonical correto, `FAQPage=0`, sem Liquid error.
- `/collections/puma-speedcat`: HTTP 200, canonical correto, `FAQPage=0`, sem Liquid error.
- `/collections/asics-gel-nyc`: HTTP 200, canonical correto, `FAQPage=1`, sem Liquid error.
- `/collections/new-balance-740`: HTTP 200 mas final/canonical/title da coleção geral `/collections/new-balance-todos-os-modelos`; `FAQPage=0`.

## Próximo desbloqueio necessário

Escolher uma das opções:

1. **Preferida:** Lucas/Hermes interativo completar `shopify store auth` oficial para `lk-sneakerss.myshopify.com` com escopos read-only. Depois Growth retoma Admin/theme readback.
2. **Exceção:** Lucas aprovar explicitamente uso read-only temporário de Admin API direta via secrets Doppler existentes, apenas para readback de collection/metafields/theme assets, sem mutations, sem imprimir token e com receipt. Essa exceção deve ser justificada porque o OAuth oficial está bloqueado neste runtime.

## Non-actions

Não alterado:
- Shopify production;
- theme asset;
- collection/product/metafield;
- preço;
- estoque/Tiny/inventory;
- GMC/feed;
- campanhas;
- Klaviyo/WhatsApp/e-mail;
- checkout.
