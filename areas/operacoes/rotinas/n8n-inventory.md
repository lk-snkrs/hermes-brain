# Inventário n8n — lc.vps

Data da verificação: 2026-05-04.

## Objetivo

Verificar se existem workflows n8n ativos que funcionem como crons/rotinas de negócio para LK, Zipper, SPITI ou Hermes.

## Ambiente verificado

VPS: `lc.vps` / `72.60.150.124`.

Container:

| Container | Imagem | Status | Porta |
|---|---|---|---|
| `n8n-vdgm-n8n-1` | `docker.n8n.io/n8nio/n8n` | Up | container 5678, host 32769 |

Compose:

- `/docker/n8n-vdgm/docker-compose.yml`

Config segura observada:

- `NODE_ENV=production`
- `GENERIC_TIMEZONE=America/Sao_Paulo`
- `TZ=America/Sao_Paulo`
- `N8N_RUNNERS_ENABLED=true`
- `N8N_SECURE_COOKIE=false`
- `WEBHOOK_URL=https://n8n-vdgm.srv1331756.hstgr.cloud/`

## Método

1. API n8n read-only via `N8N_API_KEY`/`N8N_API_TOKEN` do Doppler, sem imprimir valores.
2. Consulta local read-only do SQLite do container, copiando temporariamente `database.sqlite` para `/tmp` na VPS e removendo após leitura.
3. Redação de padrões de secrets antes de registrar qualquer saída.

## Resultado API

Endpoint interno testado a partir da VPS:

```text
http://localhost:32769/api/v1/workflows?limit=250
```

Resultado:

- `workflow_count`: 0

## Resultado SQLite

Banco encontrado:

- `/home/node/.n8n/database.sqlite`
- tamanho observado: 585728 bytes

Tabela `workflow_entity` existe, mas está vazia:

- `workflow_count`: 0

Tabela `credentials_entity` existe, mas não foram listadas credenciais com valores. O inventário não expõe `data` de credenciais.

Tabela `execution_entity` existe, mas não retornou execuções recentes.

## Conclusão

No n8n da VPS `lc.vps`, não foram encontrados workflows n8n ativos nem arquivados no momento da coleta.

Portanto, as rotinas de negócio documentadas no Hermes Brain não estão implementadas neste n8n como workflows no ambiente verificado.

## Impacto no Brain

As seguintes rotinas continuam documentadas, mas sem execução n8n encontrada em `lc.vps`:

- LK full sync, morning briefing, cross-sell, RFM, outcomes, creative pipeline e FAQ.
- Zipper consulta de vendas, abordagem de colecionadores e planejamento de feiras.
- SPITI verificação de lances, alertas e relatórios.

## Próximas ações

1. Confirmar se existe outro n8n em outra VPS/domínio ou workspace.
2. Se houver workflows exportados fora deste container, importar apenas com revisão/approval.
3. Se Lucas quiser automação real, criar workflows de forma incremental, começando por rotinas read-only/Telegram preview.
4. Não criar/ativar workflows que enviem mensagens ou alterem dados sem aprovação explícita.

## Regra de comunicação

> n8n em `lc.vps` está rodando, mas sem workflows encontrados no banco/API durante a coleta de 2026-05-04.
