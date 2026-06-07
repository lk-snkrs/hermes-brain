# Threat Model — Dashboard v0.16 OIDC / Auth upgrade

Data: 2026-06-06
Card: `t_5a0bca56` — `[R3] Preparar threat model OIDC/Dashboard`
Status: análise documental aprovada; nenhuma alteração de Traefik, Docker, DNS, secrets, Dashboard, gateway ou auth feita
Owner: Hermes Geral / Infra
Fonte: `reports/governance/dashboard-v016-oidc-security-upgrade-approval-packet-2026-06-06.md`

## Ativo protegido

Dashboard Hermes recomendado para Lucas:

- `https://hermes.lucascimino.com`

Premissas documentais atuais:

- basic auth ativo;
- API principal não deve ficar pública;
- API local/host-local deve permanecer protegida;
- mudanças de auth/Traefik/Docker/secrets são sensíveis.

## Objetivo de segurança

Melhorar controle de acesso sem:

- bloquear Lucas;
- expor API bruta;
- vazar secrets;
- criar lockout;
- quebrar Dashboard/API local;
- fazer mudança irreversível sem rollback validado.

## Ameaças principais

### 1. Exposição indevida da API

Risco:

- rota do Dashboard ou proxy expõe endpoint de API não protegido.

Mitigação exigida:

- testar que endpoints sensíveis sem auth continuam bloqueados/protegidos;
- manter API bruta fora da superfície pública;
- separar Dashboard público de API local sempre que possível.

### 2. Lockout do Lucas

Risco:

- OIDC/callback/Traefik mal configurado impede login.

Mitigação exigida:

- manter basic auth funcional durante transição;
- testar login em janela controlada;
- rollback documentado e testado;
- não remover basic auth antes de fallback comprovado.

### 3. Vazamento de secrets

Risco:

- client secret, cookie secret, provider token ou env aparece em logs/artefatos.

Mitigação exigida:

- não imprimir secrets;
- backup sanitizado;
- secret scan de docs/receipts;
- logs revisados sem valores sensíveis.

### 4. Bypass por rota paralela

Risco:

- Traefik mantém rota antiga sem middleware forte.

Mitigação exigida:

- inventário de routers/middlewares antes;
- testar URL canônica e rotas alternativas;
- remover/fechar rotas antigas só após rollback validado.

### 5. Falha por dependência externa

Risco:

- provider OIDC fora, Cloudflare/SSO fora, DNS/callback quebrado.

Mitigação exigida:

- política de fallback;
- opção de acesso administrativo temporário seguro;
- manter basic auth ou túnel como escape até estabilizar.

## Comparação de opções

### A — Manter basic auth

Risco técnico imediato: baixo.

Bom quando:

- Dashboard está funcional;
- prioridade é estabilidade;
- não há exigência de MFA/SSO agora.

Limites:

- gestão de acesso menos granular;
- sem MFA nativo.

### B — OIDC/SSO via proxy

Risco técnico imediato: médio/alto.

Bom quando:

- Lucas quer SSO/MFA;
- há janela de manutenção;
- há rollback testado;
- provider e callback estão bem definidos.

Bloqueios antes de execução:

- escolher provider;
- definir callback URL;
- plano de secrets;
- backup de Traefik/compose/config;
- staging ou ativação paralela;
- health checks.

### C — Túnel/VPN/Tailscale

Risco de exposição pública: baixo.

Bom quando:

- segurança por rede é prioridade;
- Lucas aceita acesso um pouco menos conveniente.

Limites:

- pode piorar uso mobile/browser simples;
- adiciona dependência de cliente/túnel.

## Rollback mínimo para qualquer mudança futura

Antes de qualquer execução real:

1. backup de configs relevantes;
2. registrar estado atual de routers/middlewares;
3. confirmar basic auth atual funcionando;
4. aplicar mudança em paralelo quando possível;
5. testar Dashboard HTTPS;
6. testar endpoint sensível sem auth;
7. se falhar, restaurar basic auth/rota anterior;
8. testar login pós-rollback.

## Go / No-Go futuro

Go somente se:

- provider escolhido;
- secrets prontos sem exposição;
- janela aprovada;
- rollback claro;
- teste de lockout planejado;
- API pública bloqueada;
- Lucas aceita eventual breve indisponibilidade.

No-Go se:

- objetivo é só “melhorar por impulso”;
- basic auth atual atende;
- não há rollback testado;
- não há como validar API não exposta;
- qualquer secret precisar ser manuseado sem procedimento seguro.

## Recomendação

Manter basic auth por enquanto e só avançar para OIDC/SSO quando houver novo approval específico de execução. A próxima fase segura seria um mini-PRD de implementação com provider escolhido, rollback, janela e testes, ainda antes de mexer em Traefik/Docker/secrets.

## Resultado

Card `t_5a0bca56` pode ser considerado concluído no escopo aprovado: threat model documental criado, sem mudança de auth/infra/runtime.
