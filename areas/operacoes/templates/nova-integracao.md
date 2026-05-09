# Template — Nova integração Hermes Brain

Use este template antes de conectar ou documentar uma ferramenta nova.

## Identificação

- Integração:
- Negócio/área: Global / LK / Zipper / SPITI / Operações / Tecnologia / Governança
- Dono operacional:
- Data:
- Fonte de documentação:
- Repo/API/console:

## Problema que resolve

- Dor operacional:
- Frequência esperada:
- Quem usa:
- Resultado esperado:

## Decisão Hermes-native

- Isso precisa ser integração real, ou basta rotina manual/documentação?
- Hermes já resolve com tool existente, browser, terminal, API, skill ou cron?
- Há volume suficiente para automação?
- Decisão: aplicar / adaptar / deferir / rejeitar.

## Dados e permissões

- Dados lidos:
- Dados escritos:
- Dados pessoais/comerciais sensíveis:
- Ações external-send:
- Ações admin/destructive:

## Secrets

- Doppler project/config: `lc-keys/prd` ou outro
- Secret names necessários, sem valores:
  - `NOME_DO_SECRET`
- Escopo mínimo do token:
- Rotação/revogação:

## Níveis de permissão

### Read-only

O que pode fazer sem aprovação extra:

### Write

O que exige aprovação Lucas:

### External-send

Mensagens, campanhas, publicações, webhooks que impactam terceiros:

### Admin/destructive

Ações bloqueadas sem plano de backup/rollback:

## Fluxo operacional

1. Preparar ambiente read-only.
2. Validar autenticação sem imprimir secrets.
3. Executar teste mínimo sem mutação.
4. Documentar comandos/endpoints seguros.
5. Criar rotina em `areas/operacoes/rotinas/` se recorrente.
6. Criar skill só se o fluxo se repetir e tiver entrada/saída previsível.
7. Criar cron apenas depois de rotina manual validada.

## Guardrails por negócio

- LK: campanhas, WhatsApp, email e alteração de loja exigem preview + aprovação Lucas.
- Zipper: contato com colecionador, proposta, negociação ou publicação exige Lucas/Osmar/equipe responsável.
- SPITI: silêncio > dado errado; email é fonte principal para lances; ações externas exigem aprovação.
- Infra: Docker/VPS/Traefik/volumes/redes/DNS/firewall exigem aprovação + rollback.

## Verificação

- Health check:
- Secret scan:
- Teste read-only:
- Diff review:
- Aprovação necessária:

## Resultado

- Status: proposto / documentado / read-only validado / pronto para PR / bloqueado
- Próxima ação segura:
- Bloqueio real:
