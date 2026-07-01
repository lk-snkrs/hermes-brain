# SPITI Hub — Deploy, contas e acessos

Data de registro: 2026-07-01.

Mapa de "onde vive a produção do SPITI Hub e como deployar".
Descoberto na prática entregando a feature de criar usuário (#262) e o fix do
merge de artistas (#264). **Só nomes de secrets — nunca valores.**

## Fato central: produção do SPITI está em contas SEPARADAS

A produção real (o que o Lucas usa em `hub.spiti.cloud`) vive numa **conta SPITI
própria** (`spiti@spiti.auction`), **distinta** das contas pessoais dele (LC / lk-snkrs).
Isso vale pra Supabase E Vercel. As chaves pessoais de `lc-keys` **não** alcançam a conta SPITI.

| Camada | Produção real (conta SPITI) | Onde deployar / chave |
|---|---|---|
| Vercel | time **`spiti-auctions-projects`** (`team_jGBDS9Brr5k8gShwMxJfV1pn`), projeto `spiti-hub` (`prj_KhIaK1Cb…`), domínios **`hub.spiti.cloud`** + `spiti-hub.vercel.app` | token `VERCEL_SPITI_TOKEN` (Doppler `lc-keys/prd`) |
| Supabase | projeto `ryitwaxguhggtkwefnke` (hub) | deploy: `SUPABASE_SPITI_ACCESS_TOKEN`; dado: `SUPABASE_SPITI_HUB_SERVICE_KEY`; url: `SUPABASE_SPITI_HUB_URL` |

Cuidado: no time **lk-snkrs** existe um **espelho** do projeto (`spiti-hub-one.vercel.app`).
Deploy feito com `VERCEL_API_TOKEN`/`VERCEL_API_TOKEN_LUCASCIMINO` cai nesse espelho,
**não** em `hub.spiti.cloud`. Idem Supabase: `SUPABASE_ACCESS_TOKEN`/`SUPABASE_MANAGEMENT_API_TOKEN`
(pessoais) dão **403** no projeto SPITI. Use sempre os `*_SPITI_*`.

## Como deployar (sem CLI — os CLIs não rodam no ambiente Claude)

**Front (Vercel):** `vercel deploy --prod --token=$VERCEL_SPITI_TOKEN --yes` a partir do
repo em `main`. Rodar em **background** (o CLI streama build e pode estourar timeout).
O projeto **não tem git-integration** → nada de auto-deploy no push; é manual.

**Edge function (Supabase) — via Management API, sem CLI:**
```
curl -X POST "https://api.supabase.com/v1/projects/ryitwaxguhggtkwefnke/functions/deploy?slug=NOME" \
  -H "Authorization: Bearer $SUPABASE_SPITI_ACCESS_TOKEN" \
  -F 'metadata={"name":"NOME","entrypoint_path":"NOME/index.ts","verify_jwt":true,"import_map_path":null};type=application/json' \
  -F 'file=@NOME/index.ts;filename=NOME/index.ts;type=application/typescript' \
  -F 'file=@_shared/auth.ts;filename=_shared/auth.ts;type=application/typescript'
```
(rodar de `supabase/functions/`; incluir cada arquivo importado — a import relativa
`../_shared/auth.ts` resolve porque o entrypoint fica um nível abaixo).

## Gotchas

- **Vercel bloqueia deploy por CLI se o autor do commit HEAD não é membro do time.**
  Erro: `Git author <email> must have access to the team …`. Merges de PR via API com o
  token do GitHub do SPITI ficam autorados por `spiti@spiti.auction`. No time **SPITI**
  isso passa (ele é dono). No time **lk-snkrs** NÃO — lá, deployar com autor de time
  (`lucascimino@gmail.com` / `lk@lksneakers.com.br`), ex.:
  `git commit --allow-empty --author="Lucas Cimino <lucascimino@gmail.com>"` antes do deploy.
- **Verificar deploy por hash de bundle engana em rota lazy:** o `index-*.js` (shell) não
  muda; a mudança vai pro chunk da rota (ex.: `Artistas-*.js`). Verificar o chunk da feature.
- **CLIs no ambiente Claude Code:** `supabase` morre com SIGKILL(137); `vercel` trava/estoura.
  Caminho robusto = **APIs via curl** (com `dangerouslyDisableSandbox`).
- **Service key ≠ SERVICE_ROLE_KEY injetado nas edge functions** deste projeto — o atalho
  `requireStaffOrService` por service-role não autentica com `SUPABASE_SPITI_HUB_SERVICE_KEY`.
  Pra testar function protegida, logar como usuário real (anon key + password) e usar o JWT.
- Shell: não usar variável `UID` (read-only → erro `failed to change user ID`).

## Estado das entregas (2026-07-01) — CONCLUÍDO

- **#262** criar usuário em `/admin/usuarios`: **live em `hub.spiti.cloud`**. Front deployado +
  edge function `admin-create-user` deployada (Management API). Testado ponta-a-ponta:
  gerente → 403; admin → 201 + trigger cria linha em `usuarios` + update de papel. OK.
- **#264** fix do merge de artistas em `/crm/artistas`: **live em `hub.spiti.cloud`**
  (chunk `Artistas-*.js` servido contém o código novo).

## Ligações

- `contexto/spiti-hub-github.md` — repo `spiti-auction/spiti-hub` (privado), token `GITHUB_SPITI_HUB_TOKEN`.
