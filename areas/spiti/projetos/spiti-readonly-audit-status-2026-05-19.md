# SPITI OS — auditoria read-only Hub + Financial

Data: 2026-05-19T16:18:42+00:00
Modo: read-only/local. Sem push, PR, merge, deploy, Supabase mutation, Vercel mutation, mensagem externa ou exposição de secrets.

## Escopo auditado

- Repo principal: `/opt/data/hermes_bruno_ingest/spiti-hub-git` → `spiti-auction/spiti-hub`.
- Repo financial ativo: `/opt/data/hermes_bruno_ingest/spiti-financial-git` → `spiti-auction/spiti-financial`.
- Brain SPITI: `/opt/data/hermes_bruno_ingest/hermes-brain/areas/spiti`.

## Estado Git

### spiti-hub

- Branch local: `dev`.
- Status: limpo, `dev...origin/dev`.
- Último commit: `4f5426c docs: add SPITI OS financial hub inventory (#93)`.
- Fluxo declarado: feature branch a partir de `dev`, PR para `dev`; `main` é produção.
- Arquivos sensíveis por CODEOWNERS: `migrations/**`, `.github/workflows/**`, `src/lib/supabase.js`, `src/lib/auth.js`, `package.json`, `vercel.json`, `CODEOWNERS`.

### spiti-financial

- Branch local: `main`.
- Status: limpo, `main...origin/main`.
- Último commit: `cab1c69 fix(vendas): handleDeletarVenda agora sincroniza a cobrança`.
- Financial continua ativo/fallback; não tratar como legado congelado.
- `.env.local` aparece rastreado pelo Git; conteúdo não foi aberto/impressso nesta auditoria. Risco de governança: revisar/remover valores sensíveis via PR/rotação se necessário.

## Stack e módulos

### Hub

- Stack: React 19, Vite 8, Tailwind, Supabase, React Router, Recharts, React PDF.
- Scripts: `dev`, `build`, `lint`, `preview`.
- Rotas/módulos observados: Dashboard, CRM Pessoas, Obras, Bulk Fotos, Artistas, Admin Usuários, Admin Audit, Galeria, Relatórios, Resultado, Comprovantes, Tarefas, Captações, Leilões, Pós-leilão, Pedidos, Vendas, Financeiro, Documentos, Marketing, Segmentos, Campanha, Catálogo público, Cobrança pública, Inativos, Top Compradores, Perfil.
- Arquivos auditados em docs: inventário Financial ↔ Hub, checklist QA, backlog P0–P3, auditoria Supabase canônico.
- `npm run lint --if-present`: passou.

### Financial

- Stack: React 19, Vite 8, Tailwind, Supabase, React Router, Recharts.
- Scripts: `dev`, `build`, `lint`, `preview`.
- Rotas/módulos observados: Dashboard, Contas a Receber, Contas a Pagar, Vendas, Custos, Resultado, Lotes, Clientes.
- Restrição interna simples observada: `restrictedUsers = ['helena@spiti.art']` bloqueia Custos/Resultado.
- `npm ci --no-audit --no-fund`: passou localmente.
- `npm run lint --if-present`: falhou com 15 erros de lint atuais.
- `npm run build`: passou; bundle JS grande (~950 kB) com warning de code splitting.

## Segurança e fontes de verdade

- Brain/SPITI mantém regra: silêncio > dado errado.
- Para lances/lotes/valores: email/fonte operacional verificada antes de site/meta tags.
- Base Supabase canônica documentada no Brain/Hub docs: `rmdugdkantdydivgnimb.supabase.co`.
- Backlog já aponta risco P0: Hub preview observado em documentação anterior com possível divergência para outro project ref (`ryitwaxguhggtkwefnke`); precisa auditoria read-only de env/bundle/Vercel antes de qualquer mudança.
- Hub contém Edge Functions/integrações com capacidade externa (Gmail/Evolution/campanhas). Não acionar/deployar sem aprovação explícita.
- Secret scan simples do Hub gerou falsos positivos/nomes de env em `process.env`/`Deno.env` e placeholders em docs; não houve valor sensível copiado. Ainda assim, recomenda-se PR de documentação de env para reduzir ruído.

## Principais riscos

1. Financial tem `.env.local` rastreado pelo Git — risco P0 de segredo no repo, mesmo sem imprimir valores aqui.
2. Financial build passa, mas lint falha — risco de manutenção/CI se enforcement for ativado.
3. Possível divergência de Supabase canônico vs ambiente preview/prod do Hub — risco P0 operacional.
4. Regra de comissão comprador citada em backlog como divergente entre docs/código — precisa decisão antes de cálculo/PR.
5. Hub tem módulos com efeitos externos potenciais (cobrança por email, WhatsApp Evolution, campanhas, Ads/segments); manter preview/approval-first.
6. Public catalog/cobrança pública existem como rotas; validar publicação/visibilidade antes de expor dados.

## Próximos PRs seguros sugeridos

1. `spiti-financial`: PR P0 para remover `.env.local` do versionamento, adicionar `.env.local`/`.env*` ao `.gitignore`, documentar `.env.example` sem valores e orientar rotação se o arquivo tiver segredo real.
2. `spiti-financial`: PR P1 de lint cleanup sem lógica funcional: unused vars e regras React lint; depois validar `npm run lint` + `npm run build`.
3. `spiti-hub`: PR docs/admin read-only para página ou doc `Fonte de dados / ambiente`, exibindo project ref/branch/build sem secrets.
4. `spiti-hub`: PR de testes/cálculo financeiro após Lucas confirmar regra de comissão comprador.
5. `spiti-hub`: PR de relatório read-only de paridade SPITI 9 Financial ↔ Hub por agregados/amostras; sem mutation.

## Bloqueios / requer aprovação

- Qualquer Supabase migration/mutation.
- Qualquer deploy Vercel/produção.
- Qualquer Edge Function deploy.
- Qualquer envio Gmail/WhatsApp/Evolution/MailerLite/Ads/campanha.
- Qualquer merge para `main`.
- Qualquer alteração em arquivos sensíveis CODEOWNERS.

## Veredito executivo

- Hub está mais maduro, em `dev`, lint verde, com inventário recente e backlog seguro já no repo.
- Financial continua operacional e buildável, mas precisa higiene P0 de env rastreado e limpeza de lint.
- O próximo passo mais seguro é PR pequeno de segurança no `spiti-financial` para governança de `.env.local`, sem tocar produção nem dados.
