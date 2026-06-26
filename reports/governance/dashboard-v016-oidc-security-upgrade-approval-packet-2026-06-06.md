# Approval Packet — Dashboard v0.16 OIDC / Security Upgrade

Data: 2026-06-06T16:40:25Z
Status: packet de decisão — nenhuma alteração de auth, Traefik, Docker, secrets ou Dashboard executada
Owner: Hermes Geral / Infra

## Decisão solicitada futuramente

Avaliar substituir ou complementar o basic auth atual do Dashboard por OIDC/SSO ou camada de autenticação mais robusta.

## Estado atual conhecido

- Dashboard público recomendado para Lucas: `https://hermes.lucascimino.com`.
- Basic auth está ativo.
- API principal não deve ser exposta sem controle; permanece host-local no desenho atual.
- Qualquer mudança de auth/Traefik/Docker/secrets é sensível.

## Objetivo do upgrade

Melhorar segurança e conforto de acesso ao Dashboard sem bloquear Lucas, sem expor API bruta e sem risco de lockout.

## Opções

### Opção A — Manter basic auth por enquanto

Prós:

- zero mudança;
- menor risco;
- já funciona.

Contras:

- gestão de usuário/senha menos granular;
- sem SSO/MFA nativo.

### Opção B — OIDC via proxy/authelia/cloudflare/access equivalente

Prós:

- SSO/MFA;
- controle mais granular;
- melhor postura de segurança.

Contras:

- mexe em Traefik/DNS/callback/secrets;
- risco de lockout;
- precisa rollback testado.

### Opção C — Dashboard só por túnel/VPN/Tailscale

Prós:

- reduz superfície pública;
- forte segurança por rede.

Contras:

- menos conveniente para Lucas;
- pode atrapalhar uso mobile/browser simples.

## Recomendação

Não mexer agora por impulso. Fazer um mini-PRD de segurança antes, com escolha explícita entre A/B/C.

Se Lucas quiser avançar, minha recomendação técnica é:

1. manter basic auth até o plano OIDC estar testado;
2. criar ambiente/staging ou janela controlada;
3. configurar OIDC em paralelo;
4. testar login e fallback;
5. só então cortar tráfego;
6. manter rollback para basic auth.

## Escopo bloqueado sem aprovação explícita

- editar Traefik labels/routes/middlewares;
- alterar containers/compose;
- trocar secrets;
- mexer em DNS;
- reiniciar gateway/dashboard;
- expor API server;
- remover basic auth antes de fallback comprovado.

## Plano de rollback exigido

- backup de config/compose/labels antes;
- manter basic auth funcional como fallback;
- comando de reversão documentado;
- health check Dashboard + API local;
- teste de login pós-rollback.

## Verificações necessárias se aprovado

- `GET /api/config` sem auth deve continuar bloqueado ou protegido;
- login Lucas funciona;
- sessão expira conforme política;
- logs não imprimem secrets;
- Dashboard segue acessível em HTTPS;
- API bruta não fica pública por acidente;
- rollback testado.

## Botões recomendados para decisão futura

- Aprovar mini-PRD OIDC/security sem mudanças runtime
- Manter basic auth por enquanto
- Quero túnel/VPN em vez de OIDC
- Ajustar escopo

## Status

Este arquivo é apenas o packet de decisão. Nenhuma mudança sensível foi feita.
