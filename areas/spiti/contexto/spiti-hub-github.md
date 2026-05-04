# SPITI Hub — GitHub e inventário inicial

Data de registro: 2026-05-04.

## Repositório

- Owner/repo: `spiti-auction/spiti-hub`.
- URL: `https://github.com/spiti-auction/spiti-hub`.
- Visibilidade: privado.
- Branch padrão: `main`.
- Permissão observada com token fornecido por Lucas: `admin`, `maintain`, `push`, `triage` e `pull`.
- Cópia local de inspeção: `/opt/data/hermes_bruno_ingest/spiti-hub`.
- Forma de obtenção local nesta rodada: zipball read-only via GitHub API; token não foi gravado no remote Git.

## Escopo do sistema

Pelo README/PRD do repo, o Spiti Hub é o sistema operacional unificado da galeria Spiti:

- CRM de pessoas e obras.
- Gestão de leilões, vendas, financeiro e marketing.
- Substitui gradualmente Tango/FileMaker e `spiti-financial`.
- Stack declarada: React + Vite + Tailwind, Supabase DB/Auth/Storage, Vercel, Claude API, Evolution/WhatsApp, MailerLite, Meta Marketing API e Google Ads API.
- Marco crítico declarado: Spiti 10 em 2–3 de agosto de 2026 rodando no Hub.

## Estrutura observada

- Frontend React/Vite em `src/`.
- Páginas principais: pessoas, obras, leilões, pedidos, financeiro, marketing, relatórios, pós-leilão, documentos, comprovantes e admin.
- Supabase Edge Functions em `supabase/functions/`.
- Migrações SQL em `migrations/`.
- Documentos PRD/operacionais em `docs/`.
- CI GitHub Actions em `.github/workflows/ci.yml`.

## Verificações executadas

Rodada read-only/local, sem alteração em GitHub, produção, Supabase, Vercel ou VPS:

- GitHub API confirmou acesso ao repo privado.
- Repo baixado localmente por zipball para inspeção.
- Inventário local encontrou 128 arquivos:
  - 44 `.jsx`;
  - 22 `.sql`;
  - 16 `.md`;
  - 12 `.js`;
  - 9 `.ts`;
  - demais configs/scripts.
- `npm install --no-audit --no-fund`: OK local.
- `npm run lint --if-present`: OK com warnings, sem erros.
- `npm run build`: OK.
- Vite alertou bundle grande (`dist/assets/index-*.js` acima de 500 kB), recomendando code splitting futuro.

## Warnings principais observados

Lint passou, mas com 46 warnings, principalmente:

- variáveis/imports não usados;
- dependências ausentes em hooks React;
- `eslint-disable` sem efeito;
- avisos de Fast Refresh em arquivos que exportam componentes e helpers juntos.

Esses warnings não bloquearam build, mas devem entrar em uma rodada futura de hardening técnico antes de produção crítica.

## Secrets e credenciais

- O token GitHub fornecido por Lucas foi usado apenas para acesso GitHub nesta rodada; não deve ser commitado nem repetido em docs.
- Como o token foi enviado por chat, recomenda-se rotacionar/revogar depois que o acesso estiver devidamente movido para Doppler ou outro cofre seguro.
- Scan local encontrou 2 assignments secret-like em `docs/deploy-edge-functions.md` nas linhas 26–27, relacionadas a `GOOGLE_OAUTH_CLIENT_SECRET` e `GOOGLE_REFRESH_TOKEN`. Os valores não foram copiados para o Brain; precisam de revisão no próprio repo para confirmar se são exemplos, placeholders ou credenciais reais.
- Se forem credenciais reais, remover/redigir do repo e rotacionar/revogar antes de qualquer uso em produção.
- Supabase frontend usa `VITE_SUPABASE_URL` e `VITE_SUPABASE_ANON_KEY`; secrets sensíveis devem ficar em Vercel/Supabase/Doppler, nunca no repo.

## Regras de segurança operacional

- Não fazer push, alterar branch, abrir PR, mexer em settings, secrets, Vercel, Supabase ou GitHub Actions sem intenção explícita de tarefa.
- Mudanças em `migrations/**`, `.github/workflows/**`, `src/lib/supabase.js`, `src/lib/auth.js`, `package.json` e `vercel.json` exigem atenção especial e revisão Lucas conforme `CODEOWNERS`/`CONTRIBUTING.md`.
- Fluxo declarado no repo: feature branch a partir de `dev`, PR para `dev`; `main` representa produção.
- Para qualquer automação externa (WhatsApp, email, campanhas, contatos, cobrança), exigir preview e aprovação Lucas antes de envio.

## Próximas ações recomendadas

1. Salvar/atualizar o token correto de GitHub da Spiti em Doppler com nome separado do token `lk-snkrs`, sem expor valor em chat.
2. Fazer clone Git completo usando credencial via helper/askpass seguro quando houver necessidade de branch/PR; manter remote sem token embutido.
3. Criar rodada de hardening lint: remover warnings de hooks/unused/disable antes do Spiti 10.
4. Criar mapa técnico do schema Supabase a partir das migrações, sem aplicar nada em produção.
5. Criar plano de integração Hermes Brain ↔ Spiti Hub: o Brain documenta regras/processos; o Hub é sistema operacional vivo.
## Rodada local de hardening — 2026-05-04

Executado apenas na cópia local `/opt/data/hermes_bruno_ingest/spiti-hub`; sem push, PR, alteração de GitHub remoto, Vercel, Supabase ou produção.

Resultado:

- `docs/deploy-edge-functions.md` foi redigido localmente para substituir assignments secret-like por placeholders (`<google-oauth-client-secret>` e `<google-refresh-token>`).
- `npm run lint -- --fix` aplicado localmente: warnings reduziram de 46 para 39.
- `npm run lint --if-present`: OK, 0 errors, 39 warnings restantes.
- `npm run build`: OK; bundle grande permanece como warning.
- Secret scan local pós-redação: 0 achados nos padrões verificados.

Arquivos alterados localmente pela rodada:

- `docs/deploy-edge-functions.md`
- `src/components/DrawerObra.jsx`
- `src/lib/segmentos.js`
- `src/pages/CatalogoPublico.jsx`
- `src/pages/Documentos.jsx`
- `src/pages/Leiloes.jsx`
- `src/pages/Pedidos.jsx`
- `src/pages/Vendas.jsx`

Credencial para PR/push:

- Em 2026-05-04, Lucas forneceu novo token e pediu para salvar.
- Secret salvo no Doppler `lc-keys/prd` como `GITHUB_SPITI_HUB_TOKEN`.
- Verificação segura confirmou acesso ao repo `spiti-auction/spiti-hub` com permissões `admin`, `maintain`, `push`, `triage` e `pull`.
- Como o token foi enviado por chat, ainda deve ser tratado como exposto até futura rotação/revogação; não repetir, imprimir, commitar ou embutir em remote.

Próximo passo seguro para publicar mudanças no Spiti Hub:

1. Usar `GITHUB_SPITI_HUB_TOKEN` via Doppler/askpass, sem gravar token em remote.
2. Fazer clone Git completo do repo.
3. Criar branch a partir de `dev`.
4. Aplicar as mudanças locais ou refazê-las, rodar lint/build/secret scan e abrir PR para `dev`.
5. Após a sequência, considerar rotacionar/revogar o token enviado por chat e substituir no Doppler.
## PR de hardening aberto — 2026-05-04

Publicação segura feita via Git, sem token embutido no remote:

- Clone Git completo: `/opt/data/hermes_bruno_ingest/spiti-hub-git`.
- Branch criada a partir de `dev`: `hermes/spiti-hub-secrets-lint-hardening`.
- Commit no Spiti Hub: `8c8549b chore: redact edge function secret examples`.
- Pull Request aberto para `dev`: `https://github.com/spiti-auction/spiti-hub/pull/89`.

Mudanças no PR:

- `docs/deploy-edge-functions.md`: exemplos de `GOOGLE_OAUTH_CLIENT_ID`, `GOOGLE_OAUTH_CLIENT_SECRET` e `GOOGLE_REFRESH_TOKEN` trocados por placeholders seguros.
- Aplicado resultado seguro do `eslint --fix` em comentários/disable directives de arquivos JSX/JS, reduzindo warnings sem alterar lógica funcional.

Verificações locais antes do push/PR:

- `git diff --check`: OK.
- Secret scan local: 0 achados nos padrões verificados.
- `npm run lint --if-present`: OK, 0 errors, 39 warnings restantes.
- `npm run build`: OK; warning de bundle grande permanece.

Estado do PR via API:

- PR aberto.
- `mergeable: true`.
- `mergeable_state: unstable` no momento da coleta, provavelmente por checks/status ainda pendentes ou inacessíveis pela API/token.
- Endpoints de status/check-runs retornaram `403 Resource not accessible by personal access token`; validar CI visualmente no GitHub ou com token com escopo apropriado se necessário.

Não realizado:

- Não houve merge.
- Não houve alteração em `main`, Supabase, Vercel, produção, VPS, Docker, campaigns ou mensagens externas.

