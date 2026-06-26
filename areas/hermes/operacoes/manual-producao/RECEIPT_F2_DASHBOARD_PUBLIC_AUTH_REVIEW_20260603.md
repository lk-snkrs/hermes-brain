# Receipt — F2 Dashboard público / auth & exposição

- Data UTC: 2026-06-03T18:07:33Z
- Board: `hermes-lk-improvements`
- Card: `t_2302a6a6` — `[F2][DASHBOARD][A1] Review public dashboard auth/exposure read-only`
- Escopo aprovado por Lucas: revisão read-only de autenticação/exposição do dashboard público antes de qualquer cockpit/plugin operacional.
- Superfície revisada: `https://hermes-agent-5ajw.srv1331756.hstgr.cloud`
- Modo: GET/HEAD e inspeção local read-only. Nenhum POST/PUT/PATCH/DELETE. Nenhum Docker/Traefik/config/restart alterado. Nenhum segredo preservado.

## Resultado executivo

Classificação: **Atenção alta / corrigir antes de usar como cockpit operacional**.

O dashboard público não é apenas uma página estática. Ele expõe uma aplicação FastAPI/dashboard com documentação OpenAPI pública e injeta no HTML um token de sessão acessível a qualquer visitante da página. Com esse token público de página, endpoints sensíveis retornaram dados operacionais, incluindo configuração, sessões, skills e logs.

Isso não prova que alguém externo já acessou, e eu não executei nenhuma ação mutante. Mas prova que a superfície pública está forte demais para permanecer como cockpit operacional sem autenticação/restrição adicional.

## Evidências read-only

### Página inicial

- `GET /`: HTTP 200
- Título: `Hermes Agent - Dashboard`
- HTML contém atribuição `window.__HERMES_SESSION_TOKEN__`.
- Token não foi salvo nem impresso; evidência registrada apenas como booleano e tamanho aproximado.
- Header de segurança observado: `cache-control: no-store, no-cache, must-revalidate`.
- Não foram observados, na amostra, headers como CSP, HSTS, X-Frame-Options, X-Content-Type-Options, Referrer-Policy ou Permissions-Policy.

### Documentação/API pública

- `GET /openapi.json`: HTTP 200 sem token.
- `GET /docs`: HTTP 200 sem token.
- `GET /redoc`: HTTP 200 sem token.
- O OpenAPI lista rotas operacionais, inclusive rotas mutantes como gateway restart/update. Não foram chamadas rotas mutantes.

### Endpoints testados sem token

- `GET /api/status`: HTTP 200, retorna JSON com versão, paths internos, estado de gateway e `auth_required=false`.
- `GET /api/health`: HTTP 401.
- `GET /api/config`: HTTP 401.
- `GET /api/sessions`: HTTP 401.
- `GET /api/skills`: HTTP 401.
- `GET /api/logs`: HTTP 401.

### Endpoints testados com token público injetado pela própria página

Token foi usado apenas para prova read-only de alcance da própria aplicação pública; não foi preservado.

- `GET /api/config`: HTTP 200, retorna configuração operacional sanitizada na inspeção.
- `GET /api/sessions`: HTTP 200, retorna lista volumosa de sessões e trechos de prompt/contexto.
- `GET /api/skills`: HTTP 200, retorna skills habilitadas.
- `GET /api/logs`: HTTP 200, retorna linhas de log com paths internos e erros.
- `GET /api/status`: HTTP 200.

### Container/Traefik read-only

- Container identificado: `hermes-agent-5ajw-hermes-agent-1`.
- Imagem: `hermes-agent-custom:v0.14.0-20260516-entrypointfix`.
- Serviço interno: porta `4860`.
- Porta host publicada: `0.0.0.0:33855` e `:::33855` para `4860/tcp`.
- Labels Traefik publicam `Host(hermes-agent-5ajw.srv1331756.hstgr.cloud)` em `websecure` com TLS letsencrypt.
- Env resumido sem segredos: `HERMES_HOME=/opt/data`, `HERMES_WEB_DIST=/opt/hermes/hermes_cli/web_dist`, `ADMIN_PASSWORD=<set>`.

## Classificação de risco

- Dashboard/UI pública: **Pública e operacional; risco A3 se permanecer exposta com token de página e endpoints sensíveis**.
- OpenAPI/docs: **Públicos; risco A2/A3 por revelar superfície operacional e rotas mutantes**.
- API interna default `8642`: não reclassificada neste receipt; F2-004 anterior classificou como host-local.
- Webhook default `8644`: não reclassificado neste receipt; F2-004 anterior classificou como público via Traefik/Cloudflare.
- Cockpit/plugin operacional: **bloqueado até mitigação ou isolamento**.

## Decisão recomendada

Não avançar o plugin/cockpit operacional neste dashboard público enquanto não houver uma das mitigações abaixo.

Opção recomendada P0:

1. Tirar o dashboard público da internet ou restringi-lo por Traefik/Cloudflare Access/VPN/Tailscale/allowlist.
2. Desabilitar `/docs`, `/redoc` e `/openapi.json` em produção pública ou protegê-los com autenticação real.
3. Remover token de sessão estático/injetado em HTML público; autenticação deve ser server-side ou via login forte, não bearer exposto na página.
4. Confirmar que endpoints mutantes exigem autenticação robusta e autorização por papel/escopo.
5. Reexecutar probes read-only: sem token público, `/api/config`, `/api/sessions`, `/api/logs`, `/api/skills` devem retornar 401/403; docs devem estar fechados ou autenticados.

## Approval packet para mitigação futura

Escopo que exigiria nova aprovação explícita de Lucas:

- Alterar Traefik/Cloudflare/Docker/compose/firewall/dashboard runtime.
- Reiniciar container/gateway/dashboard.
- Mudar variáveis de ambiente, `ADMIN_PASSWORD`, auth, docs/openapi, ou portas publicadas.

Rollback mínimo esperado:

- Backup do compose/env/labels antes da alteração.
- Plano para restaurar labels/porta pública anteriores.
- Verificação local e pública pós-mudança.
- Receipt Brain sanitizado.

## O que não foi feito

- Não foram chamados endpoints POST/PUT/PATCH/DELETE.
- Não foi usado brute force, scanner agressivo, fuzzing ou tentativa de bypass.
- Não foi impresso nem salvo token, API key, secret ou senha.
- Não houve alteração em Docker, Traefik, VPS, gateway, webhook, cron, providers, `.env` ou arquivos de config.

## Próximo passo recomendado

Abrir uma mitigação P0 separada para **fechar/proteger o dashboard público** antes de qualquer plugin/cockpit operacional. Até lá, tratar o dashboard como superfície sensível exposta e não como base segura para operação.
