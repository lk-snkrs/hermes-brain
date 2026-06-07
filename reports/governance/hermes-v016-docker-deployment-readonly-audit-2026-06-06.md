# Hermes v0.16 — Auditoria read-only Docker/deployment

Data: 2026-06-06
Escopo: read-only/local/documental. Nenhum container, compose, Traefik, gateway ou porta foi alterado.

## Evidência coletada

### Runtime Hermes

- `Hermes Agent v0.16.0 (2026.6.5)`.
- Config version `27 ✓`.
- Gateway service: running, manager `docker (foreground)`.
- Scheduled jobs: `28 active`, `32 total` no momento do snapshot.
- Sessions: `7 active` no momento do snapshot.

### Dashboard público

Container: `hermes-dashboard-public`.

Achados:

- Estado: `running`.
- Usuário do container: `10000:10000`.
- Labels Traefik presentes:
  - router `hermes-dashboard-public`;
  - entrypoint `websecure`;
  - TLS via `letsencrypt`;
  - service port `9119`;
  - host rule `hermes.lucascimino.com`.
- `PortBindings`: `{}` no inspect do container, consistente com exposição via rede/Traefik em vez de publish direto.

Interpretação:

- Alinhado com direção v0.16 de containers non-root para superfície Dashboard.
- Mantém Dashboard como cockpit público protegido por auth, sem publicar API bruta por este container.

### Gateway principal Telegram/API

Container: `hermes-agent-5ajw-hermes-telegram-1`.

Achados read-only:

- Estado: `running`.
- Usuário do container: `root`.
- API server port `8642` publicado em host-local `127.0.0.1:8642`.
- Traefik labels para webhooks/Crisp apontam porta `8644`.
- StartedAt: `2026-06-06T14:15:08Z` no snapshot.

Interpretação:

- API local/host-local está alinhada com guardrail de não expor API bruta publicamente.
- O gateway ainda roda como `root`; isso pode ser legado/necessário pelo container principal, mas é candidato a investigação futura. Não alterar sem PRD/rollback.

### Container Hermes agent adicional

Container: `hermes-agent-5ajw-hermes-agent-1`.

Achados read-only:

- Estado: `running`.
- Usuário do container: `root`.
- Traefik label para host `hermes-agent-5ajw.srv1331756.hstgr.cloud` e porta `4860`.

Interpretação:

- Superfície de rede/Traefik existente deve ser tratada como infra sensível.
- Qualquer mudança aqui é A3/A4.

## Recomendações

### P0 — manter

- Não expor API bruta publicamente.
- Manter Dashboard protegido por auth.
- Manter qualquer mudança de Traefik/Docker/gateway sob approval packet.

### P1 — próxima auditoria read-only

- Mapear todos os containers Hermes com owner, função, porta, labels e usuário.
- Confirmar se containers root são necessários ou apenas legado.
- Confirmar se labels Hermes v0.16 podem ser adotadas em deploy futuro.
- Comparar compose atual com runtime vivo sem alterar arquivo.

### A3 — só com aprovação separada

- Migrar container principal para non-root.
- Alterar compose/imagem/labels/ports.
- Recriar containers.
- Mudar Traefik/OIDC/API exposure.
- Ativar cleanup/orphan reaper em produção.

## Decisão desta rodada

Nenhuma ação aplicada. A v0.16 sugere melhorias úteis de deployment, mas no nosso ambiente elas devem entrar como PRD de hardening futuro, não como mudança oportunista.
