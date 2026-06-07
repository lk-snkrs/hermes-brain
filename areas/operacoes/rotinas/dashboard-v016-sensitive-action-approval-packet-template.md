# Template — Approval Packet para ações sensíveis via Dashboard Hermes v0.16

Criado em: 2026-06-06
Uso: antes de qualquer ação sensível feita pelo Dashboard v0.16.

## Quando usar

Obrigatório antes de alterar pelo Dashboard:

- credentials/API keys/OAuth;
- webhooks/hook creation;
- channels/messaging platforms;
- MCP servers/tools com permissões fortes;
- gateway controls/restart/update;
- model default/fallback de perfis vivos;
- API pública/auth/OIDC;
- Docker/Traefik/infra;
- qualquer integração externa com write.

## Formato do packet

### 1. Decisão solicitada

- Ação proposta:
- Perfil/runtime afetado:
- Superfície: Dashboard / CLI / config / outro:
- Quem pediu:
- Urgência:

### 2. Escopo permitido

- Pode fazer:
  - ...
- Não pode fazer:
  - ...

### 3. Evidência read-only antes

- Estado atual:
- Config atual sem segredos:
- Runtime/processo/container afetado:
- Health atual:
- Artefatos/links relevantes:

### 4. Risco

Classificação:

- A0: local/read-only;
- A1: local/documental;
- A2: mudança local reversível;
- A3: runtime/integração sensível;
- A4: externo/produção/dinheiro/clientes/secrets.

Riscos específicos:

- Segurança:
- Disponibilidade:
- Dados/memória/sessões:
- Canais/Telegram/ruído:
- Empresa afetada:

### 5. Plano de execução

Passos exatos:

1. Backup/snapshot:
2. Aplicar mudança:
3. Readback:
4. Smoke test:
5. Registrar receipt:

### 6. Rollback

- O que restaurar:
- Comando/ação de rollback:
- Critério para acionar rollback:
- Como verificar rollback:

### 7. Verificação pós-ação

Mínimo:

- health/API/dashboard probe;
- processo/runtime correto;
- logs sem erro novo;
- Telegram sem wrapper/ruído;
- secret scan em receipt;
- Brain Health se docs forem tocados.

### 8. Botões/opções para Lucas

Quando a plataforma suportar inline buttons, apresentar como:

- Aprovar;
- Bloquear;
- Ajustar;
- Agendar depois.

Se não houver botões, aceitar resposta textual clara.

## Guardrail de linguagem

Mensagem para Lucas deve ser curta e humana:

```text
Decisão: [ação]
Impacto: [benefício]
Risco: [baixo/médio/alto]
Rollback: [sim/não, como]
Excluído: [o que NÃO será tocado]
Opções: Aprovar / Bloquear / Ajustar / Agendar
```

Não incluir:

- JSON bruto;
- job_id;
- preflight metadata;
- tokens ou segredos;
- logs extensos;
- comandos destrutivos sem contexto.

## Exemplo curto

```text
Decisão: habilitar MCP X no Dashboard para o profile Y.
Impacto: permitirá consultar Z em modo read-only.
Risco: médio, porque amplia ferramentas do profile.
Rollback: desabilitar MCP X e reiniciar só o profile Y, se necessário.
Excluído: credentials novas, webhooks, Docker, Traefik, writes externos.
Verificação: tool list, smoke read-only, logs, receipt e secret scan.
```

## Decisão desta rodada

Este arquivo é template/governança. Não autoriza nenhuma ação sensível por si só.
