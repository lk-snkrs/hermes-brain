# Receipt — estoque.lkskrs.online 404 repair

- timestamp_utc: 2026-06-15T19:05:20Z
- classification: external-write
- owner_profile: lk-shopify
- user_approval: Lucas pediu explicitamente: `CORRIGIR, o SITE ESTA DANDO 404 page not found` para `https://estoque.lkskrs.online`.

## Symptom

- `https://estoque.lkskrs.online/` retornava `404 page not found`.
- DNS resolvia para `72.60.150.124`.

## Root cause

No VPS `lc` (`72.60.150.124`), o container público `lk-estoque-web` estava rodando, mas sem labels Traefik e na rede `bridge`, apesar de `/opt/lk-estoque-web/docker-compose.yml` já conter as labels corretas para o host `estoque.lkskrs.online`.

Evidência antes:

- `docker inspect lk-estoque-web --format {{json .Config.Labels}}` retornou `{}`.
- `curl http://127.0.0.1:3009/` retornava o app com `401 Senha obrigatoria`, então o app em si estava vivo localmente; o problema era roteamento público/Traefik.

## Change performed

- Criado backup em `/opt/lk-estoque-web/backups/repair-404-20260615T190345Z/` com:
  - `docker-compose.yml`
  - `.env` local do app
  - `lk-estoque-web.inspect.json`
  - `docker-compose-ps.before.txt`
- O container antigo quebrado foi preservado como:
  - `lk-estoque-web-pre404-20260615T190413Z`
- Removido o container temporário criado parcialmente pela tentativa de recreate.
- Subido o serviço `web` pelo `docker compose up -d web` a partir do compose correto.

## Verification

Depois da correção:

- Container novo: `lk-estoque-web` `Up`, porta interna `3000/tcp`.
- Labels Traefik presentes:
  - `traefik.enable=true`
  - router host `Host(`estoque.lkskrs.online`)`
  - entrypoint `websecure`
  - TLS true
  - service port `3000`
- Stock API segue saudável:
  - `lk-estoque-stock-api` `Up ... (healthy)`
- Live public URL:
  - `https://estoque.lkskrs.online/` agora retorna `401 Unauthorized`
  - body: `Senha obrigatoria`
  - header: `WWW-Authenticate: Basic realm="LK Estoque"`

Interpretação: o 404 foi corrigido. O `401` é o comportamento esperado de proteção por senha do painel, não erro de site fora do ar.

## Non-actions

- Não alterado código do app.
- Não alterado DNS.
- Não alterado Traefik global.
- Não alterado banco/Stock OS/Tiny/Shopify/estoque.
- Não impresso segredo/senha/token (`values_printed=false`).

## Rollback

Se precisar voltar ao estado anterior:

1. Parar/remover o container atual `lk-estoque-web`.
2. Renomear `lk-estoque-web-pre404-20260615T190413Z` de volta para `lk-estoque-web`.
3. Iniciar o container antigo.

Atenção: esse rollback volta também o 404 público; preferir manter o estado atual.
